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
module: oci_devops_connection_actions
short_description: Perform actions on a Connection resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Connection resource in Oracle Cloud Infrastructure
    - For I(action=validate), return whether the credentials of the connection are valid.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_id:
        description:
            - Unique connection identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Connection.
        type: str
        required: true
        choices:
            - "validate"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action validate on connection
  oci_devops_connection_actions:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    action: validate

"""

RETURN = """
connection:
    description:
        - Details of the Connection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        username:
            description:
                - Public Bitbucket Cloud Username in plain text
            returned: on success
            type: str
            sample: username_example
        app_password:
            description:
                - OCID of personal Bitbucket Cloud AppPassword saved in secret store
            returned: on success
            type: str
            sample: example-password
        tls_verify_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                tls_verify_mode:
                    description:
                        - The type of TLS verification.
                    returned: on success
                    type: str
                    sample: CA_CERTIFICATE_VERIFY
                ca_certificate_bundle_id:
                    description:
                        - The OCID of OCI certificate service CA bundle.
                    returned: on success
                    type: str
                    sample: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the connection.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Connection display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment containing the connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The OCID of the DevOps project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type:
            description:
                - The type of connection.
            returned: on success
            type: str
            sample: GITHUB_ACCESS_TOKEN
        time_created:
            description:
                - The time the connection was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the connection was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        last_connection_validation_result:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                result:
                    description:
                        - The latest result of whether the credentials pass the validation.
                    returned: on success
                    type: str
                    sample: PASS
                time_validated:
                    description:
                        - The latest timestamp when the connection was validated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                message:
                    description:
                        - A message describing the result of connection validation in more detail.
                    returned: on success
                    type: str
                    sample: message_example
        lifecycle_details:
            description:
                - A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the connection.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        access_token:
            description:
                - The OCID of personal access token saved in secret store.
            returned: on success
            type: str
            sample: access_token_example
        base_url:
            description:
                - The Base URL of the hosted BitbucketServer.
            returned: on success
            type: str
            sample: base_url_example
    sample: {
        "username": "username_example",
        "app_password": "example-password",
        "tls_verify_config": {
            "tls_verify_mode": "CA_CERTIFICATE_VERIFY",
            "ca_certificate_bundle_id": "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_type": "GITHUB_ACCESS_TOKEN",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "last_connection_validation_result": {
            "result": "PASS",
            "time_validated": "2013-10-20T19:20:30+01:00",
            "message": "message_example"
        },
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "access_token": "access_token_example",
        "base_url": "base_url_example"
    }
"""

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
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsConnectionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        validate
    """

    @staticmethod
    def get_module_resource_id_param():
        return "connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_id")

    def get_get_fn(self):
        return self.client.get_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def validate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(connection_id=self.module.params.get("connection_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


DevopsConnectionActionsHelperCustom = get_custom_class(
    "DevopsConnectionActionsHelperCustom"
)


class ResourceHelper(
    DevopsConnectionActionsHelperCustom, DevopsConnectionActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            connection_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["validate"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
