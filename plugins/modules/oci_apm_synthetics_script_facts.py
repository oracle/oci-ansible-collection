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
module: oci_apm_synthetics_script_facts
short_description: Fetches details about one or multiple Script resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Script resources in Oracle Cloud Infrastructure
    - Returns a list of scripts.
    - If I(script_id) is specified, the details of a single Script will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    script_id:
        description:
            - The OCID of the script.
            - Required to get a specific script.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    content_type:
        description:
            - A filter to return only resources that match the content type given.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order of displayName and contentType is ascending.
              Default order of timeCreated and timeUpdated is descending.
              The displayName sort by is case insensitive.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
            - "timeUpdated"
            - "contentType"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List scripts
  oci_apm_synthetics_script_facts:
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific script
  oci_apm_synthetics_script_facts:
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    script_id: "ocid1.script.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
scripts:
    description:
        - List of Script resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the script.
                  scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.
            returned: on success
            type: string
            sample: ocid1.apmsyntheticscript.oc1.phx.aaaaaaaanmvshzvtvvv7uh43f73f37wytshyh46zj2hinnavme6xzbfiw7tq
        display_name:
            description:
                - Unique name that can be edited. The name should not contain any confidential information.
            returned: on success
            type: string
            sample: exampleName
        content_type:
            description:
                - Content type of the script.
            returned: on success
            type: string
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
            type: string
            sample: sample_content
        time_uploaded:
            description:
                - The time when the script was uploaded.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
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
            type: string
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
                            type: string
                            sample: testName
                        param_value:
                            description:
                                - Value of the parameter.
                            returned: on success
                            type: string
                            sample: openPage
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
                    sample: false
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
                    sample: 5
                enabled:
                    description:
                        - Number of enabled monitors using the script.
                    returned: on success
                    type: int
                    sample: 3
                disabled:
                    description:
                        - Number of disabled monitors using the script.
                    returned: on success
                    type: int
                    sample: 3
                invalid:
                    description:
                        - Number of invalid monitors using the script.
                    returned: on success
                    type: int
                    sample: 0
        time_created:
            description:
                - "The time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-12T22:47:12.613Z`"
            returned: on success
            type: string
            sample: 2020-02-12T22:47:12.613Z
        time_updated:
            description:
                - "The time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-13T22:47:12.613Z`"
            returned: on success
            type: string
            sample: 2020-02-13T22:47:12.613Z
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
    sample: [{
        "id": "ocid1.apmsyntheticscript.oc1.phx.aaaaaaaanmvshzvtvvv7uh43f73f37wytshyh46zj2hinnavme6xzbfiw7tq",
        "display_name": "exampleName",
        "content_type": "SIDE",
        "content": "sample_content",
        "time_uploaded": "2013-10-20T19:20:30+01:00",
        "content_size_in_bytes": 56,
        "content_file_name": "content_file_name_example",
        "parameters": [{
            "script_parameter": {
                "param_name": "testName",
                "param_value": "openPage",
                "is_secret": true
            },
            "is_overwritten": false
        }],
        "monitor_status_count_map": {
            "total": 5,
            "enabled": 3,
            "disabled": 3,
            "invalid": 0
        },
        "time_created": "2020-02-12T22:47:12.613Z",
        "time_updated": "2020-02-13T22:47:12.613Z",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apm_synthetics import ApmSyntheticClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ScriptFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "script_id",
        ]

    def get_required_params_for_list(self):
        return [
            "apm_domain_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_script,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            script_id=self.module.params.get("script_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "content_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_scripts,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            **optional_kwargs
        )


ScriptFactsHelperCustom = get_custom_class("ScriptFactsHelperCustom")


class ResourceFactsHelper(ScriptFactsHelperCustom, ScriptFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            script_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            content_type=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["displayName", "timeCreated", "timeUpdated", "contentType"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="script",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(scripts=result)


if __name__ == "__main__":
    main()
