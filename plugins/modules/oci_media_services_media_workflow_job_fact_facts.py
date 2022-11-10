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
module: oci_media_services_media_workflow_job_fact_facts
short_description: Fetches details about one or multiple MediaWorkflowJobFact resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MediaWorkflowJobFact resources in Oracle Cloud Infrastructure
    - Internal API to get a point-in-time snapshot of a MediaWorkflowJob.
    - If I(key) is specified, the details of a single MediaWorkflowJobFact will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    media_workflow_job_id:
        description:
            - Unique MediaWorkflowJob identifier.
        type: str
        required: true
    key:
        description:
            - Identifier of the MediaWorkflowJobFact within a MediaWorkflowJob.
            - Required to get a specific media_workflow_job_fact.
        type: int
    type:
        description:
            - Types of details to include.
        type: str
        choices:
            - "runnableJob"
            - "taskDeclaration"
            - "workflow"
            - "configuration"
            - "parameterResolutionEvent"
    sort_by:
        description:
            - Types of details to include.
        type: str
        choices:
            - "key"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific media_workflow_job_fact
  oci_media_services_media_workflow_job_fact_facts:
    # required
    media_workflow_job_id: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
    key: 56

- name: List media_workflow_job_facts
  oci_media_services_media_workflow_job_fact_facts:
    # required
    media_workflow_job_id: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    key: 56
    type: runnableJob
    sort_by: key
    sort_order: ASC

"""

RETURN = """
media_workflow_job_facts:
    description:
        - List of MediaWorkflowJobFact resources
    returned: on success
    type: complex
    contains:
        detail:
            description:
                - The body of the detail captured as JSON.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        media_workflow_job_id:
            description:
                - Reference to the parent job.
            returned: on success
            type: str
            sample: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
        key:
            description:
                - System generated serial number to uniquely identify a detail in order within a MediaWorkflowJob.
            returned: on success
            type: int
            sample: 56
        name:
            description:
                - Unique name. It is read-only and generated for the fact.
            returned: on success
            type: str
            sample: name_example
        type:
            description:
                - The type of information contained in this detail.
            returned: on success
            type: str
            sample: type_example
    sample: [{
        "detail": {},
        "media_workflow_job_id": "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx",
        "key": 56,
        "name": "name_example",
        "type": "type_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.media_services import MediaServicesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaWorkflowJobFactFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "media_workflow_job_id",
            "key",
        ]

    def get_required_params_for_list(self):
        return [
            "media_workflow_job_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow_job_fact,
            media_workflow_job_id=self.module.params.get("media_workflow_job_id"),
            key=self.module.params.get("key"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "key",
            "type",
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_media_workflow_job_facts,
            media_workflow_job_id=self.module.params.get("media_workflow_job_id"),
            **optional_kwargs
        )


MediaWorkflowJobFactFactsHelperCustom = get_custom_class(
    "MediaWorkflowJobFactFactsHelperCustom"
)


class ResourceFactsHelper(
    MediaWorkflowJobFactFactsHelperCustom, MediaWorkflowJobFactFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            media_workflow_job_id=dict(type="str", required=True),
            key=dict(type="int", no_log=True),
            type=dict(
                type="str",
                choices=[
                    "runnableJob",
                    "taskDeclaration",
                    "workflow",
                    "configuration",
                    "parameterResolutionEvent",
                ],
            ),
            sort_by=dict(type="str", choices=["key"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="media_workflow_job_fact",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(media_workflow_job_facts=result)


if __name__ == "__main__":
    main()
