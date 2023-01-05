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
module: oci_logging_log_group_facts
short_description: Fetches details about one or multiple LogGroup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LogGroup resources in Oracle Cloud Infrastructure
    - Lists all log groups for the specified compartment or tenancy.
    - If I(log_group_id) is specified, the details of a single LogGroup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    log_group_id:
        description:
            - OCID of a log group to work with.
            - Required to get a specific log_group.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - Compartment OCID to list resources in. See compartmentIdInSubtree
                   for nested compartments traversal.
            - Required to list multiple log_groups.
        type: str
    is_compartment_id_in_subtree:
        description:
            - Specifies whether or not nested compartments should be traversed. Defaults to false.
        type: bool
    display_name:
        description:
            - Resource name
        type: str
        aliases: ["name"]
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
- name: Get a specific log_group
  oci_logging_log_group_facts:
    # required
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"

- name: List log_groups
  oci_logging_log_group_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_compartment_id_in_subtree: true
    display_name: display_name_example
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
log_groups:
    description:
        - List of LogGroup resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that the resource belongs to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly display name. This must be unique within the enclosing resource,
                  and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description for this resource.
            returned: on success
            type: str
            sample: description_example
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
        time_created:
            description:
                - Time the resource was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_modified:
            description:
                - Time the resource was last modified.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The log group object state.
            returned: on success
            type: str
            sample: CREATING
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_modified": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.logging import LoggingManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogGroupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "log_group_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_group,
            log_group_id=self.module.params.get("log_group_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "is_compartment_id_in_subtree",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_log_groups,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LogGroupFactsHelperCustom = get_custom_class("LogGroupFactsHelperCustom")


class ResourceFactsHelper(LogGroupFactsHelperCustom, LogGroupFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            log_group_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            is_compartment_id_in_subtree=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_group",
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

    module.exit_json(log_groups=result)


if __name__ == "__main__":
    main()
