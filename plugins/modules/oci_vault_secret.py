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
module: oci_vault_secret
short_description: Manage a Secret resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a Secret resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new secret according to the details of the request.
    - This operation is not supported by the Oracle Cloud Infrastructure Terraform Provider.
    - "This resource has the following action operations in the M(oci_secret_actions) module: cancel_secret_deletion, schedule_secret_deletion."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where you want to create the secret.
            - Required for create using I(state=present).
        type: str
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    description:
        description:
            - A brief description of the secret. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    key_id:
        description:
            - The OCID of the master encryption key that is used to encrypt the secret.
        type: str
    metadata:
        description:
            - Additional metadata that you can use to provide context about how to use the secret during rotation or
              other administrative tasks. For example, for a secret that you use to connect to a database, the additional
              metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.
            - This parameter is updatable.
        type: dict
    secret_content:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            content_type:
                description:
                    - The base64-encoded content of the secret.
                type: str
                choices:
                    - "BASE64"
                required: true
            name:
                description:
                    - Names should be unique within a secret. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
                type: str
            stage:
                description:
                    - The rotation state of the secret content. The default is `CURRENT`, meaning that the secret is currently in use. A secret version
                      that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example,
                      you might create or update a secret and mark its rotation state as `PENDING` if you haven't yet updated the secret on the target system.
                      When creating a secret, only the value `CURRENT` is applicable, although the value `LATEST` is also automatically applied. When updating
                      a secret, you can specify a version's rotation state as either `CURRENT` or `PENDING`.
                type: str
                choices:
                    - "CURRENT"
                    - "PENDING"
            content:
                description:
                    - The base64-encoded content of the secret.
                type: str
    secret_name:
        description:
            - A user-friendly name for the secret. Secret names should be unique within a vault. Avoid entering confidential information. Valid characters are
              uppercase or lowercase letters, numbers, hyphens, underscores, and periods.
            - Required for create using I(state=present).
        type: str
    secret_rules:
        description:
            - A list of rules to control how the secret is used and managed.
            - This parameter is updatable.
        type: list
        suboptions:
            rule_type:
                description:
                    - The type of rule, which either controls when the secret contents expire or whether they can be reused.
                type: str
                choices:
                    - "SECRET_EXPIRY_RULE"
                    - "SECRET_REUSE_RULE"
                required: true
            secret_version_expiry_interval:
                description:
                    - A property indicating how long the secret contents will be considered valid, expressed in
                      L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format. The secret needs to be
                      updated when the secret content expires. No enforcement mechanism exists at this time, but audit logs
                      record the expiration on the appropriate date, according to the time interval specified in the rule.
                      The timer resets after you update the secret contents.
                      The minimum value is 1 day and the maximum value is 90 days for this property. Currently, only intervals expressed in days are supported.
                      For example, pass `P3D` to have the secret version expire every 3 days.
                    - Applicable when rule_type is 'SECRET_EXPIRY_RULE'
                type: str
            time_of_absolute_expiry:
                description:
                    - "An optional property indicating the absolute time when this secret will expire, expressed in L(RFC
                      3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                      The minimum number of days from current time is 1 day and the maximum number of days from current time is 365 days.
                      Example: `2019-04-03T21:10:29.600Z`"
                    - Applicable when rule_type is 'SECRET_EXPIRY_RULE'
                type: str
            is_secret_content_retrieval_blocked_on_expiry:
                description:
                    - A property indicating whether to block retrieval of the secret content, on expiry. The default is false.
                      If the secret has already expired and you would like to retrieve the secret contents,
                      you need to edit the secret rule to disable this property, to allow reading the secret content.
                    - Applicable when rule_type is 'SECRET_EXPIRY_RULE'
                type: bool
            is_enforced_on_deleted_secret_versions:
                description:
                    - A property indicating whether the rule is applied even if the secret version with the content you are trying to reuse was deleted.
                    - Applicable when rule_type is 'SECRET_REUSE_RULE'
                type: bool
    vault_id:
        description:
            - The OCID of the vault where you want to create the secret.
            - Required for create using I(state=present).
        type: str
    secret_id:
        description:
            - The OCID of the secret.
            - Required for update using I(state=present).
        type: str
        aliases: ["id"]
    current_version_number:
        description:
            - Details to update the secret version of the specified secret. The secret contents,
              version number, and rules can't be specified at the same time.
              Updating the secret contents automatically creates a new secret version.
            - This parameter is updatable.
        type: int
    state:
        description:
            - The state of the Secret.
            - Use I(state=present) to create or update a Secret.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create secret
  oci_vault_secret:
    vault_id: vault_OCID
    secret_rules: '[]'
    compartment_id:
    secret_name: testSecret
    description: my test secret
    key_id: key_OCID
    secret_content:
      content: base64_encoded_secret_contents
      content_type: BASE64

- name: Update secret
  oci_vault_secret:
    description: updated version of my test secret
    current_version_number: 4
    secret_id: ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
