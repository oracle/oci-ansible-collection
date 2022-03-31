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
module: oci_data_connectivity_reference_artifact_facts
short_description: Fetches details about one or multiple ReferenceArtifact resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ReferenceArtifact resources in Oracle Cloud Infrastructure
    - Retrieves a list of all reference info of a dcms artifact.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry Ocid.
        type: str
        required: true
    dcms_artifact_id:
        description:
            - The ID of a dcms artifact (DataAsset or Endpoint).
        type: str
        required: true
    fields:
        description:
            - Specifies the fields to get for an object.
        type: list
        elements: str
    type:
        description:
            - Type of the object to filter the results with.
        type: str
    sort_by:
        description:
            - Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other
              fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is
              by relevance score in descending order).
        type: str
        choices:
            - "id"
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    name:
        description:
            - Used to filter by the name of the object.
        type: str
    exclude_types:
        description:
            - Types which wont be listed while listing dataAsset/Connection
        type: list
        elements: str
    favorites_query_param:
        description:
            - If value is FAVORITES_ONLY, then only objects marked as favorite by the requesting user will be included in result. If value is
              NON_FAVORITES_ONLY, then objects marked as favorites by the requesting user will be skipped. If value is ALL or if not specified, all objects,
              irrespective of favorites or not will be returned. Default is ALL.
        type: str
        choices:
            - "FAVORITES_ONLY"
            - "NON_FAVORITES_ONLY"
            - "ALL"
    service_artifact_id:
        description:
            - Unique key of the service.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List reference_artifacts
  oci_data_connectivity_reference_artifact_facts:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    dcms_artifact_id: "ocid1.dcmsartifact.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    fields: [ "fields_example" ]
    type: type_example
    sort_by: id
    sort_order: ASC
    name: name_example
    exclude_types: [ "exclude_types_example" ]
    favorites_query_param: FAVORITES_ONLY
    service_artifact_id: "ocid1.serviceartifact.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
reference_artifacts:
    description:
        - List of ReferenceArtifact resources
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
                - Generated key that can be used in API calls to identify referenceinfo.
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
                - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable
                  and is restricted to 1000 characters.
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
                - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be
                  modified.
            returned: on success
            type: str
            sample: identifier_example
        dcms_artifact_id:
            description:
                - unique id of dcms artifact that is getting registered.
            returned: on success
            type: str
            sample: "ocid1.dcmsartifact.oc1..xxxxxxEXAMPLExxxxxx"
        service_artifact_id:
            description:
                - unique id of service which is referencing dcms artifact.
            returned: on success
            type: str
            sample: "ocid1.serviceartifact.oc1..xxxxxxEXAMPLExxxxxx"
        reference_count:
            description:
                - count of how many times a dcms artifact has been registered by a service.
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
                        - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to
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
                        - Specifies whether this object is a favorite or not.
                    returned: on success
                    type: bool
                    sample: true
                created_by_user_id:
                    description:
                        - The id of the user who created the object.
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
                        - The id of the user who updated the object.
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
                        - The full path to identify this object.
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
                        - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to
                          categorize content.
                    returned: on success
                    type: list
                    sample: []
                is_favorite:
                    description:
                        - Specifies whether this object is a favorite or not.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReferenceArtifactFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "registry_id",
            "dcms_artifact_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "fields",
            "type",
            "sort_by",
            "sort_order",
            "name",
            "exclude_types",
            "favorites_query_param",
            "service_artifact_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_reference_artifacts,
            registry_id=self.module.params.get("registry_id"),
            dcms_artifact_id=self.module.params.get("dcms_artifact_id"),
            **optional_kwargs
        )


ReferenceArtifactFactsHelperCustom = get_custom_class(
    "ReferenceArtifactFactsHelperCustom"
)


class ResourceFactsHelper(
    ReferenceArtifactFactsHelperCustom, ReferenceArtifactFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            registry_id=dict(type="str", required=True),
            dcms_artifact_id=dict(type="str", required=True),
            fields=dict(type="list", elements="str"),
            type=dict(type="str"),
            sort_by=dict(type="str", choices=["id", "timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
            exclude_types=dict(type="list", elements="str"),
            favorites_query_param=dict(
                type="str", choices=["FAVORITES_ONLY", "NON_FAVORITES_ONLY", "ALL"]
            ),
            service_artifact_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="reference_artifact",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(reference_artifacts=result)


if __name__ == "__main__":
    main()
