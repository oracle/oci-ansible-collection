#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_instance
short_description: Launch, terminate and control the lifecycle of OCI Compute instances
description:
    - This module allows the user to launch/create, terminate and perform other power actions on OCI Compute Service
      instances. An instance represents a compute host. The image used to launch the instance determines its operating
      system and other software. The shape specified during the launch process determines the number of CPUs and memory
      allocated to the instance. For more information, see Overview of the Compute Service at
      U(https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Concepts/computeoverview.htm). In experimental mode,
      this module also allows attaching/detaching volumes and boot volumes to an instance.
version_added: "2.5"
options:
    availability_domain:
        description: The Availability Domain of the instance. Required when creating a compute instance with
                     I(state=present).
    boot_volume_details:
        description: Details for attaching/detaching a boot volume to/from an instance. I(boot_volume_details) is
                     mutually exclusive with I(image_id). This option is only supported in experimental mode. To use
                     an experimental feature, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.
        suboptions:
            attachment_state:
                description: Attach a boot volume to the instance I(instance_id) with I(attachment_state=present).
                             Detach a boot volume from the instance I(instance_id) with I(attachment_state=absent).
                default: present
                choices: ['present', 'absent']
            boot_volume_id:
                description: The OCID of the boot volume.
                required: true
    compartment_id:
        description: The OCID of the compartment. Required when I(state=present).
    extended_metadata:
        description: Additional metadata key/value pairs that you provide. They serve a similar purpose and
                     functionality from fields in the I(metadata) object. They are distinguished from I(metadata)
                     fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps
                     only).
                     If you don't need nested metadata values, it is strongly advised to avoid using this object and
                     use the Metadata object instead.
    fault_domain:
        description: A fault domain is a grouping of hardware and infrastructure within an availability domain. Each
                     availability domain contains three fault domains. Fault domains let you distribute your instances
                     so that they are not on the same physical hardware within a single availability domain. A hardware
                     failure or Compute hardware maintenance that affects one fault domain does not affect instances in
                     other fault domains. If you do not specify the fault domain, the system selects one for you. To
                     change the fault domain for an instance, terminate it and launch a new instance in the preferred
                     fault domain. To get a list of fault domains, use M(oci_fault_domain_facts).
    metadata:
        description: A hash/dictionary of custom key/value pairs that are associated with the instance. This
                     option is also used to provide information to cloud-init and specifying
                     "ssh_authorized_keys" for the default user of the instance. This hash is specified
                     as '{"key":"value"}' and '{"key":"value","key":"value"}'.
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information.
        aliases: ['name']
    image_id:
        description: The OCID of the image used to boot the instance. I(image_id) is mutually exclusive with
                     I(boot_volume_details) and I(source_details). This option is deprecated. Use I(source_details)
                     with I(source_type=image) instead.
    instance_id:
        description: The OCID of the compute instance. Required for updating an existing compute instance
                     when I(state=present), for performing power actions (such as start, stop, softreset
                     or reset) on an instance, and for terminating an instance I(state=absent).
        aliases: [ 'id' ]
    ipxe_script:
        description: custom iPXE script that will run when the instance boots.
    preserve_boot_volume:
        description: Whether to preserve the boot volume when terminating an instance with I(state=absent).
        default: False
        type: bool
    shape:
        description: The shape of the instance. Required when creating a compute instance with I(state=present).
    source_details:
        description: Details for creating an instance. Use this parameter to specify whether a boot volume or an image
                     should be used to launch a new instance.
        required: true
        suboptions:
            source_type:
                description: The source type for the instance. Use image when specifying the image OCID. Use bootVolume
                             when specifying the boot volume OCID.
                required: true
                choices: ['image', 'bootVolume']
            image_id:
                description: The OCID of the image used to boot the instance. Required if I(source_type) is "image".
            boot_volume_size_in_gbs:
                description: The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is
                             16384 GB (16TB). Applicable only when I(source_type=image).
            boot_volume_id:
                description: The OCID of the boot volume used to boot the instance. Required if I(source_type) is
                             "bootVolume".
    state:
        description: The state of the instance that must be asserted to. When I(state=present), and the
                     compute instance doesn't exist, the instance is launched/created with the specified
                     details. When I(state=absent), the compute instance is terminated. When
                     I(state=stopped), the compute instance is powered off. When I(state=running), the
                     compute instance is powered on. When I(state=softreset), an ACPI shutdown is
                     initiated and the compute instance is powered on. When I(state=reset), the
                     compute instance is powered off and then powered on.
                     Note that I(state=softreset) and I(state=reset) states are not idempotent. Every time a play is
                     executed with these C(state) options, a shutdown and a power on sequence is executed against the
                     instance.
        default: "present"
        choices: ['present', 'absent', 'running', 'reset', 'softreset', 'stopped']
    volume_details:
        description: Details for attaching or detaching a volume to an instance with I(state=present) or
                     I(state=RUNNING). This option is only supported in experimental mode. To use an experimental
                     feature, set the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.
        suboptions:
            attachment_state:
                description: Attach a volume to the instance I(instance_id) with I(attachment_state=present). Detach a
                             volume from the instance I(instance_id) with I(attachment_state=absent).
                default: present
                choices: ['present', 'absent']
            attachment_name:
                description: A user-friendly name. Does not have to be unique, and it cannot be changed. Avoid entering
                             confidential information.
            type:
                description: The type of volume. The only supported value is "iscsi".
                default: iscsi
                choices: ['iscsi']
            volume_id:
                description: The OCID of the volume to be attached to or detached from the instance I(instance_id).
    vnic:
        description: Details for the primary VNIC that is automatically created and attached when the instance is
                     launched. Required when creating a compute instance with I(state=present).
        aliases: ['create_vnic_details']
        suboptions:
            assign_public_ip:
                description: Determines whether the VNIC should be assigned a public IP address.  If
                             not set and the VNIC is being created in a private subnet (that is,
                             where I(prohibitPublicIpOnVnic = true) in the Subnet), then no public
                             IP address is assigned. If not set and the subnet is public
                             I(prohibitPublicIpOnVnic = false), then a public IP address is
                             assigned. If set to true and I(prohibitPublicIpOnVnic = true),
                             an error is returned.
            hostname_label:
                description: The hostname for the VNIC's primary private IP. Used for DNS. The value
                             is the hostname portion of the primary private IP's fully qualified
                             domain name (FQDN) (for example, bminstance-1 in FQDN
                             bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all
                             VNICs in the subnet and comply with RFC 952 and RFC 1123.
            name:
                description: A user-friendly name for the VNIC. Does not have to be unique.
            private_ip:
                description: The private IP to assign to the VNIC. Must be an available IP address
                             within the subnet's CIDR. If you don't specify a value, Oracle
                             automatically assigns a private IP address from the subnet. This is
                             the VNIC's primary private IP address.
            skip_source_dest_check:
                description: Determines whether the source/destination check is disabled on the VNIC.
                             Defaults to false, which means the check is performed.
                default: false
            subnet_id:
                description: The OCID of the subnet to create the VNIC in.
                required: true

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Launch/create an instance using an image, with custom metadata and a private IP assignment
  oci_instance:
     name: myinstance1
     availability_domain: "BnQb:PHX-AD-1"
     compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
     shape: "BM.Standard1.36"
     metadata:
        foo: bar
        baz: quux
     source_details:
        source_type: image
        image_id: ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx
     volume_details:
        attachment_state: present
        volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
     vnic:
        hostname_label: "myinstance1"
        private_ip: "10.0.0.5"
        subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"

- name: Launch/create an instance using a boot volume, a private IP assignment and attach a volume, and a specific
        fault domain
  oci_instance:
     name: myinstance2
     availability_domain: "BnQb:PHX-AD-1"
     fault_domain: "FAULT-DOMAIN-2"
     source_details:
        source_type: bootVolume
        boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
     compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
     shape: "BM.Standard1.36"
     volume_details:
        attachment_state: present
        volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
     vnic:
        hostname_label: "myinstance2"
        private_ip: "10.0.0.6"
        subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"

- name: Launch/create an instance using an image with custom boot volume size
  oci_instance:
     name: myinstance1
     availability_domain: "BnQb:PHX-AD-1"
     compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq"
     shape: "BM.Standard1.36"
     source_details:
        source_type: image
        image_id: ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx
        boot_volume_size_in_gbs: 100
     vnic:
        hostname_label: "myinstance1"
        subnet_id: "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa"

- name: Update an instance's name
  oci_instance:
     name: myinstance1-new-name
     id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"

- name: Detach a volume from an instance
  oci_instance:
     id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
     volume_details:
        attachment_state: absent
        volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx

- name: Stop an instance
  oci_instance:
     id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
     state: "stopped"

- name: Stop an instance and detach boot volume
  oci_instance:
     id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
     state: "stopped"
     boot_volume_details:
        boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
        attachment_state: absent

- name: Attach a boot volume & Start an instance
  oci_instance:
     id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
     state: "running"
     boot_volume_details:
        boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx

- name: Reset an instance
  oci_instance:
     id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
     state: "reset"

- name: Terminate/delete an instance
  oci_instance:
     id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
     state: "absent"

- name: Terminate/delete an instance and preserve boot volume
  oci_instance:
     id: "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx...lxiggdq"
     state: "absent"
     preserve_boot_volume: yes
"""

RETURN = """
instance:
    description: Details of the OCI compute instance launched, updated or terminated as a result of the current operation
    returned: On successful operation (create, update and terminate) on a single Compute instance
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain the instance is running in.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        boot_volume_attachment:
            description: Information of the boot volume attachment.
            returned: In experimental mode.
            type: dict
            contains:
                availability_domain:
                    description: The Availability Domain of the instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                boot_volume_id:
                    description: The OCID of the boot volume.
                    returned: always
                    type: string
                    sample: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My boot volume attachment
                id:
                    description: The OCID of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the boot volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                lifecycle_state:
                    description: The current state of the boot volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                time_created:
                    description: The date and time the boot volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
        compartment_id:
            description: The OCID of the compartment that contains the instance.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx....62xq
        display_name:
            description: A user-friendly name for the instance
            returned: always
            type: string
            sample: ansible-instance-968
        extended_metadata:
            description: Additional key-value pairs associated with the instance
            returned: always
            type: dict(str, str)
            sample: {'foo': 'bar'}
        fault_domain:
            description: The name of the fault domain the instance is running in. A fault domain is a grouping of
                         hardware and infrastructure within an availability domain. Each availability domain contains
                         three fault domains. Fault domains let you distribute your instances so that they are not on
                         the same physical hardware within a single availability domain. A hardware failure or Compute
                         hardware maintenance that affects one fault domain does not affect instances in other fault
                         domains. If you do not specify the fault domain, the system selects one for you. To change the
                         fault domain for an instance, terminate it and launch a new instance in the preferred fault
                         domain.
            returned: always
            type: string
            sample: "FAULT-DOMAIN-1"
        id:
            description: The OCID of the instance.
            returned: always
            type: string
            sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
        image_id:
            description: The OCID of the image that the instance is based on
            returned: always
            type: string
            sample: ocid1.image.oc1.iad.xxxxxEXAMPLExxxxx
        ipxe_script:
            description: A custom iPXE script that will run when the instance boots
            returned: always
            type: string
            sample: null
        lifecycle_state:
            description: The current state of the instance.
            returned: always
            type: string
            sample: TERMINATED
        metadata:
            description: Custom metadata that was associated with the instance
            returned: always
            type: dict(str, str)
            sample: {"foo": "bar"}
        region:
            description: The region that contains the Availability Domain the instance is running in.
            returned: always
            type: string
            sample: phx
        shape:
            description: The shape of the instance. The shape determines the number of CPUs and the amount of memory
                         allocated to the instance.
            returned: always
            type: string
            sample: BM.Standard1.36
        time_created:
            description: The date and time the instance was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00
        volume_attachments:
            description: List of information about volume attachments
            returned: In experimental mode.
            type: complex
            contains:
                attachment_type:
                    description: The type of volume attachment.
                    returned: always
                    type: string
                    sample: iscsi
                availability_domain:
                    description: The Availability Domain of an instance.
                    returned: always
                    type: string
                    sample: BnQb:PHX-AD-1
                chap_secret:
                    description: The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP
                         user name. (Also called the "CHAP password".)
                    returned: always
                    type: string
                    sample: d6866c0d-298b-48ba-95af-309b4faux45e
                chap_username:
                    description: The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: always
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: always
                    type: string
                    sample: My volume attachment
                id:
                    description: The OCID of the volume attachment.
                    returned: always
                    type: string
                    sample: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the volume is attached to.
                    returned: always
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                ipv4:
                    description: The volume's iSCSI IP address.
                    returned: always
                    type: string
                    sample: 169.254.0.2
                iqn:
                    description: The target volume's iSCSI Qualified Name in the format defined by RFC 3720.
                    returned: always
                    type: string
                    sample: iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9
                lifecycle_state:
                    description: The current state of the volume attachment.
                    returned: always
                    type: string
                    sample: ATTACHED
                port:
                    description: The volume's iSCSI port.
                    returned: always
                    type: int
                    sample: 3260
                time_created:
                    description: The date and time the volume was created, in the format defined by RFC3339.
                    returned: always
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                volume_id:
                    description: The OCID of the volume.
                    returned: always
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx

    sample: [{"availability_domain": "BnQb:PHX-AD-1",
              "boot_volume_attachment": {
                                          "availability_domain": "IwGV:US-ASHBURN-AD-1",
                                          "boot_volume_id": "ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx",
                                          "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                                          "display_name": "Remote boot attachment for instance",
                                          "id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                                          "instance_id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                                          "lifecycle_state": "ATTACHED",
                                          "time_created": "2018-01-15T07:23:10.838000+00:00"
              },
             "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq",
             "display_name": "ansible-test-968",
             "extended_metadata": {},
             "fault_domain": "FAULT-DOMAIN-1",
             "id": "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx....lxiggdq",
             "image_id": "ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx....7klnoa",
             "ipxe_script": null,
             "lifecycle_state": "RUNNING",
             "metadata": {"baz": "quux", "foo": "bar"},
             "region": "phx",
             "shape": "BM.Standard1.36",
             "time_created": "2017-11-14T16:09:07.557000+00:00",
             "volume_attachments":  [{
                                    "attachment_type": "iscsi",
                                    "availability_domain": "BnQb:PHX-AD-1",
                                    "chap_secret": null,
                                    "chap_username": null,
                                    "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                                    "display_name": "ansible_volume_attachment",
                                    "id": "ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx",
                                    "instance_id": "ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx",
                                    "ipv4": "169.254.2.2",
                                    "iqn": "iqn.2015-12.com.oracleiaas:472a085d-41a9-4c18-ae7d-dea5b296dad3",
                                    "lifecycle_state": "ATTACHED",
                                    "port": 3260,
                                    "time_created": "2017-11-23T11:17:50.139000+00:00",
                                    "volume_id": "ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx"
                                  }]
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_compute_utils
from ansible.module_utils.oracle.oci_utils import check_mode

from ansible.module_utils import six

try:
    import oci
    from oci.core.compute_client import ComputeClient
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import AttachBootVolumeDetails
    from oci.core.models import AttachVolumeDetails
    from oci.core.models import LaunchInstanceDetails
    from oci.core.models import UpdateInstanceDetails
    from oci.core.models import CreateVnicDetails
    from oci.core.models import InstanceSourceViaBootVolumeDetails
    from oci.core.models import InstanceSourceViaImageDetails
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "instance"


def detach_volume(compute_client, module, volume_attachment_id):
    result = dict()
    result["changed"] = False

    try:
        volume_attachment = oci_utils.call_with_backoff(
            compute_client.get_volume_attachment,
            volume_attachment_id=volume_attachment_id,
        ).data
        if volume_attachment.lifecycle_state in ["DETACHING", "DETACHED"]:
            result["changed"] = False
            result["volume_attachment"] = to_dict(volume_attachment)
        else:
            oci_utils.call_with_backoff(
                compute_client.detach_volume, volume_attachment_id=volume_attachment_id
            )
            response = oci_utils.call_with_backoff(
                compute_client.get_volume_attachment,
                volume_attachment_id=volume_attachment_id,
            )
            result["volume_attachment"] = to_dict(
                oci.wait_until(
                    compute_client, response, "lifecycle_state", "DETACHED"
                ).data
            )
            result["changed"] = True
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    return result


def get_attach_volume_details(instance_id, volume_id, type, attachment_name=None):
    attach_volume_details = AttachVolumeDetails()
    attach_volume_details.display_name = attachment_name
    attach_volume_details.instance_id = instance_id
    attach_volume_details.type = type
    attach_volume_details.volume_id = volume_id
    return attach_volume_details


def attach_volume(compute_client, module, attach_volume_details):
    result = dict()
    result["changed"] = False

    try:
        response = oci_utils.call_with_backoff(
            compute_client.attach_volume, attach_volume_details=attach_volume_details
        )
        response = oci_utils.call_with_backoff(
            compute_client.get_volume_attachment, volume_attachment_id=response.data.id
        )
        result["volume_attachment"] = to_dict(
            oci.wait_until(compute_client, response, "lifecycle_state", "ATTACHED").data
        )
        result["changed"] = True
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))


def terminate_instance(compute_client, id, module):
    return oci_utils.delete_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_client,
        get_fn=compute_client.get_instance,
        kwargs_get={"instance_id": id},
        delete_fn=compute_client.terminate_instance,
        kwargs_delete={
            "instance_id": id,
            "preserve_boot_volume": module.params["preserve_boot_volume"],
        },
        module=module,
    )


