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
module: oci_cims_user
short_description: Manage an User resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create an User resource in Oracle Cloud Infrastructure
    - For I(state=present), create user to request Customer Support Identifier(CSI) to Customer User Administrator(CUA).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy.
        type: str
        required: true
    first_name:
        description:
            - First name of the user.
        type: str
        required: true
    last_name:
        description:
            - Last name of the user.
        type: str
        required: true
    country:
        description:
            - Country of the user.
        type: str
        required: true
    csi:
        description:
            - CSI to be associated to the user.
        type: str
        required: true
    phone:
        description:
            - Contact number of the user.
        type: str
        required: true
    timezone:
        description:
            - Timezone of the user.
        type: str
        required: true
    organization_name:
        description:
            - Organization of the user.
        type: str
        required: true
    ocid:
        description:
            - User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.
        type: str
        required: true
    homeregion:
        description:
            - The region of the tenancy.
        type: str
    state:
        description:
            - The state of the User.
            - Use I(state=present) to create an User.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create user
  oci_cims_user:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    first_name: first_name_example
    last_name: last_name_example
    country: country_example
    csi: csi_example
    phone: phone_example
    timezone: timezone_example
    organization_name: organization_name_example
    ocid: ocid_example

    # optional
    homeregion: us-phoenix-1

"""

RETURN = """
user:
    description:
        - Details of the User resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique identifier for the user.
            returned: on success
            type: str
            sample: key_example
        first_name:
            description:
                - First name of the user.
            returned: on success
            type: str
            sample: first_name_example
        last_name:
            description:
                - Last name of the user.
            returned: on success
            type: str
            sample: last_name_example
        country:
            description:
                - Country of the user.
            returned: on success
            type: str
            sample: country_example
        csi:
            description:
                - CSI to be associated to the user.
            returned: on success
            type: str
            sample: csi_example
        phone:
            description:
                - Contact number of the user.
            returned: on success
            type: str
            sample: phone_example
        timezone:
            description:
                - Timezone of the user.
            returned: on success
            type: str
            sample: timezone_example
        organization_name:
            description:
                - Organization of the user.
            returned: on success
            type: str
            sample: organization_name_example
        compartment_id:
            description:
                - The OCID of the tenancy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        contact_email:
            description:
                - The email of the contact person.
            returned: on success
            type: str
            sample: contact_email_example
    sample: {
        "key": "key_example",
        "first_name": "first_name_example",
        "last_name": "last_name_example",
        "country": "country_example",
        "csi": "csi_example",
        "phone": "phone_example",
        "timezone": "timezone_example",
        "organization_name": "organization_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "contact_email": "contact_email_example"
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
    from oci.cims import UserClient
    from oci.cims.models import CreateUserDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UserHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_possible_entity_types(self):
        return super(UserHelperGen, self).get_possible_entity_types() + [
            "user",
            "users",
            "cimsuser",
            "cimsusers",
            "userresource",
            "usersresource",
            "cims",
        ]

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return CreateUserDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_user,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_user_details=create_details,
                ocid=self.module.params.get("ocid"),
                homeregion=self.module.params.get("homeregion"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


UserHelperCustom = get_custom_class("UserHelperCustom")


class ResourceHelper(UserHelperCustom, UserHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            first_name=dict(type="str", required=True),
            last_name=dict(type="str", required=True),
            country=dict(type="str", required=True),
            csi=dict(type="str", required=True),
            phone=dict(type="str", required=True),
            timezone=dict(type="str", required=True),
            organization_name=dict(type="str", required=True),
            ocid=dict(type="str", required=True),
            homeregion=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="user",
        service_client_class=UserClient,
        namespace="cims",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
