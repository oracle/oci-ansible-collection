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
module: oci_os_management_hub_search_software_source_module_streams_facts
short_description: Fetches details about one or multiple SearchSoftwareSourceModuleStreams resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SearchSoftwareSourceModuleStreams resources in Oracle Cloud Infrastructure
    - Returns a list of module streams from the specified software sources. Filter the list against a variety of
      criteria including the module name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    software_source_ids:
        description:
            - List of software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
        required: true
    sort_order:
        description:
            - The sort order.
        type: str
        choices:
            - "ASC"
            - "DESC"
    module_name:
        description:
            - The name of a module.
        type: str
    sort_by:
        description:
            - The field to sort by.
        type: str
        choices:
            - "MODULENAME"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List search_software_source_module_streams
  oci_os_management_hub_search_software_source_module_streams_facts:
    # required
    software_source_ids: [ "software_source_ids_example" ]

    # optional
    sort_order: ASC
    module_name: module_name_example
    sort_by: MODULENAME

"""

RETURN = """
search_software_source_module_streams:
    description:
        - List of SearchSoftwareSourceModuleStreams resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the stream.
            returned: on success
            type: str
            sample: name_example
        module_name:
            description:
                - The name of the module that contains the stream.
            returned: on success
            type: str
            sample: module_name_example
        profiles:
            description:
                - List of profiles in the stream.
            returned: on success
            type: list
            sample: []
        is_latest:
            description:
                - Indicates whether this module stream is the latest.
            returned: on success
            type: bool
            sample: true
        software_source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that contains the the module
                  stream.
            returned: on success
            type: str
            sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "name": "name_example",
        "module_name": "module_name_example",
        "profiles": [],
        "is_latest": true,
        "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import SoftwareSourceClient
    from oci.os_management_hub.models import SearchSoftwareSourceModuleStreamsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubSearchSoftwareSourceModuleStreamsFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "software_source_ids",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.search_software_source_module_streams,
            search_software_source_module_streams_details=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, SearchSoftwareSourceModuleStreamsDetails
            ),
            **optional_kwargs
        )


OsManagementHubSearchSoftwareSourceModuleStreamsFactsHelperCustom = get_custom_class(
    "OsManagementHubSearchSoftwareSourceModuleStreamsFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubSearchSoftwareSourceModuleStreamsFactsHelperCustom,
    OsManagementHubSearchSoftwareSourceModuleStreamsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_source_ids=dict(type="list", elements="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            module_name=dict(type="str"),
            sort_by=dict(type="str", choices=["MODULENAME"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="search_software_source_module_streams",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(search_software_source_module_streams=result)


if __name__ == "__main__":
    main()
