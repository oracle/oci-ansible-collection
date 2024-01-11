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
module: oci_compute_capacity_reservation_facts
short_description: Fetches details about one or multiple ComputeCapacityReservation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ComputeCapacityReservation resources in Oracle Cloud Infrastructure
    - Lists the compute capacity reservations that match the specified criteria and compartment.
    - You can limit the list by specifying a compute capacity reservation display name
      (the list will include all the identically-named compute capacity reservations in the compartment).
    - If I(capacity_reservation_id) is specified, the details of a single ComputeCapacityReservation will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    capacity_reservation_id:
        description:
            - The OCID of the compute capacity reservation.
            - Required to get a specific compute_capacity_reservation.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple compute_capacity_reservations.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "UPDATING"
            - "MOVING"
            - "DELETED"
            - "DELETING"
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
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
- name: Get a specific compute_capacity_reservation
  oci_compute_capacity_reservation_facts:
    # required
    capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"

- name: List compute_capacity_reservations
  oci_compute_capacity_reservation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    availability_domain: Uocm:PHX-AD-1
    lifecycle_state: ACTIVE
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
compute_capacity_reservations:
    description:
        - List of ComputeCapacityReservation resources
    returned: on success
    type: complex
    contains:
        instance_reservation_configs:
            description:
                - The capacity configurations for the capacity reservation.
                - To use the reservation for the desired shape, specify the shape, count, and
                  optionally the fault domain where you want this configuration.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                fault_domain:
                    description:
                        - The fault domain of this capacity configuration.
                          If a value is not supplied, this capacity configuration is applicable to all fault domains in the specified availability domain.
                          For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                cluster_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        hpc_island_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the HPC island.
                            returned: on success
                            type: str
                            sample: "ocid1.hpcisland.oc1..xxxxxxEXAMPLExxxxxx"
                        network_block_ids:
                            description:
                                - The list of OCIDs of the network blocks.
                            returned: on success
                            type: list
                            sample: []
                instance_shape:
                    description:
                        - The shape to use when launching instances using compute capacity reservations. The shape determines the number of CPUs, the amount of
                          memory,
                          and other resources allocated to the instance.
                          You can list all available shapes by calling L(ListComputeCapacityReservationInstanceShapes,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/iaas/computeCapacityReservationInstanceShapes/ListComputeCapacityReservationInstanceShapes).
                    returned: on success
                    type: str
                    sample: instance_shape_example
                instance_shape_config:
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
                reserved_count:
                    description:
                        - The total number of instances that can be launched from the capacity configuration.
                    returned: on success
                    type: int
                    sample: 56
                used_count:
                    description:
                        - The amount of capacity in use out of the total capacity reserved in this capacity configuration.
                    returned: on success
                    type: int
                    sample: 56
        time_updated:
            description:
                - The date and time the compute capacity reservation was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compute capacity reservation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
                  containing the compute capacity reservation.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        lifecycle_state:
            description:
                - The current state of the compute capacity reservation.
            returned: on success
            type: str
            sample: ACTIVE
        availability_domain:
            description:
                - The availability domain of the compute capacity reservation.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        reserved_instance_count:
            description:
                - The number of instances for which capacity will be held with this
                  compute capacity reservation. This number is the sum of the values of the `reservedCount` fields
                  for all of the instance capacity configurations under this reservation.
                  The purpose of this field is to calculate the percentage usage of the reservation.
            returned: on success
            type: int
            sample: 56
        used_instance_count:
            description:
                - The total number of instances currently consuming space in
                  this compute capacity reservation. This number is the sum of the values of the `usedCount` fields
                  for all of the instance capacity configurations under this reservation.
                  The purpose of this field is to calculate the percentage usage of the reservation.
            returned: on success
            type: int
            sample: 56
        is_default_reservation:
            description:
                - Whether this capacity reservation is the default.
                  For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The date and time the compute capacity reservation was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "instance_reservation_configs": [{
            "fault_domain": "FAULT-DOMAIN-1",
            "cluster_config": {
                "hpc_island_id": "ocid1.hpcisland.oc1..xxxxxxEXAMPLExxxxxx",
                "network_block_ids": []
            },
            "instance_shape": "instance_shape_example",
            "instance_shape_config": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            },
            "reserved_count": 56,
            "used_count": 56
        }],
        "time_updated": "2013-10-20T19:20:30+01:00",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "lifecycle_state": "ACTIVE",
        "availability_domain": "Uocm:PHX-AD-1",
        "reserved_instance_count": 56,
        "used_instance_count": 56,
        "is_default_reservation": true,
        "time_created": "2013-10-20T19:20:30+01:00"
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


class ComputeCapacityReservationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "capacity_reservation_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_compute_capacity_reservation,
            capacity_reservation_id=self.module.params.get("capacity_reservation_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "availability_domain",
            "lifecycle_state",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_compute_capacity_reservations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ComputeCapacityReservationFactsHelperCustom = get_custom_class(
    "ComputeCapacityReservationFactsHelperCustom"
)


class ResourceFactsHelper(
    ComputeCapacityReservationFactsHelperCustom,
    ComputeCapacityReservationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            capacity_reservation_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "UPDATING",
                    "MOVING",
                    "DELETED",
                    "DELETING",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="compute_capacity_reservation",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(compute_capacity_reservations=result)


if __name__ == "__main__":
    main()
