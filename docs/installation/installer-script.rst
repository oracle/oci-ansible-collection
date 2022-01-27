Installer Script
----------------
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
