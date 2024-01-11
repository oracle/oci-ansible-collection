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
module: oci_cims_incident_resource_type_facts
short_description: Fetches details about one or multiple IncidentResourceType resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple IncidentResourceType resources in Oracle Cloud Infrastructure
    - During support ticket creation, returns the list of all possible products that Oracle Cloud Infrastructure supports.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    problem_type:
        description:
            - The kind of support request.
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the tenancy.
        type: str
        required: true
    csi:
        description:
            - The Customer Support Identifier associated with the support account.
        type: str
        required: true
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
    name:
        description:
            - The user-friendly name of the incident type.
        type: str
    homeregion:
        description:
            - The region of the tenancy.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List incident_resource_types
  oci_cims_incident_resource_type_facts:
    # required
    problem_type: problem_type_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    csi: csi_example
    ocid: ocid_example

    # optional
    sort_by: dateUpdated
    sort_order: ASC
    name: name_example
    homeregion: us-phoenix-1

"""

RETURN = """
incident_resource_types:
    description:
        - List of IncidentResourceType resources
    returned: on success
    type: complex
    contains:
        resource_type_key:
            description:
                - Unique identifier of the resource.
            returned: on success
            type: str
            sample: resource_type_key_example
        name:
            description:
                - The display name of the resource.
            returned: on success
            type: str
            sample: name_example
        label:
            description:
                - The label associated with the resource.
            returned: on success
            type: str
            sample: label_example
        description:
            description:
                - The description of the resource.
            returned: on success
            type: str
            sample: description_example
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
    sample: [{
        "resource_type_key": "resource_type_key_example",
        "name": "name_example",
        "label": "label_example",
        "description": "description_example",
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


class IncidentResourceTypeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "problem_type",
            "compartment_id",
            "csi",
            "ocid",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
            "homeregion",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_incident_resource_types,
            problem_type=self.module.params.get("problem_type"),
            compartment_id=self.module.params.get("compartment_id"),
            csi=self.module.params.get("csi"),
            ocid=self.module.params.get("ocid"),
            **optional_kwargs
        )


IncidentResourceTypeFactsHelperCustom = get_custom_class(
    "IncidentResourceTypeFactsHelperCustom"
)


class ResourceFactsHelper(
    IncidentResourceTypeFactsHelperCustom, IncidentResourceTypeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            problem_type=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            csi=dict(type="str", required=True),
            ocid=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["dateUpdated", "severity"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
            homeregion=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="incident_resource_type",
        service_client_class=IncidentClient,
        namespace="cims",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(incident_resource_types=result)


if __name__ == "__main__":
    main()
