#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_log_analytics_object_collection_rule
short_description: Manage a LogAnalyticsObjectCollectionRule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a LogAnalyticsObjectCollectionRule resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a rule to collect logs from an object storage bucket.
    - "This resource has the following action operations in the M(oracle.oci.oci_log_analytics_object_collection_rule_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - A unique name given to the rule. The name must be unique within the tenancy, and cannot be modified.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to which this rule belongs.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    os_namespace:
        description:
            - Object Storage namespace.
            - Required for create using I(state=present).
        type: str
    os_bucket_name:
        description:
            - Name of the Object Storage bucket.
            - Required for create using I(state=present).
        type: str
    collection_type:
        description:
            - The type of collection.
        type: str
        choices:
            - "LIVE"
            - "HISTORIC"
            - "HISTORIC_LIVE"
    poll_since:
        description:
            - "The oldest time of the file in the bucket to consider for collection.
              Accepted values are: BEGINNING or CURRENT_TIME or RFC3339 formatted datetime string.
              Use this for HISTORIC or HISTORIC_LIVE collection types. When collectionType is LIVE, specifying pollSince value other than CURRENT_TIME will
              result in error."
        type: str
    poll_till:
        description:
            - "The newest time of the file in the bucket to consider for collection.
              Accepted values are: CURRENT_TIME or RFC3339 formatted datetime string.
              Use this for HISTORIC collection type. When collectionType is LIVE or HISTORIC_LIVE, specifying pollTill will result in error."
        type: str
    description:
        description:
            - A string that describes the details of the rule. It does not have to be unique, and can be changed.
              Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    log_group_id:
        description:
            - Logging Analytics Log group OCID to associate the processed logs with.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    log_source_name:
        description:
            - Name of the Logging Analytics Source to use for the processing.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    entity_id:
        description:
            - Logging Analytics entity OCID. Associates the processed logs with the given entity (optional).
            - This parameter is updatable.
        type: str
    char_encoding:
        description:
            - An optional character encoding to aid in detecting the character encoding of the contents of the objects while processing.
              It is recommended to set this value as ISO_8859_1 when configuring content of the objects having more numeric characters,
              and very few alphabets.
              For e.g. this applies when configuring VCN Flow Logs.
            - This parameter is updatable.
        type: str
    is_enabled:
        description:
            - Whether or not this rule is currently enabled.
            - This parameter is updatable.
        type: bool
    timezone:
        description:
            - Timezone to be used when processing log entries whose timestamps do not include an explicit timezone.
              When this property is not specified, the timezone of the entity specified is used.
              If the entity is also not specified or do not have a valid timezone then UTC is used.
            - This parameter is updatable.
        type: str
    log_set:
        description:
            - The logSet to be associated with the processed logs. The logSet feature can be used by customers with high volume of data
              and this feature has to be enabled for a given tenancy prior to its usage.
              When logSetExtRegex value is provided, it will take precedence over this logSet value and logSet will be computed dynamically
              using logSetKey and logSetExtRegex.
            - This parameter is updatable.
        type: str
    log_set_key:
        description:
            - An optional parameter to indicate from where the logSet to be extracted using logSetExtRegex. Default value is OBJECT_PATH (e.g.
              /n/<namespace>/b/<bucketname>/o/<objectname>).
            - This parameter is updatable.
        type: str
        choices:
            - "OBJECT_PATH"
    log_set_ext_regex:
        description:
            - The regex to be applied against given logSetKey. Regex has to be in string escaped format.
            - This parameter is updatable.
        type: str
    overrides:
        description:
            - "The override is used to modify some important configuration properties for objects matching a specific pattern inside the bucket.
              Supported propeties for override are: logSourceName, charEncoding, entityId.
              Supported matchType for override are \\"contains\\"."
            - This parameter is updatable.
        type: dict
    object_name_filters:
        description:
            - "When the filters are provided, only the objects matching the filters are picked up for processing.
              The matchType supported is exact match and accommodates wildcard \\"*\\".
              For more information on filters, see L(Event Filters,https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/filterevents.htm)."
            - This parameter is updatable.
        type: list
        elements: str
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    log_analytics_object_collection_rule_id:
        description:
            - The Logging Analytics Object Collection Rule L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the LogAnalyticsObjectCollectionRule.
            - Use I(state=present) to create or update a LogAnalyticsObjectCollectionRule.
            - Use I(state=absent) to delete a LogAnalyticsObjectCollectionRule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create log_analytics_object_collection_rule
  oci_log_analytics_object_collection_rule:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    os_namespace: os_namespace_example
    os_bucket_name: os_bucket_name_example
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    log_source_name: log_source_name_example
    namespace_name: namespace_name_example

    # optional
    collection_type: LIVE
    poll_since: poll_since_example
    poll_till: poll_till_example
    description: description_example
    entity_id: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
    char_encoding: char_encoding_example
    is_enabled: true
    timezone: timezone_example
    log_set: log_set_example
    log_set_key: OBJECT_PATH
    log_set_ext_regex: log_set_ext_regex_example
    overrides: null
    object_name_filters: [ "object_name_filters_example" ]
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update log_analytics_object_collection_rule
  oci_log_analytics_object_collection_rule:
    # required
    namespace_name: namespace_name_example
    log_analytics_object_collection_rule_id: "ocid1.loganalyticsobjectcollectionrule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    log_source_name: log_source_name_example
    entity_id: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
    char_encoding: char_encoding_example
    is_enabled: true
    timezone: timezone_example
    log_set: log_set_example
    log_set_key: OBJECT_PATH
    log_set_ext_regex: log_set_ext_regex_example
    overrides: null
    object_name_filters: [ "object_name_filters_example" ]
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update log_analytics_object_collection_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_log_analytics_object_collection_rule:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_name: namespace_name_example

    # optional
    description: description_example
    log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
    log_source_name: log_source_name_example
    entity_id: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
    char_encoding: char_encoding_example
    is_enabled: true
    timezone: timezone_example
    log_set: log_set_example
    log_set_key: OBJECT_PATH
    log_set_ext_regex: log_set_ext_regex_example
    overrides: null
    object_name_filters: [ "object_name_filters_example" ]
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete log_analytics_object_collection_rule
  oci_log_analytics_object_collection_rule:
    # required
    namespace_name: namespace_name_example
    log_analytics_object_collection_rule_id: "ocid1.loganalyticsobjectcollectionrule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete log_analytics_object_collection_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_log_analytics_object_collection_rule:
    # required
    name: name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_name: namespace_name_example
    state: absent

