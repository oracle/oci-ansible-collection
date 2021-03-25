#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_compute_image_capability_schema_facts
short_description: Fetches details about one or multiple ComputeImageCapabilitySchema resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ComputeImageCapabilitySchema resources in Oracle Cloud Infrastructure
    - Lists Compute Image Capability Schema in the specified compartment. You can also query by a specific imageId.
    - If I(compute_image_capability_schema_id) is specified, the details of a single ComputeImageCapabilitySchema will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compute_image_capability_schema_id:
        description:
            - The id of the compute image capability schema or the image ocid
            - Required to get a specific compute_image_capability_schema.
        type: str
        aliases: ["id"]
    is_merge_enabled:
        description:
            - Merge the image capability schema with the global image capability schema
        type: bool
    compartment_id:
        description:
            - A filter to return only resources that match the given compartment OCID exactly.
        type: str
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of an image.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
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
- name: List compute_image_capability_schemas
  oci_compute_image_capability_schema_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific compute_image_capability_schema
  oci_compute_image_capability_schema_facts:
    compute_image_capability_schema_id: "ocid1.computeimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
compute_image_capability_schemas:
    description:
        - List of ComputeImageCapabilitySchema resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The id of the compute global image capability schema version
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the resource.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        compute_global_image_capability_schema_id:
            description:
                - The ocid of the compute global image capability schema
            returned: on success
            type: string
            sample: "ocid1.computeglobalimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx"
        compute_global_image_capability_schema_version_name:
            description:
                - The name of the compute global image capability schema version
            returned: on success
            type: string
            sample: compute_global_image_capability_schema_version_name_example
        image_id:
            description:
                - The OCID of the image associated with this compute image capability schema
            returned: on success
            type: string
            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name for the compute global image capability schema
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        schema_data:
            description:
                - The map of each capability name to its ImageCapabilityDescriptor.
            returned: on success
            type: complex
            contains:
                descriptor_type:
                    description:
                        - The image capability schema descriptor type for the capability
                    returned: on success
                    type: string
                    sample: descriptor_type_example
                source:
                    description:
                        - ""
                    returned: on success
                    type: string
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
                    type: string
                    sample: default_value_example
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
                boolean_default_value:
                    description:
                        - the default value
                    returned: on success
                    type: bool
                    sample: true
        time_created:
            description:
                - The date and time the compute image capability schema was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_global_image_capability_schema_id": "ocid1.computeglobalimagecapabilityschema.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_global_image_capability_schema_version_name": "compute_global_image_capability_schema_version_name_example",
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "schema_data": {
            "descriptor_type": "descriptor_type_example",
            "source": "GLOBAL",
            "enum_string_values": [],
            "enum_string_default_value": "default_value_example",
            "enum_integer_values": [],
            "enum_integer_default_value": 56,
            "boolean_default_value": true
        },
        "time_created": "2016-08-25T21:10:29.600Z"
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


class ComputeImageCapabilitySchemaFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "compute_image_capability_schema_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        optional_get_method_params = [
            "is_merge_enabled",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_compute_image_capability_schema,
            compute_image_capability_schema_id=self.module.params.get(
                "compute_image_capability_schema_id"
            ),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "image_id",
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
            self.client.list_compute_image_capability_schemas, **optional_kwargs
        )


ComputeImageCapabilitySchemaFactsHelperCustom = get_custom_class(
    "ComputeImageCapabilitySchemaFactsHelperCustom"
)


class ResourceFactsHelper(
    ComputeImageCapabilitySchemaFactsHelperCustom,
    ComputeImageCapabilitySchemaFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compute_image_capability_schema_id=dict(aliases=["id"], type="str"),
            is_merge_enabled=dict(type="bool"),
            compartment_id=dict(type="str"),
            image_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="compute_image_capability_schema",
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

    module.exit_json(compute_image_capability_schemas=result)


if __name__ == "__main__":
    main()