def update_instance(compute_client, instance, module):
    result = dict()
    changed = False
    try:
        uid = UpdateInstanceDetails()
        if not oci_utils.are_attrs_equal(
            current_resource=instance,
            module=module,
            attributes=uid.attribute_map.keys(),
        ):
            # Update-able attributes are unequal, let us update the resource
            uid = oci_utils.update_model_with_user_options(
                curr_model=instance, update_model=uid, module=module
            )

            response = oci_utils.call_with_backoff(
                compute_client.update_instance,
                instance_id=instance.id,
                update_instance_details=uid,
            )
            changed = True
            # retain instances for backward compat
            # result["instances"] = [to_dict(response.data)]
            result["instance"] = to_dict(response.data)
        else:
            # No change needed, return the current instance
            # retain instances for backward compat
            # result["instances"] = [to_dict(instance)]
            result["instance"] = to_dict(instance)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result["changed"] = changed
    return result


def power_action_on_instance(compute_client, id, desired_state, module):
    result = {}
    changed = False
    # The power action to execute on a compute instance to reach the desired 'state'
    state_action_map = {
        "stopped": "STOP",
        "running": "START",
        "reset": "RESET",
        "softreset": "SOFTRESET",
    }
    # The desired lifecycle state for the compute instance to reach the user specified 'state'
    desired_lifecycle_states = {
        "stopped": "STOPPED",
        "running": "RUNNING",
        "reset": "RUNNING",
        "softreset": "RUNNING",
    }
    try:
        response = oci_utils.call_with_backoff(
            compute_client.get_instance, instance_id=id
        )
        curr_state = response.data.lifecycle_state

        change_required = False

        # We need to perform a power action if the current state doesn't match the desired state
        if curr_state != desired_lifecycle_states[desired_state]:
            change_required = True

        # Resets also require a change
        if desired_state in ["softreset", "reset"]:
            change_required = True

        if change_required:
            changed = True
            oci_utils.call_with_backoff(
                compute_client.instance_action,
                instance_id=id,
                action=state_action_map[desired_state],
            )
            response = oci_utils.call_with_backoff(
                compute_client.get_instance, instance_id=id
            )
            # for now the power actions on instances do not go through common utilities for wait.
            if module.params.get("wait", None):
                debug(
                    "waiting for lifecycle_state to reach {0}".format(
                        desired_lifecycle_states[desired_state]
                    )
                )
                oci.wait_until(
                    compute_client,
                    response,
                    "lifecycle_state",
                    desired_lifecycle_states[desired_state],
                    max_wait_seconds=module.params.get(
                        "wait_timeout", oci_utils.MAX_WAIT_TIMEOUT_IN_SECONDS
                    ),
                )
                response = oci_utils.call_with_backoff(
                    compute_client.get_instance, instance_id=id
                )
            else:
                debug(
                    "Not waiting for power action request {0} as 'wait' is false.".format(
                        desired_state
                    )
                )
        # retain instances for backward compat
        # result["instances"] = [to_dict(response.data)]
        result["instance"] = to_dict(response.data)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    result["changed"] = changed
    return result


