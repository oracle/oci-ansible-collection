#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_os_management_software_source_actions
short_description: Perform actions on a SoftwareSource resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SoftwareSource resource in Oracle Cloud Infrastructure
    - For I(action=add_packages), adds a given list of Software Packages to a specific Software Source.
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, If-Match
      is checked against ETag values of the resource.
    - For I(action=remove_packages), removes a given list of Software Packages from a specific Software Source.
version_added: "2.9"
author: Oracle (@oracle)
options:
    software_source_id:
        description:
            - The OCID of the software source.
        type: str
        aliases: ["id"]
        required: true
    package_names:
        description:
            - the list of package names
            - Required for I(action=add_packages), I(action=remove_packages).
        type: list
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              compartment into which the resource should be moved.
            - Applicable only for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the SoftwareSource.
        type: str
        required: true
        choices:
            - "add_packages"
            - "change_compartment"
            - "remove_packages"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action add_packages on software_source
  oci_os_management_software_source_actions:
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_packages

- name: Perform action change_compartment on software_source
  oci_os_management_software_source_actions:
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_packages on software_source
  oci_os_management_software_source_actions:
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_packages

"""

RETURN = """
software_source:
    description:
        - Details of the SoftwareSource resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID for the Software Source
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
            sample: "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx"
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
            sample: "ocid1.gpgkey.oc1..xxxxxxEXAMPLExxxxxx"
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
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: {
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient
    from oci.os_management.models import AddPackagesToSoftwareSourceDetails
    from oci.os_management.models import ChangeSoftwareSourceCompartmentDetails
    from oci.os_management.models import RemovePackagesFromSoftwareSourceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SoftwareSourceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_packages
        change_compartment
        remove_packages
    """

    @staticmethod
    def get_module_resource_id_param():
        return "software_source_id"

    def get_module_resource_id(self):
        return self.module.params.get("software_source_id")

    def get_get_fn(self):
        return self.client.get_software_source

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_software_source,
            software_source_id=self.module.params.get("software_source_id"),
        )

    def add_packages(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddPackagesToSoftwareSourceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_packages_to_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
                add_packages_to_software_source_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSoftwareSourceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_software_source_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
                change_software_source_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def remove_packages(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemovePackagesFromSoftwareSourceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_packages_from_software_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                software_source_id=self.module.params.get("software_source_id"),
                remove_packages_from_software_source_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


SoftwareSourceActionsHelperCustom = get_custom_class(
    "SoftwareSourceActionsHelperCustom"
)


class ResourceHelper(SoftwareSourceActionsHelperCustom, SoftwareSourceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            software_source_id=dict(aliases=["id"], type="str", required=True),
            package_names=dict(type="list"),
            compartment_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["add_packages", "change_compartment", "remove_packages"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="software_source",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
