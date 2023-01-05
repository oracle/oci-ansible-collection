#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_compute_capacity_reservation_actions
short_description: Perform actions on a ComputeCapacityReservation resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ComputeCapacityReservation resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a compute capacity reservation into a different compartment. For information about
      moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    capacity_reservation_id:
        description:
            - The OCID of the compute capacity reservation.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
              to move the compute capacity reservation to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ComputeCapacityReservation.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on compute_capacity_reservation
  oci_compute_capacity_reservation_actions:
    # required
    capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
compute_capacity_reservation:
    description:
        - Details of the ComputeCapacityReservation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the compute capacity reservation.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
                  containing the compute capacity reservation.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compute capacity reservation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_default_reservation:
            description:
                - Whether this capacity reservation is the default.
                  For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
            returned: on success
            type: bool
            sample: true
        instance_reservation_configs:
            description:
                - The capacity configurations for the capacity reservation.
                - To use the reservation for the desired shape, specify the shape, count, and
                  optionally the fault domain where you want this configuration.
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
        lifecycle_state:
            description:
                - The current state of the compute capacity reservation.
            returned: on success
            type: str
            sample: ACTIVE
        reserved_instance_count:
            description:
                - The number of instances for which capacity will be held with this
                  compute capacity reservation. This number is the sum of the values of the `reservedCount` fields
                  for all of the instance capacity configurations under this reservation.
                  The purpose of this field is to calculate the percentage usage of the reservation.
            returned: on success
            type: int
            sample: 56
        time_updated:
            description:
                - The date and time the compute capacity reservation was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date and time the compute capacity reservation was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        used_instance_count:
            description:
                - The total number of instances currently consuming space in
                  this compute capacity reservation. This number is the sum of the values of the `usedCount` fields
                  for all of the instance capacity configurations under this reservation.
                  The purpose of this field is to calculate the percentage usage of the reservation.
            returned: on success
            type: int
            sample: 56
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_default_reservation": true,
        "instance_reservation_configs": [{
            "fault_domain": "FAULT-DOMAIN-1",
            "instance_shape": "instance_shape_example",
            "instance_shape_config": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            },
            "reserved_count": 56,
            "used_count": 56
        }],
        "lifecycle_state": "ACTIVE",
        "reserved_instance_count": 56,
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "used_instance_count": 56
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeClient
    from oci.core.models import ChangeComputeCapacityReservationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputeCapacityReservationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def __init__(self, *args, **kwargs):
        super(ComputeCapacityReservationActionsHelperGen, self).__init__(
            *args, **kwargs
        )
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "capacity_reservation_id"

    def get_module_resource_id(self):
        return self.module.params.get("capacity_reservation_id")

    def get_get_fn(self):
        return self.client.get_compute_capacity_reservation

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_compute_capacity_reservation,
            capacity_reservation_id=self.module.params.get("capacity_reservation_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeComputeCapacityReservationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_compute_capacity_reservation_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                capacity_reservation_id=self.module.params.get(
                    "capacity_reservation_id"
                ),
                change_compute_capacity_reservation_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ComputeCapacityReservationActionsHelperCustom = get_custom_class(
    "ComputeCapacityReservationActionsHelperCustom"
)


class ResourceHelper(
    ComputeCapacityReservationActionsHelperCustom,
    ComputeCapacityReservationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            capacity_reservation_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="compute_capacity_reservation",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
