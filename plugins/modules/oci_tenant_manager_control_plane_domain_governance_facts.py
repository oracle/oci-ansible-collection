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
module: oci_tenant_manager_control_plane_domain_governance_facts
short_description: Fetches details about one or multiple DomainGovernance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DomainGovernance resources in Oracle Cloud Infrastructure
    - Return a (paginated) list of domain governance entities.
    - If I(domain_governance_id) is specified, the details of a single DomainGovernance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple domain_governances.
        type: str
    domain_id:
        description:
            - The domain OCID.
        type: str
    domain_governance_id:
        description:
            - The domain governance OCID.
            - Required to get a specific domain_governance.
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
- name: Get a specific domain_governance
  oci_tenant_manager_control_plane_domain_governance_facts:
    # required
    domain_governance_id: "ocid1.domaingovernance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List domain_governances
  oci_tenant_manager_control_plane_domain_governance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    domain_governance_id: "ocid1.domaingovernance.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    name: name_example
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
domain_governances:
    description:
        - List of DomainGovernance resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        owner_id:
            description:
                - The OCID of the tenancy that owns this domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.owner.oc1..xxxxxxEXAMPLExxxxxx"
        domain_id:
            description:
                - The OCID of the domain associated with this domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the domain governance entity.
            returned: on success
            type: str
            sample: ACTIVE
        is_governance_enabled:
            description:
                - Indicates whether governance is enabled for this domain.
            returned: on success
            type: bool
            sample: true
        subscription_email:
            description:
                - The email to notify the user, and that the ONS subscription will be created with.
            returned: on success
            type: str
            sample: subscription_email_example
        ons_topic_id:
            description:
                - The ONS topic associated with this domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
        ons_subscription_id:
            description:
                - The ONS subscription associated with this domain governance entity.
            returned: on success
            type: str
            sample: "ocid1.onssubscription.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date-time when this domain governance was created. An RFC 3339-formatted date and time string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when this domain governance was last updated. An RFC 3339-formatted date and time string.
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
        "owner_id": "ocid1.owner.oc1..xxxxxxEXAMPLExxxxxx",
        "domain_id": "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "is_governance_enabled": true,
        "subscription_email": "subscription_email_example",
        "ons_topic_id": "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx",
        "ons_subscription_id": "ocid1.onssubscription.oc1..xxxxxxEXAMPLExxxxxx",
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
    from oci.tenant_manager_control_plane import DomainGovernanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DomainGovernanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "domain_governance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_domain_governance,
            domain_governance_id=self.module.params.get("domain_governance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "domain_id",
            "domain_governance_id",
            "lifecycle_state",
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
            self.client.list_domain_governances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DomainGovernanceFactsHelperCustom = get_custom_class(
    "DomainGovernanceFactsHelperCustom"
)


class ResourceFactsHelper(
    DomainGovernanceFactsHelperCustom, DomainGovernanceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            domain_id=dict(type="str"),
            domain_governance_id=dict(aliases=["id"], type="str"),
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
        resource_type="domain_governance",
        service_client_class=DomainGovernanceClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(domain_governances=result)


if __name__ == "__main__":
    main()
