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
module: oci_os_management_hub_managed_instance_group
short_description: Manage a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new managed instance group.
    - "This resource has the following action operations in the M(oracle.oci.oci_os_management_hub_managed_instance_group_actions) module:
      attach_managed_instances, attach_software_sources, change_compartment, detach_managed_instances, detach_software_sources, disable_module_stream,
      enable_module_stream, install_module_stream_profile, install_packages, install_windows_updates, manage_module_streams, remove_module_stream_profile,
      remove_packages, switch_module_stream, update_all_packages."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the managed instance
              group.
            - Required for create using I(state=present).
        type: str
    os_family:
        description:
            - The operating system type of the managed instances that will be attached to this group.
            - Required for create using I(state=present).
        type: str
        choices:
            - "ORACLE_LINUX_9"
            - "ORACLE_LINUX_8"
            - "ORACLE_LINUX_7"
            - "ORACLE_LINUX_6"
            - "WINDOWS_SERVER_2016"
            - "WINDOWS_SERVER_2019"
            - "WINDOWS_SERVER_2022"
            - "ALL"
    arch_type:
        description:
            - The CPU architecture type of the managed instances that will be attached to this group.
            - Required for create using I(state=present).
        type: str
        choices:
            - "X86_64"
            - "AARCH64"
            - "I686"
            - "NOARCH"
            - "SRC"
    vendor_name:
        description:
            - The vendor of the operating system that will be used by the managed instances in the group.
            - Required for create using I(state=present).
        type: str
        choices:
            - "ORACLE"
            - "MICROSOFT"
    location:
        description:
            - The location of managed instances attached to the group. If no location is provided, the default is on premises.
        type: str
        choices:
            - "ON_PREMISE"
            - "OCI_COMPUTE"
            - "AZURE"
            - "EC2"
            - "GCP"
    software_source_ids:
        description:
            - The list of software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) available to the managed
              instances in the group.
        type: list
        elements: str
    managed_instance_ids:
        description:
            - The list of managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) to be added to the group.
        type: list
        elements: str
    display_name:
        description:
            - A user-friendly name for the managed instance group. Does not have to be unique and you can change the name later. Avoid entering confidential
              information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User-specified description of the managed instance group. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    notification_topic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Oracle Notifications service (ONS) topic. ONS is
              the channel used to send notifications to the customer.
            - This parameter is updatable.
        type: str
    autonomous_settings:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_data_collection_authorized:
                description:
                    - Indicates whether Autonomous Linux will collect crash files.
                type: bool
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
    managed_instance_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ManagedInstanceGroup.
            - Use I(state=present) to create or update a ManagedInstanceGroup.
            - Use I(state=absent) to delete a ManagedInstanceGroup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create managed_instance_group
  oci_os_management_hub_managed_instance_group:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    os_family: ORACLE_LINUX_9
    arch_type: X86_64
    vendor_name: ORACLE
    display_name: display_name_example

    # optional
    location: ON_PREMISE
    software_source_ids: [ "software_source_ids_example" ]
    managed_instance_ids: [ "managed_instance_ids_example" ]
    description: description_example
    notification_topic_id: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_settings:
      # optional
      is_data_collection_authorized: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update managed_instance_group
  oci_os_management_hub_managed_instance_group:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    notification_topic_id: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_settings:
      # optional
      is_data_collection_authorized: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update managed_instance_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_managed_instance_group:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    notification_topic_id: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_settings:
      # optional
      is_data_collection_authorized: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete managed_instance_group
  oci_os_management_hub_managed_instance_group:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete managed_instance_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_os_management_hub_managed_instance_group:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
