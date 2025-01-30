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
module: oci_certificates_management_ca_bundle_actions
short_description: Perform actions on a CaBundle resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CaBundle resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a CA bundle to a different compartment in the same tenancy. For information about
      moving resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      When provided, if-match is checked against the ETag values of the secret.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ca_bundle_id:
        description:
            - The OCID of the CA bundle.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the CA bundle should move.
        type: str
        required: true
    action:
        description:
            - The action to perform on the CaBundle.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on ca_bundle
  oci_certificates_management_ca_bundle_actions:
    # required
    ca_bundle_id: "ocid1.cabundle.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
ca_bundle:
    description:
        - Details of the CaBundle resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the CA bundle.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A user-friendly name for the CA bundle. Names are unique within a compartment. Avoid entering confidential information. Valid characters
                  include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - A brief description of the CA bundle.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "A property indicating when the CA bundle was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the CA bundle.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the CA bundle.
            returned: on success
            type: str
            sample: lifecycle_details_example
        compartment_id:
            description:
                - The OCID of the compartment for the CA bundle.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.certificates_management import CertificatesManagementClient
    from oci.certificates_management.models import ChangeCaBundleCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificatesManagementCaBundleActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "ca_bundle_id"

    def get_module_resource_id(self):
        return self.module.params.get("ca_bundle_id")

    def get_get_fn(self):
        return self.client.get_ca_bundle

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ca_bundle,
            ca_bundle_id=self.module.params.get("ca_bundle_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCaBundleCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_ca_bundle_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ca_bundle_id=self.module.params.get("ca_bundle_id"),
                change_ca_bundle_compartment_details=action_details,
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


CertificatesManagementCaBundleActionsHelperCustom = get_custom_class(
    "CertificatesManagementCaBundleActionsHelperCustom"
)


class ResourceHelper(
    CertificatesManagementCaBundleActionsHelperCustom,
    CertificatesManagementCaBundleActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            ca_bundle_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ca_bundle",
        service_client_class=CertificatesManagementClient,
        namespace="certificates_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
