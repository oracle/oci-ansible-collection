#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_logging_log
short_description: Manage a Log resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Log resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a log within the specified log group. This call fails if a log group has already been created
      with the same displayName or (service, resource, category) triplet.
    - "This resource has the following action operations in the M(oci_log_actions) module: change_log_log_group."
version_added: "2.9"
author: Oracle (@oracle)
options:
    log_group_id:
        description:
            - OCID of a log group to work with.
        type: str
        required: true
    display_name:
        description:
            - The user-friendly display name. This must be unique within the enclosing resource,
              and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    log_type:
        description:
            - The logType that the log object is for, whether custom or service.
            - Required for create using I(state=present).
        type: str
        choices:
            - "CUSTOM"
            - "SERVICE"
    is_enabled:
        description:
            - Whether or not this resource is currently enabled.
            - This parameter is updatable.
        type: bool
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    configuration:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            compartment_id:
                description:
                    - The OCID of the compartment that the resource belongs to.
                type: str
            source:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    source_type:
                        description:
                            - "The log source.
                              * **OCISERVICE:** Oracle Service."
                        type: str
                        choices:
                            - "OCISERVICE"
                    service:
                        description:
                            - Service generating log.
                        type: str
                    resource:
                        description:
                            - The unique identifier of the resource emitting the log.
                        type: str
                    category:
                        description:
                            - Log object category.
                        type: str
                    parameters:
                        description:
                            - Log category parameters are stored here.
                            - This parameter is updatable.
                        type: dict
            archiving:
                description:
                    - ""
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - True if archiving enabled. This field is now decrecated, you should use cloud flow to enable archiving.
                        type: bool
    retention_duration:
        description:
            - Log retention duration in 30-day increments (30, 60, 90 and so on).
            - This parameter is updatable.
        type: int
    log_id:
        description:
            - OCID of a log to work with.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Log.
            - Use I(state=present) to create or update a Log.
            - Use I(state=absent) to delete a Log.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create log
  oci_logging_log:
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    log_type: CUSTOM

- name: Update log using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_logging_log:
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    is_enabled: true
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    retention_duration: 56

- name: Update log
  oci_logging_log:
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete log
  oci_logging_log:
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete log using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_logging_log:
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
log:
    description:
        - Details of the Log resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        tenancy_id:
            description:
                - The OCID of the tenancy.
            returned: on success
            type: string
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        log_group_id:
            description:
                - Log group OCID.
            returned: on success
            type: string
            sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly display name. This must be unique within the enclosing resource,
                  and it's changeable. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        log_type:
            description:
                - The logType that the log object is for, whether custom or service.
            returned: on success
            type: string
            sample: CUSTOM
        is_enabled:
            description:
                - Whether or not this resource is currently enabled.
            returned: on success
            type: bool
            sample: true
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                compartment_id:
                    description:
                        - The OCID of the compartment that the resource belongs to.
                    returned: on success
                    type: string
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        source_type:
                            description:
                                - "The log source.
                                  * **OCISERVICE:** Oracle Service."
                            returned: on success
                            type: string
                            sample: OCISERVICE
                        service:
                            description:
                                - Service generating log.
                            returned: on success
                            type: string
                            sample: service_example
                        resource:
                            description:
                                - The unique identifier of the resource emitting the log.
                            returned: on success
                            type: string
                            sample: resource_example
                        category:
                            description:
                                - Log object category.
                            returned: on success
                            type: string
                            sample: category_example
                        parameters:
                            description:
                                - Log category parameters are stored here.
                            returned: on success
                            type: dict
                            sample: {}
                archiving:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - True if archiving enabled. This field is now decrecated, you should use cloud flow to enable archiving.
                            returned: on success
                            type: bool
                            sample: true
        lifecycle_state:
            description:
                - The pipeline state.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - Time the resource was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_modified:
            description:
                - Time the resource was last modified.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        retention_duration:
            description:
                - Log retention duration in 30-day increments (30, 60, 90 and so on).
            returned: on success
            type: int
            sample: 56
        compartment_id:
            description:
                - The OCID of the compartment that the resource belongs to.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "log_type": "CUSTOM",
        "is_enabled": true,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "configuration": {
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "source": {
                "source_type": "OCISERVICE",
                "service": "service_example",
                "resource": "resource_example",
                "category": "category_example",
                "parameters": {}
            },
            "archiving": {
                "is_enabled": true
            }
        },
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_modified": "2013-10-20T19:20:30+01:00",
        "retention_duration": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.logging import LoggingManagementClient
    from oci.logging.models import CreateLogDetails
    from oci.logging.models import UpdateLogDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "log_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_id")

    def get_get_fn(self):
        return self.client.get_log

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log,
            log_group_id=self.module.params.get("log_group_id"),
            log_id=self.module.params.get("log_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "log_group_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["log_type", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_logs, **kwargs)

    def get_create_model_class(self):
        return CreateLogDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_log,
            call_fn_args=(),
            call_fn_kwargs=dict(
                log_group_id=self.module.params.get("log_group_id"),
                create_log_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateLogDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_log,
            call_fn_args=(),
            call_fn_kwargs=dict(
                log_group_id=self.module.params.get("log_group_id"),
                log_id=self.module.params.get("log_id"),
                update_log_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_log,
            call_fn_args=(),
            call_fn_kwargs=dict(
                log_group_id=self.module.params.get("log_group_id"),
                log_id=self.module.params.get("log_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


LogHelperCustom = get_custom_class("LogHelperCustom")


class ResourceHelper(LogHelperCustom, LogHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            log_group_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            log_type=dict(type="str", choices=["CUSTOM", "SERVICE"]),
            is_enabled=dict(type="bool"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            configuration=dict(
                type="dict",
                options=dict(
                    compartment_id=dict(type="str"),
                    source=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            source_type=dict(type="str", choices=["OCISERVICE"]),
                            service=dict(type="str"),
                            resource=dict(type="str"),
                            category=dict(type="str"),
                            parameters=dict(type="dict"),
                        ),
                    ),
                    archiving=dict(
                        type="dict", options=dict(is_enabled=dict(type="bool"))
                    ),
                ),
            ),
            retention_duration=dict(type="int"),
            log_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log",
        service_client_class=LoggingManagementClient,
        namespace="logging",
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
