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
Please refer to [Logging In OCI Ansible Module](https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/guides/logging-guide.html)
