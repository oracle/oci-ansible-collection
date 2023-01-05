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
module: oci_oda_skill_parameter_facts
short_description: Fetches details about one or multiple SkillParameter resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SkillParameter resources in Oracle Cloud Infrastructure
    - Returns a page of Skill Parameters that belong to the specified Skill.
    - If the `opc-next-page` header appears in the response, then
      there are more items to retrieve. To get the next page in the subsequent
      GET request, include the header's value as the `page` query parameter.
    - If I(parameter_name) is specified, the details of a single SkillParameter will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    parameter_name:
        description:
            - The name of a Skill Parameter.
            - Required to get a specific skill_parameter.
        type: str
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    skill_id:
        description:
            - Unique Skill identifier.
        type: str
        required: true
    name:
        description:
            - List only Parameters with this name.
        type: str
    lifecycle_state:
        description:
            - List only the resources that are in this lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `name`.
            - The default sort order is ascending.
        type: str
        choices:
            - "name"
            - "displayName"
            - "type"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific skill_parameter
  oci_oda_skill_parameter_facts:
    # required
    parameter_name: parameter_name_example
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    skill_id: "ocid1.skill.oc1..xxxxxxEXAMPLExxxxxx"

- name: List skill_parameters
  oci_oda_skill_parameter_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    skill_id: "ocid1.skill.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: name

"""

RETURN = """
skill_parameters:
    description:
        - List of SkillParameter resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The Parameter name.  This must be unique within the parent resource.
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - The display name for the Parameter.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A description of the Parameter.
            returned: on success
            type: str
            sample: description_example
        type:
            description:
                - The value type.
            returned: on success
            type: str
            sample: STRING
        value:
            description:
                - The current value.  The value will be interpreted based on the `type`.
            returned: on success
            type: str
            sample: value_example
        lifecycle_state:
            description:
                - The Parameter's current state.
            returned: on success
            type: str
            sample: CREATING
    sample: [{
        "name": "name_example",
        "display_name": "display_name_example",
        "description": "description_example",
        "type": "STRING",
        "value": "value_example",
        "lifecycle_state": "CREATING"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.oda import ManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SkillParameterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
            "skill_id",
            "parameter_name",
        ]

    def get_required_params_for_list(self):
        return [
            "oda_instance_id",
            "skill_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_skill_parameter,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            skill_id=self.module.params.get("skill_id"),
            parameter_name=self.module.params.get("parameter_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_skill_parameters,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            skill_id=self.module.params.get("skill_id"),
            **optional_kwargs
        )


SkillParameterFactsHelperCustom = get_custom_class("SkillParameterFactsHelperCustom")


class ResourceFactsHelper(
    SkillParameterFactsHelperCustom, SkillParameterFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            parameter_name=dict(type="str"),
            oda_instance_id=dict(type="str", required=True),
            skill_id=dict(type="str", required=True),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name", "displayName", "type"]),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="skill_parameter",
        service_client_class=ManagementClient,
        namespace="oda",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(skill_parameters=result)


if __name__ == "__main__":
    main()
