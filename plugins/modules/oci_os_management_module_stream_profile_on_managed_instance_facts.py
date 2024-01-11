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
module: oci_os_management_module_stream_profile_on_managed_instance_facts
short_description: Fetches details about one or multiple ModuleStreamProfileOnManagedInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ModuleStreamProfileOnManagedInstance resources in Oracle Cloud Infrastructure
    - Retrieve a list of module stream profiles, along with a summary of their
      of their status, from a managed instance.  Filters may be applied to
      select a subset of profiles based on the filter criteria.
    - "The \\"moduleName\\", \\"streamName\\", and \\"profileName\\" attributes combine
      to form a set of filters on the list of module stream profiles.  If
      a \\"modulName\\" is provided, only profiles that belong to that module
      are returned.  If both a \\"moduleName\\" and \\"streamName\\" are given,
      only profiles belonging to that module stream are returned.  Finally,
      if all three are given then only the particular profile indicated
      by the triple is returned.  It is not valid to supply a \\"streamName\\"
      without a \\"moduleName\\".  It is also not valid to supply a \\"profileName\\"
      without a \\"streamName\\"."
    - "The \\"status\\" attribute filters against the state of a module stream
      profile.  Valid values are \\"INSTALLED\\" and \\"AVAILABLE\\".  If the
      attribute is set to \\"INSTALLED\\", only module stream profiles that
      are installed are included in the result set.  If the attribute is
      set to \\"AVAILABLE\\", only module stream profiles that are not
      installed are included in the result set.  If the attribute is not
      defined, the request is not subject to this filter."
    - When sorting by display name, the result set is sorted first by
      module name, then by stream name, and finally by profile name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - OCID for the managed instance
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
        type: str
    module_name:
        description:
            - The name of a module.  This parameter is required if a
              streamName is specified.
        type: str
    stream_name:
        description:
            - The name of the stream of the containing module.  This parameter
              is required if a profileName is specified.
        type: str
    profile_name:
        description:
            - The name of the profile of the containing module stream
        type: str
    profile_status:
        description:
            - The status of the profile.
            - "A profile with the \\"INSTALLED\\" status indicates that the
              profile has been installed."
            - "A profile with the \\"AVAILABLE\\" status indicates that the
              profile is not installed, but can be."
        type: str
        choices:
            - "INSTALLED"
            - "AVAILABLE"
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
- name: List module_stream_profile_on_managed_instances
  oci_os_management_module_stream_profile_on_managed_instance_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    module_name: module_name_example
    stream_name: stream_name_example
    profile_name: profile_name_example
    profile_status: INSTALLED
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
module_stream_profile_on_managed_instances:
    description:
        - List of ModuleStreamProfileOnManagedInstance resources
    returned: on success
    type: complex
    contains:
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
        status:
            description:
                - The status of the profile.
                - "A profile with the \\"INSTALLED\\" status indicates that the profile has been
                  installed."
                - "A profile with the \\"AVAILABLE\\" status indicates that the profile is
                  not installed, but can be."
            returned: on success
            type: str
            sample: INSTALLED
        time_modified:
            description:
                - The date and time of the last status change for this profile, as
                  described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339),
                  section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "module_name": "module_name_example",
        "stream_name": "stream_name_example",
        "profile_name": "profile_name_example",
        "status": "INSTALLED",
        "time_modified": "2013-10-20T19:20:30+01:00"
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


class ModuleStreamProfileOnManagedInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "module_name",
            "stream_name",
            "profile_name",
            "profile_status",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_module_stream_profiles_on_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


ModuleStreamProfileOnManagedInstanceFactsHelperCustom = get_custom_class(
    "ModuleStreamProfileOnManagedInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    ModuleStreamProfileOnManagedInstanceFactsHelperCustom,
    ModuleStreamProfileOnManagedInstanceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            module_name=dict(type="str"),
            stream_name=dict(type="str"),
            profile_name=dict(type="str"),
            profile_status=dict(type="str", choices=["INSTALLED", "AVAILABLE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="module_stream_profile_on_managed_instance",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(module_stream_profile_on_managed_instances=result)


if __name__ == "__main__":
    main()
