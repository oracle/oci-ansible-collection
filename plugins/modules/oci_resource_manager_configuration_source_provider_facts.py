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
module: oci_resource_manager_configuration_source_provider_facts
short_description: Fetches details about one or multiple ConfigurationSourceProvider resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ConfigurationSourceProvider resources in Oracle Cloud Infrastructure
    - "Lists configuration source providers according to the specified filter.
      - For `compartmentId`, lists all configuration source providers in the matching compartment.
      - For `configurationSourceProviderId`, lists the matching configuration source provider."
    - If I(configuration_source_provider_id) is specified, the details of a single ConfigurationSourceProvider will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    configuration_source_provider_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration source provider.
            - Required to get a specific configuration_source_provider.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter to return only resources that exist in the compartment, identified by
              L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
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
    config_source_provider_type:
        description:
            - A filter to return only configuration source providers of the specified type (GitHub or GitLab).
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific configuration_source_provider
  oci_resource_manager_configuration_source_provider_facts:
    # required
    configuration_source_provider_id: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"

- name: List configuration_source_providers
  oci_resource_manager_configuration_source_provider_facts:

    # optional
    configuration_source_provider_id: "ocid1.configurationsourceprovider.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC
    config_source_provider_type: config_source_provider_type_example

"""

RETURN = """
configuration_source_providers:
    description:
        - List of ConfigurationSourceProvider resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration source provider.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where the configuration source
                  provider is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Human-readable display name for the configuration source provider.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the configuration source provider.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "The date and time when the configuration source provider was created.
                  Format is defined by RFC3339.
                  Example: `2020-01-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2020-01-25T21:10:29.600Z"
        lifecycle_state:
            description:
                - The current lifecycle state of the configuration source provider.
                  For more information about configuration source provider lifecycle states in Resource Manager, see
                  L(Key Concepts,https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__CSPStates).
            returned: on success
            type: str
            sample: ACTIVE
        config_source_provider_type:
            description:
                - The type of configuration source provider.
                  The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab.
                  The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.
            returned: on success
            type: str
            sample: GITLAB_ACCESS_TOKEN
        freeform_tags:
            description:
                - "Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        api_endpoint:
            description:
                - "The GitHub service endpoint.
                  Example: `https://github.com/`"
            returned: on success
            type: str
            sample: https://github.com/
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2020-01-25T21:10:29.600Z",
        "lifecycle_state": "ACTIVE",
        "config_source_provider_type": "GITLAB_ACCESS_TOKEN",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "api_endpoint": "https://github.com/"
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


class ConfigurationSourceProviderFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "configuration_source_provider_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_configuration_source_provider,
            configuration_source_provider_id=self.module.params.get(
                "configuration_source_provider_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "configuration_source_provider_id",
            "display_name",
            "sort_by",
            "sort_order",
            "config_source_provider_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_configuration_source_providers, **optional_kwargs
        )


ConfigurationSourceProviderFactsHelperCustom = get_custom_class(
    "ConfigurationSourceProviderFactsHelperCustom"
)


class ResourceFactsHelper(
    ConfigurationSourceProviderFactsHelperCustom,
    ConfigurationSourceProviderFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            configuration_source_provider_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            config_source_provider_type=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="configuration_source_provider",
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

    module.exit_json(configuration_source_providers=result)


if __name__ == "__main__":
    main()
