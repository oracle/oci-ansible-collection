#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_identity_network_sources_facts
short_description: Fetches details about one or multiple NetworkSources resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NetworkSources resources in Oracle Cloud Infrastructure
    - Lists the network sources in your tenancy. You must specify your tenancy's OCID as the value for
      the compartment ID (remember that the tenancy is simply the root compartment).
      See L(Where to Get the Tenancy's OCID and User's OCID,https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#five).
    - If I(network_source_id) is specified, the details of a single NetworkSources will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_source_id:
        description:
            - The OCID of the network source.
            - Required to get a specific network_sources.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
            - Required to list multiple network_sources.
        type: str
    name:
        description:
            - A filter to only return resources that match the given name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for NAME is ascending. The NAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by Availability Domain if the scope of the resource type is within a
              single Availability Domain. If you call one of these \\"List\\" operations without specifying
              an Availability Domain, the resources are grouped by Availability Domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific network_sources
  oci_identity_network_sources_facts:
    # required
    network_source_id: "ocid1.networksource.oc1..xxxxxxEXAMPLExxxxxx"

- name: List network_sources
  oci_identity_network_sources_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: CREATING

"""

RETURN = """
network_sources:
    description:
        - List of NetworkSources resources
    returned: on success
    type: complex
    contains:
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        id:
            description:
                - The OCID of the network source.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the network source. The tenancy is the root compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the network source during creation. The name must be unique across
                  the tenancy and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description you assign to the network source. Does not have to be unique, and it's changeable.
            returned: on success
            type: str
            sample: description_example
        public_source_list:
            description:
                - A list of allowed public IPs and CIDR ranges.
            returned: on success
            type: list
            sample: []
        virtual_source_list:
            description:
                - "A list of allowed VCN OCID and IP range pairs.
                  Example:`\\"vcnId\\": \\"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\\", \\"ipRanges\\": [ \\"129.213.39.0/24\\" ]`"
            returned: on success
            type: complex
            contains:
                vcn_id:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
                ip_ranges:
                    description:
                        - ""
                    returned: on success
                    type: list
                    sample: []
        services:
            description:
                - "-- The services attribute has no effect and is reserved for use by Oracle. --"
            returned: on success
            type: list
            sample: []
        lifecycle_state:
            description:
                - The network source object's current state. After creating a network source, make sure its `lifecycleState` changes from CREATING to
                  ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - Date and time the network source was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "inactive_status": 56,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "public_source_list": [],
        "virtual_source_list": [{
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "ip_ranges": []
        }],
        "services": [],
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkSourcesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "network_source_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_source,
            network_source_id=self.module.params.get("network_source_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_network_sources,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


NetworkSourcesFactsHelperCustom = get_custom_class("NetworkSourcesFactsHelperCustom")


class ResourceFactsHelper(
    NetworkSourcesFactsHelperCustom, NetworkSourcesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            network_source_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="network_sources",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(network_sources=result)


if __name__ == "__main__":
    main()
