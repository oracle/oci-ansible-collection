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
module: oci_identity_provider_group_facts
short_description: Fetches details about one or multiple IdentityProviderGroup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple IdentityProviderGroup resources in Oracle Cloud Infrastructure
    - Lists the identity provider groups.
version_added: "2.9"
author: Oracle (@oracle)
options:
    identity_provider_id:
        description:
            - The OCID of the identity provider.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List identity_provider_groups
  oci_identity_provider_group_facts:
    identity_provider_id: ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
identity_provider_groups:
    description:
        - List of IdentityProviderGroup resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the `IdentityProviderGroup`.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        identity_provider_id:
            description:
                - The OCID of the `IdentityProvider` this group belongs to.
            returned: on success
            type: string
            sample: ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - Display name of the group
            returned: on success
            type: string
            sample: display_name_example
        external_identifier:
            description:
                - Identifier of the group in the identity provider
            returned: on success
            type: string
            sample: external_identifier_example
        time_created:
            description:
                - Date and time the `IdentityProviderGroup` was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_modified:
            description:
                - Date and time the `IdentityProviderGroup` was last modified, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "identity_provider_id": "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "external_identifier": "external_identifier_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_modified": "2016-08-25T21:10:29.600Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IdentityProviderGroupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "identity_provider_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_identity_provider_groups,
            identity_provider_id=self.module.params.get("identity_provider_id"),
            **optional_kwargs
        )


IdentityProviderGroupFactsHelperCustom = get_custom_class(
    "IdentityProviderGroupFactsHelperCustom"
)


class ResourceFactsHelper(
    IdentityProviderGroupFactsHelperCustom, IdentityProviderGroupFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            identity_provider_id=dict(type="str", required=True),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="identity_provider_group",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(identity_provider_groups=result)


if __name__ == "__main__":
    main()
