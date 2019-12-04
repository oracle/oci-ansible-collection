#!/bin/bash


# Pre-requisites:
#  cd "$WKSP/ansible"
#  pip install -r requirements.txt
#  cd test/runner/requirements
#  pip install -r integration.cloud.oci.txt -r units.txt -r sanity.txt -r ansible-test.txt -r integration.txt


# Runs a set of sanity, unit and other code validation checks
# Useful to run this before commit.

set -e # fail on non-zero exits

export ANSIBLE_NOCOWS=1 # no cowsay!

WKSP="$(git rev-parse --show-toplevel)/ansible"
cd "$WKSP"
source hacking/env-setup

# unit tests
echo "Run unit tests"
pytest -r a --cov=. --cov-report=term --fulltrace --color yes test/units/modules/cloud/oracle test/units/module_utils/oracle/ -vvv

# sanity validate-modules
# echo "Run sanity > validate-modules tests"
# ./test/sanity/validate-modules/validate-modules lib/ansible/modules/cloud/oracle/
# ./test/sanity/validate-modules/validate-modules --arg-spec --warnings  lib/ansible/modules/cloud/oracle
# ansible-test sanity --test pep8 lib/ansible/modules/cloud/oracle/*py lib/ansible/module_utils/oracle/oci*.py contrib/inventory/oci*.py
# ansible-test sanity --test pylint lib/ansible/modules/cloud/oracle/*py lib/ansible/module_utils/oracle/oci*.py contrib/inventory/oci*.py
# ansible-test sanity --test boilerplate lib/ansible/modules/cloud/oracle/*py lib/ansible/module_utils/oracle/oci*.py contrib/inventory/oci*.py
# ansible-test sanity --test shebang lib/ansible/modules/cloud/oracle/*py lib/ansible/module_utils/oracle/oci*.py contrib/inventory/oci*.py

# Run all the sanity tests that ansible runs
ansible-test sanity --color -v --junit ${COVERAGE:+"$COVERAGE"} ${CHANGED:+"$CHANGED"} --docker --docker-keep-git \
    --skip-test pylint --skip-test ansible-doc --skip-test docs-build --skip-test integration-aliases --skip-test botmeta \
    lib/ansible/modules/cloud/oracle/*py lib/ansible/module_utils/oracle/oci*.py \
    contrib/inventory/oci*.py lib/ansible/plugins/inventory/oci*.py \
    $(find test/integration/targets/oci* -type f \( -name '*.yaml' -o -name '*.yml' \) ) \
    test/units/modules/cloud/oracle/ test/units/module_utils/oracle/
ansible-test sanity --color -v --junit ${COVERAGE:+"$COVERAGE"} ${CHANGED:+"$CHANGED"} --docker --docker-keep-git \
    --test ansible-doc lib/ansible/modules/cloud/oracle/*py \
    lib/ansible/module_utils/oracle/oci*.py contrib/inventory/oci*.py lib/ansible/plugins/inventory/oci*.py \
    lib/ansible/plugins/doc_fragments/oracle*.py
ansible-test sanity --color -v --junit ${COVERAGE:+"$COVERAGE"} ${CHANGED:+"$CHANGED"} --docker --docker-keep-git \
    --test pylint --exclude test/units/ \
    contrib/inventory/oci*.py \
    lib/ansible/plugins/inventory/oci*.py \
    lib/ansible/plugins/doc_fragments/oracle*.py \
    lib/ansible/modules/cloud/oracle/*py \
    lib/ansible/module_utils/oracle/oci*.py
ansible-test sanity --color -v --junit ${COVERAGE:+"$COVERAGE"} ${CHANGED:+"$CHANGED"} --docker --docker-keep-git \
    --test pylint \
    test/units/modules/cloud/oracle/ \
    test/units/module_utils/oracle/

# flake8
flake8 --count test/units/module_utils/oracle/*py lib/ansible/module_utils/oracle/*py contrib/inventory/oci*.py
flake8 --count lib/ansible/modules/cloud/oracle/*py lib/ansible/module_utils/oracle/*py contrib/inventory/oci*.py

# copyright checks
cd ..
./scripts/copyright-check.sh $(git diff --name-only origin/master | grep 'ansible/lib/ansible/modules/cloud/oracle/.*py\|ansible/lib/ansible/module_utils/oracle/.*py\|ansible/contrib/inventory/oci.*py\|ansible/test/units/modules/cloud/oracle/test.*py\|^scripts/.*py')
./scripts/copyright-check.sh $(git diff --name-only origin/master | grep '^samples.*ya\?ml')

# ./scripts/ocid-check.sh ansible/lib/ansible/modules/cloud/oracle/*.py ansible/lib/ansible/module_utils/oracle/*.py ansible/contrib/inventory/oci*.py

# Black formatting checks
./scripts/test-black-formatted.sh

# ensure that we don't check in with a debug statement in it. Some of us use "q" for debugging. Check if there is an "imports q"
# in your staged changes.
# h/t: http://codeinthehole.com/tips/tips-for-using-a-git-pre-commit-hook/
PY_FILES_PATTERN="\.py"
FORBIDDEN='import q'
git diff --cached --name-only | \
    grep -E $PY_FILES_PATTERN | \
    GREP_COLOR='4;5;37;41' xargs grep --color --with-filename -n "$FORBIDDEN" && echo "Found $FORBIDDEN references. Please remove them before commiting" && exit 1
