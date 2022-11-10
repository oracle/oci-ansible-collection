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
module: oci_os_management_errata_facts
short_description: Fetches details about one or multiple Errata resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Errata resources in Oracle Cloud Infrastructure
    - Returns a list of all of the currently available Errata in the system
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
        type: str
    erratum_id:
        description:
            - The OCID of the erratum.
        type: str
    advisory_name:
        description:
            - The assigned erratum name. It's unique and not changeable.
            - "Example: `ELSA-2020-5804`"
        type: str
    time_issue_date_start:
        description:
            - The issue date after which to list all errata, in ISO 8601 format
            - "Example: 2017-07-14T02:40:00.000Z"
        type: str
    time_issue_date_end:
        description:
            - The issue date before which to list all errata, in ISO 8601 format
            - "Example: 2017-07-14T02:40:00.000Z"
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort errata by. Only one sort order may be provided. Default order for ISSUEDATE is descending. Default order for ADVISORYNAME is
              ascending. If no value is specified ISSUEDATE is default.
        type: str
        choices:
            - "ISSUEDATE"
            - "ADVISORYNAME"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List errata
  oci_os_management_errata_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    erratum_id: "ocid1.erratum.oc1..xxxxxxEXAMPLExxxxxx"
    advisory_name: advisory_name_example
    time_issue_date_start: 2013-10-20T19:20:30+01:00
    time_issue_date_end: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: ISSUEDATE

"""

RETURN = """
errata:
    description:
        - List of Errata resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Advisory name
            returned: on success
            type: str
            sample: name_example
        id:
            description:
                - OCID for the Erratum.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID for the Compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        synopsis:
            description:
                - Summary description of the erratum.
            returned: on success
            type: str
            sample: synopsis_example
        issued:
            description:
                - date the erratum was issued
            returned: on success
            type: str
            sample: issued_example
        updated:
            description:
                - most recent date the erratum was updated
            returned: on success
            type: str
            sample: updated_example
        advisory_type:
            description:
                - Type of the erratum.
            returned: on success
            type: str
            sample: SECURITY
        related_cves:
            description:
                - list of CVEs applicable to this erratum
            returned: on success
            type: list
            sample: []
    sample: [{
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "synopsis": "synopsis_example",
        "issued": "issued_example",
        "updated": "updated_example",
        "advisory_type": "SECURITY",
        "related_cves": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ErrataFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "erratum_id",
            "advisory_name",
            "time_issue_date_start",
            "time_issue_date_end",
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_errata, **optional_kwargs
        )


ErrataFactsHelperCustom = get_custom_class("ErrataFactsHelperCustom")


class ResourceFactsHelper(ErrataFactsHelperCustom, ErrataFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            erratum_id=dict(type="str"),
            advisory_name=dict(type="str"),
            time_issue_date_start=dict(type="str"),
            time_issue_date_end=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ISSUEDATE", "ADVISORYNAME"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="errata",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(errata=result)


if __name__ == "__main__":
    main()
