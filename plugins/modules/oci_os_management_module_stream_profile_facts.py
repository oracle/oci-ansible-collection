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
module: oci_os_management_module_stream_profile_facts
short_description: Fetches details about one or multiple ModuleStreamProfile resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ModuleStreamProfile resources in Oracle Cloud Infrastructure
    - Retrieve a list of module stream profiles from a software source.
      Filters may be applied to select a subset of module stream profiles
      based on the filter criteria.
    - "The \\"moduleName\\", \\"streamName\\", and \\"profileName\\" attributes combine
      to form a set of filters on the list of module stream profiles.  If
      a \\"moduleName\\" is provided, only profiles that belong to that module
      are returned.  If both a \\"moduleName\\" and \\"streamName\\" are given,
      only profiles belonging to that module stream are returned.  Finally,
      if all three are given then only the particular profile indicated
      by the triple is returned.  It is not valid to supply a \\"streamName\\"
      without a \\"moduleName\\".  It is also not valid to supply a \\"profileName\\"
      without a \\"streamName\\"."
    - If I(profile_name) is specified, the details of a single ModuleStreamProfile will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    software_source_id:
        description:
            - The OCID of the software source.
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
        type: str
    module_name:
        description:
            - The name of the module
            - Required to get a specific module_stream_profile.
        type: str
    stream_name:
        description:
            - The name of the stream of the containing module
            - Required to get a specific module_stream_profile.
        type: str
    profile_name:
        description:
            - The name of the profile of the containing module stream
            - Required to get a specific module_stream_profile.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific module_stream_profile
  oci_os_management_module_stream_profile_facts:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    stream_name: stream_name_example
    profile_name: profile_name_example

- name: List module_stream_profiles
  oci_os_management_module_stream_profile_facts:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    stream_name: stream_name_example
    profile_name: profile_name_example
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
module_stream_profiles:
    description:
        - List of ModuleStreamProfile resources
    returned: on success
    type: complex
    contains:
        is_default:
            description:
                - Indicates if this profile is the default for its module stream.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        description:
            description:
                - A description of the contents of the module stream profile
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        packages:
            description:
                - A list of packages that constitute the profile.  Each element
                  in the list is the name of a package.  The name is suitable to
                  use as an argument to other OS Management APIs that interact
                  directly with packages.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        module_name:
            description:
                - The name of the module that contains the stream profile
            returned: on success
            type: str
            sample: module_name_example
        stream_name:
            description:
                - The name of the stream that contains the profile
            returned: on success
            type: str
            sample: stream_name_example
        profile_name:
            description:
                - The name of the profile
            returned: on success
            type: str
            sample: profile_name_example
    sample: [{
        "is_default": true,
        "description": "description_example",
        "packages": [],
        "module_name": "module_name_example",
        "stream_name": "stream_name_example",
        "profile_name": "profile_name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ModuleStreamProfileFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "software_source_id",
            "module_name",
            "stream_name",
            "profile_name",
        ]

    def get_required_params_for_list(self):
        return [
            "software_source_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_module_stream_profile,
            software_source_id=self.module.params.get("software_source_id"),
            module_name=self.module.params.get("module_name"),
            stream_name=self.module.params.get("stream_name"),
            profile_name=self.module.params.get("profile_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "module_name",
            "stream_name",
            "profile_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_module_stream_profiles,
            software_source_id=self.module.params.get("software_source_id"),
            **optional_kwargs
        )


ModuleStreamProfileFactsHelperCustom = get_custom_class(
    "ModuleStreamProfileFactsHelperCustom"
)


class ResourceFactsHelper(
    ModuleStreamProfileFactsHelperCustom, ModuleStreamProfileFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_source_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            module_name=dict(type="str"),
            stream_name=dict(type="str"),
            profile_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="module_stream_profile",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(module_stream_profiles=result)


if __name__ == "__main__":
    main()
