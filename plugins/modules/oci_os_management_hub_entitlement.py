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
module: oci_os_management_hub_entitlement
short_description: Manage an Entitlement resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create an Entitlement resource in Oracle Cloud Infrastructure
    - For I(state=present), registers the necessary entitlement credentials for OS vendor software sources for a tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the entitlement.
        type: str
        required: true
    csi:
        description:
            - The Customer Support Identifier (CSI) which unlocks the software sources. The CSI is is a unique key given to a customer and it uniquely
              identifies the entitlement.
        type: str
        required: true
    state:
        description:
            - The state of the Entitlement.
            - Use I(state=present) to create an Entitlement.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create entitlement
  oci_os_management_hub_entitlement:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    csi: csi_example

"""

RETURN = """
entitlement:
    description:
        - Details of the Entitlement resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the entitlement.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        csi:
            description:
                - The Customer Support Identifier (CSI) which unlocks the software sources. The CSI is is a unique key given to a customer and it uniquely
                  identifies the entitlement.
            returned: on success
            type: str
            sample: csi_example
        vendor_name:
            description:
                - The vendor for the entitlement.
            returned: on success
            type: str
            sample: vendor_name_example
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "csi": "csi_example",
        "vendor_name": "vendor_name_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import SoftwareSourceClient
    from oci.os_management_hub.models import CreateEntitlementDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubEntitlementHelperGen(OCIResourceHelperBase):
    """Supported operations: create and list"""

    def get_possible_entity_types(self):
        return super(
            OsManagementHubEntitlementHelperGen, self
        ).get_possible_entity_types() + [
            "osmhsoftwaresource",
            "osmhsoftwaresources",
            "osManagementHubosmhsoftwaresource",
            "osManagementHubosmhsoftwaresources",
            "osmhsoftwaresourceresource",
            "osmhsoftwaresourcesresource",
            "entitlement",
            "entitlements",
            "osManagementHubentitlement",
            "osManagementHubentitlements",
            "entitlementresource",
            "entitlementsresource",
            "osmanagementhub",
        ]

    # needs custom GET via LIST implementation because resource does not have an 'id' field

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["csi"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_entitlements, **kwargs
        )

    def get_create_model_class(self):
        return CreateEntitlementDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_entitlement,
            call_fn_args=(),
            call_fn_kwargs=dict(create_entitlement_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


OsManagementHubEntitlementHelperCustom = get_custom_class(
    "OsManagementHubEntitlementHelperCustom"
)


class ResourceHelper(
    OsManagementHubEntitlementHelperCustom, OsManagementHubEntitlementHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            csi=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="entitlement",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
