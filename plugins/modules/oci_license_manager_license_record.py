#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_license_manager_license_record
short_description: Manage a LicenseRecord resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a LicenseRecord resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new license record for the given product license ID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    product_license_id:
        description:
            - Unique product license identifier.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - License record name.
            - Required for create using I(state=present), update using I(state=present) with license_record_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    is_perpetual:
        description:
            - Specifies if the license record term is perpertual.
            - Required for create using I(state=present), update using I(state=present) with license_record_id present.
        type: bool
    expiration_date:
        description:
            - "The license record end date in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
              date format.
              Example: `2018-09-12`"
            - This parameter is updatable.
        type: str
    support_end_date:
        description:
            - "The license record support end date in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
              date format.
              Example: `2018-09-12`"
            - This parameter is updatable.
        type: str
    is_unlimited:
        description:
            - Specifies if the license count is unlimited.
            - Required for create using I(state=present), update using I(state=present) with license_record_id present.
        type: bool
    license_count:
        description:
            - The number of license units added by a user in a license record.
              Default 1
            - This parameter is updatable.
        type: int
    product_id:
        description:
            - The license record product ID.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    license_record_id:
        description:
            - Unique license record identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the LicenseRecord.
            - Use I(state=present) to create or update a LicenseRecord.
            - Use I(state=absent) to delete a LicenseRecord.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create license_record
  oci_license_manager_license_record:
    # required
    product_license_id: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    is_perpetual: true
    is_unlimited: true

    # optional
    expiration_date: expiration_date_example
    support_end_date: support_end_date_example
    license_count: 56
    product_id: "ocid1.product.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update license_record
  oci_license_manager_license_record:
    # required
    display_name: display_name_example
    is_perpetual: true
    is_unlimited: true
    license_record_id: "ocid1.licenserecord.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    expiration_date: expiration_date_example
    support_end_date: support_end_date_example
    license_count: 56
    product_id: "ocid1.product.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update license_record using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_license_manager_license_record:
    # required
    product_license_id: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    is_perpetual: true
    expiration_date: expiration_date_example
    support_end_date: support_end_date_example
    is_unlimited: true
    license_count: 56
    product_id: "ocid1.product.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete license_record
  oci_license_manager_license_record:
    # required
    license_record_id: "ocid1.licenserecord.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete license_record using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_license_manager_license_record:
    # required
    product_license_id: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
license_record:
    description:
        - Details of the LicenseRecord resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The license record L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        product_license_id:
            description:
                - The product license L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) with which the license record is
                  associated.
            returned: on success
            type: str
            sample: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) where the license record is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The license record display name. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        product_id:
            description:
                - The license record product ID.
            returned: on success
            type: str
            sample: "ocid1.product.oc1..xxxxxxEXAMPLExxxxxx"
        license_count:
            description:
                - The number of license units added by the user for the given license record.
                  Default 1
            returned: on success
            type: int
            sample: 56
        expiration_date:
            description:
                - "The license record end date in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  date format.
                  Example: `2018-09-12`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        support_end_date:
            description:
                - "The license record support end date in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  date format.
                  Example: `2018-09-12`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_unlimited:
            description:
                - Specifies if the license count is unlimited.
            returned: on success
            type: bool
            sample: true
        is_perpetual:
            description:
                - Specifies if the license record term is perpertual.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the license record was created. An L(RFC 3339,https://tools.ietf.org/html/rfc3339)-formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the license record was updated. An L(RFC 3339,https://tools.ietf.org/html/rfc3339)-formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current license record state.
            returned: on success
            type: str
            sample: ACTIVE
        license_unit:
            description:
                - The product license unit.
            returned: on success
            type: str
            sample: OCPU
        product_license:
            description:
                - The product license name with which the license record is associated.
            returned: on success
            type: str
            sample: product_license_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "product_license_id": "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "product_id": "ocid1.product.oc1..xxxxxxEXAMPLExxxxxx",
        "license_count": 56,
        "expiration_date": "2013-10-20T19:20:30+01:00",
        "support_end_date": "2013-10-20T19:20:30+01:00",
        "is_unlimited": true,
        "is_perpetual": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "license_unit": "OCPU",
        "product_license": "product_license_example",
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
    from oci.license_manager import LicenseManagerClient
    from oci.license_manager.models import CreateLicenseRecordDetails
    from oci.license_manager.models import UpdateLicenseRecordDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LicenseRecordHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(LicenseRecordHelperGen, self).get_possible_entity_types() + [
            "licensemanagerlicenserecord",
            "licensemanagerlicenserecords",
            "licenseManagerlicensemanagerlicenserecord",
            "licenseManagerlicensemanagerlicenserecords",
            "licensemanagerlicenserecordresource",
            "licensemanagerlicenserecordsresource",
            "licenserecord",
            "licenserecords",
            "licenseManagerlicenserecord",
            "licenseManagerlicenserecords",
            "licenserecordresource",
            "licenserecordsresource",
            "licensemanager",
        ]

    def get_module_resource_id_param(self):
        return "license_record_id"

    def get_module_resource_id(self):
        return self.module.params.get("license_record_id")

    def get_get_fn(self):
        return self.client.get_license_record

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_license_record, license_record_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_license_record,
            license_record_id=self.module.params.get("license_record_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "product_license_id",
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
            self.client.list_license_records, **kwargs
        )

    def get_create_model_class(self):
        return CreateLicenseRecordDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_license_record,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_license_record_details=create_details,
                product_license_id=self.module.params.get("product_license_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateLicenseRecordDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_license_record,
            call_fn_args=(),
            call_fn_kwargs=dict(
                license_record_id=self.module.params.get("license_record_id"),
                update_license_record_details=update_details,
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
            call_fn=self.client.delete_license_record,
            call_fn_args=(),
            call_fn_kwargs=dict(
                license_record_id=self.module.params.get("license_record_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


LicenseRecordHelperCustom = get_custom_class("LicenseRecordHelperCustom")


class ResourceHelper(LicenseRecordHelperCustom, LicenseRecordHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            product_license_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_perpetual=dict(type="bool"),
            expiration_date=dict(type="str"),
            support_end_date=dict(type="str"),
            is_unlimited=dict(type="bool"),
            license_count=dict(type="int"),
            product_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            license_record_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="license_record",
        service_client_class=LicenseManagerClient,
        namespace="license_manager",
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
