# Frequently Asked Questions (FAQs)

## How to install the OCI Ansible Collection
Please refer the [Installation Guide](https://github.com/oracle/oci-ansible-collection/blob/master/InstallationGuide.md) on different ways to install the OCI Ansible Collection.

## How do I upgrade to the latest version
```
ansible-galaxy collection install -f oracle.oci
```

## How to find the version of the OCI Ansible Collection installed
The below command lists all the collections installed in your system and their versions. You can check the version for the entry `oracle.oci`
```
ansible-galaxy collection list
```
*Note: You need ansible >= 2.10 to run the above command*

## How to find the version of oci python sdk installed
You can run the below command:
```
python -c 'import oci; print(oci.__version__)'
```

## What are the dependencies for using OCI Ansible Collection
You need `ansible >= 2.9` and the latest version of `oci`.

-----------------------------------

## Logging in OCI Ansible Modules
OCI Ansible Cloud Modules uses standard Python logging facilities for logging. By default, logging will be disabled. Logging will be enabled based on verbosity levels of OCI Ansible Module or using environment variables. 
**Note: Logging using environment variables takes higher priority than using verbosity**


- By default, log level can be determined based on verbosity of OCI Ansible module. You can change the log level using environment variables. **Logging using environment variables takes higher priority than using verbosity**
  - Log level based on verbosity of OCI Ansible module
    - You can set verbosity for OCI Ansible modules or executing a playbook. On console, use -v flag while executing playbook or calling OCI Ansible modules using adhoc commands
    - If verbosity is 0(i.e. -v flag is not passed), then logging will be disabled
    - If verbosity is 1(i.e. -v can be passed), then log level will be `WARNING`
    - If verbosity is 2(i.e. -vv can be passed), then log level will be `INFO` 
    - If verbosity is 3 or higher(i.e. -vvv, -vvvv, etc. can be passed), then log level will be `DEBUG`. At this level, **request logging in OCI-Python-Sdk will be enabled**
  - Log level based on environment variable
    - Export environment variable named `OCI_ANSIBLE_LOG_LEVEL` or `LOG_LEVEL`. **`LOG_LEVEL` is deprecated. In next major release, we will be removing a support for `LOG_LEVEL` environment variable**
    ```sh
       $ export OCI_ANSIBLE_LOG_LEVEL="INFO/WARNING/DEBUG"
    ```
    - consider env_var = `OCI_ANSIBLE_LOG_LEVEL` or `LOG_LEVEL`. 
    - If env_var is not set, then log level will be determined based on verbosity of OCI Ansible module
    - If env_var="WARNING", then log level will be `WARNING`
    - If env_var="INFO", then log level will be `INFO`
    - If env_var="DEBUG", then log level will be `DEBUG`. At this level, **request logging in OCI-Python-Sdk will be enabled**

- By default, logs will be shown on Console together with result of OCI Ansible module. If you want to collect logs in a file, then please use environment variable and provide a directory where the log_file should be created. **Logging using environment variables takes higher priority than using verbosity**
  - Logs on Console
    - Logs will be collected in a list & will be shown in `oci_ansible_logs` key together with the result of OCI Ansible module
  - Logs in a File using environment variable
    - Export environment variable named `OCI_ANSIBLE_LOG_DIR` or `LOG_PATH`. **`LOG_PATH` is deprecated. In next major release, we will be removing a support for `LOG_PATH` environment variable**
    ```sh
       $ export OCI_ANSIBLE_LOG_DIR="path_to_the_directory"
    ```
    - If OCI_ANSIBLE_LOG_DIR is set, then `oci_ansible_module.log` file will be created in a directory and all the logs will be placed in that file. So you can access logs in `somepath_to_the_directory/oci_ansible_module.log`