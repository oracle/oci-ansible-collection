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
module: oci_data_safe_target_database_actions
short_description: Perform actions on a TargetDatabase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TargetDatabase resource in Oracle Cloud Infrastructure
    - For I(action=activate), reactivates a previously deactivated Data Safe target database.
    - For I(action=change_compartment), moves the Data Safe target database to the specified compartment.
    - For I(action=deactivate), deactivates a target database in Data Safe.
    - For I(action=download_privilege_script), downloads the privilege script to grant/revoke required roles from the Data Safe account on the target database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    credentials:
        description:
            - ""
            - Required for I(action=activate).
        type: dict
        suboptions:
            user_name:
                description:
                    - The database user name.
                type: str
                required: true
            password:
                description:
                    - The password of the database user.
                type: str
                required: true
    target_database_id:
        description:
            - The OCID of the Data Safe target database.
            - Required for I(action=activate), I(action=change_compartment), I(action=deactivate).
        type: str
    compartment_id:
        description:
            - The OCID of the new compartment to where you want to move the Data Safe target database.
            - Required for I(action=change_compartment).
        type: str
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
            - Required for I(action=download_privilege_script).
        type: str
    action:
        description:
            - The action to perform on the TargetDatabase.
        type: str
        required: true
        choices:
            - "activate"
            - "change_compartment"
            - "deactivate"
            - "download_privilege_script"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on target_database
  oci_data_safe_target_database_actions:
    # required
    credentials:
      # required
      user_name: user_name_example
      password: example-password
    target_database_id: "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: activate

- name: Perform action change_compartment on target_database
  oci_data_safe_target_database_actions:
    # required
    target_database_id: "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action deactivate on target_database
  oci_data_safe_target_database_actions:
    # required
    target_database_id: "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: deactivate

- name: Perform action download_privilege_script on target_database
  oci_data_safe_target_database_actions:
    # required
    dest: /tmp/myfile
    action: download_privilege_script

