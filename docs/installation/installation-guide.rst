



Installation Guide
~~~~~~~~~~~~~~~~~~~

This topic describes different installation methods in detail


Installation using installer script
------------------------------------
Run the following command to install the oci-ansible-collection and its dependencies.

.. code-block:: bash

    curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --verbose


.. Warning::
   On some Linux distributions, ``python-venv`` support is not there. The script installs the necessary dependencies which require ``sudo`` access. Ensure that the current user has sudo permissions before beginning to install the script.


You can also pass arguments to the script for a custom installation. To list all the supported arguments run the following command.

.. code-block:: bash

     curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --help
     
     # List of supported arguments

     --virtual-env-dir
        Users can use this flag to specify the location where the virtual environment is located or should be created
        if not already present. If this path already exists then it will be used else it will be created.

        default value: ~/lib

    --virtual-env-name
        Users can use this flag to specify the python virtual env name where
        python dependencies for oci-ansible-collections will be installed.
        This virtual env is created in the path sepcified in --virtual-env-dir flag else in the default folder path
        used by --virtual-env-dir flag.
        
        default value: oci-ansible-collection

    --ansible-version
        Users can specify particular version of ansible python package they want to install. Ex: 2.9
        To use the latest version dont't set this flag (recommended).
        This flag doesn't support upgrading the version in case user has already installed ansible 
        and wants to upgrade to a higher version.

        default value: latest version will be installed

    --oci-ansible-collection-path
        Users can use this flag to specify the location of collections where oci-ansible-collection 
        will be installed. Default path for this is determined by ansible-galaxy installer.

    --version
        Users can use this flag to specify the version of oci-ansible-collection will be installed.
        To use the latest version don't set any value(recommended). If not specified the latest 
        version will be used.
        Ex: 2.20.0

        Speciying --version along with --upgrade will result in a conflict
        Error will raised and installation will not continue.

        default value: latest version is picked
    
    --python-path
        Users can specify the specific python they want to use for installation.
        Note: minimum python version supported is python3.6

    --verbose
        Users can use this flag to enable more loggings in case of debugging purpose.
        Disabled by default.
        Ex: --verbose    will enable logging

    --dry-run
        Runs the script in dry run mode i.e no network calls during installation and installation of dependecies.
        Disabled by default.
        Ex: --dry-run    will enable the dry run mode
    
    --upgrade
        Users can specify this to upgrade the oci-ansible-collection and its required dependencies.
        This is will upgrade oci package and oci-ansible-collection to the latest one.
        Note: This will not upgrade ansible dependency to the latest version.

        Speciying --version along with --upgrade will result in a conflict
        Error will raised and installation will not continue.

    --help|-h
        Show help section
     




Installing using yum
---------------------

You can use yum to install the Oracle Cloud Infrastructure Ansible Module Collection RPM.

| The RPM also installs the required dependencies: the OCI SDK for Python and Ansible.

| The following example shows how to use yum to install the Ansible Module Collection RPM:


.. Note::
    This installation uses Python version 3.6.

.. code-block:: bash

    yum -y install oraclelinux-developer-release-el7 && sudo yum install oci-ansible-collection


To test the installation of the RPM and configuration of the SDK, you can run a sample playbook. For example:

.. code-block:: bash
    
    ansible-playbook-3 /usr/share/doc/oci-ansible-collection-<version>/samples/object_storage/get_namespace/sample.yaml


Manual
-------

.. code-block:: bash

    sudo pip3 install virtualenv
    virtualenv ociansible
    source ociansible/bin/activate
    pip3 install oci
    pip3 install ansible
    ansible-galaxy collection install -f oracle.oci


To test the installation, you can run this sample:

.. code-block:: bash
    
    venvansible/bin/ansible-playbook -vvv ~/.ansible/collections/ansible_collections/oracle/oci/samples/object_storage/get_namespace/sample.yaml