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
module: oci_database_management_open_alert_history_facts
short_description: Fetches details about a OpenAlertHistory resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a OpenAlertHistory resource in Oracle Cloud Infrastructure
    - Get open alerts from storage server.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_exadata_storage_server_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific open_alert_history
  oci_database_management_open_alert_history_facts:
    # required
    external_exadata_storage_server_id: "ocid1.externalexadatastorageserver.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
open_alert_history:
    description:
        - OpenAlertHistory resource
    returned: on success
    type: complex
    contains:
        alerts:
            description:
                - A list of open alerts.
            returned: on success
            type: complex
            contains:
                severity:
                    description:
                        - The severity of the alert.
                    returned: on success
                    type: str
                    sample: CLEAR
                type:
                    description:
                        - The type of the alert.
                    returned: on success
                    type: str
                    sample: STATEFUL
                time_start_at:
                    description:
                        - The start time of the alert.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                message:
                    description:
                        - The alert message.
                    returned: on success
                    type: str
                    sample: message_example
    sample: {
        "alerts": [{
            "severity": "CLEAR",
            "type": "STATEFUL",
            "time_start_at": "2013-10-20T19:20:30+01:00",
            "message": "message_example"
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpenAlertHistoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "external_exadata_storage_server_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_open_alert_history,
            external_exadata_storage_server_id=self.module.params.get(
                "external_exadata_storage_server_id"
            ),
        )


OpenAlertHistoryFactsHelperCustom = get_custom_class(
    "OpenAlertHistoryFactsHelperCustom"
)


class ResourceFactsHelper(
    OpenAlertHistoryFactsHelperCustom, OpenAlertHistoryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_exadata_storage_server_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="open_alert_history",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(open_alert_history=result)


if __name__ == "__main__":
    main()
