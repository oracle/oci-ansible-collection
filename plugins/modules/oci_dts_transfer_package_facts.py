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
module: oci_dts_transfer_package_facts
short_description: Fetches details about one or multiple TransferPackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TransferPackage resources in Oracle Cloud Infrastructure
    - Lists Transfer Packages associated with a transferJob
    - If I(transfer_package_label) is specified, the details of a single TransferPackage will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    transfer_package_label:
        description:
            - Label of the Transfer Package
            - Required to get a specific transfer_package.
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
            - "PREPARING"
            - "SHIPPING"
            - "RECEIVED"
            - "PROCESSING"
            - "PROCESSED"
            - "RETURNED"
            - "DELETED"
            - "CANCELLED"
            - "CANCELLED_RETURNED"
    display_name:
        description:
            - filtering by displayName
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific transfer_package
  oci_dts_transfer_package_facts:
    # required
    transfer_package_label: transfer_package_label_example
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: List transfer_packages
  oci_dts_transfer_package_facts:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: PREPARING
    display_name: display_name_example

"""

RETURN = """
transfer_packages:
    description:
        - List of TransferPackage resources
    returned: on success
    type: complex
    contains:
        label:
            description:
                - ""
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
            sample: PREPARING
        transfer_job_id:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx"
        creation_time:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        original_package_delivery_tracking_number:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: original_package_delivery_tracking_number_example
        return_package_delivery_tracking_number:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: return_package_delivery_tracking_number_example
        package_delivery_vendor:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: package_delivery_vendor_example
        transfer_site_shipping_address:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: transfer_site_shipping_address_example
        attached_transfer_device_labels:
            description:
                - Transfer Devices attached to this Transfer Package
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        transfer_package_objects:
            description:
                - List of TransferPackage summary's
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
                    sample: PREPARING
                creation_time:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "label": "label_example",
        "lifecycle_state": "PREPARING",
        "transfer_job_id": "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx",
        "creation_time": "2013-10-20T19:20:30+01:00",
        "original_package_delivery_tracking_number": "original_package_delivery_tracking_number_example",
        "return_package_delivery_tracking_number": "return_package_delivery_tracking_number_example",
        "package_delivery_vendor": "package_delivery_vendor_example",
        "transfer_site_shipping_address": "transfer_site_shipping_address_example",
        "attached_transfer_device_labels": [],
        "transfer_package_objects": [{
            "label": "label_example",
            "lifecycle_state": "PREPARING",
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
    from oci.dts import TransferPackageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferPackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "id",
            "transfer_package_label",
        ]

    def get_required_params_for_list(self):
        return [
            "id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_package,
            id=self.module.params.get("id"),
            transfer_package_label=self.module.params.get("transfer_package_label"),
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
            self.client.list_transfer_packages,
            id=self.module.params.get("id"),
            **optional_kwargs
        )


TransferPackageFactsHelperCustom = get_custom_class("TransferPackageFactsHelperCustom")


class ResourceFactsHelper(
    TransferPackageFactsHelperCustom, TransferPackageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            transfer_package_label=dict(type="str"),
            id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PREPARING",
                    "SHIPPING",
                    "RECEIVED",
                    "PROCESSING",
                    "PROCESSED",
                    "RETURNED",
                    "DELETED",
                    "CANCELLED",
                    "CANCELLED_RETURNED",
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
        resource_type="transfer_package",
        service_client_class=TransferPackageClient,
        namespace="dts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(transfer_packages=result)


if __name__ == "__main__":
    main()
