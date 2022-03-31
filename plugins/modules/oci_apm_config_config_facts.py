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
module: oci_apm_config_config_facts
short_description: Fetches details about one or multiple Config resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Config resources in Oracle Cloud Infrastructure
    - Returns all configuration items, which can optionally be filtered by configuration type.
    - If I(config_id) is specified, the details of a single Config will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    config_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the configuration item.
            - Required to get a specific config.
        type: str
        aliases: ["id"]
    apm_domain_id:
        description:
            - The APM Domain ID the request is intended for.
        type: str
        required: true
    config_type:
        description:
            - A filter to match configuration items of a given type.
              Supported values are SPAN_FILTER, METRIC_GROUP, and APDEX.
        type: str
    display_name:
        description:
            - A filter to return resources that match the given display name.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The displayName sort order
              is case-sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - "The field to sort by. You can provide one \\"sortBy\\" value. The default order for displayName, timeCreated
              and timeUpdated is ascending. The displayName sort by is case-sensitive."
        type: str
        choices:
            - "displayName"
            - "timeCreated"
            - "timeUpdated"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific config
  oci_apm_config_config_facts:
    # required
    config_id: "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx"
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

- name: List configs
  oci_apm_config_config_facts:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    config_type: config_type_example
    display_name: display_name_example
    sort_order: ASC
    sort_by: displayName

"""

RETURN = """
configs:
    description:
        - List of Config resources
    returned: on success
    type: complex
    contains:
        rules:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                filter_text:
                    description:
                        - The string that defines the Span Filter expression.
                    returned: on success
                    type: str
                    sample: filter_text_example
                priority:
                    description:
                        - The priority controls the order in which multiple rules in a rule set are applied. Lower values indicate higher
                          priorities. Rules with higher priority are applied first, and once a match is found, the rest of the rules are
                          ignored. Rules within the same rule set cannot have the same priority.
                    returned: on success
                    type: int
                    sample: 56
                is_enabled:
                    description:
                        - "Specifies whether the Apdex score should be computed for spans matching the rule. This can be used to disable
                          Apdex score for spans that do not need or require it. The default is \\"true\\"."
                    returned: on success
                    type: bool
                    sample: true
                satisfied_response_time:
                    description:
                        - "The maximum response time in milliseconds that is considered \\"satisfactory\\" for the end user."
                    returned: on success
                    type: int
                    sample: 56
                tolerating_response_time:
                    description:
                        - "The maximum response time in milliseconds that is considered \\"tolerable\\" for the end user. A response
                          time beyond this threshold is considered \\"frustrating\\".
                          This value cannot be lower than \\"satisfiedResponseTime\\"."
                    returned: on success
                    type: int
                    sample: 56
                is_apply_to_error_spans:
                    description:
                        - "Specifies whether an Apdex score should be computed for error spans. Setting it to \\"true\\" means that the Apdex
                          score is computed in the usual way. Setting it to \\"false\\" skips the Apdex computation and sets the Apdex
                          score to \\"frustrating\\" regardless of the configured thresholds. The default is \\"false\\"."
                    returned: on success
                    type: bool
                    sample: true
                display_name:
                    description:
                        - A user-friendly name that provides a short description of this rule.
                    returned: on success
                    type: str
                    sample: display_name_example
        filter_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Span Filter. The filterId is mandatory for the
                  creation
                  of MetricGroups. A filterId is generated when a Span Filter is created.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.filter.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - The namespace to which the metrics are published. It must be one of several predefined namespaces.
                - Returned for get operation
            returned: on success
            type: str
            sample: namespace_example
        dimensions:
            description:
                - A list of dimensions for the metric. This variable should not be used.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the dimension.
                    returned: on success
                    type: str
                    sample: name_example
                value_source:
                    description:
                        - The source to populate the dimension. This must not be specified.
                    returned: on success
                    type: str
                    sample: value_source_example
        metrics:
            description:
                - The list of metrics in this group.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the metric. This must be a known metric name.
                    returned: on success
                    type: str
                    sample: name_example
                value_source:
                    description:
                        - This must not be set.
                    returned: on success
                    type: str
                    sample: value_source_example
                unit:
                    description:
                        - The unit of the metric.
                    returned: on success
                    type: str
                    sample: unit_example
                description:
                    description:
                        - A description of the metric.
                    returned: on success
                    type: str
                    sample: description_example
        display_name:
            description:
                - The name by which the rule set is displayed to the end user.
                - Returned for get operation
            returned: on success
            type: str
            sample: display_name_example
        filter_text:
            description:
                - The string that defines the Span Filter expression.
                - Returned for get operation
            returned: on success
            type: str
            sample: filter_text_example
        description:
            description:
                - An optional string that describes what the span filter is intended or used for.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the configuration item. An OCID is generated
                  when the item is created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        config_type:
            description:
                - The type of configuration item.
            returned: on success
            type: str
            sample: SPAN_FILTER
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
    sample: [{
        "rules": [{
            "filter_text": "filter_text_example",
            "priority": 56,
            "is_enabled": true,
            "satisfied_response_time": 56,
            "tolerating_response_time": 56,
            "is_apply_to_error_spans": true,
            "display_name": "display_name_example"
        }],
        "filter_id": "ocid1.filter.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "dimensions": [{
            "name": "name_example",
            "value_source": "value_source_example"
        }],
        "metrics": [{
            "name": "name_example",
            "value_source": "value_source_example",
            "unit": "unit_example",
            "description": "description_example"
        }],
        "display_name": "display_name_example",
        "filter_text": "filter_text_example",
        "description": "description_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "config_type": "SPAN_FILTER",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.apm_config import ConfigClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "apm_domain_id",
            "config_id",
        ]

    def get_required_params_for_list(self):
        return [
            "apm_domain_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_config,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            config_id=self.module.params.get("config_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "config_type",
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
            self.client.list_configs,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            **optional_kwargs
        )


ConfigFactsHelperCustom = get_custom_class("ConfigFactsHelperCustom")


class ResourceFactsHelper(ConfigFactsHelperCustom, ConfigFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            config_id=dict(aliases=["id"], type="str"),
            apm_domain_id=dict(type="str", required=True),
            config_type=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["displayName", "timeCreated", "timeUpdated"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="config",
        service_client_class=ConfigClient,
        namespace="apm_config",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(configs=result)


if __name__ == "__main__":
    main()
