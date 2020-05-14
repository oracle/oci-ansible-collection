#!/usr/bin/env bash
set -e

WKSP="$(git rev-parse --show-toplevel)"
source "$WKSP"/scripts/common-vars.sh

cd "$WKSP"

# remove the tests and the scripts directory
ls -la
rm -rf "$COLLECTION_DIR"/tests
rm -rf "$WKSP"/scripts
rm -rf "$WKSP"/.dockerignore
rm -rf "$WKSP"/.gitignore
rm -rf "$WKSP"/.gitlab-ci.yml
rm -rf "$WKSP"/.idea
rm -rf "$WKSP"/.oci
rm "$WKSP"/tox.ini
ls -la

# remove the ansible_collections/oracle/oci directory structure to obtain
# the proper structure for final release
mv "$COLLECTION_DIR"/* "$WKSP"
rm -r "$WKSP"/ansible_collections
ls -la

# initialising the ssh-agent
eval `ssh-agent -s`
# reading the SSH_KEY from the Gitlab CI/CD Variables
echo "$COLLECTIONS_PRIVATE_KEY" | tr -d '\r' | ssh-add -

set +e
ssh -o StrictHostKeyChecking=no github.com
ssh -o StrictHostKeyChecking=no git@gitlab-odx.oracledx.com
set -e

# create a new branch for the PR
git fetch --unshallow
GITLAB_BRANCH_NAME=merge_to_github$(date +%Y-%m-%d-%H-%M-%S)
git checkout -b "$GITLAB_BRANCH_NAME"

# reset it to what look like the 'github' branch
ls -la

GIT_USER_EMAIL="ameya.lokre@oracle.com"
GIT_USER_NAME="Ameya Lokre"

# create a commit for this release
git config user.email "$GIT_USER_EMAIL"
git config user.name "$GIT_USER_NAME"

# changin the gitlab repo from HTTPS to SSH
git remote set-url origin "$GITLAB_COLLECTIONS_TARGET"

# --all will include file removals
git add --all .
git commit -m "Releasing version $COLLECTIONS_VERSION"
git push origin "$GITLAB_BRANCH_NAME" --force

echo "Branch $GITLAB_BRANCH_NAME is in desired state for github repo,
create a PR to merge to Gitlab $GITLAB_BRANCH_NAME branch"


# Merge Gitlab 'github' to public Github
# - STEP 3 IN RELEASE PROCESS
# - this script creates a remote branch on the GitHub repository with the
#   exact state of the gitlab $GITLAB_BRANCH_NAME branch
# - this should be executed *after* merge_from_gitlab_master
#   to release new internal changes to GitHub
# - This requires that a $GITHUB_COLLECTIONS_TARGET environment variable be set. This should be the
#   "Clone With SSH" string from the GitHub repo, for example:
#   git@github.com:oracle/oci-ansible-collections.git

[[ -z "$GIT_USER_EMAIL" ]] && { echo "GIT_USER_EMAIL is empty" ; exit 1; }
[[ -z "$GIT_USER_NAME" ]] && { echo "GIT_USER_NAME is empty" ; exit 1; }

# We should only have the files of mentioned in the github.whitelist file in this directory
ls -la

# this script requires that you have the ssh-agent
# build feature enabled with a key that has r/w access
# to the gitlab repository
#ls -la ~/.ssh
#cat ~/.ssh/config
#printf "\n\nHost * \n  StrictHostKeyChecking no\n" >> ~/.ssh/config
#cat ~/.ssh/config

# Create a $COLLECTIONS_NAME directory where we'll put in the clone from GitHub
cd "$WKSP"/..
mkdir "$COLLECTIONS_NAME"
cd "$COLLECTIONS_NAME"
git clone "$GITHUB_COLLECTIONS_TARGET" .
git fetch
git checkout master
git reset --hard origin/master
ls -la

# ensure we are on the $GITLAB_BRANCH_NAME branch in the ansible_collections_oci repo
cd "$WKSP"
ls -la
cat .git/config
git branch
git fetch
git checkout "$GITLAB_BRANCH_NAME"
cd ..

# add remote for gitlab
cd "$COLLECTIONS_NAME"
git remote add gitlab "$WKSP"
git fetch gitlab

git config user.email "$GIT_USER_EMAIL"
git config user.name "$GIT_USER_NAME"

# changin the github repo from HTTPS to SSH
git remote set-url origin "$GITHUB_COLLECTIONS_TARGET"

# create new branch, fast-forward merge from Bitbucket
RELEASE_BRANCH_NAME=release_"$COLLECTIONS_VERSION"_$(date +%Y-%m-%d)
git checkout -b "$RELEASE_BRANCH_NAME"
git merge --ff gitlab/"$GITLAB_BRANCH_NAME" --allow-unrelated-histories -m "Release version $COLLECTIONS_VERSION"

# push to Github, create PR from '$RELEASE_BRANCH_NAME' > 'master', merge (fast-forward) when approved
git push origin "$RELEASE_BRANCH_NAME"
