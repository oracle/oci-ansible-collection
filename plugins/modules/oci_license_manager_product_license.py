#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_license_manager_product_license
short_description: Manage a ProductLicense resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ProductLicense resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new product license.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) where product licenses are created.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    is_vendor_oracle:
        description:
            - Specifies if the product license vendor is Oracle or a third party.
            - Required for create using I(state=present).
        type: bool
    display_name:
        description:
            - Name of the product license.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    license_unit:
        description:
            - The product license unit.
            - Required for create using I(state=present).
        type: str
        choices:
            - "OCPU"
            - "NAMED_USER_PLUS"
            - "PROCESSORS"
    vendor_name:
        description:
            - "The product license vendor name, for example: Microsoft, RHEL, and so on."
        type: str
    images:
        description:
            - The image details associated with the product license.
            - Required for update using I(state=present) with product_license_id present.
        type: list
        elements: dict
        suboptions:
            listing_id:
                description:
                    - Marketplace image listing ID.
                type: str
                required: true
            package_version:
                description:
                    - Image package version.
                type: str
                required: true
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
    product_license_id:
        description:
            - Unique product license identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ProductLicense.
            - Use I(state=present) to create or update a ProductLicense.
            - Use I(state=absent) to delete a ProductLicense.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create product_license
  oci_license_manager_product_license:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_vendor_oracle: true
    display_name: display_name_example
    license_unit: OCPU

    # optional
    vendor_name: vendor_name_example
    images:
    - # required
      listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
      package_version: package_version_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update product_license
  oci_license_manager_product_license:
    # required
    images:
    - # required
      listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
      package_version: package_version_example
    product_license_id: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update product_license using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_license_manager_product_license:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    images:
    - # required
      listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
      package_version: package_version_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete product_license
  oci_license_manager_product_license:
    # required
    product_license_id: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete product_license using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_license_manager_product_license:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
product_license:
    description:
        - Details of the ProductLicense resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The product license L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) where the product license is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The current product license status.
            returned: on success
            type: str
            sample: INCOMPLETE
        status_description:
            description:
                - Status description for the current product license status.
            returned: on success
            type: str
            sample: status_description_example
        total_active_license_unit_count:
            description:
                - The total number of licenses available for the product license, calculated by adding up all the license counts for active license records
                  associated with the product license.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current product license state.
            returned: on success
            type: str
            sample: ACTIVE
        total_license_units_consumed:
            description:
                - The number of license units consumed. Updated after each allocation run.
            returned: on success
            type: float
            sample: 1.2
        total_license_record_count:
            description:
                - The number of license records associated with the product license.
            returned: on success
            type: int
            sample: 56
        active_license_record_count:
            description:
                - The number of active license records associated with the product license.
            returned: on success
            type: int
            sample: 56
        license_unit:
            description:
                - The product license unit.
            returned: on success
            type: str
            sample: OCPU
        is_vendor_oracle:
            description:
                - Specifies whether the vendor is Oracle or a third party.
            returned: on success
            type: bool
            sample: true
        is_over_subscribed:
            description:
                - Specifies whether or not the product license is oversubscribed.
            returned: on success
            type: bool
            sample: true
        is_unlimited:
            description:
                - Specifies if the license unit count is unlimited.
            returned: on success
            type: bool
            sample: true
        display_name:
            description:
                - License record name
            returned: on success
            type: str
            sample: display_name_example
        vendor_name:
            description:
                - The vendor of the ProductLicense
            returned: on success
            type: str
            sample: vendor_name_example
        time_created:
            description:
                - The time the product license was created. An L(RFC 3339,https://tools.ietf.org/html/rfc3339)-formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the product license was updated. An L(RFC 3339,https://tools.ietf.org/html/rfc3339)-formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        images:
            description:
                - The images associated with the product license.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The image ID associated with the product license.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                listing_name:
                    description:
                        - The listing name associated with the product license.
                    returned: on success
                    type: str
                    sample: listing_name_example
                publisher:
                    description:
                        - The image publisher.
                    returned: on success
                    type: str
                    sample: publisher_example
                listing_id:
                    description:
                        - The image listing ID.
                    returned: on success
                    type: str
                    sample: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
                package_version:
                    description:
                        - The image package version.
                    returned: on success
                    type: str
                    sample: package_version_example
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "INCOMPLETE",
        "status_description": "status_description_example",
        "total_active_license_unit_count": 56,
        "lifecycle_state": "ACTIVE",
        "total_license_units_consumed": 1.2,
        "total_license_record_count": 56,
        "active_license_record_count": 56,
        "license_unit": "OCPU",
        "is_vendor_oracle": true,
        "is_over_subscribed": true,
        "is_unlimited": true,
        "display_name": "display_name_example",
        "vendor_name": "vendor_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "images": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "listing_name": "listing_name_example",
            "publisher": "publisher_example",
            "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
            "package_version": "package_version_example"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.license_manager import LicenseManagerClient
    from oci.license_manager.models import CreateProductLicenseDetails
    from oci.license_manager.models import UpdateProductLicenseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProductLicenseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ProductLicenseHelperGen, self).get_possible_entity_types() + [
            "licensemanagerproductlicense",
            "licensemanagerproductlicenses",
            "licenseManagerlicensemanagerproductlicense",
            "licenseManagerlicensemanagerproductlicenses",
            "licensemanagerproductlicenseresource",
            "licensemanagerproductlicensesresource",
            "productlicense",
            "productlicenses",
            "licenseManagerproductlicense",
            "licenseManagerproductlicenses",
            "productlicenseresource",
            "productlicensesresource",
            "licensemanager",
        ]

    def get_module_resource_id_param(self):
        return "product_license_id"

    def get_module_resource_id(self):
        return self.module.params.get("product_license_id")

    def get_get_fn(self):
        return self.client.get_product_license

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_product_license, product_license_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_product_license,
            product_license_id=self.module.params.get("product_license_id"),
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
            self.client.list_product_licenses, **kwargs
        )

    def get_create_model_class(self):
        return CreateProductLicenseDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_product_license,
            call_fn_args=(),
            call_fn_kwargs=dict(create_product_license_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateProductLicenseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_product_license,
            call_fn_args=(),
            call_fn_kwargs=dict(
                product_license_id=self.module.params.get("product_license_id"),
                update_product_license_details=update_details,
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
            call_fn=self.client.delete_product_license,
            call_fn_args=(),
            call_fn_kwargs=dict(
                product_license_id=self.module.params.get("product_license_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ProductLicenseHelperCustom = get_custom_class("ProductLicenseHelperCustom")


class ResourceHelper(ProductLicenseHelperCustom, ProductLicenseHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            is_vendor_oracle=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            license_unit=dict(
                type="str", choices=["OCPU", "NAMED_USER_PLUS", "PROCESSORS"]
            ),
            vendor_name=dict(type="str"),
            images=dict(
                type="list",
                elements="dict",
                options=dict(
                    listing_id=dict(type="str", required=True),
                    package_version=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            product_license_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="product_license",
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
