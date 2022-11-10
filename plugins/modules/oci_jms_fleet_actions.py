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
module: oci_jms_fleet_actions
short_description: Perform actions on a Fleet resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Fleet resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move a specified Fleet into the compartment identified in the POST form. When provided, If-Match is checked against ETag
      values of the resource.
    - For I(action=generate_agent_deploy_script), generates Agent Deploy Script for Fleet using the information provided.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the Fleet should be moved.
            - Required for I(action=change_compartment).
        type: str
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
            - Required for I(action=generate_agent_deploy_script).
        type: str
    fleet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Fleet.
        type: str
        aliases: ["id"]
        required: true
    install_key_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the install key for which to generate the script.
            - Required for I(action=generate_agent_deploy_script).
        type: str
    os_family:
        description:
            - The operating system type for the script. Currently only 'LINUX' and 'WINDOWS' are supported.
            - Required for I(action=generate_agent_deploy_script).
        type: str
        choices:
            - "LINUX"
            - "WINDOWS"
            - "MACOS"
            - "UNKNOWN"
    is_user_name_enabled:
        description:
            - Enable/disable user name collection on agent.
            - Required for I(action=generate_agent_deploy_script).
        type: bool
    action:
        description:
            - The action to perform on the Fleet.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "generate_agent_deploy_script"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on fleet
  oci_jms_fleet_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action generate_agent_deploy_script on fleet
  oci_jms_fleet_actions:
    # required
    dest: /tmp/myfile
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"
    install_key_id: "ocid1.installkey.oc1..xxxxxxEXAMPLExxxxxx"
    os_family: LINUX
    is_user_name_enabled: true
    action: generate_agent_deploy_script

"""

RETURN = """
fleet:
    description:
        - Details of the Fleet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Fleet.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the Fleet.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The Fleet's description.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment of the Fleet.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        approximate_jre_count:
            description:
                - The approximate count of all unique Java Runtimes in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_installation_count:
            description:
                - The approximate count of all unique Java installations in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_application_count:
            description:
                - The approximate count of all unique applications in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_managed_instance_count:
            description:
                - The approximate count of all unique managed instances in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        inventory_log:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                log_group_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log group.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        operation_log:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                log_group_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log group.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the log.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        is_advanced_features_enabled:
            description:
                - Whether or not advanced features are enabled in this fleet.  By default, this is set to false.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The creation date and time of the Fleet (formatted according to L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The lifecycle state of the Fleet.
            returned: on success
            type: str
            sample: ACTIVE
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. (See L(Understanding Free-form
                  Tags,https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm))."
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`. (See L(Managing Tags and Tag
                  Namespaces,https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm).)"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "approximate_jre_count": 56,
        "approximate_installation_count": 56,
        "approximate_application_count": 56,
        "approximate_managed_instance_count": 56,
        "inventory_log": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "operation_log": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_advanced_features_enabled": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "system_tags": {}
    }
"""

from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.jms import JavaManagementServiceClient
    from oci.jms.models import ChangeFleetCompartmentDetails
    from oci.jms.models import GenerateAgentDeployScriptDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FleetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        generate_agent_deploy_script
    """

    @staticmethod
    def get_module_resource_id_param():
        return "fleet_id"

    def get_module_resource_id(self):
        return self.module.params.get("fleet_id")

    def get_get_fn(self):
        return self.client.get_fleet

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fleet, fleet_id=self.module.params.get("fleet_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeFleetCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_fleet_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                change_fleet_compartment_details=action_details,
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

    def generate_agent_deploy_script(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateAgentDeployScriptDetails
        )
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_agent_deploy_script,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                generate_agent_deploy_script_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


FleetActionsHelperCustom = get_custom_class("FleetActionsHelperCustom")


class ResourceHelper(FleetActionsHelperCustom, FleetActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            dest=dict(type="str"),
            fleet_id=dict(aliases=["id"], type="str", required=True),
            install_key_id=dict(type="str"),
            os_family=dict(
                type="str", choices=["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
            ),
            is_user_name_enabled=dict(type="bool"),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "generate_agent_deploy_script"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="fleet",
        service_client_class=JavaManagementServiceClient,
        namespace="jms",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
