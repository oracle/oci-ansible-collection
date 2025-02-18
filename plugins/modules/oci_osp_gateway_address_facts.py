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
module: oci_osp_gateway_address_facts
short_description: Fetches details about a Address resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Address resource in Oracle Cloud Infrastructure
    - Get the address by id for the compartment
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    osp_home_region:
        description:
            - The home region's public name of the logged in user.
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    address_id:
        description:
            - The identifier of the address.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific address
  oci_osp_gateway_address_facts:
    # required
    osp_home_region: us-phoenix-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    address_id: "ocid1.address.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
address:
    description:
        - Address resource
    returned: on success
    type: complex
    contains:
        address_key:
            description:
                - Address identifier.
            returned: on success
            type: str
            sample: address_key_example
        line1:
            description:
                - Address line 1.
            returned: on success
            type: str
            sample: line1_example
        line2:
            description:
                - Address line 2.
            returned: on success
            type: str
            sample: line2_example
        line3:
            description:
                - Address line 3.
            returned: on success
            type: str
            sample: line3_example
        line4:
            description:
                - Address line 4.
            returned: on success
            type: str
            sample: line4_example
        street_name:
            description:
                - Street name of the address.
            returned: on success
            type: str
            sample: street_name_example
        street_number:
            description:
                - Street number of the address.
            returned: on success
            type: str
            sample: street_number_example
        city:
            description:
                - Name of the city.
            returned: on success
            type: str
            sample: city_example
        county:
            description:
                - County of the address.
            returned: on success
            type: str
            sample: county_example
        country:
            description:
                - Country of the address.
            returned: on success
            type: str
            sample: country_example
        province:
            description:
                - Province of the address.
            returned: on success
            type: str
            sample: province_example
        postal_code:
            description:
                - Post code of the address.
            returned: on success
            type: str
            sample: postal_code_example
        state:
            description:
                - State of the address.
            returned: on success
            type: str
            sample: state_example
        email_address:
            description:
                - Contact person email address.
            returned: on success
            type: str
            sample: email_address_example
        company_name:
            description:
                - Name of the customer company.
            returned: on success
            type: str
            sample: company_name_example
        first_name:
            description:
                - First name of the contact person.
            returned: on success
            type: str
            sample: first_name_example
        middle_name:
            description:
                - Middle name of the contact person.
            returned: on success
            type: str
            sample: middle_name_example
        last_name:
            description:
                - Last name of the contact person.
            returned: on success
            type: str
            sample: last_name_example
        phone_country_code:
            description:
                - Phone country code of the contact person.
            returned: on success
            type: str
            sample: phone_country_code_example
        phone_number:
            description:
                - Phone number of the contact person.
            returned: on success
            type: str
            sample: phone_number_example
        job_title:
            description:
                - Job title of the contact person.
            returned: on success
            type: str
            sample: job_title_example
        department_name:
            description:
                - Department name of the customer company.
            returned: on success
            type: str
            sample: department_name_example
        internal_number:
            description:
                - Internal number of the customer company.
            returned: on success
            type: str
            sample: internal_number_example
        contributor_class:
            description:
                - Contributor class of the customer company.
            returned: on success
            type: str
            sample: contributor_class_example
        state_inscription:
            description:
                - State Inscription.
            returned: on success
            type: str
            sample: state_inscription_example
        municipal_inscription:
            description:
                - Municipal Inscription.
            returned: on success
            type: str
            sample: municipal_inscription_example
    sample: {
        "address_key": "address_key_example",
        "line1": "line1_example",
        "line2": "line2_example",
        "line3": "line3_example",
        "line4": "line4_example",
        "street_name": "street_name_example",
        "street_number": "street_number_example",
        "city": "city_example",
        "county": "county_example",
        "country": "country_example",
        "province": "province_example",
        "postal_code": "postal_code_example",
        "state": "state_example",
        "email_address": "email_address_example",
        "company_name": "company_name_example",
        "first_name": "first_name_example",
        "middle_name": "middle_name_example",
        "last_name": "last_name_example",
        "phone_country_code": "phone_country_code_example",
        "phone_number": "phone_number_example",
        "job_title": "job_title_example",
        "department_name": "department_name_example",
        "internal_number": "internal_number_example",
        "contributor_class": "contributor_class_example",
        "state_inscription": "state_inscription_example",
        "municipal_inscription": "municipal_inscription_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osp_gateway import AddressServiceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddressFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "osp_home_region",
            "compartment_id",
            "address_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_address,
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
            address_id=self.module.params.get("address_id"),
        )


AddressFactsHelperCustom = get_custom_class("AddressFactsHelperCustom")


class ResourceFactsHelper(AddressFactsHelperCustom, AddressFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            osp_home_region=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            address_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="address",
        service_client_class=AddressServiceClient,
        namespace="osp_gateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(address=result)


if __name__ == "__main__":
    main()
