#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_container_instances_container_instance_facts
short_description: Fetches details about one or multiple ContainerInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ContainerInstance resources in Oracle Cloud Infrastructure
    - Returns a list of ContainerInstances.
    - If I(container_instance_id) is specified, the details of a single ContainerInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    container_instance_id:
        description:
            - The system-generated unique identifier for the ContainerInstance.
            - Required to get a specific container_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple container_instances.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific container_instance
  oci_container_instances_container_instance_facts:
    # required
    container_instance_id: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List container_instances
  oci_container_instances_container_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    availability_domain: Uocm:PHX-AD-1
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
container_instances:
    description:
        - List of ContainerInstance resources
    returned: on success
    type: complex
    contains:
        volumes:
            description:
                - A Volume represents a directory with data that is accessible across multiple containers in a
                  ContainerInstance.
                - Returned for get operation
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
                        - The name of the volume. This has be unique cross single ContainerInstance.
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
                        - Volume type that we are using for empty dir where it could be either File Storage or Memory
                    returned: on success
                    type: str
                    sample: EPHEMERAL_STORAGE
        containers:
            description:
                - The Containers on this Instance
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                container_id:
                    description:
                        - The ID of the Container on this Instance.
                    returned: on success
                    type: str
                    sample: "ocid1.container.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Display name for the Container.
                    returned: on success
                    type: str
                    sample: display_name_example
        vnics:
            description:
                - The virtual networks available to containers running on this Container Instance.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                vnic_id:
                    description:
                        - The ID of the Virtual Network Interface Card (VNIC) over which
                          Containers accessing this network can communicate with the
                          larger Virtual Client Network.
                    returned: on success
                    type: str
                    sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        dns_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                nameservers:
                    description:
                        - Name server IP address
                    returned: on success
                    type: list
                    sample: []
                searches:
                    description:
                        - Search list for host-name lookup.
                    returned: on success
                    type: list
                    sample: []
                options:
                    description:
                        - Options allows certain internal resolver variables to be modified.
                    returned: on success
                    type: list
                    sample: []
        image_pull_secrets:
            description:
                - The image pull secrets for accessing private registry to pull images for containers
                - Returned for get operation
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
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Display name for the ContainerInstance. Can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
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
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        availability_domain:
            description:
                - Availability Domain where the ContainerInstance is running.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - Fault Domain where the ContainerInstance is running.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        lifecycle_state:
            description:
                - The current state of the ContainerInstance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide
                  actionable information for a resource in Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time the the ContainerInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the ContainerInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        shape:
            description:
                - The shape of the Container Instance. The shape determines the resources available to the Container Instance.
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
                        - The total number of OCPUs available to the instance.
                    returned: on success
                    type: float
                    sample: 3.4
                memory_in_gbs:
                    description:
                        - The total amount of memory available to the instance, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
                processor_description:
                    description:
                        - A short description of the instance's processor (CPU).
                    returned: on success
                    type: str
                    sample: processor_description_example
                networking_bandwidth_in_gbps:
                    description:
                        - The networking bandwidth available to the instance, in gigabits per second.
                    returned: on success
                    type: float
                    sample: 3.4
        container_count:
            description:
                - The number of containers on this Instance
            returned: on success
            type: int
            sample: 56
        graceful_shutdown_timeout_in_seconds:
            description:
                - Duration in seconds processes within a Container have to gracefully terminate. This applies whenever a Container must be halted, such as when
                  the Container Instance is deleted. Processes will first be sent a termination signal. After this timeout is reached, the processes will be
                  sent a termination signal.
            returned: on success
            type: int
            sample: 56
        volume_count:
            description:
                - The number of volumes that attached to this Instance
            returned: on success
            type: int
            sample: 56
        container_restart_policy:
            description:
                - The container restart policy is applied for all containers in container instance.
            returned: on success
            type: str
            sample: ALWAYS
    sample: [{
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
        "containers": [{
            "container_id": "ocid1.container.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "vnics": [{
            "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "dns_config": {
            "nameservers": [],
            "searches": [],
            "options": []
        },
        "image_pull_secrets": [{
            "secret_type": "BASIC",
            "registry_endpoint": "registry_endpoint_example",
            "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        }],
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
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "shape": "shape_example",
        "shape_config": {
            "ocpus": 3.4,
            "memory_in_gbs": 3.4,
            "processor_description": "processor_description_example",
            "networking_bandwidth_in_gbps": 3.4
        },
        "container_count": 56,
        "graceful_shutdown_timeout_in_seconds": 56,
        "volume_count": 56,
        "container_restart_policy": "ALWAYS"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.container_instances import ContainerInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "container_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_instance,
            container_instance_id=self.module.params.get("container_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "availability_domain",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_container_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ContainerInstanceFactsHelperCustom = get_custom_class(
    "ContainerInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    ContainerInstanceFactsHelperCustom, ContainerInstanceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            container_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            availability_domain=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="container_instance",
        service_client_class=ContainerInstanceClient,
        namespace="container_instances",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(container_instances=result)


if __name__ == "__main__":
    main()
