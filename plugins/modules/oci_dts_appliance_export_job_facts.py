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
module: oci_dts_appliance_export_job_facts
short_description: Fetches details about one or multiple ApplianceExportJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ApplianceExportJob resources in Oracle Cloud Infrastructure
    - Lists Appliance Export Jobs in a given compartment
    - If I(appliance_export_job_id) is specified, the details of a single ApplianceExportJob will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    appliance_export_job_id:
        description:
            - OCID of the Appliance Export Job
            - Required to get a specific appliance_export_job.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - compartment id
            - Required to list multiple appliance_export_jobs.
        type: str
    lifecycle_state:
        description:
            - filtering by lifecycleState
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INPROGRESS"
            - "SUCCEEDED"
            - "FAILED"
            - "CANCELLED"
            - "DELETED"
    display_name:
        description:
            - filtering by displayName
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific appliance_export_job
  oci_dts_appliance_export_job_facts:
    # required
    appliance_export_job_id: "ocid1.applianceexportjob.oc1..xxxxxxEXAMPLExxxxxx"

- name: List appliance_export_jobs
  oci_dts_appliance_export_job_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example

"""

RETURN = """
appliance_export_jobs:
    description:
        - List of ApplianceExportJob resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        appliance_serial_number:
            description:
                - Serial Number of the Appliance associated with this Export Job.
                - Returned for get operation
            returned: on success
            type: str
            sample: appliance_serial_number_example
        appliance_decryption_passphrase:
            description:
                - Passphrase associated with the Appliance.
                - Returned for get operation
            returned: on success
            type: str
            sample: appliance_decryption_passphrase_example
        appliance_delivery_vendor:
            description:
                - Shipping Vendor selected to ship the Appliance associated with this job.
                - Returned for get operation
            returned: on success
            type: str
            sample: appliance_delivery_vendor_example
        appliance_delivery_tracking_number:
            description:
                - Tracking number associated with the shipment while shipping the Appliance to Customer.
                - Returned for get operation
            returned: on success
            type: str
            sample: appliance_delivery_tracking_number_example
        appliance_return_delivery_tracking_number:
            description:
                - Tracking number associated with the shipment while shipping the Appliance back to Oracle.
                - Returned for get operation
            returned: on success
            type: str
            sample: appliance_return_delivery_tracking_number_example
        sending_security_tie:
            description:
                - Unique number associated with the security tie used to seal the Appliance case.
                - Returned for get operation
            returned: on success
            type: str
            sample: sending_security_tie_example
        receiving_security_tie:
            description:
                - Unique number associated with the return security tie used to seal the Appliance case.
                - Returned for get operation
            returned: on success
            type: str
            sample: receiving_security_tie_example
        prefix:
            description:
                - List of objects with names matching this prefix would be part of this export job.
                - Returned for get operation
            returned: on success
            type: str
            sample: prefix_example
        range_start:
            description:
                - The name of the first object in the range of objects that are expected to be part of this export job.
                - Returned for get operation
            returned: on success
            type: str
            sample: range_start_example
        range_end:
            description:
                - The name of the last object in the range of objects that are expected to be part of this export job.
                - Returned for get operation
            returned: on success
            type: str
            sample: range_end_example
        number_of_objects:
            description:
                - Total number of objects that are exported in this job.
                - Returned for get operation
            returned: on success
            type: str
            sample: number_of_objects_example
        total_size_in_bytes:
            description:
                - Total size of objects in Bytes that are exported in this job.
                - Returned for get operation
            returned: on success
            type: str
            sample: total_size_in_bytes_example
        first_object:
            description:
                - First object in the list of objects that are exported in this job.
                - Returned for get operation
            returned: on success
            type: str
            sample: first_object_example
        last_object:
            description:
                - Last object in the list of objects that are exported in this job.
                - Returned for get operation
            returned: on success
            type: str
            sample: last_object_example
        next_object:
            description:
                - First object from which the next potential export job could start.
                - Returned for get operation
            returned: on success
            type: str
            sample: next_object_example
        manifest_file:
            description:
                - Url of the Manifest File associated with this export job.
                - Returned for get operation
            returned: on success
            type: str
            sample: manifest_file_example
        manifest_md5:
            description:
                - md5 digest of the manifest file.
                - Returned for get operation
            returned: on success
            type: str
            sample: manifest_md5_example
        bucket_access_policies:
            description:
                - Polices to grant Data Transfer Service to access objects in the Bucket
                - Returned for get operation
            returned: on success
            type: list
            sample: []
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
        id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "bucket_name": "bucket_name_example",
        "display_name": "display_name_example",
        "creation_time": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.dts import ApplianceExportJobClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApplianceExportJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "appliance_export_job_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_appliance_export_job,
            appliance_export_job_id=self.module.params.get("appliance_export_job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_appliance_export_jobs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ApplianceExportJobFactsHelperCustom = get_custom_class(
    "ApplianceExportJobFactsHelperCustom"
)


class ResourceFactsHelper(
    ApplianceExportJobFactsHelperCustom, ApplianceExportJobFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            appliance_export_job_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
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
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="appliance_export_job",
        service_client_class=ApplianceExportJobClient,
        namespace="dts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(appliance_export_jobs=result)


if __name__ == "__main__":
    main()