"""

RETURN = """
log_analytics_object_collection_rule:
    description:
        - Details of the LogAnalyticsObjectCollectionRule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A unique name to the rule. The name must be unique, within the tenancy, and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - A string that describes the details of the rule. It does not have to be unique, and can be changed.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to which this rule belongs.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        os_namespace:
            description:
                - Object Storage namespace.
            returned: on success
            type: str
            sample: os_namespace_example
        os_bucket_name:
            description:
                - Name of the Object Storage bucket.
            returned: on success
            type: str
            sample: os_bucket_name_example
        collection_type:
            description:
                - The type of log collection.
            returned: on success
            type: str
            sample: LIVE
        poll_since:
            description:
                - "The oldest time of the file in the bucket to consider for collection.
                  Accepted values are: BEGINNING or CURRENT_TIME or RFC3339 formatted datetime string.
                  Use this for HISTORIC or HISTORIC_LIVE collection types. When collectionType is LIVE, specifying pollSince value other than CURRENT_TIME will
                  result in error."
            returned: on success
            type: str
            sample: poll_since_example
        poll_till:
            description:
                - "The newest time of the file in the bucket to consider for collection.
                  Accepted values are: CURRENT_TIME or RFC3339 formatted datetime string.
                  Use this for HISTORIC collection type. When collectionType is LIVE or HISTORIC_LIVE, specifying pollTill will result in error."
            returned: on success
            type: str
            sample: poll_till_example
        log_group_id:
            description:
                - Logging Analytics Log group OCID to associate the processed logs with.
            returned: on success
            type: str
            sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
        log_source_name:
            description:
                - Name of the Logging Analytics Source to use for the processing.
            returned: on success
            type: str
            sample: log_source_name_example
        entity_id:
            description:
                - Logging Analytics entity OCID to associate the processed logs with.
            returned: on success
            type: str
            sample: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
        char_encoding:
            description:
                - An optional character encoding to aid in detecting the character encoding of the contents of the objects while processing.
                  It is recommended to set this value as ISO_8859_1 when configuring content of the objects having more numeric characters,
                  and very few alphabets.
                  For e.g. this applies when configuring VCN Flow Logs.
            returned: on success
            type: str
            sample: char_encoding_example
        timezone:
            description:
                - Timezone to be used when processing log entries whose timestamps do not include an explicit timezone.
                  When this property is not specified, the timezone of the entity specified is used.
                  If the entity is also not specified or do not have a valid timezone then UTC is used.
            returned: on success
            type: str
            sample: timezone_example
        log_set:
            description:
                - The logSet to be associated with the processed logs. The logSet feature can be used by customers with high volume of data
                  and this feature has to be enabled for a given tenancy prior to its usage.
                  When logSetExtRegex value is provided, it will take precedence over this logSet value and logSet will be computed dynamically
                  using logSetKey and logSetExtRegex.
            returned: on success
            type: str
            sample: log_set_example
        log_set_key:
            description:
                - An optional parameter to indicate from where the logSet to be extracted using logSetExtRegex. Default value is OBJECT_PATH (e.g.
                  /n/<namespace>/b/<bucketname>/o/<objectname>).
            returned: on success
            type: str
            sample: OBJECT_PATH
        log_set_ext_regex:
            description:
                - The regex to be applied against given logSetKey. Regex has to be in string escaped format.
            returned: on success
            type: str
            sample: log_set_ext_regex_example
        overrides:
            description:
                - "Use this to override some property values which are defined at bucket level to the scope of object.
                  Supported propeties for override are: logSourceName, charEncoding, entityId.
                  Supported matchType for override are \\"contains\\"."
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - The current state of the rule.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A detailed status of the life cycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time when this rule was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when this rule was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_enabled:
            description:
                - Whether or not this rule is currently enabled.
            returned: on success
            type: bool
            sample: true
        object_name_filters:
            description:
                - "When the filters are provided, only the objects matching the filters are picked up for processing.
                  The matchType supported is exact match and accommodates wildcard \\"*\\".
                  For more information on filters, see L(Event Filters,https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/filterevents.htm)."
            returned: on success
            type: list
            sample: []
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "os_namespace": "os_namespace_example",
        "os_bucket_name": "os_bucket_name_example",
        "collection_type": "LIVE",
        "poll_since": "poll_since_example",
        "poll_till": "poll_till_example",
        "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
        "log_source_name": "log_source_name_example",
        "entity_id": "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx",
        "char_encoding": "char_encoding_example",
        "timezone": "timezone_example",
        "log_set": "log_set_example",
        "log_set_key": "OBJECT_PATH",
        "log_set_ext_regex": "log_set_ext_regex_example",
        "overrides": {},
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "is_enabled": true,
        "object_name_filters": [],
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import CreateLogAnalyticsObjectCollectionRuleDetails
    from oci.log_analytics.models import UpdateLogAnalyticsObjectCollectionRuleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsObjectCollectionRuleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            LogAnalyticsObjectCollectionRuleHelperGen, self
        ).get_possible_entity_types() + [
            "loganalyticsobjectcollectionrule",
            "loganalyticsobjectcollectionrules",
            "logAnalyticsloganalyticsobjectcollectionrule",
            "logAnalyticsloganalyticsobjectcollectionrules",
            "loganalyticsobjectcollectionruleresource",
            "loganalyticsobjectcollectionrulesresource",
            "loganalytics",
        ]

    def get_module_resource_id_param(self):
        return "log_analytics_object_collection_rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_analytics_object_collection_rule_id")

    def get_get_fn(self):
        return self.client.get_log_analytics_object_collection_rule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_object_collection_rule,
            log_analytics_object_collection_rule_id=summary_model.id,
            namespace_name=self.module.params.get("namespace_name"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_object_collection_rule,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_object_collection_rule_id=self.module.params.get(
                "log_analytics_object_collection_rule_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "namespace_name",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

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
        return oci_common_utils.list_all_resources(
            self.client.list_log_analytics_object_collection_rules, **kwargs
        )

    def get_create_model_class(self):
        return CreateLogAnalyticsObjectCollectionRuleDetails

    def get_exclude_attributes(self):
        return ["poll_since", "poll_till"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_log_analytics_object_collection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                create_log_analytics_object_collection_rule_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateLogAnalyticsObjectCollectionRuleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_log_analytics_object_collection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_object_collection_rule_id=self.module.params.get(
                    "log_analytics_object_collection_rule_id"
                ),
                update_log_analytics_object_collection_rule_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_log_analytics_object_collection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_object_collection_rule_id=self.module.params.get(
                    "log_analytics_object_collection_rule_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


LogAnalyticsObjectCollectionRuleHelperCustom = get_custom_class(
    "LogAnalyticsObjectCollectionRuleHelperCustom"
)


class ResourceHelper(
    LogAnalyticsObjectCollectionRuleHelperCustom,
    LogAnalyticsObjectCollectionRuleHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            compartment_id=dict(type="str"),
            os_namespace=dict(type="str"),
            os_bucket_name=dict(type="str"),
            collection_type=dict(
                type="str", choices=["LIVE", "HISTORIC", "HISTORIC_LIVE"]
            ),
            poll_since=dict(type="str"),
            poll_till=dict(type="str"),
            description=dict(type="str"),
            log_group_id=dict(type="str"),
            log_source_name=dict(type="str"),
            entity_id=dict(type="str"),
            char_encoding=dict(type="str"),
            is_enabled=dict(type="bool"),
            timezone=dict(type="str"),
            log_set=dict(type="str"),
            log_set_key=dict(type="str", choices=["OBJECT_PATH"], no_log=True),
            log_set_ext_regex=dict(type="str"),
            overrides=dict(type="dict"),
            object_name_filters=dict(type="list", elements="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            namespace_name=dict(type="str", required=True),
            log_analytics_object_collection_rule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_analytics_object_collection_rule",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
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
