#! /bin/bash
set -e

. "$CI_PROJECT_DIR"/scripts/common-vars.sh
. "$CI_PROJECT_DIR"/scripts/run-integration-tests-common.sh

# push the role archive to the webserver
function push_role_to_webserver {
    # activate 2.7 virtual env
    source "$VENVDIR"/my-2.7-venv-"$CI_COMMIT_REF_NAME"/bin/activate

    pip install oci
    pip install ansible

    ansible --version

    # push role to webserver
    cd "$CI_PROJECT_DIR"
    echo "Role archive being published is $1"
    ansible-playbook --extra-vars "role_archive=$1" ./scripts/roles-and-docs-webserver/publish_role.yml

    deactivate
}

# Merge the candidate branch with master branch of the oci-ansible-role repo, and tag it, and push the tag and master branch changes to the repo.
function release_oci_roles {
    #This gitlab auth token is required to clone the `oci-ansible-role`
    #repository without any additional credentials
    API_TOKEN=3ywQiK1w8LczUzFjsxMa
    git clone https://oauth2:${API_TOKEN}@gitlab-odx.oracledx.com/oci/oci-ansible-role.git
    TAG_NAME=${CI_COMMIT_TAG}_${CI_PIPELINE_ID}_candidate
    BRANCH_NAME=${CI_BUILD_TAG}_${CI_PIPELINE_ID}
    cd oci-ansible-role/

    git merge --ff-only origin/$BRANCH_NAME
    git push origin master

    description=$(git tag -l -n100 "${TAG_NAME}")
    echo "description is ${description}"

    git push --delete origin $TAG_NAME
    git tag --delete $TAG_NAME
    git push origin --delete $BRANCH_NAME
    echo "Push a new tag ${CI_COMMIT_TAG} to the stage repo"
    tag_message="Version: ${CI_COMMIT_TAG} Description: ${description}"
    TAG_NAME="${CI_COMMIT_TAG}"
    echo "tag_message is $tag_message"
    echo "TAG_NAME is $TAG_NAME"

    git tag -a "${TAG_NAME}" -m "${tag_message}"
    git push origin tag "${TAG_NAME}"

    # create the role archive for publishing
    rm -rf .git
    cd ..
    ROLE_ARCHIVE="$(pwd)/oci-ansible-role.tar.gz"
    tar -zcvf $ROLE_ARCHIVE oci-ansible-role
    echo "ROLE_ARCHIVE is $ROLE_ARCHIVE"
    push_role_to_webserver $ROLE_ARCHIVE
}

release_oci_roles

