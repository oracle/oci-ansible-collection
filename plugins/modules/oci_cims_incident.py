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
module: oci_cims_incident
short_description: Manage an Incident resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update an Incident resource in Oracle Cloud Infrastructure
    - For I(state=present), enables the customer to create an support ticket.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy.
            - Required for create using I(state=present).
        type: str
    problem_type:
        description:
            - The kind of support ticket, such as a technical issue request.
            - Required for create using I(state=present).
        type: str
        choices:
            - "LIMIT"
            - "LEGACY_LIMIT"
            - "TECH"
            - "ACCOUNT"
    contacts:
        description:
            - The list of contacts.
        type: list
        elements: dict
        suboptions:
            contact_name:
                description:
                    - The name of the contact person.
                type: str
            contact_email:
                description:
                    - The email of the contact person.
                type: str
            contact_phone:
                description:
                    - The phone number of the contact person.
                type: str
            contact_type:
                description:
                    - The type of contact, such as primary or alternate.
                type: str
                choices:
                    - "PRIMARY"
                    - "ALTERNATE"
                    - "SECONDARY"
                    - "ADMIN"
                    - "MANAGER"
    referrer:
        description:
            - The incident referrer. This value is often the URL that the customer used when creating the support ticket.
        type: str
    incident_key:
        description:
            - Unique identifier for the support ticket.
            - Required for update using I(state=present).
        type: str
    csi:
        description:
            - The Customer Support Identifier number for the support account.
            - Required for create using I(state=present), update using I(state=present) with incident_key present.
        type: str
    ticket:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            severity:
                description:
                    - The severity of the support ticket.
                type: str
                choices:
                    - "HIGHEST"
                    - "HIGH"
                    - "MEDIUM"
            resource_list:
                description:
                    - The list of resources.
                type: list
                elements: dict
                suboptions:
                    item:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            type:
                                description:
                                    - The type of the item.
                                type: str
                                choices:
                                    - "tech"
                                    - "limit"
                                required: true
                            category:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    category_key:
                                        description:
                                            - Unique identifier for the category.
                                            - Applicable when type is 'tech'
                                        type: str
                            sub_category:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    sub_category_key:
                                        description:
                                            - Unique identifier for the subcategory.
                                            - Applicable when type is 'tech'
                                        type: str
                            issue_type:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    issue_type_key:
                                        description:
                                            - Unique identifier for the issue type.
                                            - Applicable when type is 'tech'
                                        type: str
                            name:
                                description:
                                    - The display name of the item.
                                type: str
                            current_limit:
                                description:
                                    - The limit of the resource currently available.
                                    - Applicable when type is 'limit'
                                type: int
                            current_usage:
                                description:
                                    - The current usage of the resource.
                                    - Applicable when type is 'limit'
                                type: int
                            requested_limit:
                                description:
                                    - Reserved for future use.
                                    - Applicable when type is 'limit'
                                type: int
                            limit_status:
                                description:
                                    - The current status of the request.
                                    - Applicable when type is 'limit'
                                type: str
                                choices:
                                    - "APPROVED"
                                    - "PARTIALLY_APPROVED"
                                    - "NOT_APPROVED"
                    region:
                        description:
                            - The list of available Oracle Cloud Infrastructure regions.
                        type: str
                        choices:
                            - "DEV"
                            - "SEA"
                            - "INTEG_NEXT"
                            - "INTEG_STABLE"
                            - "PHX"
                            - "IAD"
                            - "FRA"
                            - "EU_FRANKFURT_1"
                            - "LHR"
                            - "YYZ"
                            - "NRT"
                            - "ICN"
                            - "BOM"
                            - "GRU"
                            - "SYD"
                            - "ZRH"
                            - "JED"
                            - "AMS"
                            - "KIX"
                            - "MEL"
                            - "YUL"
                            - "HYD"
                            - "YNY"
                    availability_domain:
                        description:
                            - The list of available Oracle Cloud Infrastructure availability domains.
                        type: str
                        choices:
                            - "DEV_1"
                            - "DEV_2"
                            - "DEV_3"
                            - "INTEG_NEXT_1"
                            - "INTEG_STABLE_1"
                            - "SEA_AD_1"
                            - "SEA_AD_2"
                            - "SEA_AD_3"
                            - "PHX_AD_1"
                            - "PHX_AD_2"
                            - "PHX_AD_3"
                            - "US_ASHBURN_AD_1"
                            - "US_ASHBURN_AD_2"
                            - "US_ASHBURN_AD_3"
                            - "US_ASHBURN_AD_4"
                            - "EU_FRANKFURT_1_AD_1"
                            - "EU_FRANKFURT_1_AD_2"
                            - "EU_FRANKFURT_1_AD_3"
                            - "UK_LONDON_1_AD_1"
                            - "UK_LONDON_1_AD_2"
                            - "UK_LONDON_1_AD_3"
                            - "CA_TORONTO_1_AD_1"
                            - "AP_TOKYO_1_AD_1"
                            - "AP_SEOUL_1_AD_1"
                            - "AP_MUMBAI_1_AD_1"
                            - "SA_SAOPAULO_1_AD_1"
                            - "ME_JEDDAH_1_AD_1"
                            - "AP_OSAKA_1_AD_1"
                            - "AP_SYDNEY_1_AD_1"
                            - "EU_ZURICH_1_AD_1"
                            - "EU_AMSTERDAM_1_AD_1"
                            - "AP_MELBOURNE_1_AD_1"
                            - "CA_MONTREAL_1_AD_1"
                            - "AP_HYDERABAD_1_AD_1"
                            - "AP_CHUNCHEON_1_AD_1"
                            - "NO_AD"
            title:
                description:
                    - The title of the support ticket.
                type: str
            description:
                description:
                    - The description of the support ticket.
                type: str
            contextual_data:
                description:
                    - The context from where the ticket is getting created.
                type: dict
                suboptions:
                    client_id:
                        description:
                            - The unique client identifier
                        type: str
                        required: true
                    schema_name:
                        description:
                            - The schema name
                        type: str
                        required: true
                    schema_version:
                        description:
                            - The schema version
                        type: str
                        required: true
                    payload:
                        description:
                            - The context data payload
                        type: str
                        required: true
            resource:
                description:
                    - The list of resources.
                    - This parameter is updatable.
                type: dict
    ocid:
        description:
            - User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.
        type: str
        required: true
    homeregion:
        description:
            - The region of the tenancy.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the Incident.
            - Use I(state=present) to create or update an Incident.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create incident
  oci_cims_incident:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    problem_type: LIMIT
    csi: csi_example
    ticket:
      # optional
      severity: HIGHEST
      resource_list:
      - # optional
        item:
          # required
          type: tech

          # optional
          category:
            # optional
            category_key: category_key_example
          sub_category:
            # optional
            sub_category_key: sub_category_key_example
          issue_type:
            # optional
            issue_type_key: issue_type_key_example
          name: name_example
        region: us-phoenix-1
        availability_domain: Uocm:PHX-AD-1
      title: title_example
      description: description_example
      contextual_data:
        # required
        client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        schema_name: schema_name_example
        schema_version: schema_version_example
        payload: payload_example
      resource: null
    ocid: ocid_example

    # optional
    contacts:
    - # optional
      contact_name: contact_name_example
      contact_email: contact_email_example
      contact_phone: contact_phone_example
      contact_type: PRIMARY
    referrer: referrer_example
    homeregion: us-phoenix-1

