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
module: oci_opsi_host_insight
short_description: Manage a HostInsight resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a HostInsight resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric
      collection and analysis will be started.
    - "This resource has the following action operations in the M(oci_host_insight_actions) module: change_compartment, disable, enable."
version_added: "2.9"
author: Oracle (@oracle)
options:
    entity_source:
        description:
            - Source of the host entity.
            - Required for create using I(state=present), update using I(state=present) with host_insight_id present.
        type: str
        choices:
            - "MACS_MANAGED_EXTERNAL_HOST"
    compartment_id:
        description:
            - Compartment Identifier of host
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    management_agent_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Management Agent
            - Required for create using I(state=present).
        type: str
    host_insight_id:
        description:
            - Unique host insight identifier
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the HostInsight.
            - Use I(state=present) to create or update a HostInsight.
            - Use I(state=absent) to delete a HostInsight.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create host_insight
  oci_opsi_host_insight:
    entity_source: MACS_MANAGED_EXTERNAL_HOST
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    management_agent_id: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update host_insight
  oci_opsi_host_insight:
    entity_source: MACS_MANAGED_EXTERNAL_HOST
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    management_agent_id: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
    host_insight_id: "ocid1.hostinsight.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete host_insight
  oci_opsi_host_insight:
    host_insight_id: "ocid1.hostinsight.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
host_insight:
    description:
        - Details of the HostInsight resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        entity_source:
            description:
                - Source of the host entity.
            returned: on success
            type: string
            sample: MACS_MANAGED_EXTERNAL_HOST
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host insight resource.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        host_name:
            description:
                - The host name. The host name is unique amongst the hosts managed by the same management agent.
            returned: on success
            type: string
            sample: host_name_example
        host_display_name:
            description:
                - The user-friendly name for the host. The name does not have to be unique.
            returned: on success
            type: string
            sample: host_display_name_example
        host_type:
            description:
                - Operations Insights internal representation of the host type. Possible value is EXTERNAL-HOST.
            returned: on success
            type: string
            sample: host_type_example
        processor_count:
            description:
                - Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.
            returned: on success
            type: int
            sample: 56
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        status:
            description:
                - Indicates the status of a host insight in Operations Insights
            returned: on success
            type: string
            sample: ENABLED
        time_created:
            description:
                - The time the the host insight was first enabled. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the host insight was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the host.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        management_agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Management Agent
            returned: on success
            type: string
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        platform_name:
            description:
                - Platform name.
            returned: on success
            type: string
            sample: platform_name_example
        platform_type:
            description:
                - Platform type.
            returned: on success
            type: string
            sample: LINUX
        platform_version:
            description:
                - Platform version.
            returned: on success
            type: string
            sample: platform_version_example
    sample: {
        "entity_source": "MACS_MANAGED_EXTERNAL_HOST",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "host_name": "host_name_example",
        "host_display_name": "host_display_name_example",
        "host_type": "host_type_example",
        "processor_count": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "status": "ENABLED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "platform_name": "platform_name_example",
        "platform_type": "LINUX",
        "platform_version": "platform_version_example"
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateHostInsightDetails
    from oci.opsi.models import UpdateHostInsightDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HostInsightHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "host_insight_id"

    def get_module_resource_id(self):
        return self.module.params.get("host_insight_id")

    def get_get_fn(self):
        return self.client.get_host_insight

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_host_insight,
            host_insight_id=self.module.params.get("host_insight_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id"]

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
            self.client.list_host_insights, **kwargs
        )

    def get_create_model_class(self):
        return CreateHostInsightDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_host_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(create_host_insight_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateHostInsightDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_host_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                host_insight_id=self.module.params.get("host_insight_id"),
                update_host_insight_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_host_insight,
            call_fn_args=(),
            call_fn_kwargs=dict(
                host_insight_id=self.module.params.get("host_insight_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


HostInsightHelperCustom = get_custom_class("HostInsightHelperCustom")


class ResourceHelper(HostInsightHelperCustom, HostInsightHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            entity_source=dict(type="str", choices=["MACS_MANAGED_EXTERNAL_HOST"]),
            compartment_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            management_agent_id=dict(type="str"),
            host_insight_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="host_insight",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
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
