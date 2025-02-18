#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_oda_translator_facts
short_description: Fetches details about one or multiple Translator resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Translator resources in Oracle Cloud Infrastructure
    - Returns a page of Translators that belong to the specified Digital Assistant instance.
    - If the `opc-next-page` header appears in the response, then
      there are more items to retrieve. To get the next page in the subsequent
      GET request, include the header's value as the `page` query parameter.
    - If I(translator_id) is specified, the details of a single Translator will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    translator_id:
        description:
            - Unique Translator identifier.
            - Required to get a specific translator.
        type: str
        aliases: ["id"]
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    type:
        description:
            - List only Translators of this type.
        type: str
        choices:
            - "GOOGLE"
            - "MICROSOFT"
    name:
        description:
            - List only Translators with this name. Translator names are unique and may not change.
            - "Example: `MyTranslator`"
        type: str
    lifecycle_state:
        description:
            - List only the resources that are in this lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.
            - The default sort order for `timeCreated` and `timeUpdated` is descending.
              For all other sort fields the default sort order is ascending.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "name"
            - "type"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific translator
  oci_oda_translator_facts:
    # required
    translator_id: "ocid1.translator.oc1..xxxxxxEXAMPLExxxxxx"
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List translators
  oci_oda_translator_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    type: GOOGLE
    name: name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
translators:
    description:
        - List of Translator resources
    returned: on success
    type: complex
    contains:
        base_url:
            description:
                - The base URL for invoking the Translation Service.
                - Returned for get operation
            returned: on success
            type: str
            sample: base_url_example
        properties:
            description:
                - Properties used when invoking the translation service.
                  Each property is a simple key-value pair.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
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
        lifecycle_state:
            description:
                - The Translator's current state.
            returned: on success
            type: str
            sample: CREATING
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
    sample: [{
        "base_url": "base_url_example",
        "properties": {},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "GOOGLE",
        "name": "name_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.oda import ManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TranslatorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
            "translator_id",
        ]

    def get_required_params_for_list(self):
        return [
            "oda_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_translator,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            translator_id=self.module.params.get("translator_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "type",
            "name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_translators,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            **optional_kwargs
        )


TranslatorFactsHelperCustom = get_custom_class("TranslatorFactsHelperCustom")


class ResourceFactsHelper(TranslatorFactsHelperCustom, TranslatorFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            translator_id=dict(aliases=["id"], type="str"),
            oda_instance_id=dict(type="str", required=True),
            type=dict(type="str", choices=["GOOGLE", "MICROSOFT"]),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeCreated", "timeUpdated", "name", "type"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="translator",
        service_client_class=ManagementClient,
        namespace="oda",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(translators=result)


if __name__ == "__main__":
    main()