- name: Update incident
  oci_cims_incident:
    # required
    incident_key: incident_key_example
    csi: csi_example
    ticket:
      # optional
      severity: HIGHEST
      resource_list:
      - # optional
        item:
          # required
          type: tech

          # optional
          category:
            # optional
            category_key: category_key_example
          sub_category:
            # optional
            sub_category_key: sub_category_key_example
          issue_type:
            # optional
            issue_type_key: issue_type_key_example
          name: name_example
        region: us-phoenix-1
        availability_domain: Uocm:PHX-AD-1
      title: title_example
      description: description_example
      contextual_data:
        # required
        client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        schema_name: schema_name_example
        schema_version: schema_version_example
        payload: payload_example
      resource: null
    ocid: ocid_example

    # optional
    homeregion: us-phoenix-1

"""

RETURN = """
incident:
    description:
        - Details of the Incident resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique identifier for the support ticket.
            returned: on success
            type: str
            sample: key_example
        compartment_id:
            description:
                - The OCID of the tenancy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        contact_list:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                contact_list:
                    description:
                        - The list of contacts.
                    returned: on success
                    type: complex
                    contains:
                        contact_name:
                            description:
                                - The name of the contact person.
                            returned: on success
                            type: str
                            sample: contact_name_example
                        contact_email:
                            description:
                                - The email of the contact person.
                            returned: on success
                            type: str
                            sample: contact_email_example
                        contact_phone:
                            description:
                                - The phone number of the contact person.
                            returned: on success
                            type: str
                            sample: contact_phone_example
                        contact_type:
                            description:
                                - The type of contact, such as primary or alternate.
                            returned: on success
                            type: str
                            sample: PRIMARY
        tenancy_information:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                customer_support_key:
                    description:
                        - The Customer Support Identifier number associated with the tenancy.
                    returned: on success
                    type: str
                    sample: customer_support_key_example
                tenancy_id:
                    description:
                        - The OCID of the tenancy.
                    returned: on success
                    type: str
                    sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        ticket:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ticket_number:
                    description:
                        - Unique identifier for the ticket.
                    returned: on success
                    type: str
                    sample: ticket_number_example
                severity:
                    description:
                        - The severity assigned to the ticket.
                    returned: on success
                    type: str
                    sample: HIGHEST
                resource_list:
                    description:
                        - The list of resources associated with the ticket.
                    returned: on success
                    type: complex
                    contains:
                        item:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                comments:
                                    description:
                                        - Comments added with the activity on the support ticket.
                                    returned: on success
                                    type: str
                                    sample: comments_example
                                time_created:
                                    description:
                                        - The time when the activity was created, in milliseconds since epoch time.
                                    returned: on success
                                    type: int
                                    sample: 56
                                time_updated:
                                    description:
                                        - The time when the activity was updated, in milliseconds since epoch time.
                                    returned: on success
                                    type: int
                                    sample: 56
                                activity_type:
                                    description:
                                        - The type of activity occuring on the support ticket.
                                    returned: on success
                                    type: str
                                    sample: NOTES
                                activity_author:
                                    description:
                                        - The person who updates the activity on the support ticket.
                                    returned: on success
                                    type: str
                                    sample: CUSTOMER
                                current_limit:
                                    description:
                                        - The currently available limit of the resource.
                                    returned: on success
                                    type: int
                                    sample: 56
                                current_usage:
                                    description:
                                        - The current usage of the resource.
                                    returned: on success
                                    type: int
                                    sample: 56
                                requested_limit:
                                    description:
                                        - The requested limit for the resource.
                                    returned: on success
                                    type: int
                                    sample: 56
                                limit_status:
                                    description:
                                        - The status of the request.
                                    returned: on success
                                    type: str
                                    sample: APPROVED
                                item_key:
                                    description:
                                        - Unique identifier for the item.
                                    returned: on success
                                    type: str
                                    sample: item_key_example
                                name:
                                    description:
                                        - The display name of the item.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                type:
                                    description:
                                        - The type of the support request.
                                    returned: on success
                                    type: str
                                    sample: activity
                                category:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        category_key:
                                            description:
                                                - Unique identifier for the category.
                                            returned: on success
                                            type: str
                                            sample: category_key_example
                                        name:
                                            description:
                                                - The name of the category. For example, `Compute` or `Identity`.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                sub_category:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        sub_category_key:
                                            description:
                                                - Unique identifier for the subcategory.
                                            returned: on success
                                            type: str
                                            sample: sub_category_key_example
                                        name:
                                            description:
                                                - The name of the subcategory. For example, `Backup Count` or `Custom Image Count`.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                issue_type:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        issue_type_key:
                                            description:
                                                - Unique identifier for the issue type.
                                            returned: on success
                                            type: str
                                            sample: issue_type_key_example
                                        label:
                                            description:
                                                - The label for the issue type. For example, `Instance Performance`.
                                            returned: on success
                                            type: str
                                            sample: label_example
                        region:
                            description:
                                - The list of available Oracle Cloud Infrastructure regions.
                            returned: on success
                            type: str
                            sample: us-phoenix-1
                        availability_domain:
                            description:
                                - The list of available Oracle Cloud Infrastructure availability domains.
                            returned: on success
                            type: str
                            sample: Uocm:PHX-AD-1
                title:
                    description:
                        - The title of the ticket.
                    returned: on success
                    type: str
                    sample: title_example
                description:
                    description:
                        - The description of the issue addressed in the ticket.
                    returned: on success
                    type: str
                    sample: description_example
                time_created:
                    description:
                        - The time when the ticket was created, in milliseconds since epoch time.
                    returned: on success
                    type: int
                    sample: 56
                time_updated:
                    description:
                        - The time when the ticket was updated, in milliseconds since epoch time.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the ticket.
                    returned: on success
                    type: str
                    sample: ACTIVE
                lifecycle_details:
                    description:
                        - Additional information about the current `lifecycleState`.
                    returned: on success
                    type: str
                    sample: PENDING_WITH_ORACLE
        incident_type:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - Unique identifier for the incident type.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the incident type.
                    returned: on success
                    type: str
                    sample: name_example
                label:
                    description:
                        - The label associated with the incident type.
                    returned: on success
                    type: str
                    sample: label_example
                description:
                    description:
                        - The description of the incident type.
                    returned: on success
                    type: str
                    sample: description_example
                classifier_list:
                    description:
                        - The list of classifiers.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - Unique identifier of the classifier.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        name:
                            description:
                                - The display name of the classifier.
                            returned: on success
                            type: str
                            sample: name_example
                        label:
                            description:
                                - The label associated with the classifier.
                            returned: on success
                            type: str
                            sample: label_example
                        description:
                            description:
                                - The description of the classifier.
                            returned: on success
                            type: str
                            sample: description_example
                        issue_type_list:
                            description:
                                - The list of issues.
                            returned: on success
                            type: complex
                            contains:
                                issue_type_key:
                                    description:
                                        - Unique identifier for the issue type.
                                    returned: on success
                                    type: str
                                    sample: issue_type_key_example
                                label:
                                    description:
                                        - The label for the issue type. For example, `Instance Performance`.
                                    returned: on success
                                    type: str
                                    sample: label_example
                        scope:
                            description:
                                - The scope of the service category or resource.
                            returned: on success
                            type: str
                            sample: AD
                        unit:
                            description:
                                - The unit to use to measure the service category or resource.
                            returned: on success
                            type: str
                            sample: COUNT
        problem_type:
            description:
                - The kind of support ticket, such as a technical support request.
            returned: on success
            type: str
            sample: LIMIT
        referrer:
            description:
                - The incident referrer. This value is often the URL that the customer used when creating the support ticket.
            returned: on success
            type: str
            sample: referrer_example
    sample: {
        "key": "key_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "contact_list": {
            "contact_list": [{
                "contact_name": "contact_name_example",
                "contact_email": "contact_email_example",
                "contact_phone": "contact_phone_example",
                "contact_type": "PRIMARY"
            }]
        },
        "tenancy_information": {
            "customer_support_key": "customer_support_key_example",
            "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "ticket": {
            "ticket_number": "ticket_number_example",
            "severity": "HIGHEST",
            "resource_list": [{
                "item": {
                    "comments": "comments_example",
                    "time_created": 56,
                    "time_updated": 56,
                    "activity_type": "NOTES",
                    "activity_author": "CUSTOMER",
                    "current_limit": 56,
                    "current_usage": 56,
                    "requested_limit": 56,
                    "limit_status": "APPROVED",
                    "item_key": "item_key_example",
                    "name": "name_example",
                    "type": "activity",
                    "category": {
                        "category_key": "category_key_example",
                        "name": "name_example"
                    },
                    "sub_category": {
                        "sub_category_key": "sub_category_key_example",
                        "name": "name_example"
                    },
                    "issue_type": {
                        "issue_type_key": "issue_type_key_example",
                        "label": "label_example"
                    }
                },
                "region": "us-phoenix-1",
                "availability_domain": "Uocm:PHX-AD-1"
            }],
            "title": "title_example",
            "description": "description_example",
            "time_created": 56,
            "time_updated": 56,
            "lifecycle_state": "ACTIVE",
            "lifecycle_details": "PENDING_WITH_ORACLE"
        },
        "incident_type": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "label": "label_example",
            "description": "description_example",
            "classifier_list": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "name": "name_example",
                "label": "label_example",
                "description": "description_example",
                "issue_type_list": [{
                    "issue_type_key": "issue_type_key_example",
                    "label": "label_example"
                }],
                "scope": "AD",
                "unit": "COUNT"
            }]
        },
        "problem_type": "LIMIT",
        "referrer": "referrer_example"
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
    from oci.cims import IncidentClient
    from oci.cims.models import CreateIncident
    from oci.cims.models import UpdateIncident

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IncidentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(IncidentHelperGen, self).get_possible_entity_types() + [
            "incident",
            "incidents",
            "cimsincident",
            "cimsincidents",
            "incidentresource",
            "incidentsresource",
            "cims",
        ]

    def get_module_resource_id_param(self):
        return "incident_key"

    def get_module_resource_id(self):
        return self.module.params.get("incident_key")

    def get_get_fn(self):
        return self.client.get_incident

    def get_resource(self):
        optional_params = [
            "homeregion",
            "problem_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_incident,
            incident_key=self.module.params.get("incident_key"),
            csi=self.module.params.get("csi"),
            ocid=self.module.params.get("ocid"),
            **optional_kwargs
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "csi",
            "compartment_id",
            "ocid",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["homeregion", "problem_type"]

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
        return oci_common_utils.list_all_resources(self.client.list_incidents, **kwargs)

    def get_create_model_class(self):
        return CreateIncident

    def get_exclude_attributes(self):
        return ["ticket.contextual_data", "csi", "contacts"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_incident,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_incident_details=create_details,
                ocid=self.module.params.get("ocid"),
                homeregion=self.module.params.get("homeregion"),
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
        return UpdateIncident

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_incident,
            call_fn_args=(),
            call_fn_kwargs=dict(
                incident_key=self.module.params.get("incident_key"),
                csi=self.module.params.get("csi"),
                update_incident_details=update_details,
                ocid=self.module.params.get("ocid"),
                homeregion=self.module.params.get("homeregion"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


IncidentHelperCustom = get_custom_class("IncidentHelperCustom")


class ResourceHelper(IncidentHelperCustom, IncidentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            problem_type=dict(
                type="str", choices=["LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT"]
            ),
            contacts=dict(
                type="list",
                elements="dict",
                options=dict(
                    contact_name=dict(type="str"),
                    contact_email=dict(type="str"),
                    contact_phone=dict(type="str"),
                    contact_type=dict(
                        type="str",
                        choices=[
                            "PRIMARY",
                            "ALTERNATE",
                            "SECONDARY",
                            "ADMIN",
                            "MANAGER",
                        ],
                    ),
                ),
            ),
            referrer=dict(type="str"),
            incident_key=dict(type="str", no_log=True),
            csi=dict(type="str"),
            ticket=dict(
                type="dict",
                required=True,
                options=dict(
                    severity=dict(type="str", choices=["HIGHEST", "HIGH", "MEDIUM"]),
                    resource_list=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            item=dict(
                                type="dict",
                                options=dict(
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=["tech", "limit"],
                                    ),
                                    category=dict(
                                        type="dict",
                                        options=dict(
                                            category_key=dict(type="str", no_log=True)
                                        ),
                                    ),
                                    sub_category=dict(
                                        type="dict",
                                        options=dict(
                                            sub_category_key=dict(
                                                type="str", no_log=True
                                            )
                                        ),
                                    ),
                                    issue_type=dict(
                                        type="dict",
                                        options=dict(
                                            issue_type_key=dict(type="str", no_log=True)
                                        ),
                                    ),
                                    name=dict(type="str"),
                                    current_limit=dict(type="int"),
                                    current_usage=dict(type="int"),
                                    requested_limit=dict(type="int"),
                                    limit_status=dict(
                                        type="str",
                                        choices=[
                                            "APPROVED",
                                            "PARTIALLY_APPROVED",
                                            "NOT_APPROVED",
                                        ],
                                    ),
                                ),
                            ),
                            region=dict(
                                type="str",
                                choices=[
                                    "DEV",
                                    "SEA",
                                    "INTEG_NEXT",
                                    "INTEG_STABLE",
                                    "PHX",
                                    "IAD",
                                    "FRA",
                                    "EU_FRANKFURT_1",
                                    "LHR",
                                    "YYZ",
                                    "NRT",
                                    "ICN",
                                    "BOM",
                                    "GRU",
                                    "SYD",
                                    "ZRH",
                                    "JED",
                                    "AMS",
                                    "KIX",
                                    "MEL",
                                    "YUL",
                                    "HYD",
                                    "YNY",
                                ],
                            ),
                            availability_domain=dict(
                                type="str",
                                choices=[
                                    "DEV_1",
                                    "DEV_2",
                                    "DEV_3",
                                    "INTEG_NEXT_1",
                                    "INTEG_STABLE_1",
                                    "SEA_AD_1",
                                    "SEA_AD_2",
                                    "SEA_AD_3",
                                    "PHX_AD_1",
                                    "PHX_AD_2",
                                    "PHX_AD_3",
                                    "US_ASHBURN_AD_1",
                                    "US_ASHBURN_AD_2",
                                    "US_ASHBURN_AD_3",
                                    "US_ASHBURN_AD_4",
                                    "EU_FRANKFURT_1_AD_1",
                                    "EU_FRANKFURT_1_AD_2",
                                    "EU_FRANKFURT_1_AD_3",
                                    "UK_LONDON_1_AD_1",
                                    "UK_LONDON_1_AD_2",
                                    "UK_LONDON_1_AD_3",
                                    "CA_TORONTO_1_AD_1",
                                    "AP_TOKYO_1_AD_1",
                                    "AP_SEOUL_1_AD_1",
                                    "AP_MUMBAI_1_AD_1",
                                    "SA_SAOPAULO_1_AD_1",
                                    "ME_JEDDAH_1_AD_1",
                                    "AP_OSAKA_1_AD_1",
                                    "AP_SYDNEY_1_AD_1",
                                    "EU_ZURICH_1_AD_1",
                                    "EU_AMSTERDAM_1_AD_1",
                                    "AP_MELBOURNE_1_AD_1",
                                    "CA_MONTREAL_1_AD_1",
                                    "AP_HYDERABAD_1_AD_1",
                                    "AP_CHUNCHEON_1_AD_1",
                                    "NO_AD",
                                ],
                            ),
                        ),
                    ),
                    title=dict(type="str"),
                    description=dict(type="str"),
                    contextual_data=dict(
                        type="dict",
                        options=dict(
                            client_id=dict(type="str", required=True),
                            schema_name=dict(type="str", required=True),
                            schema_version=dict(type="str", required=True),
                            payload=dict(type="str", required=True),
                        ),
                    ),
                    resource=dict(type="dict"),
                ),
            ),
            ocid=dict(type="str", required=True),
            homeregion=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="incident",
        service_client_class=IncidentClient,
        namespace="cims",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
