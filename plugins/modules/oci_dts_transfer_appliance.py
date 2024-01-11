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
module: oci_dts_transfer_appliance
short_description: Manage a TransferAppliance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a TransferAppliance resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    lifecycle_state:
        description:
            - ""
            - This parameter is updatable.
        type: str
        choices:
            - "PREPARING"
            - "FINALIZED"
            - "RETURN_LABEL_REQUESTED"
            - "RETURN_LABEL_GENERATING"
            - "RETURN_LABEL_AVAILABLE"
            - "DELETED"
            - "CUSTOMER_NEVER_RECEIVED"
            - "CANCELLED"
    customer_shipping_address:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            addressee:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
                required: true
            care_of:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
            address1:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
                required: true
            address2:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
            address3:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
            address4:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
            city_or_locality:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
                required: true
            state_or_region:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
                required: true
            zipcode:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
                required: true
            country:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
                required: true
            phone_number:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
            email:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
    expected_return_date:
        description:
            - Expected return date from customer for the device, time portion should be zero.
            - This parameter is updatable.
        type: str
    pickup_window_start_time:
        description:
            - Start time for the window to pickup the device from customer.
            - This parameter is updatable.
        type: str
    pickup_window_end_time:
        description:
            - End time for the window to pickup the device from customer.
            - This parameter is updatable.
        type: str
    minimum_storage_capacity_in_terabytes:
        description:
            - Minimum storage capacity of the device, in terabytes. Valid options are 50, 95 and 150.
            - This parameter is updatable.
        type: int
    id:
        description:
            - ID of the Transfer Job
        type: str
        required: true
    transfer_appliance_label:
        description:
            - Label of the Transfer Appliance
        type: str
        required: true
    state:
        description:
            - The state of the TransferAppliance.
            - Use I(state=present) to update an existing a TransferAppliance.
            - Use I(state=absent) to delete a TransferAppliance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update transfer_appliance
  oci_dts_transfer_appliance:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    transfer_appliance_label: transfer_appliance_label_example

    # optional
    lifecycle_state: PREPARING
    customer_shipping_address:
      # required
      addressee: addressee_example
      address1: address1_example
      city_or_locality: city_or_locality_example
      state_or_region: us-phoenix-1
      zipcode: zipcode_example
      country: country_example

      # optional
      care_of: care_of_example
      address2: address2_example
      address3: address3_example
      address4: address4_example
      phone_number: phone_number_example
      email: email_example
    expected_return_date: expected_return_date_example
    pickup_window_start_time: pickup_window_start_time_example
    pickup_window_end_time: pickup_window_end_time_example
    minimum_storage_capacity_in_terabytes: 56

- name: Delete transfer_appliance
  oci_dts_transfer_appliance:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    transfer_appliance_label: transfer_appliance_label_example
    state: absent

