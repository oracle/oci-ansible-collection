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
module: oci_service_catalog_private_application_actions
short_description: Perform actions on a PrivateApplication resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a PrivateApplication resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified private application from one compartment to another.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    private_application_id:
        description:
            - The unique identifier for the private application.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where you want to move the private
              application.
        type: str
    action:
        description:
            - The action to perform on the PrivateApplication.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on private_application
  oci_service_catalog_private_application_actions:
    # required
    private_application_id: "ocid1.privateapplication.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
private_application:
    description:
        - Details of the PrivateApplication resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The lifecycle state of the private application.
            returned: on success
            type: str
            sample: CREATING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the private application resides.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The unique identifier for the private application in Marketplace.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the private application.
            returned: on success
            type: str
            sample: display_name_example
        short_description:
            description:
                - A short description of the private application.
            returned: on success
            type: str
            sample: short_description_example
        long_description:
            description:
                - A long description of the private application.
            returned: on success
            type: str
            sample: long_description_example
        logo:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - The name used to refer to the uploaded data.
                    returned: on success
                    type: str
                    sample: display_name_example
                content_url:
                    description:
                        - The content URL of the uploaded data.
                    returned: on success
                    type: str
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the uploaded data.
                    returned: on success
                    type: str
                    sample: mime_type_example
        package_type:
            description:
                - Type of packages within this private application.
            returned: on success
            type: str
            sample: STACK
        time_created:
            description:
                - The date and time the private application was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-05-26T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the private application was last modified, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-12-10T05:10:29.721Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: {
        "lifecycle_state": "CREATING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "short_description": "short_description_example",
        "long_description": "long_description_example",
        "logo": {
            "display_name": "display_name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example"
        },
        "package_type": "STACK",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
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
    from oci.service_catalog import ServiceCatalogClient
    from oci.service_catalog.models import ChangePrivateApplicationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateApplicationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "private_application_id"

    def get_module_resource_id(self):
        return self.module.params.get("private_application_id")

    def get_get_fn(self):
        return self.client.get_private_application

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_application,
            private_application_id=self.module.params.get("private_application_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePrivateApplicationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_private_application_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_application_id=self.module.params.get("private_application_id"),
                change_private_application_compartment_details=action_details,
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


PrivateApplicationActionsHelperCustom = get_custom_class(
    "PrivateApplicationActionsHelperCustom"
)


class ResourceHelper(
    PrivateApplicationActionsHelperCustom, PrivateApplicationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            private_application_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="private_application",
        service_client_class=ServiceCatalogClient,
        namespace="service_catalog",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
