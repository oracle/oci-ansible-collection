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
module: oci_adm_knowledge_base_facts
short_description: Fetches details about one or multiple KnowledgeBase resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple KnowledgeBase resources in Oracle Cloud Infrastructure
    - Returns a list of KnowledgeBases based on the specified query parameters.
      At least id or compartmentId query parameter must be provided.
    - If I(knowledge_base_id) is specified, the details of a single KnowledgeBase will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    knowledge_base_id:
        description:
            - The Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of a Knowledge Base, as a URL path
              parameter.
            - Required to get a specific knowledge_base.
        type: str
        aliases: ["id"]
    sort_by:
        description:
            - "The field used to sort Knowledge Bases. Only one sort order is allowed.
              Default order for _displayName_ is **ascending alphabetical order**.
              Default order for _lifecyleState_ is the following sequence: **CREATING, ACTIVE, UPDATING, FAILED, DELETING, and DELETED**.Default order for
              _timeCreated_ is **descending**.
              Default order for _timeUpdated_ is **descending**."
        type: str
        choices:
            - "DISPLAY_NAME"
            - "LIFECYCLE_STATE"
            - "TIME_CREATED"
            - "TIME_UPDATED"
    lifecycle_state:
        description:
            - A filter to return only Knowledge Bases that match the specified lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "FAILED"
            - "DELETING"
            - "DELETED"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - A filter to return only resources that belong to the specified compartment identifier.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific knowledge_base
  oci_adm_knowledge_base_facts:
    # required
    knowledge_base_id: "ocid1.knowledgebase.oc1..xxxxxxEXAMPLExxxxxx"

- name: List knowledge_bases
  oci_adm_knowledge_base_facts:

    # optional
    sort_by: DISPLAY_NAME
    lifecycle_state: CREATING
    sort_order: ASC
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
knowledge_bases:
    description:
        - List of KnowledgeBase resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the Knowledge Base.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the Knowledge Base.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The creation date and time of the Knowledge Base (formatted according to L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the Knowledge Base was last updated (formatted according to L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        compartment_id:
            description:
                - The Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)) of the Knowledge Base's
                  compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the Knowledge Base.
            returned: on success
            type: str
            sample: CREATING
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.adm import ApplicationDependencyManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KnowledgeBaseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "knowledge_base_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_knowledge_base,
            knowledge_base_id=self.module.params.get("knowledge_base_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "lifecycle_state",
            "sort_order",
            "display_name",
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_knowledge_bases, **optional_kwargs
        )


KnowledgeBaseFactsHelperCustom = get_custom_class("KnowledgeBaseFactsHelperCustom")


class ResourceFactsHelper(KnowledgeBaseFactsHelperCustom, KnowledgeBaseFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            knowledge_base_id=dict(aliases=["id"], type="str"),
            sort_by=dict(
                type="str",
                choices=[
                    "DISPLAY_NAME",
                    "LIFECYCLE_STATE",
                    "TIME_CREATED",
                    "TIME_UPDATED",
                ],
            ),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "FAILED",
                    "DELETING",
                    "DELETED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="knowledge_base",
        service_client_class=ApplicationDependencyManagementClient,
        namespace="adm",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(knowledge_bases=result)


if __name__ == "__main__":
    main()
