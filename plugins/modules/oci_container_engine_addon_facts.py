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
module: oci_container_engine_addon_facts
short_description: Fetches details about one or multiple Addon resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Addon resources in Oracle Cloud Infrastructure
    - List addon for a provisioned cluster.
    - If I(addon_name) is specified, the details of a single Addon will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    addon_name:
        description:
            - The name of the addon.
            - Required to get a specific addon.
        type: str
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    sort_order:
        description:
            - The optional order in which to sort the results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The optional field to sort the results by.
        type: str
        choices:
            - "NAME"
            - "TIME_CREATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific addon
  oci_container_engine_addon_facts:
    # required
    addon_name: addon_name_example
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: List addons
  oci_container_engine_addon_facts:
    # required
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: NAME

"""

RETURN = """
addons:
    description:
        - List of Addon resources
    returned: on success
    type: complex
    contains:
        configurations:
            description:
                - Addon configuration details.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - configuration key name
                    returned: on success
                    type: str
                    sample: key_example
                value:
                    description:
                        - configuration value name
                    returned: on success
                    type: str
                    sample: value_example
        name:
            description:
                - The name of the addon.
            returned: on success
            type: str
            sample: name_example
        version:
            description:
                - selected addon version, or null indicates autoUpdate
            returned: on success
            type: str
            sample: version_example
        current_installed_version:
            description:
                - current installed version of the addon
            returned: on success
            type: str
            sample: current_installed_version_example
        time_created:
            description:
                - The time the cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the addon.
            returned: on success
            type: str
            sample: CREATING
        addon_error:
            description:
                - The error info of the addon.
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - A short error code that defines the upstream error, meant for programmatic parsing. See L(API Errors,https://docs.us-
                          phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm).
                    returned: on success
                    type: str
                    sample: code_example
                message:
                    description:
                        - A human-readable error string of the upstream error.
                    returned: on success
                    type: str
                    sample: message_example
                status:
                    description:
                        - The status of the HTTP response encountered in the upstream error.
                    returned: on success
                    type: str
                    sample: status_example
    sample: [{
        "configurations": [{
            "key": "key_example",
            "value": "value_example"
        }],
        "name": "name_example",
        "version": "version_example",
        "current_installed_version": "current_installed_version_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "addon_error": {
            "code": "code_example",
            "message": "message_example",
            "status": "status_example"
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddonFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cluster_id",
            "addon_name",
        ]

    def get_required_params_for_list(self):
        return [
            "cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_addon,
            cluster_id=self.module.params.get("cluster_id"),
            addon_name=self.module.params.get("addon_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_addons,
            cluster_id=self.module.params.get("cluster_id"),
            **optional_kwargs
        )


AddonFactsHelperCustom = get_custom_class("AddonFactsHelperCustom")


class ResourceFactsHelper(AddonFactsHelperCustom, AddonFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            addon_name=dict(type="str"),
            cluster_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAME", "TIME_CREATED"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="addon",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(addons=result)


if __name__ == "__main__":
    main()
