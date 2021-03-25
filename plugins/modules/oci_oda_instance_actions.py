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
module: oci_oda_instance_actions
short_description: Perform actions on an OdaInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OdaInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an Digital Assistant instance into a different compartment. When provided, If-Match is checked against
      ETag values of the resource.
    - For I(action=start), starts an inactive Digital Assistant instance. Once active, the instance will be accessible and metering
      of requests will be started again.
    - For I(action=stop), stops an active Digital Assistant instance. Once inactive, the instance will not be accessible and metering
      of requests will be stopped until the instance is started again. Data associated with the instance
      is not affected.
version_added: "2.9"
author: Oracle (@oracle)
options:
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - Identifier of the compartment into which the Digital Assistant instance should be moved.
            - Required for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the OdaInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on oda_instance
  oci_oda_instance_actions:
    oda_instance_id: ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    action: change_compartment

- name: Perform action start on oda_instance
  oci_oda_instance_actions:
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on oda_instance
  oci_oda_instance_actions:
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
oda_instance:
    description:
        - Details of the OdaInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique immutable identifier that was assigned when the instance was created.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-defined name for the Digital Assistant instance. Avoid entering confidential information.
                  You can change this value.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Description of the Digital Assistant instance.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - Identifier of the compartment that the instance belongs to.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        shape_name:
            description:
                - Shape or size of the instance.
            returned: on success
            type: string
            sample: DEVELOPMENT
        web_app_url:
            description:
                - URL for the Digital Assistant web application that's associated with the instance.
            returned: on success
            type: string
            sample: web_app_url_example
        connector_url:
            description:
                - URL for the connector's endpoint.
            returned: on success
            type: string
            sample: connector_url_example
        time_created:
            description:
                - When the Digital Assistant instance was created. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section
                  14.29.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - When the Digital Assistance instance was last updated. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339),
                  section 14.29.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the Digital Assistant instance.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_sub_state:
            description:
                - The current sub-state of the Digital Assistant instance.
            returned: on success
            type: string
            sample: CREATING
        state_message:
            description:
                - A message that describes the current state in more detail.
                  For example, actionable information about an instance that's in the `FAILED` state.
            returned: on success
            type: string
            sample: state_message_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "shape_name": "DEVELOPMENT",
        "web_app_url": "web_app_url_example",
        "connector_url": "connector_url_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_sub_state": "CREATING",
        "state_message": "state_message_example",
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.oda import OdaClient
    from oci.oda.models import ChangeOdaInstanceCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OdaInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "oda_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("oda_instance_id")

    def get_get_fn(self):
        return self.client.get_oda_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_oda_instance,
            oda_instance_id=self.module.params.get("oda_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeOdaInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_oda_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                change_oda_instance_compartment_details=action_details,
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

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_oda_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
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

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_oda_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
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


OdaInstanceActionsHelperCustom = get_custom_class("OdaInstanceActionsHelperCustom")


class ResourceHelper(OdaInstanceActionsHelperCustom, OdaInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            oda_instance_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "start", "stop"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="oda_instance",
        service_client_class=OdaClient,
        namespace="oda",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
