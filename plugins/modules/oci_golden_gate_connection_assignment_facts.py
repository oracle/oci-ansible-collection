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
module: oci_golden_gate_connection_assignment_facts
short_description: Fetches details about one or multiple ConnectionAssignment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ConnectionAssignment resources in Oracle Cloud Infrastructure
    - Lists the Connection Assignments in the compartment.
    - If I(connection_assignment_id) is specified, the details of a single ConnectionAssignment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_assignment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Connection Assignment.
            - Required to get a specific connection_assignment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment that contains the work request. Work requests should be scoped
              to the same compartment as the resource the work request affects. If the work request concerns
              multiple resources, and those resources are not in the same compartment, it is up to the service team
              to pick the primary resource whose compartment should be used.
            - Required to list multiple connection_assignments.
        type: str
    deployment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment in which to list resources.
        type: str
    connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection.
        type: str
    name:
        description:
            - The name of the connection in the assignment (aliasName).
        type: str
    lifecycle_state:
        description:
            - A filter to return only connection assignments having the 'lifecycleState' given.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "FAILED"
            - "UPDATING"
            - "DELETING"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is
              descending.  Default order for 'displayName' is ascending. If no value is specified
              timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific connection_assignment
  oci_golden_gate_connection_assignment_facts:
    # required
    connection_assignment_id: "ocid1.connectionassignment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List connection_assignments
  oci_golden_gate_connection_assignment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
connection_assignments:
    description:
        - List of ConnectionAssignment resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection assignment being
                  referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        connection_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection being
                  referenced.
            returned: on success
            type: str
            sample: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        alias_name:
            description:
                - Credential store alias.
            returned: on success
            type: str
            sample: alias_name_example
        lifecycle_state:
            description:
                - Possible lifecycle states for connection assignments.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The time the resource was created. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_id": "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "alias_name": "alias_name_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionAssignmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "connection_assignment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection_assignment,
            connection_assignment_id=self.module.params.get("connection_assignment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "deployment_id",
            "connection_id",
            "name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_connection_assignments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ConnectionAssignmentFactsHelperCustom = get_custom_class(
    "ConnectionAssignmentFactsHelperCustom"
)


class ResourceFactsHelper(
    ConnectionAssignmentFactsHelperCustom, ConnectionAssignmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            connection_assignment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            deployment_id=dict(type="str"),
            connection_id=dict(type="str"),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="connection_assignment",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(connection_assignments=result)


if __name__ == "__main__":
    main()
