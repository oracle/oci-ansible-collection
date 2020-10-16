#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_analytics_instance
short_description: Manage an AnalyticsInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AnalyticsInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new AnalyticsInstance in the specified compartment. The operation is long-running
      and creates a new WorkRequest.
    - "This resource has the following action operations in the M(oci_analytics_instance_actions) module: change_analytics_instance_network_endpoint, scale,
      start, stop."
version_added: "2.9"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - Optional description.
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    feature_set:
        description:
            - Analytics feature set.
            - Required for create using I(state=present).
        type: str
        choices:
            - "SELF_SERVICE_ANALYTICS"
            - "ENTERPRISE_ANALYTICS"
    capacity:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            capacity_type:
                description:
                    - The capacity model to use.
                type: str
                choices:
                    - "OLPU_COUNT"
                    - "USER_COUNT"
                required: true
            capacity_value:
                description:
                    - The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the
                      number of CPUs, amount of memory or other resources allocated to the instance.
                type: int
                required: true
    license_type:
        description:
            - The license used for the service.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    email_notification:
        description:
            - Email address receiving notifications.
            - This parameter is updatable.
        type: str
    network_endpoint_details:
        description:
            - ""
        type: dict
        suboptions:
            network_endpoint_type:
                description:
                    - The type of network endpoint.
                type: str
                choices:
                    - "PRIVATE"
                    - "PUBLIC"
                required: true
            vcn_id:
                description:
                    - The VCN OCID for the private endpoint.
                    - Required when network_endpoint_type is 'PRIVATE'
                type: str
            subnet_id:
                description:
                    - The subnet OCID for the private endpoint.
                    - Required when network_endpoint_type is 'PRIVATE'
                type: str
            whitelisted_ips:
                description:
                    - Source IP addresses or IP address ranges igress rules.
                    - Applicable when network_endpoint_type is 'PUBLIC'
                type: list
            whitelisted_vcns:
                description:
                    - Virtual Cloud Networks allowed to access this network endpoint.
                    - Applicable when network_endpoint_type is 'PUBLIC'
                type: list
                suboptions:
                    id:
                        description:
                            - The Virtual Cloud Network OCID.
                            - Required when network_endpoint_type is 'PUBLIC'
                        type: str
                        required: true
                    whitelisted_ips:
                        description:
                            - Source IP addresses or IP address ranges igress rules.
                            - Applicable when network_endpoint_type is 'PUBLIC'
                        type: list
    idcs_access_token:
        description:
            - IDCS access token identifying a stripe and service administrator user.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    analytics_instance_id:
        description:
            - The OCID of the AnalyticsInstance.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AnalyticsInstance.
            - Use I(state=present) to create or update an AnalyticsInstance.
            - Use I(state=absent) to delete an AnalyticsInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create analytics_instance
  oci_analytics_instance:
    name: name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    feature_set: SELF_SERVICE_ANALYTICS
    capacity:
      capacity_type: OLPU_COUNT
      capacity_value: 56
    license_type: LICENSE_INCLUDED

- name: Update analytics_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_analytics_instance:
    name: name_example
    description: description_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    license_type: LICENSE_INCLUDED
    email_notification: email_notification_example
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update analytics_instance
  oci_analytics_instance:
    description: description_example
    license_type: LICENSE_INCLUDED
    analytics_instance_id: ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete analytics_instance
  oci_analytics_instance:
    analytics_instance_id: ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete analytics_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_analytics_instance:
    name: name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
