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
module: oci_visual_builder_vb_instance_facts
short_description: Fetches details about one or multiple VbInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VbInstance resources in Oracle Cloud Infrastructure
    - Returns a list of Vb Instances.
    - If I(vb_instance_id) is specified, the details of a single VbInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vb_instance_id:
        description:
            - Unique Vb Instance identifier.
            - Required to get a specific vb_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple vb_instances.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Life cycle state to query on.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order
              for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific vb_instance
  oci_visual_builder_vb_instance_facts:
    # required
    vb_instance_id: "ocid1.vbinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List vb_instances
  oci_visual_builder_vb_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
vb_instances:
    description:
        - List of VbInstance resources
    returned: on success
    type: complex
    contains:
        idcs_info:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                idcs_app_location_url:
                    description:
                        - URL for the location of the IDCS Application (used by IDCS APIs)
                    returned: on success
                    type: str
                    sample: idcs_app_location_url_example
                idcs_app_display_name:
                    description:
                        - The IDCS application display name associated with the instance
                    returned: on success
                    type: str
                    sample: idcs_app_display_name_example
                idcs_app_id:
                    description:
                        - The IDCS application ID associated with the instance
                    returned: on success
                    type: str
                    sample: "ocid1.idcsapp.oc1..xxxxxxEXAMPLExxxxxx"
                idcs_app_name:
                    description:
                        - The IDCS application name associated with the instance
                    returned: on success
                    type: str
                    sample: idcs_app_name_example
                instance_primary_audience_url:
                    description:
                        - "The URL used as the primary audience for visual builder flows in this instance
                          type: string"
                    returned: on success
                    type: str
                    sample: instance_primary_audience_url_example
        attachments:
            description:
                - A list of associated attachments to other services
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                target_role:
                    description:
                        - "The role of the target attachment.
                             * `PARENT` - The target instance is the parent of this attachment.
                             * `CHILD` - The target instance is the child of this attachment."
                    returned: on success
                    type: str
                    sample: PARENT
                is_implicit:
                    description:
                        - "* If role == `PARENT`, the attached instance was created by this service instance
                          * If role == `CHILD`, this instance was created from attached instance on behalf of a user"
                    returned: on success
                    type: bool
                    sample: true
                target_id:
                    description:
                        - The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.
                    returned: on success
                    type: str
                    sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
                target_instance_url:
                    description:
                        - The dataplane instance URL of the attached instance
                    returned: on success
                    type: str
                    sample: target_instance_url_example
                target_service_type:
                    description:
                        - "The type of the target instance, such as \\"FUSION\\"."
                    returned: on success
                    type: str
                    sample: target_service_type_example
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Vb Instance Identifier, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the VbInstance was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the VbInstance was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the vb instance.
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
        instance_url:
            description:
                - The Vb Instance URL.
            returned: on success
            type: str
            sample: instance_url_example
        node_count:
            description:
                - The number of Nodes
            returned: on success
            type: int
            sample: 56
        is_visual_builder_enabled:
            description:
                - Visual Builder is enabled or not.
            returned: on success
            type: bool
            sample: true
        custom_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the vb instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
        alternate_custom_endpoints:
            description:
                - A list of alternate custom endpoints used for the vb instance URL.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the vb instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
        consumption_model:
            description:
                - The entitlement used for billing purposes.
            returned: on success
            type: str
            sample: UCM
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
    sample: [{
        "idcs_info": {
            "idcs_app_location_url": "idcs_app_location_url_example",
            "idcs_app_display_name": "idcs_app_display_name_example",
            "idcs_app_id": "ocid1.idcsapp.oc1..xxxxxxEXAMPLExxxxxx",
            "idcs_app_name": "idcs_app_name_example",
            "instance_primary_audience_url": "instance_primary_audience_url_example"
        },
        "attachments": [{
            "target_role": "PARENT",
            "is_implicit": true,
            "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
            "target_instance_url": "target_instance_url_example",
            "target_service_type": "target_service_type_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "instance_url": "instance_url_example",
        "node_count": 56,
        "is_visual_builder_enabled": true,
        "custom_endpoint": {
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56
        },
        "alternate_custom_endpoints": [{
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56
        }],
        "consumption_model": "UCM",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.visual_builder import VbInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VbInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "vb_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vb_instance,
            vb_instance_id=self.module.params.get("vb_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
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
            self.client.list_vb_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VbInstanceFactsHelperCustom = get_custom_class("VbInstanceFactsHelperCustom")


class ResourceFactsHelper(VbInstanceFactsHelperCustom, VbInstanceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vb_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vb_instance",
        service_client_class=VbInstanceClient,
        namespace="visual_builder",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vb_instances=result)


if __name__ == "__main__":
    main()
