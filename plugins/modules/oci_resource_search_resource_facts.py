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
module: oci_resource_search_resource_facts
short_description: Fetches details about one or multiple Resource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Resource resources in Oracle Cloud Infrastructure
    - Queries any and all compartments in the specified tenancy to find resources that match the specified criteria.
      Results include resources that you have permission to view and can span different resource types.
      You can also sort results based on a specified resource attribute.
version_added: "2.9"
author: Oracle (@oracle)
options:
    type:
        description:
            - The type of SearchDetails, whether `FreeText` or `Structured`.
        type: str
        choices:
            - "Structured"
            - "FreeText"
        required: true
    matching_context_type:
        description:
            - The type of matching context returned in the response. If you specify `HIGHLIGHTS`, then the service will highlight fragments in its response.
              (For more information, see ResourceSummary.searchContext and SearchContext.) The default setting is `NONE`.
        type: str
        choices:
            - "NONE"
            - "HIGHLIGHTS"
    query:
        description:
            - The structured query describing which resources to search for.
            - Required when type is 'Structured'
        type: str
    text:
        description:
            - The text to search for.
            - Required when type is 'FreeText'
        type: str
    tenant_id:
        description:
            - The tenancy ID, which can be used to specify a different tenancy (for cross-tenancy authorization) when searching for resources in a different
              tenancy.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List resources
  oci_resource_search_resource_facts:
    type: "FreeText"
    text: "jane"
    matching_context_type: "HIGHLIGHTS"

"""

RETURN = """
resources:
    description:
        - List of Resource resources
    returned: on success
    type: complex
    contains:
        resource_type:
            description:
                - The resource type name.
            returned: on success
            type: string
            sample: resource_type_example
        identifier:
            description:
                - The unique identifier for this particular resource, usually an OCID.
            returned: on success
            type: string
            sample: identifier_example
        compartment_id:
            description:
                - The OCID of the compartment that contains this resource.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time that this resource was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        display_name:
            description:
                - The display name (or name) of this resource, if one exists.
            returned: on success
            type: string
            sample: display_name_example
        availability_domain:
            description:
                - The availability domain where this resource exists, if applicable.
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        lifecycle_state:
            description:
                - The lifecycle state of this resource, if applicable.
            returned: on success
            type: string
            sample: lifecycle_state_example
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
        system_tags:
            description:
                - "System tags associated with this resource, if any. System tags are set by Oracle Cloud Infrastructure services. Each key is predefined and
                  scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
        search_context:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                highlights:
                    description:
                        - "Describes what in each field matched the search criteria by showing highlighted values, but only for free text searches or for
                          structured
                          queries that use a MATCHING clause. The list of strings represents fragments of values that matched the query conditions. Highlighted
                          values are wrapped with &lt;h1&gt;..&lt;/h1&gt; tags. All values are HTML-encoded (except &lt;h1&gt; tags)."
                    returned: on success
                    type: dict
                    sample: {}
        identity_context:
            description:
                - "Additional identifiers to use together in a \\"Get\\" request for a specified resource, only required for resource types
                  that explicitly cannot be retrieved by using a single identifier, such as the resource's OCID."
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "resource_type": "resource_type_example",
        "identifier": "identifier_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "lifecycle_state": "lifecycle_state_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "search_context": {
            "highlights": {}
        },
        "identity_context": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.resource_search import ResourceSearchClient
    from oci.resource_search.models import SearchDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "type",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "tenant_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.search_resources,
            search_details=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, SearchDetails
            ),
            **optional_kwargs
        )


ResourceFactsHelperCustom = get_custom_class("ResourceFactsHelperCustom")


class ResourceFactsHelper(ResourceFactsHelperCustom, ResourceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            type=dict(type="str", required=True, choices=["Structured", "FreeText"]),
            matching_context_type=dict(type="str", choices=["NONE", "HIGHLIGHTS"]),
            query=dict(type="str"),
            text=dict(type="str"),
            tenant_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource",
        service_client_class=ResourceSearchClient,
        namespace="resource_search",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(resources=result)


if __name__ == "__main__":
    main()
