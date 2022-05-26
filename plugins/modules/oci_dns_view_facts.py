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
module: oci_dns_view_facts
short_description: Fetches details about one or multiple View resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple View resources in Oracle Cloud Infrastructure
    - Gets a list of all views within a compartment.
    - The collection can be filtered by display name, id, or lifecycle state. It can be sorted
      on creation time or displayName both in ASC or DESC order. Note that when no lifecycleState
      query parameter is provided, the collection does not include views in the DELETED
      lifecycleState to be consistent with other operations of the API.
    - If I(view_id) is specified, the details of a single View will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    view_id:
        description:
            - The OCID of the target view.
            - Required to get a specific view.
        type: str
        aliases: ["id"]
    if_modified_since:
        description:
            - The `If-Modified-Since` header field makes a GET or HEAD request method
              conditional on the selected representation's modification date being more
              recent than the date provided in the field-value.  Transfer of the
              selected representation's data is avoided if that data has not changed.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment the resource belongs to.
            - Required to list multiple views.
        type: str
    display_name:
        description:
            - The displayName of a resource.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The order to sort the resources.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field by which to sort views.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
    lifecycle_state:
        description:
            - The state of a resource.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
            - "DELETING"
            - "UPDATING"
    scope:
        description:
            - Specifies to operate only on resources that have a matching DNS scope.
        type: str
        choices:
            - "GLOBAL"
            - "PRIVATE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific view
  oci_dns_view_facts:
    # required
    view_id: "ocid1.view.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    if_modified_since: if_modified_since_example
    scope: GLOBAL

- name: List views
  oci_dns_view_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: displayName
    lifecycle_state: ACTIVE
    scope: GLOBAL

"""

RETURN = """
views:
    description:
        - List of View resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the owning compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the view.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "**Example:** `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "**Example:** `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        id:
            description:
                - The OCID of the view.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        _self:
            description:
                - The canonical absolute URL of the resource.
            returned: on success
            type: str
            sample: _self_example
        time_created:
            description:
                - "The date and time the resource was created in \\"YYYY-MM-ddThh:mm:ssZ\\" format
                  with a Z offset, as defined by RFC 3339."
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time the resource was last updated in \\"YYYY-MM-ddThh:mm:ssZ\\"
                  format with a Z offset, as defined by RFC 3339."
                - "**Example:** `2016-07-22T17:23:59:60Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: str
            sample: ACTIVE
        is_protected:
            description:
                - A Boolean flag indicating whether or not parts of the resource are unable to be explicitly managed.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "_self": "_self_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "is_protected": true
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.dns import DnsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ViewFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "view_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "if_modified_since",
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_view,
            view_id=self.module.params.get("view_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "scope",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_views,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ViewFactsHelperCustom = get_custom_class("ViewFactsHelperCustom")


class ResourceFactsHelper(ViewFactsHelperCustom, ViewFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            view_id=dict(aliases=["id"], type="str"),
            if_modified_since=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "DELETED", "DELETING", "UPDATING"]
            ),
            scope=dict(type="str", choices=["GLOBAL", "PRIVATE"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="view",
        service_client_class=DnsClient,
        namespace="dns",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(views=result)


if __name__ == "__main__":
    main()
