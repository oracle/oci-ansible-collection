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
module: oci_devops_repository_author_facts
short_description: Fetches details about one or multiple RepositoryAuthor resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RepositoryAuthor resources in Oracle Cloud Infrastructure
    - Retrieve a list of all the authors.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - Unique repository identifier.
        type: str
        required: true
    ref_name:
        description:
            - A filter to return only resources that match the given reference name.
        type: str
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
- name: List repository_authors
  oci_devops_repository_author_facts:
    # required
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    ref_name: ref_name_example
    sort_order: ASC

"""

RETURN = """
repository_authors:
    description:
        - List of RepositoryAuthor resources
    returned: on success
    type: complex
    contains:
        author_name:
            description:
                - Author name.
            returned: on success
            type: str
            sample: author_name_example
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
        "author_name": "author_name_example",
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
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RepositoryAuthorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "repository_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "ref_name",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_authors,
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )


RepositoryAuthorFactsHelperCustom = get_custom_class(
    "RepositoryAuthorFactsHelperCustom"
)


class ResourceFactsHelper(
    RepositoryAuthorFactsHelperCustom, RepositoryAuthorFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(type="str", required=True),
            ref_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="repository_author",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(repository_authors=result)


if __name__ == "__main__":
    main()
