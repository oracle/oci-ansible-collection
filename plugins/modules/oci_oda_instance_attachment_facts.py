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
module: oci_oda_instance_attachment_facts
short_description: Fetches details about one or multiple OdaInstanceAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OdaInstanceAttachment resources in Oracle Cloud Infrastructure
    - Returns a list of ODA instance attachments
    - If I(attachment_id) is specified, the details of a single OdaInstanceAttachment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    attachment_id:
        description:
            - Unique Digital Assistant instance attachment identifier.
            - Required to get a specific oda_instance_attachment.
        type: str
        aliases: ["id"]
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    include_owner_metadata:
        description:
            - Whether to send attachment owner info during get/list call.
        type: bool
    lifecycle_state:
        description:
            - List only the ODA instance attachments that are in this lifecycle state.
        type: str
        choices:
            - "ATTACHING"
            - "ACTIVE"
            - "DETACHING"
            - "INACTIVE"
            - "FAILED"
    sort_order:
        description:
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.
              The default sort order for `TIMECREATED` is descending.
        type: str
        choices:
            - "TIMECREATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific oda_instance_attachment
  oci_oda_instance_attachment_facts:
    # required
    attachment_id: "ocid1.attachment.oc1..xxxxxxEXAMPLExxxxxx"
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    include_owner_metadata: true

- name: List oda_instance_attachments
  oci_oda_instance_attachment_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    include_owner_metadata: true
    lifecycle_state: ATTACHING
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
oda_instance_attachments:
    description:
        - List of OdaInstanceAttachment resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique immutable identifier that was assigned when the ODA instance attachment was created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - The OCID of the ODA instance to which the attachment applies.
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        attach_to_id:
            description:
                - The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which the ODA instance is or is being attached.
            returned: on success
            type: str
            sample: "ocid1.attachto.oc1..xxxxxxEXAMPLExxxxxx"
        attachment_type:
            description:
                - The type of attachment defined as an enum.
            returned: on success
            type: str
            sample: FUSION
        attachment_metadata:
            description:
                - Attachment-specific metadata, defined by the target service.
            returned: on success
            type: str
            sample: attachment_metadata_example
        restricted_operations:
            description:
                - List of operation names that are restricted while this ODA instance is attached.
            returned: on success
            type: list
            sample: []
        owner:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                owner_service_name:
                    description:
                        - Name of the owner service principal
                    returned: on success
                    type: str
                    sample: owner_service_name_example
                owner_service_tenancy:
                    description:
                        - Tenancy OCID of the owner service principal
                    returned: on success
                    type: str
                    sample: owner_service_tenancy_example
        time_created:
            description:
                - The time the attachment was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_update:
            description:
                - The time the attachment was last modified. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the attachment.
            returned: on success
            type: str
            sample: ATTACHING
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "attach_to_id": "ocid1.attachto.oc1..xxxxxxEXAMPLExxxxxx",
        "attachment_type": "FUSION",
        "attachment_metadata": "attachment_metadata_example",
        "restricted_operations": [],
        "owner": {
            "owner_service_name": "owner_service_name_example",
            "owner_service_tenancy": "owner_service_tenancy_example"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_update": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ATTACHING",
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
    from oci.oda import OdaClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OdaInstanceAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
            "attachment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "oda_instance_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "include_owner_metadata",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_oda_instance_attachment,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            attachment_id=self.module.params.get("attachment_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "include_owner_metadata",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_oda_instance_attachments,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            **optional_kwargs
        )


OdaInstanceAttachmentFactsHelperCustom = get_custom_class(
    "OdaInstanceAttachmentFactsHelperCustom"
)


class ResourceFactsHelper(
    OdaInstanceAttachmentFactsHelperCustom, OdaInstanceAttachmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            attachment_id=dict(aliases=["id"], type="str"),
            oda_instance_id=dict(type="str", required=True),
            include_owner_metadata=dict(type="bool"),
            lifecycle_state=dict(
                type="str",
                choices=["ATTACHING", "ACTIVE", "DETACHING", "INACTIVE", "FAILED"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="oda_instance_attachment",
        service_client_class=OdaClient,
        namespace="oda",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(oda_instance_attachments=result)


if __name__ == "__main__":
    main()
