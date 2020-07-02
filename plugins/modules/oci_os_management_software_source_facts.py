#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_os_management_software_source_facts
short_description: Fetches details about one or multiple SoftwareSource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SoftwareSource resources in Oracle Cloud Infrastructure
    - Returns a list of all Software Sources.
    - If I(software_source_id) is specified, the details of a single SoftwareSource will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    software_source_id:
        description:
            - The OCID of the software source.
            - Required to get a specific software_source.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple software_sources.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
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
    lifecycle_state:
        description:
            - The current lifecycle state for the object.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List software_sources
  oci_os_management_software_source_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific software_source
  oci_os_management_software_source_facts:
    software_source_id: ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
software_sources:
    description:
        - List of SoftwareSource resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID for the Software Source
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - User friendly name for the software source
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Information specified by the user about the software source
            returned: on success
            type: string
            sample: description_example
        repo_type:
            description:
                - Type of the Software Source
            returned: on success
            type: string
            sample: repo_type_example
        arch_type:
            description:
                - The architecture type supported by the Software Source
            returned: on success
            type: string
            sample: IA_32
        url:
            description:
                - URL for the repostiory
            returned: on success
            type: string
            sample: url_example
        parent_id:
            description:
                - OCID for the parent software source, if there is one
            returned: on success
            type: string
            sample: ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx
        parent_name:
            description:
                - Display name the parent software source, if there is one
            returned: on success
            type: string
            sample: parent_name_example
        checksum_type:
            description:
                - The yum repository checksum type used by this software source
            returned: on success
            type: string
            sample: SHA1
        maintainer_name:
            description:
                - Name of the person maintaining this software source
            returned: on success
            type: string
            sample: maintainer_name_example
        maintainer_email:
            description:
                - Email address of the person maintaining this software source
            returned: on success
            type: string
            sample: maintainer_email_example
        maintainer_phone:
            description:
                - Phone number of the person maintaining this software source
            returned: on success
            type: string
            sample: maintainer_phone_example
        gpg_key_url:
            description:
                - URL of the GPG key for this software source
            returned: on success
            type: string
            sample: gpg_key_url_example
        gpg_key_id:
            description:
                - ID of the GPG key for this software source
            returned: on success
            type: string
            sample: ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx
        gpg_key_fingerprint:
            description:
                - Fingerprint of the GPG key for this software source
            returned: on success
            type: string
            sample: gpg_key_fingerprint_example
        status:
            description:
                - status of the software source.
            returned: on success
            type: string
            sample: NORMAL
        lifecycle_state:
            description:
                - The current state of the Software Source.
            returned: on success
            type: string
            sample: CREATING
        packages:
            description:
                - Number of packages
            returned: on success
            type: int
            sample: 56
        associated_managed_instances:
            description:
                - list of the Managed Instances associated with this Software Sources
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: string
                    sample: display_name_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "repo_type": "repo_type_example",
        "arch_type": "IA_32",
        "url": "url_example",
        "parent_id": "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_name": "parent_name_example",
        "checksum_type": "SHA1",
        "maintainer_name": "maintainer_name_example",
        "maintainer_email": "maintainer_email_example",
        "maintainer_phone": "maintainer_phone_example",
        "gpg_key_url": "gpg_key_url_example",
        "gpg_key_id": "ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx",
        "gpg_key_fingerprint": "gpg_key_fingerprint_example",
        "status": "NORMAL",
        "lifecycle_state": "CREATING",
        "packages": 56,
        "associated_managed_instances": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
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
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SoftwareSourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "software_source_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_source,
            software_source_id=self.module.params.get("software_source_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_software_sources,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SoftwareSourceFactsHelperCustom = get_custom_class("SoftwareSourceFactsHelperCustom")


class ResourceFactsHelper(
    SoftwareSourceFactsHelperCustom, SoftwareSourceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_source_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="software_source",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(software_sources=result)


if __name__ == "__main__":
    main()
