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
module: oci_opa_instance_facts
short_description: Fetches details about one or multiple OpaInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OpaInstance resources in Oracle Cloud Infrastructure
    - Returns a list of OpaInstances.
    - If I(opa_instance_id) is specified, the details of a single OpaInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    opa_instance_id:
        description:
            - unique OpaInstance identifier
            - Required to get a specific opa_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
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
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific opa_instance
  oci_opa_instance_facts:
    # required
    opa_instance_id: "ocid1.opainstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List opa_instances
  oci_opa_instance_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
opa_instances:
    description:
        - List of OpaInstance resources
    returned: on success
    type: complex
    contains:
        identity_app_guid:
            description:
                - This property specifies the GUID of the Identity Application instance OPA has created inside the user-specified identity domain. This identity
                  application instance may be used to host user role mappings to grant access to this OPA instance for users within the identity domain.
                - Returned for get operation
            returned: on success
            type: str
            sample: identity_app_guid_example
        identity_app_display_name:
            description:
                - This property specifies the name of the Identity Application instance OPA has created inside the user-specified identity domain. This identity
                  application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity domain.
                - Returned for get operation
            returned: on success
            type: str
            sample: identity_app_display_name_example
        identity_domain_url:
            description:
                - This property specifies the domain url of the Identity Application instance OPA has created inside the user-specified identity domain. This
                  identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the identity
                  domain.
                - Returned for get operation
            returned: on success
            type: str
            sample: identity_domain_url_example
        identity_app_opc_service_instance_guid:
            description:
                - This property specifies the OPC Service Instance GUID of the Identity Application instance OPA has created inside the user-specified identity
                  domain. This identity application instance may be used to host user roll mappings to grant access to this OPA instance for users within the
                  identity domain.
                - Returned for get operation
            returned: on success
            type: str
            sample: identity_app_opc_service_instance_guid_example
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
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - OpaInstance Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the Process Automation instance.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        instance_url:
            description:
                - OPA Instance URL
            returned: on success
            type: str
            sample: instance_url_example
        consumption_model:
            description:
                - The entitlement used for billing purposes
            returned: on success
            type: str
            sample: UCM
        shape_name:
            description:
                - Shape of the instance.
            returned: on success
            type: str
            sample: DEVELOPMENT
        metering_type:
            description:
                - MeteringType Identifier
            returned: on success
            type: str
            sample: EXECUTION_PACK
        time_created:
            description:
                - The time when OpaInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the OpaInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the OpaInstance.
            returned: on success
            type: str
            sample: CREATING
        is_breakglass_enabled:
            description:
                - indicates if breakGlass is enabled for the opa instance.
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "identity_app_guid": "identity_app_guid_example",
        "identity_app_display_name": "identity_app_display_name_example",
        "identity_domain_url": "identity_domain_url_example",
        "identity_app_opc_service_instance_guid": "identity_app_opc_service_instance_guid_example",
        "attachments": [{
            "target_role": "PARENT",
            "is_implicit": true,
            "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
            "target_instance_url": "target_instance_url_example",
            "target_service_type": "target_service_type_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_url": "instance_url_example",
        "consumption_model": "UCM",
        "shape_name": "DEVELOPMENT",
        "metering_type": "EXECUTION_PACK",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "is_breakglass_enabled": true,
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
    from oci.opa import OpaInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpaInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "opa_instance_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opa_instance,
            opa_instance_id=self.module.params.get("opa_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_opa_instances, **optional_kwargs
        )


OpaInstanceFactsHelperCustom = get_custom_class("OpaInstanceFactsHelperCustom")


class ResourceFactsHelper(OpaInstanceFactsHelperCustom, OpaInstanceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            opa_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
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
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="opa_instance",
        service_client_class=OpaInstanceClient,
        namespace="opa",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(opa_instances=result)


if __name__ == "__main__":
    main()
