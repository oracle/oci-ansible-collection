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
module: oci_data_science_model_actions
short_description: Perform actions on a Model resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Model resource in Oracle Cloud Infrastructure
    - For I(action=activate), activates the model.
    - For I(action=change_compartment), moves a model resource into a different compartment.
    - For I(action=deactivate), deactivates the model.
    - For I(action=export_model_artifact), export model artifact from source to the service bucket
    - For I(action=import_model_artifact), import model artifact from service bucket
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    artifact_export_details:
        description:
            - ""
            - Required for I(action=export_model_artifact).
        type: dict
        suboptions:
            artifact_source_type:
                description:
                    - Source type where actually artifact is being stored
                type: str
                choices:
                    - "ORACLE_OBJECT_STORAGE"
                required: true
            namespace:
                description:
                    - The Object Storage namespace used for the request.
                type: str
            source_bucket:
                description:
                    - The name of the bucket. Avoid entering confidential information.
                type: str
            source_object_name:
                description:
                    - The name of the object resulting from the copy operation.
                type: str
            source_region:
                description:
                    - Region in which OSS bucket is present
                type: str
    model_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model.
        type: str
        aliases: ["id"]
        required: true
    artifact_import_details:
        description:
            - ""
            - Required for I(action=import_model_artifact).
        type: dict
        suboptions:
            artifact_source_type:
                description:
                    - Source type where actually artifact is being stored
                type: str
                choices:
                    - "ORACLE_OBJECT_STORAGE"
                required: true
            namespace:
                description:
                    - The Object Storage namespace used for the request.
                type: str
            destination_bucket:
                description:
                    - The name of the bucket. Avoid entering confidential information.
                type: str
            destination_object_name:
                description:
                    - The name of the object resulting from the copy operation.
                type: str
            destination_region:
                description:
                    - Region in which OSS bucket is present
                type: str
    action:
        description:
            - The action to perform on the Model.
        type: str
        required: true
        choices:
            - "activate"
            - "change_compartment"
            - "deactivate"
            - "export_model_artifact"
            - "import_model_artifact"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on model
  oci_data_science_model_actions:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    action: activate

- name: Perform action change_compartment on model
  oci_data_science_model_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action deactivate on model
  oci_data_science_model_actions:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    action: deactivate

- name: Perform action export_model_artifact on model
  oci_data_science_model_actions:
    # required
    artifact_export_details:
      # required
      artifact_source_type: ORACLE_OBJECT_STORAGE

      # optional
      namespace: namespace_example
      source_bucket: source_bucket_example
      source_object_name: source_object_name_example
      source_region: us-phoenix-1
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    action: export_model_artifact

- name: Perform action import_model_artifact on model
  oci_data_science_model_actions:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    artifact_import_details:
      # required
      artifact_source_type: ORACLE_OBJECT_STORAGE

      # optional
      namespace: namespace_example
      destination_bucket: destination_bucket_example
      destination_object_name: destination_object_name_example
      destination_region: us-phoenix-1
    action: import_model_artifact

