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
module: oci_apm_config_metric_group_actions
short_description: Perform actions on a MetricGroup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MetricGroup resource in Oracle Cloud Infrastructure
    - For I(action=retrieve_namespace_metrics), returns all metrics associated with the specified namespace.
    - For I(action=retrieve_namespaces), returns all namespaces available in APM.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - Name of the namespace.
            - Required for I(action=retrieve_namespace_metrics).
        type: str
    apm_domain_id:
        description:
            - The APM Domain ID the request is intended for.
        type: str
        required: true
    action:
        description:
            - The action to perform on the MetricGroup.
        type: str
        required: true
        choices:
            - "retrieve_namespace_metrics"
            - "retrieve_namespaces"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action retrieve_namespace_metrics on metric_group
  oci_apm_config_metric_group_actions:
    # required
    name: name_example
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    action: retrieve_namespace_metrics

- name: Perform action retrieve_namespaces on metric_group
  oci_apm_config_metric_group_actions:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    action: retrieve_namespaces

"""

RETURN = """
namespace_metric_collection:
    description:
        - Details of the MetricGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Name of the metric.
            returned: on success
            type: str
            sample: name_example
        type:
            description:
                - Type of metric.
            returned: on success
            type: str
            sample: COUNTER
        unit:
            description:
                - Unit of the metric.
            returned: on success
            type: str
            sample: unit_example
    sample: {
        "name": "name_example",
        "type": "COUNTER",
        "unit": "unit_example"
    }

namespace_collection:
    description:
        - Details of the MetricGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Name of the namespace.
            returned: on success
            type: str
            sample: name_example
    sample: {
        "name": "name_example"
    }
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
    from oci.apm_config.models import RetrieveNamespaceMetricsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MetricGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        retrieve_namespace_metrics
        retrieve_namespaces
    """

    def retrieve_namespace_metrics(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RetrieveNamespaceMetricsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.retrieve_namespace_metrics,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                retrieve_namespace_metrics_details=action_details,
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

    def retrieve_namespaces(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.retrieve_namespaces,
            call_fn_args=(),
            call_fn_kwargs=dict(apm_domain_id=self.module.params.get("apm_domain_id"),),
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


MetricGroupActionsHelperCustom = get_custom_class("MetricGroupActionsHelperCustom")


class ResourceHelper(MetricGroupActionsHelperCustom, MetricGroupActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            apm_domain_id=dict(type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["retrieve_namespace_metrics", "retrieve_namespaces"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="metric_group",
        service_client_class=ConfigClient,
        namespace="apm_config",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
