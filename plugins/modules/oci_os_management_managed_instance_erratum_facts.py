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
module: oci_os_management_managed_instance_erratum_facts
short_description: Fetches details about one or multiple ManagedInstanceErratum resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedInstanceErratum resources in Oracle Cloud Infrastructure
    - Returns a list of errata relevant to the Managed Instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - OCID for the managed instance
        type: str
        required: true
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
    compartment_id:
        description:
            - The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
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
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List managed_instance_errata
  oci_os_management_managed_instance_erratum_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
managed_instance_errata:
    description:
        - List of ManagedInstanceErratum resources
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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceErratumFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "compartment_id",
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
            self.client.list_managed_instance_errata,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


ManagedInstanceErratumFactsHelperCustom = get_custom_class(
    "ManagedInstanceErratumFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagedInstanceErratumFactsHelperCustom, ManagedInstanceErratumFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            display_name=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance_erratum",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instance_errata=result)


if __name__ == "__main__":
    main()
