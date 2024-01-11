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
module: oci_waa_web_app_acceleration_actions
short_description: Perform actions on a WebAppAcceleration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a WebAppAcceleration resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a Web App Acceleration resource from one compartment to another.
      When provided, If-Match is checked against ETag values of the resource.
    - For I(action=purge_web_app_acceleration_cache), clears resources from the cache of the WebAppAcceleration. Each new request for a purged resource will be
      forwarded to the origin server to fetch a new version of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    web_app_acceleration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppAcceleration.
        type: str
        aliases: ["id"]
        required: true
    purge_type:
        description:
            - Type of cache purge to perform.
            - Required for I(action=purge_web_app_acceleration_cache).
        type: str
        choices:
            - "ENTIRE_CACHE"
    action:
        description:
            - The action to perform on the WebAppAcceleration.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "purge_web_app_acceleration_cache"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on web_app_acceleration
  oci_waa_web_app_acceleration_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    web_app_acceleration_id: "ocid1.webappacceleration.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action purge_web_app_acceleration_cache on web_app_acceleration with purge_type = ENTIRE_CACHE
  oci_waa_web_app_acceleration_actions:
    # required
    purge_type: ENTIRE_CACHE

"""

RETURN = """
web_app_acceleration:
    description:
        - Details of the WebAppAcceleration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WebAppAcceleration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - WebAppAcceleration display name, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        backend_type:
            description:
                - Type of the WebAppFirewall, as example LOAD_BALANCER.
            returned: on success
            type: str
            sample: LOAD_BALANCER
        web_app_acceleration_policy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of WebAppAccelerationPolicy, which is attached to the
                  resource.
            returned: on success
            type: str
            sample: "ocid1.webappaccelerationpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the WebAppAcceleration was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the WebAppAcceleration was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the WebAppAcceleration.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource in FAILED state.
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
        load_balancer_id:
            description:
                - LoadBalancer L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) to which the WebAppAccelerationPolicy is attached
                  to.
            returned: on success
            type: str
            sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "backend_type": "LOAD_BALANCER",
        "web_app_acceleration_policy_id": "ocid1.webappaccelerationpolicy.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.waa import WorkRequestClient
    from oci.waa import WaaClient
    from oci.waa.models import ChangeWebAppAccelerationCompartmentDetails
    from oci.waa.models import PurgeWebAppAccelerationCacheDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WebAppAccelerationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        purge_web_app_acceleration_cache
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "web_app_acceleration_id"

    def get_module_resource_id(self):
        return self.module.params.get("web_app_acceleration_id")

    def get_get_fn(self):
        return self.client.get_web_app_acceleration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_web_app_acceleration,
            web_app_acceleration_id=self.module.params.get("web_app_acceleration_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeWebAppAccelerationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_web_app_acceleration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_acceleration_id=self.module.params.get(
                    "web_app_acceleration_id"
                ),
                change_web_app_acceleration_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def purge_web_app_acceleration_cache(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PurgeWebAppAccelerationCacheDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.purge_web_app_acceleration_cache,
            call_fn_args=(),
            call_fn_kwargs=dict(
                web_app_acceleration_id=self.module.params.get(
                    "web_app_acceleration_id"
                ),
                purge_web_app_acceleration_cache_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WebAppAccelerationActionsHelperCustom = get_custom_class(
    "WebAppAccelerationActionsHelperCustom"
)


class ResourceHelper(
    WebAppAccelerationActionsHelperCustom, WebAppAccelerationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            web_app_acceleration_id=dict(aliases=["id"], type="str", required=True),
            purge_type=dict(type="str", choices=["ENTIRE_CACHE"]),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "purge_web_app_acceleration_cache"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="web_app_acceleration",
        service_client_class=WaaClient,
        namespace="waa",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
