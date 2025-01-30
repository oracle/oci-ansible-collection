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
module: oci_oda_instance
short_description: Manage an OdaInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OdaInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), starts an asynchronous job to create a Digital Assistant instance.
    - To monitor the status of the job, take the `opc-work-request-id` response
      header value and use it to call `GET /workRequests/{workRequestId}`.
    - "This resource has the following action operations in the M(oracle.oci.oci_oda_instance_actions) module: change_compartment, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Identifier of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    shape_name:
        description:
            - Shape or size of the instance.
            - Required for create using I(state=present).
        type: str
        choices:
            - "DEVELOPMENT"
            - "PRODUCTION"
    is_role_based_access:
        description:
            - Should this Digital Assistant instance use role-based authorization via an identity domain (true) or use the default policy-based authorization
              via IAM policies (false)
        type: bool
    identity_domain:
        description:
            - If isRoleBasedAccess is set to true, this property specifies the identity domain that is to be used to implement this type of authorzation.
              Digital Assistant will create an Identity Application instance and Application Roles within this identity domain. The caller may then perform and
              user roll mappings they like to grant access to users within the identity domain.
        type: str
    display_name:
        description:
            - User-friendly name for the instance. Avoid entering confidential information. You can change this value anytime.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the Digital Assistant instance.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OdaInstance.
            - Use I(state=present) to create or update an OdaInstance.
            - Use I(state=absent) to delete an OdaInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create oda_instance
  oci_oda_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    shape_name: DEVELOPMENT

    # optional
    is_role_based_access: true
    identity_domain: identity_domain_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update oda_instance
  oci_oda_instance:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update oda_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_oda_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete oda_instance
  oci_oda_instance:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete oda_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_oda_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
oda_instance:
    description:
        - Details of the OdaInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique immutable identifier that was assigned when the instance was created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-defined name for the Digital Assistant instance. Avoid entering confidential information.
                  You can change this value.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the Digital Assistant instance.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Identifier of the compartment that the instance belongs to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        shape_name:
            description:
                - Shape or size of the instance.
            returned: on success
            type: str
            sample: DEVELOPMENT
        web_app_url:
            description:
                - URL for the Digital Assistant web application that's associated with the instance.
            returned: on success
            type: str
            sample: web_app_url_example
        connector_url:
            description:
                - URL for the connector's endpoint.
            returned: on success
            type: str
            sample: connector_url_example
        time_created:
            description:
                - When the Digital Assistant instance was created. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section
                  14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the Digital Assistance instance was last updated. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339),
                  section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Digital Assistant instance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_sub_state:
            description:
                - The current sub-state of the Digital Assistant instance.
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - A message that describes the current state in more detail.
                  For example, actionable information about an instance that's in the `FAILED` state.
            returned: on success
            type: str
            sample: state_message_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_role_based_access:
            description:
                - Should this Digital Assistant instance use role-based authorization via an identity domain (true) or use the default policy-based
                  authorization via IAM policies (false)
            returned: on success
            type: bool
            sample: true
        identity_domain:
            description:
                - If isRoleBasedAccess is set to true, this property specifies the identity domain that is to be used to implement this type of authorzation.
                  Digital Assistant will create an Identity Application instance and Application Roles within this identity domain. The caller may then perform
                  and user roll mappings they like to grant access to users within the identity domain.
            returned: on success
            type: str
            sample: identity_domain_example
        identity_app_guid:
            description:
                - If isRoleBasedAccess is set to true, this property specifies the GUID of the Identity Application instance Digital Assistant has created
                  inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this
                  Digital Assistant instance for users within the identity domain.
            returned: on success
            type: str
            sample: identity_app_guid_example
        identity_app_console_url:
            description:
                - If isRoleBasedAccess is set to true, this property specifies the URL for the administration console used to manage the Identity Application
                  instance Digital Assistant has created inside the user-specified identity domain.
            returned: on success
            type: str
            sample: identity_app_console_url_example
        imported_package_names:
            description:
                - A list of package names imported into this instance (if any). Use importedPackageIds field to get the details of the imported packages.
            returned: on success
            type: list
            sample: []
        imported_package_ids:
            description:
                - A list of package ids imported into this instance (if any). Use GetImportedPackage to get the details of the imported packages.
            returned: on success
            type: list
            sample: []
        attachment_types:
            description:
                - A list of attachment types for this instance (if any). Use attachmentIds to get the details of the attachments.
            returned: on success
            type: list
            sample: []
        attachment_ids:
            description:
                - A list of attachment identifiers for this instance (if any). Use GetOdaInstanceAttachment to get the details of the attachments.
            returned: on success
            type: list
            sample: []
        restricted_operations:
            description:
                - A list of restricted operations (across all attachments) for this instance (if any). Use GetOdaInstanceAttachment to get the details of the
                  attachments.
            returned: on success
            type: complex
            contains:
                operation_name:
                    description:
                        - Name of the restricted operation.
                    returned: on success
                    type: str
                    sample: operation_name_example
                restricting_service:
                    description:
                        - Name of the service restricting the operation.
                    returned: on success
                    type: str
                    sample: restricting_service_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "shape_name": "DEVELOPMENT",
        "web_app_url": "web_app_url_example",
        "connector_url": "connector_url_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_sub_state": "CREATING",
        "state_message": "state_message_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_role_based_access": true,
        "identity_domain": "identity_domain_example",
        "identity_app_guid": "identity_app_guid_example",
        "identity_app_console_url": "identity_app_console_url_example",
        "imported_package_names": [],
        "imported_package_ids": [],
        "attachment_types": [],
        "attachment_ids": [],
        "restricted_operations": [{
            "operation_name": "operation_name_example",
            "restricting_service": "restricting_service_example"
        }]
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
    from oci.oda import OdaClient
    from oci.oda.models import CreateOdaInstanceDetails
    from oci.oda.models import UpdateOdaInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OdaInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(OdaInstanceHelperGen, self).get_possible_entity_types() + [
            "odainstance",
            "odainstances",
            "odaodainstance",
            "odaodainstances",
            "odainstanceresource",
            "odainstancesresource",
            "oda",
        ]

    def get_module_resource_id_param(self):
        return "oda_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("oda_instance_id")

    def get_get_fn(self):
        return self.client.get_oda_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_oda_instance, oda_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_oda_instance,
            oda_instance_id=self.module.params.get("oda_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_oda_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateOdaInstanceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_oda_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_oda_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOdaInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_oda_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                update_oda_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_oda_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OdaInstanceHelperCustom = get_custom_class("OdaInstanceHelperCustom")


class ResourceHelper(OdaInstanceHelperCustom, OdaInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            shape_name=dict(type="str", choices=["DEVELOPMENT", "PRODUCTION"]),
            is_role_based_access=dict(type="bool"),
            identity_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            oda_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="oda_instance",
        service_client_class=OdaClient,
        namespace="oda",
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
