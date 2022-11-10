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
module: oci_license_manager_bulk_upload_license_records_actions
short_description: Perform actions on a BulkUploadLicenseRecords resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BulkUploadLicenseRecords resource in Oracle Cloud Infrastructure
    - For I(action=bulk_upload_license_records), bulk upload the product licenses and license records for a given compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) where license records are created.
        type: str
        required: true
    file_name:
        description:
            - Name of the file that is being uploaded.
        type: str
        required: true
    file_content:
        description:
            - The file to be uploaded.
        type: str
        required: true
    action:
        description:
            - The action to perform on the BulkUploadLicenseRecords.
        type: str
        required: true
        choices:
            - "bulk_upload_license_records"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action bulk_upload_license_records on bulk_upload_license_records
  oci_license_manager_bulk_upload_license_records_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    file_name: file_name_example
    file_content: file_content_example
    action: bulk_upload_license_records

"""

RETURN = """
bulk_upload_response:
    description:
        - Details of the BulkUploadLicenseRecords resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        total_supported_records:
            description:
                - The number of license records which were supported.
            returned: on success
            type: int
            sample: 56
        total_supported_records_saved:
            description:
                - The number of supported license records that were uploaded successfully.
            returned: on success
            type: int
            sample: 56
        total_supported_duplicate_records:
            description:
                - The number of supported license records that were valid but not uploaded since they were duplicates.
            returned: on success
            type: int
            sample: 56
        total_supported_failed_license_records:
            description:
                - The number of supported license records that were valid but failed with errors during upload.
            returned: on success
            type: int
            sample: 56
        total_supported_invalid_records:
            description:
                - The number of supported license records that could not be uploaded since they were invalid.
            returned: on success
            type: int
            sample: 56
        validation_error_info:
            description:
                - Detailed error information corresponding to each supported but invalid row for the uploaded file.
            returned: on success
            type: complex
            contains:
                row_number:
                    description:
                        - Refers to the license record number as provided in the bulk upload file.
                    returned: on success
                    type: int
                    sample: 56
                product_name:
                    description:
                        - Product name of invalid row.
                    returned: on success
                    type: str
                    sample: product_name_example
                row_error:
                    description:
                        - Error information corresponding to each column.
                    returned: on success
                    type: complex
                    contains:
                        column_index:
                            description:
                                - Column index as in the given bulk upload file.
                            returned: on success
                            type: str
                            sample: column_index_example
                        error_info:
                            description:
                                - Error information corresponding to a particular column.
                            returned: on success
                            type: str
                            sample: error_info_example
        failed_license_record_info:
            description:
                - Error information corresponding to the supported records which are valid but could not be created.
            returned: on success
            type: complex
            contains:
                row_number:
                    description:
                        - Refers to the license record number as provided in the bulk upload file.
                    returned: on success
                    type: int
                    sample: 56
                product_name:
                    description:
                        - Product name of the failed row.
                    returned: on success
                    type: str
                    sample: product_name_example
                error:
                    description:
                        - Failed license record error information.
                    returned: on success
                    type: str
                    sample: error_example
        message:
            description:
                - Response message for bulk upload.
            returned: on success
            type: str
            sample: message_example
    sample: {
        "total_supported_records": 56,
        "total_supported_records_saved": 56,
        "total_supported_duplicate_records": 56,
        "total_supported_failed_license_records": 56,
        "total_supported_invalid_records": 56,
        "validation_error_info": [{
            "row_number": 56,
            "product_name": "product_name_example",
            "row_error": [{
                "column_index": "column_index_example",
                "error_info": "error_info_example"
            }]
        }],
        "failed_license_record_info": [{
            "row_number": 56,
            "product_name": "product_name_example",
            "error": "error_example"
        }],
        "message": "message_example"
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
    from oci.license_manager import LicenseManagerClient
    from oci.license_manager.models import BulkUploadLicenseRecordsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BulkUploadLicenseRecordsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        bulk_upload_license_records
    """

    def bulk_upload_license_records(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkUploadLicenseRecordsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_upload_license_records,
            call_fn_args=(),
            call_fn_kwargs=dict(bulk_upload_license_records_details=action_details,),
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


BulkUploadLicenseRecordsActionsHelperCustom = get_custom_class(
    "BulkUploadLicenseRecordsActionsHelperCustom"
)


class ResourceHelper(
    BulkUploadLicenseRecordsActionsHelperCustom,
    BulkUploadLicenseRecordsActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            file_name=dict(type="str", required=True),
            file_content=dict(type="str", required=True),
            action=dict(
                type="str", required=True, choices=["bulk_upload_license_records"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bulk_upload_license_records",
        service_client_class=LicenseManagerClient,
        namespace="license_manager",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
