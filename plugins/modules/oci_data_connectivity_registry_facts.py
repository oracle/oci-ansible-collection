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
module: oci_data_connectivity_registry_facts
short_description: Fetches details about one or multiple Registry resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Registry resources in Oracle Cloud Infrastructure
    - Retrieves a list of Data Connectivity Management registries.
    - If I(registry_id) is specified, the details of a single Registry will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry OCID.
            - Required to get a specific registry.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment containing the resources you want to list.
            - Required to list multiple registries.
        type: str
    name:
        description:
            - Used to filter by the name of the object.
        type: str
    is_deep_lookup:
        description:
            - This parameter allows list registries to deep look at the whole tenancy.
        type: bool
    lifecycle_state:
        description:
            - Lifecycle state of the resource.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "STARTING"
            - "STOPPING"
            - "STOPPED"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific registry
  oci_data_connectivity_registry_facts:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

- name: List registries
  oci_data_connectivity_registry_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    is_deep_lookup: true
    lifecycle_state: CREATING

"""

RETURN = """
registries:
    description:
        - List of Registry resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - A unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Registry description
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Data Connectivity Management registry display name; registries can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Time when the Data Connectivity Management registry was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time when the Data Connectivity Management registry was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        updated_by:
            description:
                - Name of the user who updated the DCMS registry.
            returned: on success
            type: str
            sample: updated_by_example
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        lifecycle_state:
            description:
                - "Lifecycle states for registries in the Data Connectivity Management Service
                  CREATING - The resource is being created and may not be usable until the entire metadata is defined.
                  UPDATING - The resource is being updated and may not be usable until all changes are commited.
                  DELETING - The resource is being deleted and might require deep cleanup of children.
                  ACTIVE   - The resource is valid and available for access.
                  INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                           administrative reasons.
                  DELETED  - The resource has been deleted and isn't available.
                  FAILED   - The resource is in a failed state due to validation or other errors."
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "updated_by": "updated_by_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RegistryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "registry_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_registry, registry_id=self.module.params.get("registry_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "is_deep_lookup",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_registries,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


RegistryFactsHelperCustom = get_custom_class("RegistryFactsHelperCustom")


class ResourceFactsHelper(RegistryFactsHelperCustom, RegistryFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            registry_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            is_deep_lookup=dict(type="bool"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "STARTING",
                    "STOPPING",
                    "STOPPED",
                ],
            ),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="registry",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(registries=result)


if __name__ == "__main__":
    main()
