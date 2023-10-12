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
module: oci_container_instances_container_facts
short_description: Fetches details about one or multiple Container resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Container resources in Oracle Cloud Infrastructure
    - Returns a list of containers in a compartment.
    - If I(container_id) is specified, the details of a single Container will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    container_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container.
            - Required to get a specific container.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
            - Required to list multiple containers.
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
    container_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container instance.
        type: str
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
- name: Get a specific container
  oci_container_instances_container_facts:
    # required
    container_id: "ocid1.container.oc1..xxxxxxEXAMPLExxxxxx"

- name: List containers
  oci_container_instances_container_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    container_instance_id: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
containers:
    description:
        - List of Container resources
    returned: on success
    type: complex
    contains:
        exit_code:
            description:
                - The exit code of the container process when it stopped running.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        time_terminated:
            description:
                - The time when the container last deleted (terminated), in the format defined by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        command:
            description:
                - This command overrides ENTRYPOINT process of the container.
                  If you do not specify this command, the existing ENTRYPOINT process defined in the image is the default.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        arguments:
            description:
                - A list of string arguments for the ENTRYPOINT process of the container.
                - Many containers use an ENTRYPOINT process pointing to a shell
                  `/bin/bash`. For those containers, you can use the argument list to specify the main command in the container process.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        working_directory:
            description:
                - The working directory within the container's filesystem for
                  the container process. If not specified, the default
                  working directory from the image is used.
                - Returned for get operation
            returned: on success
            type: str
            sample: working_directory_example
        environment_variables:
            description:
                - A map of additional environment variables to set in the environment of the
                  ENTRYPOINT process of the container. These variables are in addition to any variables already defined
                  in the container's image.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        volume_mounts:
            description:
                - List of the volume mounts.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                mount_path:
                    description:
                        - Describes the volume access path.
                    returned: on success
                    type: str
                    sample: mount_path_example
                volume_name:
                    description:
                        - The name of the volume.
                    returned: on success
                    type: str
                    sample: volume_name_example
                sub_path:
                    description:
                        - A sub-path inside the referenced volume.
                    returned: on success
                    type: str
                    sample: sub_path_example
                is_read_only:
                    description:
                        - Whether the volume was mounted in read-only mode. By default, the volume is mounted with write access.
                    returned: on success
                    type: bool
                    sample: true
                partition:
                    description:
                        - "If there is more than one partition in the volume, reference this number of partitions.
                          Here is an example:
                          Number  Start   End     Size    File system  Name                  Flags
                          1      1049kB  106MB   105MB   fat16        EFI System Partition  boot, esp
                          2      106MB   1180MB  1074MB  xfs
                          3      1180MB  50.0GB  48.8GB                                     lvm"
                    returned: on success
                    type: int
                    sample: 56
        health_checks:
            description:
                - List of container health checks
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                command:
                    description:
                        - The list of strings that will be simplified to a single command for checking the status of the container.
                    returned: on success
                    type: list
                    sample: []
                path:
                    description:
                        - Container health check HTTP path.
                    returned: on success
                    type: str
                    sample: path_example
                headers:
                    description:
                        - Container health check HTTP headers.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Container HTTP header Key.
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - Container HTTP header value.
                            returned: on success
                            type: str
                            sample: value_example
                name:
                    description:
                        - Health check name.
                    returned: on success
                    type: str
                    sample: name_example
                health_check_type:
                    description:
                        - Container health check type.
                    returned: on success
                    type: str
                    sample: HTTP
                initial_delay_in_seconds:
                    description:
                        - The initial delay in seconds before start checking container health status.
                    returned: on success
                    type: int
                    sample: 56
                interval_in_seconds:
                    description:
                        - Number of seconds between two consecutive runs for checking container health.
                    returned: on success
                    type: int
                    sample: 56
                failure_threshold:
                    description:
                        - Number of consecutive failures at which we consider the check failed.
                    returned: on success
                    type: int
                    sample: 56
                success_threshold:
                    description:
                        - Number of consecutive successes at which we consider the check succeeded again after it was in failure state.
                    returned: on success
                    type: int
                    sample: 56
                timeout_in_seconds:
                    description:
                        - Length of waiting time in seconds before marking health check failed.
                    returned: on success
                    type: int
                    sample: 56
                status:
                    description:
                        - Status of container
                    returned: on success
                    type: str
                    sample: HEALTHY
                status_details:
                    description:
                        - A message describing the current status in more details.
                    returned: on success
                    type: str
                    sample: status_details_example
                failure_action:
                    description:
                        - "The action will be triggered when the container health check fails. There are two types of action: KILL or NONE. The default
                          action is KILL. If failure action is KILL, the container will be subject to the container restart policy."
                    returned: on success
                    type: str
                    sample: KILL
                port:
                    description:
                        - Container health check HTTP port.
                    returned: on success
                    type: int
                    sample: 56
        container_restart_attempt_count:
            description:
                - The number of container restart attempts. Depending on the restart policy, a restart might be attempted after a health check failure or a
                  container exit.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container.
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
                - The OCID of the compartment that contains the container.
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
                - The availability domain where the container instance that hosts the container runs.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - The fault domain of the container instance that hosts the container runs.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        lifecycle_state:
            description:
                - The current state of the container.
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
                - The time the container was created, in the format defined by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the container was updated, in the format defined by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        container_instance_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container instance that the container is
                  running on.
            returned: on success
            type: str
            sample: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"
        resource_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                vcpus_limit:
                    description:
                        - The maximum amount of CPUs that can be consumed by the container's process.
                        - If you do not set a value, then the process
                          may use all available CPU resources on the container instance.
                        - CPU usage is defined in terms of logical CPUs. This means that the
                          maximum possible value on an E3 ContainerInstance with 1 OCPU is 2.0.
                    returned: on success
                    type: float
                    sample: 3.4
                memory_limit_in_gbs:
                    description:
                        - The maximum amount of memory that can be consumed by the container's
                          process. If you do not set a value, then the process
                          may use all available memory on the instance.
                    returned: on success
                    type: float
                    sample: 3.4
        image_url:
            description:
                - The container image information. Currently only supports public Docker registry.
                - You can provide either the image name (containerImage), image name with version (containerImagev1), or complete Docker image URL
                  `docker.io/library/containerImage:latest`.
                - If you do not provide a registry, the registry defaults to public Docker hub `docker.io/library`.
                  The registry used for the container image must be reachable over the VNIC of the container instance.
            returned: on success
            type: str
            sample: image_url_example
        is_resource_principal_disabled:
            description:
                - Determines if the container will have access to the container instance resource principal.
                - This method utilizes resource principal version 2.2. For more information on how to use the exposed resource principal elements, see
                  https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal.
            returned: on success
            type: bool
            sample: true
        security_context:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                security_context_type:
                    description:
                        - The type of security context
                    returned: on success
                    type: str
                    sample: LINUX
                run_as_user:
                    description:
                        - The user ID (UID) to run the entrypoint process of the container. Defaults to user specified UID in container image metadata if not
                          provided. This must be provided if runAsGroup is provided.
                    returned: on success
                    type: int
                    sample: 56
                run_as_group:
                    description:
                        - The group ID (GID) to run the entrypoint process of the container. Uses runtime default if not provided.
                    returned: on success
                    type: int
                    sample: 56
                is_non_root_user_check_enabled:
                    description:
                        - Indicates if the container must run as a non-root user. If true, the service validates the container image at runtime to ensure that
                          it is not going to run with UID 0 (root) and fails the container instance creation if the validation fails.
                    returned: on success
                    type: bool
                    sample: true
                is_root_file_system_readonly:
                    description:
                        - Determines if the container will have a read-only root file system. Default value is false.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
        "exit_code": 56,
        "time_terminated": "2013-10-20T19:20:30+01:00",
        "command": [],
        "arguments": [],
        "working_directory": "working_directory_example",
        "environment_variables": {},
        "volume_mounts": [{
            "mount_path": "mount_path_example",
            "volume_name": "volume_name_example",
            "sub_path": "sub_path_example",
            "is_read_only": true,
            "partition": 56
        }],
        "health_checks": [{
            "command": [],
            "path": "path_example",
            "headers": [{
                "name": "name_example",
                "value": "value_example"
            }],
            "name": "name_example",
            "health_check_type": "HTTP",
            "initial_delay_in_seconds": 56,
            "interval_in_seconds": 56,
            "failure_threshold": 56,
            "success_threshold": 56,
            "timeout_in_seconds": 56,
            "status": "HEALTHY",
            "status_details": "status_details_example",
            "failure_action": "KILL",
            "port": 56
        }],
        "container_restart_attempt_count": 56,
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
        "container_instance_id": "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_config": {
            "vcpus_limit": 3.4,
            "memory_limit_in_gbs": 3.4
        },
        "image_url": "image_url_example",
        "is_resource_principal_disabled": true,
        "security_context": {
            "security_context_type": "LINUX",
            "run_as_user": 56,
            "run_as_group": 56,
            "is_non_root_user_check_enabled": true,
            "is_root_file_system_readonly": true
        }
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


class ContainerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "container_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container,
            container_id=self.module.params.get("container_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "container_instance_id",
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
            self.client.list_containers,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ContainerFactsHelperCustom = get_custom_class("ContainerFactsHelperCustom")


class ResourceFactsHelper(ContainerFactsHelperCustom, ContainerFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            container_id=dict(aliases=["id"], type="str"),
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
            container_instance_id=dict(type="str"),
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
        resource_type="container",
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

    module.exit_json(containers=result)


if __name__ == "__main__":
    main()
