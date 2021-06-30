#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_golden_gate_deployment_backup
short_description: Manage a DeploymentBackup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DeploymentBackup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new DeploymentBackup.
    - "This resource has the following action operations in the M(oci_deployment_backup_actions) module: change_compartment, restore_deployment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - An object's Display Name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    deployment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            - Required for create using I(state=present).
        type: str
    namespace_name:
        description:
            - Name of namespace that serves as a container for all of your buckets
            - Required for create using I(state=present).
        type: str
    bucket_name:
        description:
            - Name of the bucket where the object is to be uploaded in the object storage
            - Required for create using I(state=present).
        type: str
    object_name:
        description:
            - Name of the object to be uploaded to object storage
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - "A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Tags defined for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    deployment_backup_id:
        description:
            - A unique DeploymentBackup identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DeploymentBackup.
            - Use I(state=present) to create or update a DeploymentBackup.
            - Use I(state=absent) to delete a DeploymentBackup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deployment_backup
  oci_golden_gate_deployment_backup:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_name: namespace_name_example
    bucket_name: bucket_name_example
    object_name: object_name_example

- name: Update deployment_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_golden_gate_deployment_backup:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deployment_backup
  oci_golden_gate_deployment_backup:
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    deployment_backup_id: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete deployment_backup
  oci_golden_gate_deployment_backup:
    deployment_backup_id: "ocid1.deploymentbackup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete deployment_backup using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_golden_gate_deployment_backup:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
deployment_backup:
    description:
        - Details of the DeploymentBackup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup being referenced.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: string
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - An object's Display Name.
            returned: on success
            type: string
            sample: display_name_example
        is_automatic:
            description:
                - True if this object is automatically created
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - Possible lifecycle states.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_of_backup:
            description:
                - The time of the resource backup. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        backup_type:
            description:
                - Possible Deployment backup types.
            returned: on success
            type: string
            sample: INCREMENTAL
        ogg_version:
            description:
                - Version of OGG
            returned: on success
            type: string
            sample: ogg_version_example
        namespace_name:
            description:
                - Name of namespace that serves as a container for all of your buckets
            returned: on success
            type: string
            sample: namespace_name_example
        bucket_name:
            description:
                - Name of the bucket where the object is to be uploaded in the object storage
            returned: on success
            type: string
            sample: bucket_name_example
        object_name:
            description:
                - Name of the object to be uploaded to object storage
            returned: on success
            type: string
            sample: object_name_example
        time_created:
            description:
                - The time the resource was created. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by L(RFC3339,https://tools.ietf.org/html/rfc3339), such as
                  `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        freeform_tags:
            description:
                - "A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Tags defined for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is
                  predefined and scoped to namespaces.  For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "is_automatic": true,
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_of_backup": "2013-10-20T19:20:30+01:00",
        "backup_type": "INCREMENTAL",
        "ogg_version": "ogg_version_example",
        "namespace_name": "namespace_name_example",
        "bucket_name": "bucket_name_example",
        "object_name": "object_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CreateDeploymentBackupDetails
    from oci.golden_gate.models import UpdateDeploymentBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentBackupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "deployment_backup_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_backup_id")

    def get_get_fn(self):
        return self.client.get_deployment_backup

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment_backup,
            deployment_backup_id=self.module.params.get("deployment_backup_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["deployment_id", "display_name"]

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
        return oci_common_utils.list_all_resources(
            self.client.list_deployment_backups, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeploymentBackupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deployment_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deployment_backup_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeploymentBackupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deployment_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_backup_id=self.module.params.get("deployment_backup_id"),
                update_deployment_backup_details=update_details,
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
            call_fn=self.client.delete_deployment_backup,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_backup_id=self.module.params.get("deployment_backup_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DeploymentBackupHelperCustom = get_custom_class("DeploymentBackupHelperCustom")


class ResourceHelper(DeploymentBackupHelperCustom, DeploymentBackupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            deployment_id=dict(type="str"),
            namespace_name=dict(type="str"),
            bucket_name=dict(type="str"),
            object_name=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            deployment_backup_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment_backup",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
