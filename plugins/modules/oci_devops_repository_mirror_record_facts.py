#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_devops_repository_mirror_record_facts
short_description: Fetches details about one or multiple RepositoryMirrorRecord resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RepositoryMirrorRecord resources in Oracle Cloud Infrastructure
    - Returns a list of mirror entry in history within 30 days
    - If I(mirror_record_type) is specified, the details of a single RepositoryMirrorRecord will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - unique Repository identifier.
        type: str
        required: true
    mirror_record_type:
        description:
            - "The field of mirror record type. Only one mirror record type may be provided.
              current - The current mirror record.
              lastSuccessful - The last successful mirror record"
            - Required to get a specific repository_mirror_record.
        type: str
        choices:
            - "current"
            - "lastSuccessful"
    sort_order:
        description:
            - The sort order to use. Use either ascending or descending.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific repository_mirror_record
  oci_devops_repository_mirror_record_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    mirror_record_type: current

- name: List repository_mirror_records
  oci_devops_repository_mirror_record_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC

"""

RETURN = """
repository_mirror_records:
    description:
        - List of RepositoryMirrorRecord resources
    returned: on success
    type: complex
    contains:
        mirror_status:
            description:
                - "Mirror status of current mirror entry.
                  QUEUED - Mirroring Queued
                  RUNNING - Mirroring is Running
                  PASSED - Mirroring Passed
                  FAILED - Mirroring Failed"
            returned: on success
            type: str
            sample: NONE
        work_request_id:
            description:
                - Workrequest Id to track current mirror operation
            returned: on success
            type: str
            sample: "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx"
        time_enqueued:
            description:
                - The time to enqueue a mirror operation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - The time to start a mirror operation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - Time that the mirror operation ended or null if it hasn't yet ended.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_completed:
            description:
                - The time complete a mirror operation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "mirror_status": "NONE",
        "work_request_id": "ocid1.workrequest.oc1..xxxxxxEXAMPLExxxxxx",
        "time_enqueued": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "time_completed": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RepositoryMirrorRecordFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
            "mirror_record_type",
        ]

    def get_required_params_for_list(self):
        return [
            "repository_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_mirror_record,
            repository_id=self.module.params.get("repository_id"),
            mirror_record_type=self.module.params.get("mirror_record_type"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_mirror_records,
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )


RepositoryMirrorRecordFactsHelperCustom = get_custom_class(
    "RepositoryMirrorRecordFactsHelperCustom"
)


class ResourceFactsHelper(
    RepositoryMirrorRecordFactsHelperCustom, RepositoryMirrorRecordFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(type="str", required=True),
            mirror_record_type=dict(type="str", choices=["current", "lastSuccessful"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repository_mirror_record",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(repository_mirror_records=result)


if __name__ == "__main__":
    main()
