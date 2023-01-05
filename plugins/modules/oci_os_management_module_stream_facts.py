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
module: oci_os_management_module_stream_facts
short_description: Fetches details about one or multiple ModuleStream resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ModuleStream resources in Oracle Cloud Infrastructure
    - Retrieve a list of module streams from a software source.
      Filters may be applied to select a subset of module streams
      based on the filter criteria.
    - "The 'moduleName' attribute filters against the name of a module.
      It accepts strings of the format \\"<module>\\".  If this attribute
      is defined, only streams that belong to the specified module are
      included in the result set.  If it is not defined, the request is
      not subject to this filter.  The 'streamName' attribute filters
      against the name of a stream of a module.  If this attribute is
      defined, only the particular module stream that matches both the
      module and stream names is included in the result set.  It is
      not valid to supply 'streamName' without also supplying a
      'moduleName'."
    - When sorting by display name, the result set is sorted first by
      module name, then by stream name.
    - If I(stream_name) is specified, the details of a single ModuleStream will be returned.
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
            - Required to get a specific module_stream.
        type: str
    stream_name:
        description:
            - The name of the stream of the containing module
            - Required to get a specific module_stream.
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
- name: Get a specific module_stream
  oci_os_management_module_stream_facts:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    stream_name: stream_name_example

- name: List module_streams
  oci_os_management_module_stream_facts:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    stream_name: stream_name_example
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
module_streams:
    description:
        - List of ModuleStream resources
    returned: on success
    type: complex
    contains:
        is_default:
            description:
                - Indicates if this stream is the default for its module.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        architecture:
            description:
                - The architecture for which the packages in this module stream were built
                - Returned for get operation
            returned: on success
            type: str
            sample: architecture_example
        description:
            description:
                - A description of the contents of the module stream
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        profiles:
            description:
                - A list of profiles that are part of the stream.  Each element in
                  the list is the name of a profile.  The name is suitable to use as
                  an argument to other OS Management APIs that interact directly with
                  module stream profiles.  However, it is not URL encoded.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        packages:
            description:
                - A list of packages that are contained by the stream.  Each element
                  in the list is the name of a package.  The name is suitable to use
                  as an argument to other OS Management APIs that interact directly
                  with packages.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        module_name:
            description:
                - The name of the module that contains the stream
            returned: on success
            type: str
            sample: module_name_example
        stream_name:
            description:
                - The name of the stream
            returned: on success
            type: str
            sample: stream_name_example
        software_source_id:
            description:
                - The OCID of the software source that provides this module stream.
            returned: on success
            type: str
            sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "is_default": true,
        "architecture": "architecture_example",
        "description": "description_example",
        "profiles": [],
        "packages": [],
        "module_name": "module_name_example",
        "stream_name": "stream_name_example",
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
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ModuleStreamFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "software_source_id",
            "module_name",
            "stream_name",
        ]

    def get_required_params_for_list(self):
        return [
            "software_source_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_module_stream,
            software_source_id=self.module.params.get("software_source_id"),
            module_name=self.module.params.get("module_name"),
            stream_name=self.module.params.get("stream_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "module_name",
            "stream_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_module_streams,
            software_source_id=self.module.params.get("software_source_id"),
            **optional_kwargs
        )


ModuleStreamFactsHelperCustom = get_custom_class("ModuleStreamFactsHelperCustom")


class ResourceFactsHelper(ModuleStreamFactsHelperCustom, ModuleStreamFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_source_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            module_name=dict(type="str"),
            stream_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="module_stream",
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

    module.exit_json(module_streams=result)


if __name__ == "__main__":
    main()
