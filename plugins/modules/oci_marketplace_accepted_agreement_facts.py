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
module: oci_marketplace_accepted_agreement_facts
short_description: Fetches details about one or multiple AcceptedAgreement resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AcceptedAgreement resources in Oracle Cloud Infrastructure
    - Lists the terms of use agreements that have been accepted in the specified compartment.
      You can filter results by specifying query parameters.
    - If I(accepted_agreement_id) is specified, the details of a single AcceptedAgreement will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier for the compartment.
            - Required to list multiple accepted_agreements.
        type: str
    display_name:
        description:
            - The display name of the resource.
        type: str
        aliases: ["name"]
    listing_id:
        description:
            - The unique identifier for the listing.
        type: str
    package_version:
        description:
            - The version of the package. Package versions are unique within a listing.
        type: str
    accepted_agreement_id:
        description:
            - The unique identifier for the accepted terms of use agreement.
            - Required to get a specific accepted_agreement.
        type: str
        aliases: ["id"]
    sort_by:
        description:
            - The field to use to sort listed results. You can only specify one field to sort by.
              `TIMEACCEPTED` displays results in descending order by default. You can change your
              preference by specifying a different sort order.
        type: str
        choices:
            - "TIMEACCEPTED"
    sort_order:
        description:
            - The sort order to use, either `ASC` or `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific accepted_agreement
  oci_marketplace_accepted_agreement_facts:
    # required
    accepted_agreement_id: "ocid1.acceptedagreement.oc1..xxxxxxEXAMPLExxxxxx"

- name: List accepted_agreements
  oci_marketplace_accepted_agreement_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
    package_version: package_version_example
    accepted_agreement_id: "ocid1.acceptedagreement.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMEACCEPTED
    sort_order: ASC

"""

RETURN = """
accepted_agreements:
    description:
        - List of AcceptedAgreement resources
    returned: on success
    type: complex
    contains:
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The unique identifier for the acceptance of the agreement within a specific compartment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A display name for the accepted agreement.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The unique identifier for the compartment where the agreement was accepted.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        listing_id:
            description:
                - The unique identifier for the listing associated with the agreement.
            returned: on success
            type: str
            sample: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
        package_version:
            description:
                - The package version associated with the agreement.
            returned: on success
            type: str
            sample: package_version_example
        agreement_id:
            description:
                - The unique identifier for the terms of use agreement itself.
            returned: on success
            type: str
            sample: "ocid1.agreement.oc1..xxxxxxEXAMPLExxxxxx"
        time_accepted:
            description:
                - The time the agreement was accepted.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
        "package_version": "package_version_example",
        "agreement_id": "ocid1.agreement.oc1..xxxxxxEXAMPLExxxxxx",
        "time_accepted": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.marketplace import MarketplaceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AcceptedAgreementFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "accepted_agreement_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_accepted_agreement,
            accepted_agreement_id=self.module.params.get("accepted_agreement_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "listing_id",
            "package_version",
            "accepted_agreement_id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_accepted_agreements,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AcceptedAgreementFactsHelperCustom = get_custom_class(
    "AcceptedAgreementFactsHelperCustom"
)


class ResourceFactsHelper(
    AcceptedAgreementFactsHelperCustom, AcceptedAgreementFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            listing_id=dict(type="str"),
            package_version=dict(type="str"),
            accepted_agreement_id=dict(aliases=["id"], type="str"),
            sort_by=dict(type="str", choices=["TIMEACCEPTED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="accepted_agreement",
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

    module.exit_json(accepted_agreements=result)


if __name__ == "__main__":
    main()
