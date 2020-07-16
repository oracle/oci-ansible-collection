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
module: oci_healthchecks_http_probe
short_description: Manage a HttpProbe resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a HttpProbe resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an on-demand HTTP probe. The location response header contains the URL for
      fetching the probe results.
    - "*Note:* On-demand probe configurations are not saved."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        required: true
    targets:
        description:
            - A list of targets (hostnames or IP addresses) of the probe.
        type: list
        required: true
    vantage_point_names:
        description:
            - A list of names of vantage points from which to execute the probe.
        type: list
    port:
        description:
            - The port on which to probe endpoints. If unspecified, probes will use the
              default port of their protocol.
        type: int
    timeout_in_seconds:
        description:
            - "The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
              The probe timeout must be less than or equal to `intervalInSeconds` for monitors."
        type: int
    protocol:
        description:
            - ""
        type: str
        choices:
            - "HTTP"
            - "HTTPS"
        required: true
    method:
        description:
            - ""
        type: str
        choices:
            - "GET"
            - "HEAD"
    path:
        description:
            - The optional URL path to probe, including query parameters.
        type: str
    headers:
        description:
            - A dictionary of HTTP request headers.
            - "*Note:* Monitors and probes do not support the use of the `Authorization` HTTP header."
        type: dict
    state:
        description:
            - The state of the HttpProbe.
            - Use I(state=present) to create a HttpProbe.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create http_probe
  oci_healthchecks_http_probe:
    compartment_id: ocid1.tenancy.oc1...
    targets:
    - 192.0.2.0
    protocol: HTTP

"""

RETURN = """
http_probe:
    description:
        - Details of the HttpProbe resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        results_url:
            description:
                - A URL for fetching the probe results.
            returned: on success
            type: string
            sample: results_url_example
        home_region:
            description:
                - The region where updates must be made and where results must be fetched from.
            returned: on success
            type: string
            sample: home_region_example
        time_created:
            description:
                - The RFC 3339-formatted creation date and time of the probe.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        targets:
            description:
                - A list of targets (hostnames or IP addresses) of the probe.
            returned: on success
            type: list
            sample: []
        vantage_point_names:
            description:
                - A list of names of vantage points from which to execute the probe.
            returned: on success
            type: list
            sample: []
        port:
            description:
                - The port on which to probe endpoints. If unspecified, probes will use the
                  default port of their protocol.
            returned: on success
            type: int
            sample: 56
        timeout_in_seconds:
            description:
                - "The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
                  The probe timeout must be less than or equal to `intervalInSeconds` for monitors."
            returned: on success
            type: int
            sample: 56
        protocol:
            description:
                - ""
            returned: on success
            type: string
            sample: HTTP
        method:
            description:
                - ""
            returned: on success
            type: string
            sample: GET
        path:
            description:
                - The optional URL path to probe, including query parameters.
            returned: on success
            type: string
            sample: path_example
        headers:
            description:
                - A dictionary of HTTP request headers.
                - "*Note:* Monitors and probes do not support the use of the `Authorization` HTTP header."
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "results_url": "results_url_example",
        "home_region": "home_region_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "targets": [],
        "vantage_point_names": [],
        "port": 56,
        "timeout_in_seconds": 56,
        "protocol": "HTTP",
        "method": "GET",
        "path": "path_example",
        "headers": {}
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
    from oci.healthchecks import HealthChecksClient
    from oci.healthchecks.models import CreateOnDemandHttpProbeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HttpProbeHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return CreateOnDemandHttpProbeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_on_demand_http_probe,
            call_fn_args=(),
            call_fn_kwargs=dict(create_on_demand_http_probe_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )


HttpProbeHelperCustom = get_custom_class("HttpProbeHelperCustom")


class ResourceHelper(HttpProbeHelperCustom, HttpProbeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            targets=dict(type="list", required=True),
            vantage_point_names=dict(type="list"),
            port=dict(type="int"),
            timeout_in_seconds=dict(type="int"),
            protocol=dict(type="str", required=True, choices=["HTTP", "HTTPS"]),
            method=dict(type="str", choices=["GET", "HEAD"]),
            path=dict(type="str"),
            headers=dict(type="dict"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="http_probe",
        service_client_class=HealthChecksClient,
        namespace="healthchecks",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
