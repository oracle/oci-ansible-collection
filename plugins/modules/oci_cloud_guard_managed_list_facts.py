#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_cloud_guard_managed_list_facts
short_description: Fetches details about one or multiple ManagedList resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedList resources in Oracle Cloud Infrastructure
    - Returns a list of ListManagedLists.
      The ListManagedLists operation returns only the managed lists in `compartmentId` passed.
      The list does not include any subcompartments of the compartmentId passed.
    - The parameter `accessLevel` specifies whether to return ManagedLists in only
      those compartments for which the requestor has INSPECT permissions on at least one resource directly
      or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if
      Principal doesn't have access to even one of the child compartments. This is valid only when
      `compartmentIdInSubtree` is set to `true`.
    - The parameter `compartmentIdInSubtree` applies when you perform ListManagedLists on the
      `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned.
      To get a full list of all compartments and subcompartments in the tenancy (root compartment),
      set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.
    - If I(managed_list_id) is specified, the details of a single ManagedList will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    managed_list_id:
        description:
            - The cloudguard list OCID to be passed in the request.
            - Required to get a specific managed_list.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple managed_lists.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    resource_metadata_only:
        description:
            - Default is false.
              When set to true, the list of all Oracle Managed Resources
              Metadata supported by Cloud Guard is returned.
        type: bool
    lifecycle_state:
        description:
            - The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    list_type:
        description:
            - The type of the ManagedList.
        type: str
        choices:
            - "CIDR_BLOCK"
            - "USERS"
            - "GROUPS"
            - "IPV4ADDRESS"
            - "IPV6ADDRESS"
            - "RESOURCE_OCID"
            - "REGION"
            - "COUNTRY"
            - "STATE"
            - "CITY"
            - "TAGS"
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed
              and all compartments and subcompartments in the tenancy are
              returned depending on the the setting of `accessLevel`.
        type: bool
    access_level:
        description:
            - Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`.
              Setting this to `ACCESSIBLE` returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment).
              When set to `RESTRICTED` permissions are checked and no partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
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
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List managed_lists
  oci_cloud_guard_managed_list_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific managed_list
  oci_cloud_guard_managed_list_facts:
    managed_list_id: ocid1.managedlist.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
managed_lists:
    description:
        - List of ManagedList resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - ManagedList display name
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - ManagedList description
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier where the resource is created
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        source_managed_list_id:
            description:
                - OCID of the Source ManagedList
            returned: on success
            type: string
            sample: ocid1.sourcemanagedlist.oc1..xxxxxxEXAMPLExxxxxx
        list_type:
            description:
                - type of the list
            returned: on success
            type: string
            sample: CIDR_BLOCK
        list_items:
            description:
                - List of ManagedListItem
            returned: on success
            type: list
            sample: []
        feed_provider:
            description:
                - provider of the feed
            returned: on success
            type: string
            sample: CUSTOMER
        is_editable:
            description:
                - If this list is editable or not
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The date and time the managed list was created. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The date and time the managed list was updated. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: string
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecyle_details_example
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
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        items:
            description:
                - List of ManagedListSummary
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - Unique identifier that is immutable on creation
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - ManagedList display name
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - ManagedList description
                    returned: on success
                    type: string
                    sample: description_example
                compartment_id:
                    description:
                        - Compartment Identifier where the resource is created
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                source_managed_list_id:
                    description:
                        - OCID of the Source ManagedList
                    returned: on success
                    type: string
                    sample: ocid1.sourcemanagedlist.oc1..xxxxxxEXAMPLExxxxxx
                list_type:
                    description:
                        - type of the list
                    returned: on success
                    type: string
                    sample: CIDR_BLOCK
                feed_provider:
                    description:
                        - provider of the feed
                    returned: on success
                    type: string
                    sample: CUSTOMER
                is_editable:
                    description:
                        - If this list is editable or not
                    returned: on success
                    type: bool
                    sample: true
                list_items:
                    description:
                        - List of ManagedListItem
                    returned: on success
                    type: list
                    sample: []
                time_created:
                    description:
                        - The date and time the managed list was created. Format defined by RFC3339.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_updated:
                    description:
                        - The date and time the managed list was updated. Format defined by RFC3339.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                lifecycle_state:
                    description:
                        - The current state of the resource.
                    returned: on success
                    type: string
                    sample: CREATING
                lifecyle_details:
                    description:
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: string
                    sample: lifecyle_details_example
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
                        - System tags for this resource. Each key is predefined and scoped to a namespace.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                          System tags can be viewed by users, but can only be created by the system.
                        - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
                    returned: on success
                    type: dict
                    sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "source_managed_list_id": "ocid1.sourcemanagedlist.oc1..xxxxxxEXAMPLExxxxxx",
        "list_type": "CIDR_BLOCK",
        "list_items": [],
        "feed_provider": "CUSTOMER",
        "is_editable": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "items": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "source_managed_list_id": "ocid1.sourcemanagedlist.oc1..xxxxxxEXAMPLExxxxxx",
            "list_type": "CIDR_BLOCK",
            "feed_provider": "CUSTOMER",
            "is_editable": true,
            "list_items": [],
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "lifecyle_details": "lifecyle_details_example",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "system_tags": {}
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.cloud_guard import CloudGuardClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedListFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "managed_list_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_list,
            managed_list_id=self.module.params.get("managed_list_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "resource_metadata_only",
            "lifecycle_state",
            "list_type",
            "compartment_id_in_subtree",
            "access_level",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_managed_lists,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ManagedListFactsHelperCustom = get_custom_class("ManagedListFactsHelperCustom")


class ResourceFactsHelper(ManagedListFactsHelperCustom, ManagedListFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_list_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            resource_metadata_only=dict(type="bool"),
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
            list_type=dict(
                type="str",
                choices=[
                    "CIDR_BLOCK",
                    "USERS",
                    "GROUPS",
                    "IPV4ADDRESS",
                    "IPV6ADDRESS",
                    "RESOURCE_OCID",
                    "REGION",
                    "COUNTRY",
                    "STATE",
                    "CITY",
                    "TAGS",
                ],
            ),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_list",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_lists=result)


if __name__ == "__main__":
    main()
