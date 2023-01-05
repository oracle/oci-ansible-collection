#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_email_dkim
short_description: Manage a Dkim resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Dkim resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new DKIM for a email domain.
      This DKIM will sign all approved senders in the tenancy that are in this email domain.
      Best security practices indicate to periodically rotate the DKIM that is doing the signing.
      When a second DKIM is applied, all senders will seamlessly pick up the new key
      without interruption in signing.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - "The DKIM selector. This selector is required to be globally unique for this email domain.
              If you do not provide the selector, we will generate one for you.
              If you do provide the selector, we suggest adding a short region indicator
              to differentiate from your signing of emails in other regions you may be subscribed to.
              Selectors limited to ASCII characters may use alphanumeric, dash (\\"-\\"), and dot (\\".\\") characters.
              Non-ASCII selector names should adopt IDNA2008 normalization (RFC 5891-5892)."
            - Avoid entering confidential information.
            - "Example: `mydomain-phx-20210228`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    email_domain_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the EmailDomain for this DKIM.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - A string that describes the details about the DKIM. It does not have to be unique,
              and you can change it. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    dkim_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this DKIM.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Dkim.
            - Use I(state=present) to create or update a Dkim.
            - Use I(state=absent) to delete a Dkim.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create dkim
  oci_email_dkim:
    # required
    email_domain_id: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dkim
  oci_email_dkim:
    # required
    dkim_id: "ocid1.dkim.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dkim using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_email_dkim:
    # required
    name: name_example
    email_domain_id: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete dkim
  oci_email_dkim:
    # required
    dkim_id: "ocid1.dkim.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete dkim using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_email_dkim:
    # required
    name: name_example
    email_domain_id: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
dkim:
    description:
        - Details of the Dkim resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The DKIM selector.
                  If the same domain is managed in more than one region, each region must use different selectors.
            returned: on success
            type: str
            sample: name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DKIM.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        email_domain_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the email domain
                  that this DKIM belongs to.
            returned: on success
            type: str
            sample: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains this DKIM.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the DKIM.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource.
            returned: on success
            type: str
            sample: lifecycle_details_example
        description:
            description:
                - The description of the DKIM. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "The time the DKIM was created.
                  Times are expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format, \\"YYYY-MM-ddThh:mmZ\\"."
                - "Example: `2021-02-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time of the last change to the DKIM configuration, due to a state change or
                  an update operation.
                  Times are expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format, \\"YYYY-MM-ddThh:mmZ\\"."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        dns_subdomain_name:
            description:
                - The name of the DNS subdomain that must be provisioned to enable email recipients to verify DKIM signatures.
                  It is usually created with a CNAME record set to the cnameRecordValue
            returned: on success
            type: str
            sample: dns_subdomain_name_example
        cname_record_value:
            description:
                - The DNS CNAME record value to provision to the DKIM DNS subdomain, when using the CNAME method for DKIM setup (preferred).
            returned: on success
            type: str
            sample: cname_record_value_example
        txt_record_value:
            description:
                - The DNS TXT record value to provision to the DKIM DNS subdomain in place of using a CNAME record.
                  This is used in cases where a CNAME can not be used, such as when the cnameRecordValue would exceed the maximum length for a DNS entry.
                  This can also be used by customers who have an existing procedure to directly provision TXT records for DKIM.
                  Be aware that many DNS APIs will require you to break this string into segments of less than 255 characters.
            returned: on success
            type: str
            sample: txt_record_value_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "email_domain_id": "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "dns_subdomain_name": "dns_subdomain_name_example",
        "cname_record_value": "cname_record_value_example",
        "txt_record_value": "txt_record_value_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.email import EmailClient
    from oci.email.models import CreateDkimDetails
    from oci.email.models import UpdateDkimDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DkimHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DkimHelperGen, self).get_possible_entity_types() + [
            "emaildkim",
            "emaildkims",
            "emailemaildkim",
            "emailemaildkims",
            "emaildkimresource",
            "emaildkimsresource",
            "dkim",
            "dkims",
            "dkimresource",
            "dkimsresource",
            "email",
        ]

    def get_module_resource_id_param(self):
        return "dkim_id"

    def get_module_resource_id(self):
        return self.module.params.get("dkim_id")

    def get_get_fn(self):
        return self.client.get_dkim

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_dkim, dkim_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dkim, dkim_id=self.module.params.get("dkim_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "email_domain_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(self.client.list_dkims, **kwargs)

    def get_create_model_class(self):
        return CreateDkimDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dkim,
            call_fn_args=(),
            call_fn_kwargs=dict(create_dkim_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDkimDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dkim,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dkim_id=self.module.params.get("dkim_id"),
                update_dkim_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dkim,
            call_fn_args=(),
            call_fn_kwargs=dict(dkim_id=self.module.params.get("dkim_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DkimHelperCustom = get_custom_class("DkimHelperCustom")


class ResourceHelper(DkimHelperCustom, DkimHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            email_domain_id=dict(type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            dkim_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dkim",
        service_client_class=EmailClient,
        namespace="email",
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
