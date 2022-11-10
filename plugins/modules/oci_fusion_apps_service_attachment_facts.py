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
module: oci_fusion_apps_service_attachment_facts
short_description: Fetches details about one or multiple ServiceAttachment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ServiceAttachment resources in Oracle Cloud Infrastructure
    - Returns a list of service attachments.
    - If I(service_attachment_id) is specified, the details of a single ServiceAttachment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    service_attachment_id:
        description:
            - OCID of the Service Attachment
            - Required to get a specific service_attachment.
        type: str
        aliases: ["id"]
    fusion_environment_id:
        description:
            - unique FusionEnvironment identifier
        type: str
        required: true
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter that returns all resources that match the specified lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    service_instance_type:
        description:
            - A filter that returns all resources that match the specified lifecycle state.
        type: str
        choices:
            - "DIGITAL_ASSISTANT"
            - "INTEGRATION_CLOUD"
            - "ANALYTICS_WAREHOUSE"
            - "VBCS"
            - "VISUAL_BUILDER_STUDIO"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "TIME_CREATED"
            - "DISPLAY_NAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific service_attachment
  oci_fusion_apps_service_attachment_facts:
    # required
    service_attachment_id: "ocid1.serviceattachment.oc1..xxxxxxEXAMPLExxxxxx"
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List service_attachments
  oci_fusion_apps_service_attachment_facts:
    # required
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    service_instance_type: DIGITAL_ASSISTANT
    sort_order: ASC
    sort_by: TIME_CREATED

"""

RETURN = """
service_attachments:
    description:
        - List of ServiceAttachment resources
    returned: on success
    type: complex
    contains:
        action:
            description:
                - Action
                - Returned for get operation
            returned: on success
            type: str
            sample: action_example
        compartment_id:
            description:
                - Compartment Identifier
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Service Attachment Display name, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        service_instance_type:
            description:
                - Type of the serviceInstance.
            returned: on success
            type: str
            sample: DIGITAL_ASSISTANT
        service_instance_id:
            description:
                - The ID of the service instance created that can be used to identify this on the service control plane
            returned: on success
            type: str
            sample: "ocid1.serviceinstance.oc1..xxxxxxEXAMPLExxxxxx"
        service_url:
            description:
                - Public URL
            returned: on success
            type: str
            sample: service_url_example
        time_created:
            description:
                - The time the the ServiceInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the ServiceInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the ServiceInstance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        is_sku_based:
            description:
                - Whether this service is provisioned due to the customer being subscribed to a specific SKU
            returned: on success
            type: bool
            sample: true
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
        "action": "action_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "service_instance_type": "DIGITAL_ASSISTANT",
        "service_instance_id": "ocid1.serviceinstance.oc1..xxxxxxEXAMPLExxxxxx",
        "service_url": "service_url_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "is_sku_based": true,
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
    from oci.fusion_apps import FusionApplicationsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceAttachmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "fusion_environment_id",
            "service_attachment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "fusion_environment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_attachment,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            service_attachment_id=self.module.params.get("service_attachment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "service_instance_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_service_attachments,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            **optional_kwargs
        )


ServiceAttachmentFactsHelperCustom = get_custom_class(
    "ServiceAttachmentFactsHelperCustom"
)


class ResourceFactsHelper(
    ServiceAttachmentFactsHelperCustom, ServiceAttachmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            service_attachment_id=dict(aliases=["id"], type="str"),
            fusion_environment_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
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
            service_instance_type=dict(
                type="str",
                choices=[
                    "DIGITAL_ASSISTANT",
                    "INTEGRATION_CLOUD",
                    "ANALYTICS_WAREHOUSE",
                    "VBCS",
                    "VISUAL_BUILDER_STUDIO",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIME_CREATED", "DISPLAY_NAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="service_attachment",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(service_attachments=result)


if __name__ == "__main__":
    main()
