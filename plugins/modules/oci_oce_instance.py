#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_oce_instance
short_description: Manage an OceInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OceInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new OceInstance.
    - "This resource has the following action operations in the M(oci_oce_instance_actions) module: change_compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    description:
        description:
            - OceInstance description
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - OceInstance Name
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    tenancy_id:
        description:
            - Tenancy Identifier
            - Required for create using I(state=present).
        type: str
    idcs_access_token:
        description:
            - Identity Cloud Service access token identifying a stripe and service administrator user
            - Required for create using I(state=present).
        type: str
    identity_stripe:
        description:
            - ""
        type: dict
        suboptions:
            service_name:
                description:
                    - "Name of the Identity Cloud Service instance in My Services to be used.
                      Example: `secondstripe`"
                type: str
                required: true
            tenancy:
                description:
                    - "Value of the Identity Cloud Service tenancy.
                      Example: `idcs-8416ebdd0d674f84803f4193cce026e9`"
                type: str
                required: true
    tenancy_name:
        description:
            - Tenancy Name
            - Required for create using I(state=present).
        type: str
    instance_usage_type:
        description:
            - Instance type based on its usage
            - This parameter is updatable.
        type: str
        choices:
            - "PRIMARY"
            - "NONPRIMARY"
    object_storage_namespace:
        description:
            - Object Storage Namespace of Tenancy
            - Required for create using I(state=present).
        type: str
    admin_email:
        description:
            - Admin Email for Notification
            - Required for create using I(state=present).
        type: str
    upgrade_schedule:
        description:
            - Upgrade schedule type representing service to be upgraded immediately whenever latest version is released
              or delay upgrade of the service to previous released version
        type: str
    waf_primary_domain:
        description:
            - Web Application Firewall(WAF) primary domain
            - This parameter is updatable.
        type: str
    instance_access_type:
        description:
            - Flag indicating whether the instance access is private or public
        type: str
        choices:
            - "PUBLIC"
            - "PRIVATE"
    instance_license_type:
        description:
            - Flag indicating whether the instance license is new cloud or bring your own license
            - This parameter is updatable.
        type: str
        choices:
            - "NEW"
            - "BYOL"
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    oce_instance_id:
        description:
            - unique OceInstance identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OceInstance.
            - Use I(state=present) to create or update an OceInstance.
            - Use I(state=absent) to delete an OceInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create oce_instance
  oci_oce_instance:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    idcs_access_token: idcs_access_token_example
    tenancy_name: tenancy_name_example
    object_storage_namespace: object_storage_namespace_example
    admin_email: admin_email_example

- name: Update oce_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_oce_instance:
    description: description_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    instance_usage_type: PRIMARY
    waf_primary_domain: waf_primary_domain_example
    instance_license_type: NEW
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update oce_instance
  oci_oce_instance:
    description: description_example
    instance_usage_type: PRIMARY
    oce_instance_id: "ocid1.oceinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete oce_instance
  oci_oce_instance:
    oce_instance_id: "ocid1.oceinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete oce_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_oce_instance:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

