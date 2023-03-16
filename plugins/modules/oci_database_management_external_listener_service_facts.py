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
module: oci_database_management_external_listener_service_facts
short_description: Fetches details about one or multiple ExternalListenerService resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalListenerService resources in Oracle Cloud Infrastructure
    - Lists the database services registered with the specified external listener
      for the specified Managed Database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_listener_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external listener.
        type: str
        required: true
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The
              default sort order for `NAME` is ascending and it is case-sensitive.
        type: str
        choices:
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List external_listener_services
  oci_database_management_external_listener_service_facts:
    # required
    external_listener_id: "ocid1.externallistener.oc1..xxxxxxEXAMPLExxxxxx"
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: NAME
    sort_order: ASC

"""

RETURN = """
external_listener_services:
    description:
        - List of ExternalListenerService resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the service.
            returned: on success
            type: str
            sample: name_example
        listener_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external listener.
            returned: on success
            type: str
            sample: "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx"
        managed_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
            returned: on success
            type: str
            sample: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "name": "name_example",
        "listener_id": "ocid1.listener.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_database_id": "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalListenerServiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "external_listener_id",
            "managed_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_external_listener_services,
            external_listener_id=self.module.params.get("external_listener_id"),
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


ExternalListenerServiceFactsHelperCustom = get_custom_class(
    "ExternalListenerServiceFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalListenerServiceFactsHelperCustom, ExternalListenerServiceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_listener_id=dict(type="str", required=True),
            managed_database_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_listener_service",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_listener_services=result)


if __name__ == "__main__":
    main()
