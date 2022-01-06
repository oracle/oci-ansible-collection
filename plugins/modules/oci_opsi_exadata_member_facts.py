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
module: oci_opsi_exadata_member_facts
short_description: Fetches details about one or multiple ExadataMember resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExadataMember resources in Oracle Cloud Infrastructure
    - Lists the software and hardware inventory of the Exadata System.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    exadata_insight_id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of exadata insight resource.
        type: str
        required: true
    exadata_type:
        description:
            - Filter by one or more Exadata types.
              Possible value are DBMACHINE, EXACS, and EXACC.
        type: list
        elements: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The order in which exadata member records are listed
        type: str
        choices:
            - "name"
            - "displayName"
            - "entityType"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List exadata_members
  oci_opsi_exadata_member_facts:
    # required
    exadata_insight_id: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    exadata_type: [ "exadata_type_example" ]
    sort_order: ASC
    sort_by: name

"""

RETURN = """
exadata_members:
    description:
        - List of ExadataMember resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Name of exadata member target
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Display Name of exadata member target
            returned: on success
            type: str
            sample: display_name_example
        entity_type:
            description:
                - Entity type of exadata member target
            returned: on success
            type: str
            sample: DATABASE
    sample: [{
        "name": "name_example",
        "display_name": "display_name_example",
        "entity_type": "DATABASE"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataMemberFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "exadata_insight_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "exadata_type",
            "sort_order",
            "sort_by",
            "name",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_exadata_members,
            exadata_insight_id=self.module.params.get("exadata_insight_id"),
            **optional_kwargs
        )


ExadataMemberFactsHelperCustom = get_custom_class("ExadataMemberFactsHelperCustom")


class ResourceFactsHelper(ExadataMemberFactsHelperCustom, ExadataMemberFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            exadata_insight_id=dict(type="str", required=True),
            exadata_type=dict(type="list", elements="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name", "displayName", "entityType"]),
            name=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="exadata_member",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(exadata_members=result)


if __name__ == "__main__":
    main()
