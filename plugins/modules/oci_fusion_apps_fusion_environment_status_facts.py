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
module: oci_fusion_apps_fusion_environment_status_facts
short_description: Fetches details about a FusionEnvironmentStatus resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a FusionEnvironmentStatus resource in Oracle Cloud Infrastructure
    - Gets the status of a Fusion environment identified by its OCID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    fusion_environment_id:
        description:
            - unique FusionEnvironment identifier
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific fusion_environment_status
  oci_fusion_apps_fusion_environment_status_facts:
    # required
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
fusion_environment_status:
    description:
        - FusionEnvironmentStatus resource
    returned: on success
    type: complex
    contains:
        status:
            description:
                - The data plane status of FusionEnvironment.
            returned: on success
            type: str
            sample: AVAILABLE
    sample: {
        "status": "AVAILABLE"
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


class FusionEnvironmentStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fusion_environment_status,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
        )


FusionEnvironmentStatusFactsHelperCustom = get_custom_class(
    "FusionEnvironmentStatusFactsHelperCustom"
)


class ResourceFactsHelper(
    FusionEnvironmentStatusFactsHelperCustom, FusionEnvironmentStatusFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(fusion_environment_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="fusion_environment_status",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(fusion_environment_status=result)


if __name__ == "__main__":
    main()
