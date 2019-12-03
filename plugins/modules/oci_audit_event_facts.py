#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_audit_event_facts
short_description: Fetches details about one or multiple AuditEvent resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AuditEvent resources in Oracle Cloud Infrastructure
    - Returns all audit events for the specified compartment that were processed within the specified time range.
version_added: "2.5"
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        required: true
    start_time:
        description:
            - Returns events that were processed at or after this start date and time, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
              format.
              For example, a start value of `2017-01-15T11:30:00Z` will retrieve a list of all events processed since 30 minutes after the 11th hour of January
              15, 2017, in Coordinated Universal Time (UTC).
              You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`.
        required: true
    end_time:
        description:
            - Returns events that were processed before this end date and time, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
              For example, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-01-02T00:00:00Z` will retrieve a list of all events processed on
              January 1, 2017.
              Similarly, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-02-01T00:00:00Z` will result in a list of all events processed
              between January 1, 2017 and January 31, 2017.
              You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`.
        required: true
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: List audit_events
  oci_audit_event_facts:
      compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
      start_time: 2013-10-20T19:20:30+01:00
      end_time: 2013-10-20T19:20:30+01:00

"""

RETURN = """
audit_events:
    description:
        - List of AuditEvent resources
    returned: on success
    type: complex
    contains:
        tenant_id:
            description:
                - The OCID of the tenant.
            returned: on success
            type: string
            sample: ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        compartment_name:
            description:
                - The name of the compartment. This value is the friendly name associated with compartmentId.
                  This value can change, but the service logs the value that appeared at the time of the audit event.
            returned: on success
            type: string
            sample: compartment_name_example
        event_id:
            description:
                - The GUID of the event.
            returned: on success
            type: string
            sample: ocid1.event.oc1..xxxxxxEXAMPLExxxxxx
        event_name:
            description:
                - "The name of the event.
                  Example: `LaunchInstance`"
            returned: on success
            type: string
            sample: LaunchInstance
        event_source:
            description:
                - The source of the event.
            returned: on success
            type: string
            sample: event_source_example
        event_type:
            description:
                - The type of the event.
            returned: on success
            type: string
            sample: event_type_example
        event_time:
            description:
                - The time the event occurred, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        principal_id:
            description:
                - The OCID of the user whose action triggered the event.
            returned: on success
            type: string
            sample: ocid1.principal.oc1..xxxxxxEXAMPLExxxxxx
        credential_id:
            description:
                - The credential ID of the user. This value is extracted from the HTTP 'Authorization' request header. It consists of the tenantId, userId, and
                  user fingerprint, all delimited by a slash (/).
            returned: on success
            type: string
            sample: ocid1.credential.oc1..xxxxxxEXAMPLExxxxxx
        request_action:
            description:
                - The HTTP method of the request.
            returned: on success
            type: string
            sample: request_action_example
        request_id:
            description:
                - The opc-request-id of the request.
            returned: on success
            type: string
            sample: ocid1.request.oc1..xxxxxxEXAMPLExxxxxx
        request_agent:
            description:
                - The user agent of the client that made the request.
            returned: on success
            type: string
            sample: request_agent_example
        request_headers:
            description:
                - The HTTP header fields and values in the request.
            returned: on success
            type: dict
            sample: {}
        request_origin:
            description:
                - The IP address of the source of the request.
            returned: on success
            type: string
            sample: request_origin_example
        request_parameters:
            description:
                - The query parameter fields and values for the request.
            returned: on success
            type: dict
            sample: {}
        request_resource:
            description:
                - The resource targeted by the request.
            returned: on success
            type: string
            sample: request_resource_example
        response_headers:
            description:
                - The headers of the response.
            returned: on success
            type: dict
            sample: {}
        response_status:
            description:
                - The status code of the response.
            returned: on success
            type: string
            sample: response_status_example
        response_time:
            description:
                - The time of the response to the audited request, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        response_payload:
            description:
                - Metadata of interest from the response payload. For example, the OCID of a resource.
            returned: on success
            type: dict
            sample: {}
        user_name:
            description:
                - The name of the user or service. This value is the friendly name associated with principalId.
            returned: on success
            type: string
            sample: user_name_example
    sample: [{
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_name": "compartment_name_example",
        "event_id": "ocid1.event.oc1..xxxxxxEXAMPLExxxxxx",
        "event_name": "LaunchInstance",
        "event_source": "event_source_example",
        "event_type": "event_type_example",
        "event_time": "2013-10-20T19:20:30+01:00",
        "principal_id": "ocid1.principal.oc1..xxxxxxEXAMPLExxxxxx",
        "credential_id": "ocid1.credential.oc1..xxxxxxEXAMPLExxxxxx",
        "request_action": "request_action_example",
        "request_id": "ocid1.request.oc1..xxxxxxEXAMPLExxxxxx",
        "request_agent": "request_agent_example",
        "request_headers": {},
        "request_origin": "request_origin_example",
        "request_parameters": {},
        "request_resource": "request_resource_example",
        "response_headers": {},
        "response_status": "response_status_example",
        "response_time": "2013-10-20T19:20:30+01:00",
        "response_payload": {},
        "user_name": "user_name_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.audit import AuditClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AuditEventFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return ["compartment_id", "start_time", "end_time"]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_events,
            compartment_id=self.module.params.get("compartment_id"),
            start_time=self.module.params.get("start_time"),
            end_time=self.module.params.get("end_time"),
            **optional_kwargs
        )


AuditEventFactsHelperCustom = get_custom_class("AuditEventFactsHelperCustom")


class ResourceFactsHelper(AuditEventFactsHelperCustom, AuditEventFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            start_time=dict(type="str", required=True),
            end_time=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module, resource_type="audit_event", service_client_class=AuditClient
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(audit_events=result)


if __name__ == "__main__":
    main()
