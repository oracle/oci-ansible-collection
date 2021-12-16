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
module: oci_marketplace_publication_actions
short_description: Perform actions on a Publication resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Publication resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified publication from one compartment to another.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    publication_id:
        description:
            - The unique identifier for the publication.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where you want to move the publication.
        type: str
    action:
        description:
            - The action to perform on the Publication.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on publication
  oci_marketplace_publication_actions:
    # required
    publication_id: "ocid1.publication.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
publication:
    description:
        - Details of the Publication resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The lifecycle state of the publication.
            returned: on success
            type: str
            sample: CREATING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the publication exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The unique identifier for the publication in Marketplace.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the publication, which is also used in the listing.
            returned: on success
            type: str
            sample: name_example
        short_description:
            description:
                - A short description of the publication to use in the listing.
            returned: on success
            type: str
            sample: short_description_example
        long_description:
            description:
                - A long description of the publication to use in the listing.
            returned: on success
            type: str
            sample: long_description_example
        support_contacts:
            description:
                - Contact information for getting support from the publisher for the listing.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the contact.
                    returned: on success
                    type: str
                    sample: name_example
                phone:
                    description:
                        - The phone number of the contact.
                    returned: on success
                    type: str
                    sample: phone_example
                email:
                    description:
                        - The email of the contact.
                    returned: on success
                    type: str
                    sample: email_example
                subject:
                    description:
                        - The email subject line to use when contacting support.
                    returned: on success
                    type: str
                    sample: subject_example
        icon:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name used to refer to the upload data.
                    returned: on success
                    type: str
                    sample: name_example
                content_url:
                    description:
                        - The content URL of the upload data.
                    returned: on success
                    type: str
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the upload data.
                    returned: on success
                    type: str
                    sample: mime_type_example
                file_extension:
                    description:
                        - The file extension of the upload data.
                    returned: on success
                    type: str
                    sample: file_extension_example
        package_type:
            description:
                - The listing's package type.
            returned: on success
            type: str
            sample: ORCHESTRATION
        listing_type:
            description:
                - The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.
            returned: on success
            type: str
            sample: COMMUNITY
        supported_operating_systems:
            description:
                - The list of operating systems supprted by the listing.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the operating system.
                    returned: on success
                    type: str
                    sample: name_example
        time_created:
            description:
                - The date and time the publication was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: {
        "lifecycle_state": "CREATING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "short_description": "short_description_example",
        "long_description": "long_description_example",
        "support_contacts": [{
            "name": "name_example",
            "phone": "phone_example",
            "email": "email_example",
            "subject": "subject_example"
        }],
        "icon": {
            "name": "name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example",
            "file_extension": "file_extension_example"
        },
        "package_type": "ORCHESTRATION",
        "listing_type": "COMMUNITY",
        "supported_operating_systems": [{
            "name": "name_example"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
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
    from oci.marketplace import MarketplaceClient
    from oci.marketplace.models import ChangePublicationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "publication_id"

    def get_module_resource_id(self):
        return self.module.params.get("publication_id")

    def get_get_fn(self):
        return self.client.get_publication

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_publication,
            publication_id=self.module.params.get("publication_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePublicationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_publication_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                publication_id=self.module.params.get("publication_id"),
                change_publication_compartment_details=action_details,
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


PublicationActionsHelperCustom = get_custom_class("PublicationActionsHelperCustom")


class ResourceHelper(PublicationActionsHelperCustom, PublicationActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            publication_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="publication",
        service_client_class=MarketplaceClient,
        namespace="marketplace",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
