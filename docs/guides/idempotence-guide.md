## Idempotence in OCI Ansible Collection modules 

### Introduction

Most of the operations supported by OCI Ansible Collection are **idempotent** by design i.e we check whether it is necessary to perform the tasks in the playbook.

Consider a playbook which has task for creating a **compute instance**
```yaml
- name: Create instance
  oci_compute_instance:
    display_name: "instance_name"
    availability_domain: "Uocm:PHX-AD-1"
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
  shape: "VM.Standard2.1"
  source_details:
    source_type: "image"
    image_id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx"
  create_vnic_details:
    hostname_label: "insatncelabel"
    private_ip: "10.0.0.2"
    subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"
```

When this playbook is run for first time, it will create a compute instance resource in the compartment. Further reruns of the same playbook will be a no-op, resulting in 0 changes.

---

### How does idempotency work in OCI Ansible Collection
Whenever we execute a task, following steps occur:
- Fetch all the existing resources
- For each existing resource, we compare the input parameters of the task with the properties of that resource.
  - In case of complex input parameters, child parameters are also compared.
- If a resource is matched, we stop further comparison and don't perform the operation.
- If there is no match found, we perform the operation.

---
### Customising idempotence behaviour
By default all the input parameters, related to the resource, in the playbook task are compared.Users can override this behavior by following ways:

 - #### Using `key_by` parameter 
 
    The list of attributes of the resource which should be used to uniquely identify an instance of the resource. By default, all the input attributes provided for the resource in the task are used to uniquely identify a resource.

    ##### Example
    ```yaml
    - name: Create instance
      oci_compute_instance:
        display_name: "instance_name"
        availability_domain: "Uocm:PHX-AD-1"
        compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
        shape: "VM.Standard2.1"
        source_details:
            source_type: "image"
            image_id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx"
        create_vnic_details:
          hostname_label: "insatncelabel"
          private_ip: "10.0.0.2"
          subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"
        key_by: [compartment_id, availability_domain, display_name]
    ```

    We have passed an additional `key_by` parameter. In this case, we will only compare the attributes passed in the `key_by` parameter instead of comparing all the input attributes.
  
    We will compare the values for `compartment_id` , `availability_domain` and `display_name` with that for the existing resources (other attributes will be ignored for comparison).
    
    **Limitations:**
    - `key_by` is only applicable for `create` operations and not for `update` or `delete` operations.
    - Only top level attributes should be added to `key_by` parameter list. Any nested or child attribute will not be considered, if added in the list.
      Ex: `key_by: [compartment_id, availability_domain, source_type]`, `source_type` will be ignored as it is a child attribute of `source_details`
    

    **Note:**
    **We need to be careful while using `key_by` parameter. It is advised to pass a list of attributes which can uniquely identify a resource.**

---
 - #### Using `force_create` parameter

    Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn't create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with `key_by`.
  
    Users can pass this parameter to forcefully create the resource.This will skip all the idempotence checks and will perform the **create operation**.

    By default `force_create` is set as **False**.
    ##### Example
    ```yaml
    - name: Create instance
      oci_compute_instance:
        display_name: "instance_name"
        availability_domain: "Uocm:PHX-AD-1"
        compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
        shape: "VM.Standard2.1"
        source_details:
          source_type: "image"
          image_id: "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx"
        create_vnic_details:
          hostname_label: "insatncelabel"
          private_ip: "10.0.0.2"
          subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"
        force_create: True
    ```

    In this case as we have passed `force_create` as **True**, idempotence checks will be skipped while creating the resource.

---

### Non Idempotent Operations
There are few operations where idempotence is not supported by design. 
Following are some example(s) where idempotence is not supported:
-  operations involving restarting resource.

---
