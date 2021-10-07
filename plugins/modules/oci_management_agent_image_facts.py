#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_management_agent_image_facts
short_description: Fetches details about one or multiple ManagementAgentImage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagementAgentImage resources in Oracle Cloud Infrastructure
    - Get supported agent image information
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to which a request will be scoped.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for platformType is descending. Default order for version is descending.
              If no value is specified platformType is default.
        type: str
        choices:
            - "platformType"
            - "version"
    name:
        description:
            - A filter to return only resources that match the entire platform name given.
        type: str
    lifecycle_state:
        description:
            - Filter to return only Management Agents in the particular lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "TERMINATED"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List management_agent_images
  oci_management_agent_image_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
management_agent_images:
    description:
        - List of ManagementAgentImage resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Agent image resource id
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        platform_type:
            description:
                - Agent image platform type
            returned: on success
            type: str
            sample: LINUX
        platform_name:
            description:
                - Agent image platform display name
            returned: on success
            type: str
            sample: platform_name_example
        version:
            description:
                - Agent image version
            returned: on success
            type: str
            sample: version_example
        size:
            description:
                - Agent image size in bytes
            returned: on success
            type: float
            sample: 10
        checksum:
            description:
                - Agent image content SHA256 Hash
            returned: on success
            type: str
            sample: checksum_example
        object_url:
            description:
                - Object storage URL for download
            returned: on success
            type: str
            sample: object_url_example
        lifecycle_state:
            description:
                - The current state of Management Agent Image
            returned: on success
            type: str
            sample: CREATING
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "platform_type": "LINUX",
        "platform_name": "platform_name_example",
        "version": "version_example",
        "size": 10,
        "checksum": "checksum_example",
        "object_url": "object_url_example",
        "lifecycle_state": "CREATING"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.management_agent import ManagementAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementAgentImageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "name",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_management_agent_images,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ManagementAgentImageFactsHelperCustom = get_custom_class(
    "ManagementAgentImageFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagementAgentImageFactsHelperCustom, ManagementAgentImageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["platformType", "version"]),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "TERMINATED",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_agent_image",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_agent_images=result)


if __name__ == "__main__":
    main()
