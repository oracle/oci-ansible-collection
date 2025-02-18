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
module: oci_fusion_apps_data_masking_activity_facts
short_description: Fetches details about one or multiple DataMaskingActivity resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DataMaskingActivity resources in Oracle Cloud Infrastructure
    - Returns a list of DataMaskingActivities.
    - If I(data_masking_activity_id) is specified, the details of a single DataMaskingActivity will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    data_masking_activity_id:
        description:
            - Unique DataMasking run identifier.
            - Required to get a specific data_masking_activity.
        type: str
        aliases: ["id"]
    fusion_environment_id:
        description:
            - unique FusionEnvironment identifier
        type: str
        required: true
    lifecycle_state:
        description:
            - A filter that returns all resources that match the specified status
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "FAILED"
            - "SUCCEEDED"
            - "CANCELED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "TIME_CREATED"
            - "DISPLAY_NAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific data_masking_activity
  oci_fusion_apps_data_masking_activity_facts:
    # required
    data_masking_activity_id: "ocid1.datamaskingactivity.oc1..xxxxxxEXAMPLExxxxxx"
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List data_masking_activities
  oci_fusion_apps_data_masking_activity_facts:
    # required
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACCEPTED
    sort_order: ASC
    sort_by: TIME_CREATED

"""

RETURN = """
data_masking_activities:
    description:
        - List of DataMaskingActivity resources
    returned: on success
    type: complex
    contains:
        fusion_environment_id:
            description:
                - Fusion Environment Identifier.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the DataMaskingActivity.
            returned: on success
            type: str
            sample: ACCEPTED
        time_masking_start:
            description:
                - The time the data masking activity started. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_masking_finish:
            description:
                - The time the data masking activity ended. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "fusion_environment_id": "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACCEPTED",
        "time_masking_start": "2013-10-20T19:20:30+01:00",
        "time_masking_finish": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.fusion_apps import FusionApplicationsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataMaskingActivityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_id",
            "data_masking_activity_id",
        ]

    def get_required_params_for_list(self):
        return [
            "fusion_environment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_masking_activity,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            data_masking_activity_id=self.module.params.get("data_masking_activity_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_data_masking_activities,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            **optional_kwargs
        )


DataMaskingActivityFactsHelperCustom = get_custom_class(
    "DataMaskingActivityFactsHelperCustom"
)


class ResourceFactsHelper(
    DataMaskingActivityFactsHelperCustom, DataMaskingActivityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            data_masking_activity_id=dict(aliases=["id"], type="str"),
            fusion_environment_id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str",
                choices=["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIME_CREATED", "DISPLAY_NAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="data_masking_activity",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(data_masking_activities=result)


if __name__ == "__main__":
    main()
