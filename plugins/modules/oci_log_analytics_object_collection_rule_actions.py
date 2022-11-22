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
module: oci_log_analytics_object_collection_rule_actions
short_description: Perform actions on a LogAnalyticsObjectCollectionRule resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a LogAnalyticsObjectCollectionRule resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move the rule from it's current compartment to the given compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    log_analytics_object_collection_rule_id:
        description:
            - The Logging Analytics Object Collection Rule L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to which the rule have to be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the LogAnalyticsObjectCollectionRule.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on log_analytics_object_collection_rule
  oci_log_analytics_object_collection_rule_actions:
    # required
    namespace_name: namespace_name_example
    log_analytics_object_collection_rule_id: "ocid1.loganalyticsobjectcollectionrule.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import (
        ChangeLogAnalyticsObjectCollectionRuleCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsObjectCollectionRuleActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "log_analytics_object_collection_rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_analytics_object_collection_rule_id")

    def get_get_fn(self):
        return self.client.get_log_analytics_object_collection_rule

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_object_collection_rule,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_object_collection_rule_id=self.module.params.get(
                "log_analytics_object_collection_rule_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeLogAnalyticsObjectCollectionRuleCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_log_analytics_object_collection_rule_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_object_collection_rule_id=self.module.params.get(
                    "log_analytics_object_collection_rule_id"
                ),
                change_log_analytics_object_collection_rule_compartment_details=action_details,
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


LogAnalyticsObjectCollectionRuleActionsHelperCustom = get_custom_class(
    "LogAnalyticsObjectCollectionRuleActionsHelperCustom"
)


class ResourceHelper(
    LogAnalyticsObjectCollectionRuleActionsHelperCustom,
    LogAnalyticsObjectCollectionRuleActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            log_analytics_object_collection_rule_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