def launch_instance(compute_client, module):
    lid = get_launch_instance_details(module)
    cvd = get_vnic_details(module)
    lid.create_vnic_details = cvd

    debug("Provisioning " + str(lid))
    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        client=compute_client,
        create_fn=compute_client.launch_instance,
        kwargs_create={"launch_instance_details": lid},
        get_fn=compute_client.get_instance,
        get_param="instance_id",
        module=module,
    )
    return result


def get_vnic_details(module):
    vnic_details = module.params.get("vnic", None)
    if not vnic_details:
        # Primary VNIC details(especially subnet_id is required)
        module.fail_json(
            msg="state is present and instance_id is not specified, but create_vnic_details is not "
            "specified."
        )

    cvd = CreateVnicDetails()
    cvd.display_name = vnic_details.get("name", None)
    cvd.assign_public_ip = vnic_details.get("assign_public_ip", None)
    cvd.hostname_label = vnic_details.get("hostname_label", None)
    cvd.private_ip = vnic_details.get("private_ip", None)
    cvd.skip_source_dest_check = vnic_details.get("skip_source_dest_check", None)
    cvd.subnet_id = vnic_details["subnet_id"]
    return cvd


def get_source_details_from_module(module):
    # An instance's source can either be specified by top-level options "image_id" or via "source_details"
    if "source_details" in module.params and module.params["source_details"]:
        source_details = module.params["source_details"]
        source_type = source_details.get("source_type")
        if source_type == "image":
            image_id = source_details.get("image_id")
            boot_volume_size_in_gbs = source_details.get("boot_volume_size_in_gbs")
            if not image_id:
                module.fail_json(
                    msg="state is present, source_details' type is specified as image, but image_id is not"
                    "specified"
                )
            return _create_instance_source_via_image(
                image_id, boot_volume_size_in_gbs=boot_volume_size_in_gbs
            )
        if source_type == "bootVolume":
            boot_volume_id = source_details.get("boot_volume_id")
            if not boot_volume_id:
                module.fail_json(
                    msg="state is present, source_details' type is specified as bootVolume, but "
                    "boot_volume_id is not specified"
                )
            return _create_instance_source_via_boot_volume(boot_volume_id)
        module.fail_json(
            msg="value of source_type must be one of: 'bootVolume', 'image'"
        )
    elif "image_id" in module.params and module.params["image_id"]:
        return _create_instance_source_via_image(module.params["image_id"])
    return None


