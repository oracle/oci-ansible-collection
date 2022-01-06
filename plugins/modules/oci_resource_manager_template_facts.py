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
module: oci_resource_manager_template_facts
short_description: Fetches details about one or multiple Template resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Template resources in Oracle Cloud Infrastructure
    - Lists templates according to the specified filter.
      The attributes `compartmentId` and `templateCategoryId` are required unless `templateId` is specified.
    - If I(template_id) is specified, the details of a single Template will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    template_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the template.
            - Required to get a specific template.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
    template_category_id:
        description:
            - Unique identifier of the template category.
              Possible values are `0` (Quick Starts), `1` (Service), `2` (Architecture), and `3` (Private).
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
              Use this filter to list a resource by name.
              Requires `sortBy` set to `DISPLAYNAME`.
              Alternatively, when you know the resource OCID, use the related Get operation.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to use when sorting returned resources.
              By default, `TIMECREATED` is ordered descending.
              By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific template
  oci_resource_manager_template_facts:
    # required
    template_id: "ocid1.template.oc1..xxxxxxEXAMPLExxxxxx"

- name: List templates
  oci_resource_manager_template_facts:

    # optional
    template_id: "ocid1.template.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    template_category_id: "ocid1.templatecategory.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
templates:
    description:
        - List of Template resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the template.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing this template.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        category_id:
            description:
                - Unique identifier for the category where the template is located.
                  Possible values are `0` (Quick Starts), `1` (Service), `2` (Architecture), and `3` (Private).
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Human-readable name of the template.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Brief description of the template.
            returned: on success
            type: str
            sample: description_example
        long_description:
            description:
                - Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid
                  entering confidential information.
                - Returned for get operation
            returned: on success
            type: str
            sample: long_description_example
        is_free_tier:
            description:
                - whether the template will work for free tier tenancy.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - "The date and time at which the template was created.
                  Format is defined by RFC3339.
                  Example: `2020-11-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        template_config_source:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                template_config_source_type:
                    description:
                        - The type of configuration source to use for the template configuration.
                    returned: on success
                    type: str
                    sample: ZIP_UPLOAD
        lifecycle_state:
            description:
                - The current lifecycle state of the template.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "category_id": "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "long_description": "long_description_example",
        "is_free_tier": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "template_config_source": {
            "template_config_source_type": "ZIP_UPLOAD"
        },
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.resource_manager import ResourceManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TemplateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "template_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_template, template_id=self.module.params.get("template_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "template_category_id",
            "template_id",
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
            self.client.list_templates, **optional_kwargs
        )


TemplateFactsHelperCustom = get_custom_class("TemplateFactsHelperCustom")


class ResourceFactsHelper(TemplateFactsHelperCustom, TemplateFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            template_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            template_category_id=dict(type="str"),
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
        resource_type="template",
        service_client_class=ResourceManagerClient,
        namespace="resource_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(templates=result)


if __name__ == "__main__":
    main()
