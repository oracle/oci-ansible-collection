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

## How to enable `debug` mode

-  Set the `log_requests` variable in your ~/.oci/config to `True` to [enable Request logging in the OCI python SDK](https://github.com/oracle/oci-python-sdk/blob/master/docs/logging.rst)
-  Export an environment variable named `LOG_LEVEL` with the value `DEBUG` to enable DEBUG mode for the OCI Ansible modules
```sh
$ export LOG_LEVEL="DEBUG"
```

All subsequent debug messages from an Ansible playbook execution using the OCI Ansible Cloud Modules 
would go to `/tmp/oci_ansible_module.log` (the default logging location for the OCI Ansible modules).

OCI Ansible Cloud Modules uses standard Python logging facilities for logging.
Use the environment variable `LOG_PATH` to change the directory where the log file should be placed and `LOG_LEVEL` to change the log level. 
The default log level is `INFO`.
