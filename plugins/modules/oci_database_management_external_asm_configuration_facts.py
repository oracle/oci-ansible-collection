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
module: oci_database_management_external_asm_configuration_facts
short_description: Fetches details about a ExternalAsmConfiguration resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ExternalAsmConfiguration resource in Oracle Cloud Infrastructure
    - Gets configuration details including disk groups for the external ASM specified by `externalAsmId`.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_asm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external ASM.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific external_asm_configuration
  oci_database_management_external_asm_configuration_facts:
    # required
    external_asm_id: "ocid1.externalasm.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
external_asm_configuration:
    description:
        - ExternalAsmConfiguration resource
    returned: on success
    type: complex
    contains:
        init_parameters:
            description:
                - An array of initialization parameters for the external ASM instances.
            returned: on success
            type: complex
            contains:
                asm_instance_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external ASM instance.
                    returned: on success
                    type: str
                    sample: "ocid1.asminstance.oc1..xxxxxxEXAMPLExxxxxx"
                asm_instance_display_name:
                    description:
                        - The user-friendly name for the ASM instance. The name does not have to be unique.
                    returned: on success
                    type: str
                    sample: asm_instance_display_name_example
                disk_discovery_path:
                    description:
                        - An operating system-dependent value used to limit the set of disks considered for discovery.
                    returned: on success
                    type: str
                    sample: disk_discovery_path_example
                auto_mount_disk_groups:
                    description:
                        - The list of disk group names that an ASM instance mounts at startup or when the `ALTER DISKGROUP ALL MOUNT` statement is issued.
                    returned: on success
                    type: list
                    sample: []
                rebalance_power:
                    description:
                        - The maximum power on an ASM instance for disk rebalancing.
                    returned: on success
                    type: int
                    sample: 56
                preferred_read_failure_groups:
                    description:
                        - The list of failure groups that contain preferred read disks.
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "init_parameters": [{
            "asm_instance_id": "ocid1.asminstance.oc1..xxxxxxEXAMPLExxxxxx",
            "asm_instance_display_name": "asm_instance_display_name_example",
            "disk_discovery_path": "disk_discovery_path_example",
            "auto_mount_disk_groups": [],
            "rebalance_power": 56,
            "preferred_read_failure_groups": []
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalAsmConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "external_asm_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_asm_configuration,
            external_asm_id=self.module.params.get("external_asm_id"),
        )


ExternalAsmConfigurationFactsHelperCustom = get_custom_class(
    "ExternalAsmConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    ExternalAsmConfigurationFactsHelperCustom, ExternalAsmConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(external_asm_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_asm_configuration",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_asm_configuration=result)


if __name__ == "__main__":
    main()
