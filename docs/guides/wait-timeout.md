# OCI Ansible Collection - Wait Timeout

## Introduction

OCI Ansible Collection provides machanism to wait for operations to complete before timeout. Users can override this behaviour by using `wait` & `wait_timeout` parameters in playbook.

### `wait` parameter

    Description:        Whether to wait for operations to complete.
    Type:               Bool
    Default:            True

### `wait_timeout` parameter

    Description:        Time, in seconds, to wait for operations to complete when I(wait=yes).
                        Default timeout value for most of the services is 1200 seconds.
                        But, some services might have a longer wait timeout.
    Type:               Int
    Default:            1200 seconds

**Default wait timeout** for most of the services is **1200 seconds**. But, some services takes longer wait time. Following services are some examples where default wait timeout is different.

    waas:               2400 seconds
    analytics:          2000 seconds
    mysql:              2400 seconds
    bds:                4000 seconds
    database:           3600 seconds

## Customise wait behaviour

Users can override wait behavior by following ways:

### Using `wait_timeout` parameter

Users can use `wait_timeout` parameter in the task to override the default timeout value. Following is an example to override timeout value in playbook.

#### Example

```yaml
- name: Create new compute instance
  oci_compute_instance:
    name: "test_instance"
    image_id: ""ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx""
    shape: "VM.Standard2.1"
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    availability_domain: "Uocm:PHX-AD-1"
    create_vnic_details:
      hostname_label: "myinstance1"
      subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"
    wait_timeout: 2400
  register: result
```

In this case, operation will wait for 2400 seconds to complete instead of service's default timeout.

### Using `wait` parameter

Users can opt not to wait for the operation to complete by using `wait` parameter in playbooks. Below is an example to demonstrate this.

#### Example

```yaml
- name: Create an instance
  oci_compute_instance:
    name: "test_instance"
    image_id: ""ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx""
    shape: "VM.Standard2.1"
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    availability_domain: "Uocm:PHX-AD-1"
    create_vnic_details:
      hostname_label: "myinstance1"
      subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"
    wait: False
  register: result

- name: Create second instance
  oci_compute_instance:
    name: "test_instance_2"
    image_id: ""ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx""
    shape: "VM.Standard2.1"
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
    availability_domain: "Uocm:PHX-AD-1"
    create_vnic_details:
      hostname_label: "myinstance2"
      subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"
    wait: False
  register: result
```

In this example, playbook will not wait for operations to complete and it will move to next task.
