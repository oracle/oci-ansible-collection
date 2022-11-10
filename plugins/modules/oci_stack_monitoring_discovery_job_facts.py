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
module: oci_stack_monitoring_discovery_job_facts
short_description: Fetches details about one or multiple DiscoveryJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DiscoveryJob resources in Oracle Cloud Infrastructure
    - API to get the details of all Discovery Jobs.
    - If I(discovery_job_id) is specified, the details of a single DiscoveryJob will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    discovery_job_id:
        description:
            - The Discovery Job ID
            - Required to get a specific discovery_job.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which data is listed.
            - Required to list multiple discovery_jobs.
        type: str
    name:
        description:
            - A filter to return only discovery jobs that match the entire resource name given.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeUpdated is descending. Default order for resourceName is
              ascending.
        type: str
        choices:
            - "timeUpdated"
            - "resourceName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific discovery_job
  oci_stack_monitoring_discovery_job_facts:
    # required
    discovery_job_id: "ocid1.discoveryjob.oc1..xxxxxxEXAMPLExxxxxx"

- name: List discovery_jobs
  oci_stack_monitoring_discovery_job_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: timeUpdated

"""

RETURN = """
discovery_jobs:
    description:
        - List of DiscoveryJob resources
    returned: on success
    type: complex
    contains:
        discovery_client:
            description:
                - Client who submits discovery job.
                - Returned for get operation
            returned: on success
            type: str
            sample: discovery_client_example
        discovery_details:
            description:
                - ""
                - Returned for get operation
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
        id:
            description:
                - The OCID of Discovery job
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        resource_type:
            description:
                - Resource Type
                - Returned for list operation
            returned: on success
            type: str
            sample: WEBLOGIC_DOMAIN
        resource_name:
            description:
                - The name of resource type
                - Returned for list operation
            returned: on success
            type: str
            sample: resource_name_example
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
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_type": "WEBLOGIC_DOMAIN",
        "resource_name": "resource_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "discovery_type": "ADD",
        "status": "SUCCESS",
        "status_message": "status_message_example",
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.stack_monitoring import StackMonitoringClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DiscoveryJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "discovery_job_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_discovery_job,
            discovery_job_id=self.module.params.get("discovery_job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_discovery_jobs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DiscoveryJobFactsHelperCustom = get_custom_class("DiscoveryJobFactsHelperCustom")


class ResourceFactsHelper(DiscoveryJobFactsHelperCustom, DiscoveryJobFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            discovery_job_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeUpdated", "resourceName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="discovery_job",
        service_client_class=StackMonitoringClient,
        namespace="stack_monitoring",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(discovery_jobs=result)


if __name__ == "__main__":
    main()
