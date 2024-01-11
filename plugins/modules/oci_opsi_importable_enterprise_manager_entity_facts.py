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
module: oci_opsi_importable_enterprise_manager_entity_facts
short_description: Fetches details about one or multiple ImportableEnterpriseManagerEntity resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ImportableEnterpriseManagerEntity resources in Oracle Cloud Infrastructure
    - Gets a list of importable entities for an Operations Insights Enterprise Manager bridge that have not been imported before.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    enterprise_manager_bridge_id:
        description:
            - Unique Enterprise Manager bridge identifier
        type: str
        required: true
    enterprise_manager_entity_type:
        description:
            - "Filter by one or more Enterprise Manager entity types. Currently, the supported types are \\"oracle_pdb\\", \\"oracle_database\\", \\"host\\",
              \\"oracle_dbmachine\\", \\"oracle_exa_cloud_service\\", and \\"oracle_oci_exadata_cloud_service\\". If this parameter is not specified, targets of
              all supported entity types are returned by default."
        type: list
        elements: str
    enterprise_manager_identifier:
        description:
            - Used in combination with enterpriseManagerParentEntityIdentifier to return the members of a particular Enterprise Manager parent entity. Both
              enterpriseManagerIdentifier and enterpriseManagerParentEntityIdentifier must be specified to identify a particular Enterprise Manager parent
              entity.
        type: str
    enterprise_manager_parent_entity_identifier:
        description:
            - Used in combination with enterpriseManagerIdentifier to return the members of a particular Enterprise Manager parent entity. Both
              enterpriseManagerIdentifier and enterpriseManagerParentEntityIdentifier must be specified to identify a particular  Enterprise Manager parent
              entity.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List importable_enterprise_manager_entities
  oci_opsi_importable_enterprise_manager_entity_facts:
    # required
    enterprise_manager_bridge_id: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    enterprise_manager_entity_type: [ "enterprise_manager_entity_type_example" ]
    enterprise_manager_identifier: enterprise_manager_identifier_example
    enterprise_manager_parent_entity_identifier: enterprise_manager_parent_entity_identifier_example

"""

RETURN = """
importable_enterprise_manager_entities:
    description:
        - List of ImportableEnterpriseManagerEntity resources
    returned: on success
    type: complex
    contains:
        enterprise_manager_identifier:
            description:
                - Enterprise Manager Unique Identifier
            returned: on success
            type: str
            sample: enterprise_manager_identifier_example
        enterprise_manager_entity_name:
            description:
                - Enterprise Manager Entity Name
            returned: on success
            type: str
            sample: enterprise_manager_entity_name_example
        enterprise_manager_entity_type:
            description:
                - Enterprise Manager Entity Type
            returned: on success
            type: str
            sample: enterprise_manager_entity_type_example
        enterprise_manager_entity_identifier:
            description:
                - Enterprise Manager Entity Unique Identifier
            returned: on success
            type: str
            sample: enterprise_manager_entity_identifier_example
        opsi_entity_type:
            description:
                - Operations Insights internal representation of the resource type.
            returned: on success
            type: str
            sample: opsi_entity_type_example
    sample: [{
        "enterprise_manager_identifier": "enterprise_manager_identifier_example",
        "enterprise_manager_entity_name": "enterprise_manager_entity_name_example",
        "enterprise_manager_entity_type": "enterprise_manager_entity_type_example",
        "enterprise_manager_entity_identifier": "enterprise_manager_entity_identifier_example",
        "opsi_entity_type": "opsi_entity_type_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ImportableEnterpriseManagerEntityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "enterprise_manager_bridge_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "enterprise_manager_entity_type",
            "enterprise_manager_identifier",
            "enterprise_manager_parent_entity_identifier",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_importable_enterprise_manager_entities,
            enterprise_manager_bridge_id=self.module.params.get(
                "enterprise_manager_bridge_id"
            ),
            **optional_kwargs
        )


ImportableEnterpriseManagerEntityFactsHelperCustom = get_custom_class(
    "ImportableEnterpriseManagerEntityFactsHelperCustom"
)


class ResourceFactsHelper(
    ImportableEnterpriseManagerEntityFactsHelperCustom,
    ImportableEnterpriseManagerEntityFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            enterprise_manager_bridge_id=dict(type="str", required=True),
            enterprise_manager_entity_type=dict(type="list", elements="str"),
            enterprise_manager_identifier=dict(type="str"),
            enterprise_manager_parent_entity_identifier=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="importable_enterprise_manager_entity",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(importable_enterprise_manager_entities=result)


if __name__ == "__main__":
    main()