def get_launch_instance_details(module):
    lid = LaunchInstanceDetails()

    lid.display_name = module.params["name"]
    lid.availability_domain = module.params["availability_domain"]
    lid.compartment_id = module.params["compartment_id"]

    # 'fault_domain' requires OCI Python SDK 2.0.1
    fault_domain = module.params["fault_domain"]
    if fault_domain is not None:
        if "fault_domain" in lid.attribute_map:
            lid.fault_domain = fault_domain
        else:
            module.fail_json(
                msg="OCI Python SDK 2.0.1 or above is required to support `fault_domain`. The local SDK"
                "version is {0}".format(oci.__version__)
            )

    lid.extended_metadata = module.params["extended_metadata"]
    lid.metadata = module.params["metadata"]
    lid.ipxe_script = module.params["ipxe_script"]
    lid.shape = module.params["shape"]
    oci_utils.add_tags_to_model_from_module(lid, module)
    lid.source_details = get_source_details_from_module(module)
    return lid


def _create_instance_source_via_image(image_id, boot_volume_size_in_gbs=None):
    instance_source_details = InstanceSourceViaImageDetails()
    instance_source_details.image_id = image_id
    if boot_volume_size_in_gbs:
        instance_source_details.boot_volume_size_in_gbs = boot_volume_size_in_gbs
    return instance_source_details


