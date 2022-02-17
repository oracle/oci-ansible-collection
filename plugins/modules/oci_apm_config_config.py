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
module: oci_apm_config_config
short_description: Manage a Config resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Config resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Configuration item.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM Domain Id the request is intended for.
        type: str
        required: true
    config_type:
        description:
            - The type of configuration item
            - Required for create using I(state=present), update using I(state=present) with config_id present.
        type: str
        choices:
            - "SPAN_FILTER"
            - "METRIC_GROUP"
            - "APDEX"
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
    display_name:
        description:
            - The name by which this filter can be displayed in the UI.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Applicable when config_type is one of ['APDEX', 'METRIC_GROUP', 'SPAN_FILTER']
        type: str
        aliases: ["name"]
    filter_text:
        description:
            - The string that defines the Span Filter expression.
            - This parameter is updatable.
            - Applicable when config_type is 'SPAN_FILTER'
            - Required when config_type is 'SPAN_FILTER'
        type: str
    description:
        description:
            - An optional string that describes what the filter is intended or used for.
            - This parameter is updatable.
            - Applicable when config_type is 'SPAN_FILTER'
        type: str
    filter_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Span Filter. The filterId is mandatory for the creation
              of MetricGroups. A filterId will be generated when a Span Filter is created.
            - This parameter is updatable.
            - Applicable when config_type is 'METRIC_GROUP'
            - Required when config_type is 'METRIC_GROUP'
        type: str
    namespace:
        description:
            - The namespace to write the metrics to
            - This parameter is updatable.
            - Applicable when config_type is 'METRIC_GROUP'
        type: str
    dimensions:
        description:
            - A list of dimensions for this metric
            - This parameter is updatable.
            - Applicable when config_type is 'METRIC_GROUP'
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - The dimension name
                    - Required when config_type is 'METRIC_GROUP'
                type: str
                required: true
            value_source:
                description:
                    - The source to populate the dimension. Must be NULL at the moment.
                    - Applicable when config_type is 'METRIC_GROUP'
                type: str
    metrics:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when config_type is 'METRIC_GROUP'
            - Required when config_type is 'METRIC_GROUP'
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - The name of the metric
                    - Required when config_type is 'METRIC_GROUP'
                type: str
                required: true
            value_source:
                description:
                    - "Must be NULL at the moment, and \\"name\\" must be a known metric."
                    - Applicable when config_type is 'METRIC_GROUP'
                type: str
            unit:
                description:
                    - The unit of the metric
                    - Applicable when config_type is 'METRIC_GROUP'
                type: str
            description:
                description:
                    - A description of the metric
                    - Applicable when config_type is 'METRIC_GROUP'
                type: str
    rules:
        description:
            - ""
            - This parameter is updatable.
            - Required when config_type is 'APDEX'
        type: list
        elements: dict
        suboptions:
            filter_text:
                description:
                    - The string that defines the Span Filter expression.
                    - Required when config_type is 'APDEX'
                type: str
                required: true
            priority:
                description:
                    - The priority controls the order in which multiple rules in a rule set are applied. Lower values indicate higher
                      priorities. Rules with higher priority are applied first, and once a match is found, the rest of the rules are
                      ignored. Rules within the same rule set cannot have the same priority.
                    - Required when config_type is 'APDEX'
                type: int
                required: true
            is_enabled:
                description:
                    - "Specifies if the Apdex rule will be computed for spans matching the rule. Can be used to make sure certain
                      spans don't get an Apdex score. The default is \\"true\\"."
                    - Applicable when config_type is 'APDEX'
                type: bool
            satisfied_response_time:
                description:
                    - The maximum response time in milliseconds that will be considered satisfactory for the end user.
                    - Applicable when config_type is 'APDEX'
                type: int
            tolerating_response_time:
                description:
                    - "The maximum response time in milliseconds that will be considered tolerable for the end user. Response
                      times beyond this threshold will be considered frustrating.
                      This value cannot be lower than \\"satisfiedResponseTime\\"."
                    - Applicable when config_type is 'APDEX'
                type: int
            is_apply_to_error_spans:
                description:
                    - If true, the rule will compute the actual Apdex score for spans that have been marked as errors. If false,
                      the rule will always set the Apdex for error spans to frustrating, regardless of the configured thresholds.
                      Default is false.
                    - Applicable when config_type is 'APDEX'
                type: bool
            display_name:
                description:
                    - A user-friendly name that provides a short description this rule.
                    - Applicable when config_type is 'APDEX'
                type: str
                aliases: ["name"]
    opc_dry_run:
        description:
            - "Indicates that this request is a dry-run.
              If set to \\"true\\", nothing will be modified, only the validation will be performed."
            - This parameter is updatable.
        type: str
    config_id:
        description:
            - The OCID of the ConfiguredItem.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Config.
            - Use I(state=present) to create or update a Config.
            - Use I(state=absent) to delete a Config.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create config with config_type = SPAN_FILTER
  oci_apm_config_config:
    # required
    config_type: SPAN_FILTER

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    filter_text: filter_text_example
    description: description_example