secret:
    description:
        - Details of the Secret resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment where you want to create the secret.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        current_version_number:
            description:
                - The version number of the secret version that's currently in use.
            returned: on success
            type: int
            sample: 56
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        description:
            description:
                - A brief description of the secret. Avoid entering confidential information.
            returned: on success
            type: string
            sample: description_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the secret.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        key_id:
            description:
                - The OCID of the master encryption key that is used to encrypt the secret.
            returned: on success
            type: string
            sample: ocid1.key.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the secret.
            returned: on success
            type: string
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current lifecycle state of the secret.
            returned: on success
            type: string
            sample: CREATING
        metadata:
            description:
                - Additional metadata that you can use to provide context about how to use the secret or during rotation or
                  other administrative tasks. For example, for a secret that you use to connect to a database, the additional
                  metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.
            returned: on success
            type: dict
            sample: {}
        secret_name:
            description:
                - The user-friendly name of the secret. Avoid entering confidential information.
            returned: on success
            type: string
            sample: secret_name_example
        secret_rules:
            description:
                - A list of rules that control how the secret is used and managed.
            returned: on success
            type: complex
            contains:
                rule_type:
                    description:
                        - The type of rule, which either controls when the secret contents expire or whether they can be reused.
                    returned: on success
                    type: string
                    sample: SECRET_EXPIRY_RULE
                secret_version_expiry_interval:
                    description:
                        - A property indicating how long the secret contents will be considered valid, expressed in
                          L(ISO 8601,https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) format. The secret needs to be
                          updated when the secret content expires. No enforcement mechanism exists at this time, but audit logs
                          record the expiration on the appropriate date, according to the time interval specified in the rule.
                          The timer resets after you update the secret contents.
                          The minimum value is 1 day and the maximum value is 90 days for this property. Currently, only intervals expressed in days are
                          supported.
                          For example, pass `P3D` to have the secret version expire every 3 days.
                    returned: on success
                    type: string
                    sample: secret_version_expiry_interval_example
                time_of_absolute_expiry:
                    description:
                        - "An optional property indicating the absolute time when this secret will expire, expressed in L(RFC
                          3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                          The minimum number of days from current time is 1 day and the maximum number of days from current time is 365 days.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2019-04-03T21:10:29.600Z
                is_secret_content_retrieval_blocked_on_expiry:
                    description:
                        - A property indicating whether to block retrieval of the secret content, on expiry. The default is false.
                          If the secret has already expired and you would like to retrieve the secret contents,
                          you need to edit the secret rule to disable this property, to allow reading the secret content.
                    returned: on success
                    type: bool
                    sample: true
                is_enforced_on_deleted_secret_versions:
                    description:
                        - A property indicating whether the rule is applied even if the secret version with the content you are trying to reuse was deleted.
                    returned: on success
                    type: bool
                    sample: true
        time_created:
            description:
                - "A property indicating when the secret was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        time_of_current_version_expiry:
            description:
                - "An optional property indicating when the current secret version will expire, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the secret, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        vault_id:
            description:
                - The OCID of the vault where the secret exists.
            returned: on success
            type: string
            sample: ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "current_version_number": 56,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "CREATING",
        "metadata": {},
        "secret_name": "secret_name_example",
        "secret_rules": [{
            "rule_type": "SECRET_EXPIRY_RULE",
            "secret_version_expiry_interval": "secret_version_expiry_interval_example",
            "time_of_absolute_expiry": "2019-04-03T21:10:29.600Z",
            "is_secret_content_retrieval_blocked_on_expiry": true,
            "is_enforced_on_deleted_secret_versions": true
        }],
        "time_created": "2019-04-03T21:10:29.600Z",
        "time_of_current_version_expiry": "2019-04-03T21:10:29.600Z",
        "time_of_deletion": "2019-04-03T21:10:29.600Z",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.vault import VaultsClient
    from oci.vault.models import CreateSecretDetails
    from oci.vault.models import UpdateSecretDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecretHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_module_resource_id_param(self):
        return "secret_id"

    def get_module_resource_id(self):
        return self.module.params.get("secret_id")

    def get_get_fn(self):
        return self.client.get_secret

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_secret, secret_id=self.module.params.get("secret_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["vault_id"]

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
        return oci_common_utils.list_all_resources(self.client.list_secrets, **kwargs)

    def get_create_model_class(self):
        return CreateSecretDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_secret,
            call_fn_args=(),
            call_fn_kwargs=dict(create_secret_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateSecretDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_secret,
            call_fn_args=(),
            call_fn_kwargs=dict(
                secret_id=self.module.params.get("secret_id"),
                update_secret_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


SecretHelperCustom = get_custom_class("SecretHelperCustom")


class ResourceHelper(SecretHelperCustom, SecretHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            key_id=dict(type="str"),
            metadata=dict(type="dict"),
            secret_content=dict(
                type="dict",
                options=dict(
                    content_type=dict(type="str", required=True, choices=["BASE64"]),
                    name=dict(type="str"),
                    stage=dict(type="str", choices=["CURRENT", "PENDING"]),
                    content=dict(type="str"),
                ),
            ),
            secret_name=dict(type="str"),
            secret_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    rule_type=dict(
                        type="str",
                        required=True,
                        choices=["SECRET_EXPIRY_RULE", "SECRET_REUSE_RULE"],
                    ),
                    secret_version_expiry_interval=dict(type="str"),
                    time_of_absolute_expiry=dict(type="str"),
                    is_secret_content_retrieval_blocked_on_expiry=dict(type="bool"),
                    is_enforced_on_deleted_secret_versions=dict(type="bool"),
                ),
            ),
            vault_id=dict(type="str"),
            secret_id=dict(aliases=["id"], type="str"),
            current_version_number=dict(type="int"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="secret",
        service_client_class=VaultsClient,
        namespace="vault",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
