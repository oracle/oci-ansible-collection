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
module: oci_jms_fleet_actions
short_description: Perform actions on a Fleet resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Fleet resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move a specified Fleet into the compartment identified in the POST form. When provided, If-Match is checked against ETag
      values of the resource.
    - For I(action=generate_agent_deploy_script), generates Agent Deploy Script for Fleet using the information provided.
    - For I(action=request_crypto_analyses), request to perform crypto analysis on one or more selected targets in the Fleet. The result of the crypto analysis
      will be uploaded to the object storage bucket created by JMS on enabling the Crypto Event Analysis feature in the Fleet.
    - For I(action=request_java_migration_analyses), request to perform a Java migration analysis. The results of the Java migration analysis will be uploaded
      to the
      Object Storage bucket that you designate when you enable the Java Migration Analysis feature.
    - For I(action=request_jfr_recordings), request to collect the JFR recordings on the selected target in the Fleet. The JFR files are uploaded to the object
      storage bucket created by JMS on enabling Generic JFR feature in the Fleet.
    - For I(action=request_performance_tuning_analyses), request to perform performance tuning analyses. The result of performance tuning analysis will be
      uploaded to the
      object storage bucket that you designated when you enabled the recording feature.
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
    jfc_profile_name:
        description:
            - The profile used for JFR events selection. If the name isn't recognized, the settings from jfcV1 or jfcV2
              will be used depending on the JVM version.
              Both jfcV2 and jfcV1 should be provided to ensure JFR collection on different JVM versions.
            - Required for I(action=request_jfr_recordings).
        type: str
    jfc_v1:
        description:
            - The BASE64 encoded string of JFR settings XML with schema used by JDK 8.
            - Applicable only for I(action=request_jfr_recordings).
        type: str
    jfc_v2:
        description:
            - The BASE64 encoded string of JFR settings XML with L(schema used by JDK 9 and
              after,https://raw.githubusercontent.com/openjdk/jdk/master/src/jdk.jfr/share/classes/jdk/jfr/internal/jfc/jfc.xsd).
            - Applicable only for I(action=request_jfr_recordings).
        type: str
    recording_size_in_mb:
        description:
            - The maximum size limit for the JFR file collected.
            - Applicable only for I(action=request_jfr_recordings).
        type: int
    fleet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Fleet.
        type: str
        aliases: ["id"]
        required: true
    targets:
        description:
            - The attachment targets to start JFR.
            - Required for I(action=request_java_migration_analyses).
        type: list
        elements: dict
        suboptions:
            application_key:
                description:
                    - Unique key that identifies the application for JFR data collection.
                type: str
            jre_key:
                description:
                    - Unique key that identify the JVM for JFR data collection.
                type: str
            managed_instance_id:
                description:
                    - OCID of the Managed Instance to collect JFR data.
                type: str
                required: true
            application_installation_key:
                description:
                    - Unique key that identifies the application installation for JFR data collection.
                type: str
            source_jdk_version:
                description:
                    - The JDK version the application is currently running on.
                type: str
            target_jdk_version:
                description:
                    - The JDK version against which the migration analysis was performed to identify effort required to move from source JDK.
                type: str
    recording_duration_in_minutes:
        description:
            - Duration of the JFR recording in minutes.
            - Required for I(action=request_performance_tuning_analyses).
        type: int
    waiting_period_in_minutes:
        description:
            - Period to looking for JVMs. In addition to attach to running JVMs when given the command,
              JVM started within the waiting period will also be attached for JFR. The value should be
              larger than the agent polling interval setting for the fleet to ensure agent can get the
              instructions. If not specified, the agent polling interval for the fleet is used.
            - Applicable only for I(action=request_crypto_analyses)I(action=request_jfr_recordings)I(action=request_performance_tuning_analyses).
        type: int
    action:
        description:
            - The action to perform on the Fleet.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "generate_agent_deploy_script"
            - "request_crypto_analyses"
            - "request_java_migration_analyses"
            - "request_jfr_recordings"
            - "request_performance_tuning_analyses"
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
    install_key_id: "ocid1.installkey.oc1..xxxxxxEXAMPLExxxxxx"
    os_family: LINUX
    is_user_name_enabled: true
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"
    action: generate_agent_deploy_script

- name: Perform action request_crypto_analyses on fleet
  oci_jms_fleet_actions:
    # required
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"
    action: request_crypto_analyses

    # optional
    targets:
    - # required
      managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      application_key: application_key_example
      jre_key: jre_key_example
      application_installation_key: application_installation_key_example
      source_jdk_version: source_jdk_version_example
      target_jdk_version: target_jdk_version_example
    recording_duration_in_minutes: 56
    waiting_period_in_minutes: 56

- name: Perform action request_java_migration_analyses on fleet
  oci_jms_fleet_actions:
    # required
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"
    targets:
    - # required
      managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      application_key: application_key_example
      jre_key: jre_key_example
      application_installation_key: application_installation_key_example
      source_jdk_version: source_jdk_version_example
      target_jdk_version: target_jdk_version_example
    action: request_java_migration_analyses

- name: Perform action request_jfr_recordings on fleet
  oci_jms_fleet_actions:
    # required
    jfc_profile_name: jfc_profile_name_example
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"
    action: request_jfr_recordings

    # optional
    jfc_v1: jfc_v1_example
    jfc_v2: jfc_v2_example
    recording_size_in_mb: 56
    targets:
    - # required
      managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      application_key: application_key_example
      jre_key: jre_key_example
      application_installation_key: application_installation_key_example
      source_jdk_version: source_jdk_version_example
      target_jdk_version: target_jdk_version_example
    recording_duration_in_minutes: 56
    waiting_period_in_minutes: 56

- name: Perform action request_performance_tuning_analyses on fleet
  oci_jms_fleet_actions:
    # required
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"
    recording_duration_in_minutes: 56
    action: request_performance_tuning_analyses

    # optional
    targets:
    - # required
      managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      application_key: application_key_example
      jre_key: jre_key_example
      application_installation_key: application_installation_key_example
      source_jdk_version: source_jdk_version_example
      target_jdk_version: target_jdk_version_example
    waiting_period_in_minutes: 56

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
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_installation_count:
            description:
                - The approximate count of all unique Java installations in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_application_count:
            description:
                - The approximate count of all unique applications in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_managed_instance_count:
            description:
                - The approximate count of all unique managed instances in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_java_server_count:
            description:
                - The approximate count of all unique Java servers in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and isn't taken into account when computing the resource ETag.
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
                - Whether or not advanced features are enabled in this Fleet.
                  Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` API instead.
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
                - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
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
        "approximate_java_server_count": 56,
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
    from oci.jms.models import RequestCryptoAnalysesDetails
    from oci.jms.models import RequestJavaMigrationAnalysesDetails
    from oci.jms.models import RequestJfrRecordingsDetails
    from oci.jms.models import RequestPerformanceTuningAnalysesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FleetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        generate_agent_deploy_script
        request_crypto_analyses
        request_java_migration_analyses
        request_jfr_recordings
        request_performance_tuning_analyses
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

    def request_crypto_analyses(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestCryptoAnalysesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.request_crypto_analyses,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                request_crypto_analyses_details=action_details,
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

    def request_java_migration_analyses(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestJavaMigrationAnalysesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.request_java_migration_analyses,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                request_java_migration_analyses_details=action_details,
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

    def request_jfr_recordings(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestJfrRecordingsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.request_jfr_recordings,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                request_jfr_recordings_details=action_details,
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

    def request_performance_tuning_analyses(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestPerformanceTuningAnalysesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.request_performance_tuning_analyses,
            call_fn_args=(),
            call_fn_kwargs=dict(
                fleet_id=self.module.params.get("fleet_id"),
                request_performance_tuning_analyses_details=action_details,
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
            install_key_id=dict(type="str"),
            os_family=dict(
                type="str", choices=["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
            ),
            is_user_name_enabled=dict(type="bool"),
            jfc_profile_name=dict(type="str"),
            jfc_v1=dict(type="str"),
            jfc_v2=dict(type="str"),
            recording_size_in_mb=dict(type="int"),
            fleet_id=dict(aliases=["id"], type="str", required=True),
            targets=dict(
                type="list",
                elements="dict",
                options=dict(
                    application_key=dict(type="str", no_log=True),
                    jre_key=dict(type="str", no_log=True),
                    managed_instance_id=dict(type="str", required=True),
                    application_installation_key=dict(type="str", no_log=True),
                    source_jdk_version=dict(type="str"),
                    target_jdk_version=dict(type="str"),
                ),
            ),
            recording_duration_in_minutes=dict(type="int"),
            waiting_period_in_minutes=dict(type="int"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "generate_agent_deploy_script",
                    "request_crypto_analyses",
                    "request_java_migration_analyses",
                    "request_jfr_recordings",
                    "request_performance_tuning_analyses",
                ],
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
