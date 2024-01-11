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
module: oci_compute_capacity_report
short_description: Manage a ComputeCapacityReport resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a ComputeCapacityReport resource in Oracle Cloud Infrastructure
    - For I(state=present), generates a report of the host capacity within an availability domain that is available for you
      to create compute instances. Host capacity is the physical infrastructure that resources such as compute
      instances run on.
    - Use the capacity report to determine whether sufficient capacity is available for a shape before
      you create an instance or change the shape of an instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the compartment. This should always be the root
              compartment.
        type: str
        required: true
    availability_domain:
        description:
            - The availability domain for the capacity report.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
        required: true
    shape_availabilities:
        description:
            - Information about the shapes in the capacity report.
        type: list
        elements: dict
        required: true
        suboptions:
            fault_domain:
                description:
                    - The fault domain for the capacity report.
                    - If you do not specify a fault domain, the capacity report includes information about all fault domains.
                type: str
            instance_shape:
                description:
                    - The shape that you want to request a capacity report for. You can enumerate all available shapes by calling
                      L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
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
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage.
                        type: int
    state:
        description:
            - The state of the ComputeCapacityReport.
            - Use I(state=present) to create a ComputeCapacityReport.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create compute_capacity_report
  oci_compute_capacity_report:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    shape_availabilities:
    - # required
      instance_shape: instance_shape_example

      # optional
      fault_domain: FAULT-DOMAIN-1
      instance_shape_config:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
        nvmes: 56

"""

RETURN = """
compute_capacity_report:
    description:
        - Details of the ComputeCapacityReport resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the compartment. This should always be the root
                  compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - The availability domain for the capacity report.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        shape_availabilities:
            description:
                - Information about the available capacity for each shape in a capacity report.
            returned: on success
            type: complex
            contains:
                fault_domain:
                    description:
                        - The fault domain for the capacity report.
                        - If you do not specify the fault domain, the capacity report includes information about all fault domains.
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                instance_shape:
                    description:
                        - The shape that the capacity report was requested for.
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
                        nvmes:
                            description:
                                - The number of NVMe drives to be used for storage.
                            returned: on success
                            type: int
                            sample: 56
                available_count:
                    description:
                        - The total number of new instances that can be created with the specified shape configuration.
                    returned: on success
                    type: int
                    sample: 56
                availability_status:
                    description:
                        - A flag denoting whether capacity is available.
                    returned: on success
                    type: str
                    sample: OUT_OF_HOST_CAPACITY
        time_created:
            description:
                - The date and time the capacity report was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "shape_availabilities": [{
            "fault_domain": "FAULT-DOMAIN-1",
            "instance_shape": "instance_shape_example",
            "instance_shape_config": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4,
                "nvmes": 56
            },
            "available_count": 56,
            "availability_status": "OUT_OF_HOST_CAPACITY"
        }],
        "time_created": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeClient
    from oci.core.models import CreateComputeCapacityReportDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputeCapacityReportHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_possible_entity_types(self):
        return super(
            ComputeCapacityReportHelperGen, self
        ).get_possible_entity_types() + [
            "computecapacityreport",
            "computecapacityreports",
            "corecomputecapacityreport",
            "corecomputecapacityreports",
            "computecapacityreportresource",
            "computecapacityreportsresource",
            "core",
        ]

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return CreateComputeCapacityReportDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_compute_capacity_report,
            call_fn_args=(),
            call_fn_kwargs=dict(create_compute_capacity_report_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


ComputeCapacityReportHelperCustom = get_custom_class(
    "ComputeCapacityReportHelperCustom"
)


class ResourceHelper(ComputeCapacityReportHelperCustom, ComputeCapacityReportHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str", required=True),
            shape_availabilities=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    fault_domain=dict(type="str"),
                    instance_shape=dict(type="str", required=True),
                    instance_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="float"),
                            memory_in_gbs=dict(type="float"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="compute_capacity_report",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
