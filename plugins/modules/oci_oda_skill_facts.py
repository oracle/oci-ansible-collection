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
module: oci_oda_skill_facts
short_description: Fetches details about one or multiple Skill resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Skill resources in Oracle Cloud Infrastructure
    - Returns a page of Skills that belong to the specified Digital Assistant instance.
    - If the `opc-next-page` header appears in the response, then
      there are more items to retrieve. To get the next page in the subsequent
      GET request, include the header's value as the `page` query parameter.
    - If I(skill_id) is specified, the details of a single Skill will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    skill_id:
        description:
            - Unique Skill identifier.
            - Required to get a specific skill.
        type: str
        aliases: ["id"]
    category:
        description:
            - List only Bot resources with this category.
        type: str
    name:
        description:
            - List only Bot resources with this name. Names are unique and may not change.
            - "Example: `MySkill`"
        type: str
    version:
        description:
            - List only Bot resources with this version. Versions are unique and may not change.
            - "Example: `1.0`"
        type: str
    namespace:
        description:
            - List only Bot resources with this namespace. Namespaces may not change.
            - "Example: `MyNamespace`"
        type: str
    platform_version:
        description:
            - List only Bot resources with this platform version.
        type: str
    lifecycle_state:
        description:
            - List only the resources that are in this lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    lifecycle_details:
        description:
            - List only Bot resources with this lifecycle details.
        type: str
    sort_order:
        description:
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.
            - The default sort order for `timeCreated` and `timeUpdated` is descending.
              For all other sort fields the default sort order is ascending.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific skill
  oci_oda_skill_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    skill_id: "ocid1.skill.oc1..xxxxxxEXAMPLExxxxxx"

- name: List skills
  oci_oda_skill_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    skill_id: "ocid1.skill.oc1..xxxxxxEXAMPLExxxxxx"
    category: category_example
    name: name_example
    version: version_example
    namespace: namespace_example
    platform_version: platform_version_example
    lifecycle_state: CREATING
    lifecycle_details: lifecycle_details_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
skills:
    description:
        - List of Skill resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A short description of the resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        base_id:
            description:
                - The unique identifier for the base reource (when this resource extends another).
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.base.oc1..xxxxxxEXAMPLExxxxxx"
        multilingual_mode:
            description:
                - The multilingual mode for the resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: NATIVE
        primary_language_tag:
            description:
                - The primary language for the resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: primary_language_tag_example
        native_language_tags:
            description:
                - A list of native languages supported by this resource.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - Unique immutable identifier that was assigned when the resource was created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.
            returned: on success
            type: str
            sample: name_example
        version:
            description:
                - The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a
                  letter or a number.
            returned: on success
            type: str
            sample: version_example
        display_name:
            description:
                - The resource's display name.
            returned: on success
            type: str
            sample: display_name_example
        namespace:
            description:
                - The resource's namespace.
            returned: on success
            type: str
            sample: namespace_example
        category:
            description:
                - The resource's category.  This is used to group resource's together.
            returned: on success
            type: str
            sample: category_example
        lifecycle_state:
            description:
                - The resource's current state.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - The resource's publish state.
            returned: on success
            type: str
            sample: PUBLISHED
        platform_version:
            description:
                - The ODA Platform Version for this resource.
            returned: on success
            type: str
            sample: platform_version_example
        time_created:
            description:
                - When the resource was created. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the resource was last updated. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "description": "description_example",
        "base_id": "ocid1.base.oc1..xxxxxxEXAMPLExxxxxx",
        "multilingual_mode": "NATIVE",
        "primary_language_tag": "primary_language_tag_example",
        "native_language_tags": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "version": "version_example",
        "display_name": "display_name_example",
        "namespace": "namespace_example",
        "category": "category_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "PUBLISHED",
        "platform_version": "platform_version_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.oda import ManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SkillFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
            "skill_id",
        ]

    def get_required_params_for_list(self):
        return [
            "oda_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_skill,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            skill_id=self.module.params.get("skill_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "skill_id",
            "category",
            "name",
            "version",
            "namespace",
            "platform_version",
            "lifecycle_state",
            "lifecycle_details",
            "sort_order",
            "sort_by",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_skills,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            **optional_kwargs
        )


SkillFactsHelperCustom = get_custom_class("SkillFactsHelperCustom")


class ResourceFactsHelper(SkillFactsHelperCustom, SkillFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            oda_instance_id=dict(type="str", required=True),
            skill_id=dict(aliases=["id"], type="str"),
            category=dict(type="str"),
            name=dict(type="str"),
            version=dict(type="str"),
            namespace=dict(type="str"),
            platform_version=dict(type="str"),
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
            lifecycle_details=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "timeUpdated", "name"]),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="skill",
        service_client_class=ManagementClient,
        namespace="oda",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(skills=result)


if __name__ == "__main__":
    main()
