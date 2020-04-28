#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_identity_tag_facts
short_description: Fetches details about one or multiple Tag resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Tag resources in Oracle Cloud Infrastructure
    - Lists the tag definitions in the specified tag namespace.
    - If I(tag_name) is specified, the details of a single Tag will be returned.
version_added: "2.5"
options:
    tag_namespace_id:
        description:
            - The OCID of the tag namespace.
        type: str
        required: true
    tag_name:
        description:
            - The name of the tag.
            - Required to get a specific tag.
        type: str
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List tags
  oci_identity_tag_facts:
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific tag
  oci_identity_tag_facts:
    tag_namespace_id: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
    tag_name: tag_name_example

"""

RETURN = """
tags:
    description:
        - List of Tag resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains the tag definition.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        tag_namespace_id:
            description:
                - The OCID of the namespace that contains the tag definition.
            returned: on success
            type: string
            sample: ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx
        tag_namespace_name:
            description:
                - The name of the tag namespace that contains the tag definition.
            returned: on success
            type: string
            sample: tag_namespace_name_example
        id:
            description:
                - The OCID of the tag definition.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name assigned to the tag during creation. This is the tag key definition.
                  The name must be unique within the tag namespace and cannot be changed.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description you assign to the tag.
            returned: on success
            type: string
            sample: description_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_retired:
            description:
                - Indicates whether the tag is retired.
                  See L(Retiring Key Definitions and Namespace
                  Definitions,https://docs.cloud.oracle.com/Content/Identity/Concepts/taggingoverview.htm#Retiring).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The tag's current state. After creating a tag, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tag, make sure its
                  `lifecycleState` is INACTIVE before using it. If you delete a tag, you cannot delete another tag until the deleted tag's `lifecycleState`
                  changes from DELETING to DELETED.
            returned: on success
            type: string
            sample: ACTIVE
        time_created:
            description:
                - Date and time the tag was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        is_cost_tracking:
            description:
                - Indicates whether the tag is enabled for cost tracking.
            returned: on success
            type: bool
            sample: true
        validator:
            description:
                - The tag must have a value type, which is specified with a validator. Tags can use either a
                  static value or a list of possible values. Static values are entered by a user applying the tag
                  to a resource. Lists are created by you and the user must apply a value from the list. Lists
                  are validiated.
                - If you use the default validiator (or don't define a validator), the user applying the tag
                  enters a value. No additional validation is performed.
                - To clear the validator, call UpdateTag with
                  L(DefaultTagDefinitionValidator,https://docs.cloud.oracle.com/api/#/en/identity/latest/datatypes/DefaultTagDefinitionValidator).
            returned: on success
            type: complex
            contains:
                validator_type:
                    description:
                        - "Specifies the type of validation: a static value (no validation) or a list."
                    returned: on success
                    type: string
                    sample: ENUM
                values:
                    description:
                        - The list of allowed values for a definedTag value.
                    returned: on success
                    type: list
                    sample: []
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_id": "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_name": "tag_namespace_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_retired": true,
        "lifecycle_state": "ACTIVE",
        "time_created": "2016-08-25T21:10:29.600Z",
        "is_cost_tracking": true,
        "validator": {
            "validator_type": "ENUM",
            "values": []
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
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "tag_namespace_id",
            "tag_name",
        ]

    def get_required_params_for_list(self):
        return [
            "tag_namespace_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
            tag_name=self.module.params.get("tag_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_tags,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
            **optional_kwargs
        )


TagFactsHelperCustom = get_custom_class("TagFactsHelperCustom")


class ResourceFactsHelper(TagFactsHelperCustom, TagFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tag_namespace_id=dict(type="str", required=True),
            tag_name=dict(type="str"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "INACTIVE", "DELETING", "DELETED"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tag",
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

    module.exit_json(tags=result)


if __name__ == "__main__":
    main()
