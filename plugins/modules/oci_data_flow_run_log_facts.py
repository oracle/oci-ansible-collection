#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_data_flow_run_log_facts
short_description: Fetches details about one or multiple RunLog resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RunLog resources in Oracle Cloud Infrastructure
    - Retrieves summaries of the run's logs.
version_added: "2.9"
author: Oracle (@oracle)
options:
    run_id:
        description:
            - The unique ID for the run
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List run_logs
  oci_data_flow_run_log_facts:
    run_id: ocid1.run.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
run_logs:
    description:
        - List of RunLog resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - "The name of the log.
                  Example: spark_driver_stderr_20190917T114000Z.log.gz"
            returned: on success
            type: string
            sample: name_example
        run_id:
            description:
                - The runId associated with the log.
            returned: on success
            type: string
            sample: ocid1.run.oc1..xxxxxxEXAMPLExxxxxx
        size_in_bytes:
            description:
                - The size of the object in bytes.
            returned: on success
            type: int
            sample: 56
        source:
            description:
                - The source of the log such as driver and executor.
            returned: on success
            type: string
            sample: APPLICATION
        time_created:
            description:
                - The date and time the object was created, as described in L(RFC 2616,https://tools.ietf.org/rfc/rfc2616), section 14.29.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        type:
            description:
                - The type of log such as stdout and stderr.
            returned: on success
            type: string
            sample: STDERR
    sample: [{
        "name": "name_example",
        "run_id": "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx",
        "size_in_bytes": 56,
        "source": "APPLICATION",
        "time_created": "2013-10-20T19:20:30+01:00",
        "type": "STDERR"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_flow import DataFlowClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowRunLogFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "run_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_run_logs,
            run_id=self.module.params.get("run_id"),
            **optional_kwargs
        )


DataFlowRunLogFactsHelperCustom = get_custom_class("DataFlowRunLogFactsHelperCustom")


class ResourceFactsHelper(
    DataFlowRunLogFactsHelperCustom, DataFlowRunLogFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(run_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="run_log",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(run_logs=result)


if __name__ == "__main__":
    main()
