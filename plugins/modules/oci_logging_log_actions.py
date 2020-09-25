#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_logging_log_actions
short_description: Perform actions on a Log resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Log resource in Oracle Cloud Infrastructure
    - For I(action=change_log_log_group), moves a log into a different log group within the same tenancy.  When provided, If-Match is checked against ETag
      values of the resource.
version_added: "2.9"
author: Oracle (@oracle)
options:
    log_group_id:
        description:
            - OCID of a log group to work with.
        type: str
        required: true
    log_id:
        description:
            - OCID of a log to work with.
        type: str
        aliases: ["id"]
        required: true
    target_log_group_id:
        description:
            - Log group OCID.
        type: str
    action:
        description:
            - The action to perform on the Log.
        type: str
        required: true
        choices:
            - "change_log_log_group"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_log_log_group on log
  oci_logging_log_actions:
    log_group_id: ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx
    log_id: ocid1.log.oc1..xxxxxxEXAMPLExxxxxx
    action: change_log_log_group

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
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        tenancy_id:
            description:
                - The OCID of the tenancy.
            returned: on success
            type: string
            sample: ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx
        log_group_id:
            description:
                - Log group OCID.
            returned: on success
            type: string
            sample: ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The display name of a user-friendly name. It has to be unique within enclosing resource,
                  and it's changeable. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        log_type:
            description:
                - The logType that the log object is for, custom or service.
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
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        source_type:
                            description:
                                - "The source of the log.
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
                - The state of an pipeline.
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
                - Log retention duration in days.
            returned: on success
            type: int
            sample: 56
        compartment_id:
            description:
                - The OCID of the compartment that the resource belongs to.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.logging import LoggingManagementClient
    from oci.logging.models import ChangeLogLogGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_log_log_group
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def change_log_log_group(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeLogLogGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_log_log_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                log_group_id=self.module.params.get("log_group_id"),
                log_id=self.module.params.get("log_id"),
                change_log_log_group_details=action_details,
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


LogActionsHelperCustom = get_custom_class("LogActionsHelperCustom")


class ResourceHelper(LogActionsHelperCustom, LogActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            log_group_id=dict(type="str", required=True),
            log_id=dict(aliases=["id"], type="str", required=True),
            target_log_group_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_log_log_group"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
