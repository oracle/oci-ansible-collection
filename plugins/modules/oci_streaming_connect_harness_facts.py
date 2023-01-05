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
module: oci_streaming_connect_harness_facts
short_description: Fetches details about one or multiple ConnectHarness resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ConnectHarness resources in Oracle Cloud Infrastructure
    - Lists the connectharness.
    - If I(connect_harness_id) is specified, the details of a single ConnectHarness will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connect_harness_id:
        description:
            - The OCID of the connect harness.
            - Required to get a specific connect_harness.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple connect_harness.
        type: str
    name:
        description:
            - A filter to return only resources that match the given name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide no more than one sort order. By default, `TIMECREATED` sorts results in descending order and `NAME` sorts
              results in ascending order.
        type: str
        choices:
            - "NAME"
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "UPDATING"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific connect_harness
  oci_streaming_connect_harness_facts:
    # required
    connect_harness_id: "ocid1.connectharness.oc1..xxxxxxEXAMPLExxxxxx"

- name: List connect_harness
  oci_streaming_connect_harness_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_by: NAME
    sort_order: ASC
    lifecycle_state: CREATING

"""

RETURN = """
connect_harness:
    description:
        - List of ConnectHarness resources
    returned: on success
    type: complex
    contains:
        lifecycle_state_details:
            description:
                - Any additional details about the current state of the connect harness.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_state_details_example
        name:
            description:
                - The name of the connect harness. Avoid entering confidential information.
                - "Example: `JDBCConnector`"
            returned: on success
            type: str
            sample: name_example
        id:
            description:
                - The OCID of the connect harness.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the connect harness.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the connect harness.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the connect harness was created, expressed in in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2018-04-20T00:00:07.405Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-
                  compatibility only.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}'"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "lifecycle_state_details": "lifecycle_state_details_example",
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.streaming import StreamAdminClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectHarnessFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "connect_harness_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connect_harness,
            connect_harness_id=self.module.params.get("connect_harness_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_connect_harnesses,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ConnectHarnessFactsHelperCustom = get_custom_class("ConnectHarnessFactsHelperCustom")


class ResourceFactsHelper(
    ConnectHarnessFactsHelperCustom, ConnectHarnessFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            connect_harness_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["NAME", "TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "UPDATING",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="connect_harness",
        service_client_class=StreamAdminClient,
        namespace="streaming",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(connect_harness=result)


if __name__ == "__main__":
    main()
