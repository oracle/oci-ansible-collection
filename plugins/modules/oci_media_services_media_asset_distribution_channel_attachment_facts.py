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
module: oci_media_services_media_asset_distribution_channel_attachment_facts
short_description: Fetches details about one or multiple MediaAssetDistributionChannelAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MediaAssetDistributionChannelAttachment resources in Oracle Cloud Infrastructure
    - Lists the MediaAssetDistributionChannelAttachments for a MediaAsset by identifier.
    - If I(distribution_channel_id) is specified, the details of a single MediaAssetDistributionChannelAttachment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    version:
        description:
            - Version of the attachment.
        type: int
    media_asset_id:
        description:
            - Unique MediaAsset identifier
        type: str
        required: true
    display_name:
        description:
            - A filter to return only the resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "mediaAssetId"
            - "distributionChannelId"
            - "displayName"
            - "version"
    distribution_channel_id:
        description:
            - Unique DistributionChannel identifier.
            - Required to get a specific media_asset_distribution_channel_attachment.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific media_asset_distribution_channel_attachment
  oci_media_services_media_asset_distribution_channel_attachment_facts:
    # required
    media_asset_id: "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    version: 56

- name: List media_asset_distribution_channel_attachments
  oci_media_services_media_asset_distribution_channel_attachment_facts:
    # required
    media_asset_id: "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: mediaAssetId
    distribution_channel_id: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
media_asset_distribution_channel_attachments:
    description:
        - List of MediaAssetDistributionChannelAttachment resources
    returned: on success
    type: complex
    contains:
        media_asset_id:
            description:
                - OCID of associated media asset.
                - Returned for list operation
            returned: on success
            type: str
            sample: "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        distribution_channel_id:
            description:
                - OCID of associated Distribution Channel.
            returned: on success
            type: str
            sample: "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx"
        version:
            description:
                - Version of the attachment.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - Lifecycle state of the attachment.
            returned: on success
            type: str
            sample: CREATING
        metadata_ref:
            description:
                - The identifier for the metadata.
            returned: on success
            type: str
            sample: metadata_ref_example
        media_workflow_job_id:
            description:
                - The ingest MediaWorkflowJob ID that created this attachment.
            returned: on success
            type: str
            sample: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "media_asset_id": "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "distribution_channel_id": "ocid1.distributionchannel.oc1..xxxxxxEXAMPLExxxxxx",
        "version": 56,
        "lifecycle_state": "CREATING",
        "metadata_ref": "metadata_ref_example",
        "media_workflow_job_id": "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.media_services import MediaServicesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaAssetDistributionChannelAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "media_asset_id",
            "distribution_channel_id",
        ]

    def get_required_params_for_list(self):
        return [
            "media_asset_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "version",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_media_asset_distribution_channel_attachment,
            media_asset_id=self.module.params.get("media_asset_id"),
            distribution_channel_id=self.module.params.get("distribution_channel_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
            "distribution_channel_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_media_asset_distribution_channel_attachments,
            media_asset_id=self.module.params.get("media_asset_id"),
            **optional_kwargs
        )


MediaAssetDistributionChannelAttachmentFactsHelperCustom = get_custom_class(
    "MediaAssetDistributionChannelAttachmentFactsHelperCustom"
)


class ResourceFactsHelper(
    MediaAssetDistributionChannelAttachmentFactsHelperCustom,
    MediaAssetDistributionChannelAttachmentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            version=dict(type="int"),
            media_asset_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "mediaAssetId",
                    "distributionChannelId",
                    "displayName",
                    "version",
                ],
            ),
            distribution_channel_id=dict(aliases=["id"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="media_asset_distribution_channel_attachment",
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

    module.exit_json(media_asset_distribution_channel_attachments=result)


if __name__ == "__main__":
    main()
