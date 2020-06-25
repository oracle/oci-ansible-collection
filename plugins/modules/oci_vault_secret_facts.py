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
module: oci_vault_secret_facts
short_description: Fetches details about one or multiple Secret resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Secret resources in Oracle Cloud Infrastructure
    - Lists all secrets in the specified vault and compartment.
    - If I(secret_id) is specified, the details of a single Secret will be returned.
version_added: "2.5"
options:
    secret_id:
        description:
            - The OCID of the secret.
            - Required to get a specific secret.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple secrets.
        type: str
    name:
        description:
            - The secret name.
        type: str
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order. The default order for
              `TIMECREATED` is descending. The default order for `NAME` is ascending.
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    vault_id:
        description:
            - The OCID of the vault.
        type: str
    lifecycle_state:
        description:
            - A filter that returns only resources that match the specified lifecycle state. The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "SCHEDULING_DELETION"
            - "PENDING_DELETION"
            - "CANCELLING_DELETION"
            - "FAILED"
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List secrets
  oci_vault_secret_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific secret
  oci_vault_secret_facts:
    secret_id: ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
secrets:
    description:
        - List of Secret resources
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.vault import VaultsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecretFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "secret_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_secret, secret_id=self.module.params.get("secret_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_by",
            "sort_order",
            "vault_id",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_secrets,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SecretFactsHelperCustom = get_custom_class("SecretFactsHelperCustom")


class ResourceFactsHelper(SecretFactsHelperCustom, SecretFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            secret_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            vault_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "SCHEDULING_DELETION",
                    "PENDING_DELETION",
                    "CANCELLING_DELETION",
                    "FAILED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="secret",
        service_client_class=VaultsClient,
        namespace="vault",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(secrets=result)


if __name__ == "__main__":
    main()
