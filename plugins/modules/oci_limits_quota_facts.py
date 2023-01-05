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
module: oci_limits_quota_facts
short_description: Fetches details about one or multiple Quota resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Quota resources in Oracle Cloud Infrastructure
    - Lists all quotas on resources from the given compartment.
    - If I(quota_id) is specified, the details of a single Quota will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    quota_id:
        description:
            - The OCID of the quota.
            - Required to get a specific quota.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the parent compartment (remember that the tenancy is simply the root compartment).
            - Required to list multiple quotas.
        type: str
    name:
        description:
            - name
        type: str
    lifecycle_state:
        description:
            - Filters returned quotas based on the given state.
        type: str
        choices:
            - "ACTIVE"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'. By default, it is ascending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Time created is default ordered as descending. Display name is default ordered as
              ascending.
        type: str
        choices:
            - "NAME"
            - "TIMECREATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific quota
  oci_limits_quota_facts:
    # required
    quota_id: "ocid1.quota.oc1..xxxxxxEXAMPLExxxxxx"

- name: List quotas
  oci_limits_quota_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: NAME

"""

RETURN = """
quotas:
    description:
        - List of Quota resources
    returned: on success
    type: complex
    contains:
        statements:
            description:
                - An array of one or more quota statements written in the declarative quota statement language.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - The OCID of the quota.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the resource this quota applies to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the quota during creation. The name must be unique across all quotas
                  in the tenancy and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description you assign to the quota.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - "Date and time the quota was created, in the format defined by RFC 3339.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        locks:
            description:
                - Locks associated with this resource.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Lock type.
                    returned: on success
                    type: str
                    sample: FULL
                related_resource_id:
                    description:
                        - The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.
                    returned: on success
                    type: str
                    sample: "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx"
                message:
                    description:
                        - A message added by the lock creator. The message typically gives an
                          indication of why the resource is locked.
                    returned: on success
                    type: str
                    sample: message_example
                time_created:
                    description:
                        - Indicates when the lock was created, in the format defined by RFC 3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The quota's current state. After creating a quota, make sure its `lifecycleState` is set to
                  ACTIVE before using it.
            returned: on success
            type: str
            sample: ACTIVE
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
        "statements": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "locks": [{
            "type": "FULL",
            "related_resource_id": "ocid1.relatedresource.oc1..xxxxxxEXAMPLExxxxxx",
            "message": "message_example",
            "time_created": "2013-10-20T19:20:30+01:00"
        }],
        "lifecycle_state": "ACTIVE",
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
    from oci.limits import QuotasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QuotaFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "quota_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_quota, quota_id=self.module.params.get("quota_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
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
            self.client.list_quotas,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


QuotaFactsHelperCustom = get_custom_class("QuotaFactsHelperCustom")


class ResourceFactsHelper(QuotaFactsHelperCustom, QuotaFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            quota_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAME", "TIMECREATED"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="quota",
        service_client_class=QuotasClient,
        namespace="limits",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(quotas=result)


if __name__ == "__main__":
    main()
