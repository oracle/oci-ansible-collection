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
module: oci_optimizer_enrollment_status_facts
short_description: Fetches details about one or multiple EnrollmentStatus resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple EnrollmentStatus resources in Oracle Cloud Infrastructure
    - Lists the Cloud Advisor enrollment statuses.
    - If I(enrollment_status_id) is specified, the details of a single EnrollmentStatus will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    enrollment_status_id:
        description:
            - The unique OCID associated with the enrollment status.
            - Required to get a specific enrollment_status.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple enrollment_statuses.
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
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is
              ascending. The NAME sort order is case sensitive.
        type: str
        choices:
            - "NAME"
            - "TIMECREATED"
    lifecycle_state:
        description:
            - A filter that returns results that match the lifecycle state specified.
        type: str
        choices:
            - "ACTIVE"
            - "FAILED"
            - "INACTIVE"
            - "ATTACHING"
            - "DETACHING"
            - "DELETING"
            - "DELETED"
            - "UPDATING"
            - "CREATING"
    status:
        description:
            - A filter that returns results that match the Cloud Advisor enrollment status specified.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List enrollment_statuses
  oci_optimizer_enrollment_status_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific enrollment_status
  oci_optimizer_enrollment_status_facts:
    enrollment_status_id: "ocid1.enrollmentstatus.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
enrollment_statuses:
    description:
        - List of EnrollmentStatus resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the enrollment status.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The enrollment status' current state.
            returned: on success
            type: str
            sample: ACTIVE
        status:
            description:
                - The current Cloud Advisor enrollment status.
            returned: on success
            type: str
            sample: ACTIVE
        status_reason:
            description:
                - The reason for the enrollment status of the tenancy.
            returned: on success
            type: str
            sample: status_reason_example
        time_created:
            description:
                - The date and time the enrollment status was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2020-08-25T21:10:29.600Z"
        time_updated:
            description:
                - The date and time the enrollment status was last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2020-08-25T21:10:29.600Z"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "status": "ACTIVE",
        "status_reason": "status_reason_example",
        "time_created": "2020-08-25T21:10:29.600Z",
        "time_updated": "2020-08-25T21:10:29.600Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.optimizer import OptimizerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EnrollmentStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "enrollment_status_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_enrollment_status,
            enrollment_status_id=self.module.params.get("enrollment_status_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "status",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_enrollment_statuses,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


EnrollmentStatusFactsHelperCustom = get_custom_class(
    "EnrollmentStatusFactsHelperCustom"
)


class ResourceFactsHelper(
    EnrollmentStatusFactsHelperCustom, EnrollmentStatusFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            enrollment_status_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAME", "TIMECREATED"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "FAILED",
                    "INACTIVE",
                    "ATTACHING",
                    "DETACHING",
                    "DELETING",
                    "DELETED",
                    "UPDATING",
                    "CREATING",
                ],
            ),
            status=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="enrollment_status",
        service_client_class=OptimizerClient,
        namespace="optimizer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(enrollment_statuses=result)


if __name__ == "__main__":
    main()
