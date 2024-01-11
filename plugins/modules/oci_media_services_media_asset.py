#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_media_services_media_asset
short_description: Manage a MediaAsset resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a MediaAsset resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new MediaAsset.
    - "This resource has the following action operations in the M(oracle.oci.oci_media_services_media_asset_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source_media_workflow_id:
        description:
            - The ID of the MediaWorkflow used to produce this asset.
        type: str
    media_workflow_job_id:
        description:
            - The ID of the MediaWorkflowJob used to produce this asset.
        type: str
    source_media_workflow_version:
        description:
            - The version of the MediaWorkflow used to produce this asset.
        type: int
    compartment_id:
        description:
            - Compartment Identifier.
            - Required for create using I(state=present).
        type: str
    bucket_name:
        description:
            - The name of the object storage bucket where this asset is located.
        type: str
    namespace_name:
        description:
            - The object storage namespace where this asset is located.
        type: str
    object_name:
        description:
            - The object storage object name that identifies this asset.
        type: str
    object_etag:
        description:
            - eTag of the underlying object storage object.
        type: str
    segment_range_start_index:
        description:
            - The start index for video segment files.
        type: int
    segment_range_end_index:
        description:
            - The end index for video segment files.
        type: int
    display_name:
        description:
            - Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    type:
        description:
            - The type of the media asset.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "AUDIO"
            - "VIDEO"
            - "PLAYLIST"
            - "IMAGE"
            - "CAPTION_FILE"
            - "UNKNOWN"
    parent_media_asset_id:
        description:
            - The ID of the parent asset from which this asset is derived.
            - This parameter is updatable.
        type: str
    master_media_asset_id:
        description:
            - The ID of the senior most asset from which this asset is derived.
            - This parameter is updatable.
        type: str
    metadata:
        description:
            - List of Metadata.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            metadata:
                description:
                    - JSON string containing the technial metadata for the media asset.
                type: str
                required: true
    media_asset_tags:
        description:
            - list of tags for the MediaAsset.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - Type of the tag.
                type: str
                choices:
                    - "USER"
                    - "SYSTEM"
            value:
                description:
                    - Tag of the MediaAsset.
                type: str
                required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    media_asset_id:
        description:
            - Unique MediaAsset identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    delete_mode:
        description:
            - DeleteMode decides whether to delete all the immediate children or all assets with the asset's ID as their masterMediaAssetId.
        type: str
        choices:
            - "DELETE_CHILDREN"
            - "DELETE_DERIVATIONS"
    state:
        description:
            - The state of the MediaAsset.
            - Use I(state=present) to create or update a MediaAsset.
            - Use I(state=absent) to delete a MediaAsset.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create media_asset
  oci_media_services_media_asset:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    type: AUDIO

    # optional
    source_media_workflow_id: "ocid1.sourcemediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
    media_workflow_job_id: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
    source_media_workflow_version: 56
    bucket_name: bucket_name_example
    namespace_name: namespace_name_example
    object_name: object_name_example
    object_etag: object_etag_example
    segment_range_start_index: 56
    segment_range_end_index: 56
    display_name: display_name_example
    parent_media_asset_id: "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    master_media_asset_id: "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    metadata:
    - # required
      metadata: metadata_example
    media_asset_tags:
    - # required
      value: value_example

      # optional
      type: USER
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update media_asset
  oci_media_services_media_asset:
    # required
    media_asset_id: "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    type: AUDIO
    parent_media_asset_id: "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    master_media_asset_id: "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    metadata:
    - # required
      metadata: metadata_example
    media_asset_tags:
    - # required
      value: value_example

      # optional
      type: USER
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update media_asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_media_asset:
    # required
    display_name: display_name_example

    # optional
    type: AUDIO
    parent_media_asset_id: "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    master_media_asset_id: "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    metadata:
    - # required
      metadata: metadata_example
    media_asset_tags:
    - # required
      value: value_example

      # optional
      type: USER
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete media_asset
  oci_media_services_media_asset:
    # required
    media_asset_id: "ocid1.mediaasset.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    delete_mode: DELETE_CHILDREN

