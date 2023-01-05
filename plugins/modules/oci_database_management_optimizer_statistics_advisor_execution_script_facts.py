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
module: oci_database_management_optimizer_statistics_advisor_execution_script_facts
short_description: Fetches details about a OptimizerStatisticsAdvisorExecutionScript resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a OptimizerStatisticsAdvisorExecutionScript resource in Oracle Cloud Infrastructure
    - Gets the Oracle system-generated script for the specified Optimizer Statistics Advisor execution.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    execution_name:
        description:
            - The name of the Optimizer Statistics Advisor execution.
        type: str
        required: true
    task_name:
        description:
            - The name of the optimizer statistics collection execution task.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific optimizer_statistics_advisor_execution_script
  oci_database_management_optimizer_statistics_advisor_execution_script_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    execution_name: execution_name_example
    task_name: task_name_example

"""

RETURN = """
optimizer_statistics_advisor_execution_script:
    description:
        - OptimizerStatisticsAdvisorExecutionScript resource
    returned: on success
    type: complex
    contains:
        script:
            description:
                - The Optimizer Statistics Advisor execution script.
            returned: on success
            type: str
            sample: script_example
    sample: {
        "script": "script_example"
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


class OptimizerStatisticsAdvisorExecutionScriptFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "execution_name",
            "task_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_optimizer_statistics_advisor_execution_script,
            managed_database_id=self.module.params.get("managed_database_id"),
            execution_name=self.module.params.get("execution_name"),
            task_name=self.module.params.get("task_name"),
        )


OptimizerStatisticsAdvisorExecutionScriptFactsHelperCustom = get_custom_class(
    "OptimizerStatisticsAdvisorExecutionScriptFactsHelperCustom"
)


class ResourceFactsHelper(
    OptimizerStatisticsAdvisorExecutionScriptFactsHelperCustom,
    OptimizerStatisticsAdvisorExecutionScriptFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            execution_name=dict(type="str", required=True),
            task_name=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="optimizer_statistics_advisor_execution_script",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(optimizer_statistics_advisor_execution_script=result)


if __name__ == "__main__":
    main()
