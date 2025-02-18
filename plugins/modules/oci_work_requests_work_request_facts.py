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
module: oci_work_requests_work_request_facts
short_description: Fetches details about one or multiple WorkRequest resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WorkRequest resources in Oracle Cloud Infrastructure
    - Lists the work requests in a compartment or for a specified resource.
    - If I(work_request_id) is specified, the details of a single WorkRequest will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    work_request_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the work request.
            - Required to get a specific work_request.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple work_requests.
        type: str
    resource_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific work_request
  oci_work_requests_work_request_facts:
    # required
    work_request_id: "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"

- name: List work_requests
  oci_work_requests_work_request_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
work_requests:
    description:
        - List of WorkRequest resources
    returned: on success
    type: complex
    contains:
        resources:
            description:
                - The resources that are affected by this work request.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                action_type:
                    description:
                        - The way in which this resource was affected by the operation that spawned the work
                          request.
                    returned: on success
                    type: str
                    sample: CREATED
                entity_type:
                    description:
                        - The resource type the work request affects.
                    returned: on success
                    type: str
                    sample: entity_type_example
                identifier:
                    description:
                        - An L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) or other unique identifier for the
                          resource.
                    returned: on success
                    type: str
                    sample: identifier_example
                entity_uri:
                    description:
                        - The URI path that you can use for a GET request to access the resource metadata.
                    returned: on success
                    type: str
                    sample: entity_uri_example
        operation_type:
            description:
                - The asynchronous operation tracked by this work request.
            returned: on success
            type: str
            sample: operation_type_example
        status:
            description:
                - The status of the work request.
            returned: on success
            type: str
            sample: ACCEPTED
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the work request.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment
                  that contains the work request.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        percent_complete:
            description:
                - The percentage complete of the operation tracked by this work request.
            returned: on success
            type: float
            sample: 3.4
        time_accepted:
            description:
                - The date and time the work request was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`,
                  in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`.
                  Format is defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "resources": [{
            "action_type": "CREATED",
            "entity_type": "entity_type_example",
            "identifier": "identifier_example",
            "entity_uri": "entity_uri_example"
        }],
        "operation_type": "operation_type_example",
        "status": "ACCEPTED",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "percent_complete": 3.4,
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WorkRequestFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "work_request_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_work_request,
            work_request_id=self.module.params.get("work_request_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "resource_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_work_requests,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


WorkRequestFactsHelperCustom = get_custom_class("WorkRequestFactsHelperCustom")


class ResourceFactsHelper(WorkRequestFactsHelperCustom, WorkRequestFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            work_request_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            resource_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="work_request",
        service_client_class=WorkRequestClient,
        namespace="work_requests",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(work_requests=result)


if __name__ == "__main__":
    main()
