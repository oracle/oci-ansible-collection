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
module: oci_data_catalog_catalog_actions
short_description: Perform actions on a Catalog resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Catalog resource in Oracle Cloud Infrastructure
    - For I(action=attach_catalog_private_endpoint), attaches a private reverse connection endpoint resource to a data catalog resource. When provided, 'If-
      Match' is checked against 'ETag' values of the resource.
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the
      resource.
    - For I(action=detach_catalog_private_endpoint), detaches a private reverse connection endpoint resource to a data catalog resource. When provided, 'If-
      Match' is checked against 'ETag' values of the resource.
    - For I(action=object_stats), returns stats on objects by type in the repository.
    - For I(action=users), returns active users in the system.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The identifier of the compartment where the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    catalog_private_endpoint_id:
        description:
            - The identifier of the private endpoint to be attached to the catalog resource.
            - Required for I(action=attach_catalog_private_endpoint), I(action=detach_catalog_private_endpoint).
        type: str
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        aliases: ["id"]
        required: true
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
            - Applicable only for I(action=object_stats)I(action=users).
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
            - Applicable only for I(action=object_stats)I(action=users).
        type: str
        choices:
            - "ASC"
            - "DESC"
    action:
        description:
            - The action to perform on the Catalog.
        type: str
        required: true
        choices:
            - "attach_catalog_private_endpoint"
            - "change_compartment"
            - "detach_catalog_private_endpoint"
            - "object_stats"
            - "users"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action attach_catalog_private_endpoint on catalog
  oci_data_catalog_catalog_actions:
    # required
    catalog_private_endpoint_id: "ocid1.catalogprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    action: attach_catalog_private_endpoint

- name: Perform action change_compartment on catalog
  oci_data_catalog_catalog_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action detach_catalog_private_endpoint on catalog
  oci_data_catalog_catalog_actions:
    # required
    catalog_private_endpoint_id: "ocid1.catalogprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    action: detach_catalog_private_endpoint

- name: Perform action object_stats on catalog
  oci_data_catalog_catalog_actions:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    action: object_stats

    # optional
    sort_by: TIMECREATED
    sort_order: ASC

- name: Perform action users on catalog
  oci_data_catalog_catalog_actions:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    action: users

    # optional
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
catalog:
    description:
        - Details of the Catalog resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the data catalog instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Data catalog identifier, which can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the data catalog was created. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the data catalog was updated. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        service_api_url:
            description:
                - The REST front endpoint URL to the data catalog instance.
            returned: on success
            type: str
            sample: service_api_url_example
        service_console_url:
            description:
                - The console front endpoint URL to the data catalog instance.
            returned: on success
            type: str
            sample: service_console_url_example
        number_of_objects:
            description:
                - The number of data objects added to the data catalog.
                  Please see the data catalog documentation for further information on how this is calculated.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the data catalog resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - An message describing the current state in more detail.
                  For example, it can be used to provide actionable information for a resource in 'Failed' state.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        attached_catalog_private_endpoints:
            description:
                - The list of private reverse connection endpoints attached to the catalog
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "service_api_url": "service_api_url_example",
        "service_console_url": "service_console_url_example",
        "number_of_objects": 56,
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "attached_catalog_private_endpoints": []
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
    from oci.data_catalog.models import AttachCatalogPrivateEndpointDetails
    from oci.data_catalog.models import ChangeCatalogCompartmentDetails
    from oci.data_catalog.models import DetachCatalogPrivateEndpointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogCatalogActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_catalog_private_endpoint
        change_compartment
        detach_catalog_private_endpoint
        object_stats
        users
    """

    @staticmethod
    def get_module_resource_id_param():
        return "catalog_id"

    def get_module_resource_id(self):
        return self.module.params.get("catalog_id")

    def get_get_fn(self):
        return self.client.get_catalog

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_catalog, catalog_id=self.module.params.get("catalog_id"),
        )

    def attach_catalog_private_endpoint(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachCatalogPrivateEndpointDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_catalog_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                attach_catalog_private_endpoint_details=action_details,
                catalog_id=self.module.params.get("catalog_id"),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCatalogCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_catalog_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_catalog_compartment_details=action_details,
                catalog_id=self.module.params.get("catalog_id"),
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

    def detach_catalog_private_endpoint(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachCatalogPrivateEndpointDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_catalog_private_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detach_catalog_private_endpoint_details=action_details,
                catalog_id=self.module.params.get("catalog_id"),
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

    def object_stats(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.object_stats,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                sort_by=self.module.params.get("sort_by"),
                sort_order=self.module.params.get("sort_order"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def users(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.users,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                sort_by=self.module.params.get("sort_by"),
                sort_order=self.module.params.get("sort_order"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


DataCatalogCatalogActionsHelperCustom = get_custom_class(
    "DataCatalogCatalogActionsHelperCustom"
)


class ResourceHelper(
    DataCatalogCatalogActionsHelperCustom, DataCatalogCatalogActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            catalog_private_endpoint_id=dict(type="str"),
            catalog_id=dict(aliases=["id"], type="str", required=True),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "attach_catalog_private_endpoint",
                    "change_compartment",
                    "detach_catalog_private_endpoint",
                    "object_stats",
                    "users",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="catalog",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
