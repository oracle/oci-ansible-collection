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
module: oci_email_dkim_facts
short_description: Fetches details about one or multiple Dkim resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Dkim resources in Oracle Cloud Infrastructure
    - Lists DKIMs for a email domain.
    - If I(dkim_id) is specified, the details of a single Dkim will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dkim_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this DKIM.
            - Required to get a specific dkim.
        type: str
        aliases: ["id"]
    email_domain_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the email domain to which this DKIM belongs.
            - Required to list multiple dkims.
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
            - "INACTIVE"
            - "NEEDS_ATTENTION"
            - "UPDATING"
    sort_by:
        description:
            - Specifies the attribute with which to sort the DKIMs.
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
- name: Get a specific dkim
  oci_email_dkim_facts:
    # required
    dkim_id: "ocid1.dkim.oc1..xxxxxxEXAMPLExxxxxx"

- name: List dkims
  oci_email_dkim_facts:
    # required
    email_domain_id: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    lifecycle_state: ACTIVE
    sort_by: TIMECREATED

"""

RETURN = """
dkims:
    description:
        - List of Dkim resources
    returned: on success
    type: complex
    contains:
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        dns_subdomain_name:
            description:
                - The name of the DNS subdomain that must be provisioned to enable email recipients to verify DKIM signatures.
                  It is usually created with a CNAME record set to the cnameRecordValue
                - Returned for get operation
            returned: on success
            type: str
            sample: dns_subdomain_name_example
        cname_record_value:
            description:
                - The DNS CNAME record value to provision to the DKIM DNS subdomain, when using the CNAME method for DKIM setup (preferred).
                - Returned for get operation
            returned: on success
            type: str
            sample: cname_record_value_example
        txt_record_value:
            description:
                - The DNS TXT record value to provision to the DKIM DNS subdomain in place of using a CNAME record.
                  This is used in cases where a CNAME can not be used, such as when the cnameRecordValue would exceed the maximum length for a DNS entry.
                  This can also be used by customers who have an existing procedure to directly provision TXT records for DKIM.
                  Be aware that many DNS APIs will require you to break this string into segments of less than 255 characters.
                - Returned for get operation
            returned: on success
            type: str
            sample: txt_record_value_example
        name:
            description:
                - The DKIM selector.
                  If the same domain is managed in more than one region, each region must use different selectors.
            returned: on success
            type: str
            sample: name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DKIM.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        email_domain_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the email domain
                  that this DKIM belongs to.
            returned: on success
            type: str
            sample: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains this DKIM.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the DKIM.
            returned: on success
            type: str
            sample: ACTIVE
        description:
            description:
                - The description of the DKIM. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "The time the DKIM was created.
                  Times are expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format, \\"YYYY-MM-ddThh:mmZ\\"."
                - "Example: `2021-02-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time of the last change to the DKIM configuration, due to a state change or
                  an update operation.
                  Times are expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format, \\"YYYY-MM-ddThh:mmZ\\"."
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
        "lifecycle_details": "lifecycle_details_example",
        "dns_subdomain_name": "dns_subdomain_name_example",
        "cname_record_value": "cname_record_value_example",
        "txt_record_value": "txt_record_value_example",
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "email_domain_id": "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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


class DkimFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dkim_id",
        ]

    def get_required_params_for_list(self):
        return [
            "email_domain_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dkim, dkim_id=self.module.params.get("dkim_id"),
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
            self.client.list_dkims,
            email_domain_id=self.module.params.get("email_domain_id"),
            **optional_kwargs
        )


DkimFactsHelperCustom = get_custom_class("DkimFactsHelperCustom")


class ResourceFactsHelper(DkimFactsHelperCustom, DkimFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dkim_id=dict(aliases=["id"], type="str"),
            email_domain_id=dict(type="str"),
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
                    "INACTIVE",
                    "NEEDS_ATTENTION",
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
        resource_type="dkim",
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

    module.exit_json(dkims=result)


if __name__ == "__main__":
    main()
