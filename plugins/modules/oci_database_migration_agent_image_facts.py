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
module: oci_database_migration_agent_image_facts
short_description: Fetches details about one or multiple AgentImage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AgentImage resources in Oracle Cloud Infrastructure
    - Get details of the ODMS Agent Images available to install on-premises.
version_added: "2.9"
author: Oracle (@oracle)
options:
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List agent_images
  oci_database_migration_agent_image_facts:

"""

RETURN = """
agent_images:
    description:
        - List of AgentImage resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - ODMS Agent Image version.
            returned: on success
            type: string
            sample: version_example
        download_url:
            description:
                - URL to download Agent Image of the ODMS Agent.
            returned: on success
            type: string
            sample: download_url_example
    sample: [{
        "version": "version_example",
        "download_url": "download_url_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_migration import DatabaseMigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AgentImageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_agent_images, **optional_kwargs
        )


AgentImageFactsHelperCustom = get_custom_class("AgentImageFactsHelperCustom")


class ResourceFactsHelper(AgentImageFactsHelperCustom, AgentImageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(sort_order=dict(type="str", choices=["ASC", "DESC"]),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="agent_image",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(agent_images=result)


if __name__ == "__main__":
    main()
