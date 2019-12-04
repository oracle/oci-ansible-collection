#! /bin/bash
set -e

#Merge the candidate branch with master branch of the stage repo, and tag it, and push the tag and master branch changes to stage repo.
function push_oci_modules_to_stage_repo {

    #This gitlab auth token is required to clone the `oci-ansible-role`
    #repository without any additional credentials
    API_TOKEN=3ywQiK1w8LczUzFjsxMa
    STAGE_PROJECT_NAME="oci-ansible-role-stage"
    git clone https://oauth2:${API_TOKEN}@gitlab-odx.oracledx.com/oci/$STAGE_PROJECT_NAME.git
    TAG_NAME=${CI_COMMIT_TAG}_${CI_PIPELINE_ID}_candidate
    BRANCH_NAME=${CI_BUILD_TAG}_${CI_PIPELINE_ID}
    cd $STAGE_PROJECT_NAME
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
}

push_oci_modules_to_stage_repo
