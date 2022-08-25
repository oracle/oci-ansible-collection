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
module: oci_apm_synthetics_dedicated_vantage_point
short_description: Manage a DedicatedVantagePoint resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DedicatedVantagePoint resource in Oracle Cloud Infrastructure
    - For I(state=present), registers a new dedicated vantage point.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    status:
        description:
            - Status of the dedicated vantage point.
            - This parameter is updatable.
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
    dvp_stack_details:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            dvp_stack_type:
                description:
                    - Type of stack.
                type: str
                choices:
                    - "ORACLE_RM_STACK"
                required: true
            dvp_version:
                description:
                    - Version of the dedicated vantage point.
                type: str
                required: true
            dvp_stack_id:
                description:
                    - Stack L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Resource Manager stack for dedicated vantage
                      point.
                type: str
                required: true
            dvp_stream_id:
                description:
                    - Stream L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Resource Manager stack for dedicated vantage
                      point.
                type: str
                required: true
    region:
        description:
            - Name of the region.
            - Required for create using I(state=present).
            - This parameter is updatable.
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
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    dedicated_vantage_point_id:
        description:
            - The OCID of the dedicated vantage point.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DedicatedVantagePoint.
            - Use I(state=present) to create or update a DedicatedVantagePoint.
            - Use I(state=absent) to delete a DedicatedVantagePoint.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create dedicated_vantage_point
  oci_apm_synthetics_dedicated_vantage_point:
    # required
    display_name: display_name_example
    dvp_stack_details:
      # required
      dvp_stack_type: ORACLE_RM_STACK
      dvp_version: dvp_version_example
      dvp_stack_id: "ocid1.dvpstack.oc1..xxxxxxEXAMPLExxxxxx"
      dvp_stream_id: "ocid1.dvpstream.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    status: ENABLED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dedicated_vantage_point
  oci_apm_synthetics_dedicated_vantage_point:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    dedicated_vantage_point_id: "ocid1.dedicatedvantagepoint.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    status: ENABLED
    dvp_stack_details:
      # required
      dvp_stack_type: ORACLE_RM_STACK
      dvp_version: dvp_version_example
      dvp_stack_id: "ocid1.dvpstack.oc1..xxxxxxEXAMPLExxxxxx"
      dvp_stream_id: "ocid1.dvpstream.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dedicated_vantage_point using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apm_synthetics_dedicated_vantage_point:
    # required
    display_name: display_name_example
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    status: ENABLED
    dvp_stack_details:
      # required
      dvp_stack_type: ORACLE_RM_STACK
      dvp_version: dvp_version_example
      dvp_stack_id: "ocid1.dvpstack.oc1..xxxxxxEXAMPLExxxxxx"
      dvp_stream_id: "ocid1.dvpstream.oc1..xxxxxxEXAMPLExxxxxx"
    region: us-phoenix-1
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete dedicated_vantage_point
  oci_apm_synthetics_dedicated_vantage_point:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    dedicated_vantage_point_id: "ocid1.dedicatedvantagepoint.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete dedicated_vantage_point using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apm_synthetics_dedicated_vantage_point:
    # required
    display_name: display_name_example
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
dedicated_vantage_point:
    description:
        - Details of the DedicatedVantagePoint resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the dedicated vantage point.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.
            returned: on success
            type: str
            sample: display_name_example
        name:
            description:
                - Unique permanent name of the dedicated vantage point. This is the same as the displayName.
            returned: on success
            type: str
            sample: name_example
        status:
            description:
                - Status of the dedicated vantage point.
            returned: on success
            type: str
            sample: ENABLED
        dvp_stack_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dvp_stack_type:
                    description:
                        - Type of stack.
                    returned: on success
                    type: str
                    sample: ORACLE_RM_STACK
                dvp_version:
                    description:
                        - Version of the dedicated vantage point.
                    returned: on success
                    type: str
                    sample: dvp_version_example
                dvp_stack_id:
                    description:
                        - Stack L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Resource Manager stack for dedicated
                          vantage point.
                    returned: on success
                    type: str
                    sample: "ocid1.dvpstack.oc1..xxxxxxEXAMPLExxxxxx"
                dvp_stream_id:
                    description:
                        - Stream L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Resource Manager stack for dedicated
                          vantage point.
                    returned: on success
                    type: str
                    sample: "ocid1.dvpstream.oc1..xxxxxxEXAMPLExxxxxx"
        region:
            description:
                - Name of the region.
            returned: on success
            type: str
            sample: us-phoenix-1
        monitor_status_count_map:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                total:
                    description:
                        - Total number of monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                enabled:
                    description:
                        - Number of enabled monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                disabled:
                    description:
                        - Number of disabled monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
                invalid:
                    description:
                        - Number of invalid monitors using the script.
                    returned: on success
                    type: int
                    sample: 56
        time_created:
            description:
                - "The time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2020-02-13T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "name": "name_example",
        "status": "ENABLED",
        "dvp_stack_details": {
            "dvp_stack_type": "ORACLE_RM_STACK",
            "dvp_version": "dvp_version_example",
            "dvp_stack_id": "ocid1.dvpstack.oc1..xxxxxxEXAMPLExxxxxx",
            "dvp_stream_id": "ocid1.dvpstream.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "region": "us-phoenix-1",
        "monitor_status_count_map": {
            "total": 56,
            "enabled": 56,
            "disabled": 56,
            "invalid": 56
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.apm_synthetics import ApmSyntheticClient
    from oci.apm_synthetics.models import CreateDedicatedVantagePointDetails
    from oci.apm_synthetics.models import UpdateDedicatedVantagePointDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DedicatedVantagePointHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DedicatedVantagePointHelperGen, self
        ).get_possible_entity_types() + [
            "dedicatedvantagepoint",
            "dedicatedvantagepoints",
            "apmSyntheticsdedicatedvantagepoint",
            "apmSyntheticsdedicatedvantagepoints",
            "dedicatedvantagepointresource",
            "dedicatedvantagepointsresource",
            "apmsynthetics",
        ]

    def get_module_resource_id_param(self):
        return "dedicated_vantage_point_id"

    def get_module_resource_id(self):
        return self.module.params.get("dedicated_vantage_point_id")

    def get_get_fn(self):
        return self.client.get_dedicated_vantage_point

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dedicated_vantage_point,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            dedicated_vantage_point_id=self.module.params.get(
                "dedicated_vantage_point_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "apm_domain_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "status"]
        )

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
            self.client.list_dedicated_vantage_points, **kwargs
        )

    def get_create_model_class(self):
        return CreateDedicatedVantagePointDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dedicated_vantage_point,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                create_dedicated_vantage_point_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDedicatedVantagePointDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dedicated_vantage_point,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                dedicated_vantage_point_id=self.module.params.get(
                    "dedicated_vantage_point_id"
                ),
                update_dedicated_vantage_point_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dedicated_vantage_point,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                dedicated_vantage_point_id=self.module.params.get(
                    "dedicated_vantage_point_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DedicatedVantagePointHelperCustom = get_custom_class(
    "DedicatedVantagePointHelperCustom"
)


class ResourceHelper(DedicatedVantagePointHelperCustom, DedicatedVantagePointHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            status=dict(type="str", choices=["ENABLED", "DISABLED"]),
            dvp_stack_details=dict(
                type="dict",
                options=dict(
                    dvp_stack_type=dict(
                        type="str", required=True, choices=["ORACLE_RM_STACK"]
                    ),
                    dvp_version=dict(type="str", required=True),
                    dvp_stack_id=dict(type="str", required=True),
                    dvp_stream_id=dict(type="str", required=True),
                ),
            ),
            region=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            apm_domain_id=dict(type="str", required=True),
            dedicated_vantage_point_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dedicated_vantage_point",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
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
