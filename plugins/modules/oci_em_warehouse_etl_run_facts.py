#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_em_warehouse_etl_run_facts
short_description: Fetches details about one or multiple EtlRun resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple EtlRun resources in Oracle Cloud Infrastructure
    - Gets a list of runs of an EmWarehouseResource by identifier
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    em_warehouse_id:
        description:
            - unique EmWarehouse identifier
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List etl_runs
  oci_em_warehouse_etl_run_facts:
    # required
    em_warehouse_id: "ocid1.emwarehouse.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
etl_runs:
    description:
        - List of EtlRun resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        data_read_in_bytes:
            description:
                - Data read by the dataflow run
            returned: on success
            type: int
            sample: 56
        data_written:
            description:
                - Data written by the dataflow run
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the etlRun.
            returned: on success
            type: str
            sample: ACCEPTED
        display_name:
            description:
                - The name of the ETLRun.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_details:
            description:
                - Details of the lifecycle state
            returned: on success
            type: str
            sample: lifecycle_details_example
        run_duration_in_milliseconds:
            description:
                - Dataflow run duration
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - Time when the dataflow run was created
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time when the dataflow run was updated
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
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "data_read_in_bytes": 56,
        "data_written": 56,
        "lifecycle_state": "ACCEPTED",
        "display_name": "display_name_example",
        "lifecycle_details": "lifecycle_details_example",
        "run_duration_in_milliseconds": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.em_warehouse import EmWarehouseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EtlRunFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "em_warehouse_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_etl_runs,
            em_warehouse_id=self.module.params.get("em_warehouse_id"),
            **optional_kwargs
        )


EtlRunFactsHelperCustom = get_custom_class("EtlRunFactsHelperCustom")


class ResourceFactsHelper(EtlRunFactsHelperCustom, EtlRunFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            em_warehouse_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="etl_run",
        service_client_class=EmWarehouseClient,
        namespace="em_warehouse",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(etl_runs=result)


if __name__ == "__main__":
    main()
