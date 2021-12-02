#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_log_analytics_object_collection_rule_facts
short_description: Fetches details about one or multiple LogAnalyticsObjectCollectionRule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LogAnalyticsObjectCollectionRule resources in Oracle Cloud Infrastructure
    - Gets list of collection rules.
    - If I(log_analytics_object_collection_rule_id) is specified, the details of a single LogAnalyticsObjectCollectionRule will be returned.
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
            - Required to get a specific log_analytics_object_collection_rule.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple log_analytics_object_collection_rules.
        type: str
    name:
        description:
            - A filter to return rules only matching with this name.
        type: str
    lifecycle_state:
        description:
            - Lifecycle state filter.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeUpdated is descending.
              Default order for name is ascending. If no value is specified timeUpdated is default.
        type: str
        choices:
            - "timeUpdated"
            - "timeCreated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific log_analytics_object_collection_rule
  oci_log_analytics_object_collection_rule_facts:
    # required
    namespace_name: namespace_name_example
    log_analytics_object_collection_rule_id: "ocid1.loganalyticsobjectcollectionrule.oc1..xxxxxxEXAMPLExxxxxx"

- name: List log_analytics_object_collection_rules
  oci_log_analytics_object_collection_rule_facts:
    # required
    namespace_name: namespace_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: timeUpdated

"""

RETURN = """
log_analytics_object_collection_rules:
    description:
        - List of LogAnalyticsObjectCollectionRule resources
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
    sample: [{
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
        "overrides": {},
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "is_enabled": true,
        "object_name_filters": [],
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsObjectCollectionRuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "log_analytics_object_collection_rule_id",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_object_collection_rule,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_object_collection_rule_id=self.module.params.get(
                "log_analytics_object_collection_rule_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_log_analytics_object_collection_rules,
            namespace_name=self.module.params.get("namespace_name"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LogAnalyticsObjectCollectionRuleFactsHelperCustom = get_custom_class(
    "LogAnalyticsObjectCollectionRuleFactsHelperCustom"
)


class ResourceFactsHelper(
    LogAnalyticsObjectCollectionRuleFactsHelperCustom,
    LogAnalyticsObjectCollectionRuleFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            log_analytics_object_collection_rule_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeUpdated", "timeCreated", "name"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_analytics_object_collection_rule",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_analytics_object_collection_rules=result)


if __name__ == "__main__":
    main()
