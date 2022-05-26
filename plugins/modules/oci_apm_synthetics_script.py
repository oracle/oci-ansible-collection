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
module: oci_apm_synthetics_script
short_description: Manage a Script resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Script resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new script.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Unique name that can be edited. The name should not contain any confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    content_type:
        description:
            - Content type of script.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "SIDE"
            - "JS"
    content:
        description:
            - "The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters.
              The format to set dynamic parameters is: `<ORAP><ON>param name</ON><OV>param value</OV><OS>isParamValueSecret(true/false)</OS></ORAP>`.
              Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false.
              Examples:
              With mandatory param name : `<ORAP><ON>param name</ON></ORAP>`
              With parameter name and value : `<ORAP><ON>param name</ON><OV>param value</OV></ORAP>`
              Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in Side
              script format. If the content type is JS, then the content should be in JavaScript format."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    content_file_name:
        description:
            - File name of uploaded script content.
            - This parameter is updatable.
        type: str
    parameters:
        description:
            - "List of script parameters. Example: `[{\\"paramName\\": \\"userid\\", \\"paramValue\\":\\"testuser\\", \\"isSecret\\": false}]`"
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            param_name:
                description:
                    - Name of the parameter.
                type: str
                required: true
            param_value:
                description:
                    - Value of the parameter.
                type: str
            is_secret:
                description:
                    - If the parameter value is secret and should be kept confidential, then set isSecret to true.
                type: bool
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    script_id:
        description:
            - The OCID of the script.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Script.
            - Use I(state=present) to create or update a Script.
            - Use I(state=absent) to delete a Script.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create script
  oci_apm_synthetics_script:
    # required
    display_name: display_name_example
    content_type: SIDE
    content: content_example
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    content_file_name: content_file_name_example
    parameters:
    - # required
      param_name: param_name_example

      # optional
      param_value: param_value_example
      is_secret: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update script
  oci_apm_synthetics_script:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    script_id: "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    content_type: SIDE
    content: content_example
    content_file_name: content_file_name_example
    parameters:
    - # required
      param_name: param_name_example

      # optional
      param_value: param_value_example
      is_secret: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update script using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apm_synthetics_script:
    # required
    display_name: display_name_example
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    content_type: SIDE
    content: content_example
    content_file_name: content_file_name_example
    parameters:
    - # required
      param_name: param_name_example

      # optional
      param_value: param_value_example
      is_secret: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete script
  oci_apm_synthetics_script:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    script_id: "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete script using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apm_synthetics_script:
    # required
    display_name: display_name_example
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
script:
    description:
        - Details of the Script resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the script.
                  scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Unique name that can be edited. The name should not contain any confidential information.
            returned: on success
            type: str
            sample: display_name_example
        content_type:
            description:
                - Content type of the script.
            returned: on success
            type: str
            sample: SIDE
        content:
            description:
                - "The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters.
                  The format to set dynamic parameters is: `<ORAP><ON>param name</ON><OV>param value</OV><OS>isParamValueSecret(true/false)</OS></ORAP>`.
                  Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false.
                  Examples:
                  With mandatory param name : `<ORAP><ON>param name</ON></ORAP>`
                  With parameter name and value : `<ORAP><ON>param name</ON><OV>param value</OV></ORAP>`
                  Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in
                  Side script format. If the content type is JS, then the content should be in JavaScript format."
            returned: on success
            type: str
            sample: sample_content
        time_uploaded:
            description:
                - The time the script was uploaded.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        content_size_in_bytes:
            description:
                - Size of the script content.
            returned: on success
            type: int
            sample: 56
        content_file_name:
            description:
                - File name of the uploaded script content.
            returned: on success
            type: str
            sample: content_file_name_example
        parameters:
            description:
                - "List of script parameters. Example: `[{\\"scriptParameter\\": {\\"paramName\\": \\"userid\\", \\"paramValue\\":\\"testuser\\",
                  \\"isSecret\\": false}, \\"isOverwritten\\": false}]`"
            returned: on success
            type: complex
            contains:
                script_parameter:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        param_name:
                            description:
                                - Name of the parameter.
                            returned: on success
                            type: str
                            sample: param_name_example
                        param_value:
                            description:
                                - Value of the parameter.
                            returned: on success
                            type: str
                            sample: param_value_example
                        is_secret:
                            description:
                                - If the parameter value is secret and should be kept confidential, then set isSecret to true.
                            returned: on success
                            type: bool
                            sample: true
                is_overwritten:
                    description:
                        - If parameter value is default or overwritten.
                    returned: on success
                    type: bool
                    sample: true
        monitor_status_count_map:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                total:
                    description:
                        - Total number of monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                enabled:
                    description:
                        - Number of enabled monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                disabled:
                    description:
                        - Number of disabled monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                invalid:
                    description:
                        - Number of invalid monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
        time_created:
            description:
                - "The time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-13T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "content_type": "SIDE",
        "content": "sample_content",
        "time_uploaded": "2013-10-20T19:20:30+01:00",
        "content_size_in_bytes": 56,
        "content_file_name": "content_file_name_example",
        "parameters": [{
            "script_parameter": {
                "param_name": "param_name_example",
                "param_value": "param_value_example",
                "is_secret": true
            },
            "is_overwritten": true
        }],
        "monitor_status_count_map": {
            "total": 56,
            "enabled": 56,
            "disabled": 56,
            "invalid": 56
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.apm_synthetics import ApmSyntheticClient
    from oci.apm_synthetics.models import CreateScriptDetails
    from oci.apm_synthetics.models import UpdateScriptDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScriptHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ScriptHelperGen, self).get_possible_entity_types() + [
            "script",
            "scripts",
            "apmSyntheticsscript",
            "apmSyntheticsscripts",
            "scriptresource",
            "scriptsresource",
            "apmsynthetics",
        ]

    def get_module_resource_id_param(self):
        return "script_id"

    def get_module_resource_id(self):
        return self.module.params.get("script_id")

    def get_get_fn(self):
        return self.client.get_script

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_script,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            script_id=self.module.params.get("script_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "apm_domain_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "content_type"]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_scripts, **kwargs)

    def get_create_model_class(self):
        return CreateScriptDetails

    def get_exclude_attributes(self):
        return [
            "parameters.param_value",
            "parameters.is_secret",
            "parameters.param_name",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_script,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                create_script_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateScriptDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_script,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                script_id=self.module.params.get("script_id"),
                update_script_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_script,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                script_id=self.module.params.get("script_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ScriptHelperCustom = get_custom_class("ScriptHelperCustom")


class ResourceHelper(ScriptHelperCustom, ScriptHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            content_type=dict(type="str", choices=["SIDE", "JS"]),
            content=dict(type="str"),
            content_file_name=dict(type="str"),
            parameters=dict(
                type="list",
                elements="dict",
                options=dict(
                    param_name=dict(type="str", required=True),
                    param_value=dict(type="str"),
                    is_secret=dict(type="bool", no_log=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            apm_domain_id=dict(type="str", required=True),
            script_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="script",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
