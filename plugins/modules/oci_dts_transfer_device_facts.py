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
module: oci_dts_transfer_device_facts
short_description: Fetches details about one or multiple TransferDevice resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TransferDevice resources in Oracle Cloud Infrastructure
    - Lists Transfer Devices associated with a transferJob
    - If I(transfer_device_label) is specified, the details of a single TransferDevice will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    transfer_device_label:
        description:
            - Label of the Transfer Device
            - Required to get a specific transfer_device.
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
            - "READY"
            - "PACKAGED"
            - "ACTIVE"
            - "PROCESSING"
            - "COMPLETE"
            - "MISSING"
            - "ERROR"
            - "DELETED"
            - "CANCELLED"
    display_name:
        description:
            - filtering by displayName
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific transfer_device
  oci_dts_transfer_device_facts:
    # required
    transfer_device_label: transfer_device_label_example
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: List transfer_devices
  oci_dts_transfer_device_facts:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: PREPARING
    display_name: display_name_example

"""

RETURN = """
transfer_devices:
    description:
        - List of TransferDevice resources
    returned: on success
    type: complex
    contains:
        serial_number:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: serial_number_example
        iscsi_iqn:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: iscsi_iqn_example
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
        attached_transfer_package_label:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: attached_transfer_package_label_example
        creation_time:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        upload_status_log_uri:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: str
            sample: upload_status_log_uri_example
        transfer_device_objects:
            description:
                - List of TransferDeviceObject's
                - Returned for list operation
            returned: on success
            type: complex
            contains:
                serial_number:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: serial_number_example
                iscsi_iqn:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: iscsi_iqn_example
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
                attached_transfer_package_label:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: attached_transfer_package_label_example
                creation_time:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                upload_status_log_uri:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: upload_status_log_uri_example
    sample: [{
        "serial_number": "serial_number_example",
        "iscsi_iqn": "iscsi_iqn_example",
        "label": "label_example",
        "lifecycle_state": "PREPARING",
        "transfer_job_id": "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx",
        "attached_transfer_package_label": "attached_transfer_package_label_example",
        "creation_time": "2013-10-20T19:20:30+01:00",
        "upload_status_log_uri": "upload_status_log_uri_example",
        "transfer_device_objects": [{
            "serial_number": "serial_number_example",
            "iscsi_iqn": "iscsi_iqn_example",
            "label": "label_example",
            "lifecycle_state": "PREPARING",
            "attached_transfer_package_label": "attached_transfer_package_label_example",
            "creation_time": "2013-10-20T19:20:30+01:00",
            "upload_status_log_uri": "upload_status_log_uri_example"
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
    from oci.dts import TransferDeviceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferDeviceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "id",
            "transfer_device_label",
        ]

    def get_required_params_for_list(self):
        return [
            "id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_device,
            id=self.module.params.get("id"),
            transfer_device_label=self.module.params.get("transfer_device_label"),
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
            self.client.list_transfer_devices,
            id=self.module.params.get("id"),
            **optional_kwargs
        )


TransferDeviceFactsHelperCustom = get_custom_class("TransferDeviceFactsHelperCustom")


class ResourceFactsHelper(
    TransferDeviceFactsHelperCustom, TransferDeviceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            transfer_device_label=dict(type="str"),
            id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PREPARING",
                    "READY",
                    "PACKAGED",
                    "ACTIVE",
                    "PROCESSING",
                    "COMPLETE",
                    "MISSING",
                    "ERROR",
                    "DELETED",
                    "CANCELLED",
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
        resource_type="transfer_device",
        service_client_class=TransferDeviceClient,
        namespace="dts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(transfer_devices=result)


if __name__ == "__main__":
    main()
