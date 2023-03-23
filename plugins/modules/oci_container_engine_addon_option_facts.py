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
module: oci_container_engine_addon_option_facts
short_description: Fetches details about one or multiple AddonOption resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AddonOption resources in Oracle Cloud Infrastructure
    - Get list of supported addons for a specific kubernetes version.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    kubernetes_version:
        description:
            - The kubernetes version to fetch the addons.
        type: str
        required: true
    addon_name:
        description:
            - The name of the addon.
        type: str
    sort_order:
        description:
            - The optional order in which to sort the results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The optional field to sort the results by.
        type: str
        choices:
            - "NAME"
            - "TIME_CREATED"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List addon_options
  oci_container_engine_addon_option_facts:
    # required
    kubernetes_version: kubernetes_version_example

    # optional
    addon_name: addon_name_example
    sort_order: ASC
    sort_by: NAME

"""

RETURN = """
addon_options:
    description:
        - List of AddonOption resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Name of the addon and it would be unique.
            returned: on success
            type: str
            sample: name_example
        addon_schema_version:
            description:
                - Addon definition schema version to validate addon.
            returned: on success
            type: str
            sample: addon_schema_version_example
        addon_group:
            description:
                - Addon group info, a namespace concept that groups addons with similar functionalities.
            returned: on success
            type: str
            sample: addon_group_example
        lifecycle_state:
            description:
                - The life cycle state of the addon.
            returned: on success
            type: str
            sample: ACTIVE
        description:
            description:
                - Description on the addon.
            returned: on success
            type: str
            sample: description_example
        is_essential:
            description:
                - Is it an essential addon for cluster operation or not.
            returned: on success
            type: bool
            sample: true
        versions:
            description:
                - The resources this work request affects.
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - Current state of the addon, only active will be visible to customer, visibility of versions in other status will be filtered  based on
                          limits property.
                    returned: on success
                    type: str
                    sample: ACTIVE
                version_number:
                    description:
                        - Version number, need be comparable within an addon.
                    returned: on success
                    type: str
                    sample: version_number_example
                description:
                    description:
                        - Information about the addon version.
                    returned: on success
                    type: str
                    sample: description_example
                kubernetes_version_filters:
                    description:
                        - The range of kubernetes versions an addon can be configured.
                    returned: on success
                    type: complex
                    contains:
                        minimal_version:
                            description:
                                - The earliest kubernetes version.
                            returned: on success
                            type: str
                            sample: minimal_version_example
                        maximum_version:
                            description:
                                - The latest kubernetes version.
                            returned: on success
                            type: str
                            sample: maximum_version_example
                        exact_kubernetes_versions:
                            description:
                                - The exact version of kubernetes that are compatible.
                            returned: on success
                            type: list
                            sample: []
                configurations:
                    description:
                        - Addon version configuration details.
                    returned: on success
                    type: complex
                    contains:
                        is_required:
                            description:
                                - If the the configuration is required or not.
                            returned: on success
                            type: bool
                            sample: true
                        key:
                            description:
                                - Addon configuration key
                            returned: on success
                            type: str
                            sample: key_example
                        value:
                            description:
                                - Addon configuration value
                            returned: on success
                            type: str
                            sample: value_example
                        display_name:
                            description:
                                - Display name of addon version.
                            returned: on success
                            type: str
                            sample: display_name_example
                        description:
                            description:
                                - Information about the addon version configuration.
                            returned: on success
                            type: str
                            sample: description_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time the work request was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "name": "name_example",
        "addon_schema_version": "addon_schema_version_example",
        "addon_group": "addon_group_example",
        "lifecycle_state": "ACTIVE",
        "description": "description_example",
        "is_essential": true,
        "versions": [{
            "status": "ACTIVE",
            "version_number": "version_number_example",
            "description": "description_example",
            "kubernetes_version_filters": {
                "minimal_version": "minimal_version_example",
                "maximum_version": "maximum_version_example",
                "exact_kubernetes_versions": []
            },
            "configurations": [{
                "is_required": true,
                "key": "key_example",
                "value": "value_example",
                "display_name": "display_name_example",
                "description": "description_example"
            }]
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddonOptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "kubernetes_version",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "addon_name",
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_addon_options,
            kubernetes_version=self.module.params.get("kubernetes_version"),
            **optional_kwargs
        )


AddonOptionFactsHelperCustom = get_custom_class("AddonOptionFactsHelperCustom")


class ResourceFactsHelper(AddonOptionFactsHelperCustom, AddonOptionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            kubernetes_version=dict(type="str", required=True),
            addon_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAME", "TIME_CREATED"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="addon_option",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(addon_options=result)


if __name__ == "__main__":
    main()