- name: Create config with config_type = METRIC_GROUP
  oci_apm_config_config:
    # required
    config_type: METRIC_GROUP

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    filter_id: "ocid1.filter.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    dimensions:
    - # required
      name: name_example

      # optional
      value_source: value_source_example
    metrics:
    - # required
      name: name_example

      # optional
      value_source: value_source_example
      unit: unit_example
      description: description_example

- name: Create config with config_type = APDEX
  oci_apm_config_config:
    # required
    config_type: APDEX
    rules:
    - # required
      filter_text: filter_text_example
      priority: 56

      # optional
      is_enabled: true
      satisfied_response_time: 56
      tolerating_response_time: 56
      is_apply_to_error_spans: true
      display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example

- name: Update config with config_type = SPAN_FILTER
  oci_apm_config_config:
    # required
    config_type: SPAN_FILTER

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    filter_text: filter_text_example
    description: description_example

- name: Update config with config_type = METRIC_GROUP
  oci_apm_config_config:
    # required
    config_type: METRIC_GROUP

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    filter_id: "ocid1.filter.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    dimensions:
    - # required
      name: name_example

      # optional
      value_source: value_source_example
    metrics:
    - # required
      name: name_example

      # optional
      value_source: value_source_example
      unit: unit_example
      description: description_example

- name: Update config with config_type = APDEX
  oci_apm_config_config:
    # required
    config_type: APDEX
    rules:
    - # required
      filter_text: filter_text_example
      priority: 56

      # optional
      is_enabled: true
      satisfied_response_time: 56
      tolerating_response_time: 56
      is_apply_to_error_spans: true
      display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example

- name: Update config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with config_type = SPAN_FILTER
  oci_apm_config_config:
    # required
    config_type: SPAN_FILTER

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    filter_text: filter_text_example
    description: description_example

- name: Update config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with config_type = METRIC_GROUP
  oci_apm_config_config:
    # required
    config_type: METRIC_GROUP

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    filter_id: "ocid1.filter.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    dimensions:
    - # required
      name: name_example

      # optional
      value_source: value_source_example
    metrics:
    - # required
      name: name_example

      # optional
      value_source: value_source_example
      unit: unit_example
      description: description_example

- name: Update config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with config_type = APDEX
  oci_apm_config_config:
    # required
    config_type: APDEX
    rules:
    - # required
      filter_text: filter_text_example
      priority: 56

      # optional
      is_enabled: true
      satisfied_response_time: 56
      tolerating_response_time: 56
      is_apply_to_error_spans: true
      display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example

- name: Delete config
  oci_apm_config_config:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    config_id: "ocid1.config.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apm_config_config:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
