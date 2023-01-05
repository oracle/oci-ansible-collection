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
module: oci_dts_appliance_export_job
short_description: Manage an ApplianceExportJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ApplianceExportJob resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Appliance Export Job that corresponds with customer's logical dataset
    - "This resource has the following action operations in the M(oracle.oci.oci_dts_appliance_export_job_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - ""
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    bucket_name:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    prefix:
        description:
            - List of objects with names matching this prefix would be part of this export job.
            - This parameter is updatable.
        type: str
    range_start:
        description:
            - Object names returned by a list query must be greater or equal to this parameter.
            - This parameter is updatable.
        type: str
    range_end:
        description:
            - Object names returned by a list query must be strictly less than this parameter.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - ""
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - ""
            - This parameter is updatable.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INPROGRESS"
            - "SUCCEEDED"
            - "FAILED"
            - "CANCELLED"
            - "DELETED"
    lifecycle_state_details:
        description:
            - A property that can contain details on the lifecycle.
            - This parameter is updatable.
        type: str
    manifest_file:
        description:
            - Manifest File associated with this export job.
            - This parameter is updatable.
        type: str
    manifest_md5:
        description:
            - md5 digest of the manifest file.
            - This parameter is updatable.
        type: str
    number_of_objects:
        description:
            - Total number of objects that are exported in this job.
            - This parameter is updatable.
        type: str
    total_size_in_bytes:
        description:
            - Total size of objects in Bytes that are exported in this job.
            - This parameter is updatable.
        type: str
    first_object:
        description:
            - First object in the list of objects that are exported in this job.
            - This parameter is updatable.
        type: str
    last_object:
        description:
            - Last object in the list of objects that are exported in this job.
            - This parameter is updatable.
        type: str
    next_object:
        description:
            - First object from which the next potential export job could start.
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
    customer_shipping_address:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            addressee:
                description:
                    - ""
                type: str
                required: true
            care_of:
                description:
                    - ""
                type: str
            address1:
                description:
                    - ""
                type: str
                required: true
            address2:
                description:
                    - ""
                type: str
            address3:
                description:
                    - ""
                type: str
            address4:
                description:
                    - ""
                type: str
            city_or_locality:
                description:
                    - ""
                type: str
                required: true
            state_or_region:
                description:
                    - ""
                type: str
                required: true
            zipcode:
                description:
                    - ""
                type: str
                required: true
            country:
                description:
                    - ""
                type: str
                required: true
            phone_number:
                description:
                    - ""
                type: str
            email:
                description:
                    - ""
                type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    appliance_export_job_id:
        description:
            - ID of the Appliance Export Job
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ApplianceExportJob.
            - Use I(state=present) to create or update an ApplianceExportJob.
            - Use I(state=absent) to delete an ApplianceExportJob.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create appliance_export_job
  oci_dts_appliance_export_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    bucket_name: bucket_name_example
    display_name: display_name_example
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

    # optional
    prefix: prefix_example
    range_start: range_start_example
    range_end: range_end_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update appliance_export_job
  oci_dts_appliance_export_job:
    # required
    appliance_export_job_id: "ocid1.applianceexportjob.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    bucket_name: bucket_name_example
    prefix: prefix_example
    range_start: range_start_example
    range_end: range_end_example
    display_name: display_name_example
    lifecycle_state: CREATING
    lifecycle_state_details: lifecycle_state_details_example
    manifest_file: manifest_file_example
    manifest_md5: manifest_md5_example
    number_of_objects: number_of_objects_example
    total_size_in_bytes: total_size_in_bytes_example
    first_object: first_object_example
    last_object: last_object_example
    next_object: next_object_example
    expected_return_date: expected_return_date_example
    pickup_window_start_time: pickup_window_start_time_example
    pickup_window_end_time: pickup_window_end_time_example
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
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update appliance_export_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dts_appliance_export_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    bucket_name: bucket_name_example
    prefix: prefix_example
    range_start: range_start_example
    range_end: range_end_example
    lifecycle_state: CREATING
    lifecycle_state_details: lifecycle_state_details_example
    manifest_file: manifest_file_example
    manifest_md5: manifest_md5_example
    number_of_objects: number_of_objects_example
    total_size_in_bytes: total_size_in_bytes_example
    first_object: first_object_example
    last_object: last_object_example
    next_object: next_object_example
    expected_return_date: expected_return_date_example
    pickup_window_start_time: pickup_window_start_time_example
    pickup_window_end_time: pickup_window_end_time_example
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
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete appliance_export_job
  oci_dts_appliance_export_job:
    # required
    appliance_export_job_id: "ocid1.applianceexportjob.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete appliance_export_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_dts_appliance_export_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.dts import ApplianceExportJobClient
    from oci.dts.models import CreateApplianceExportJobDetails
    from oci.dts.models import UpdateApplianceExportJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApplianceExportJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ApplianceExportJobHelperGen, self).get_possible_entity_types() + [
            "applianceexportjob",
            "applianceexportjobs",
            "dtsapplianceexportjob",
            "dtsapplianceexportjobs",
            "applianceexportjobresource",
            "applianceexportjobsresource",
            "dts",
        ]

    def get_module_resource_id_param(self):
        return "appliance_export_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("appliance_export_job_id")

    def get_get_fn(self):
        return self.client.get_appliance_export_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_appliance_export_job,
            appliance_export_job_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_appliance_export_job,
            appliance_export_job_id=self.module.params.get("appliance_export_job_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["lifecycle_state", "display_name"]
        )

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
            self.client.list_appliance_export_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateApplianceExportJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_appliance_export_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_appliance_export_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateApplianceExportJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_appliance_export_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                appliance_export_job_id=self.module.params.get(
                    "appliance_export_job_id"
                ),
                update_appliance_export_job_details=update_details,
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
            call_fn=self.client.delete_appliance_export_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                appliance_export_job_id=self.module.params.get(
                    "appliance_export_job_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ApplianceExportJobHelperCustom = get_custom_class("ApplianceExportJobHelperCustom")


class ResourceHelper(ApplianceExportJobHelperCustom, ApplianceExportJobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            bucket_name=dict(type="str"),
            prefix=dict(type="str"),
            range_start=dict(type="str"),
            range_end=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INPROGRESS",
                    "SUCCEEDED",
                    "FAILED",
                    "CANCELLED",
                    "DELETED",
                ],
            ),
            lifecycle_state_details=dict(type="str"),
            manifest_file=dict(type="str"),
            manifest_md5=dict(type="str"),
            number_of_objects=dict(type="str"),
            total_size_in_bytes=dict(type="str"),
            first_object=dict(type="str"),
            last_object=dict(type="str"),
            next_object=dict(type="str"),
            expected_return_date=dict(type="str"),
            pickup_window_start_time=dict(type="str"),
            pickup_window_end_time=dict(type="str"),
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
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            appliance_export_job_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
