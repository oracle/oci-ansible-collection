# Oracle Cloud Infrastructure Ansible Collection User Guide

The purpose of this document is to outline high level features and best practices that apply across a large set of our modules.

### Name as identifier
Instead of using the OCID to update resources, the resource name can be used now. Example:

```
    oci_compute_image:
      compartment_id: "{{ compartment_ocid }}"
      display_name: "MyCustomImage"
      operating_system: "Oracle Linux"
      operating_system_version: "7.4"
    environment:
      OCI_USE_NAME_AS_IDENTIFIER: 1
```
Resource name can also be used to delete resources, example:
```
    oci_compute_image:
      display_name: "MyCustomImage"
      state: absent
    environment:
      OCI_USE_NAME_AS_IDENTIFIER: 1
```

If you attempt to use `OCI_USE_NAME_AS_IDENTIFIER` and multiple resources are found with the same name, an error will be thrown because the module will not be able to determine which resource you intend to act upon.  Many OCI services / resources allow duplicate display names, so if you use this setting in Ansible it is up to you to ensure you don't introduce resources with duplicate display names.

### Check mode
Helps in checking if the create operation will create the resource or not. It will return changed status without executing the request. Example:
```
    oci_compute_image:
      compartment_id: "{{ compartment_ocid }}"
      display_name: "MyCustomImage"
    register: result
    check_mode: yes
```

### Identity Home Region Redirect
By default, Identity requests are redirected to the user home region even if you specify a different region. 
If you need to use Identity service with a region other than your home region, you can override this behavior by setting this variable to any value:
- Environment variable: OCI_IDENTITY_DO_NOT_REDIRECT_TO_HOME_REGION


### Avoiding reliance on server side default values
Before our modules execute any operation, they check with the service to determine if that operation is necessary or if the state is already such that the operation would be a no-op. For create operations, this means checking if a resource already exists that matches the parameters a user supplied. The modules will attempt to find a matching resource *only* based on the parameters you supply. This means that if you omit an optional parameter and rely on the server side default value, future invocations of the same playbook can potentially match a resource that has a different value for that parameter.

Here is a simple example to illustrate the potential affects of this behavior.
There are 2 volumes that exist in the user's tenancy, both named "MyVolume", one is 50 GB (the default) and one is 100 GB.

The user runs the following playbook:
```
oci_volume:
  display_name: "MyVolume"
  state: present
```

If there were no existing volumes in the tenancy, then a new volume would be created and the blockstorage service would default to a size of 50 GBs. Given that there *are* 2 existing volumes that match all other attributes in this play (display_name), the module may consider either the 50 GB "MyVolume" or the 100 GB "MyVolume" a match, and return that resource with changed = False. This is non-deterministic and therefore is probably not desirable for the user. In this case because the play only specifies the name and state = present, that is all that Ansible considers when trying to find a matching resource.

If the playbook looked instead like the following:
```
oci_volume:
  display_name: "MyVolume"
  size_in_gbs: 50
  state: present
```
There would be no ambiguity and it would only ever match the 50 GB block volume.

It is important to note that matching these extra fields only comes into play if *all* other fields match *and* you did not specify optional values with defaults.  Thus, this corner case can be avoided very easily by doing either of the following:
- Use unique attributes or tags for resources of the same type so there is no potential for ambiguity in matching resources
- Specify optional values that you care about instead of relying on server side defaults


### Passing json vars ot modules in Ansible 2.10
Please use the the keyword `to_json` in ansible version 2.10 for passing in json vars to the collections module. Find more about it in [official Ansible documentation](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#formatting-data-yaml-and-json)

For example, if a json input was expected for a module like this before:
```
oci_events_rule:
  display_name: "EventRule"
  condition: '{"eventType": "com.oraclecloud.databaseservice.autonomous.database.backup.end"}'
```

Please rewrite it to look like this:
```
oci_events_rule:
  display_name: "EventRule"
  condition: '{{ {"eventType": "com.oraclecloud.databaseservice.autonomous.database.backup.end"} | to_json }}'
```


## Additional Module parameters

### Support for `key_by` option
All modules support the key_by option. It takes a list of comma-separated attributes of the resource which should be used to uniquely identify the resource. By default, all the attributes of a resource are used to uniquely identify a resource.

### Force Create resources `force_create`
Ansible recommends that all the modules be idempotent, so that repeated playbook executions by users result in reaching the desired state quickly and reliably. 
Unless documented explicitly in the module's `ansible-doc`, all resource lifecycle operations initiated through OCI Ansible Modules are idempotent. 
To forcefully perform a non-idempotent creation of a resource, use the `force_create` option.

### Manage Waiting `wait`
All modules wait for the resource to be created/updated/deleted before returning. 
We provide two options in each module to control the waiting:
- `wait`: Whether to wait for create or delete operation to complete.
- `wait_timeout`: Time, in seconds, to wait when wait=yes. Defaults to 1200 for most of the services but some services might have a longer wait timeout.