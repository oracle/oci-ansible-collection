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
module: oci_compute_global_image_capability_schema_version_facts
short_description: Fetches details about one or multiple ComputeGlobalImageCapabilitySchemaVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ComputeGlobalImageCapabilitySchemaVersion resources in Oracle Cloud Infrastructure
    - Lists Compute Global Image Capability Schema versions in the specified compartment.
    - If I(compute_global_image_capability_schema_version_name) is specified, the details of a single ComputeGlobalImageCapabilitySchemaVersion will be
      returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compute_global_image_capability_schema_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compute global image capability schema
        type: str
        required: true
    compute_global_image_capability_schema_version_name:
        description:
            - The name of the compute global image capability schema version
            - Required to get a specific compute_global_image_capability_schema_version.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific compute_global_image_capability_schema_version
  oci_compute_global_image_capability_schema_version_facts:
    # required
    compute_global_image_capability_schema_id: "ocid1.computeglobalimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"
    compute_global_image_capability_schema_version_name: compute_global_image_capability_schema_version_name_example

- name: List compute_global_image_capability_schema_versions
  oci_compute_global_image_capability_schema_version_facts:
    # required
    compute_global_image_capability_schema_id: "ocid1.computeglobalimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
compute_global_image_capability_schema_versions:
    description:
        - List of ComputeGlobalImageCapabilitySchemaVersion resources
    returned: on success
    type: complex
    contains:
        schema_data:
            description:
                - The map of each capability name to its ImageCapabilityDescriptor.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                boolean_default_value:
                    description:
                        - the default value
                    returned: on success
                    type: bool
                    sample: true
                enum_integer_values:
                    description:
                        - the list of values for the enum
                    returned: on success
                    type: list
                    sample: []
                enum_integer_default_value:
                    description:
                        - the default value
                    returned: on success
                    type: int
                    sample: 56
                descriptor_type:
                    description:
                        - The image capability schema descriptor type for the capability
                    returned: on success
                    type: str
                    sample: boolean
                source:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: GLOBAL
                enum_string_values:
                    description:
                        - the list of values for the enum
                    returned: on success
                    type: list
                    sample: []
                enum_string_default_value:
                    description:
                        - the default value
                    returned: on success
                    type: str
                    sample: default_value_example
        name:
            description:
                - The name of the compute global image capability schema version
            returned: on success
            type: str
            sample: name_example
        compute_global_image_capability_schema_id:
            description:
                - The ocid of the compute global image capability schema
            returned: on success
            type: str
            sample: "ocid1.computeglobalimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time the compute global image capability schema version was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "schema_data": {
            "boolean_default_value": true,
            "enum_integer_values": [],
            "enum_integer_default_value": 56,
            "descriptor_type": "boolean",
            "source": "GLOBAL",
            "enum_string_values": [],
            "enum_string_default_value": "default_value_example"
        },
        "name": "name_example",
        "compute_global_image_capability_schema_id": "ocid1.computeglobalimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputeGlobalImageCapabilitySchemaVersionFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "compute_global_image_capability_schema_id",
            "compute_global_image_capability_schema_version_name",
        ]

    def get_required_params_for_list(self):
        return [
            "compute_global_image_capability_schema_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_compute_global_image_capability_schema_version,
            compute_global_image_capability_schema_id=self.module.params.get(
                "compute_global_image_capability_schema_id"
            ),
            compute_global_image_capability_schema_version_name=self.module.params.get(
                "compute_global_image_capability_schema_version_name"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_compute_global_image_capability_schema_versions,
            compute_global_image_capability_schema_id=self.module.params.get(
                "compute_global_image_capability_schema_id"
            ),
            **optional_kwargs
        )


ComputeGlobalImageCapabilitySchemaVersionFactsHelperCustom = get_custom_class(
    "ComputeGlobalImageCapabilitySchemaVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    ComputeGlobalImageCapabilitySchemaVersionFactsHelperCustom,
    ComputeGlobalImageCapabilitySchemaVersionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compute_global_image_capability_schema_id=dict(type="str", required=True),
            compute_global_image_capability_schema_version_name=dict(type="str"),
            display_name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="compute_global_image_capability_schema_version",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(compute_global_image_capability_schema_versions=result)


if __name__ == "__main__":
    main()
