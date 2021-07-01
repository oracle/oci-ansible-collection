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
module: oci_identity_compartment_facts
short_description: Fetches details about one or multiple Compartment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Compartment resources in Oracle Cloud Infrastructure
    - Lists the compartments in a specified compartment. The members of the list
      returned depends on the values set for several parameters.
    - With the exception of the tenancy (root compartment), the ListCompartments operation
      returns only the first-level child compartments in the parent compartment specified in
      `compartmentId`. The list does not include any subcompartments of the child
      compartments (grandchildren).
    - The parameter `accessLevel` specifies whether to return only those compartments for which the
      requestor has INSPECT permissions on at least one resource directly
      or indirectly (the resource can be in a subcompartment).
    - The parameter `compartmentIdInSubtree` applies only when you perform ListCompartments on the
      tenancy (root compartment). When set to true, the entire hierarchy of compartments can be returned.
      To get a full list of all compartments and subcompartments in the tenancy (root compartment),
      set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ANY.
    - See L(Where to Get the Tenancy's OCID and User's OCID,https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#five).
    - If I(compartment_id) is specified, the details of a single Compartment will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to get a specific compartment.
        type: str
        aliases: ["id"]
    parent_compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
            - Required to list multiple compartments.
        type: str
    access_level:
        description:
            - Valid values are `ANY` and `ACCESSIBLE`. Default is `ANY`.
              Setting this to `ACCESSIBLE` returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment). For the compartments on which the user indirectly has
              INSPECT permissions, a restricted set of fields is returned.
            - When set to `ANY` permissions are not checked.
        type: str
        choices:
            - "ANY"
            - "ACCESSIBLE"
    compartment_id_in_subtree:
        description:
            - Default is false. Can only be set to true when performing
              ListCompartments on the tenancy (root compartment).
              When set to true, the hierarchy of compartments is traversed
              and all compartments and subcompartments in the tenancy are
              returned depending on the the setting of `accessLevel`.
        type: bool
    name:
        description:
            - A filter to only return resources that match the given name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for NAME is ascending. The NAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by Availability Domain if the scope of the resource type is within a
              single Availability Domain. If you call one of these \\"List\\" operations without specifying
              an Availability Domain, the resources are grouped by Availability Domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List compartments
  oci_identity_compartment_facts:
    parent_compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific compartment
  oci_identity_compartment_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
compartments:
    description:
        - List of Compartment resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the parent compartment containing the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the compartment during creation. The name must be unique across all
                  compartments in the parent. Avoid entering confidential information.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description you assign to the compartment. Does not have to be unique, and it's changeable.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - Date and time the compartment was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The compartment's current state. After creating a compartment, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
            returned: on success
            type: string
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
        is_accessible:
            description:
                - Indicates whether or not the compartment is accessible for the user making the request.
                  Returns true when the user has INSPECT permissions directly on a resource in the
                  compartment or indirectly (permissions can be on a resource in a subcompartment).
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "is_accessible": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CompartmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "parent_compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_compartment,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "access_level",
            "compartment_id_in_subtree",
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_compartments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CompartmentFactsHelperCustom = get_custom_class("CompartmentFactsHelperCustom")


class ResourceFactsHelper(CompartmentFactsHelperCustom, CompartmentFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(aliases=["id"], type="str"),
            parent_compartment_id=dict(type="str"),
            access_level=dict(type="str", choices=["ANY", "ACCESSIBLE"]),
            compartment_id_in_subtree=dict(type="bool"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="compartment",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(compartments=result)


if __name__ == "__main__":
    main()
