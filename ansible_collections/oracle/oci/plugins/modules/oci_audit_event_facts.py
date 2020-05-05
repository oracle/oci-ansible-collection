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
module: oci_audit_event_facts
short_description: Fetches details about one or multiple AuditEvent resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AuditEvent resources in Oracle Cloud Infrastructure
    - Returns all the audit events processed for the specified compartment within the specified
      time range.
version_added: "2.5"
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    start_time:
        description:
            - Returns events that were processed at or after this start date and time, expressed in
              L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
            - For example, a start value of `2017-01-15T11:30:00Z` will retrieve a list of all events processed
              since 30 minutes after the 11th hour of January 15, 2017, in Coordinated Universal Time (UTC).
              You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must
              be set to `0`.
        type: str
        required: true
    end_time:
        description:
            - Returns events that were processed before this end date and time, expressed in
              L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
            - For example, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-01-02T00:00:00Z`
              will retrieve a list of all events processed on January 1, 2017. Similarly, a start value of
              `2017-01-01T00:00:00Z` and an end value of `2017-02-01T00:00:00Z` will result in a list of all
              events processed between January 1, 2017 and January 31, 2017. You can specify a value with
              granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`.
        type: str
        required: true
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
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
        event_type:
            description:
                - The type of event that happened.
                - The service that produces the event can also add, remove, or change the meaning of a field.
                  A service implementing these type changes would publish a new version of an `eventType` and
                  revise the `eventTypeVersion` field.
                - "Example: `com.oraclecloud.ComputeApi.GetInstance`"
            returned: on success
            type: string
            sample: com.oraclecloud.ComputeApi.GetInstance
        cloud_events_version:
            description:
                - The version of the CloudEvents specification. The structure of the envelope follows the
                  L(CloudEvents,https://github.com/cloudevents/spec) industry standard format hosted by the
                  L(Cloud Native Computing Foundation ( CNCF),https://www.cncf.io/).
                - Audit uses version 0.1 specification of the CloudEvents event envelope.
                - "Example: `0.1`"
            returned: on success
            type: string
            sample: 0.1
        event_type_version:
            description:
                - The version of the event type. This version applies to the payload of the event, not the envelope.
                  Use `cloudEventsVersion` to determine the version of the envelope.
                - "Example: `2.0`"
            returned: on success
            type: string
            sample: 2.0
        source:
            description:
                - The source of the event.
                - "Example: `ComputeApi`"
            returned: on success
            type: string
            sample: ComputeApi
        event_id:
            description:
                - The GUID of the event.
            returned: on success
            type: string
            sample: ocid1.event.oc1..xxxxxxEXAMPLExxxxxx
        event_time:
            description:
                - The time the event occurred, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                - "Example: `2019-09-18T00:10:59.252Z`"
            returned: on success
            type: string
            sample: 2019-09-18T00:10:59.252Z
        content_type:
            description:
                - The content type of the data contained in `data`.
                - "Example: `application/json`"
            returned: on success
            type: string
            sample: application/json
        data:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                event_grouping_id:
                    description:
                        - This value links multiple audit events that are part of the same API operation. For example,
                          a long running API operations that emit an event at the start and the end of an operation
                          would use the same value in this field for both events.
                    returned: on success
                    type: string
                    sample: ocid1.eventgrouping.oc1..xxxxxxEXAMPLExxxxxx
                event_name:
                    description:
                        - Name of the API operation that generated this event.
                        - "Example: `GetInstance`"
                    returned: on success
                    type: string
                    sample: GetInstance
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment of the resource
                          emitting the event.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                compartment_name:
                    description:
                        - The name of the compartment. This value is the friendly name associated with compartmentId.
                          This value can change, but the service logs the value that appeared at the time of the audit
                          event.
                        - "Example: `CompartmentA`"
                    returned: on success
                    type: string
                    sample: CompartmentA
                resource_name:
                    description:
                        - The name of the resource emitting the event.
                    returned: on success
                    type: string
                    sample: resource_name_example
                resource_id:
                    description:
                        - An L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) or some other ID for the resource
                          emitting the event.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                availability_domain:
                    description:
                        - The availability domain where the resource resides.
                    returned: on success
                    type: string
                    sample: Uocm:PHX-AD-1
                freeform_tags:
                    description:
                        - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                          type, or namespace. Exists for cross-compatibility only. For more information,
                          see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more
                          information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
                identity:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        principal_name:
                            description:
                                - The name of the user or service. This value is the friendly name associated with `principalId`.
                                - "Example: `ExampleName`"
                            returned: on success
                            type: string
                            sample: ExampleName
                        principal_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the principal.
                            returned: on success
                            type: string
                            sample: ocid1.principal.oc1..xxxxxxEXAMPLExxxxxx
                        auth_type:
                            description:
                                - The type of authentication used.
                                - "Example: `natv`"
                            returned: on success
                            type: string
                            sample: natv
                        caller_name:
                            description:
                                - The name of the user or service. This value is the friendly name associated with `callerId`.
                            returned: on success
                            type: string
                            sample: caller_name_example
                        caller_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the caller. The caller that made a
                                  request on behalf of the prinicpal.
                            returned: on success
                            type: string
                            sample: ocid1.caller.oc1..xxxxxxEXAMPLExxxxxx
                        tenant_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the tenant.
                            returned: on success
                            type: string
                            sample: ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx
                        ip_address:
                            description:
                                - The IP address of the source of the request.
                                - "Example: `172.24.80.88`"
                            returned: on success
                            type: string
                            sample: 172.24.80.88
                        credentials:
                            description:
                                - The credential ID of the user. This value is extracted from the HTTP 'Authorization' request
                                  header. It consists of the tenantId, userId, and user fingerprint, all delimited by a slash (/).
                            returned: on success
                            type: string
                            sample: credentials_example
                        user_agent:
                            description:
                                - The user agent of the client that made the request.
                                - "Example: `Jersey/2.23 (HttpUrlConnection 1.8.0_212)`"
                            returned: on success
                            type: string
                            sample: Jersey/2.23 (HttpUrlConnection 1.8.0_212)
                        console_session_id:
                            description:
                                - This value identifies any Console session associated with this request.
                            returned: on success
                            type: string
                            sample: ocid1.consolesession.oc1..xxxxxxEXAMPLExxxxxx
                request:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The opc-request-id of the request.
                            returned: on success
                            type: string
                            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                        path:
                            description:
                                - The full path of the API request.
                                - "Example: `/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>`"
                            returned: on success
                            type: string
                            sample: /20160918/instances/ocid1.instance.oc1.phx.<unique_ID>
                        action:
                            description:
                                - The HTTP method of the request.
                                - "Example: `GET`"
                            returned: on success
                            type: string
                            sample: GET
                        parameters:
                            description:
                                - The parameters supplied by the caller during this operation.
                            returned: on success
                            type: dict
                            sample: {}
                        headers:
                            description:
                                - The HTTP header fields and values in the request.
                                - "Example:"
                                - |
                                  " -----
                                      {
                                        \\"opc-principal\\": [
                                          \\"{\\\\\\"tenantId\\\\\\":\\\\\\"ocid1.tenancy.oc1..<unique_ID>\\\\\\",\\\\\\"subjectId\\\\\\":\\\\\\"ocid1.user.oc1.
                                          .<unique_ID>\\\\\\",\\\\\\"claims\\\\\\":[{\\\\\\"key\\\\\\":\\\\\\"pstype\\\\\\",\\\\\\"value\\\\\\":\\\\\\"natv\\\\\
                                          \",\\\\\\"issuer\\\\\\":\\\\\\"authService.oracle.com\\\\\\"},{\\\\\\"key\\\\\\":\\\\\\"h_host\\\\\\",\\\\\\"value\\\\
                                          \\":\\\\\\"iaas.r2.oracleiaas.com\\\\\\",\\\\\\"issuer\\\\\\":\\\\\\"h\\\\\\"},{\\\\\\"key\\\\\\":\\\\\\"h_opc-
                                          request-id\\\\\\",\\\\\\"value\\\\\\":\\\\\\"<unique_ID>\\\\\\",\\\\\\"issuer\\\\\\":\\\\\\"h\\\\\\"},{\\\\\\"key\\\\\
                                          \":\\\\\\"ptype\\\\\\",\\\\\\"value\\\\\\":\\\\\\"user\\\\\\",\\\\\\"issuer\\\\\\":\\\\\\"authService.oracle.com\\\\\\
                                          "},{\\\\\\"key\\\\\\":\\\\\\"h_date\\\\\\",\\\\\\"value\\\\\\":\\\\\\"Wed, 18 Sep 2019 00:10:58 UTC\\\\\\",\\\\\\"issu
                                          er\\\\\\":\\\\\\"h\\\\\\"},{\\\\\\"key\\\\\\":\\\\\\"h_accept\\\\\\",\\\\\\"value\\\\\\":\\\\\\"application/json\\\\\\
                                          ",\\\\\\"issuer\\\\\\":\\\\\\"h\\\\\\"},{\\\\\\"key\\\\\\":\\\\\\"authorization\\\\\\",\\\\\\"value\\\\\\":\\\\\\"Sign
                                          ature headers=\\\\\\\\\\\\\\"date (request-target) host accept opc-request-id\\\\\\\\\\\\\\",keyId=\\\\\\\\\\\\\\"ocid
                                          1.tenancy.oc1..<unique_ID>/ocid1.user.oc1..<unique_ID>/8c:b4:5f:18:e7:ec:db:08:b8:fa:d2:2a:7d:11:76:ac\\\\\\\\\\\\\\",
                                          algorithm=\\\\\\\\\\\\\\"rsa-pss-sha256\\\\\\\\\\\\\\",signature=\\\\\\\\\\\\\\"<unique_ID>\\\\\\\\\\\\\\",version=\\\
                                          \\\\\\\\\\\"1\\\\\\\\\\\\\\"\\\\\\",\\\\\\"issuer\\\\\\":\\\\\\"h\\\\\\"},{\\\\\\"key\\\\\\":\\\\\\"h_(request-
                                          target)\\\\\\",\\\\\\"value\\\\\\":\\\\\\"get
                                          /20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\\\\\\",\\\\\\"issuer\\\\\\":\\\\\\"h\\\\\\"}]}\\"
                                        ],
                                        \\"Accept\\": [
                                          \\"application/json\\"
                                        ],
                                        \\"X-Oracle-Auth-Client-CN\\": [
                                          \\"splat-proxy-se-02302.node.ad2.r2\\"
                                        ],
                                        \\"X-Forwarded-Host\\": [
                                          \\"compute-api.svc.ad1.r2\\"
                                        ],
                                        \\"Connection\\": [
                                          \\"close\\"
                                        ],
                                        \\"User-Agent\\": [
                                          \\"Jersey/2.23 (HttpUrlConnection 1.8.0_212)\\"
                                        ],
                                        \\"X-Forwarded-For\\": [
                                          \\"172.24.80.88\\"
                                        ],
                                        \\"X-Real-IP\\": [
                                          \\"172.24.80.88\\"
                                        ],
                                        \\"oci-original-url\\": [
                                          \\"https://iaas.r2.oracleiaas.com/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>\\"
                                        ],
                                        \\"opc-request-id\\": [
                                          \\"<unique_ID>\\"
                                        ],
                                        \\"Date\\": [
                                          \\"Wed, 18 Sep 2019 00:10:58 UTC\\"
                                        ]
                                      }
                                    -----"
                            returned: on success
                            type: dict
                            sample: {}
                response:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        status:
                            description:
                                - The status code of the response.
                                - "Example: `200`"
                            returned: on success
                            type: string
                            sample: 200
                        response_time:
                            description:
                                - The time of the response to the audited request, expressed in
                                  L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                                - "Example: `2019-09-18T00:10:59.278Z`"
                            returned: on success
                            type: string
                            sample: 2019-09-18T00:10:59.278Z
                        headers:
                            description:
                                - The headers of the response.
                                - "Example:"
                                - |
                                  " -----
                                      {
                                        \\"ETag\\": [
                                          \\"<unique_ID>\\"
                                        ],
                                        \\"Connection\\": [
                                          \\"close\\"
                                        ],
                                        \\"Content-Length\\": [
                                          \\"1828\\"
                                        ],
                                        \\"opc-request-id\\": [
                                          \\"<unique_ID>\\"
                                        ],
                                        \\"Date\\": [
                                          \\"Wed, 18 Sep 2019 00:10:59 GMT\\"
                                        ],
                                        \\"Content-Type\\": [
                                          \\"application/json\\"
                                        ]
                                      }
                                    -----"
                            returned: on success
                            type: dict
                            sample: {}
                        payload:
                            description:
                                - This value is included for backward compatibility with the Audit version 1 schema, where
                                  it contained metadata of interest from the response payload.
                                - "Example:"
                                - |
                                  " -----
                                      {
                                        \\"resourceName\\": \\"my_instance\\",
                                        \\"id\\": \\"ocid1.instance.oc1.phx.<unique_ID>\\"
                                      }
                                    -----"
                            returned: on success
                            type: dict
                            sample: {}
                        message:
                            description:
                                - A friendly description of what happened during the operation. Use this for troubleshooting.
                            returned: on success
                            type: string
                            sample: message_example
                state_change:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        previous:
                            description:
                                - Provides the previous state of fields that may have changed during an operation. To determine
                                  how the current operation changed a resource, compare the information in this attribute to
                                  `current`.
                            returned: on success
                            type: dict
                            sample: {}
                        current:
                            description:
                                - Provides the current state of fields that may have changed during an operation. To determine
                                  how the current operation changed a resource, compare the information in this attribute to
                                  `previous`.
                            returned: on success
                            type: dict
                            sample: {}
                additional_details:
                    description:
                        - A container object for attribues unique to the resource emitting the event.
                        - "Example:"
                        - |
                          " -----
                              {
                                \\"imageId\\": \\"ocid1.image.oc1.phx.<unique_ID>\\",
                                \\"shape\\": \\"VM.Standard1.1\\",
                                \\"type\\": \\"CustomerVmi\\"
                              }
                            -----"
                    returned: on success
                    type: dict
                    sample: {}
    sample: [{
        "event_type": "com.oraclecloud.ComputeApi.GetInstance",
        "cloud_events_version": "0.1",
        "event_type_version": "2.0",
        "source": "ComputeApi",
        "event_id": "ocid1.event.oc1..xxxxxxEXAMPLExxxxxx",
        "event_time": "2019-09-18T00:10:59.252Z",
        "content_type": "application/json",
        "data": {
            "event_grouping_id": "ocid1.eventgrouping.oc1..xxxxxxEXAMPLExxxxxx",
            "event_name": "GetInstance",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_name": "CompartmentA",
            "resource_name": "resource_name_example",
            "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "availability_domain": "Uocm:PHX-AD-1",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "identity": {
                "principal_name": "ExampleName",
                "principal_id": "ocid1.principal.oc1..xxxxxxEXAMPLExxxxxx",
                "auth_type": "natv",
                "caller_name": "caller_name_example",
                "caller_id": "ocid1.caller.oc1..xxxxxxEXAMPLExxxxxx",
                "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
                "ip_address": "172.24.80.88",
                "credentials": "credentials_example",
                "user_agent": "Jersey/2.23 (HttpUrlConnection 1.8.0_212)",
                "console_session_id": "ocid1.consolesession.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "request": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "path": "/20160918/instances/ocid1.instance.oc1.phx.<unique_ID>",
                "action": "GET",
                "parameters": {},
                "headers": {}
            },
            "response": {
                "status": "200",
                "response_time": "2019-09-18T00:10:59.278Z",
                "headers": {},
                "payload": {},
                "message": "message_example"
            },
            "state_change": {
                "previous": {},
                "current": {}
            },
            "additional_details": {}
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
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
        return [
            "compartment_id",
            "start_time",
            "end_time",
        ]

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
        module=module,
        resource_type="audit_event",
        service_client_class=AuditClient,
        namespace="audit",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(audit_events=result)


if __name__ == "__main__":
    main()
