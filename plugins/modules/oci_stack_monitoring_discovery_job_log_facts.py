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
module: oci_stack_monitoring_discovery_job_log_facts
short_description: Fetches details about one or multiple DiscoveryJobLog resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DiscoveryJobLog resources in Oracle Cloud Infrastructure
    - API to get all the logs of a Discovery Job.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    discovery_job_id:
        description:
            - The Discovery Job ID
        type: str
        required: true
    log_type:
        description:
            - The log type like INFO, WARNING, ERROR, SUCCESS
        type: str
        choices:
            - "INFO"
            - "WARNING"
            - "ERROR"
            - "SUCCESS"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for logType is ascending.
        type: str
        choices:
            - "timeCreated"
            - "logType"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List discovery_job_logs
  oci_stack_monitoring_discovery_job_log_facts:
    # required
    discovery_job_id: "ocid1.discoveryjob.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    log_type: INFO
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
discovery_job_logs:
    description:
        - List of DiscoveryJobLog resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of Discovery job
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        log_type:
            description:
                - Type of log (INFO, WARNING, ERROR or SUCCESS)
            returned: on success
            type: str
            sample: INFO
        log_message:
            description:
                - Log message
            returned: on success
            type: str
            sample: log_message_example
        time_created:
            description:
                - Time the Job log was created
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "log_type": "INFO",
        "log_message": "log_message_example",
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.stack_monitoring import StackMonitoringClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DiscoveryJobLogFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "discovery_job_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "log_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_discovery_job_logs,
            discovery_job_id=self.module.params.get("discovery_job_id"),
            **optional_kwargs
        )


DiscoveryJobLogFactsHelperCustom = get_custom_class("DiscoveryJobLogFactsHelperCustom")


class ResourceFactsHelper(
    DiscoveryJobLogFactsHelperCustom, DiscoveryJobLogFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            discovery_job_id=dict(type="str", required=True),
            log_type=dict(type="str", choices=["INFO", "WARNING", "ERROR", "SUCCESS"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "logType"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="discovery_job_log",
        service_client_class=StackMonitoringClient,
        namespace="stack_monitoring",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(discovery_job_logs=result)


if __name__ == "__main__":
    main()
