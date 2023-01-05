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
module: oci_dts_transfer_appliance_facts
short_description: Fetches details about one or multiple TransferAppliance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TransferAppliance resources in Oracle Cloud Infrastructure
    - Lists Transfer Appliances associated with a transferJob
    - If I(transfer_appliance_label) is specified, the details of a single TransferAppliance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    transfer_appliance_label:
        description:
            - Label of the Transfer Appliance
            - Required to get a specific transfer_appliance.
        type: str
    id:
        description:
            - ID of the Transfer Job
        type: str
        required: true
    lifecycle_state:
        description:
            - filtering by lifecycleState
        type: str
        choices:
            - "REQUESTED"
            - "ORACLE_PREPARING"
            - "SHIPPING"
            - "DELIVERED"
            - "PREPARING"
            - "FINALIZED"
            - "RETURN_LABEL_REQUESTED"
            - "RETURN_LABEL_GENERATING"
            - "RETURN_LABEL_AVAILABLE"
            - "RETURN_DELAYED"
            - "RETURN_SHIPPED"
            - "RETURN_SHIPPED_CANCELLED"
            - "ORACLE_RECEIVED"
            - "ORACLE_RECEIVED_CANCELLED"
            - "PROCESSING"
            - "COMPLETE"
            - "CUSTOMER_NEVER_RECEIVED"
            - "ORACLE_NEVER_RECEIVED"
            - "CUSTOMER_LOST"
            - "CANCELLED"
            - "DELETED"
            - "REJECTED"
            - "ERROR"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific transfer_appliance
  oci_dts_transfer_appliance_facts:
    # required
    transfer_appliance_label: transfer_appliance_label_example
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: List transfer_appliances
  oci_dts_transfer_appliance_facts:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: REQUESTED

"""

RETURN = """
transfer_appliances:
    description:
        - List of TransferAppliance resources
    returned: on success
    type: complex
    contains:
        label:
            description:
                - Unique alpha-numeric identifier for a transfer appliance auto generated during create.
                - Returned for get operation
            returned: on success
            type: str
            sample: label_example
        lifecycle_state:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: REQUESTED
        transfer_job_id:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx"
        serial_number:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: serial_number_example
        creation_time:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        customer_received_time:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        customer_returned_time:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        next_billing_time:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        delivery_security_tie_id:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.deliverysecuritytie.oc1..xxxxxxEXAMPLExxxxxx"
        return_security_tie_id:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.returnsecuritytie.oc1..xxxxxxEXAMPLExxxxxx"
        appliance_delivery_tracking_number:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: appliance_delivery_tracking_number_example
        appliance_return_delivery_tracking_number:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: appliance_return_delivery_tracking_number_example
        appliance_delivery_vendor:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: appliance_delivery_vendor_example
        customer_shipping_address:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: str
            sample: upload_status_log_uri_example
        return_shipping_label_uri:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: return_shipping_label_uri_example
        expected_return_date:
            description:
                - Expected return date from customer for the device, time portion should be zero.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        pickup_window_start_time:
            description:
                - Start time for the window to pickup the device from customer.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        pickup_window_end_time:
            description:
                - End time for the window to pickup the device from customer.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        minimum_storage_capacity_in_terabytes:
            description:
                - Minimum storage capacity of the device, in terabytes. Valid options are 50, 95 and 150.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        transfer_appliance_objects:
            description:
                - List of TransferAppliance summary's
                - Returned for list operation
            returned: on success
            type: complex
            contains:
                label:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: label_example
                lifecycle_state:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: REQUESTED
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
    sample: [{
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
        "minimum_storage_capacity_in_terabytes": 56,
        "transfer_appliance_objects": [{
            "label": "label_example",
            "lifecycle_state": "REQUESTED",
            "serial_number": "serial_number_example",
            "creation_time": "2013-10-20T19:20:30+01:00"
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.dts import TransferApplianceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferApplianceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "id",
            "transfer_appliance_label",
        ]

    def get_required_params_for_list(self):
        return [
            "id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_appliance,
            id=self.module.params.get("id"),
            transfer_appliance_label=self.module.params.get("transfer_appliance_label"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_transfer_appliances,
            id=self.module.params.get("id"),
            **optional_kwargs
        )


TransferApplianceFactsHelperCustom = get_custom_class(
    "TransferApplianceFactsHelperCustom"
)


class ResourceFactsHelper(
    TransferApplianceFactsHelperCustom, TransferApplianceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            transfer_appliance_label=dict(type="str"),
            id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "REQUESTED",
                    "ORACLE_PREPARING",
                    "SHIPPING",
                    "DELIVERED",
                    "PREPARING",
                    "FINALIZED",
                    "RETURN_LABEL_REQUESTED",
                    "RETURN_LABEL_GENERATING",
                    "RETURN_LABEL_AVAILABLE",
                    "RETURN_DELAYED",
                    "RETURN_SHIPPED",
                    "RETURN_SHIPPED_CANCELLED",
                    "ORACLE_RECEIVED",
                    "ORACLE_RECEIVED_CANCELLED",
                    "PROCESSING",
                    "COMPLETE",
                    "CUSTOMER_NEVER_RECEIVED",
                    "ORACLE_NEVER_RECEIVED",
                    "CUSTOMER_LOST",
                    "CANCELLED",
                    "DELETED",
                    "REJECTED",
                    "ERROR",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="transfer_appliance",
        service_client_class=TransferApplianceClient,
        namespace="dts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(transfer_appliances=result)


if __name__ == "__main__":
    main()
