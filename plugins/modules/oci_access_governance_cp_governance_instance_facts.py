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
module: oci_access_governance_cp_governance_instance_facts
short_description: Fetches details about one or multiple GovernanceInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple GovernanceInstance resources in Oracle Cloud Infrastructure
    - Returns a list of Governance Instances.
    - If I(governance_instance_id) is specified, the details of a single GovernanceInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    governance_instance_id:
        description:
            - The OCID of the GovernanceInstance
            - Required to get a specific governance_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment in which resources are listed.
            - Required to list multiple governance_instances.
        type: str
    lifecycle_state:
        description:
            - The lifecycle state to filter on.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
            - "timeUpdated"
            - "lifecycleState"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific governance_instance
  oci_access_governance_cp_governance_instance_facts:
    # required
    governance_instance_id: "ocid1.governanceinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List governance_instances
  oci_access_governance_cp_governance_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: lifecycle_state_example
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
governance_instances:
    description:
        - List of GovernanceInstance resources
    returned: on success
    type: complex
    contains:
        tenancy_namespace:
            description:
                - The namespace for tenancy object storage.
                - Returned for get operation
            returned: on success
            type: str
            sample: tenancy_namespace_example
        id:
            description:
                - The unique OCID of the GovernanceInstance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name for the GovernanceInstance.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the GovernanceInstance.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment where the GovernanceInstance resides.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the GovernanceInstance was created in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the GovernanceInstance was updated in an RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the GovernanceInstance.
            returned: on success
            type: str
            sample: CREATING
        license_type:
            description:
                - The licenseType being used.
            returned: on success
            type: str
            sample: NEW_LICENSE
        instance_url:
            description:
                - The access URL of the GovernanceInstance.
            returned: on success
            type: str
            sample: instance_url_example
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "tenancy_namespace": "tenancy_namespace_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "license_type": "NEW_LICENSE",
        "instance_url": "instance_url_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
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
    from oci.access_governance_cp import AccessGovernanceCPClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GovernanceInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "governance_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_governance_instance,
            governance_instance_id=self.module.params.get("governance_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_governance_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


GovernanceInstanceFactsHelperCustom = get_custom_class(
    "GovernanceInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    GovernanceInstanceFactsHelperCustom, GovernanceInstanceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            governance_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["timeCreated", "displayName", "timeUpdated", "lifecycleState"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="governance_instance",
        service_client_class=AccessGovernanceCPClient,
        namespace="access_governance_cp",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(governance_instances=result)


if __name__ == "__main__":
    main()
