#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_database_management_db_management_private_endpoint_facts
short_description: Fetches details about one or multiple DbManagementPrivateEndpoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbManagementPrivateEndpoint resources in Oracle Cloud Infrastructure
    - Gets a list of Database Management private endpoints.
    - If I(db_management_private_endpoint_id) is specified, the details of a single DbManagementPrivateEndpoint will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_management_private_endpoint_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Management private endpoint.
            - Required to get a specific db_management_private_endpoint.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple db_management_private_endpoints.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire name.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
    is_cluster:
        description:
            - The option to filter Database Management private endpoints that can used for Oracle Databases in a cluster. This should be used along with the
              vcnId query parameter.
        type: bool
    lifecycle_state:
        description:
            - The lifecycle state of a resource.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for 'TIMECREATED' is descending and the default sort order for 'NAME' is ascending.
              The 'NAME' sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific db_management_private_endpoint
  oci_database_management_db_management_private_endpoint_facts:
    # required
    db_management_private_endpoint_id: "ocid1.dbmanagementprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: List db_management_private_endpoints
  oci_database_management_db_management_private_endpoint_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    is_cluster: true
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
db_management_private_endpoints:
    description:
        - List of DbManagementPrivateEndpoint resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Management private endpoint.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The display name of the Database Management private endpoint.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_cluster:
            description:
                - Specifies whether the Database Management private endpoint can be used for Oracle Databases in a cluster.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        private_ip:
            description:
                - The IP addresses assigned to the Database Management private endpoint.
                - Returned for get operation
            returned: on success
            type: str
            sample: private_ip_example
        description:
            description:
                - The description of the Database Management private endpoint.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time the Database Managament private endpoint was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the Database Management private endpoint.
            returned: on success
            type: str
            sample: CREATING
        nsg_ids:
            description:
                - The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cluster": true,
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "private_ip": "private_ip_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "nsg_ids": []
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbManagementPrivateEndpointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_management_private_endpoint_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_management_private_endpoint,
            db_management_private_endpoint_id=self.module.params.get(
                "db_management_private_endpoint_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "vcn_id",
            "is_cluster",
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
            self.client.list_db_management_private_endpoints,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DbManagementPrivateEndpointFactsHelperCustom = get_custom_class(
    "DbManagementPrivateEndpointFactsHelperCustom"
)


class ResourceFactsHelper(
    DbManagementPrivateEndpointFactsHelperCustom,
    DbManagementPrivateEndpointFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_management_private_endpoint_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            vcn_id=dict(type="str"),
            is_cluster=dict(type="bool"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_management_private_endpoint",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_management_private_endpoints=result)


if __name__ == "__main__":
    main()
