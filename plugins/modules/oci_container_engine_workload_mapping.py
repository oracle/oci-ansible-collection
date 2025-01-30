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
module: oci_container_engine_workload_mapping
short_description: Manage a WorkloadMapping resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a WorkloadMapping resource in Oracle Cloud Infrastructure
    - For I(state=present), create the specified workloadMapping for a cluster.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace:
        description:
            - The namespace of the workloadMapping.
            - Required for create using I(state=present).
        type: str
    mapped_compartment_id:
        description:
            - The OCID of the mapped customer compartment.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    workload_mapping_id:
        description:
            - The OCID of the workloadMapping.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the WorkloadMapping.
            - Use I(state=present) to create or update a WorkloadMapping.
            - Use I(state=absent) to delete a WorkloadMapping.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create workload_mapping
  oci_container_engine_workload_mapping:
    # required
    namespace: namespace_example
    mapped_compartment_id: "ocid1.mappedcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update workload_mapping
  oci_container_engine_workload_mapping:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    workload_mapping_id: "ocid1.workloadmapping.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    mapped_compartment_id: "ocid1.mappedcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete workload_mapping
  oci_container_engine_workload_mapping:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    workload_mapping_id: "ocid1.workloadmapping.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
workload_mapping:
    description:
        - Details of the WorkloadMapping resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The ocid of the workloadMapping.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_id:
            description:
                - The OCID of the cluster.
            returned: on success
            type: str
            sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - The namespace of the workloadMapping.
            returned: on success
            type: str
            sample: namespace_example
        mapped_tenancy_id:
            description:
                - The OCID of the mapped customer tenancy.
            returned: on success
            type: str
            sample: "ocid1.mappedtenancy.oc1..xxxxxxEXAMPLExxxxxx"
        mapped_compartment_id:
            description:
                - The OCID of the mapped customer compartment.
            returned: on success
            type: str
            sample: "ocid1.mappedcompartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the workloadMapping.
            returned: on success
            type: str
            sample: CREATING
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "mapped_tenancy_id": "ocid1.mappedtenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "mapped_compartment_id": "ocid1.mappedcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import CreateWorkloadMappingDetails
    from oci.container_engine.models import UpdateWorkloadMappingDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WorkloadMappingHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(WorkloadMappingHelperGen, self).get_possible_entity_types() + [
            "workloadmapping",
            "workloadmappings",
            "containerEngineworkloadmapping",
            "containerEngineworkloadmappings",
            "workloadmappingresource",
            "workloadmappingsresource",
            "containerengine",
        ]

    def get_module_resource_id_param(self):
        return "workload_mapping_id"

    def get_module_resource_id(self):
        return self.module.params.get("workload_mapping_id")

    def get_get_fn(self):
        return self.client.get_workload_mapping

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_workload_mapping,
            workload_mapping_id=summary_model.id,
            cluster_id=self.module.params.get("cluster_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_workload_mapping,
            cluster_id=self.module.params.get("cluster_id"),
            workload_mapping_id=self.module.params.get("workload_mapping_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "cluster_id",
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
            self.client.list_workload_mappings, **kwargs
        )

    def get_create_model_class(self):
        return CreateWorkloadMappingDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_workload_mapping,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                create_workload_mapping_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateWorkloadMappingDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_workload_mapping,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                workload_mapping_id=self.module.params.get("workload_mapping_id"),
                update_workload_mapping_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_workload_mapping,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cluster_id=self.module.params.get("cluster_id"),
                workload_mapping_id=self.module.params.get("workload_mapping_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


WorkloadMappingHelperCustom = get_custom_class("WorkloadMappingHelperCustom")


class ResourceHelper(WorkloadMappingHelperCustom, WorkloadMappingHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            namespace=dict(type="str"),
            mapped_compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            cluster_id=dict(type="str", required=True),
            workload_mapping_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="workload_mapping",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
