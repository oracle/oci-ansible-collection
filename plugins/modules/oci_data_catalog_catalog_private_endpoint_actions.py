#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_data_catalog_catalog_private_endpoint_actions
short_description: Perform actions on a CatalogPrivateEndpoint resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CatalogPrivateEndpoint resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the
      resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The identifier of the compartment where the resource should be moved.
        type: str
        required: true
    catalog_private_endpoint_id:
        description:
            - Unique private reverse connection identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the CatalogPrivateEndpoint.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on catalog_private_endpoint
  oci_data_catalog_catalog_private_endpoint_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    catalog_private_endpoint_id: "ocid1.catalogprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
catalog_private_endpoint:
    description:
        - Details of the CatalogPrivateEndpoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - Subnet Identifier
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Private Reverse Connection Endpoint display name
            returned: on success
            type: str
            sample: display_name_example
        dns_zones:
            description:
                - "List of DNS zones to be used by the data assets to be harvested.
                  Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com"
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The time the private endpoint was created. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the private endpoint was updated. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        lifecycle_state:
            description:
                - The current state of the private endpoint resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed'
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        attached_catalogs:
            description:
                - The list of catalogs using the private reverse connection endpoint
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "dns_zones": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "attached_catalogs": []
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.data_catalog import DataCatalogClient
    from oci.data_catalog.models import ChangeCatalogPrivateEndpointCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogCatalogPrivateEndpointActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "catalog_private_endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("catalog_private_endpoint_id")

    def get_get_fn(self):
        return self.client.get_catalog_private_endpoint

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_catalog_private_endpoint,
            catalog_private_endpoint_id=self.module.params.get(
                "catalog_private_endpoint_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCatalogPrivateEndpointCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_catalog_private_endpoint_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_catalog_private_endpoint_compartment_details=action_details,
                catalog_private_endpoint_id=self.module.params.get(
                    "catalog_private_endpoint_id"
                ),
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


DataCatalogCatalogPrivateEndpointActionsHelperCustom = get_custom_class(
    "DataCatalogCatalogPrivateEndpointActionsHelperCustom"
)


class ResourceHelper(
    DataCatalogCatalogPrivateEndpointActionsHelperCustom,
    DataCatalogCatalogPrivateEndpointActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            catalog_private_endpoint_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="catalog_private_endpoint",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
