## Installation Guides

To install `oci-ansible-collection` and related dependencies you can use the following methods

## Installation using installer script

Use the following command
`curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --verbose`
#### Ubuntu, Debian and other Linux distributions

On some Linux distributions, python-venv support is not there. The script installs the necessary dependencies which 
require `sudo` access. Ensure that the current user has `sudo` permissions before beginning to install the script.

###### Use the following command to get all the arguments that can be passed while installing using the installer script

`curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --help`

Currently we support following arguments:

```
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
```

### Installing the Collection with yum

You can use yum to install the Oracle Cloud Infrastructure Ansible Module Collection RPM.

The RPM also installs the required dependencies: the OCI SDK for Python and Ansible.

The following example shows how to use yum to install the Ansible Module Collection RPM:
  ``` bash
$ yum -y install oraclelinux-developer-release-el7 && sudo yum install oci-ansible-collection
  ```
Note:
This installation uses Python version 3.6.

To test the installation of the RPM and configuration of the SDK, you can run a sample playbook. For example:
  ``` bash
$ ansible-playbook-3 /usr/share/doc/oci-ansible-collection-<version>/samples/object_storage/get_namespace/sample.yaml
  ```

### Manual Installation Steps:
```
    sudo pip3 install virtualenv
    virtualenv venvansible
    source venvansible/bin/activate
    pip3 install oci
    pip3 install ansible
    ansible-galaxy collection install -f oracle.oci
```

To test the installation, you can run this sample:
```
venvansible/bin/ansible-playbook -vvv ~/.ansible/collections/ansible_collections/oracle/oci/samples/object_storage/get_namespace/sample.yaml
```

### How to troubleshoot installation errors?
#### Troubleshoot the error `oci python sdk required for this module`

You will get an error if Ansible runs using python2 and the python SDK is installed under python 3.<br/>
The above installation should run python from the virtual env path: `venvansible/bin/python`.<br/>
You should see this in the logs when running the playbook using -vvv flag:
`venvansible/bin/python /Users/.ansible/tmp/ansible-tmp/AnsiballZ_setup.py`<br/>
Make sure Ansible is not using `/usr/bin/python` when running:
`/usr/bin/python /Users/.ansible/tmp/ansible-tmp/AnsiballZ_setup.py`<br/>
Refer to Ansible python 3 support: https://docs.ansible.com/ansible/2.4/python_3_support.html

Note: Ansible only uses the current python environment if you are using the implicit localhost i.e if you use the 
host as localhost and do not define any host configuration. Else it goes through the interpreter discovery process 
'and picks the first one. It provides a configuration setting (both at system level and the host level) to 
explicitly set the python interpreter to use. <br/>
Please check https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html. Please set it 
to the environment (path to python executable) where OCI python SDK is installed and re-run the playbook.
 