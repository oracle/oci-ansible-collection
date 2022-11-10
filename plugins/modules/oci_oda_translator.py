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
module: oci_oda_translator
short_description: Manage a Translator resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Translator resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Translator
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    type:
        description:
            - The Translation Service to use for this Translator.
            - Required for create using I(state=present).
        type: str
        choices:
            - "GOOGLE"
            - "MICROSOFT"
    base_url:
        description:
            - The base URL for invoking the Translation Service.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    auth_token:
        description:
            - The authentication token to use when invoking the Translation Service
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    properties:
        description:
            - Properties used when invoking the translation service.
              Each property is a simple key-value pair.
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    translator_id:
        description:
            - Unique Translator identifier.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Translator.
            - Use I(state=present) to create or update a Translator.
            - Use I(state=absent) to delete a Translator.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create translator
  oci_oda_translator:
    # required
    type: GOOGLE
    base_url: base_url_example
    auth_token: auth_token_example
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    properties: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update translator
  oci_oda_translator:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    translator_id: "ocid1.translator.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    base_url: base_url_example
    auth_token: auth_token_example
    properties: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete translator
  oci_oda_translator:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    translator_id: "ocid1.translator.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
translator:
    description:
        - Details of the Translator resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique immutable identifier that was assigned when the Translator was created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - The Translation Service to use for this Translator.
            returned: on success
            type: str
            sample: GOOGLE
        name:
            description:
                - The descriptive name for this Translator.
            returned: on success
            type: str
            sample: name_example
        base_url:
            description:
                - The base URL for invoking the Translation Service.
            returned: on success
            type: str
            sample: base_url_example
        lifecycle_state:
            description:
                - The Translator's current state.
            returned: on success
            type: str
            sample: CREATING
        properties:
            description:
                - Properties used when invoking the translation service.
                  Each property is a simple key-value pair.
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - When the resource was created. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the resource was last updated. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "type": "GOOGLE",
        "name": "name_example",
        "base_url": "base_url_example",
        "lifecycle_state": "CREATING",
        "properties": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.oda import ManagementClient
    from oci.oda.models import CreateTranslatorDetails
    from oci.oda.models import UpdateTranslatorDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TranslatorHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TranslatorHelperGen, self).get_possible_entity_types() + [
            "translator",
            "translators",
            "odatranslator",
            "odatranslators",
            "translatorresource",
            "translatorsresource",
            "oda",
        ]

    def get_module_resource_id_param(self):
        return "translator_id"

    def get_module_resource_id(self):
        return self.module.params.get("translator_id")

    def get_get_fn(self):
        return self.client.get_translator

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_translator,
            translator_id=summary_model.id,
            oda_instance_id=self.module.params.get("oda_instance_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_translator,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            translator_id=self.module.params.get("translator_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "oda_instance_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["type"]

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
            self.client.list_translators, **kwargs
        )

    def get_create_model_class(self):
        return CreateTranslatorDetails

    def get_exclude_attributes(self):
        return ["auth_token"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_translator,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                create_translator_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTranslatorDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_translator,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                translator_id=self.module.params.get("translator_id"),
                update_translator_details=update_details,
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
            call_fn=self.client.delete_translator,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                translator_id=self.module.params.get("translator_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TranslatorHelperCustom = get_custom_class("TranslatorHelperCustom")


class ResourceHelper(TranslatorHelperCustom, TranslatorHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            type=dict(type="str", choices=["GOOGLE", "MICROSOFT"]),
            base_url=dict(type="str"),
            auth_token=dict(type="str", no_log=True),
            properties=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            oda_instance_id=dict(type="str", required=True),
            translator_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="translator",
        service_client_class=ManagementClient,
        namespace="oda",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
