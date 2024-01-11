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
module: oci_threat_intelligence_indicator_facts
short_description: Fetches details about one or multiple Indicator resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Indicator resources in Oracle Cloud Infrastructure
    - Get a list of threat indicator summaries based on the search criteria.
    - If I(indicator_id) is specified, the details of a single Indicator will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    indicator_id:
        description:
            - The unique identifier (OCID) of the threat indicator.
            - Required to get a specific indicator.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the tenancy (root compartment) that is used to filter results.
        type: str
        required: true
    threat_type_name:
        description:
            - The threat type of entites to be returned. To filter for multiple threat types, repeat this parameter.
        type: list
        elements: str
    type:
        description:
            - The indicator type of entities to be returned.
        type: str
        choices:
            - "DOMAIN_NAME"
            - "FILE_NAME"
            - "MD5_HASH"
            - "SHA1_HASH"
            - "SHA256_HASH"
            - "IP_ADDRESS"
            - "URL"
    value:
        description:
            - The indicator value of entities to be returned.
        type: str
    confidence_greater_than_or_equal_to:
        description:
            - The minimum confidence score of entities to be returned.
        type: int
    time_updated_greater_than_or_equal_to:
        description:
            - The oldest update time of entities to be returned.
        type: str
    time_updated_less_than:
        description:
            - Return indicators updated before the provided time.
        type: str
    time_last_seen_greater_than_or_equal_to:
        description:
            - The oldest last seen time of entities to be returned.
        type: str
    time_last_seen_less_than:
        description:
            - Return indicators last seen before the provided time.
        type: str
    time_created_greater_than_or_equal_to:
        description:
            - The oldest created/first seen time of entities to be returned.
        type: str
    time_created_less_than:
        description:
            - Return indicators created/first seen before the provided time.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one field to sort by may be provided.
        type: str
        choices:
            - "confidence"
            - "timeCreated"
            - "timeUpdated"
            - "timeLastSeen"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific indicator
  oci_threat_intelligence_indicator_facts:
    # required
    indicator_id: "ocid1.indicator.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List indicators
  oci_threat_intelligence_indicator_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    threat_type_name: [ "threat_type_name_example" ]
    type: DOMAIN_NAME
    value: value_example
    confidence_greater_than_or_equal_to: 0
    time_updated_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_updated_less_than: 2013-10-20T19:20:30+01:00
    time_last_seen_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_last_seen_less_than: 2013-10-20T19:20:30+01:00
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_created_less_than: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: confidence

