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
module: oci_dns_steering_policy_attachment_facts
short_description: Fetches details about one or multiple SteeringPolicyAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SteeringPolicyAttachment resources in Oracle Cloud Infrastructure
    - Lists the steering policy attachments in the specified compartment.
    - If I(steering_policy_attachment_id) is specified, the details of a single SteeringPolicyAttachment will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    steering_policy_attachment_id:
        description:
            - The OCID of the target steering policy attachment.
            - Required to get a specific steering_policy_attachment.
        type: str
        aliases: ["id"]
    if_modified_since:
        description:
            - The `If-Modified-Since` header field makes a GET or HEAD request method
              conditional on the selected representation's modification date being more
              recent than the date provided in the field-value.  Transfer of the
              selected representation's data is avoided if that data has not changed.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
            - Required to list multiple steering_policy_attachments.
        type: str
    id:
        description:
            - The OCID of a resource.
        type: str
    display_name:
        description:
            - The displayName of a resource.
        type: str
        aliases: ["name"]
    steering_policy_id:
        description:
            - Search by steering policy OCID.
              Will match any resource whose steering policy ID matches the provided value.
        type: str
    zone_id:
        description:
            - Search by zone OCID.
              Will match any resource whose zone ID matches the provided value.
        type: str
    domain:
        description:
            - Search by domain.
              Will match any record whose domain (case-insensitive) equals the provided value.
        type: str
    domain_contains:
        description:
            - Search by domain.
              Will match any record whose domain (case-insensitive) contains the provided value.
        type: str
    time_created_greater_than_or_equal_to:
        description:
            - An L(RFC 3339,https://www.ietf.org/rfc/rfc3339.txt) timestamp that states
              all returned resources were created on or after the indicated time.
        type: str
    time_created_less_than:
        description:
            - An L(RFC 3339,https://www.ietf.org/rfc/rfc3339.txt) timestamp that states
              all returned resources were created before the indicated time.
        type: str
    lifecycle_state:
        description:
            - The state of a resource.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
    sort_by:
        description:
            - The field by which to sort steering policy attachments. If unspecified, defaults to `timeCreated`.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
            - "domainName"
    sort_order:
        description:
            - The order to sort the resources.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List steering_policy_attachments
  oci_dns_steering_policy_attachment_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific steering_policy_attachment
  oci_dns_steering_policy_attachment_facts:
    steering_policy_attachment_id: ocid1.steeringpolicyattachment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
steering_policy_attachments:
    description:
        - List of SteeringPolicyAttachment resources
    returned: on success
    type: complex
    contains:
        steering_policy_id:
            description:
                - The OCID of the attached steering policy.
            returned: on success
            type: string
            sample: ocid1.steeringpolicy.oc1..xxxxxxEXAMPLExxxxxx
        zone_id:
            description:
                - The OCID of the attached zone.
            returned: on success
            type: string
            sample: ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx
        domain_name:
            description:
                - The attached domain within the attached zone.
            returned: on success
            type: string
            sample: domain_name_example
        display_name:
            description:
                - A user-friendly name for the steering policy attachment.
                  Does not have to be unique and can be changed.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        rtypes:
            description:
                - The record types covered by the attachment at the domain. The set of record types is
                  determined by aggregating the record types from the answers defined in the steering
                  policy.
            returned: on success
            type: list
            sample: []
        compartment_id:
            description:
                - The OCID of the compartment containing the steering policy attachment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        _self:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: string
            sample: _self_example
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the resource was created, expressed in RFC 3339 timestamp format.
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: string
            sample: CREATING
    sample: [{
        "steering_policy_id": "ocid1.steeringpolicy.oc1..xxxxxxEXAMPLExxxxxx",
        "zone_id": "ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx",
        "domain_name": "domain_name_example",
        "display_name": "display_name_example",
        "rtypes": [],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "_self": "_self_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SteeringPolicyAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "steering_policy_attachment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "if_modified_since",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_steering_policy_attachment,
            steering_policy_attachment_id=self.module.params.get(
                "steering_policy_attachment_id"
            ),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "id",
            "display_name",
            "steering_policy_id",
            "zone_id",
            "domain",
            "domain_contains",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_steering_policy_attachments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SteeringPolicyAttachmentFactsHelperCustom = get_custom_class(
    "SteeringPolicyAttachmentFactsHelperCustom"
)


class ResourceFactsHelper(
    SteeringPolicyAttachmentFactsHelperCustom, SteeringPolicyAttachmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            steering_policy_attachment_id=dict(aliases=["id"], type="str"),
            if_modified_since=dict(type="str"),
            compartment_id=dict(type="str"),
            id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            steering_policy_id=dict(type="str"),
            zone_id=dict(type="str"),
            domain=dict(type="str"),
            domain_contains=dict(type="str"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            lifecycle_state=dict(
                type="str", choices=["CREATING", "ACTIVE", "DELETING"]
            ),
            sort_by=dict(
                type="str", choices=["displayName", "timeCreated", "domainName"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="steering_policy_attachment",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(steering_policy_attachments=result)


if __name__ == "__main__":
    main()
