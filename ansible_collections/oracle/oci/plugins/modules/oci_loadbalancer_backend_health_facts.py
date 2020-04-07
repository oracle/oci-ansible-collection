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
module: oci_loadbalancer_backend_health_facts
short_description: Fetches details about a BackendHealth resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a BackendHealth resource in Oracle Cloud Infrastructure
    - Gets the current health status of the specified backend server.
version_added: "2.5"
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer associated with the backend server health
              status to be retrieved.
        type: str
        required: true
    backend_set_name:
        description:
            - The name of the backend set associated with the backend server to retrieve the health status for.
            - "Example: `example_backend_set`"
        type: str
        required: true
    backend_name:
        description:
            - The IP address and port of the backend server to retrieve the health status for.
            - "Example: `10.0.0.3:8080`"
        type: str
        required: true
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific backend_health
  oci_loadbalancer_backend_health_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    backend_set_name: example_backend_set
    backend_name: 10.0.0.3:8080

"""

RETURN = """
backend_health:
    description:
        - BackendHealth resource
    returned: on success
    type: complex
    contains:
        status:
            description:
                - The general health status of the specified backend server as reported by the primary and standby load balancers.
                - "*   **OK:** Both health checks returned `OK`."
                - "*   **WARNING:** One health check returned `OK` and one did not."
                - "*   **CRITICAL:** Neither health check returned `OK`."
                - "*   **UNKNOWN:** One or both health checks returned `UNKNOWN`, or the system was unable to retrieve metrics at this time."
            returned: on success
            type: string
            sample: OK
        health_check_results:
            description:
                - A list of the most recent health check results returned for the specified backend server.
            returned: on success
            type: complex
            contains:
                subnet_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet hosting the load balancer that
                          reported this health check status.
                    returned: on success
                    type: string
                    sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
                source_ip_address:
                    description:
                        - The IP address of the health check status report provider. This identifier helps you differentiate same-subnet
                          load balancers that report health check status.
                        - "Example: `10.0.0.7`"
                    returned: on success
                    type: string
                    sample: 10.0.0.7
                timestamp:
                    description:
                        - The date and time the data was retrieved, in the format defined by RFC3339.
                        - "Example: `2017-06-02T18:28:11+00:00`"
                    returned: on success
                    type: string
                    sample: 2017-06-02T18:28:11+00:00
                health_check_status:
                    description:
                        - The result of the most recent health check.
                    returned: on success
                    type: string
                    sample: OK
    sample: {
        "status": "OK",
        "health_check_results": [{
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "source_ip_address": "10.0.0.7",
            "timestamp": "2017-06-02T18:28:11+00:00",
            "health_check_status": "OK"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackendHealthFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "backend_set_name",
            "backend_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend_health,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
            backend_name=self.module.params.get("backend_name"),
        )


BackendHealthFactsHelperCustom = get_custom_class("BackendHealthFactsHelperCustom")


class ResourceFactsHelper(BackendHealthFactsHelperCustom, BackendHealthFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True),
            backend_set_name=dict(type="str", required=True),
            backend_name=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backend_health",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(backend_health=result)


if __name__ == "__main__":
    main()
