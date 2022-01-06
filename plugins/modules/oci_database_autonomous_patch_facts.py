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
module: oci_database_autonomous_patch_facts
short_description: Fetches details about one or multiple AutonomousPatch resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousPatch resources in Oracle Cloud Infrastructure
    - Lists the patches applicable to the requested container database.
    - If I(autonomous_patch_id) is specified, the details of a single AutonomousPatch will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    autonomous_patch_id:
        description:
            - The autonomous patch L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific autonomous_patch.
        type: str
        aliases: ["id"]
    autonomous_container_database_id:
        description:
            - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple autonomous_patches.
        type: str
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple autonomous_patches.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific autonomous_patch
  oci_database_autonomous_patch_facts:
    # required
    autonomous_patch_id: "ocid1.autonomouspatch.oc1..xxxxxxEXAMPLExxxxxx"

- name: List autonomous_patches
  oci_database_autonomous_patch_facts:
    # required
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
autonomous_patches:
    description:
        - List of AutonomousPatch resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The text describing this patch package.
            returned: on success
            type: str
            sample: description_example
        type:
            description:
                - The type of patch. BUNDLE is one example.
            returned: on success
            type: str
            sample: type_example
        lifecycle_details:
            description:
                - A descriptive text associated with the lifecycleState.
                  Typically can contain additional displayable text.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the patch as a result of lastAction.
            returned: on success
            type: str
            sample: AVAILABLE
        time_released:
            description:
                - The date and time that the patch was released.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version:
            description:
                - The version of this patch package.
            returned: on success
            type: str
            sample: version_example
        patch_model:
            description:
                - Database patching model preference. See L(My Oracle Support note 2285040.1,https://support.oracle.com/rs?type=doc&id=2285040.1) for
                  information on the Release Update (RU) and Release Update Revision (RUR) patching models.
            returned: on success
            type: str
            sample: RELEASE_UPDATES
        quarter:
            description:
                - First month of the quarter in which the patch was released.
            returned: on success
            type: str
            sample: quarter_example
        year:
            description:
                - Year in which the patch was released.
            returned: on success
            type: str
            sample: year_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "type": "type_example",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "AVAILABLE",
        "time_released": "2013-10-20T19:20:30+01:00",
        "version": "version_example",
        "patch_model": "RELEASE_UPDATES",
        "quarter": "quarter_example",
        "year": "year_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousPatchFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "autonomous_patch_id",
        ]

    def get_required_params_for_list(self):
        return [
            "autonomous_container_database_id",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_patch,
            autonomous_patch_id=self.module.params.get("autonomous_patch_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_container_database_patches,
            autonomous_container_database_id=self.module.params.get(
                "autonomous_container_database_id"
            ),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AutonomousPatchFactsHelperCustom = get_custom_class("AutonomousPatchFactsHelperCustom")


class ResourceFactsHelper(
    AutonomousPatchFactsHelperCustom, AutonomousPatchFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            autonomous_patch_id=dict(aliases=["id"], type="str"),
            autonomous_container_database_id=dict(type="str"),
            compartment_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_patch",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_patches=result)


if __name__ == "__main__":
    main()