"""

RETURN = """
indicators:
    description:
        - List of Indicator resources
    returned: on success
    type: complex
    contains:
        relationships:
            description:
                - A map of relationships between the indicator and other entities.
                  Each relationship has a name (string), related entity, and attribution (supporting data).
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the attribute.
                    returned: on success
                    type: str
                    sample: name_example
                related_entity:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of the referenced entity.
                            returned: on success
                            type: str
                            sample: INDICATOR
                        indicator_id:
                            description:
                                - The unique OCID of the referenced threat indicator.
                            returned: on success
                            type: str
                            sample: "ocid1.indicator.oc1..xxxxxxEXAMPLExxxxxx"
                attribution:
                    description:
                        - The array of attribution data that support this relationship.
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - An integer from 0 to 100 that provides a measure of our certainty in the maliciousness of data attributed to an indicator. For
                                  example, if the source of the data being attributed is the Tor Project, our confidence that the associated indicator is a tor
                                  exit node would be 100.
                            returned: on success
                            type: int
                            sample: 56
                        source:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the source.
                                    returned: on success
                                    type: str
                                    sample: name_example
                        visibility:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the visibility level.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                tlp_name:
                                    description:
                                        - The Traffic Light Protocol (TLP) color of the visibility level.
                                    returned: on success
                                    type: str
                                    sample: TLP_INTERNAL_AUDIT
                        time_first_seen:
                            description:
                                - The date and time the attribution data was first seen for this entity. If the data source does not provide this information,
                                  it is set to the last time it was seen. An RFC3339 formatted string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_last_seen:
                            description:
                                - The last date and time the attribution data was seen for this entity. An RFC3339 formatted string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
        id:
            description:
                - The OCID of the indicator.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - The type of indicator.
            returned: on success
            type: str
            sample: DOMAIN_NAME
        value:
            description:
                - "The value for this indicator.
                  The value's format is dependent upon its `type`. Examples:"
                - "DOMAIN_NAME \\"evil.example.com\\""
                - "MD5_HASH \\"44d88612fea8a8f36de82e1278abb02f\\""
                - "IP_ADDRESS \\"2001:db8::1\\""
            returned: on success
            type: str
            sample: value_example
        confidence:
            description:
                - An integer from 0 to 100 that represents how certain we are that the indicator is malicious and a potential threat if it is detected
                  communicating with your cloud resources. This confidence value is aggregated from the confidence in the threat types, attributes, and
                  relationships to create an overall value for the indicator.
            returned: on success
            type: int
            sample: 56
        compartment_id:
            description:
                - The OCID of the compartment that contains this indicator.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        threat_types:
            description:
                - Characteristics of the threat indicator based on previous observations or behavior. May include related tactics, techniques, and procedures.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the threat type.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the threat type.
                    returned: on success
                    type: str
                    sample: name_example
                attribution:
                    description:
                        - The list of supporting attribution information.
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - An integer from 0 to 100 that provides a measure of our certainty in the maliciousness of data attributed to an indicator. For
                                  example, if the source of the data being attributed is the Tor Project, our confidence that the associated indicator is a tor
                                  exit node would be 100.
                            returned: on success
                            type: int
                            sample: 56
                        source:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the source.
                                    returned: on success
                                    type: str
                                    sample: name_example
                        visibility:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the visibility level.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                tlp_name:
                                    description:
                                        - The Traffic Light Protocol (TLP) color of the visibility level.
                                    returned: on success
                                    type: str
                                    sample: TLP_INTERNAL_AUDIT
                        time_first_seen:
                            description:
                                - The date and time the attribution data was first seen for this entity. If the data source does not provide this information,
                                  it is set to the last time it was seen. An RFC3339 formatted string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_last_seen:
                            description:
                                - The last date and time the attribution data was seen for this entity. An RFC3339 formatted string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
        attributes:
            description:
                - A map of attributes with additional information about the indicator.
                  Each attribute has a name (string), value (string), and attribution (supporting data).
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the attribute.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - The value of the attribute.
                    returned: on success
                    type: str
                    sample: value_example
                attribution:
                    description:
                        - The array of attribution data that support this attribute.
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - An integer from 0 to 100 that provides a measure of our certainty in the maliciousness of data attributed to an indicator. For
                                  example, if the source of the data being attributed is the Tor Project, our confidence that the associated indicator is a tor
                                  exit node would be 100.
                            returned: on success
                            type: int
                            sample: 56
                        source:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the source.
                                    returned: on success
                                    type: str
                                    sample: name_example
                        visibility:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the visibility level.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                tlp_name:
                                    description:
                                        - The Traffic Light Protocol (TLP) color of the visibility level.
                                    returned: on success
                                    type: str
                                    sample: TLP_INTERNAL_AUDIT
                        time_first_seen:
                            description:
                                - The date and time the attribution data was first seen for this entity. If the data source does not provide this information,
                                  it is set to the last time it was seen. An RFC3339 formatted string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_last_seen:
                            description:
                                - The last date and time the attribution data was seen for this entity. An RFC3339 formatted string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the indicator. It will always be `ACTIVE`.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - The date and time that the indicator was first detected. An RFC3339 formatted string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time that this indicator was last updated. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted
                  string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_seen:
            description:
                - The date and time that this indicator was last seen. The value is the same as `timeCreated` for a new indicator. An RFC3339 formatted string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        geodata:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                routed_prefix:
                    description:
                        - Encompassing assigned prefix for the IP
                    returned: on success
                    type: str
                    sample: routed_prefix_example
                origin:
                    description:
                        - ASN entry
                    returned: on success
                    type: str
                    sample: origin_example
                geo_id:
                    description:
                        - Unique Identifier (optional)
                    returned: on success
                    type: str
                    sample: "ocid1.geo.oc1..xxxxxxEXAMPLExxxxxx"
                country_code:
                    description:
                        - Two-letter abbreviation for country of origin
                    returned: on success
                    type: str
                    sample: country_code_example
                admin_div:
                    description:
                        - State/Province/subdivision within the country
                    returned: on success
                    type: str
                    sample: admin_div_example
                city:
                    description:
                        - City of origin
                    returned: on success
                    type: str
                    sample: city_example
                latitude:
                    description:
                        - Latitude
                    returned: on success
                    type: str
                    sample: latitude_example
                longitude:
                    description:
                        - Longitude
                    returned: on success
                    type: str
                    sample: longitude_example
                label:
                    description:
                        - Information on source providing the information
                    returned: on success
                    type: str
                    sample: label_example
    sample: [{
        "relationships": [{
            "name": "name_example",
            "related_entity": {
                "type": "INDICATOR",
                "indicator_id": "ocid1.indicator.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "attribution": [{
                "confidence": 56,
                "source": {
                    "name": "name_example"
                },
                "visibility": {
                    "name": "name_example",
                    "tlp_name": "TLP_INTERNAL_AUDIT"
                },
                "time_first_seen": "2013-10-20T19:20:30+01:00",
                "time_last_seen": "2013-10-20T19:20:30+01:00"
            }]
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "DOMAIN_NAME",
        "value": "value_example",
        "confidence": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "threat_types": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "attribution": [{
                "confidence": 56,
                "source": {
                    "name": "name_example"
                },
                "visibility": {
                    "name": "name_example",
                    "tlp_name": "TLP_INTERNAL_AUDIT"
                },
                "time_first_seen": "2013-10-20T19:20:30+01:00",
                "time_last_seen": "2013-10-20T19:20:30+01:00"
            }]
        }],
        "attributes": [{
            "name": "name_example",
            "value": "value_example",
            "attribution": [{
                "confidence": 56,
                "source": {
                    "name": "name_example"
                },
                "visibility": {
                    "name": "name_example",
                    "tlp_name": "TLP_INTERNAL_AUDIT"
                },
                "time_first_seen": "2013-10-20T19:20:30+01:00",
                "time_last_seen": "2013-10-20T19:20:30+01:00"
            }]
        }],
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_seen": "2013-10-20T19:20:30+01:00",
        "geodata": {
            "routed_prefix": "routed_prefix_example",
            "origin": "origin_example",
            "geo_id": "ocid1.geo.oc1..xxxxxxEXAMPLExxxxxx",
            "country_code": "country_code_example",
            "admin_div": "admin_div_example",
            "city": "city_example",
            "latitude": "latitude_example",
            "longitude": "longitude_example",
            "label": "label_example"
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.threat_intelligence import ThreatintelClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IndicatorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "indicator_id",
            "compartment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_indicator,
            indicator_id=self.module.params.get("indicator_id"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "threat_type_name",
            "type",
            "value",
            "confidence_greater_than_or_equal_to",
            "time_updated_greater_than_or_equal_to",
            "time_updated_less_than",
            "time_last_seen_greater_than_or_equal_to",
            "time_last_seen_less_than",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_indicators,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


IndicatorFactsHelperCustom = get_custom_class("IndicatorFactsHelperCustom")


class ResourceFactsHelper(IndicatorFactsHelperCustom, IndicatorFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            indicator_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str", required=True),
            threat_type_name=dict(type="list", elements="str"),
            type=dict(
                type="str",
                choices=[
                    "DOMAIN_NAME",
                    "FILE_NAME",
                    "MD5_HASH",
                    "SHA1_HASH",
                    "SHA256_HASH",
                    "IP_ADDRESS",
                    "URL",
                ],
            ),
            value=dict(type="str"),
            confidence_greater_than_or_equal_to=dict(type="int"),
            time_updated_greater_than_or_equal_to=dict(type="str"),
            time_updated_less_than=dict(type="str"),
            time_last_seen_greater_than_or_equal_to=dict(type="str"),
            time_last_seen_less_than=dict(type="str"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["confidence", "timeCreated", "timeUpdated", "timeLastSeen"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="indicator",
        service_client_class=ThreatintelClient,
        namespace="threat_intelligence",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(indicators=result)


if __name__ == "__main__":
    main()