analytics_instance:
    description:
        - Details of the AnalyticsInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The resource OCID.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - Optional description.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of an instance.
            returned: on success
            type: string
            sample: ACTIVE
        feature_set:
            description:
                - Analytics feature set.
            returned: on success
            type: string
            sample: SELF_SERVICE_ANALYTICS
        capacity:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                capacity_type:
                    description:
                        - The capacity model to use.
                    returned: on success
                    type: string
                    sample: OLPU_COUNT
                capacity_value:
                    description:
                        - The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the
                          number of CPUs, amount of memory or other resources allocated to the instance.
                    returned: on success
                    type: int
                    sample: 56
        license_type:
            description:
                - The license used for the service.
            returned: on success
            type: string
            sample: LICENSE_INCLUDED
        email_notification:
            description:
                - Email address receiving notifications.
            returned: on success
            type: string
            sample: email_notification_example
        network_endpoint_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                network_endpoint_type:
                    description:
                        - The type of network endpoint.
                    returned: on success
                    type: string
                    sample: PUBLIC
                vcn_id:
                    description:
                        - The VCN OCID for the private endpoint.
                    returned: on success
                    type: string
                    sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
                subnet_id:
                    description:
                        - The subnet OCID for the private endpoint.
                    returned: on success
                    type: string
                    sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
                whitelisted_ips:
                    description:
                        - Source IP addresses or IP address ranges igress rules.
                    returned: on success
                    type: list
                    sample: []
                whitelisted_vcns:
                    description:
                        - Virtual Cloud Networks allowed to access this network endpoint.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The Virtual Cloud Network OCID.
                            returned: on success
                            type: string
                            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                        whitelisted_ips:
                            description:
                                - Source IP addresses or IP address ranges igress rules.
                            returned: on success
                            type: list
                            sample: []
        service_url:
            description:
                - URL of the Analytics service.
            returned: on success
            type: string
            sample: service_url_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        time_created:
            description:
                - The date and time the instance was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_updated:
            description:
                - The date and time the instance was last updated (in the format defined by RFC3339).
                  This timestamp represents updates made through this API. External events do not
                  influence it.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "feature_set": "SELF_SERVICE_ANALYTICS",
        "capacity": {
            "capacity_type": "OLPU_COUNT",
            "capacity_value": 56
        },
        "license_type": "LICENSE_INCLUDED",
        "email_notification": "email_notification_example",
        "network_endpoint_details": {
            "network_endpoint_type": "PUBLIC",
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "whitelisted_ips": [],
            "whitelisted_vcns": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "whitelisted_ips": []
            }]
        },
        "service_url": "service_url_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.analytics import AnalyticsClient
    from oci.analytics.models import CreateAnalyticsInstanceDetails
    from oci.analytics.models import UpdateAnalyticsInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnalyticsInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "analytics_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("analytics_instance_id")

    def get_get_fn(self):
        return self.client.get_analytics_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_analytics_instance,
            analytics_instance_id=self.module.params.get("analytics_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name", "feature_set"]

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
            self.client.list_analytics_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateAnalyticsInstanceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_analytics_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_analytics_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAnalyticsInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_analytics_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                update_analytics_instance_details=update_details,
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
            call_fn=self.client.delete_analytics_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AnalyticsInstanceHelperCustom = get_custom_class("AnalyticsInstanceHelperCustom")


class ResourceHelper(AnalyticsInstanceHelperCustom, AnalyticsInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            feature_set=dict(
                type="str", choices=["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]
            ),
            capacity=dict(
                type="dict",
                options=dict(
                    capacity_type=dict(
                        type="str", required=True, choices=["OLPU_COUNT", "USER_COUNT"]
                    ),
                    capacity_value=dict(type="int", required=True),
                ),
            ),
            license_type=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            email_notification=dict(type="str"),
            network_endpoint_details=dict(
                type="dict",
                options=dict(
                    network_endpoint_type=dict(
                        type="str", required=True, choices=["PRIVATE", "PUBLIC"]
                    ),
                    vcn_id=dict(type="str"),
                    subnet_id=dict(type="str"),
                    whitelisted_ips=dict(type="list"),
                    whitelisted_vcns=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            id=dict(type="str", required=True),
                            whitelisted_ips=dict(type="list"),
                        ),
                    ),
                ),
            ),
            idcs_access_token=dict(type="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            analytics_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="analytics_instance",
        service_client_class=AnalyticsClient,
        namespace="analytics",
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
