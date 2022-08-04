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
module: oci_data_science_model_deployment_facts
short_description: Fetches details about one or multiple ModelDeployment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ModelDeployment resources in Oracle Cloud Infrastructure
    - Lists all model deployments in the specified compartment. Only one parameter other than compartmentId may also be included in a query. The query must
      include compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned.
    - If I(model_deployment_id) is specified, the details of a single ModelDeployment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    model_deployment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment.
            - Required to get a specific model_deployment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple model_deployments.
        type: str
    project_id:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project.
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
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "FAILED"
            - "INACTIVE"
            - "UPDATING"
            - "DELETED"
            - "NEEDS_ATTENTION"
    created_by:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the
              resource.
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
              in descending order. When you sort by `displayName`, results are
              shown in ascending order. Sort order for the `displayName` field is case sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific model_deployment
  oci_data_science_model_deployment_facts:
    # required
    model_deployment_id: "ocid1.modeldeployment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List model_deployments
  oci_data_science_model_deployment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    created_by: created_by_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
model_deployments:
    description:
        - List of ModelDeployment resources
    returned: on success
    type: complex
    contains:
        lifecycle_details:
            description:
                - Details about the state of the model deployment.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created, in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2019-08-25T21:10:29.41Z"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - "A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
                  Example: `My ModelDeployment`"
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A short description of the model deployment.
            returned: on success
            type: str
            sample: description_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project associated with the model deployment.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the model deployment.
            returned: on success
            type: str
            sample: created_by_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model deployment's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        model_deployment_configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                deployment_type:
                    description:
                        - The type of the model deployment.
                    returned: on success
                    type: str
                    sample: SINGLE_MODEL
                model_configuration_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        model_id:
                            description:
                                - The OCID of the model you want to deploy.
                            returned: on success
                            type: str
                            sample: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
                        instance_configuration:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                instance_shape_name:
                                    description:
                                        - The shape used to launch the model deployment instances.
                                    returned: on success
                                    type: str
                                    sample: instance_shape_name_example
                                model_deployment_instance_shape_config_details:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        ocpus:
                                            description:
                                                - A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows the ocpu count to be
                                                  specified.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                                        memory_in_gbs:
                                            description:
                                                - A model-deployment instance of type VM.Standard.E3.Flex or VM.Standard.E4.Flex allows memory to be specified.
                                                  This specifies the size of the memory in GBs.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                        scaling_policy:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                policy_type:
                                    description:
                                        - The type of scaling policy.
                                    returned: on success
                                    type: str
                                    sample: FIXED_SIZE
                                instance_count:
                                    description:
                                        - The number of instances for the model deployment.
                                    returned: on success
                                    type: int
                                    sample: 56
                        bandwidth_mbps:
                            description:
                                - The network bandwidth for the model.
                            returned: on success
                            type: int
                            sample: 56
        category_log_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                access:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        log_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log to work with.
                            returned: on success
                            type: str
                            sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
                        log_group_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log group to work with.
                            returned: on success
                            type: str
                            sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                predict:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        log_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log to work with.
                            returned: on success
                            type: str
                            sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
                        log_group_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a log group to work with.
                            returned: on success
                            type: str
                            sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
        model_deployment_url:
            description:
                - The URL to interact with the model deployment.
            returned: on success
            type: str
            sample: model_deployment_url_example
        lifecycle_state:
            description:
                - The state of the model deployment.
            returned: on success
            type: str
            sample: CREATING
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
        "lifecycle_details": "lifecycle_details_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "description": "description_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "created_by": "created_by_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "model_deployment_configuration_details": {
            "deployment_type": "SINGLE_MODEL",
            "model_configuration_details": {
                "model_id": "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx",
                "instance_configuration": {
                    "instance_shape_name": "instance_shape_name_example",
                    "model_deployment_instance_shape_config_details": {
                        "ocpus": 3.4,
                        "memory_in_gbs": 3.4
                    }
                },
                "scaling_policy": {
                    "policy_type": "FIXED_SIZE",
                    "instance_count": 56
                },
                "bandwidth_mbps": 56
            }
        },
        "category_log_details": {
            "access": {
                "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx",
                "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "predict": {
                "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx",
                "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
            }
        },
        "model_deployment_url": "model_deployment_url_example",
        "lifecycle_state": "CREATING",
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


class DataScienceModelDeploymentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "model_deployment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model_deployment,
            model_deployment_id=self.module.params.get("model_deployment_id"),
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
            self.client.list_model_deployments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataScienceModelDeploymentFactsHelperCustom = get_custom_class(
    "DataScienceModelDeploymentFactsHelperCustom"
)


class ResourceFactsHelper(
    DataScienceModelDeploymentFactsHelperCustom,
    DataScienceModelDeploymentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            model_deployment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "DELETING",
                    "FAILED",
                    "INACTIVE",
                    "UPDATING",
                    "DELETED",
                    "NEEDS_ATTENTION",
                ],
            ),
            created_by=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="model_deployment",
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

    module.exit_json(model_deployments=result)


if __name__ == "__main__":
    main()
