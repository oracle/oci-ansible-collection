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
module: oci_dts_transfer_job_facts
short_description: Fetches details about one or multiple TransferJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TransferJob resources in Oracle Cloud Infrastructure
    - Lists Transfer Jobs in a given compartment
    - If I(id) is specified, the details of a single TransferJob will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    id:
        description:
            - OCID of the Transfer Job
            - Required to get a specific transfer_job.
        type: str
    compartment_id:
        description:
            - compartment id
            - Required to list multiple transfer_jobs.
        type: str
    lifecycle_state:
        description:
            - filtering by lifecycleState
        type: str
        choices:
            - "INITIATED"
            - "PREPARING"
            - "ACTIVE"
            - "DELETED"
            - "CLOSED"
    display_name:
        description:
            - filtering by displayName
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific transfer_job
  oci_dts_transfer_job_facts:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

- name: List transfer_jobs
  oci_dts_transfer_job_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: INITIATED
    display_name: display_name_example

"""

RETURN = """
transfer_jobs:
    description:
        - List of TransferJob resources
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
        attached_transfer_appliance_labels:
            description:
                - Transfer Appliance labels associated with this transfer Job
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        attached_transfer_package_labels:
            description:
                - Transfer Package labels associated with this transfer Job
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        attached_transfer_device_labels:
            description:
                - Transfer Device labels associated with this transfer Job
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        upload_bucket_name:
            description:
                - ""
            returned: on success
            type: str
            sample: upload_bucket_name_example
        display_name:
            description:
                - ""
            returned: on success
            type: str
            sample: display_name_example
        label:
            description:
                - ""
            returned: on success
            type: str
            sample: label_example
        device_type:
            description:
                - ""
            returned: on success
            type: str
            sample: DISK
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
            sample: INITIATED
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
        "attached_transfer_appliance_labels": [],
        "attached_transfer_package_labels": [],
        "attached_transfer_device_labels": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "upload_bucket_name": "upload_bucket_name_example",
        "display_name": "display_name_example",
        "label": "label_example",
        "device_type": "DISK",
        "creation_time": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "INITIATED",
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
    from oci.dts import TransferJobClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_job, id=self.module.params.get("id"),
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
            self.client.list_transfer_jobs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TransferJobFactsHelperCustom = get_custom_class("TransferJobFactsHelperCustom")


class ResourceFactsHelper(TransferJobFactsHelperCustom, TransferJobFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            id=dict(type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["INITIATED", "PREPARING", "ACTIVE", "DELETED", "CLOSED"],
            ),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="transfer_job",
        service_client_class=TransferJobClient,
        namespace="dts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(transfer_jobs=result)


if __name__ == "__main__":
    main()
