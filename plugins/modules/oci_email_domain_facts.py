#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_email_domain_facts
short_description: Fetches details about one or multiple EmailDomain resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple EmailDomain resources in Oracle Cloud Infrastructure
    - Lists email domains in the specified compartment.
    - If I(email_domain_id) is specified, the details of a single EmailDomain will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    email_domain_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this email domain.
            - Required to get a specific email_domain.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID for the compartment.
            - Required to list multiple email_domains.
        type: str
    name:
        description:
            - A filter to only return resources that match the given name exactly.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending or descending order.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - Filter returned list by specified lifecycle state. This parameter is case-insensitive.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "UPDATING"
    sort_by:
        description:
            - Specifies the attribute with which to sort the email domains.
            - "Default: `TIMECREATED`"
            - "* **TIMECREATED:** Sorts by timeCreated.
              * **NAME:** Sorts by name.
              * **ID:** Sorts by id."
        type: str
        choices:
            - "TIMECREATED"
            - "ID"
            - "NAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific email_domain
  oci_email_domain_facts:
    # required
    email_domain_id: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"

- name: List email_domains
  oci_email_domain_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    lifecycle_state: ACTIVE
    sort_by: TIMECREATED

"""

RETURN = """
email_domains:
    description:
        - List of EmailDomain resources
    returned: on success
    type: complex
    contains:
        is_spf:
            description:
                - Value of the SPF field. For more information about SPF, please see
                  L(SPF Authentication,https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        name:
            description:
                - The name of the email domain in the Internet Domain Name System (DNS).
                - "Example: `example.net`"
            returned: on success
            type: str
            sample: name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the email domain.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains this email domain.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the email domain.
            returned: on success
            type: str
            sample: ACTIVE
        active_dkim_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DKIM key
                  that will be used to sign mail sent from this email domain.
            returned: on success
            type: str
            sample: "ocid1.activedkim.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The description of a email domain.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "The time the email domain was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format, \\"YYYY-MM-ddThh:mmZ\\"."
                - "Example: `2021-02-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "is_spf": true,
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "active_dkim_id": "ocid1.activedkim.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.email import EmailClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EmailDomainFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "email_domain_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_email_domain,
            email_domain_id=self.module.params.get("email_domain_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "lifecycle_state",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_email_domains,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


EmailDomainFactsHelperCustom = get_custom_class("EmailDomainFactsHelperCustom")


class ResourceFactsHelper(EmailDomainFactsHelperCustom, EmailDomainFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            email_domain_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "UPDATING",
                ],
            ),
            sort_by=dict(type="str", choices=["TIMECREATED", "ID", "NAME"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="email_domain",
        service_client_class=EmailClient,
        namespace="email",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(email_domains=result)


if __name__ == "__main__":
    main()
