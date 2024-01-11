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
module: oci_container_engine_workload_mapping_facts
short_description: Fetches details about one or multiple WorkloadMapping resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WorkloadMapping resources in Oracle Cloud Infrastructure
    - List workloadMappings for a provisioned cluster.
    - If I(workload_mapping_id) is specified, the details of a single WorkloadMapping will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    workload_mapping_id:
        description:
            - The OCID of the workloadMapping.
            - Required to get a specific workload_mapping.
        type: str
        aliases: ["id"]
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    sort_order:
        description:
            - The optional order in which to sort the results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The optional field to sort the results by.
        type: str
        choices:
            - "NAMESPACE"
            - "TIMECREATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific workload_mapping
  oci_container_engine_workload_mapping_facts:
    # required
    workload_mapping_id: "ocid1.workloadmapping.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List workload_mappings
  oci_container_engine_workload_mapping_facts:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: NAMESPACE

"""

RETURN = """
workload_mappings:
    description:
        - List of WorkloadMapping resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The ocid of the workloadMapping.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_id:
            description:
                - The OCID of the cluster.
            returned: on success
            type: str
            sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - The namespace of the workloadMapping.
            returned: on success
            type: str
            sample: namespace_example
        mapped_tenancy_id:
            description:
                - The OCID of the mapped customer tenancy.
            returned: on success
            type: str
            sample: "ocid1.mappedtenancy.oc1..xxxxxxEXAMPLExxxxxx"
        mapped_compartment_id:
            description:
                - The OCID of the mapped customer compartment.
            returned: on success
            type: str
            sample: "ocid1.mappedcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the workloadMapping.
            returned: on success
            type: str
            sample: CREATING
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "mapped_tenancy_id": "ocid1.mappedtenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "mapped_compartment_id": "ocid1.mappedcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
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
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WorkloadMappingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cluster_id",
            "workload_mapping_id",
        ]

    def get_required_params_for_list(self):
        return [
            "cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_workload_mapping,
            cluster_id=self.module.params.get("cluster_id"),
            workload_mapping_id=self.module.params.get("workload_mapping_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_workload_mappings,
            cluster_id=self.module.params.get("cluster_id"),
            **optional_kwargs
        )


WorkloadMappingFactsHelperCustom = get_custom_class("WorkloadMappingFactsHelperCustom")


class ResourceFactsHelper(
    WorkloadMappingFactsHelperCustom, WorkloadMappingFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            workload_mapping_id=dict(aliases=["id"], type="str"),
            cluster_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAMESPACE", "TIMECREATED"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="workload_mapping",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(workload_mappings=result)


if __name__ == "__main__":
    main()