"""

RETURN = """
oce_instance:
    description:
        - Details of the OceInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        guid:
            description:
                - Unique GUID identifier that is immutable on creation
            returned: on success
            type: string
            sample: guid_example
        description:
            description:
                - OceInstance description, can be updated
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - OceInstance Name
            returned: on success
            type: string
            sample: name_example
        tenancy_id:
            description:
                - Tenancy Identifier
            returned: on success
            type: string
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        idcs_tenancy:
            description:
                - IDCS Tenancy Identifier
            returned: on success
            type: string
            sample: idcs_tenancy_example
        tenancy_name:
            description:
                - Tenancy Name
            returned: on success
            type: string
            sample: tenancy_name_example
        upgrade_schedule:
            description:
                - Upgrade schedule type representing service to be upgraded immediately whenever latest version is released
                  or delay upgrade of the service to previous released version
            returned: on success
            type: string
            sample: UPGRADE_IMMEDIATELY
        identity_stripe:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                service_name:
                    description:
                        - "Name of the Identity Cloud Service instance in My Services to be used.
                          Example: `secondstripe`"
                    returned: on success
                    type: string
                    sample: secondstripe
                tenancy:
                    description:
                        - "Value of the Identity Cloud Service tenancy.
                          Example: `idcs-8416ebdd0d674f84803f4193cce026e9`"
                    returned: on success
                    type: string
                    sample: idcs-8416ebdd0d674f84803f4193cce026e9
        instance_usage_type:
            description:
                - Instance type based on its usage
            returned: on success
            type: string
            sample: PRIMARY
        object_storage_namespace:
            description:
                - Object Storage Namespace of tenancy
            returned: on success
            type: string
            sample: object_storage_namespace_example
        admin_email:
            description:
                - Admin Email for Notification
            returned: on success
            type: string
            sample: admin_email_example
        waf_primary_domain:
            description:
                - Web Application Firewall(WAF) primary domain
            returned: on success
            type: string
            sample: waf_primary_domain_example
        instance_access_type:
            description:
                - Flag indicating whether the instance access is private or public
            returned: on success
            type: string
            sample: PUBLIC
        instance_license_type:
            description:
                - Flag indicating whether the instance license is new cloud or bring your own license
            returned: on success
            type: string
            sample: NEW
        time_created:
            description:
                - The time the the OceInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the OceInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the file system.
            returned: on success
            type: string
            sample: CREATING
        state_message:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: state_message_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
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
        service:
            description:
                - "SERVICE data.
                  Example: `{\\"service\\": {\\"IDCS\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "guid": "guid_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "idcs_tenancy": "idcs_tenancy_example",
        "tenancy_name": "tenancy_name_example",
        "upgrade_schedule": "UPGRADE_IMMEDIATELY",
        "identity_stripe": {
            "service_name": "secondstripe",
            "tenancy": "idcs-8416ebdd0d674f84803f4193cce026e9"
        },
        "instance_usage_type": "PRIMARY",
        "object_storage_namespace": "object_storage_namespace_example",
        "admin_email": "admin_email_example",
        "waf_primary_domain": "waf_primary_domain_example",
        "instance_access_type": "PUBLIC",
        "instance_license_type": "NEW",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "service": {}
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
    from oci.oce import OceInstanceClient
    from oci.oce.models import CreateOceInstanceDetails
    from oci.oce.models import UpdateOceInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OceInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "oce_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("oce_instance_id")

    def get_get_fn(self):
        return self.client.get_oce_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_oce_instance,
            oce_instance_id=self.module.params.get("oce_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_oce_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateOceInstanceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_oce_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_oce_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOceInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_oce_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oce_instance_id=self.module.params.get("oce_instance_id"),
                update_oce_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_oce_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oce_instance_id=self.module.params.get("oce_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OceInstanceHelperCustom = get_custom_class("OceInstanceHelperCustom")


class ResourceHelper(OceInstanceHelperCustom, OceInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            tenancy_id=dict(type="str"),
            idcs_access_token=dict(type="str"),
            identity_stripe=dict(
                type="dict",
                options=dict(
                    service_name=dict(type="str", required=True),
                    tenancy=dict(type="str", required=True),
                ),
            ),
            tenancy_name=dict(type="str"),
            instance_usage_type=dict(type="str", choices=["PRIMARY", "NONPRIMARY"]),
            object_storage_namespace=dict(type="str"),
            admin_email=dict(type="str"),
            upgrade_schedule=dict(type="str"),
            waf_primary_domain=dict(type="str"),
            instance_access_type=dict(type="str", choices=["PUBLIC", "PRIVATE"]),
            instance_license_type=dict(type="str", choices=["NEW", "BYOL"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            oce_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="oce_instance",
        service_client_class=OceInstanceClient,
        namespace="oce",
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
