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
module: oci_dns_steering_policy_attachment
short_description: Manage a SteeringPolicyAttachment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a SteeringPolicyAttachment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new attachment between a steering policy and a domain, giving the
      policy permission to answer queries for the specified domain. A steering policy must
      be attached to a domain for the policy to answer DNS queries for that domain.
    - For the purposes of access control, the attachment is automatically placed
      into the same compartment as the domain's zone.
version_added: "2.9"
author: Oracle (@oracle)
options:
    steering_policy_id:
        description:
            - The OCID of the attached steering policy.
            - Required for create using I(state=present).
        type: str
    zone_id:
        description:
            - The OCID of the attached zone.
            - Required for create using I(state=present).
        type: str
    domain_name:
        description:
            - The attached domain within the attached zone.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name for the steering policy attachment.
              Does not have to be unique and can be changed.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    steering_policy_attachment_id:
        description:
            - The OCID of the target steering policy attachment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    if_unmodified_since:
        description:
            - The `If-Unmodified-Since` header field makes the request method
              conditional on the selected representation's last modification date being
              earlier than or equal to the date provided in the field-value.  This
              field accomplishes the same purpose as If-Match for cases where the user
              agent does not have an entity-tag for the representation.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the SteeringPolicyAttachment.
            - Use I(state=present) to create or update a SteeringPolicyAttachment.
            - Use I(state=absent) to delete a SteeringPolicyAttachment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create steering_policy_attachment
  oci_dns_steering_policy_attachment:
    steering_policy_id: ocid1.dnspolicy.oc1..
    zone_id: ocid1.dns-zone.oc1..
    domain_name: example.com
    display_name: attached to example

- name: Update steering_policy_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dns_steering_policy_attachment:
    display_name: IP prefix steering

- name: Update steering_policy_attachment
  oci_dns_steering_policy_attachment:
    steering_policy_attachment_id: ocid1.steeringpolicyattachment.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete steering_policy_attachment
  oci_dns_steering_policy_attachment:
    steering_policy_attachment_id: ocid1.steeringpolicyattachment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete steering_policy_attachment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dns_steering_policy_attachment:
    display_name: attached to example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
steering_policy_attachment:
    description:
        - Details of the SteeringPolicyAttachment resource acted upon by the current operation
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
    sample: {
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
    from oci.dns import DnsClient
    from oci.dns.models import CreateSteeringPolicyAttachmentDetails
    from oci.dns.models import UpdateSteeringPolicyAttachmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SteeringPolicyAttachmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "steering_policy_attachment_id"

    def get_module_resource_id(self):
        return self.module.params.get("steering_policy_attachment_id")

    def get_get_fn(self):
        return self.client.get_steering_policy_attachment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_steering_policy_attachment,
            steering_policy_attachment_id=self.module.params.get(
                "steering_policy_attachment_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "steering_policy_id", "zone_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_steering_policy_attachments, **kwargs
        )

    def get_create_model_class(self):
        return CreateSteeringPolicyAttachmentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_steering_policy_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_steering_policy_attachment_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateSteeringPolicyAttachmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_steering_policy_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                steering_policy_attachment_id=self.module.params.get(
                    "steering_policy_attachment_id"
                ),
                update_steering_policy_attachment_details=update_details,
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_steering_policy_attachment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                steering_policy_attachment_id=self.module.params.get(
                    "steering_policy_attachment_id"
                ),
                if_unmodified_since=self.module.params.get("if_unmodified_since"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


SteeringPolicyAttachmentHelperCustom = get_custom_class(
    "SteeringPolicyAttachmentHelperCustom"
)


class ResourceHelper(
    SteeringPolicyAttachmentHelperCustom, SteeringPolicyAttachmentHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            steering_policy_id=dict(type="str"),
            zone_id=dict(type="str"),
            domain_name=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            steering_policy_attachment_id=dict(aliases=["id"], type="str"),
            if_unmodified_since=dict(type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="steering_policy_attachment",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
