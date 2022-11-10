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
module: oci_application_migration_source_application_facts
short_description: Fetches details about one or multiple SourceApplication resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SourceApplication resources in Oracle Cloud Infrastructure
    - Retrieves details of all the applications associated with the specified source.
      This list is generated dynamically by interrogating the source and the list changes as applications are started or
      stopped in the source environment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source.
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a compartment. Retrieves details of objects in the
              specified compartment.
        type: str
        required: true
    sort_order:
        description:
            - The sort order, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the field on which to sort.
              By default, `TIMECREATED` is ordered descending.
              By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    display_name:
        description:
            - Resource name on which to query.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List source_applications
  oci_application_migration_source_application_facts:
    # required
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: TIMECREATED
    display_name: display_name_example

"""

RETURN = """
source_applications:
    description:
        - List of SourceApplication resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the application.
            returned: on success
            type: str
            sample: name_example
        type:
            description:
                - The type of the application.
            returned: on success
            type: str
            sample: JCS
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source to which the application belongs.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        version:
            description:
                - The version of the application.
            returned: on success
            type: str
            sample: version_example
        state:
            description:
                - The current state of the application.
            returned: on success
            type: str
            sample: state_example
    sample: [{
        "name": "name_example",
        "type": "JCS",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "version": "version_example",
        "state": "state_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.application_migration import ApplicationMigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SourceApplicationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "source_id",
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "display_name",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_source_applications,
            source_id=self.module.params.get("source_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SourceApplicationFactsHelperCustom = get_custom_class(
    "SourceApplicationFactsHelperCustom"
)


class ResourceFactsHelper(
    SourceApplicationFactsHelperCustom, SourceApplicationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            source_id=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            display_name=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="source_application",
        service_client_class=ApplicationMigrationClient,
        namespace="application_migration",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(source_applications=result)


if __name__ == "__main__":
    main()
