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
module: oci_data_connectivity_reference_info_actions
short_description: Perform actions on a ReferenceInfo resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ReferenceInfo resource in Oracle Cloud Infrastructure
    - For I(action=create_de_reference_artifact), dereferenced a dcms artifact.
    - For I(action=create_reference_artifact), reference a data asset.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry OCID.
        type: str
        required: true
    dcms_artifact_id:
        description:
            - The ID of a dcms artifact (DataAsset or Endpoint).
        type: str
        aliases: ["id"]
        required: true
    service_artifact_id:
        description:
            - The unique ID of the service that is referencing a data asset.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ReferenceInfo.
        type: str
        required: true
        choices:
            - "create_de_reference_artifact"
            - "create_reference_artifact"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action create_de_reference_artifact on reference_info
  oci_data_connectivity_reference_info_actions:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    dcms_artifact_id: "ocid1.dcmsartifact.oc1..xxxxxxEXAMPLExxxxxx"
    service_artifact_id: "ocid1.serviceartifact.oc1..xxxxxxEXAMPLExxxxxx"
    action: create_de_reference_artifact

- name: Perform action create_reference_artifact on reference_info
  oci_data_connectivity_reference_info_actions:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    dcms_artifact_id: "ocid1.dcmsartifact.oc1..xxxxxxEXAMPLExxxxxx"
    service_artifact_id: "ocid1.serviceartifact.oc1..xxxxxxEXAMPLExxxxxx"
    action: create_reference_artifact

"""

RETURN = """
reference_info:
    description:
        - Details of the ReferenceInfo resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        model_type:
            description:
                - The type of the ReferenceInfo.
            returned: on success
            type: str
            sample: model_type_example
        key:
            description:
                - Generated key that can be used in API calls to identify the referenceinfo.
            returned: on success
            type: str
            sample: key_example
        model_version:
            description:
                - The model version of an object.
            returned: on success
            type: str
            sample: model_version_example
        name:
            description:
                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                  editable and is restricted to 1000 characters.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - User-defined description of the referenceInfo.
            returned: on success
            type: str
            sample: description_example
        object_status:
            description:
                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
            returned: on success
            type: int
            sample: 56
        object_version:
            description:
                - The version of the object that is used to track changes in the object instance.
            returned: on success
            type: int
            sample: 56
        identifier:
            description:
                - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be
                  modified.
            returned: on success
            type: str
            sample: identifier_example
        dcms_artifact_id:
            description:
                - The unique ID of the DCMS artifact that is getting registered.
            returned: on success
            type: str
            sample: "ocid1.dcmsartifact.oc1..xxxxxxEXAMPLExxxxxx"
        service_artifact_id:
            description:
                - The unique ID of the service that is referencing a data asset.
            returned: on success
            type: str
            sample: "ocid1.serviceartifact.oc1..xxxxxxEXAMPLExxxxxx"
        reference_count:
            description:
                - The number of times a data asset has been registered by a service.
            returned: on success
            type: int
            sample: 56
        registry_metadata:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                aggregator_key:
                    description:
                        - The owning object's key for this object.
                    returned: on success
                    type: str
                    sample: aggregator_key_example
                labels:
                    description:
                        - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                          categorize content.
                    returned: on success
                    type: list
                    sample: []
                registry_version:
                    description:
                        - The registry version.
                    returned: on success
                    type: int
                    sample: 56
                key:
                    description:
                        - The identifying key for the object.
                    returned: on success
                    type: str
                    sample: key_example
                is_favorite:
                    description:
                        - Specifies whether the object is a favorite.
                    returned: on success
                    type: bool
                    sample: true
                created_by_user_id:
                    description:
                        - The ID of the user who created the object.
                    returned: on success
                    type: str
                    sample: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                created_by_user_name:
                    description:
                        - The name of the user who created the object.
                    returned: on success
                    type: str
                    sample: created_by_user_name_example
                updated_by_user_id:
                    description:
                        - The ID of the user who updated the object.
                    returned: on success
                    type: str
                    sample: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                updated_by_user_name:
                    description:
                        - The name of the user who updated the object.
                    returned: on success
                    type: str
                    sample: updated_by_user_name_example
                time_created:
                    description:
                        - The date and time that the object was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time that the object was updated.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        metadata:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                created_by:
                    description:
                        - The user that created the object.
                    returned: on success
                    type: str
                    sample: created_by_example
                created_by_name:
                    description:
                        - The user that created the object.
                    returned: on success
                    type: str
                    sample: created_by_name_example
                updated_by:
                    description:
                        - The user that updated the object.
                    returned: on success
                    type: str
                    sample: updated_by_example
                updated_by_name:
                    description:
                        - The user that updated the object.
                    returned: on success
                    type: str
                    sample: updated_by_name_example
                time_created:
                    description:
                        - The date and time that the object was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time that the object was updated.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                aggregator_key:
                    description:
                        - The owning object key for this object.
                    returned: on success
                    type: str
                    sample: aggregator_key_example
                aggregator:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of the aggregator.
                            returned: on success
                            type: str
                            sample: type_example
                        key:
                            description:
                                - The key of the aggregator object.
                            returned: on success
                            type: str
                            sample: key_example
                        name:
                            description:
                                - The name of the aggregator.
                            returned: on success
                            type: str
                            sample: name_example
                        identifier:
                            description:
                                - The identifier of the aggregator.
                            returned: on success
                            type: str
                            sample: identifier_example
                        description:
                            description:
                                - The description of the aggregator.
                            returned: on success
                            type: str
                            sample: description_example
                identifier_path:
                    description:
                        - The full path to identify the object.
                    returned: on success
                    type: str
                    sample: identifier_path_example
                info_fields:
                    description:
                        - Information property fields.
                    returned: on success
                    type: dict
                    sample: {}
                registry_version:
                    description:
                        - The registry version of the object.
                    returned: on success
                    type: int
                    sample: 56
                labels:
                    description:
                        - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                          categorize content.
                    returned: on success
                    type: list
                    sample: []
                is_favorite:
                    description:
                        - Specifies whether this object is a favorite.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "model_type": "model_type_example",
        "key": "key_example",
        "model_version": "model_version_example",
        "name": "name_example",
        "description": "description_example",
        "object_status": 56,
        "object_version": 56,
        "identifier": "identifier_example",
        "dcms_artifact_id": "ocid1.dcmsartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "service_artifact_id": "ocid1.serviceartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "reference_count": 56,
        "registry_metadata": {
            "aggregator_key": "aggregator_key_example",
            "labels": [],
            "registry_version": 56,
            "key": "key_example",
            "is_favorite": true,
            "created_by_user_id": "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "created_by_user_name": "created_by_user_name_example",
            "updated_by_user_id": "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "updated_by_user_name": "updated_by_user_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        },
        "metadata": {
            "created_by": "created_by_example",
            "created_by_name": "created_by_name_example",
            "updated_by": "updated_by_example",
            "updated_by_name": "updated_by_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "aggregator_key": "aggregator_key_example",
            "aggregator": {
                "type": "type_example",
                "key": "key_example",
                "name": "name_example",
                "identifier": "identifier_example",
                "description": "description_example"
            },
            "identifier_path": "identifier_path_example",
            "info_fields": {},
            "registry_version": 56,
            "labels": [],
            "is_favorite": true
        }
    }

