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
module: oci_fusion_apps_fusion_environment_family_limits_and_usage_facts
short_description: Fetches details about a FusionEnvironmentFamilyLimitsAndUsage resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a FusionEnvironmentFamilyLimitsAndUsage resource in Oracle Cloud Infrastructure
    - Gets the number of environments (usage) of each type in the fusion environment family, as well as the limit that's allowed to be created based on the
      group's associated subscriptions.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    fusion_environment_family_id:
        description:
            - The unique identifier (OCID) of the FusionEnvironmentFamily.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific fusion_environment_family_limits_and_usage
  oci_fusion_apps_fusion_environment_family_limits_and_usage_facts:
    # required
    fusion_environment_family_id: "ocid1.fusionenvironmentfamily.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
fusion_environment_family_limits_and_usage:
    description:
        - FusionEnvironmentFamilyLimitsAndUsage resource
    returned: on success
    type: complex
    contains:
        production_limit_and_usage:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                limit:
                    description:
                        - The limit of current environment.
                    returned: on success
                    type: int
                    sample: 56
                usage:
                    description:
                        - The usage of current environment.
                    returned: on success
                    type: int
                    sample: 56
        test_limit_and_usage:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                limit:
                    description:
                        - The limit of current environment.
                    returned: on success
                    type: int
                    sample: 56
                usage:
                    description:
                        - The usage of current environment.
                    returned: on success
                    type: int
                    sample: 56
        development_limit_and_usage:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                limit:
                    description:
                        - The limit of current environment.
                    returned: on success
                    type: int
                    sample: 56
                usage:
                    description:
                        - The usage of current environment.
                    returned: on success
                    type: int
                    sample: 56
    sample: {
        "production_limit_and_usage": {
            "limit": 56,
            "usage": 56
        },
        "test_limit_and_usage": {
            "limit": 56,
            "usage": 56
        },
        "development_limit_and_usage": {
            "limit": 56,
            "usage": 56
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.fusion_apps import FusionApplicationsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FusionEnvironmentFamilyLimitsAndUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_family_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fusion_environment_family_limits_and_usage,
            fusion_environment_family_id=self.module.params.get(
                "fusion_environment_family_id"
            ),
        )


FusionEnvironmentFamilyLimitsAndUsageFactsHelperCustom = get_custom_class(
    "FusionEnvironmentFamilyLimitsAndUsageFactsHelperCustom"
)


class ResourceFactsHelper(
    FusionEnvironmentFamilyLimitsAndUsageFactsHelperCustom,
    FusionEnvironmentFamilyLimitsAndUsageFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            fusion_environment_family_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="fusion_environment_family_limits_and_usage",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(fusion_environment_family_limits_and_usage=result)


if __name__ == "__main__":
    main()
