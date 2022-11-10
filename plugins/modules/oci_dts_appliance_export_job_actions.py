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
module: oci_dts_appliance_export_job_actions
short_description: Perform actions on an ApplianceExportJob resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ApplianceExportJob resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a ApplianceExportJob into a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    appliance_export_job_id:
        description:
            - ID of the Appliance Export Job
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID],https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resources should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ApplianceExportJob.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on appliance_export_job
  oci_dts_appliance_export_job_actions:
    # required
    appliance_export_job_id: "ocid1.applianceexportjob.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
appliance_export_job:
    description:
        - Details of the ApplianceExportJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        bucket_name:
            description:
                - ""
            returned: on success
            type: str
            sample: bucket_name_example
        display_name:
            description:
                - ""
            returned: on success
            type: str
            sample: display_name_example
        creation_time:
            description:
                - ""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - ""
            returned: on success
            type: str
            sample: CREATING
        lifecycle_state_details:
            description:
                - A property that can contain details on the lifecycle.
            returned: on success
            type: str
            sample: lifecycle_state_details_example
        appliance_serial_number:
            description:
                - Serial Number of the Appliance associated with this Export Job.
            returned: on success
            type: str
            sample: appliance_serial_number_example
        appliance_decryption_passphrase:
            description:
                - Passphrase associated with the Appliance.
            returned: on success
            type: str
            sample: appliance_decryption_passphrase_example
        appliance_delivery_vendor:
            description:
                - Shipping Vendor selected to ship the Appliance associated with this job.
            returned: on success
            type: str
            sample: appliance_delivery_vendor_example
        appliance_delivery_tracking_number:
            description:
                - Tracking number associated with the shipment while shipping the Appliance to Customer.
            returned: on success
            type: str
            sample: appliance_delivery_tracking_number_example
        appliance_return_delivery_tracking_number:
            description:
                - Tracking number associated with the shipment while shipping the Appliance back to Oracle.
            returned: on success
            type: str
            sample: appliance_return_delivery_tracking_number_example
        sending_security_tie:
            description:
                - Unique number associated with the security tie used to seal the Appliance case.
            returned: on success
            type: str
            sample: sending_security_tie_example
        receiving_security_tie:
            description:
                - Unique number associated with the return security tie used to seal the Appliance case.
            returned: on success
            type: str
            sample: receiving_security_tie_example
        prefix:
            description:
                - List of objects with names matching this prefix would be part of this export job.
            returned: on success
            type: str
            sample: prefix_example
        range_start:
            description:
                - The name of the first object in the range of objects that are expected to be part of this export job.
            returned: on success
            type: str
            sample: range_start_example
        range_end:
            description:
                - The name of the last object in the range of objects that are expected to be part of this export job.
            returned: on success
            type: str
            sample: range_end_example
        number_of_objects:
            description:
                - Total number of objects that are exported in this job.
            returned: on success
            type: str
            sample: number_of_objects_example
        total_size_in_bytes:
            description:
                - Total size of objects in Bytes that are exported in this job.
            returned: on success
            type: str
            sample: total_size_in_bytes_example
        first_object:
            description:
                - First object in the list of objects that are exported in this job.
            returned: on success
            type: str
            sample: first_object_example
        last_object:
            description:
                - Last object in the list of objects that are exported in this job.
            returned: on success
            type: str
            sample: last_object_example
        next_object:
            description:
                - First object from which the next potential export job could start.
            returned: on success
            type: str
            sample: next_object_example
        manifest_file:
            description:
                - Url of the Manifest File associated with this export job.
            returned: on success
            type: str
            sample: manifest_file_example
        manifest_md5:
            description:
                - md5 digest of the manifest file.
            returned: on success
            type: str
            sample: manifest_md5_example
        bucket_access_policies:
            description:
                - Polices to grant Data Transfer Service to access objects in the Bucket
            returned: on success
            type: list
            sample: []
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
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "bucket_name": "bucket_name_example",
        "display_name": "display_name_example",
        "creation_time": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "appliance_serial_number": "appliance_serial_number_example",
        "appliance_decryption_passphrase": "appliance_decryption_passphrase_example",
        "appliance_delivery_vendor": "appliance_delivery_vendor_example",
        "appliance_delivery_tracking_number": "appliance_delivery_tracking_number_example",
        "appliance_return_delivery_tracking_number": "appliance_return_delivery_tracking_number_example",
        "sending_security_tie": "sending_security_tie_example",
        "receiving_security_tie": "receiving_security_tie_example",
        "prefix": "prefix_example",
        "range_start": "range_start_example",
        "range_end": "range_end_example",
        "number_of_objects": "number_of_objects_example",
        "total_size_in_bytes": "total_size_in_bytes_example",
        "first_object": "first_object_example",
        "last_object": "last_object_example",
        "next_object": "next_object_example",
        "manifest_file": "manifest_file_example",
        "manifest_md5": "manifest_md5_example",
        "bucket_access_policies": [],
        "return_shipping_label_uri": "return_shipping_label_uri_example",
        "expected_return_date": "2013-10-20T19:20:30+01:00",
        "pickup_window_start_time": "2013-10-20T19:20:30+01:00",
        "pickup_window_end_time": "2013-10-20T19:20:30+01:00",
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
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.dts import ApplianceExportJobClient
    from oci.dts.models import ChangeApplianceExportJobCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApplianceExportJobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "appliance_export_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("appliance_export_job_id")

    def get_get_fn(self):
        return self.client.get_appliance_export_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_appliance_export_job,
            appliance_export_job_id=self.module.params.get("appliance_export_job_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeApplianceExportJobCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_appliance_export_job_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                appliance_export_job_id=self.module.params.get(
                    "appliance_export_job_id"
                ),
                change_appliance_export_job_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


ApplianceExportJobActionsHelperCustom = get_custom_class(
    "ApplianceExportJobActionsHelperCustom"
)


class ResourceHelper(
    ApplianceExportJobActionsHelperCustom, ApplianceExportJobActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            appliance_export_job_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="appliance_export_job",
        service_client_class=ApplianceExportJobClient,
        namespace="dts",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