de_reference_info:
    description:
        - Details of the ReferenceInfo resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        model_type:
            description:
                - The type of the ReferenceInfo.
            returned: on success
            type: str
            sample: model_type_example
        key:
            description:
                - Generated key that can be used in API calls to identify the referenceinfo.
            returned: on success
            type: str
            sample: key_example
        model_version:
            description:
                - The model version of an object.
            returned: on success
            type: str
            sample: model_version_example
        name:
            description:
                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                  editable and is restricted to 1000 characters.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - User-defined description of the referenceInfo.
            returned: on success
            type: str
            sample: description_example
        object_status:
            description:
                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
            returned: on success
            type: int
            sample: 56
        object_version:
            description:
                - The version of the object that is used to track changes in the object instance.
            returned: on success
            type: int
            sample: 56
        identifier:
            description:
                - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be
                  modified.
            returned: on success
            type: str
            sample: identifier_example
        dcms_artifact_id:
            description:
                - The unique ID of the DCMS artifact that is getting referenced.
            returned: on success
            type: str
            sample: "ocid1.dcmsartifact.oc1..xxxxxxEXAMPLExxxxxx"
        service_artifact_id:
            description:
                - The unique ID of the service that is referencing a DCMS artifact.
            returned: on success
            type: str
            sample: "ocid1.serviceartifact.oc1..xxxxxxEXAMPLExxxxxx"
        reference_count:
            description:
                - The number of times a DCMS artifact has been registered by a service.
            returned: on success
            type: int
            sample: 56
        registry_metadata:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                aggregator_key:
                    description:
                        - The owning object's key for this object.
                    returned: on success
                    type: str
                    sample: aggregator_key_example
                labels:
                    description:
                        - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                          categorize content.
                    returned: on success
                    type: list
                    sample: []
                registry_version:
                    description:
                        - The registry version.
                    returned: on success
                    type: int
                    sample: 56
                key:
                    description:
                        - The identifying key for the object.
                    returned: on success
                    type: str
                    sample: key_example
                is_favorite:
                    description:
                        - Specifies whether the object is a favorite.
                    returned: on success
                    type: bool
                    sample: true
                created_by_user_id:
                    description:
                        - The ID of the user who created the object.
                    returned: on success
                    type: str
                    sample: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                created_by_user_name:
                    description:
                        - The name of the user who created the object.
                    returned: on success
                    type: str
                    sample: created_by_user_name_example
                updated_by_user_id:
                    description:
                        - The ID of the user who updated the object.
                    returned: on success
                    type: str
                    sample: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                updated_by_user_name:
                    description:
                        - The name of the user who updated the object.
                    returned: on success
                    type: str
                    sample: updated_by_user_name_example
                time_created:
                    description:
                        - The date and time that the object was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time that the object was updated.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        metadata:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                created_by:
                    description:
                        - The user that created the object.
                    returned: on success
                    type: str
                    sample: created_by_example
                created_by_name:
                    description:
                        - The user that created the object.
                    returned: on success
                    type: str
                    sample: created_by_name_example
                updated_by:
                    description:
                        - The user that updated the object.
                    returned: on success
                    type: str
                    sample: updated_by_example
                updated_by_name:
                    description:
                        - The user that updated the object.
                    returned: on success
                    type: str
                    sample: updated_by_name_example
                time_created:
                    description:
                        - The date and time that the object was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time that the object was updated.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                aggregator_key:
                    description:
                        - The owning object key for this object.
                    returned: on success
                    type: str
                    sample: aggregator_key_example
                aggregator:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of the aggregator.
                            returned: on success
                            type: str
                            sample: type_example
                        key:
                            description:
                                - The key of the aggregator object.
                            returned: on success
                            type: str
                            sample: key_example
                        name:
                            description:
                                - The name of the aggregator.
                            returned: on success
                            type: str
                            sample: name_example
                        identifier:
                            description:
                                - The identifier of the aggregator.
                            returned: on success
                            type: str
                            sample: identifier_example
                        description:
                            description:
                                - The description of the aggregator.
                            returned: on success
                            type: str
                            sample: description_example
                identifier_path:
                    description:
                        - The full path to identify the object.
                    returned: on success
                    type: str
                    sample: identifier_path_example
                info_fields:
                    description:
                        - Information property fields.
                    returned: on success
                    type: dict
                    sample: {}
                registry_version:
                    description:
                        - The registry version of the object.
                    returned: on success
                    type: int
                    sample: 56
                labels:
                    description:
                        - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                          categorize content.
                    returned: on success
                    type: list
                    sample: []
                is_favorite:
                    description:
                        - Specifies whether this object is a favorite.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "model_type": "model_type_example",
        "key": "key_example",
        "model_version": "model_version_example",
        "name": "name_example",
        "description": "description_example",
        "object_status": 56,
        "object_version": 56,
        "identifier": "identifier_example",
        "dcms_artifact_id": "ocid1.dcmsartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "service_artifact_id": "ocid1.serviceartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "reference_count": 56,
        "registry_metadata": {
            "aggregator_key": "aggregator_key_example",
            "labels": [],
            "registry_version": 56,
            "key": "key_example",
            "is_favorite": true,
            "created_by_user_id": "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "created_by_user_name": "created_by_user_name_example",
            "updated_by_user_id": "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "updated_by_user_name": "updated_by_user_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        },
        "metadata": {
            "created_by": "created_by_example",
            "created_by_name": "created_by_name_example",
            "updated_by": "updated_by_example",
            "updated_by_name": "updated_by_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "aggregator_key": "aggregator_key_example",
            "aggregator": {
                "type": "type_example",
                "key": "key_example",
                "name": "name_example",
                "identifier": "identifier_example",
                "description": "description_example"
            },
            "identifier_path": "identifier_path_example",
            "info_fields": {},
            "registry_version": 56,
            "labels": [],
            "is_favorite": true
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient
    from oci.data_connectivity.models import CreateDeReferenceArtifactDetails
    from oci.data_connectivity.models import CreateReferenceArtifactDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReferenceInfoActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        create_de_reference_artifact
        create_reference_artifact
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dcms_artifact_id"

    def get_module_resource_id(self):
        return self.module.params.get("dcms_artifact_id")

    def create_de_reference_artifact(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CreateDeReferenceArtifactDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_de_reference_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                dcms_artifact_id=self.module.params.get("dcms_artifact_id"),
                create_de_reference_artifact_details=action_details,
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

    def create_reference_artifact(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CreateReferenceArtifactDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_reference_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                dcms_artifact_id=self.module.params.get("dcms_artifact_id"),
                create_reference_artifact_details=action_details,
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


ReferenceInfoActionsHelperCustom = get_custom_class("ReferenceInfoActionsHelperCustom")


class ResourceHelper(ReferenceInfoActionsHelperCustom, ReferenceInfoActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            registry_id=dict(type="str", required=True),
            dcms_artifact_id=dict(aliases=["id"], type="str", required=True),
            service_artifact_id=dict(type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["create_de_reference_artifact", "create_reference_artifact"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="reference_info",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
