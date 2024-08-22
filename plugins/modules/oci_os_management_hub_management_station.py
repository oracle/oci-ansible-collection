#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_os_management_hub_management_station
short_description: Manage a ManagementStation resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ManagementStation resource in Oracle Cloud Infrastructure
    - For I(state=present), create a management station. You must provide proxy and mirror configuration information.
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_hub_management_station_actions) module: change_compartment,
      refresh_management_station_config, synchronize_mirrors."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the management station.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - User-friendly name for the management station. Does not have to be unique and you can change the name later. Avoid entering confidential
              information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User-specified description of the management station. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    hostname:
        description:
            - Hostname of the management station.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    proxy:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            is_enabled:
                description:
                    - Indicates if the proxy should be enabled or disabled. Default is enabled.
                    - This parameter is updatable.
                type: bool
                required: true
            hosts:
                description:
                    - List of hosts.
                    - This parameter is updatable.
                type: list
                elements: str
            port:
                description:
                    - Listening port used for the proxy.
                    - This parameter is updatable.
                type: str
            forward:
                description:
                    - The URL the proxy will forward to.
                    - This parameter is updatable.
                type: str
    mirror:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            directory:
                description:
                    - Path to the data volume on the management station where software source mirrors are stored.
                    - This parameter is updatable.
                type: str
                required: true
            port:
                description:
                    - Default mirror listening port for http.
                    - This parameter is updatable.
                type: str
                required: true
            sslport:
                description:
                    - Default mirror listening port for https.
                    - This parameter is updatable.
                type: str
                required: true
            sslcert:
                description:
                    - Path to the SSL cerfificate.
                    - This parameter is updatable.
                type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    management_station_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ManagementStation.
            - Use I(state=present) to create or update a ManagementStation.
            - Use I(state=absent) to delete a ManagementStation.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create management_station
  oci_os_management_hub_management_station:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    hostname: hostname_example
    proxy:
      # required
      is_enabled: true

      # optional
      hosts: [ "hosts_example" ]
      port: port_example
      forward: forward_example
    mirror:
      # required
      directory: directory_example
      port: port_example
      sslport: sslport_example

      # optional
      sslcert: sslcert_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update management_station
  oci_os_management_hub_management_station:
    # required
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    hostname: hostname_example
    proxy:
      # required
      is_enabled: true

      # optional
      hosts: [ "hosts_example" ]
      port: port_example
      forward: forward_example
    mirror:
      # required
      directory: directory_example
      port: port_example
      sslport: sslport_example

      # optional
      sslcert: sslcert_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update management_station using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_management_station:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    hostname: hostname_example
    proxy:
      # required
      is_enabled: true

      # optional
      hosts: [ "hosts_example" ]
      port: port_example
      forward: forward_example
    mirror:
      # required
      directory: directory_example
      port: port_example
      sslport: sslport_example

      # optional
      sslcert: sslcert_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete management_station
  oci_os_management_hub_management_station:
    # required
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete management_station using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_management_station:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
management_station:
    description:
        - Details of the ManagementStation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance that is acting as the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        scheduled_job_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the scheduled job for the mirror sync.
            returned: on success
            type: str
            sample: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        profile_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile used for the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the management station.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-specified description for the management station.
            returned: on success
            type: str
            sample: description_example
        hostname:
            description:
                - Hostname of the management station.
            returned: on success
            type: str
            sample: hostname_example
        overall_state:
            description:
                - Current state of the mirror sync for the management station.
            returned: on success
            type: str
            sample: NORMAL
        overall_percentage:
            description:
                - A decimal number representing the progress of the current mirror sync.
            returned: on success
            type: int
            sample: 56
        mirror_capacity:
            description:
                - A decimal number representing the amount of mirror capacity used by the sync.
            returned: on success
            type: int
            sample: 56
        total_mirrors:
            description:
                - The number of software sources that the station is mirroring.
            returned: on success
            type: int
            sample: 56
        mirror_sync_status:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                unsynced:
                    description:
                        - Total number of software sources that have not yet been synced.
                    returned: on success
                    type: int
                    sample: 56
                queued:
                    description:
                        - Total number of software sources that are queued for sync.
                    returned: on success
                    type: int
                    sample: 56
                syncing:
                    description:
                        - Total number of software sources currently syncing.
                    returned: on success
                    type: int
                    sample: 56
                synced:
                    description:
                        - Total number of software sources that successfully synced.
                    returned: on success
                    type: int
                    sample: 56
                failed:
                    description:
                        - Total number of software sources that failed to sync.
                    returned: on success
                    type: int
                    sample: 56
        proxy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - Indicates if the proxy should be enabled or disabled. Default is enabled.
                    returned: on success
                    type: bool
                    sample: true
                hosts:
                    description:
                        - List of hosts.
                    returned: on success
                    type: list
                    sample: []
                port:
                    description:
                        - Listening port used for the proxy.
                    returned: on success
                    type: str
                    sample: port_example
                forward:
                    description:
                        - The URL the proxy will forward to.
                    returned: on success
                    type: str
                    sample: forward_example
        mirror:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                directory:
                    description:
                        - Path to the data volume on the management station where software source mirrors are stored.
                    returned: on success
                    type: str
                    sample: directory_example
                port:
                    description:
                        - Default mirror listening port for http.
                    returned: on success
                    type: str
                    sample: port_example
                sslport:
                    description:
                        - Default mirror listening port for https.
                    returned: on success
                    type: str
                    sample: sslport_example
                sslcert:
                    description:
                        - Path to the SSL cerfificate.
                    returned: on success
                    type: str
                    sample: sslcert_example
        health:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                state:
                    description:
                        - Overall health status of the management station.
                    returned: on success
                    type: str
                    sample: HEALTHY
                description:
                    description:
                        - Explanation of the health status.
                    returned: on success
                    type: str
                    sample: description_example
        lifecycle_state:
            description:
                - The current state of the management station.
            returned: on success
            type: str
            sample: CREATING
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_instance_id": "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "scheduled_job_id": "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx",
        "profile_id": "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "hostname": "hostname_example",
        "overall_state": "NORMAL",
        "overall_percentage": 56,
        "mirror_capacity": 56,
        "total_mirrors": 56,
        "mirror_sync_status": {
            "unsynced": 56,
            "queued": 56,
            "syncing": 56,
            "synced": 56,
            "failed": 56
        },
        "proxy": {
            "is_enabled": true,
            "hosts": [],
            "port": "port_example",
            "forward": "forward_example"
        },
        "mirror": {
            "directory": "directory_example",
            "port": "port_example",
            "sslport": "sslport_example",
            "sslcert": "sslcert_example"
        },
        "health": {
            "state": "HEALTHY",
            "description": "description_example"
        },
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import WorkRequestClient
    from oci.os_management_hub import ManagementStationClient
    from oci.os_management_hub.models import CreateManagementStationDetails
    from oci.os_management_hub.models import UpdateManagementStationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementStationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(ManagementStationHelperGen, self).get_possible_entity_types() + [
            "osmhmanagementstation",
            "osmhmanagementstations",
            "osManagementHubosmhmanagementstation",
            "osManagementHubosmhmanagementstations",
            "osmhmanagementstationresource",
            "osmhmanagementstationsresource",
            "managementstation",
            "managementstations",
            "osManagementHubmanagementstation",
            "osManagementHubmanagementstations",
            "managementstationresource",
            "managementstationsresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "management_station_id"

    def get_module_resource_id(self):
        return self.module.params.get("management_station_id")

    def get_get_fn(self):
        return self.client.get_management_station

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_station, management_station_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_station,
            management_station_id=self.module.params.get("management_station_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
            self.client.list_management_stations, **kwargs
        )

    def get_create_model_class(self):
        return CreateManagementStationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_management_station,
            call_fn_args=(),
            call_fn_kwargs=dict(create_management_station_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateManagementStationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_management_station,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_station_id=self.module.params.get("management_station_id"),
                update_management_station_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_management_station,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_station_id=self.module.params.get("management_station_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ManagementStationHelperCustom = get_custom_class("ManagementStationHelperCustom")


class ResourceHelper(ManagementStationHelperCustom, ManagementStationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            hostname=dict(type="str"),
            proxy=dict(
                type="dict",
                options=dict(
                    is_enabled=dict(type="bool", required=True),
                    hosts=dict(type="list", elements="str"),
                    port=dict(type="str"),
                    forward=dict(type="str"),
                ),
            ),
            mirror=dict(
                type="dict",
                options=dict(
                    directory=dict(type="str", required=True),
                    port=dict(type="str", required=True),
                    sslport=dict(type="str", required=True),
                    sslcert=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            management_station_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_station",
        service_client_class=ManagementStationClient,
        namespace="os_management_hub",
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
