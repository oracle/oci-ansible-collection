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
module: oci_bds_api_key_facts
short_description: Fetches details about one or multiple BdsApiKey resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BdsApiKey resources in Oracle Cloud Infrastructure
    - Returns a list of all API keys associated with this Big Data Service cluster.
    - If I(api_key_id) is specified, the details of a single BdsApiKey will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    api_key_id:
        description:
            - The API key identifier.
            - Required to get a specific bds_api_key.
        type: str
        aliases: ["id"]
    lifecycle_state:
        description:
            - The state of the API key.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    user_id:
        description:
            - The OCID of the user for whom the API key belongs.
        type: str
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific bds_api_key
  oci_bds_api_key_facts:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    api_key_id: "ocid1.apikey.oc1..xxxxxxEXAMPLExxxxxx"

- name: List bds_api_keys
  oci_bds_api_key_facts:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: timeCreated
    sort_order: ASC
    display_name: display_name_example

"""

RETURN = """
bds_api_keys:
    description:
        - List of BdsApiKey resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Identifier of the user's API key.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The user OCID for which this API key was created.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        key_alias:
            description:
                - User friendly identifier used to uniquely differentiate between different API keys.
                  Only ASCII alphanumeric characters with no spaces allowed.
            returned: on success
            type: str
            sample: key_alias_example
        default_region:
            description:
                - The name of the region to establish the Object Storage endpoint. Example us-phoenix-1 .
            returned: on success
            type: str
            sample: us-phoenix-1
        tenant_id:
            description:
                - The OCID of your tenancy.
            returned: on success
            type: str
            sample: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        fingerprint:
            description:
                - The fingerprint that corresponds to the public API key requested.
            returned: on success
            type: str
            sample: fingerprint_example
        pemfilepath:
            description:
                - The full path and file name of the private key used for authentication. This location will be automatically selected
                  on the BDS local file system.
            returned: on success
            type: str
            sample: pemfilepath_example
        time_created:
            description:
                - The time the API key was created, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the key.
            returned: on success
            type: str
            sample: CREATING
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "key_alias": "key_alias_example",
        "default_region": "us-phoenix-1",
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "fingerprint": "fingerprint_example",
        "pemfilepath": "pemfilepath_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.bds import BdsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsApiKeyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "bds_instance_id",
            "api_key_id",
        ]

    def get_required_params_for_list(self):
        return [
            "bds_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_api_key,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            api_key_id=self.module.params.get("api_key_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "user_id",
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_bds_api_keys,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            **optional_kwargs
        )


BdsApiKeyFactsHelperCustom = get_custom_class("BdsApiKeyFactsHelperCustom")


class ResourceFactsHelper(BdsApiKeyFactsHelperCustom, BdsApiKeyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            bds_instance_id=dict(type="str", required=True),
            api_key_id=dict(aliases=["id"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            user_id=dict(type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bds_api_key",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(bds_api_keys=result)


if __name__ == "__main__":
    main()
