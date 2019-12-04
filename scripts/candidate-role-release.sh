#! /bin/bash
set -e

function generate_module_docs {
    export INSTALLDIR="/scratch/python-installs"
    export VENVDIR="/scratch/python-venvs"
    export LD_LIBRARY_PATH="$INSTALLDIR/lib:$LD_LIBRARY_PATH"
    source $VENVDIR/my-2.7-venv-$CI_COMMIT_REF_NAME/bin/activate
    cd ansible; source hacking/env-setup
    pip install -r docsite_requirements.txt
    MODULES="$(python -c 'import os,re; print(",".join({re.sub(r"\..*", "", f) for f in os.listdir("lib/ansible/modules/cloud/oracle")}))')" make webdocs
    deactivate
    cd ..
}

# Release a candidate OCI ansible role `tag` to the `oci-ansible-role`
# gitlab project
function release_oci_roles {
    ANSIBLE_MODULE_ROOT_DIR=${CI_PROJECT_DIR}/ansible/lib/ansible
    ANSIBLE_MODULE_SRC=${ANSIBLE_MODULE_ROOT_DIR}/modules/cloud/oracle
    ANSIBLE_MODULE_UTILS_SRC=${ANSIBLE_MODULE_ROOT_DIR}/module_utils/oracle
    ANSIBLE_MODULE_DOC_FRAGMENT=${ANSIBLE_MODULE_ROOT_DIR}/utils/module_docs_fragments
    ANSIBLE_MODULE_SCRIPTS=${CI_PROJECT_DIR}/scripts
    ANSIBLE_MODULE_INVENTORY_SCRIPT_DIR=${CI_PROJECT_DIR}/ansible/contrib/inventory
    OPEN_SOURCE_REPO_CONTENT=${CI_PROJECT_DIR}/scripts/open-source-repo

    # For now this script assumes that we are just using the tag in the internal
    # repo. If it would be different we must change the logic below.
    if [ -n "$(git status --porcelain)" ]; then
      # get tag description to push to stage repo
      description=$(git tag -l -n100 "${CI_COMMIT_TAG}")
      echo "description is ${description}"
      trimmed_description=$(echo -e "${description}" | tr -d '[:space:]')
      echo "trimmed description is $trimmed_description"
    fi

    generate_module_docs

    #This gitlab auth token is required to clone the `oci-ansible-role`
    #repository without any additional credentials
    API_TOKEN=3ywQiK1w8LczUzFjsxMa
    git clone https://oauth2:${API_TOKEN}@gitlab-odx.oracledx.com/oci/oci-ansible-role.git

    cd oci-ansible-role/
    ROLE_DIR=$(pwd)
    BRANCH_NAME=${CI_BUILD_TAG}_${CI_PIPELINE_ID}
    git checkout -b ${BRANCH_NAME}
    echo "Created release branch: $BRANCH_NAME"

    # create directories if they don't exist
    mkdir -p library module_utils module_docs_fragments meta inventory-script docs

    # XXX Initialize "meta" also through this script

    # Copy modules to library.
    rm -rf library/*
    cp -fv "$ANSIBLE_MODULE_SRC"/*.py ./library/

    # copy over module utils
    rm -rf module_utils/*
    cp -rv "$ANSIBLE_MODULE_UTILS_SRC" ./module_utils/

    # copy over module doc fragments
    rm -rf module_docs_fragments/*
    cp -fv "$ANSIBLE_MODULE_DOC_FRAGMENT"/oracle*.py ./module_docs_fragments/

    cp -f "$ANSIBLE_MODULE_SCRIPTS"/install.py .
    cp -f "$ANSIBLE_MODULE_SCRIPTS"/uninstall.py .

    # copy inventory script
    # The role directory structure allows modules to be embedded using a standard "library" directory
    # but there is no standard directory defined for inventory scripts. So using
    # a directory called "inventory-script"
    rm -rf inventory-script/*
    cp -fv "$ANSIBLE_MODULE_INVENTORY_SCRIPT_DIR"/oci_* ./inventory-script/

    rm -rf docs/*
    mkdir docs/modules
    cp -fRv "$OPEN_SOURCE_REPO_CONTENT"/docs/* docs/
    cp -fv ${CI_PROJECT_DIR}/ansible/docs/docsite/rst/oci_* docs/modules/
    cp -fv ${CI_PROJECT_DIR}/ansible/docs/docsite/rst/list_of_cloud_modules.rst docs/modules/

    # Add changes, commit to local repo, and push to origin
    commit_message="New release ${CI_COMMIT_TAG} Description: ${trimmed_description}"
    echo "commit message is $commit_message"

    echo "Committing changes that are part of the new tag into the stage repo"
    git add -A
    git commit -m "${commit_message}"
    git push origin "${BRANCH_NAME}":"${BRANCH_NAME}"

    TAG_NAME="${CI_COMMIT_TAG}_${CI_PIPELINE_ID}_candidate"
    echo "Push a new tag ${TAG_NAME} to the stage repo"
    tag_message="version: ${TAG_NAME} description:${description}"

    echo "tag_message is ${tag_message}"
    echo "TAG_NAME is $TAG_NAME"

    git tag -a "${TAG_NAME}" -m "${tag_message}"
    git push origin tag "${TAG_NAME}"

    cd "$ROLE_DIR"
    cd ..
    rm -rf oci-ansible-role/
}

release_oci_roles