"""

RETURN = """
target_database:
    description:
        - Details of the TargetDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment which contains the Data Safe target database.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The OCID of the Data Safe target database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the target database in Data Safe.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the target database in Data Safe.
            returned: on success
            type: str
            sample: description_example
        database_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                database_type:
                    description:
                        - The database type.
                    returned: on success
                    type: str
                    sample: DATABASE_CLOUD_SERVICE
                infrastructure_type:
                    description:
                        - The infrastructure type the database is running on.
                    returned: on success
                    type: str
                    sample: ORACLE_CLOUD
                autonomous_database_id:
                    description:
                        - The OCID of the autonomous database registered as a target database in Data Safe.
                    returned: on success
                    type: str
                    sample: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"
                vm_cluster_id:
                    description:
                        - The OCID of the VM cluster in which the database is running.
                    returned: on success
                    type: str
                    sample: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
                db_system_id:
                    description:
                        - The OCID of the cloud database system registered as a target database in Data Safe.
                    returned: on success
                    type: str
                    sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
                service_name:
                    description:
                        - The database service name.
                    returned: on success
                    type: str
                    sample: service_name_example
                instance_id:
                    description:
                        - The OCID of the compute instance on which the database is running.
                    returned: on success
                    type: str
                    sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
                ip_addresses:
                    description:
                        - The list of database host IP Addresses. Fully qualified domain names can be used if connectionType is 'ONPREM_CONNECTOR'.
                    returned: on success
                    type: list
                    sample: []
                listener_port:
                    description:
                        - The port number of the database listener.
                    returned: on success
                    type: int
                    sample: 56
        credentials:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                user_name:
                    description:
                        - The database user name.
                    returned: on success
                    type: str
                    sample: user_name_example
                password:
                    description:
                        - The password of the database user.
                    returned: on success
                    type: str
                    sample: example-password
        tls_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - Status to represent whether the database connection is TLS enabled or not.
                    returned: on success
                    type: str
                    sample: ENABLED
                certificate_store_type:
                    description:
                        - The format of the certificate store.
                    returned: on success
                    type: str
                    sample: JKS
                store_password:
                    description:
                        - The password to read the trust store and key store files, if they are password protected.
                    returned: on success
                    type: str
                    sample: example-password
                trust_store_content:
                    description:
                        - Base64 encoded string of trust store file content.
                    returned: on success
                    type: str
                    sample: trust_store_content_example
                key_store_content:
                    description:
                        - Base64 encoded string of key store file content.
                    returned: on success
                    type: str
                    sample: key_store_content_example
        connection_option:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                connection_type:
                    description:
                        - "The connection type used to connect to the database. Allowed values:
                          - PRIVATE_ENDPOINT - Represents connection through private endpoint in Data Safe.
                          - ONPREM_CONNECTOR - Represents connection through on-premises connector in Data Safe."
                    returned: on success
                    type: str
                    sample: PRIVATE_ENDPOINT
                on_prem_connector_id:
                    description:
                        - The OCID of the on-premises connector.
                    returned: on success
                    type: str
                    sample: "ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx"
                datasafe_private_endpoint_id:
                    description:
                        - The OCID of the Data Safe private endpoint.
                    returned: on success
                    type: str
                    sample: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        associated_resource_ids:
            description:
                - The OCIDs of associated resources like Database, Data Safe private endpoint etc.
            returned: on success
            type: list
            sample: []
        lifecycle_state:
            description:
                - The current state of the target database in Data Safe.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current state of the target database in Data Safe.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time of target database registration and creation in Data Safe.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time of the target database update in Data Safe.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "database_details": {
            "database_type": "DATABASE_CLOUD_SERVICE",
            "infrastructure_type": "ORACLE_CLOUD",
            "autonomous_database_id": "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx",
            "vm_cluster_id": "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx",
            "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
            "service_name": "service_name_example",
            "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
            "ip_addresses": [],
            "listener_port": 56
        },
        "credentials": {
            "user_name": "user_name_example",
            "password": "example-password"
        },
        "tls_config": {
            "status": "ENABLED",
            "certificate_store_type": "JKS",
            "store_password": "example-password",
            "trust_store_content": "trust_store_content_example",
            "key_store_content": "key_store_content_example"
        },
        "connection_option": {
            "connection_type": "PRIVATE_ENDPOINT",
            "on_prem_connector_id": "ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx",
            "datasafe_private_endpoint_id": "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "associated_resource_ids": [],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import ActivateTargetDatabaseDetails
    from oci.data_safe.models import ChangeTargetDatabaseCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeTargetDatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        change_compartment
        deactivate
        download_privilege_script
    """

    def get_get_fn(self):
        return self.client.get_target_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_database,
            target_database_id=self.module.params.get("target_database_id"),
        )

    def activate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ActivateTargetDatabaseDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_target_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                activate_target_database_details=action_details,
                target_database_id=self.module.params.get("target_database_id"),
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeTargetDatabaseCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_target_database_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_database_id=self.module.params.get("target_database_id"),
                change_target_database_compartment_details=action_details,
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

    def deactivate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deactivate_target_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_database_id=self.module.params.get("target_database_id"),
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

    def download_privilege_script(self):
        response = oci_wait_utils.call_and_wait(
            call_fn=self.client.download_privilege_script,
            call_fn_args=(),
            call_fn_kwargs=dict(),
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


DataSafeTargetDatabaseActionsHelperCustom = get_custom_class(
    "DataSafeTargetDatabaseActionsHelperCustom"
)


class ResourceHelper(
    DataSafeTargetDatabaseActionsHelperCustom, DataSafeTargetDatabaseActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            credentials=dict(
                type="dict",
                options=dict(
                    user_name=dict(type="str", required=True),
                    password=dict(type="str", required=True, no_log=True),
                ),
            ),
            target_database_id=dict(type="str"),
            compartment_id=dict(type="str"),
            dest=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "activate",
                    "change_compartment",
                    "deactivate",
                    "download_privilege_script",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target_database",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
