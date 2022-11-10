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
module: oci_tenant_manager_control_plane_domain_facts
short_description: Fetches details about one or multiple Domain resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Domain resources in Oracle Cloud Infrastructure
    - Return a (paginated) list of domains.
    - If I(domain_id) is specified, the details of a single Domain will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple domains.
        type: str
    domain_id:
        description:
            - The domain OCID.
            - Required to get a specific domain.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - The lifecycle state of the resource.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "FAILED"
            - "TERMINATED"
    status:
        description:
            - The status of the domain.
        type: str
        choices:
            - "PENDING"
            - "RELEASING"
            - "RELEASED"
            - "EXPIRING"
            - "REVOKING"
            - "REVOKED"
            - "ACTIVE"
            - "FAILED"
    name:
        description:
            - A filter to return only resources that exactly match the name given.
        type: str
    sort_by:
        description:
            - "The field to sort by. Only one sort order can be provided.
              * The default order for timeCreated is descending.
              * The default order for displayName is ascending.
              * If no value is specified, timeCreated is the default."
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific domain
  oci_tenant_manager_control_plane_domain_facts:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"

- name: List domains
  oci_tenant_manager_control_plane_domain_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    status: PENDING
    name: name_example
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
domains:
    description:
        - List of Domain resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the domain.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        domain_name:
            description:
                - The domain name.
            returned: on success
            type: str
            sample: domain_name_example
        owner_id:
            description:
                - The OCID of the tenancy that has started the registration process for this domain.
            returned: on success
            type: str
            sample: "ocid1.owner.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the domain.
            returned: on success
            type: str
            sample: ACTIVE
        status:
            description:
                - Status of the domain.
            returned: on success
            type: str
            sample: PENDING
        txt_record:
            description:
                - The code that the owner of the domain will need to add as a TXT record to their domain.
            returned: on success
            type: str
            sample: txt_record_example
        time_created:
            description:
                - Date-time when this domain was created. An RFC 3339-formatted date and time string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when this domain was last updated. An RFC 3339-formatted date and time string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "domain_name": "domain_name_example",
        "owner_id": "ocid1.owner.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "status": "PENDING",
        "txt_record": "txt_record_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import DomainClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DomainFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "domain_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_domain, domain_id=self.module.params.get("domain_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "domain_id",
            "lifecycle_state",
            "status",
            "name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_domains,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DomainFactsHelperCustom = get_custom_class("DomainFactsHelperCustom")


class ResourceFactsHelper(DomainFactsHelperCustom, DomainFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            domain_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "FAILED",
                    "TERMINATED",
                ],
            ),
            status=dict(
                type="str",
                choices=[
                    "PENDING",
                    "RELEASING",
                    "RELEASED",
                    "EXPIRING",
                    "REVOKING",
                    "REVOKED",
                    "ACTIVE",
                    "FAILED",
                ],
            ),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="domain",
        service_client_class=DomainClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(domains=result)


if __name__ == "__main__":
    main()
