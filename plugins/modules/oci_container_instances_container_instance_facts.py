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
    - Returns a list of container instances.
    - If I(container_instance_id) is specified, the details of a single ContainerInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    container_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container instance.
            - Required to get a specific container_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
            - Required to list multiple container_instances.
        type: str
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.
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
            - The sort order to use (ASC) or (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order. Default order for timeCreated is descending. Default order for displayName is ascending. If
              you don't specify a value, timeCreated is the default.
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
                - A volume is a directory with data that is accessible across multiple containers in a
                  container instance.
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
        containers:
            description:
                - The containers on the container instance.
                - Returned for get operation
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
        vnics:
            description:
                - The virtual networks available to the containers in the container instance.
                - Returned for get operation
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
                - Returned for get operation
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
        image_pull_secrets:
            description:
                - The image pulls secrets so you can access private registry to pull container images.
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
        container_count:
            description:
                - The number of containers on the container instance.
            returned: on success
            type: int
            sample: 56
        graceful_shutdown_timeout_in_seconds:
            description:
                - The amount of time that processes in a container have to gracefully end when the container must be stopped. For example, when you delete a
                  container instance. After the timeout is reached, the processes are sent a signal to be deleted.
            returned: on success
            type: int
            sample: 56
        volume_count:
            description:
                - The number of volumes that are attached to the container instance.
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