"""

RETURN = """
transfer_appliance:
    description:
        - Details of the TransferAppliance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        label:
            description:
                - Unique alpha-numeric identifier for a transfer appliance auto generated during create.
            returned: on success
            type: str
            sample: label_example
        lifecycle_state:
            description:
                - ""
            returned: on success
            type: str
            sample: REQUESTED
        transfer_job_id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx"
        serial_number:
            description:
                - ""
            returned: on success
            type: str
            sample: serial_number_example
        creation_time:
            description:
                - ""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        customer_received_time:
            description:
                - ""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        customer_returned_time:
            description:
                - ""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        next_billing_time:
            description:
                - ""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        delivery_security_tie_id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.deliverysecuritytie.oc1..xxxxxxEXAMPLExxxxxx"
        return_security_tie_id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.returnsecuritytie.oc1..xxxxxxEXAMPLExxxxxx"
        appliance_delivery_tracking_number:
            description:
                - ""
            returned: on success
            type: str
            sample: appliance_delivery_tracking_number_example
        appliance_return_delivery_tracking_number:
            description:
                - ""
            returned: on success
            type: str
            sample: appliance_return_delivery_tracking_number_example
        appliance_delivery_vendor:
            description:
                - ""
            returned: on success
            type: str
            sample: appliance_delivery_vendor_example
        customer_shipping_address:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                addressee:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: addressee_example
                care_of:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: care_of_example
                address1:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: address1_example
                address2:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: address2_example
                address3:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: address3_example
                address4:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: address4_example
                city_or_locality:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: city_or_locality_example
                state_or_region:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                zipcode:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: zipcode_example
                country:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: country_example
                phone_number:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: phone_number_example
                email:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: email_example
        upload_status_log_uri:
            description:
                - ""
            returned: on success
            type: str
            sample: upload_status_log_uri_example
        return_shipping_label_uri:
            description:
                - ""
            returned: on success
            type: str
            sample: return_shipping_label_uri_example
        expected_return_date:
            description:
                - Expected return date from customer for the device, time portion should be zero.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        pickup_window_start_time:
            description:
                - Start time for the window to pickup the device from customer.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        pickup_window_end_time:
            description:
                - End time for the window to pickup the device from customer.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        minimum_storage_capacity_in_terabytes:
            description:
                - Minimum storage capacity of the device, in terabytes. Valid options are 50, 95 and 150.
            returned: on success
            type: int
            sample: 56
    sample: {
        "label": "label_example",
        "lifecycle_state": "REQUESTED",
        "transfer_job_id": "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx",
        "serial_number": "serial_number_example",
        "creation_time": "2013-10-20T19:20:30+01:00",
        "customer_received_time": "2013-10-20T19:20:30+01:00",
        "customer_returned_time": "2013-10-20T19:20:30+01:00",
        "next_billing_time": "2013-10-20T19:20:30+01:00",
        "delivery_security_tie_id": "ocid1.deliverysecuritytie.oc1..xxxxxxEXAMPLExxxxxx",
        "return_security_tie_id": "ocid1.returnsecuritytie.oc1..xxxxxxEXAMPLExxxxxx",
        "appliance_delivery_tracking_number": "appliance_delivery_tracking_number_example",
        "appliance_return_delivery_tracking_number": "appliance_return_delivery_tracking_number_example",
        "appliance_delivery_vendor": "appliance_delivery_vendor_example",
        "customer_shipping_address": {
            "addressee": "addressee_example",
            "care_of": "care_of_example",
            "address1": "address1_example",
            "address2": "address2_example",
            "address3": "address3_example",
            "address4": "address4_example",
            "city_or_locality": "city_or_locality_example",
            "state_or_region": "us-phoenix-1",
            "zipcode": "zipcode_example",
            "country": "country_example",
            "phone_number": "phone_number_example",
            "email": "email_example"
        },
        "upload_status_log_uri": "upload_status_log_uri_example",
        "return_shipping_label_uri": "return_shipping_label_uri_example",
        "expected_return_date": "2013-10-20T19:20:30+01:00",
        "pickup_window_start_time": "2013-10-20T19:20:30+01:00",
        "pickup_window_end_time": "2013-10-20T19:20:30+01:00",
        "minimum_storage_capacity_in_terabytes": 56
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
    from oci.dts import TransferApplianceClient
    from oci.dts.models import UpdateTransferApplianceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferApplianceHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TransferApplianceHelperGen, self).get_possible_entity_types() + [
            "transferappliance",
            "transferappliances",
            "dtstransferappliance",
            "dtstransferappliances",
            "transferapplianceresource",
            "transferappliancesresource",
            "dts",
        ]

    def get_module_resource_id_param(self):
        return "transfer_appliance_label"

    def get_module_resource_id(self):
        return self.module.params.get("transfer_appliance_label")

    def get_get_fn(self):
        return self.client.get_transfer_appliance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_appliance,
            id=self.module.params.get("id"),
            transfer_appliance_label=self.module.params.get("transfer_appliance_label"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["lifecycle_state"]

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
            self.client.list_transfer_appliances, **kwargs
        )

    def get_update_model_class(self):
        return UpdateTransferApplianceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_transfer_appliance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                transfer_appliance_label=self.module.params.get(
                    "transfer_appliance_label"
                ),
                update_transfer_appliance_details=update_details,
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
            call_fn=self.client.delete_transfer_appliance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                transfer_appliance_label=self.module.params.get(
                    "transfer_appliance_label"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TransferApplianceHelperCustom = get_custom_class("TransferApplianceHelperCustom")


class ResourceHelper(TransferApplianceHelperCustom, TransferApplianceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PREPARING",
                    "FINALIZED",
                    "RETURN_LABEL_REQUESTED",
                    "RETURN_LABEL_GENERATING",
                    "RETURN_LABEL_AVAILABLE",
                    "DELETED",
                    "CUSTOMER_NEVER_RECEIVED",
                    "CANCELLED",
                ],
            ),
            customer_shipping_address=dict(
                type="dict",
                options=dict(
                    addressee=dict(type="str", required=True),
                    care_of=dict(type="str"),
                    address1=dict(type="str", required=True),
                    address2=dict(type="str"),
                    address3=dict(type="str"),
                    address4=dict(type="str"),
                    city_or_locality=dict(type="str", required=True),
                    state_or_region=dict(type="str", required=True),
                    zipcode=dict(type="str", required=True),
                    country=dict(type="str", required=True),
                    phone_number=dict(type="str"),
                    email=dict(type="str"),
                ),
            ),
            expected_return_date=dict(type="str"),
            pickup_window_start_time=dict(type="str"),
            pickup_window_end_time=dict(type="str"),
            minimum_storage_capacity_in_terabytes=dict(type="int"),
            id=dict(type="str", required=True),
            transfer_appliance_label=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="transfer_appliance",
        service_client_class=TransferApplianceClient,
        namespace="dts",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
