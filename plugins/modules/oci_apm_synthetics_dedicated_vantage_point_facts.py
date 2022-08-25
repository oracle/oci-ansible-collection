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
module: oci_apm_synthetics_dedicated_vantage_point_facts
short_description: Fetches details about one or multiple DedicatedVantagePoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DedicatedVantagePoint resources in Oracle Cloud Infrastructure
    - Returns a list of dedicated vantage points.
    - If I(dedicated_vantage_point_id) is specified, the details of a single DedicatedVantagePoint will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dedicated_vantage_point_id:
        description:
            - The OCID of the dedicated vantage point.
            - Required to get a specific dedicated_vantage_point.
        type: str
        aliases: ["id"]
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order of displayName is ascending.
              Default order of timeCreated and timeUpdated is descending.
              The displayName sort by is case-sensitive.
        type: str
        choices:
            - "displayName"
            - "name"
            - "timeCreated"
            - "timeUpdated"
            - "status"
    display_name:
        description:
            - A filter to return only the resources that match the entire display name.
        type: str
    name:
        description:
            - A filter to return only the resources that match the entire name.
        type: str
    status:
        description:
            - A filter to return only the dedicated vantage points that match a given status.
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific dedicated_vantage_point
  oci_apm_synthetics_dedicated_vantage_point_facts:
    # required
    dedicated_vantage_point_id: "ocid1.dedicatedvantagepoint.oc1..xxxxxxEXAMPLExxxxxx"
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

- name: List dedicated_vantage_points
  oci_apm_synthetics_dedicated_vantage_point_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: displayName
    display_name: display_name_example
    name: name_example
    status: ENABLED

"""

RETURN = """
dedicated_vantage_points:
    description:
        - List of DedicatedVantagePoint resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the dedicated vantage point.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.
            returned: on success
            type: str
            sample: display_name_example
        name:
            description:
                - Unique permanent name of the dedicated vantage point. This is the same as the displayName.
            returned: on success
            type: str
            sample: name_example
        status:
            description:
                - Status of the dedicated vantage point.
            returned: on success
            type: str
            sample: ENABLED
        dvp_stack_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dvp_stack_type:
                    description:
                        - Type of stack.
                    returned: on success
                    type: str
                    sample: ORACLE_RM_STACK
                dvp_version:
                    description:
                        - Version of the dedicated vantage point.
                    returned: on success
                    type: str
                    sample: dvp_version_example
                dvp_stack_id:
                    description:
                        - Stack L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Resource Manager stack for dedicated
                          vantage point.
                    returned: on success
                    type: str
                    sample: "ocid1.dvpstack.oc1..xxxxxxEXAMPLExxxxxx"
                dvp_stream_id:
                    description:
                        - Stream L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Resource Manager stack for dedicated
                          vantage point.
                    returned: on success
                    type: str
                    sample: "ocid1.dvpstream.oc1..xxxxxxEXAMPLExxxxxx"
        region:
            description:
                - Name of the region.
            returned: on success
            type: str
            sample: us-phoenix-1
        time_created:
            description:
                - "The time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-13T22:47:12.613Z`"
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
        monitor_status_count_map:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                total:
                    description:
                        - Total number of monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                enabled:
                    description:
                        - Number of enabled monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                disabled:
                    description:
                        - Number of disabled monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                invalid:
                    description:
                        - Number of invalid monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "name": "name_example",
        "status": "ENABLED",
        "dvp_stack_details": {
            "dvp_stack_type": "ORACLE_RM_STACK",
            "dvp_version": "dvp_version_example",
            "dvp_stack_id": "ocid1.dvpstack.oc1..xxxxxxEXAMPLExxxxxx",
            "dvp_stream_id": "ocid1.dvpstream.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "region": "us-phoenix-1",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "monitor_status_count_map": {
            "total": 56,
            "enabled": 56,
            "disabled": 56,
            "invalid": 56
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apm_synthetics import ApmSyntheticClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DedicatedVantagePointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "dedicated_vantage_point_id",
        ]

    def get_required_params_for_list(self):
        return [
            "apm_domain_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dedicated_vantage_point,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            dedicated_vantage_point_id=self.module.params.get(
                "dedicated_vantage_point_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "display_name",
            "name",
            "status",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_dedicated_vantage_points,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            **optional_kwargs
        )


DedicatedVantagePointFactsHelperCustom = get_custom_class(
    "DedicatedVantagePointFactsHelperCustom"
)


class ResourceFactsHelper(
    DedicatedVantagePointFactsHelperCustom, DedicatedVantagePointFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dedicated_vantage_point_id=dict(aliases=["id"], type="str"),
            apm_domain_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["displayName", "name", "timeCreated", "timeUpdated", "status"],
            ),
            display_name=dict(type="str"),
            name=dict(type="str"),
            status=dict(type="str", choices=["ENABLED", "DISABLED"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="dedicated_vantage_point",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(dedicated_vantage_points=result)


if __name__ == "__main__":
    main()
