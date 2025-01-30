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
module: oci_apm_synthetics_monitor_result_facts
short_description: Fetches details about a MonitorResult resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a MonitorResult resource in Oracle Cloud Infrastructure
    - Gets the results for a specific execution of a monitor identified by OCID. The results are in a HAR file, Screenshot, Console Log or Network details.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    monitor_id:
        description:
            - The OCID of the monitor.
        type: str
        required: true
    vantage_point:
        description:
            - The vantagePoint name.
        type: str
        required: true
    result_type:
        description:
            - "The result type: har, screenshot, log, or network."
        type: str
        required: true
    result_content_type:
        description:
            - "The result content type: zip or raw."
        type: str
        required: true
    execution_time:
        description:
            - The time the object was posted.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific monitor_result
  oci_apm_synthetics_monitor_result_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    monitor_id: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"
    vantage_point: vantage_point_example
    result_type: result_type_example
    result_content_type: result_content_type_example
    execution_time: execution_time_example

"""

RETURN = """
monitor_result:
    description:
        - MonitorResult resource
    returned: on success
    type: complex
    contains:
        result_type:
            description:
                - "Type of result.
                  Example: HAR, Screenshot, Log or Network."
            returned: on success
            type: str
            sample: result_type_example
        result_content_type:
            description:
                - "Type of result content.
                  Example: Zip or Raw file."
            returned: on success
            type: str
            sample: result_content_type_example
        result_data_set:
            description:
                - Monitor result data set.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of the data.
                    returned: on success
                    type: str
                    sample: name_example
                byte_content:
                    description:
                        - "Data content in byte format.
                          Example: Zip or Screenshot."
                    returned: on success
                    type: str
                    sample: "null"

                string_content:
                    description:
                        - "Data content in string format.
                          Example: HAR."
                    returned: on success
                    type: str
                    sample: string_content_example
                timestamp:
                    description:
                        - "The time when the data was generated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                          timestamp format.
                          Example: `2020-02-13T22:47:12.613Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        monitor_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the monitor.
            returned: on success
            type: str
            sample: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"
        vantage_point:
            description:
                - The name of the public or dedicated vantage point.
            returned: on success
            type: str
            sample: vantage_point_example
        execution_time:
            description:
                - The specific point of time when the result of an execution is collected.
            returned: on success
            type: str
            sample: execution_time_example
    sample: {
        "result_type": "result_type_example",
        "result_content_type": "result_content_type_example",
        "result_data_set": [{
            "name": "name_example",
            "byte_content": null,
            "string_content": "string_content_example",
            "timestamp": "2013-10-20T19:20:30+01:00"
        }],
        "monitor_id": "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx",
        "vantage_point": "vantage_point_example",
        "execution_time": "execution_time_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apm_synthetics import ApmSyntheticClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MonitorResultFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "monitor_id",
            "vantage_point",
            "result_type",
            "result_content_type",
            "execution_time",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_monitor_result,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            monitor_id=self.module.params.get("monitor_id"),
            vantage_point=self.module.params.get("vantage_point"),
            result_type=self.module.params.get("result_type"),
            result_content_type=self.module.params.get("result_content_type"),
            execution_time=self.module.params.get("execution_time"),
        )


MonitorResultFactsHelperCustom = get_custom_class("MonitorResultFactsHelperCustom")


class ResourceFactsHelper(MonitorResultFactsHelperCustom, MonitorResultFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            monitor_id=dict(type="str", required=True),
            vantage_point=dict(type="str", required=True),
            result_type=dict(type="str", required=True),
            result_content_type=dict(type="str", required=True),
            execution_time=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="monitor_result",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(monitor_result=result)


if __name__ == "__main__":
    main()
