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
module: oci_compute_capacity_reservation_instance_facts
short_description: Fetches details about one or multiple CapacityReservationInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CapacityReservationInstance resources in Oracle Cloud Infrastructure
    - Lists the instances launched under a capacity reservation. You can filter results by specifying criteria.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    capacity_reservation_id:
        description:
            - The OCID of the compute capacity reservation.
        type: str
        required: true
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List capacity_reservation_instances
  oci_compute_capacity_reservation_instance_facts:
    # required
    capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
capacity_reservation_instances:
    description:
        - List of CapacityReservationInstance resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - The availability domain the instance is running in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the instance.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        fault_domain:
            description:
                - The fault domain the instance is running in.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        shape_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs available to the instance.
                    returned: on success
                    type: float
                    sample: 3.4
                memory_in_gbs:
                    description:
                        - The total amount of memory available to the instance, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
        shape:
            description:
                - The shape of the instance. The shape determines the number of CPUs, amount of memory,
                  and other resources allocated to the instance.
                - You can enumerate all available shapes by calling L(ListComputeCapacityReservationInstanceShapes,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/computeCapacityReservationInstanceShapes/ListComputeCapacityReservationInstanceShapes).
            returned: on success
            type: str
            sample: shape_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "fault_domain": "FAULT-DOMAIN-1",
        "shape_config": {
            "ocpus": 3.4,
            "memory_in_gbs": 3.4
        },
        "shape": "shape_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CapacityReservationInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "capacity_reservation_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "compartment_id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_compute_capacity_reservation_instances,
            capacity_reservation_id=self.module.params.get("capacity_reservation_id"),
            **optional_kwargs
        )


CapacityReservationInstanceFactsHelperCustom = get_custom_class(
    "CapacityReservationInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    CapacityReservationInstanceFactsHelperCustom,
    CapacityReservationInstanceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            capacity_reservation_id=dict(type="str", required=True),
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="capacity_reservation_instance",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(capacity_reservation_instances=result)


if __name__ == "__main__":
    main()
