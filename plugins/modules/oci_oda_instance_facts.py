#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_oda_instance_facts
short_description: Fetches details about one or multiple OdaInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OdaInstance resources in Oracle Cloud Infrastructure
    - Returns a page of Digital Assistant instances that belong to the specified
      compartment.
    - If the `opc-next-page` header appears in the response, then
      there are more items to retrieve. To get the next page in the subsequent
      GET request, include the header's value as the `page` query parameter.
    - If I(oda_instance_id) is specified, the details of a single OdaInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
            - Required to get a specific oda_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - List the Digital Assistant instances that belong to this compartment.
            - Required to list multiple oda_instances.
        type: str
    display_name:
        description:
            - List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - List only the Digital Assistant instances that are in this lifecycle state.
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
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.
            - The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific oda_instance
  oci_oda_instance_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List oda_instances
  oci_oda_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
oda_instances:
    description:
        - List of OdaInstance resources
    returned: on success
    type: complex
    contains:
        web_app_url:
            description:
                - URL for the Digital Assistant web application that's associated with the instance.
                - Returned for get operation
            returned: on success
            type: str
            sample: web_app_url_example
        connector_url:
            description:
                - URL for the connector's endpoint.
                - Returned for get operation
            returned: on success
            type: str
            sample: connector_url_example
        identity_app_guid:
            description:
                - If isRoleBasedAccess is set to true, this property specifies the GUID of the Identity Application instance Digital Assistant has created
                  inside the user-specified identity domain. This identity application instance may be used to host user roll mappings to grant access to this
                  Digital Assistant instance for users within the identity domain.
                - Returned for get operation
            returned: on success
            type: str
            sample: identity_app_guid_example
        identity_app_console_url:
            description:
                - If isRoleBasedAccess is set to true, this property specifies the URL for the administration console used to manage the Identity Application
                  instance Digital Assistant has created inside the user-specified identity domain.
                - Returned for get operation
            returned: on success
            type: str
            sample: identity_app_console_url_example
        imported_package_ids:
            description:
                - A list of package ids imported into this instance (if any). Use GetImportedPackage to get the details of the imported packages.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        attachment_ids:
            description:
                - A list of attachment identifiers for this instance (if any). Use GetOdaInstanceAttachment to get the details of the attachments.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        restricted_operations:
            description:
                - A list of restricted operations (across all attachments) for this instance (if any). Use GetOdaInstanceAttachment to get the details of the
                  attachments.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                operation_name:
                    description:
                        - Name of the restricted operation.
                    returned: on success
                    type: str
                    sample: operation_name_example
                restricting_service:
                    description:
                        - Name of the service restricting the operation.
                    returned: on success
                    type: str
                    sample: restricting_service_example
        id:
            description:
                - Unique immutable identifier that was assigned when the instance was created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-defined name for the Digital Assistant instance. Avoid entering confidential information.
                  You can change this value.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the Digital Assistant instance.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Identifier of the compartment that the instance belongs to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        shape_name:
            description:
                - Shape or size of the instance.
            returned: on success
            type: str
            sample: DEVELOPMENT
        time_created:
            description:
                - When the Digital Assistant instance was created. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section
                  14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the Digital Assistance instance was last updated. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339),
                  section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Digital Assistant instance.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_sub_state:
            description:
                - The current sub-state of the Digital Assistant instance.
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - A message that describes the current state in more detail.
                  For example, actionable information about an instance that's in the `FAILED` state.
            returned: on success
            type: str
            sample: state_message_example
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
        is_role_based_access:
            description:
                - Should this Digital Assistant instance use role-based authorization via an identity domain (true) or use the default policy-based
                  authorization via IAM policies (false)
            returned: on success
            type: bool
            sample: true
        identity_domain:
            description:
                - If isRoleBasedAccess is set to true, this property specifies the identity domain that is to be used to implement this type of authorzation.
                  Digital Assistant will create an Identity Application instance and Application Roles within this identity domain. The caller may then perform
                  and user roll mappings they like to grant access to users within the identity domain.
            returned: on success
            type: str
            sample: identity_domain_example
        imported_package_names:
            description:
                - A list of package names imported into this instance (if any). Use importedPackageIds field to get the details of the imported packages.
            returned: on success
            type: list
            sample: []
        attachment_types:
            description:
                - A list of attachment types for this instance (if any). Use attachmentIds to get the details of the attachments.
            returned: on success
            type: list
            sample: []
    sample: [{
        "web_app_url": "web_app_url_example",
        "connector_url": "connector_url_example",
        "identity_app_guid": "identity_app_guid_example",
        "identity_app_console_url": "identity_app_console_url_example",
        "imported_package_ids": [],
        "attachment_ids": [],
        "restricted_operations": [{
            "operation_name": "operation_name_example",
            "restricting_service": "restricting_service_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "shape_name": "DEVELOPMENT",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_sub_state": "CREATING",
        "state_message": "state_message_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_role_based_access": true,
        "identity_domain": "identity_domain_example",
        "imported_package_names": [],
        "attachment_types": []
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


class OdaInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_oda_instance,
            oda_instance_id=self.module.params.get("oda_instance_id"),
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
            self.client.list_oda_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OdaInstanceFactsHelperCustom = get_custom_class("OdaInstanceFactsHelperCustom")


class ResourceFactsHelper(OdaInstanceFactsHelperCustom, OdaInstanceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            oda_instance_id=dict(aliases=["id"], type="str"),
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
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="oda_instance",
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

    module.exit_json(oda_instances=result)


if __name__ == "__main__":
    main()
