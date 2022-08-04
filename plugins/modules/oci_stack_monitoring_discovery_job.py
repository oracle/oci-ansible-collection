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
module: oci_stack_monitoring_discovery_job
short_description: Manage a DiscoveryJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a DiscoveryJob resource in Oracle Cloud Infrastructure
    - For I(state=present), aPI to create discovery Job and submit discovery Details to agent.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    discovery_type:
        description:
            - Add option submits new discovery Job. Add with retry option to re-submit failed discovery job. Refresh option refreshes the existing discovered
              resources.
        type: str
        choices:
            - "ADD"
            - "ADD_WITH_RETRY"
            - "REFRESH"
    discovery_client:
        description:
            - Client who submits discovery job.
        type: str
    compartment_id:
        description:
            - The OCID of Compartment
            - Required for create using I(state=present).
        type: str
    discovery_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            agent_id:
                description:
                    - The OCID of Management Agent
                type: str
                required: true
            resource_type:
                description:
                    - Resource Type.
                type: str
                choices:
                    - "WEBLOGIC_DOMAIN"
                    - "EBS_INSTANCE"
                    - "ORACLE_DATABASE"
                    - "OCI_ORACLE_DB"
                    - "OCI_ORACLE_CDB"
                    - "OCI_ORACLE_PDB"
                required: true
            resource_name:
                description:
                    - The Name of resource type
                type: str
                required: true
            properties:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    properties_map:
                        description:
                            - Key/Value pair of Property
                        type: dict
            credentials:
                description:
                    - ""
                type: dict
                suboptions:
                    items:
                        description:
                            - List of DiscoveryJob credentials.
                        type: list
                        elements: dict
                        required: true
                        suboptions:
                            credential_name:
                                description:
                                    - Name of Credential
                                type: str
                                required: true
                            credential_type:
                                description:
                                    - Name of Credential Type
                                type: str
                                required: true
                            properties:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    properties_map:
                                        description:
                                            - Key/Value pair of Property
                                        type: dict
            tags:
                description:
                    - ""
                type: dict
                suboptions:
                    properties_map:
                        description:
                            - Key/Value pair of Property
                        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
        type: dict
    discovery_job_id:
        description:
            - The Discovery Job ID
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DiscoveryJob.
            - Use I(state=present) to create a DiscoveryJob.
            - Use I(state=absent) to delete a DiscoveryJob.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create discovery_job
  oci_stack_monitoring_discovery_job:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    discovery_details:
      # required
      agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
      resource_type: WEBLOGIC_DOMAIN
      resource_name: resource_name_example
      properties:
        # optional
        properties_map: null
        # optional
      credentials:
        # required
        items:
        - # required
          credential_name: credential_name_example
          credential_type: credential_type_example
          properties:
            # optional
            properties_map: null
      tags:
        # optional
        properties_map: null

    # optional
    discovery_type: ADD
    discovery_client: discovery_client_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete discovery_job
  oci_stack_monitoring_discovery_job:
    # required
    discovery_job_id: "ocid1.discoveryjob.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