config:
    description:
        - Details of the Config resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the configuration item. An OCID will be generated
                  when the item is created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        config_type:
            description:
                - The type of configuration item
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
        display_name:
            description:
                - The name by which this rule set can be displayed to the user.
            returned: on success
            type: str
            sample: display_name_example
        rules:
            description:
                - ""
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
                        - "Specifies if the Apdex rule will be computed for spans matching the rule. Can be used to make sure certain
                          spans don't get an Apdex score. The default is \\"true\\"."
                    returned: on success
                    type: bool
                    sample: true
                satisfied_response_time:
                    description:
                        - The maximum response time in milliseconds that will be considered satisfactory for the end user.
                    returned: on success
                    type: int
                    sample: 56
                tolerating_response_time:
                    description:
                        - "The maximum response time in milliseconds that will be considered tolerable for the end user. Response
                          times beyond this threshold will be considered frustrating.
                          This value cannot be lower than \\"satisfiedResponseTime\\"."
                    returned: on success
                    type: int
                    sample: 56
                is_apply_to_error_spans:
                    description:
                        - If true, the rule will compute the actual Apdex score for spans that have been marked as errors. If false,
                          the rule will always set the Apdex for error spans to frustrating, regardless of the configured thresholds.
                          Default is false.
                    returned: on success
                    type: bool
                    sample: true
                display_name:
                    description:
                        - A user-friendly name that provides a short description this rule.
                    returned: on success
                    type: str
                    sample: display_name_example
        filter_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a Span Filter. The filterId is mandatory for the
                  creation
                  of MetricGroups. A filterId will be generated when a Span Filter is created.
            returned: on success
            type: str
            sample: "ocid1.filter.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - The namespace to write the metrics to
            returned: on success
            type: str
            sample: namespace_example
        dimensions:
            description:
                - A list of dimensions for this metric
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The dimension name
                    returned: on success
                    type: str
                    sample: name_example
                value_source:
                    description:
                        - The source to populate the dimension. Must be NULL at the moment.
                    returned: on success
                    type: str
                    sample: value_source_example
        metrics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the metric
                    returned: on success
                    type: str
                    sample: name_example
                value_source:
                    description:
                        - "Must be NULL at the moment, and \\"name\\" must be a known metric."
                    returned: on success
                    type: str
                    sample: value_source_example
                unit:
                    description:
                        - The unit of the metric
                    returned: on success
                    type: str
                    sample: unit_example
                description:
                    description:
                        - A description of the metric
                    returned: on success
                    type: str
                    sample: description_example
        filter_text:
            description:
                - The string that defines the Span Filter expression.
            returned: on success
            type: str
            sample: filter_text_example
        description:
            description:
                - An optional string that describes what the filter is intended or used for.
            returned: on success
            type: str
            sample: description_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "config_type": "SPAN_FILTER",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
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
        "filter_text": "filter_text_example",
        "description": "description_example"
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
    from oci.apm_config import ConfigClient
    from oci.apm_config.models import CreateConfigDetails
    from oci.apm_config.models import UpdateConfigDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ConfigHelperGen, self).get_possible_entity_types() + [
            "config",
            "configs",
            "apmConfigconfig",
            "apmConfigconfigs",
            "configresource",
            "configsresource",
            "apmconfig",
        ]

    def get_module_resource_id_param(self):
        return "config_id"

    def get_module_resource_id(self):
        return self.module.params.get("config_id")

    def get_get_fn(self):
        return self.client.get_config

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_config, config_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_config,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            config_id=self.module.params.get("config_id"),
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
            else ["config_type", "display_name"]
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
        return oci_common_utils.list_all_resources(self.client.list_configs, **kwargs)

    def get_create_model_class(self):
        return CreateConfigDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                create_config_details=create_details,
                opc_dry_run=self.module.params.get("opc_dry_run"),
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
        return UpdateConfigDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                config_id=self.module.params.get("config_id"),
                update_config_details=update_details,
                opc_dry_run=self.module.params.get("opc_dry_run"),
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
            call_fn=self.client.delete_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                config_id=self.module.params.get("config_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ConfigHelperCustom = get_custom_class("ConfigHelperCustom")


class ResourceHelper(ConfigHelperCustom, ConfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            config_type=dict(
                type="str", choices=["SPAN_FILTER", "METRIC_GROUP", "APDEX"]
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            filter_text=dict(type="str"),
            description=dict(type="str"),
            filter_id=dict(type="str"),
            namespace=dict(type="str"),
            dimensions=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True), value_source=dict(type="str")
                ),
            ),
            metrics=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value_source=dict(type="str"),
                    unit=dict(type="str"),
                    description=dict(type="str"),
                ),
            ),
            rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    filter_text=dict(type="str", required=True),
                    priority=dict(type="int", required=True),
                    is_enabled=dict(type="bool"),
                    satisfied_response_time=dict(type="int"),
                    tolerating_response_time=dict(type="int"),
                    is_apply_to_error_spans=dict(type="bool"),
                    display_name=dict(aliases=["name"], type="str"),
                ),
            ),
            opc_dry_run=dict(type="str"),
            config_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="config",
        service_client_class=ConfigClient,
        namespace="apm_config",
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
