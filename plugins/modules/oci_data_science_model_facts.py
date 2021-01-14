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
module: oci_data_science_model_facts
short_description: Fetches details about one or multiple Model resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Model resources in Oracle Cloud Infrastructure
    - Lists models in the specified compartment.
    - If I(model_id) is specified, the details of a single Model will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    model_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the model.
            - Required to get a specific model.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple models.
        type: str
    project_id:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the project.
        type: str
    display_name:
        description:
            - <b>Filter</b> results by its user-friendly name.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - <b>Filter</b> results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
            - "FAILED"
            - "INACTIVE"
    created_by:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the user who created the resource.
        type: str
    sort_order:
        description:
            - Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the field to sort by. Accepts only one field.
              By default, when you sort by `timeCreated`, results are shown
              in descending order. All other fields default to ascending order. Sort order for `displayName` field is case sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
            - "lifecycleState"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List models
  oci_data_science_model_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific model
  oci_data_science_model_facts:
    model_id: ocid1.model.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
models:
    description:
        - List of Model resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the model.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the model's compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the project associated with the model.
            returned: on success
            type: string
            sample: ocid1.project.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - A short blurb describing the model.
            returned: on success
            type: string
            sample: description_example
        lifecycle_state:
            description:
                - The state of the model.
            returned: on success
            type: string
            sample: ACTIVE
        time_created:
            description:
                - "The date and time the resource was created, in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2019-08-25T21:10:29.41Z"
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/API/Concepts/identifiers.htm) of the user who created the model.
            returned: on success
            type: string
            sample: created_by_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
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
    from oci.data_science import DataScienceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "model_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "project_id",
            "display_name",
            "lifecycle_state",
            "created_by",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_models,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataScienceModelFactsHelperCustom = get_custom_class(
    "DataScienceModelFactsHelperCustom"
)


class ResourceFactsHelper(
    DataScienceModelFactsHelperCustom, DataScienceModelFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            model_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "DELETED", "FAILED", "INACTIVE"]
            ),
            created_by=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeCreated", "displayName", "lifecycleState"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="model",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(models=result)


if __name__ == "__main__":
    main()