"""

RETURN = """
model:
    description:
        - Details of the Model resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project associated with the model.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A short description of the model.
            returned: on success
            type: str
            sample: description_example
        lifecycle_state:
            description:
                - The state of the model.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - "The date and time the resource was created in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2019-08-25T21:10:29.41Z"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the model.
            returned: on success
            type: str
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
        custom_metadata_list:
            description:
                - An array of custom metadata details for the model.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - "Key of the model Metadata. The key can either be user defined or OCI defined.
                             List of OCI defined keys:
                                   * useCaseType
                                   * libraryName
                                   * libraryVersion
                                   * estimatorClass
                                   * hyperParameters
                                   * testartifactresults"
                    returned: on success
                    type: str
                    sample: key_example
                value:
                    description:
                        - "Allowed values for useCaseType:
                                       binary_classification, regression, multinomial_classification, clustering, recommender,
                                       dimensionality_reduction/representation, time_series_forecasting, anomaly_detection,
                                       topic_modeling, ner, sentiment_analysis, image_classification, object_localization, other"
                        - "Allowed values for libraryName:
                                       scikit-learn, xgboost, tensorflow, pytorch, mxnet, keras, lightGBM, pymc3, pyOD, spacy,
                                       prophet, sktime, statsmodels, cuml, oracle_automl, h2o, transformers, nltk, emcee, pystan,
                                       bert, gensim, flair, word2vec, ensemble, other"
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - Description of model metadata
                    returned: on success
                    type: str
                    sample: description_example
                category:
                    description:
                        - "Category of model metadata which should be null for defined metadata.For custom metadata is should be one of the following values
                          \\"Performance,Training Profile,Training and Validation Datasets,Training Environment,other\\"."
                    returned: on success
                    type: str
                    sample: category_example
        defined_metadata_list:
            description:
                - An array of defined metadata details for the model.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - "Key of the model Metadata. The key can either be user defined or OCI defined.
                             List of OCI defined keys:
                                   * useCaseType
                                   * libraryName
                                   * libraryVersion
                                   * estimatorClass
                                   * hyperParameters
                                   * testartifactresults"
                    returned: on success
                    type: str
                    sample: key_example
                value:
                    description:
                        - "Allowed values for useCaseType:
                                       binary_classification, regression, multinomial_classification, clustering, recommender,
                                       dimensionality_reduction/representation, time_series_forecasting, anomaly_detection,
                                       topic_modeling, ner, sentiment_analysis, image_classification, object_localization, other"
                        - "Allowed values for libraryName:
                                       scikit-learn, xgboost, tensorflow, pytorch, mxnet, keras, lightGBM, pymc3, pyOD, spacy,
                                       prophet, sktime, statsmodels, cuml, oracle_automl, h2o, transformers, nltk, emcee, pystan,
                                       bert, gensim, flair, word2vec, ensemble, other"
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - Description of model metadata
                    returned: on success
                    type: str
                    sample: description_example
                category:
                    description:
                        - "Category of model metadata which should be null for defined metadata.For custom metadata is should be one of the following values
                          \\"Performance,Training Profile,Training and Validation Datasets,Training Environment,other\\"."
                    returned: on success
                    type: str
                    sample: category_example
        input_schema:
            description:
                - Input schema file content in String format
            returned: on success
            type: str
            sample: input_schema_example
        output_schema:
            description:
                - Output schema file content in String format
            returned: on success
            type: str
            sample: output_schema_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "custom_metadata_list": [{
            "key": "key_example",
            "value": "value_example",
            "description": "description_example",
            "category": "category_example"
        }],
        "defined_metadata_list": [{
            "key": "key_example",
            "value": "value_example",
            "description": "description_example",
            "category": "category_example"
        }],
        "input_schema": "input_schema_example",
        "output_schema": "output_schema_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.data_science import DataScienceClient
    from oci.data_science.models import ChangeModelCompartmentDetails
    from oci.data_science.models import ExportModelArtifactDetails
    from oci.data_science.models import ImportModelArtifactDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        change_compartment
        deactivate
        export_model_artifact
        import_model_artifact
    """

    @staticmethod
    def get_module_resource_id_param():
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def activate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_model,
            call_fn_args=(),
            call_fn_kwargs=dict(model_id=self.module.params.get("model_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeModelCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_model_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                change_model_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def deactivate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deactivate_model,
            call_fn_args=(),
            call_fn_kwargs=dict(model_id=self.module.params.get("model_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def export_model_artifact(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ExportModelArtifactDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.export_model_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                export_model_artifact_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def import_model_artifact(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportModelArtifactDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_model_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                import_model_artifact_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataScienceModelActionsHelperCustom = get_custom_class(
    "DataScienceModelActionsHelperCustom"
)


class ResourceHelper(
    DataScienceModelActionsHelperCustom, DataScienceModelActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            artifact_export_details=dict(
                type="dict",
                options=dict(
                    artifact_source_type=dict(
                        type="str", required=True, choices=["ORACLE_OBJECT_STORAGE"]
                    ),
                    namespace=dict(type="str"),
                    source_bucket=dict(type="str"),
                    source_object_name=dict(type="str"),
                    source_region=dict(type="str"),
                ),
            ),
            model_id=dict(aliases=["id"], type="str", required=True),
            artifact_import_details=dict(
                type="dict",
                options=dict(
                    artifact_source_type=dict(
                        type="str", required=True, choices=["ORACLE_OBJECT_STORAGE"]
                    ),
                    namespace=dict(type="str"),
                    destination_bucket=dict(type="str"),
                    destination_object_name=dict(type="str"),
                    destination_region=dict(type="str"),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "activate",
                    "change_compartment",
                    "deactivate",
                    "export_model_artifact",
                    "import_model_artifact",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
