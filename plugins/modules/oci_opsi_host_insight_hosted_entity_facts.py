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
module: oci_opsi_host_insight_hosted_entity_facts
short_description: Fetches details about one or multiple HostInsightHostedEntity resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HostInsightHostedEntity resources in Oracle Cloud Infrastructure
    - Get a list of hosted entities details.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    id:
        description:
            - Required L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host insight resource.
        type: str
        required: true
    analysis_time_interval:
        description:
            - Specify time period in ISO 8601 format with respect to current time.
              Default is last 30 days represented by P30D.
              If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
              Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to
              current time (P25M).
        type: str
    time_interval_start:
        description:
            - Analysis start time in UTC in ISO 8601 format(inclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              The minimum allowed value is 2 years prior to the current day.
              timeIntervalStart and timeIntervalEnd parameters are used together.
              If analysisTimeInterval is specified, this parameter is ignored.
        type: str
    time_interval_end:
        description:
            - Analysis end time in UTC in ISO 8601 format(exclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              timeIntervalStart and timeIntervalEnd are used together.
              If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.
        type: str
    platform_type:
        description:
            - "Filter by one or more platform types.
              Supported platformType(s) for MACS-managed external host insight: [LINUX].
              Supported platformType(s) for MACS-managed cloud host insight: [LINUX].
              Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX]."
        type: list
        elements: str
        choices:
            - "LINUX"
            - "SOLARIS"
            - "SUNOS"
            - "ZLINUX"
    exadata_insight_id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of exadata insight resource.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Hosted entity list sort options.
        type: str
        choices:
            - "entityName"
            - "entityType"
    host_type:
        description:
            - Filter by one or more host types.
              Possible values are CLOUD-HOST, EXTERNAL-HOST
        type: list
        elements: str
    host_id:
        description:
            - Optional L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host (Compute Id)
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List host_insight_hosted_entities
  oci_opsi_host_insight_hosted_entity_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    platform_type: [ "LINUX" ]
    exadata_insight_id: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: entityName
    host_type: [ "host_type_example" ]
    host_id: "ocid1.host.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
host_insight_hosted_entities:
    description:
        - List of HostInsightHostedEntity resources
    returned: on success
    type: complex
    contains:
        entity_identifier:
            description:
                - The identifier of the entity.
            returned: on success
            type: str
            sample: entity_identifier_example
        entity_name:
            description:
                - The entity name.
            returned: on success
            type: str
            sample: entity_name_example
        entity_type:
            description:
                - The entity type.
            returned: on success
            type: str
            sample: entity_type_example
    sample: [{
        "entity_identifier": "entity_identifier_example",
        "entity_name": "entity_name_example",
        "entity_type": "entity_type_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HostInsightHostedEntityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "exadata_insight_id",
            "sort_order",
            "sort_by",
            "host_type",
            "host_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_hosted_entities,
            compartment_id=self.module.params.get("compartment_id"),
            id=self.module.params.get("id"),
            **optional_kwargs
        )


HostInsightHostedEntityFactsHelperCustom = get_custom_class(
    "HostInsightHostedEntityFactsHelperCustom"
)


class ResourceFactsHelper(
    HostInsightHostedEntityFactsHelperCustom, HostInsightHostedEntityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            id=dict(type="str", required=True),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            platform_type=dict(
                type="list",
                elements="str",
                choices=["LINUX", "SOLARIS", "SUNOS", "ZLINUX"],
            ),
            exadata_insight_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["entityName", "entityType"]),
            host_type=dict(type="list", elements="str"),
            host_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="host_insight_hosted_entity",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(host_insight_hosted_entities=result)


if __name__ == "__main__":
    main()