managed_instance_group:
    description:
        - Details of the ManagedInstanceGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the managed instance
                  group.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the managed instance group.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-specified information about the managed instance group.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The time the managed instance group was created (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_modified:
            description:
                - The time the managed instance group was last modified (in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) format).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the managed instance group.
            returned: on success
            type: str
            sample: CREATING
        os_family:
            description:
                - The operating system type of the instances in the managed instance group.
            returned: on success
            type: str
            sample: ORACLE_LINUX_9
        arch_type:
            description:
                - The CPU architecture of the instances in the managed instance group.
            returned: on success
            type: str
            sample: X86_64
        vendor_name:
            description:
                - The vendor of the operating system used by the managed instances in the group.
            returned: on success
            type: str
            sample: ORACLE
        software_source_ids:
            description:
                - The list of software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that the managed instance
                  group will use.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Software source name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Software source description.
                    returned: on success
                    type: str
                    sample: description_example
                software_source_type:
                    description:
                        - Type of the software source.
                    returned: on success
                    type: str
                    sample: VENDOR
                is_mandatory_for_autonomous_linux:
                    description:
                        - Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can't unselect it.
                    returned: on success
                    type: bool
                    sample: true
        software_sources:
            description:
                - The list of software sources that the managed instance group will use.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Software source name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Software source description.
                    returned: on success
                    type: str
                    sample: description_example
                software_source_type:
                    description:
                        - Type of the software source.
                    returned: on success
                    type: str
                    sample: VENDOR
                is_mandatory_for_autonomous_linux:
                    description:
                        - Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can't unselect it.
                    returned: on success
                    type: bool
                    sample: true
        managed_instance_ids:
            description:
                - The list of managed instance L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) attached to the managed
                  instance group.
            returned: on success
            type: list
            sample: []
        managed_instance_count:
            description:
                - The number of managed instances in the group.
            returned: on success
            type: int
            sample: 56
        location:
            description:
                - The location of managed instances attached to the group.
            returned: on success
            type: str
            sample: ON_PREMISE
        pending_job_count:
            description:
                - The number of scheduled jobs pending against the managed instance group.
            returned: on success
            type: int
            sample: 56
        notification_topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Oracle Notifications service (ONS) topic. ONS
                  is the channel used to send notifications to the customer.
            returned: on success
            type: str
            sample: "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_data_collection_authorized:
                    description:
                        - Indicates whether Autonomous Linux will collect crash files. This setting can be changed by the user.
                    returned: on success
                    type: bool
                    sample: true
                scheduled_job_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the restricted scheduled job associated
                          with this instance. This value cannot be deleted by the user.
                    returned: on success
                    type: str
                    sample: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        is_managed_by_autonomous_linux:
            description:
                - Indicates whether the Autonomous Linux service manages the group.
            returned: on success
            type: bool
            sample: true
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_modified": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "os_family": "ORACLE_LINUX_9",
        "arch_type": "X86_64",
        "vendor_name": "ORACLE",
        "software_source_ids": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "software_sources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "software_source_type": "VENDOR",
            "is_mandatory_for_autonomous_linux": true
        }],
        "managed_instance_ids": [],
        "managed_instance_count": 56,
        "location": "ON_PREMISE",
        "pending_job_count": 56,
        "notification_topic_id": "ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_settings": {
            "is_data_collection_authorized": true,
            "scheduled_job_id": "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_managed_by_autonomous_linux": true,
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
    from oci.os_management_hub import ManagedInstanceGroupClient
    from oci.os_management_hub.models import CreateManagedInstanceGroupDetails
    from oci.os_management_hub.models import UpdateManagedInstanceGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceGroupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(
            ManagedInstanceGroupHelperGen, self
        ).get_possible_entity_types() + [
            "managedinstancegroup",
            "managedinstancegroups",
            "osManagementHubmanagedinstancegroup",
            "osManagementHubmanagedinstancegroups",
            "managedinstancegroupresource",
            "managedinstancegroupsresource",
            "osmanagementhub",
        ]

    def get_module_resource_id_param(self):
        return "managed_instance_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_instance_group_id")

    def get_get_fn(self):
        return self.client.get_managed_instance_group

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance_group,
            managed_instance_group_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_instance_group,
            managed_instance_group_id=self.module.params.get(
                "managed_instance_group_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "managed_instance_group_id",
            "arch_type",
            "os_family",
        ]

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
            self.client.list_managed_instance_groups, **kwargs
        )

    def get_create_model_class(self):
        return CreateManagedInstanceGroupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(create_managed_instance_group_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateManagedInstanceGroupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
                update_managed_instance_group_details=update_details,
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
            call_fn=self.client.delete_managed_instance_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_instance_group_id=self.module.params.get(
                    "managed_instance_group_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ManagedInstanceGroupHelperCustom = get_custom_class("ManagedInstanceGroupHelperCustom")


class ResourceHelper(ManagedInstanceGroupHelperCustom, ManagedInstanceGroupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            os_family=dict(
                type="str",
                choices=[
                    "ORACLE_LINUX_9",
                    "ORACLE_LINUX_8",
                    "ORACLE_LINUX_7",
                    "ORACLE_LINUX_6",
                    "WINDOWS_SERVER_2016",
                    "WINDOWS_SERVER_2019",
                    "WINDOWS_SERVER_2022",
                    "ALL",
                ],
            ),
            arch_type=dict(
                type="str", choices=["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
            ),
            vendor_name=dict(type="str", choices=["ORACLE", "MICROSOFT"]),
            location=dict(
                type="str", choices=["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]
            ),
            software_source_ids=dict(type="list", elements="str"),
            managed_instance_ids=dict(type="list", elements="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            notification_topic_id=dict(type="str"),
            autonomous_settings=dict(
                type="dict",
                options=dict(is_data_collection_authorized=dict(type="bool")),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            managed_instance_group_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_instance_group",
        service_client_class=ManagedInstanceGroupClient,
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