- name: Delete media_asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_media_asset:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
media_asset:
    description:
        - Details of the MediaAsset resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The ID of the compartment containing the MediaAsset.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        source_media_workflow_id:
            description:
                - The ID of the MediaWorkflow used to produce this asset.
            returned: on success
            type: str
            sample: "ocid1.sourcemediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
        media_workflow_job_id:
            description:
                - The ID of the MediaWorkflowJob used to produce this asset.
            returned: on success
            type: str
            sample: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
        source_media_workflow_version:
            description:
                - The version of the MediaWorkflow used to produce this asset.
            returned: on success
            type: int
            sample: 56
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The time when the MediaAsset was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the MediaAsset.
            returned: on success
            type: str
            sample: CREATING
        type:
            description:
                - The type of the media asset.
            returned: on success
            type: str
            sample: AUDIO
        parent_media_asset_id:
            description:
                - The ID of the parent asset from which this asset is derived.
            returned: on success
            type: str
            sample: "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx"
        master_media_asset_id:
            description:
                - The ID of the senior most asset from which this asset is derived.
            returned: on success
            type: str
            sample: "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx"
        bucket_name:
            description:
                - The name of the object storage bucket where this represented asset is located.
            returned: on success
            type: str
            sample: bucket_name_example
        namespace_name:
            description:
                - The object storage namespace where this asset is located.
            returned: on success
            type: str
            sample: namespace_name_example
        object_name:
            description:
                - The object storage object name that identifies this asset.
            returned: on success
            type: str
            sample: object_name_example
        object_etag:
            description:
                - eTag of the underlying object storage object.
            returned: on success
            type: str
            sample: object_etag_example
        time_updated:
            description:
                - The time when the MediaAsset was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        segment_range_start_index:
            description:
                - The start index for video segment files.
            returned: on success
            type: int
            sample: 56
        segment_range_end_index:
            description:
                - The end index of video segment files.
            returned: on success
            type: int
            sample: 56
        metadata:
            description:
                - List of Metadata.
            returned: on success
            type: complex
            contains:
                metadata:
                    description:
                        - JSON string containing the technial metadata for the media asset.
                    returned: on success
                    type: str
                    sample: metadata_example
        media_asset_tags:
            description:
                - List of tags for the MediaAsset.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the tag.
                    returned: on success
                    type: str
                    sample: USER
                value:
                    description:
                        - Tag of the MediaAsset.
                    returned: on success
                    type: str
                    sample: value_example
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "source_media_workflow_id": "ocid1.sourcemediaworkflow.oc1..xxxxxxEXAMPLExxxxxx",
        "media_workflow_job_id": "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx",
        "source_media_workflow_version": 56,
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "type": "AUDIO",
        "parent_media_asset_id": "ocid1.parentmediaasset.oc1..xxxxxxEXAMPLExxxxxx",
        "master_media_asset_id": "ocid1.mastermediaasset.oc1..xxxxxxEXAMPLExxxxxx",
        "bucket_name": "bucket_name_example",
        "namespace_name": "namespace_name_example",
        "object_name": "object_name_example",
        "object_etag": "object_etag_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "segment_range_start_index": 56,
        "segment_range_end_index": 56,
        "metadata": [{
            "metadata": "metadata_example"
        }],
        "media_asset_tags": [{
            "type": "USER",
            "value": "value_example"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.media_services import MediaServicesClient
    from oci.media_services.models import CreateMediaAssetDetails
    from oci.media_services.models import UpdateMediaAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaAssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MediaAssetHelperGen, self).get_possible_entity_types() + [
            "mediaasset",
            "mediaassets",
            "mediaServicesmediaasset",
            "mediaServicesmediaassets",
            "mediaassetresource",
            "mediaassetsresource",
            "mediaservices",
        ]

    def get_module_resource_id_param(self):
        return "media_asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("media_asset_id")

    def get_get_fn(self):
        return self.client.get_media_asset

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_asset, media_asset_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_asset,
            media_asset_id=self.module.params.get("media_asset_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            [
                "compartment_id",
                "display_name",
                "bucket_name",
                "object_name",
                "media_workflow_job_id",
                "source_media_workflow_id",
                "source_media_workflow_version",
            ]
            if self._use_name_as_identifier()
            else [
                "compartment_id",
                "display_name",
                "parent_media_asset_id",
                "master_media_asset_id",
                "type",
                "bucket_name",
                "object_name",
                "media_workflow_job_id",
                "source_media_workflow_id",
                "source_media_workflow_version",
            ]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_media_assets, **kwargs
        )

    def get_create_model_class(self):
        return CreateMediaAssetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_media_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(create_media_asset_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateMediaAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_media_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_asset_id=self.module.params.get("media_asset_id"),
                update_media_asset_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        optional_enum_params = [
            "delete_mode",
        ]
        optional_enum_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_enum_params
            if self.module.params.get(param) is not None
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_media_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_asset_id=self.module.params.get("media_asset_id"),
                **optional_enum_kwargs
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MediaAssetHelperCustom = get_custom_class("MediaAssetHelperCustom")


class ResourceHelper(MediaAssetHelperCustom, MediaAssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            source_media_workflow_id=dict(type="str"),
            media_workflow_job_id=dict(type="str"),
            source_media_workflow_version=dict(type="int"),
            compartment_id=dict(type="str"),
            bucket_name=dict(type="str"),
            namespace_name=dict(type="str"),
            object_name=dict(type="str"),
            object_etag=dict(type="str"),
            segment_range_start_index=dict(type="int"),
            segment_range_end_index=dict(type="int"),
            display_name=dict(aliases=["name"], type="str"),
            type=dict(
                type="str",
                choices=[
                    "AUDIO",
                    "VIDEO",
                    "PLAYLIST",
                    "IMAGE",
                    "CAPTION_FILE",
                    "UNKNOWN",
                ],
            ),
            parent_media_asset_id=dict(type="str"),
            master_media_asset_id=dict(type="str"),
            metadata=dict(
                type="list",
                elements="dict",
                options=dict(metadata=dict(type="str", required=True)),
            ),
            media_asset_tags=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(type="str", choices=["USER", "SYSTEM"]),
                    value=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            media_asset_id=dict(aliases=["id"], type="str"),
            delete_mode=dict(
                type="str", choices=["DELETE_CHILDREN", "DELETE_DERIVATIONS"]
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="media_asset",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
