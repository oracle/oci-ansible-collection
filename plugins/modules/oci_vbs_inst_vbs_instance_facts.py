#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_vbs_inst_vbs_instance_facts
short_description: Fetches details about one or multiple VbsInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VbsInstance resources in Oracle Cloud Infrastructure
    - Returns a list of VbsInstances.
    - If I(vbs_instance_id) is specified, the details of a single VbsInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vbs_instance_id:
        description:
            - unique VbsInstance identifier
            - Required to get a specific vbs_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple vbs_instances.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    name:
        description:
            - A filter to return only resources that match the entire name given.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific vbs_instance
  oci_vbs_inst_vbs_instance_facts:
    # required
    vbs_instance_id: "ocid1.vbsinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List vbs_instances
  oci_vbs_inst_vbs_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    name: name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
vbs_instances:
    description:
        - List of VbsInstance resources
    returned: on success
    type: complex
    contains:
        resource_compartment_id:
            description:
                - Compartment where VBS may create additional resources for the service instance
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
        vbs_access_url:
            description:
                - Public web URL for accessing the VBS service instance
                - Returned for get operation
            returned: on success
            type: str
            sample: vbs_access_url_example
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecyle_details_example
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Service instance name (unique identifier)
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Service instance display name
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment of the service instance
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_resource_usage_agreement_granted:
            description:
                - Whether the VBS service instance owner explicitly approved VBS to create and use resources in the customer tenancy
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the the VbsInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the VbsInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the VbsInstance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        "resource_compartment_id": "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vbs_access_url": "vbs_access_url_example",
        "lifecyle_details": "lifecyle_details_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_resource_usage_agreement_granted": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.vbs_inst import VbsInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VbsInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "vbs_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vbs_instance,
            vbs_instance_id=self.module.params.get("vbs_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "name",
            "sort_order",
            "sort_by",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_vbs_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VbsInstanceFactsHelperCustom = get_custom_class("VbsInstanceFactsHelperCustom")


class ResourceFactsHelper(VbsInstanceFactsHelperCustom, VbsInstanceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vbs_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vbs_instance",
        service_client_class=VbsInstanceClient,
        namespace="vbs_inst",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vbs_instances=result)


if __name__ == "__main__":
    main()
