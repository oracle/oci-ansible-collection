#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_marketplace_agreement_facts
short_description: Fetches details about one or multiple Agreement resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Agreement resources in Oracle Cloud Infrastructure
    - Returns the terms of use agreements that must be accepted before you can deploy the specified version of a package.
    - If I(agreement_id) is specified, the details of a single Agreement will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    listing_id:
        description:
            - The unique identifier for the listing.
        type: str
        required: true
    package_version:
        description:
            - The version of the package. Package versions are unique within a listing.
        type: str
        required: true
    agreement_id:
        description:
            - The unique identifier for the agreement.
            - Required to get a specific agreement.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The unique identifier for the compartment.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List agreements
  oci_marketplace_agreement_facts:
    listing_id: ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx
    package_version: package_version_example

- name: Get a specific agreement
  oci_marketplace_agreement_facts:
    listing_id: ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx
    package_version: package_version_example
    agreement_id: ocid1.agreement.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
agreements:
    description:
        - List of Agreement resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier for the agreement.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        content_url:
            description:
                - The content URL of the agreement.
            returned: on success
            type: string
            sample: content_url_example
        signature:
            description:
                - A time-based signature that can be used to accept an agreement or remove a
                  previously accepted agreement from the list that Marketplace checks before a deployment.
            returned: on success
            type: string
            sample: signature_example
        compartment_id:
            description:
                - The unique identifier for the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        author:
            description:
                - Who authored the agreement.
            returned: on success
            type: string
            sample: ORACLE
        prompt:
            description:
                - Textual prompt to read and accept the agreement.
            returned: on success
            type: string
            sample: prompt_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "content_url": "content_url_example",
        "signature": "signature_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "author": "ORACLE",
        "prompt": "prompt_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.marketplace import MarketplaceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AgreementFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "listing_id",
            "package_version",
            "agreement_id",
        ]

    def get_required_params_for_list(self):
        return [
            "listing_id",
            "package_version",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_agreement,
            listing_id=self.module.params.get("listing_id"),
            package_version=self.module.params.get("package_version"),
            agreement_id=self.module.params.get("agreement_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_agreements,
            listing_id=self.module.params.get("listing_id"),
            package_version=self.module.params.get("package_version"),
            **optional_kwargs
        )


AgreementFactsHelperCustom = get_custom_class("AgreementFactsHelperCustom")


class ResourceFactsHelper(AgreementFactsHelperCustom, AgreementFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            listing_id=dict(type="str", required=True),
            package_version=dict(type="str", required=True),
            agreement_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="agreement",
        service_client_class=MarketplaceClient,
        namespace="marketplace",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(agreements=result)


if __name__ == "__main__":
    main()