def _create_instance_source_via_boot_volume(boot_volume_id):
    instance_source_details = InstanceSourceViaBootVolumeDetails()
    instance_source_details.boot_volume_id = boot_volume_id
    return instance_source_details


def debug(s):
    get_logger().debug(s)


def handle_volume_attachment(compute_client, module, volume_id, instance_id):
    result = dict()
    volume_details = module.params["volume_details"]
    compartment_id = module.params["compartment_id"]
    if instance_id is None:
        instance_id = module.params["instance_id"]

    if compartment_id is None:
        compartment_id = compute_client.get_instance(instance_id).data.compartment_id

    try:
        # Check if volume_id is already attached to instance_id
        volume_attachments = to_dict(
            compute_client.list_volume_attachments(
                compartment_id, instance_id=instance_id, volume_id=volume_id
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Case when volume_id is already ATTACHED or is ATTACHING to instance_id
    for volume_attachment in volume_attachments:
        if volume_attachment["lifecycle_state"] in ["ATTACHING", "ATTACHED"]:
            result["changed"] = False
            return result

    key_list = ["attachment_name", "type"]
    param_map = dict(
        (k, v)
        for (k, v) in six.iteritems(volume_details)
        if k in key_list and v is not None
    )

    attach_volume_details = get_attach_volume_details(
        instance_id=instance_id, volume_id=volume_id, **param_map
    )

    return attach_volume(compute_client, module, attach_volume_details)


def handle_volume_detachment(compute_client, module, volume_id):
    result = dict()
    compartment_id = module.params["compartment_id"]
    instance_id = module.params["instance_id"]
    if compartment_id is None:
        compartment_id = compute_client.get_instance(instance_id).data.compartment_id

    try:
        # Get the volume attachment with the instance_id & volume_id
        volume_attachments = to_dict(
            compute_client.list_volume_attachments(
                compartment_id, instance_id=instance_id, volume_id=volume_id
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Volume attachment with volume_id & instance_id does not exist

    if not volume_attachments:
        result["changed"] = False
        return result

    for volume_attachment in volume_attachments:
        if volume_attachment["lifecycle_state"] in ["ATTACHED"]:
            volume_attachment_id = volume_attachment["id"]
            return detach_volume(compute_client, module, volume_attachment_id)

    # Case when all volume attachments for instance_id & volume_id are in non-ATTACHED state
    result["changed"] = False
    return result


def combine_result(result, attachment_result, boot_volume_attachment_result):
    combined_result = result
    if attachment_result is None:
        attachment_result = {}
    if boot_volume_attachment_result is None:
        boot_volume_attachment_result = {}

    combined_result["changed"] = any(
        [
            result["changed"],
            attachment_result.get("changed", False),
            boot_volume_attachment_result.get("changed", False),
        ]
    )
    return combined_result


@check_mode
def handle_volume_details(compute_client, module, instance_id=None):
    attachment_result = dict(changed=False)
    volume_details = module.params["volume_details"]
    if volume_details:
        if "attachment_state" in volume_details:
            attachment_state = volume_details["attachment_state"]
        else:
            attachment_state = "present"

        # Check if volume_id is specified
        if "volume_id" in volume_details and volume_details["volume_id"] is not None:
            volume_id = volume_details["volume_id"]
            if attachment_state == "present":
                attachment_result = handle_volume_attachment(
                    compute_client, module, volume_id, instance_id
                )
            elif attachment_state == "absent":
                attachment_result = handle_volume_detachment(
                    compute_client, module, volume_id
                )
            else:
                module.fail_json(msg="Invalid attachment_state under volume_details")
        else:
            attachment_result["changed"] = False

    return attachment_result


@check_mode
def add_volume_attachment_info(module, compute_client, result):
    if "instance" in result:
        try:
            instance = result["instance"]
            vol_attachments = oci_compute_utils.get_volume_attachments(
                compute_client, instance
            )
            result["instance"]["volume_attachments"] = vol_attachments
        except ServiceError as ex:
            module.fail_json(msg=ex.message)


# Boot volume attachment attach and detach actions do not have separate "wait" related options. They share the
# module's options for wait and wait timeout.
def attach_boot_volume(compute_client, module, attach_boot_volume_details):
    return oci_utils.create_and_wait(
        resource_type="boot_volume_attachment",
        client=compute_client,
        create_fn=compute_client.attach_boot_volume,
        kwargs_create={"attach_boot_volume_details": attach_boot_volume_details},
        get_fn=compute_client.get_boot_volume_attachment,
        get_param="boot_volume_attachment_id",
        module=module,
    )


def add_primary_ip_info(module, compute_client, network_client, result):
    if "instance" in result:
        try:
            instance = result["instance"]
            primary_public_ip, primary_private_ip = oci_compute_utils.get_primary_ips(
                compute_client, network_client, instance
            )
            instance["primary_public_ip"] = primary_public_ip
            instance["primary_private_ip"] = primary_private_ip
        except ServiceError as ex:
            instance["primary_public_ip"] = None
            instance["primary_private_ip"] = None
            module.fail_json(msg=ex.message)


def get_attach_boot_volume_details(instance_id, boot_volume_id, attachment_name=None):
    attach_boot_volume_details = AttachBootVolumeDetails()
    attach_boot_volume_details.display_name = attachment_name
    attach_boot_volume_details.instance_id = instance_id
    attach_boot_volume_details.boot_volume_id = boot_volume_id
    return attach_boot_volume_details


def handle_boot_volume_attachment(compute_client, module, boot_volume_id, instance_id):
    result = dict()

    compartment_id = module.params["compartment_id"]
    ad = module.params["availability_domain"]
    if instance_id is None:
        instance_id = module.params["instance_id"]
    try:
        if compartment_id is None:
            compartment_id = compute_client.get_instance(
                instance_id
            ).data.compartment_id

        if ad is None:
            ad = compute_client.get_instance(instance_id).data.availability_domain

        # Check if boot_volume_id is already attached to instance_id
        boot_volume_attachments = to_dict(
            compute_client.list_boot_volume_attachments(
                ad,
                compartment_id,
                instance_id=instance_id,
                boot_volume_id=boot_volume_id,
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Case when boot_volume_id is already ATTACHED or is ATTACHING to instance_id
    for boot_volume_attachment in boot_volume_attachments:
        if boot_volume_attachment["lifecycle_state"] in ["ATTACHING", "ATTACHED"]:
            result["changed"] = False
            return result

    attach_boot_volume_details = get_attach_boot_volume_details(
        instance_id=instance_id, boot_volume_id=boot_volume_id
    )

    return attach_boot_volume(compute_client, module, attach_boot_volume_details)


def detach_boot_volume(compute_client, module, boot_volume_attachment_id):
    return oci_utils.delete_and_wait(
        resource_type="boot_volume_attachment",
        client=compute_client,
        get_fn=compute_client.get_boot_volume_attachment,
        kwargs_get={"boot_volume_attachment_id": boot_volume_attachment_id},
        delete_fn=compute_client.detach_boot_volume,
        kwargs_delete={"boot_volume_attachment_id": boot_volume_attachment_id},
        module=module,
    )


def handle_boot_volume_detachment(compute_client, module, boot_volume_id):
    result = dict()
    compartment_id = module.params["compartment_id"]
    instance_id = module.params["instance_id"]
    ad = module.params["availability_domain"]
    try:

        if compartment_id is None:
            compartment_id = compute_client.get_instance(
                instance_id
            ).data.compartment_id

        if ad is None:
            ad = compute_client.get_instance(instance_id).data.availability_domain

        # Get the boot volume attachment with the instance_id & volume_id
        boot_volume_attachments = to_dict(
            compute_client.list_boot_volume_attachments(
                ad,
                compartment_id,
                instance_id=instance_id,
                boot_volume_id=boot_volume_id,
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    # Boot volume attachment with volume_id & instance_id does not exist
    if not boot_volume_attachments:
        result["changed"] = False
        return result

    for boot_volume_attachment in boot_volume_attachments:
        if boot_volume_attachment["lifecycle_state"] == "ATTACHED":
            boot_volume_attachment_id = boot_volume_attachment["id"]
            return detach_boot_volume(compute_client, module, boot_volume_attachment_id)

    # Case when boot volume attachment for instance_id & volume_id is in non-ATTACHED state
    result["changed"] = False
    return result


@check_mode
def handle_boot_volume_details(compute_client, module, instance_id=None):
    attachment_result = dict(changed=False)
    boot_volume_details = module.params["boot_volume_details"]
    if boot_volume_details:
        if "attachment_state" in boot_volume_details:
            attachment_state = boot_volume_details["attachment_state"]
        else:
            attachment_state = "present"

        # Check if boot_volume_id is specified
        if (
            "boot_volume_id" in boot_volume_details
            and boot_volume_details["boot_volume_id"] is not None
        ):
            boot_volume_id = boot_volume_details["boot_volume_id"]
            if attachment_state == "present":
                attachment_result = handle_boot_volume_attachment(
                    compute_client, module, boot_volume_id, instance_id
                )
            elif attachment_state == "absent":
                attachment_result = handle_boot_volume_detachment(
                    compute_client, module, boot_volume_id
                )
            else:
                module.fail_json(
                    msg="Invalid attachment_state under boot_volume_details"
                )

    return attachment_result


@check_mode
def add_boot_volume_attachment_info(module, compute_client, result):
    if "instance" in result:
        try:
            instance = result["instance"]
            boot_vol_attachment = oci_compute_utils.get_boot_volume_attachment(
                compute_client, instance
            )
            result["instance"]["boot_volume_attachment"] = boot_vol_attachment
        except ServiceError as ex:
            module.fail_json(msg=ex.message)


def _get_default_source_details(module):
    """
    Return the user specified value of image_id value as default for source_details.

    The GET model of the Resource API returns `image_id` in the `source_details` section of the Resource. So,
    we construct an equivalent source_details for a user-specified "image_id" and set as the default value for
    the "source_details" object, so that an existing resource with the same state matches.
    """
    if "source_details" in module.params and module.params["source_details"]:
        return module.params["source_details"]

    elif module.params.get("image_id"):
        image_id = module.params["image_id"]
        return {"source_type": "image", "image_id": image_id}

    return None


def _get_default_image_id(module):
    """
    Return the image_id if the image_id was specified through "source_details" or None.
    """
    if "source_details" in module.params and module.params["source_details"]:
        source_details = module.params["source_details"]
        source_type = source_details.get("source_type")
        if not source_type:
            if "source_type" not in source_details:
                module.fail_json(
                    msg="source_type required and must be one of: 'bootVolume', 'image'"
                )
        if source_type == "image":
            return source_details["image_id"]
    return None


def set_logger(my_logger):
    global logger
    logger = my_logger


def get_logger():
    return logger


def _get_exclude_attributes(module):
    # display_name is generated by OCI if unspecified, so always exclude it during matching
    exclude_attributes = {"display_name": True}
    if "source_details" in module.params and module.params["source_details"]:
        source_details = module.params["source_details"]
        if "source_type" not in source_details:
            module.fail_json(
                msg="source_type required and must be one of: 'bootVolume', 'image'"
            )
        if source_details["source_type"] == "bootVolume":
            # if an Instance is being created by a boot volume id, ignore the "image_id" attribute of the existing
            # resources during matching
            exclude_attributes.update({"image_id": True})
    return exclude_attributes


def create_one_instance(compute_client, module):
    result = oci_utils.check_and_create_resource(
        resource_type="instance",
        create_fn=launch_instance,
        kwargs_create={"compute_client": compute_client, "module": module},
        list_fn=compute_client.list_instances,
        kwargs_list={"compartment_id": module.params["compartment_id"]},
        module=module,
        model=LaunchInstanceDetails(),
        exclude_attributes=_get_exclude_attributes(module),
        default_attribute_values={
            "ipxe_script": None,
            "extended_metadata": {},
            "metadata": {},
            # during matching, if an existing
            # resource has the same values as the
            # current user request, consider it as
            # a match.
            "source_details": _get_default_source_details(module),
            "image_id": _get_default_image_id(module),
        },
    )
    # Handle volume details when an instance is launched
    vol_attachment_result = {}
    if result["changed"]:
        vol_attachment_result = handle_volume_details(
            compute_client, module, instance_id=result["instance"]["id"]
        )
    return result, vol_attachment_result


def _generate_name_for_instance(name_prefix, suffix):
    # If the 'display_name' is specified as a printf like string, use the user-specified format,
    # else the standard format to generate the name is <name_prefix>-<suffix>
    try:
        return name_prefix % suffix
    except TypeError:
        if name_prefix:
            return name_prefix + "-" + str(suffix)
        return None


def main():
    my_logger = oci_utils.get_logger("oci_instance")
    set_logger(my_logger)

    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=False),
            boot_volume_details=dict(type="dict", required=False),
            compartment_id=dict(type="str", required=False),
            extended_metadata=dict(type="dict", required=False),
            fault_domain=dict(type="str", required=False),
            instance_id=dict(type="str", required=False, aliases=["id"]),
            image_id=dict(type="str", required=False),
            ipxe_script=dict(type="str", required=False),
            metadata=dict(type="dict", required=False),
            name=dict(type="str", required=False, aliases=["display_name"]),
            preserve_boot_volume=dict(type="bool", required=False, default=False),
            shape=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=[
                    "present",
                    "absent",
                    "running",
                    "stopped",
                    "reset",
                    "softreset",
                ],
            ),
            volume_details=dict(type="dict", required=False),
            source_details=dict(type="dict", required=False),
            vnic=dict(type="dict", aliases=["create_vnic_details"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[["state", "absent", ["instance_id"]]],
        mutually_exclusive=[
            ["boot_volume_details", "image_id"],
            ["vnic", "instance_id"],
            ["source_details", "image_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)
    network_client = oci_utils.create_service_client(module, VirtualNetworkClient)
    state = module.params["state"]

    result = dict(changed=False)
    vol_attachment_result = dict(changed=False)
    boot_volume_attachment_result = dict(changed=False)

    id = module.params["instance_id"]
    try:
        if id is not None:
            inst = None

            # Attempt to get the instance
            try:
                inst = oci_utils.call_with_backoff(
                    compute_client.get_instance, instance_id=id
                ).data
            except ServiceError as se:
                module.fail_json(msg=se.message())

            if state == "absent":
                if inst is not None:
                    terminate_result = terminate_instance(compute_client, id, module)
                    result["changed"] = terminate_result["changed"]
                    # result["instances"] = [terminate_result["instance"]]
                    result["instance"] = terminate_result["instance"]
                else:
                    pass  # instance is already deleted.
            elif state == "present":
                result = update_instance(compute_client, inst, module)
                # Handle volume details after update-instance operation
                vol_attachment_result = handle_volume_details(compute_client, module)
                # Handle boot volume details after update-instance operation
                boot_volume_attachment_result = handle_boot_volume_details(
                    compute_client, module
                )
            else:
                # One of the power actions needs to be applied

                # If a boot volume is to be attached to an instance & the instance should be in RUNNING state,
                # the attachment should be done before the power_action_on_instance.
                if state == "running":
                    boot_volume_attachment_result = handle_boot_volume_details(
                        compute_client, module
                    )

                # perform power actions on instance
                result = power_action_on_instance(compute_client, id, state, module)

                # Handle volume details after power action on instance
                vol_attachment_result = handle_volume_details(compute_client, module)

                # If a boot volume is to be detached from an instance & the instance should be in STOPPED state,
                # the detachment should be done after the power_action_on_instance.
                if state == "stopped":
                    boot_volume_attachment_result = handle_boot_volume_details(
                        compute_client, module
                    )
        else:
            debug("check and create instance")

            create_result, vol_attachment_result = create_one_instance(
                compute_client, module
            )
            result["changed"] = create_result["changed"]
            # result["instances"] = [create_result["instance"]]
            result["instance"] = create_result["instance"]

        result = combine_result(
            result, vol_attachment_result, boot_volume_attachment_result
        )
        add_volume_attachment_info(module, compute_client, result)
        add_boot_volume_attachment_info(module, compute_client, result)
        add_primary_ip_info(module, compute_client, network_client, result)
        result["instances"] = [result["instance"]]
        module.exit_json(**result)
    except ServiceError as se:
        module.fail_json(msg=se.message)


if __name__ == "__main__":
    main()
