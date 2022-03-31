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
module: oci_data_science_model
short_description: Manage a Model resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Model resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new model.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_science_model_actions) module: activate, change_compartment, deactivate."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to create the model in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
            - Required for create using I(state=present).
        type: str
    input_schema:
        description:
            - Input schema file content in String format
        type: str
    output_schema:
        description:
            - Output schema file content in String format
        type: str
    display_name:
        description:
            - "A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
              Example: `My Model`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A short description of the model.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    custom_metadata_list:
        description:
            - An array of custom metadata details for the model.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
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
                type: str
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
                type: str
            description:
                description:
                    - Description of model metadata
                type: str
            category:
                description:
                    - "Category of model metadata which should be null for defined metadata.For custom metadata is should be one of the following values
                      \\"Performance,Training Profile,Training and Validation Datasets,Training Environment,other\\"."
                type: str
    defined_metadata_list:
        description:
            - An array of defined metadata details for the model.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
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
                type: str
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
                type: str
            description:
                description:
                    - Description of model metadata
                type: str
            category:
                description:
                    - "Category of model metadata which should be null for defined metadata.For custom metadata is should be one of the following values
                      \\"Performance,Training Profile,Training and Validation Datasets,Training Environment,other\\"."
                type: str
    model_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the model.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Model.
            - Use I(state=present) to create or update a Model.
            - Use I(state=absent) to delete a Model.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create model
  oci_data_science_model:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    input_schema: input_schema_example
    output_schema: output_schema_example
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    custom_metadata_list:
    - # optional
      key: key_example
      value: value_example
      description: description_example
      category: category_example
    defined_metadata_list:
    - # optional
      key: key_example
      value: value_example
      description: description_example
      category: category_example

- name: Update model
  oci_data_science_model:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    custom_metadata_list:
    - # optional
      key: key_example
      value: value_example
      description: description_example
      category: category_example
    defined_metadata_list:
    - # optional
      key: key_example
      value: value_example
      description: description_example
      category: category_example

- name: Update model using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_model:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    custom_metadata_list:
    - # optional
      key: key_example
      value: value_example
      description: description_example
      category: category_example
    defined_metadata_list:
    - # optional
      key: key_example
      value: value_example
      description: description_example
      category: category_example

- name: Delete model
  oci_data_science_model:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete model using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_model:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.data_science import DataScienceClient
    from oci.data_science.models import CreateModelDetails
    from oci.data_science.models import UpdateModelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceModelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DataScienceModelHelperGen, self).get_possible_entity_types() + [
            "model",
            "models",
            "dataSciencemodel",
            "dataSciencemodels",
            "modelresource",
            "modelsresource",
            "datascience",
        ]

    def get_module_resource_id_param(self):
        return "model_id"

    def get_module_resource_id(self):
        return self.module.params.get("model_id")

    def get_get_fn(self):
        return self.client.get_model

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_model, model_id=self.module.params.get("model_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_models, **kwargs)

    def get_create_model_class(self):
        return CreateModelDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_model,
            call_fn_args=(),
            call_fn_kwargs=dict(create_model_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateModelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_model,
            call_fn_args=(),
            call_fn_kwargs=dict(
                model_id=self.module.params.get("model_id"),
                update_model_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_model,
            call_fn_args=(),
            call_fn_kwargs=dict(model_id=self.module.params.get("model_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataScienceModelHelperCustom = get_custom_class("DataScienceModelHelperCustom")


class ResourceHelper(DataScienceModelHelperCustom, DataScienceModelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            input_schema=dict(type="str"),
            output_schema=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            custom_metadata_list=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", no_log=True),
                    value=dict(type="str"),
                    description=dict(type="str"),
                    category=dict(type="str"),
                ),
            ),
            defined_metadata_list=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", no_log=True),
                    value=dict(type="str"),
                    description=dict(type="str"),
                    category=dict(type="str"),
                ),
            ),
            model_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
