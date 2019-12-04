#! /bin/bash
set -e

function cleanup {
  cd "$TMPDIR"
  ./uninstall.py --debug
  deactivate
  cd "$VENVDIR"
  rm -rf "$VENV_NAME"
  cd /tmp/
  rm -rf "$TMPDIR"
}

# Release a candidate OCI Ansible role `tag` to the `oci-ansible-role-stage`
# gitlab project
function run_install_tests {
    PYEXEC='python2.7'
    VENV_NAME="install_tests_venv-${CI_BUILD_ID}"

    # create virtual env
    cd "$VENVDIR"
    echo "Creating virtualenv $VENV_NAME"
    virtualenv -p "$(which "$PYEXEC")" "$VENV_NAME"
    cd "$VENV_NAME"
    source bin/activate

    trap cleanup EXIT

    which python
    python --version
    which pip
    pip --version

    ANSIBLE_MODULE_ROOT_DIR=${CI_PROJECT_DIR}/ansible/lib/ansible
    ANSIBLE_MODULE_SRC=${ANSIBLE_MODULE_ROOT_DIR}/modules/cloud/oracle
    ANSIBLE_MODULE_UTILS_SRC=${ANSIBLE_MODULE_ROOT_DIR}/module_utils/oracle
    ANSIBLE_MODULE_DOC_FRAGMENT=${ANSIBLE_MODULE_ROOT_DIR}/plugins/doc_fragments
    ANSIBLE_MODULE_SCRIPTS=${CI_PROJECT_DIR}/scripts
    ANSIBLE_MODULE_SAMPLES=${CI_PROJECT_DIR}/samples
    ANSIBLE_MODULE_INVENTORY_SCRIPT_DIR=${CI_PROJECT_DIR}/ansible/contrib/inventory
    ANSIBLE_MODULE_INVENTORY_PLUGIN_DIR=${ANSIBLE_MODULE_ROOT_DIR}/plugins/inventory
    ANSIBLE_MODULE_UNIT_TESTS=${CI_PROJECT_DIR}/ansible/test/units/modules/cloud/oracle
    OPEN_SOURCE_REPO_CONTENT=${CI_PROJECT_DIR}/scripts/open-source-repo

    export TMPDIR=/tmp/${CI_BUILD_TAG}_${CI_PIPELINE_ID}
    echo "Creating tempdir $TMPDIR"
    mkdir -p $TMPDIR
    cd $TMPDIR

    # create directories if they don't exist
    mkdir -p samples library module_utils module_docs_fragments meta docs inventory-script inventory_plugins test/units .github

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

    # copy over inventory plugin
    rm -rf inventory_plugins/*
    cp -fv "$ANSIBLE_MODULE_INVENTORY_PLUGIN_DIR"/oci* ./inventory_plugins/

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

    # copy over unit tests
    rm -rf test/units/*
    cp -fRv "$ANSIBLE_MODULE_UNIT_TESTS"/* ./test/units/

    # Copy .github directory containing ISSUE_TEMPLATE.md
    rm -rf .github/*
    cp -fRv "$OPEN_SOURCE_REPO_CONTENT"/.github/* .github/

    # test with ansible min version
    pip install ansible==$MIN_ANSIBLE_RELEASE_SUPPORTED
    ./install.py --debug

    ansible-doc oci_volume > volume_documentation
    # Check for one of the options of oci_volume module in the documentation to assert ansible-doc works.
    if grep -q "source_details" volume_documentation;
     then
        cat volume_documentation
     else
        echo "ansible-doc failed."
        ansible-doc oci_volume
    fi

    rm volume_documentation

    pip uninstall -y ansible
    # test with latest ansible version
    pip install ansible

    ./install.py --debug
    # just to make sure that duplicate install works
    ./install.py --debug

    ansible-doc oci_volume > volume_documentation
    # Check for one of the options of oci_volume module in the documentation to assert ansible-doc works.
    if grep -q "source_details" volume_documentation;
     then
        cat volume_documentation
     else
        echo "ansible-doc failed."
        ansible-doc oci_volume
    fi

    rm volume_documentation

}

run_install_tests
