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
module: oci_cims_incident_facts
short_description: Fetches details about one or multiple Incident resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Incident resources in Oracle Cloud Infrastructure
    - Returns the list of support tickets raised by the tenancy.
    - If I(incident_key) is specified, the details of a single Incident will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    incident_key:
        description:
            - Unique identifier for the support ticket.
            - Required to get a specific incident.
        type: str
    csi:
        description:
            - The Customer Support Identifier associated with the support account.
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the tenancy.
            - Required to list multiple incidents.
        type: str
    ocid:
        description:
            - User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.
        type: str
        required: true
    sort_by:
        description:
            - The key to use to sort the returned items.
        type: str
        choices:
            - "dateUpdated"
            - "severity"
    sort_order:
        description:
            - The order to sort the results in.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - The current state of the ticket.
        type: str
        choices:
            - "ACTIVE"
            - "CLOSED"
    homeregion:
        description:
            - The region of the tenancy.
        type: str
    problem_type:
        description:
            - The kind of support request.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific incident
  oci_cims_incident_facts:
    # required
    incident_key: incident_key_example
    csi: csi_example
    ocid: ocid_example

    # optional
    homeregion: us-phoenix-1
    problem_type: problem_type_example

- name: List incidents
  oci_cims_incident_facts:
    # required
    csi: csi_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    ocid: ocid_example

    # optional
    sort_by: dateUpdated
    sort_order: ASC
    lifecycle_state: ACTIVE
    homeregion: us-phoenix-1
    problem_type: problem_type_example

"""

RETURN = """
incidents:
    description:
        - List of Incident resources
    returned: on success
    type: complex
    contains:
        referrer:
            description:
                - The incident referrer. This value is often the URL that the customer used when creating the support ticket.
                - Returned for get operation
            returned: on success
            type: str
            sample: referrer_example
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
                resource_type_key:
                    description:
                        - Unique identifier of the resource.
                    returned: on success
                    type: str
                    sample: resource_type_key_example
                service_category_list:
                    description:
                        - The service category list.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique ID that identifies a classifier.
                            returned: on success
                            type: str
                            sample: key_example
                        name:
                            description:
                                - The name of the classifier.
                            returned: on success
                            type: str
                            sample: name_example
                        label:
                            description:
                                - The label for the classifier.
                            returned: on success
                            type: str
                            sample: label_example
                        description:
                            description:
                                - The text describing the classifier.
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
                                - The scope of the incident.
                            returned: on success
                            type: str
                            sample: AD
                        unit:
                            description:
                                - The unit to use to measure the service category or resource.
                            returned: on success
                            type: str
                            sample: COUNT
                        limit_id:
                            description:
                                - The unique ID for the limit.
                            returned: on success
                            type: str
                            sample: "ocid1.limit.oc1..xxxxxxEXAMPLExxxxxx"
        problem_type:
            description:
                - The kind of support ticket, such as a technical support request.
            returned: on success
            type: str
            sample: LIMIT
    sample: [{
        "referrer": "referrer_example",
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
            }],
            "resource_type_key": "resource_type_key_example",
            "service_category_list": [{
                "key": "key_example",
                "name": "name_example",
                "label": "label_example",
                "description": "description_example",
                "issue_type_list": [{
                    "issue_type_key": "issue_type_key_example",
                    "label": "label_example"
                }],
                "scope": "AD",
                "unit": "COUNT",
                "limit_id": "ocid1.limit.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "problem_type": "LIMIT"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cims import IncidentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IncidentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "incident_key",
            "csi",
            "ocid",
        ]

    def get_required_params_for_list(self):
        return [
            "csi",
            "compartment_id",
            "ocid",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "homeregion",
            "problem_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_incident,
            incident_key=self.module.params.get("incident_key"),
            csi=self.module.params.get("csi"),
            ocid=self.module.params.get("ocid"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "homeregion",
            "problem_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_incidents,
            csi=self.module.params.get("csi"),
            compartment_id=self.module.params.get("compartment_id"),
            ocid=self.module.params.get("ocid"),
            **optional_kwargs
        )


IncidentFactsHelperCustom = get_custom_class("IncidentFactsHelperCustom")


class ResourceFactsHelper(IncidentFactsHelperCustom, IncidentFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            incident_key=dict(type="str", no_log=True),
            csi=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            ocid=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["dateUpdated", "severity"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "CLOSED"]),
            homeregion=dict(type="str"),
            problem_type=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="incident",
        service_client_class=IncidentClient,
        namespace="cims",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(incidents=result)


if __name__ == "__main__":
    main()
