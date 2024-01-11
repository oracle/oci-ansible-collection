#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_apm_config_span_filter_actions
short_description: Perform actions on a SpanFilter resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SpanFilter resource in Oracle Cloud Infrastructure
    - For I(action=validate_span_filter_pattern), validates the Span Filter pattern (filterText) for syntactic correctness.
      Returns 204 on success, 422 when validation fails.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM Domain ID the request is intended for.
        type: str
        required: true
    filter_text:
        description:
            - The string that defines the Span Filter expression.
        type: str
        required: true
    action:
        description:
            - The action to perform on the SpanFilter.
        type: str
        required: true
        choices:
            - "validate_span_filter_pattern"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action validate_span_filter_pattern on span_filter
  oci_apm_config_span_filter_actions:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    filter_text: filter_text_example
    action: validate_span_filter_pattern

"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.apm_config import ConfigClient
    from oci.apm_config.models import ValidateSpanFilterPatternDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SpanFilterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        validate_span_filter_pattern
    """

    def validate_span_filter_pattern(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ValidateSpanFilterPatternDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_span_filter_pattern,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                validate_span_filter_pattern_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


SpanFilterActionsHelperCustom = get_custom_class("SpanFilterActionsHelperCustom")


class ResourceHelper(SpanFilterActionsHelperCustom, SpanFilterActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            filter_text=dict(type="str", required=True),
            action=dict(
                type="str", required=True, choices=["validate_span_filter_pattern"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="span_filter",
        service_client_class=ConfigClient,
        namespace="apm_config",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