discovery_job:
    description:
        - Details of the DiscoveryJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of Discovery job
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the Compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        discovery_type:
            description:
                - Add option submits new discovery Job. Add with retry option to re-submit failed discovery job. Refresh option refreshes the existing
                  discovered resources.
            returned: on success
            type: str
            sample: ADD
        status:
            description:
                - Specifies the status of the discovery job
            returned: on success
            type: str
            sample: SUCCESS
        status_message:
            description:
                - The short summary of the status of the discovery job
            returned: on success
            type: str
            sample: status_message_example
        tenant_id:
            description:
                - The OCID of Tenant
            returned: on success
            type: str
            sample: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The OCID of user in which the job is submitted
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        discovery_client:
            description:
                - Client who submits discovery job.
            returned: on success
            type: str
            sample: discovery_client_example
        discovery_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                agent_id:
                    description:
                        - The OCID of Management Agent
                    returned: on success
                    type: str
                    sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
                resource_type:
                    description:
                        - Resource Type.
                    returned: on success
                    type: str
                    sample: WEBLOGIC_DOMAIN
                resource_name:
                    description:
                        - The Name of resource type
                    returned: on success
                    type: str
                    sample: resource_name_example
                properties:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        properties_map:
                            description:
                                - Key/Value pair of Property
                            returned: on success
                            type: dict
                            sample: {}
                credentials:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        items:
                            description:
                                - List of DiscoveryJob credentials.
                            returned: on success
                            type: complex
                            contains:
                                credential_name:
                                    description:
                                        - Name of Credential
                                    returned: on success
                                    type: str
                                    sample: credential_name_example
                                credential_type:
                                    description:
                                        - Name of Credential Type
                                    returned: on success
                                    type: str
                                    sample: credential_type_example
                                properties:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        properties_map:
                                            description:
                                                - Key/Value pair of Property
                                            returned: on success
                                            type: dict
                                            sample: {}
                tags:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        properties_map:
                            description:
                                - Key/Value pair of Property
                            returned: on success
                            type: dict
                            sample: {}
        time_updated:
            description:
                - The time the discovery Job was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the DiscoveryJob Resource.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "discovery_type": "ADD",
        "status": "SUCCESS",
        "status_message": "status_message_example",
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "discovery_client": "discovery_client_example",
        "discovery_details": {
            "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
            "resource_type": "WEBLOGIC_DOMAIN",
            "resource_name": "resource_name_example",
            "properties": {
                "properties_map": {}
            },
            "credentials": {
                "items": [{
                    "credential_name": "credential_name_example",
                    "credential_type": "credential_type_example",
                    "properties": {
                        "properties_map": {}
                    }
                }]
            },
            "tags": {
                "properties_map": {}
            }
        },
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.stack_monitoring import StackMonitoringClient
    from oci.stack_monitoring.models import CreateDiscoveryJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DiscoveryJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DiscoveryJobHelperGen, self).get_possible_entity_types() + [
            "discoveryjob",
            "discoveryjobs",
            "stackMonitoringdiscoveryjob",
            "stackMonitoringdiscoveryjobs",
            "discoveryjobresource",
            "discoveryjobsresource",
            "stackmonitoring",
        ]

    def get_module_resource_id_param(self):
        return "discovery_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("discovery_job_id")

    def get_get_fn(self):
        return self.client.get_discovery_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_discovery_job, discovery_job_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_discovery_job,
            discovery_job_id=self.module.params.get("discovery_job_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_discovery_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateDiscoveryJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_discovery_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_discovery_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_discovery_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                discovery_job_id=self.module.params.get("discovery_job_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DiscoveryJobHelperCustom = get_custom_class("DiscoveryJobHelperCustom")


class ResourceHelper(DiscoveryJobHelperCustom, DiscoveryJobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            discovery_type=dict(
                type="str", choices=["ADD", "ADD_WITH_RETRY", "REFRESH"]
            ),
            discovery_client=dict(type="str"),
            compartment_id=dict(type="str"),
            discovery_details=dict(
                type="dict",
                options=dict(
                    agent_id=dict(type="str", required=True),
                    resource_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "WEBLOGIC_DOMAIN",
                            "EBS_INSTANCE",
                            "ORACLE_DATABASE",
                            "OCI_ORACLE_DB",
                            "OCI_ORACLE_CDB",
                            "OCI_ORACLE_PDB",
                        ],
                    ),
                    resource_name=dict(type="str", required=True),
                    properties=dict(
                        type="dict",
                        required=True,
                        options=dict(properties_map=dict(type="dict")),
                    ),
                    credentials=dict(
                        type="dict",
                        options=dict(
                            items=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    credential_name=dict(type="str", required=True),
                                    credential_type=dict(type="str", required=True),
                                    properties=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(properties_map=dict(type="dict")),
                                    ),
                                ),
                            )
                        ),
                    ),
                    tags=dict(
                        type="dict", options=dict(properties_map=dict(type="dict"))
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            discovery_job_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="discovery_job",
        service_client_class=StackMonitoringClient,
        namespace="stack_monitoring",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
