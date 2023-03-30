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
module: oci_golden_gate_deployment_wallets_operation_facts
short_description: Fetches details about one or multiple DeploymentWalletsOperation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DeploymentWalletsOperation resources in Oracle Cloud Infrastructure
    - Lists the wallets export/import operations to/from a deployment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    deployment_id:
        description:
            - A unique Deployment identifier.
        type: str
        required: true
    display_name:
        description:
            - A filter to return only the resources that match the entire 'displayName' given.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeStarted' is
              descending.
        type: str
        choices:
            - "timeStarted"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List deployment_wallets_operations
  oci_golden_gate_deployment_wallets_operation_facts:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: timeStarted
    sort_order: ASC

"""

RETURN = """
deployment_wallets_operations:
    description:
        - List of DeploymentWalletsOperation resources
    returned: on success
    type: complex
    contains:
        wallet_operation_id:
            description:
                - The UUID of the wallet operation performed by the customer.
                  If provided, this will reference a key which the customer can use to query or search a particular wallet operation
            returned: on success
            type: str
            sample: "ocid1.walletoperation.oc1..xxxxxxEXAMPLExxxxxx"
        wallet_secret_id:
            description:
                - The OCID of the customer's GoldenGate Service Secret.
                  If provided, it references a key that customers will be required to ensure the policies are established
                  to permit GoldenGate to use this Secret.
            returned: on success
            type: str
            sample: "ocid1.walletsecret.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_wallet_operation_type:
            description:
                - The operation type of the deployment wallet.
            returned: on success
            type: str
            sample: EXPORT
        deployment_wallet_operation_status:
            description:
                - The status of the deployment wallet.
            returned: on success
            type: str
            sample: EXPORTING
        time_started:
            description:
                - The date and time the request was started. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_completed:
            description:
                - The date and time the request was finished. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "wallet_operation_id": "ocid1.walletoperation.oc1..xxxxxxEXAMPLExxxxxx",
        "wallet_secret_id": "ocid1.walletsecret.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_wallet_operation_type": "EXPORT",
        "deployment_wallet_operation_status": "EXPORTING",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_completed": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentWalletsOperationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "deployment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_deployment_wallets_operations,
            deployment_id=self.module.params.get("deployment_id"),
            **optional_kwargs
        )


DeploymentWalletsOperationFactsHelperCustom = get_custom_class(
    "DeploymentWalletsOperationFactsHelperCustom"
)


class ResourceFactsHelper(
    DeploymentWalletsOperationFactsHelperCustom,
    DeploymentWalletsOperationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deployment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["timeStarted"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="deployment_wallets_operation",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(deployment_wallets_operations=result)


if __name__ == "__main__":
    main()
