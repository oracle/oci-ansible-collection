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

# Release a candidate OCI Ansible role `tag` to the `oci-ansible-role-stage`
# gitlab project
function release_candidate_oci_role {
    ANSIBLE_MODULE_ROOT_DIR=${CI_PROJECT_DIR}/ansible/lib/ansible
    ANSIBLE_MODULE_SRC=${ANSIBLE_MODULE_ROOT_DIR}/modules/cloud/oracle
    ANSIBLE_MODULE_UTILS_SRC=${ANSIBLE_MODULE_ROOT_DIR}/module_utils/oracle
    ANSIBLE_MODULE_DOC_FRAGMENT=${ANSIBLE_MODULE_ROOT_DIR}/utils/module_docs_fragments
    ANSIBLE_MODULE_SCRIPTS=${CI_PROJECT_DIR}/scripts
    ANSIBLE_MODULE_SAMPLES=${CI_PROJECT_DIR}/samples
    ANSIBLE_MODULE_INVENTORY_SCRIPT_DIR=${CI_PROJECT_DIR}/ansible/contrib/inventory
    ANSIBLE_MODULE_UNIT_TESTS=${CI_PROJECT_DIR}/ansible/test/units/modules/cloud/oracle
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

    #This gitlab auth token is required to clone the `oci-ansible-role-stage`
    #repository without any additional credentials
    API_TOKEN=3ywQiK1w8LczUzFjsxMa
    STAGE_PROJECT_NAME="oci-ansible-role-stage"
    git clone https://oauth2:${API_TOKEN}@gitlab-odx.oracledx.com/oci/$STAGE_PROJECT_NAME.git
    cd "$STAGE_PROJECT_NAME"
    ROLE_DIR=$(pwd)
    BRANCH_NAME=${CI_BUILD_TAG}_${CI_PIPELINE_ID}
    git checkout -b "${BRANCH_NAME}"
    echo "Created release branch: $BRANCH_NAME"

    # create directories if they don't exist
    mkdir -p samples library module_utils module_docs_fragments meta docs inventory-script test/units .github

    # copy over module sources
    rm -rf library/*
    cp -fv "$ANSIBLE_MODULE_SRC"/*.py ./library/

    # copy over module utils
    rm -rf module_utils/*
    cp -rv "$ANSIBLE_MODULE_UTILS_SRC" ./module_utils/

    # copy over module doc fragments
    rm -rf module_docs_fragments/*
    cp -fv "$ANSIBLE_MODULE_DOC_FRAGMENT"/oracle*.py ./module_docs_fragments/

    # copy over installer and uninstaller scripts

    cp -fv "$ANSIBLE_MODULE_SCRIPTS"/install.py .
    cp -fv "$ANSIBLE_MODULE_SCRIPTS"/uninstall.py .

    # copy over inventory script
    # The role directory structure allows modules to be embedded using a standard "library" directory
    # but there is no standard directory defined for inventory scripts. So using
    # a directory called "inventory-script"
    rm -rf inventory-script/*
    cp -fv "$ANSIBLE_MODULE_INVENTORY_SCRIPT_DIR"/oci_* ./inventory-script/

    # copy over samples
    rm -rf samples/*
    cp -fRv "$ANSIBLE_MODULE_SAMPLES"/* ./samples/

    # copy meta
    rm -rf meta/*
    cp -fv "$OPEN_SOURCE_REPO_CONTENT"/meta-main.yml meta/main.yml

    # copy over documentation
    cp -fv "$OPEN_SOURCE_REPO_CONTENT"/ogho-README.md README.md
    cp -fv "$OPEN_SOURCE_REPO_CONTENT"/LICENSE.txt LICENSE.txt
    cp -fv "$OPEN_SOURCE_REPO_CONTENT"/CONTRIBUTING.md CONTRIBUTING.md
    cp -fv "$OPEN_SOURCE_REPO_CONTENT"/CHANGELOG.md CHANGELOG.md
    cp -fv "$OPEN_SOURCE_REPO_CONTENT"/THIRD_PARTY_LICENSES.txt THIRD_PARTY_LICENSES.txt
    rm -rf docs/*
    mkdir docs/modules
    cp -fRv "$OPEN_SOURCE_REPO_CONTENT"/docs/* docs/
    cp -fv "${CI_PROJECT_DIR}"/ansible/docs/docsite/rst/modules/oci_* docs/modules/
    cp -fv "${CI_PROJECT_DIR}"/ansible/docs/docsite/rst/modules/list_of_cloud_modules.rst docs/modules/

    # copy over unit tests
    rm -rf test/units/*
    cp -fRv "$ANSIBLE_MODULE_UNIT_TESTS"/* ./test/units/

    # Copy .github directory containing ISSUE_TEMPLATE.md
    rm -rf .github/*
    cp -fRv "$OPEN_SOURCE_REPO_CONTENT"/.github/* .github/

    # Add changes, commit to local repo, and push to origin
    commit_message="New release: ${CI_COMMIT_TAG} Description: ${trimmed_description}"
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
    rm -rf oci-ansible-role-stage/
}

release_candidate_oci_role
