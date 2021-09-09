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
module: oci_management_agent_install_key_facts
short_description: Fetches details about one or multiple ManagementAgentInstallKey resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagementAgentInstallKey resources in Oracle Cloud Infrastructure
    - Returns a list of Management Agent installed Keys.
    - If I(management_agent_install_key_id) is specified, the details of a single ManagementAgentInstallKey will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    management_agent_install_key_id:
        description:
            - Unique Management Agent Install Key identifier
            - Required to get a specific management_agent_install_key.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment to which a request will be scoped.
            - Required to list multiple management_agent_install_keys.
        type: str
    compartment_id_in_subtree:
        description:
            - if set to true then it fetches install key for all compartments where user has access to else only on the compartment specified.
        type: bool
    access_level:
        description:
            - "Value of this is always \\"ACCESSIBLE\\" and any other value is not supported."
        type: str
    lifecycle_state:
        description:
            - Filter to return only Management Agents in the particular lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "TERMINATED"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - The display name for which the Key needs to be listed.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List management_agent_install_keys
  oci_management_agent_install_key_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific management_agent_install_key
  oci_management_agent_install_key_facts:
    management_agent_install_key_id: "ocid1.managementagentinstallkey.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
management_agent_install_keys:
    description:
        - List of ManagementAgentInstallKey resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Agent install Key identifier
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Management Agent Install Key Name
            returned: on success
            type: string
            sample: display_name_example
        key:
            description:
                - Management Agent Install Key
            returned: on success
            type: string
            sample: key_example
        created_by_principal_id:
            description:
                - Principal id of user who created the Agent Install key
            returned: on success
            type: string
            sample: "ocid1.createdbyprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        allowed_key_install_count:
            description:
                - Total number of install for this keys
            returned: on success
            type: int
            sample: 56
        current_key_install_count:
            description:
                - Total number of install for this keys
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - Status of Key
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_expires:
            description:
                - date after which key would expire after creation
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_created:
            description:
                - The time when Management Agent install Key was created. An RFC3339 formatted date time string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time when Management Agent install Key was updated. An RFC3339 formatted date time string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "key": "key_example",
        "created_by_principal_id": "ocid1.createdbyprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "allowed_key_install_count": 56,
        "current_key_install_count": 56,
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.management_agent import ManagementAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementAgentInstallKeyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "management_agent_install_key_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_agent_install_key,
            management_agent_install_key_id=self.module.params.get(
                "management_agent_install_key_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "access_level",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_management_agent_install_keys,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ManagementAgentInstallKeyFactsHelperCustom = get_custom_class(
    "ManagementAgentInstallKeyFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagementAgentInstallKeyFactsHelperCustom, ManagementAgentInstallKeyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            management_agent_install_key_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "TERMINATED",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_agent_install_key",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_agent_install_keys=result)


if __name__ == "__main__":
    main()
