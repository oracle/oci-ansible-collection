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
module: oci_container_instances_container_instance
short_description: Manage a ContainerInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ContainerInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a container instance and deploys the containers on it.
    - "This resource has the following action operations in the M(oracle.oci.oci_container_instances_container_instance_actions) module: change_compartment,
      restart, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment OCID.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    availability_domain:
        description:
            - The availability domain where the container instance runs.
            - Required for create using I(state=present).
        type: str
    fault_domain:
        description:
            - The fault domain where the container instance runs.
        type: str
    shape:
        description:
            - The shape of the container instance. The shape determines the resources available to the container instance.
            - Required for create using I(state=present).
        type: str
    shape_config:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            ocpus:
                description:
                    - The total number of OCPUs available to the container instance.
                type: float
                required: true
            memory_in_gbs:
                description:
                    - The total amount of memory available to the container instance (GB).
                type: float
    volumes:
        description:
            - A volume is a directory with data that is accessible across multiple containers in a
              container instance.
            - You can attach up to 32 volumes to single container instance.
        type: list
        elements: dict
        suboptions:
            configs:
                description:
                    - Contains key value pairs which can be mounted as individual files inside the container. The value needs to be base64 encoded. It is
                      decoded to plain text before the mount.
                    - Applicable when volume_type is 'CONFIGFILE'
                type: list
                elements: dict
                suboptions:
                    file_name:
                        description:
                            - The name of the file. The fileName should be unique across the volume.
                            - Required when volume_type is 'CONFIGFILE'
                        type: str
                        required: true
                    data:
                        description:
                            - The base64 encoded contents of the file. The contents are decoded to plain text before mounted as a file to a container inside
                              container instance.
                            - Required when volume_type is 'CONFIGFILE'
                        type: str
                        required: true
                    path:
                        description:
                            - (Optional) Relative path for this file inside the volume mount directory. By default, the file is presented at the root of the
                              volume mount path.
                            - Applicable when volume_type is 'CONFIGFILE'
                        type: str
            name:
                description:
                    - The name of the volume. This must be unique within a single container instance.
                type: str
                required: true
            volume_type:
                description:
                    - The type of volume.
                type: str
                choices:
                    - "CONFIGFILE"
                    - "EMPTYDIR"
                default: "null"
                required: true
            backing_store:
                description:
                    - The volume type of the empty directory, can be either File Storage or Memory.
                    - Applicable when volume_type is 'EMPTYDIR'
                type: str
    containers:
        description:
            - The containers to create on this container instance.
            - Required for create using I(state=present).
        type: list
        elements: dict
        suboptions:
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                      If you don't provide a name, a name is generated automatically.
                type: str
                aliases: ["name"]
            image_url:
                description:
                    - A URL identifying the image that the container runs in, such as docker.io/library/busybox:latest. If you do not provide a tag, the tag
                      will default to latest.
                    - If no registry is provided, will default the registry to public docker hub `docker.io/library`.
                    - The registry used for container image must be reachable over the Container Instance's VNIC.
                type: str
                required: true
            command:
                description:
                    - An optional command that overrides the ENTRYPOINT process.
                      If you do not provide a value, the existing ENTRYPOINT process defined in the image is used.
                type: list
                elements: str
            arguments:
                description:
                    - A list of string arguments for a container's ENTRYPOINT process.
                    - Many containers use an ENTRYPOINT process pointing to a shell
                      (/bin/bash). For those containers, this argument list
                      specifies the main command in the container process.
                    - The total size of all arguments combined must be 64 KB or smaller.
                type: list
                elements: str
            working_directory:
                description:
                    - The working directory within the container's filesystem for
                      the container process. If not specified, the default
                      working directory from the image is used.
                type: str
            environment_variables:
                description:
                    - A map of additional environment variables to set in the environment of the container's
                      ENTRYPOINT process. These variables are in addition to any variables already defined
                      in the container's image.
                    - The total size of all environment variables combined, name and values, must be 64 KB or smaller.
                type: dict
            volume_mounts:
                description:
                    - List of the volume mounts.
                type: list
                elements: dict
                suboptions:
                    mount_path:
                        description:
                            - The volume access path.
                        type: str
                        required: true
                    volume_name:
                        description:
                            - The name of the volume. Avoid entering confidential information.
                        type: str
                        required: true
                    sub_path:
                        description:
                            - A subpath inside the referenced volume.
                        type: str
                    is_read_only:
                        description:
                            - Whether the volume was mounted in read-only mode. By default, the volume is not read-only.
                        type: bool
                    partition:
                        description:
                            - "If there is more than one partition in the volume, reference this number of partitions.
                              Here is an example:
                              Number  Start   End     Size    File system  Name                  Flags
                              1      1049kB  106MB   105MB   fat16        EFI System Partition  boot, esp
                              2      106MB   1180MB  1074MB  xfs
                              3      1180MB  50.0GB  48.8GB                                     lvm"
                        type: int
            is_resource_principal_disabled:
                description:
                    - Determines if the container will have access to the container instance resource principal.
                    - This method utilizes resource principal version 2.2. For information on how to use the exposed resource principal elements, see
                      https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal.
                type: bool
            resource_config:
                description:
                    - ""
                type: dict
                suboptions:
                    vcpus_limit:
                        description:
                            - The maximum amount of CPUs that can be consumed by the container's process.
                            - If you do not set a value, then the process
                              can use all available CPU resources on the instance.
                            - CPU usage is defined in terms of logical CPUs. This means that the maximum possible value on
                              an E3 ContainerInstance with 1 OCPU is 2.0.
                            - "A container with a 2.0 vcpusLimit could consume up to 100% of the CPU resources available on the container instance.
                              Values can be fractional. A value of \\"1.5\\" means that the container
                              can consume at most the equivalent of 1 and a half logical CPUs worth of CPU capacity."
                        type: float
                    memory_limit_in_gbs:
                        description:
                            - The maximum amount of memory that can be consumed by the container's
                              process.
                            - If you do not set a value, then the process
                              may use all available memory on the instance.
                        type: float
            health_checks:
                description:
                    - list of container health checks to check container status and take appropriate action if container status is failed.
                      There are three types of health checks that we currently support HTTP, TCP, and Command.
                type: list
                elements: dict
                suboptions:
                    path:
                        description:
                            - Container health check HTTP path.
                            - Required when health_check_type is 'HTTP'
                        type: str
                    port:
                        description:
                            - Container health check port.
                            - Required when health_check_type is one of ['TCP', 'HTTP']
                        type: int
                    headers:
                        description:
                            - Container health check HTTP headers.
                            - Applicable when health_check_type is 'HTTP'
                        type: list
                        elements: dict
                        suboptions:
                            name:
                                description:
                                    - Container HTTP header Key.
                                    - Required when health_check_type is 'HTTP'
                                type: str
                                required: true
                            value:
                                description:
                                    - Container HTTP header value.
                                    - Required when health_check_type is 'HTTP'
                                type: str
                                required: true
                    name:
                        description:
                            - Health check name.
                        type: str
                    health_check_type:
                        description:
                            - Container health check type.
                        type: str
                        choices:
                            - "TCP"
                            - "HTTP"
                            - "COMMAND"
                        required: true
                    initial_delay_in_seconds:
                        description:
                            - The initial delay in seconds before start checking container health status.
                        type: int
                    interval_in_seconds:
                        description:
                            - Number of seconds between two consecutive runs for checking container health.
                        type: int
                    failure_threshold:
                        description:
                            - Number of consecutive failures at which we consider the check failed.
                        type: int
                    success_threshold:
                        description:
                            - Number of consecutive successes at which we consider the check succeeded again after it was in failure state.
                        type: int
                    timeout_in_seconds:
                        description:
                            - Length of waiting time in seconds before marking health check failed.
                        type: int
                    failure_action:
                        description:
                            - "The action will be triggered when the container health check fails. There are two types of action: KILL or NONE. The default
                              action is KILL. If failure action is KILL, the container will be subject to the container restart policy."
                        type: str
                        choices:
                            - "KILL"
                            - "NONE"
                    command:
                        description:
                            - The list of strings that will be simplified to a single command for checking the status of the container.
                            - Required when health_check_type is 'COMMAND'
                        type: list
                        elements: str
            security_context:
                description:
                    - ""
                type: dict
                suboptions:
                    security_context_type:
                        description:
                            - The type of security context
                        type: str
                        choices:
                            - "LINUX"
                        default: "LINUX"
                    run_as_user:
                        description:
                            - The user ID (UID) to run the entrypoint process of the container. Defaults to user specified UID in container image metadata if
                              not provided. This must be provided if runAsGroup is provided.
                        type: int
                    run_as_group:
                        description:
                            - The group ID (GID) to run the entrypoint process of the container. Uses runtime default if not provided.
                        type: int
                    is_non_root_user_check_enabled:
                        description:
                            - Indicates if the container must run as a non-root user. If true, the service validates the container image at runtime to ensure
                              that it is not going to run with UID 0 (root) and fails the container instance creation if the validation fails.
                        type: bool
                    is_root_file_system_readonly:
                        description:
                            - Determines if the container will have a read-only root file system. Default value is false.
                        type: bool
            freeform_tags:
                description:
                    - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                      Example: `{\\"bar-key\\": \\"value\\"}`"
                type: dict
            defined_tags:
                description:
                    - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`."
                type: dict
    vnics:
        description:
            - The networks available to containers on this container instance.
            - Required for create using I(state=present).
        type: list
        elements: dict
        suboptions:
            display_name:
                description:
                    - A user-friendly name for the VNIC. Does not have to be unique.
                      Avoid entering confidential information.
                type: str
                aliases: ["name"]
            hostname_label:
                description:
                    - The hostname for the VNIC's primary private IP. Used for DNS.
                type: str
            is_public_ip_assigned:
                description:
                    - Whether the VNIC should be assigned a public IP address.
                type: bool
            skip_source_dest_check:
                description:
                    - Whether the source/destination check is disabled on the VNIC.
                type: bool
            nsg_ids:
                description:
                    - A list of the OCIDs of the network security groups (NSGs) to add the VNIC to.
                type: list
                elements: str
            private_ip:
                description:
                    - A private IP address of your choice to assign to the VNIC. Must be an
                      available IP address within the subnet's CIDR.
                type: str
            subnet_id:
                description:
                    - The OCID of the subnet to create the VNIC in.
                type: str
                required: true
            freeform_tags:
                description:
                    - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                      Example: `{\\"bar-key\\": \\"value\\"}`"
                type: dict
            defined_tags:
                description:
                    - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`."
                type: dict
    dns_config:
        description:
            - ""
        type: dict
        suboptions:
            nameservers:
                description:
                    - IP address of a name server that the resolver should query, either an IPv4 address
                      (in dot notation), or an IPv6 address in colon (and possibly dot) notation. If null, uses
                      nameservers from subnet dhcpDnsOptions.
                type: list
                elements: str
            searches:
                description:
                    - Search list for host-name lookup. If null, we will use searches from subnet dhcpDnsOptios.
                type: list
                elements: str
            options:
                description:
                    - "Options allows certain internal resolver variables to be modified. Options are a list of objects in
                      https://man7.org/linux/man-pages/man5/resolv.conf.5.html. Examples: [\\"ndots:n\\", \\"edns0\\"]."
                type: list
                elements: str
    graceful_shutdown_timeout_in_seconds:
        description:
            - The amount of time that processes in a container have to gracefully end when the container must be stopped. For example, when you delete a
              container instance. After the timeout is reached, the processes are sent a signal to be deleted.
        type: int
    image_pull_secrets:
        description:
            - The image pulls secrets so you can access private registry to pull container images.
        type: list
        elements: dict
        suboptions:
            secret_id:
                description:
                    - The OCID of the secret for registry credentials.
                    - Required when secret_type is 'VAULT'
                type: str
            secret_type:
                description:
                    - The type of ImagePullSecret.
                type: str
                choices:
                    - "VAULT"
                    - "BASIC"
                required: true
            registry_endpoint:
                description:
                    - The registry endpoint of the container image.
                type: str
                required: true
            username:
                description:
                    - The username which should be used with the registry for authentication. The value is expected in base64 format.
                    - Required when secret_type is 'BASIC'
                type: str
            password:
                description:
                    - The password which should be used with the registry for authentication. The value is expected in base64 format.
                    - Required when secret_type is 'BASIC'
                type: str
    container_restart_policy:
        description:
            - Container restart policy
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information. If you don't provide a name, a
              name is generated automatically.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`."
            - This parameter is updatable.
        type: dict
    container_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container instance.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ContainerInstance.
            - Use I(state=present) to create or update a ContainerInstance.
            - Use I(state=absent) to delete a ContainerInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create container_instance
  oci_container_instances_container_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    shape: shape_example
    shape_config:
      # required
      ocpus: 3.4

      # optional
      memory_in_gbs: 3.4
    containers:
    - # required
      image_url: image_url_example

      # optional
      display_name: display_name_example
      command: [ "command_example" ]
      arguments: [ "arguments_example" ]
      working_directory: working_directory_example
      environment_variables: null
      volume_mounts:
      - # required
        mount_path: mount_path_example
        volume_name: volume_name_example

        # optional
        sub_path: sub_path_example
        is_read_only: true
        partition: 56
      is_resource_principal_disabled: true
      resource_config:
        # optional
        vcpus_limit: 3.4
        memory_limit_in_gbs: 3.4
      health_checks:
      - # required
        port: 56
        health_check_type: TCP

        # optional
        name: name_example
        initial_delay_in_seconds: 56
        interval_in_seconds: 56
        failure_threshold: 56
        success_threshold: 56
        timeout_in_seconds: 56
        failure_action: KILL
      security_context:
        # optional
        security_context_type: LINUX
        run_as_user: 56
        run_as_group: 56
        is_non_root_user_check_enabled: true
        is_root_file_system_readonly: true
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
    vnics:
    - # required
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      display_name: display_name_example
      hostname_label: hostname_label_example
      is_public_ip_assigned: true
      skip_source_dest_check: true
      nsg_ids: [ "nsg_ids_example" ]
      private_ip: private_ip_example
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}

    # optional
    fault_domain: FAULT-DOMAIN-1
    volumes:
    - # required
      name: name_example
      volume_type: CONFIGFILE

      # optional
      configs:
      - # required
        file_name: file_name_example
        data: data_example

        # optional
        path: path_example
    dns_config:
      # optional
      nameservers: [ "nameservers_example" ]
      searches: [ "searches_example" ]
      options: [ "options_example" ]
    graceful_shutdown_timeout_in_seconds: 56
    image_pull_secrets:
    - # required
      secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
      secret_type: VAULT
      registry_endpoint: registry_endpoint_example
    container_restart_policy: container_restart_policy_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update container_instance
  oci_container_instances_container_instance:
    # required
    container_instance_id: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update container_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_instances_container_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete container_instance
  oci_container_instances_container_instance:
    # required
    container_instance_id: "ocid1.containerinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete container_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_instances_container_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.container_instances import ContainerInstanceClient
    from oci.container_instances.models import CreateContainerInstanceDetails
    from oci.container_instances.models import UpdateContainerInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ContainerInstanceHelperGen, self).get_possible_entity_types() + [
            "containerinstance",
            "containerinstances",
            "containerInstancescontainerinstance",
            "containerInstancescontainerinstances",
            "containerinstanceresource",
            "containerinstancesresource",
        ]

    def get_module_resource_id_param(self):
        return "container_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("container_instance_id")

    def get_get_fn(self):
        return self.client.get_container_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_instance, container_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_instance,
            container_instance_id=self.module.params.get("container_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "availability_domain"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_container_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateContainerInstanceDetails

    def get_exclude_attributes(self):
        return [
            "containers.resource_config",
            "vnics.freeform_tags",
            "containers.defined_tags",
            "vnics.subnet_id",
            "containers.working_directory",
            "containers.freeform_tags",
            "vnics.defined_tags",
            "vnics.private_ip",
            "vnics.nsg_ids",
            "containers.arguments",
            "vnics.is_public_ip_assigned",
            "vnics.display_name",
            "containers.health_checks",
            "containers.security_context",
            "containers.environment_variables",
            "containers.is_resource_principal_disabled",
            "vnics.skip_source_dest_check",
            "image_pull_secrets.username",
            "containers.image_url",
            "vnics.hostname_label",
            "image_pull_secrets.password",
            "containers.volume_mounts",
            "containers.command",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_container_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateContainerInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                container_instance_id=self.module.params.get("container_instance_id"),
                update_container_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_container_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                container_instance_id=self.module.params.get("container_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ContainerInstanceHelperCustom = get_custom_class("ContainerInstanceHelperCustom")


class ResourceHelper(ContainerInstanceHelperCustom, ContainerInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            fault_domain=dict(type="str"),
            shape=dict(type="str"),
            shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float", required=True),
                    memory_in_gbs=dict(type="float"),
                ),
            ),
            volumes=dict(
                type="list",
                elements="dict",
                options=dict(
                    configs=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            file_name=dict(type="str", required=True),
                            data=dict(type="str", required=True),
                            path=dict(type="str"),
                        ),
                    ),
                    name=dict(type="str", required=True),
                    volume_type=dict(
                        type="str",
                        required=True,
                        default="null",
                        choices=["CONFIGFILE", "EMPTYDIR"],
                    ),
                    backing_store=dict(type="str"),
                ),
            ),
            containers=dict(
                type="list",
                elements="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    image_url=dict(type="str", required=True),
                    command=dict(type="list", elements="str"),
                    arguments=dict(type="list", elements="str"),
                    working_directory=dict(type="str"),
                    environment_variables=dict(type="dict"),
                    volume_mounts=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            mount_path=dict(type="str", required=True),
                            volume_name=dict(type="str", required=True),
                            sub_path=dict(type="str"),
                            is_read_only=dict(type="bool"),
                            partition=dict(type="int"),
                        ),
                    ),
                    is_resource_principal_disabled=dict(type="bool"),
                    resource_config=dict(
                        type="dict",
                        options=dict(
                            vcpus_limit=dict(type="float"),
                            memory_limit_in_gbs=dict(type="float"),
                        ),
                    ),
                    health_checks=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            path=dict(type="str"),
                            port=dict(type="int"),
                            headers=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    name=dict(type="str", required=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            name=dict(type="str"),
                            health_check_type=dict(
                                type="str",
                                required=True,
                                choices=["TCP", "HTTP", "COMMAND"],
                            ),
                            initial_delay_in_seconds=dict(type="int"),
                            interval_in_seconds=dict(type="int"),
                            failure_threshold=dict(type="int"),
                            success_threshold=dict(type="int"),
                            timeout_in_seconds=dict(type="int"),
                            failure_action=dict(type="str", choices=["KILL", "NONE"]),
                            command=dict(type="list", elements="str"),
                        ),
                    ),
                    security_context=dict(
                        type="dict",
                        options=dict(
                            security_context_type=dict(
                                type="str", default="LINUX", choices=["LINUX"]
                            ),
                            run_as_user=dict(type="int"),
                            run_as_group=dict(type="int"),
                            is_non_root_user_check_enabled=dict(type="bool"),
                            is_root_file_system_readonly=dict(type="bool"),
                        ),
                    ),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            vnics=dict(
                type="list",
                elements="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    hostname_label=dict(type="str"),
                    is_public_ip_assigned=dict(type="bool"),
                    skip_source_dest_check=dict(type="bool"),
                    nsg_ids=dict(type="list", elements="str"),
                    private_ip=dict(type="str"),
                    subnet_id=dict(type="str", required=True),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            dns_config=dict(
                type="dict",
                options=dict(
                    nameservers=dict(type="list", elements="str"),
                    searches=dict(type="list", elements="str"),
                    options=dict(type="list", elements="str"),
                ),
            ),
            graceful_shutdown_timeout_in_seconds=dict(type="int"),
            image_pull_secrets=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(
                    secret_id=dict(type="str"),
                    secret_type=dict(
                        type="str", required=True, choices=["VAULT", "BASIC"]
                    ),
                    registry_endpoint=dict(type="str", required=True),
                    username=dict(type="str"),
                    password=dict(type="str", no_log=True),
                ),
            ),
            container_restart_policy=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            container_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
