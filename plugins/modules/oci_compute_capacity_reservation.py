#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_compute_capacity_reservation
short_description: Manage a ComputeCapacityReservation resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ComputeCapacityReservation resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new compute capacity reservation in the specified compartment and availability domain.
      Compute capacity reservations let you reserve instances in a compartment.
      When you launch an instance using this reservation, you are assured that you have enough space for your instance,
      and you won't get out of capacity errors.
      For more information, see L(Reserved Capacity,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).
    - "This resource has the following action operations in the M(oci_compute_capacity_reservation_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the capacity reservation.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name for the compute capacity reservation. Does not have to be unique, and it's
              changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    availability_domain:
        description:
            - The availability domain of this compute capacity reservation.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
        type: str
    is_default_reservation:
        description:
            - Whether this capacity reservation is the default.
              For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm#default).
            - This parameter is updatable.
        type: bool
    instance_reservation_configs:
        description:
            - The reservation configurations for the capacity reservation.
            - To use the reservation for the desired shape, specify the shape, count, and
              optionally the fault domain where you want this configuration.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            instance_shape:
                description:
                    - The shape requested when launching instances using reserved capacity.
                      The shape determines the number of CPUs, amount of memory,
                      and other resources allocated to the instance.
                      You can list all available shapes by calling L(ListComputeCapacityReservationInstanceShapes,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/iaas/computeCapacityReservationInstanceShapes/ListComputeCapacityReservationInstanceShapes).
                type: str
                required: true
            instance_shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the instance.
                        type: float
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the instance, in gigabytes.
                        type: float
            fault_domain:
                description:
                    - The fault domain to use for instances created using this reservation configuration.
                      For more information, see L(Fault Domains,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault).
                      If you do not specify the fault domain, the capacity is available for an instance
                      that does not specify a fault domain. To change the fault domain for a reservation,
                      delete the reservation and create a new one in the preferred fault domain.
                    - To retrieve a list of fault domains, use the `ListFaultDomains` operation in
                      the L(Identity and Access Management Service API,https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/).
                    - "Example: `FAULT-DOMAIN-1`"
                type: str
            reserved_count:
                description:
                    - The amount of capacity to reserve in this reservation configuration.
                type: int
                required: true
    capacity_reservation_id:
        description:
            - The OCID of the compute capacity reservation.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ComputeCapacityReservation.
            - Use I(state=present) to create or update a ComputeCapacityReservation.
            - Use I(state=absent) to delete a ComputeCapacityReservation.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create compute_capacity_reservation
  oci_compute_capacity_reservation:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1

- name: Update compute_capacity_reservation using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_capacity_reservation:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    is_default_reservation: true
    instance_reservation_configs:
    - instance_shape: instance_shape_example
      reserved_count: 56

- name: Update compute_capacity_reservation
  oci_compute_capacity_reservation:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete compute_capacity_reservation
  oci_compute_capacity_reservation:
    capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete compute_capacity_reservation using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_compute_capacity_reservation:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
                - A user-friendly name for the compute capacity reservation.
                  It does not have to be unique, and it's changeable. Avoid entering confidential information.
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
                - The reservation configurations for the capacity reservation.
                - To use the reservation for the desired shape, specify the shape, count, and
                  optionally the fault domain where you want this configuration.
            returned: on success
            type: complex
            contains:
                fault_domain:
                    description:
                        - The fault domain of this reservation configuration.
                          If a value is not supplied, this reservation configuration is applicable to all fault domains in the specified availability domain.
                          For more information, see L(Capacity Reservations,https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).
                    returned: on success
                    type: str
                    sample: fault_domain_example
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
                        - The amount of capacity reserved in this configuration.
                    returned: on success
                    type: int
                    sample: 56
                used_count:
                    description:
                        - The amount of capacity in use out of the total capacity reserved in this reservation configuration.
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
                  for all of the instance reservation configurations under this reservation.
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
            sample: "2016-08-25T21:10:29.600Z"
        time_created:
            description:
                - The date and time the compute capacity reservation was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        used_instance_count:
            description:
                - The total number of instances currently consuming space in
                  this compute capacity reservation. This number is the sum of the values of the `usedCount` fields
                  for all of the instance reservation configurations under this reservation.
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
            "fault_domain": "fault_domain_example",
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
        "time_updated": "2016-08-25T21:10:29.600Z",
        "time_created": "2016-08-25T21:10:29.600Z",
        "used_instance_count": 56
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.core import ComputeClient
    from oci.core.models import CreateComputeCapacityReservationDetails
    from oci.core.models import UpdateComputeCapacityReservationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputeCapacityReservationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ComputeCapacityReservationHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["availability_domain", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_compute_capacity_reservations, **kwargs
        )

    def get_create_model_class(self):
        return CreateComputeCapacityReservationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_compute_capacity_reservation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_compute_capacity_reservation_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateComputeCapacityReservationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_compute_capacity_reservation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                capacity_reservation_id=self.module.params.get(
                    "capacity_reservation_id"
                ),
                update_compute_capacity_reservation_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_compute_capacity_reservation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                capacity_reservation_id=self.module.params.get(
                    "capacity_reservation_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ComputeCapacityReservationHelperCustom = get_custom_class(
    "ComputeCapacityReservationHelperCustom"
)


class ResourceHelper(
    ComputeCapacityReservationHelperCustom, ComputeCapacityReservationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            availability_domain=dict(type="str"),
            is_default_reservation=dict(type="bool"),
            instance_reservation_configs=dict(
                type="list",
                elements="dict",
                options=dict(
                    instance_shape=dict(type="str", required=True),
                    instance_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                        ),
                    ),
                    fault_domain=dict(type="str"),
                    reserved_count=dict(type="int", required=True),
                ),
            ),
            capacity_reservation_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="compute_capacity_reservation",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
