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
module: oci_logging_log_facts
short_description: Fetches details about one or multiple Log resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Log resources in Oracle Cloud Infrastructure
    - Lists the specified log group's log objects.
    - If I(log_id) is specified, the details of a single Log will be returned.
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
            - Required to get a specific log.
        type: str
        aliases: ["id"]
    log_type:
        description:
            - The logType that the log object is for, whether custom or service.
        type: str
        choices:
            - "CUSTOM"
            - "SERVICE"
    source_service:
        description:
            - Service that created the log object.
        type: str
    source_resource:
        description:
            - Log object resource.
        type: str
    display_name:
        description:
            - Resource name
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Lifecycle state of the log object
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "INACTIVE"
            - "DELETING"
            - "FAILED"
    sort_by:
        description:
            - The field to sort by (one column only). Default sort order is
              ascending exception of `timeCreated` and `timeLastModified` columns (descending).
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List logs
  oci_logging_log_facts:
    log_group_id: ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific log
  oci_logging_log_facts:
    log_group_id: ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx
    log_id: ocid1.log.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
logs:
    description:
        - List of Log resources
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
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.logging import LoggingManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "log_group_id",
            "log_id",
        ]

    def get_required_params_for_list(self):
        return [
            "log_group_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log,
            log_group_id=self.module.params.get("log_group_id"),
            log_id=self.module.params.get("log_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "log_type",
            "source_service",
            "source_resource",
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_logs,
            log_group_id=self.module.params.get("log_group_id"),
            **optional_kwargs
        )


LogFactsHelperCustom = get_custom_class("LogFactsHelperCustom")


class ResourceFactsHelper(LogFactsHelperCustom, LogFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            log_group_id=dict(type="str", required=True),
            log_id=dict(aliases=["id"], type="str"),
            log_type=dict(type="str", choices=["CUSTOM", "SERVICE"]),
            source_service=dict(type="str"),
            source_resource=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "INACTIVE",
                    "DELETING",
                    "FAILED",
                ],
            ),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log",
        service_client_class=LoggingManagementClient,
        namespace="logging",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(logs=result)


if __name__ == "__main__":
    main()
