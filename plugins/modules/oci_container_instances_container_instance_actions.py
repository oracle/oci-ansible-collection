#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_container_instances_container_instance_actions
short_description: Perform actions on a ContainerInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ContainerInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a container instance resource from one compartment identifier to another. When provided, If-Match is checked
      against ETag values of the resource.
    - For I(action=restart), restarts a container instance. When provided, If-Match is checked against ETag values of the container instance.
    - "For I(action=start), starts a container instance if it is \\"inactive\\". No effect otherwise. When provided, If-Match is checked against ETag values of
      the container instance."
    - "For I(action=stop), stops a container instance if it is \\"active\\". No effect otherwise. When provided, If-Match is checked against ETag values of the
      container instance."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the container instance to.
            - Required for I(action=change_compartment).
        type: str
    container_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container instance.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ContainerInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "restart"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on container_instance
  oci_container_instances_container_instance_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    container_instance_id: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action restart on container_instance
  oci_container_instances_container_instance_actions:
    # required
    container_instance_id: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: restart

- name: Perform action start on container_instance
  oci_container_instances_container_instance_actions:
    # required
    container_instance_id: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on container_instance
  oci_container_instances_container_instance_actions:
    # required
    container_instance_id: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
container_instance:
    description:
        - Details of the ContainerInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - An OCID that cannot be changed.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`."
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`."
            returned: on success
            type: dict
            sample: {}
        availability_domain:
            description:
                - The availability domain to place the container instance.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - The fault domain to place the container instance.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        lifecycle_state:
            description:
                - The current state of the container instance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message that describes the current state of the container in more detail. Can be used to provide
                  actionable information.
            returned: on success
            type: str
            sample: lifecycle_details_example
        volumes:
            description:
                - A volume is a directory with data that is accessible across multiple containers in a
                  container instance.
            returned: on success
            type: complex
            contains:
                configs:
                    description:
                        - Contains string key value pairs which can be mounted as individual files inside the container. The value needs to be base64 encoded.
                          It is decoded to plain text before the mount.
                    returned: on success
                    type: complex
                    contains:
                        file_name:
                            description:
                                - The name of the file. The fileName should be unique across the volume.
                            returned: on success
                            type: str
                            sample: file_name_example
                        data:
                            description:
                                - The base64 encoded contents of the file. The contents are decoded to plain text before mounted as a file to a container inside
                                  container instance.
                            returned: on success
                            type: str
                            sample: "null"

                        path:
                            description:
                                - (Optional) Relative path for this file inside the volume mount directory. By default, the file is presented at the root of the
                                  volume mount path.
                            returned: on success
                            type: str
                            sample: path_example
                name:
                    description:
                        - The name of the volume. This must be unique within a single container instance.
                    returned: on success
                    type: str
                    sample: name_example
                volume_type:
                    description:
                        - The type of volume.
                    returned: on success
                    type: str
                    sample: EMPTYDIR
                backing_store:
                    description:
                        - The volume type of the empty directory, can be either File Storage or Memory.
                    returned: on success
                    type: str
                    sample: EPHEMERAL_STORAGE
        volume_count:
            description:
                - The number of volumes that are attached to the container instance.
            returned: on success
            type: int
            sample: 56
        containers:
            description:
                - The containers on the container instance.
            returned: on success
            type: complex
            contains:
                container_id:
                    description:
                        - The OCID of the container.
                    returned: on success
                    type: str
                    sample: "ocid1.container.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Display name for the Container.
                    returned: on success
                    type: str
                    sample: display_name_example
        container_count:
            description:
                - The number of containers on the container instance.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The time the container instance was created, in the format defined by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the container instance was updated, in the format defined by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        shape:
            description:
                - The shape of the container instance. The shape determines the number of OCPUs, amount of memory, and other resources that are allocated to a
                  container instance.
            returned: on success
            type: str
            sample: shape_example
        shape_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs available to the container instance.
                    returned: on success
                    type: float
                    sample: 3.4
                memory_in_gbs:
                    description:
                        - The total amount of memory available to the container instance, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                processor_description:
                    description:
                        - A short description of the container instance's processor (CPU).
                    returned: on success
                    type: str
                    sample: processor_description_example
                networking_bandwidth_in_gbps:
                    description:
                        - The networking bandwidth available to the container instance, in gigabits per second.
                    returned: on success
                    type: float
                    sample: 3.4
        vnics:
            description:
                - The virtual networks available to the containers in the container instance.
            returned: on success
            type: complex
            contains:
                vnic_id:
                    description:
                        - The identifier of the virtual network interface card (VNIC) over which
                          the containers accessing this network can communicate with the
                          larger virtual cloud network.
                    returned: on success
                    type: str
                    sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        dns_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                nameservers:
                    description:
                        - "IP address of the name server.."
                    returned: on success
                    type: list
                    sample: []
                searches:
                    description:
                        - Search list for hostname lookup.
                    returned: on success
                    type: list
                    sample: []
                options:
                    description:
                        - Options allows certain internal resolver variables to be modified.
                    returned: on success
                    type: list
                    sample: []
        graceful_shutdown_timeout_in_seconds:
            description:
                - The amount of time that processes in a container have to gracefully end when the container must be stopped. For example, when you delete a
                  container instance. After the timeout is reached, the processes are sent a signal to be deleted.
            returned: on success
            type: int
            sample: 56
        image_pull_secrets:
            description:
                - The image pulls secrets so you can access private registry to pull container images.
            returned: on success
            type: complex
            contains:
                secret_type:
                    description:
                        - The type of ImagePullSecret.
                    returned: on success
                    type: str
                    sample: BASIC
                registry_endpoint:
                    description:
                        - The registry endpoint of the container image.
                    returned: on success
                    type: str
                    sample: registry_endpoint_example
                secret_id:
                    description:
                        - The OCID of the secret for registry credentials.
                    returned: on success
                    type: str
                    sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        container_restart_policy:
            description:
                - The container restart policy is applied for all containers in container instance.
            returned: on success
            type: str
            sample: ALWAYS
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domain": "FAULT-DOMAIN-1",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "volumes": [{
            "configs": [{
                "file_name": "file_name_example",
                "data": null,
                "path": "path_example"
            }],
            "name": "name_example",
            "volume_type": "EMPTYDIR",
            "backing_store": "EPHEMERAL_STORAGE"
        }],
        "volume_count": 56,
        "containers": [{
            "container_id": "ocid1.container.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "container_count": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "shape": "shape_example",
        "shape_config": {
            "ocpus": 3.4,
            "memory_in_gbs": 3.4,
            "processor_description": "processor_description_example",
            "networking_bandwidth_in_gbps": 3.4
        },
        "vnics": [{
            "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "dns_config": {
            "nameservers": [],
            "searches": [],
            "options": []
        },
        "graceful_shutdown_timeout_in_seconds": 56,
        "image_pull_secrets": [{
            "secret_type": "BASIC",
            "registry_endpoint": "registry_endpoint_example",
            "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "container_restart_policy": "ALWAYS"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.container_instances import ContainerInstanceClient
    from oci.container_instances.models import ChangeContainerInstanceCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        restart
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "container_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("container_instance_id")

    def get_get_fn(self):
        return self.client.get_container_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_instance,
            container_instance_id=self.module.params.get("container_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeContainerInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_container_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                container_instance_id=self.module.params.get("container_instance_id"),
                change_container_instance_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def restart(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restart_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                container_instance_id=self.module.params.get("container_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                container_instance_id=self.module.params.get("container_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                container_instance_id=self.module.params.get("container_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ContainerInstanceActionsHelperCustom = get_custom_class(
    "ContainerInstanceActionsHelperCustom"
)


class ResourceHelper(
    ContainerInstanceActionsHelperCustom, ContainerInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            container_instance_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "restart", "start", "stop"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="container_instance",
        service_client_class=ContainerInstanceClient,
        namespace="container_instances",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
