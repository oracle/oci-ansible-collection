#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_ai_language_model
short_description: Manage a Model resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Model resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new model for training and train the model with date provided.
    - "This resource has the following action operations in the M(oracle.oci.oci_ai_language_model_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)  for the models compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
            - Required for create using I(state=present).
        type: str
    model_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            classification_mode:
                description:
                    - ""
                    - Applicable when model_type is 'TEXT_CLASSIFICATION'
                type: dict
                suboptions:
                    classification_mode:
                        description:
                            - classification Modes
                        type: str
                        choices:
                            - "MULTI_CLASS"
                            - "MULTI_LABEL"
                        required: true
                    version:
                        description:
                            - Optional if nothing specified latest base model will be used for training. Supported versions can be found at
                              /modelTypes/{modelType}
                        type: str
            language_code:
                description:
                    - supported language default value is en
                type: str
            model_type:
                description:
                    - Model type
                type: str
                choices:
                    - "PRE_TRAINED_KEYPHRASE_EXTRACTION"
                    - "PRE_TRAINED_HEALTH_NLU"
                    - "PRE_TRAINED_UNIVERSAL"
                    - "NAMED_ENTITY_RECOGNITION"
                    - "PRE_TRAINED_LANGUAGE_DETECTION"
                    - "PRE_TRAINED_NAMED_ENTITY_RECOGNITION"
                    - "PRE_TRAINED_SENTIMENT_ANALYSIS"
                    - "PRE_TRAINED_PHI"
                    - "PRE_TRAINED_TEXT_CLASSIFICATION"
                    - "TEXT_CLASSIFICATION"
                    - "PRE_TRAINED_SUMMARIZATION"
                    - "PRE_TRAINED_PII"
                required: true
            version:
                description:
                    - Optional pre trained model version. if nothing specified latest pre trained model will be used.
                      Supported versions can be found at /modelTypes/{modelType}
                    - Applicable when model_type is one of ['NAMED_ENTITY_RECOGNITION', 'PRE_TRAINED_PII', 'PRE_TRAINED_PHI', 'PRE_TRAINED_TEXT_CLASSIFICATION',
                      'PRE_TRAINED_NAMED_ENTITY_RECOGNITION', 'PRE_TRAINED_HEALTH_NLU', 'PRE_TRAINED_LANGUAGE_DETECTION', 'PRE_TRAINED_KEYPHRASE_EXTRACTION',
                      'PRE_TRAINED_SENTIMENT_ANALYSIS', 'PRE_TRAINED_SUMMARIZATION', 'PRE_TRAINED_UNIVERSAL']
                type: str
    training_dataset:
        description:
            - ""
        type: dict
        suboptions:
            dataset_id:
                description:
                    - Data Science Labelling Service OCID
                    - Required when dataset_type is 'DATA_SCIENCE_LABELING'
                type: str
            dataset_type:
                description:
                    - Possible data sets
                type: str
                choices:
                    - "DATA_SCIENCE_LABELING"
                    - "OBJECT_STORAGE"
                required: true
            location_details:
                description:
                    - ""
                    - Required when dataset_type is 'OBJECT_STORAGE'
                type: dict
                suboptions:
                    location_type:
                        description:
                            - Possible object storage location types
                        type: str
                        choices:
                            - "OBJECT_LIST"
                        required: true
                    namespace_name:
                        description:
                            - Object storage namespace
                        type: str
                        required: true
                    bucket_name:
                        description:
                            - Object storage bucket name
                        type: str
                        required: true
                    object_names:
                        description:
                            - Array of files which need to be processed in the bucket
                        type: list
                        elements: str
                        required: true
    test_strategy:
        description:
            - ""
        type: dict
        suboptions:
            strategy_type:
                description:
                    - This information will define the test strategy
                      different datasets for test and validation(optional) dataset.
                type: str
                choices:
                    - "TEST_AND_VALIDATION_DATASET"
                required: true
            testing_dataset:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    dataset_id:
                        description:
                            - Data Science Labelling Service OCID
                            - Required when dataset_type is 'DATA_SCIENCE_LABELING'
                        type: str
                    dataset_type:
                        description:
                            - Possible data sets
                        type: str
                        choices:
                            - "DATA_SCIENCE_LABELING"
                            - "OBJECT_STORAGE"
                        required: true
                    location_details:
                        description:
                            - ""
                            - Required when dataset_type is 'OBJECT_STORAGE'
                        type: dict
                        suboptions:
                            location_type:
                                description:
                                    - Possible object storage location types
                                type: str
                                choices:
                                    - "OBJECT_LIST"
                                required: true
                            namespace_name:
                                description:
                                    - Object storage namespace
                                type: str
                                required: true
                            bucket_name:
                                description:
                                    - Object storage bucket name
                                type: str
                                required: true
                            object_names:
                                description:
                                    - Array of files which need to be processed in the bucket
                                type: list
                                elements: str
                                required: true
            validation_dataset:
                description:
                    - ""
                type: dict
                suboptions:
                    dataset_id:
                        description:
                            - Data Science Labelling Service OCID
                            - Required when dataset_type is 'DATA_SCIENCE_LABELING'
                        type: str
                    dataset_type:
                        description:
                            - Possible data sets
                        type: str
                        choices:
                            - "DATA_SCIENCE_LABELING"
                            - "OBJECT_STORAGE"
                        required: true
                    location_details:
                        description:
                            - ""
                            - Required when dataset_type is 'OBJECT_STORAGE'
                        type: dict
                        suboptions:
                            location_type:
                                description:
                                    - Possible object storage location types
                                type: str
                                choices:
                                    - "OBJECT_LIST"
                                required: true
                            namespace_name:
                                description:
                                    - Object storage namespace
                                type: str
                                required: true
                            bucket_name:
                                description:
                                    - Object storage bucket name
                                type: str
                                required: true
                            object_names:
                                description:
                                    - Array of files which need to be processed in the bucket
                                type: list
                                elements: str
                                required: true
    display_name:
        description:
            - A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A short description of the a model.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    model_id:
        description:
            - unique model OCID.
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
  oci_ai_language_model:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    model_details:
      # required
      model_type: PRE_TRAINED_KEYPHRASE_EXTRACTION

      # optional
      language_code: language_code_example
      version: version_example

    # optional
    training_dataset:
      # required
      dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
      dataset_type: DATA_SCIENCE_LABELING
    test_strategy:
      # required
      strategy_type: TEST_AND_VALIDATION_DATASET
      testing_dataset:
        # required
        dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
        dataset_type: DATA_SCIENCE_LABELING

        # optional
      validation_dataset:
        # required
        dataset_id: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
        dataset_type: DATA_SCIENCE_LABELING
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update model
  oci_ai_language_model:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update model using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_language_model:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete model
  oci_ai_language_model:
    # required
    model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete model using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ai_language_model:
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
                - Unique identifier model OCID of a model that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)  for the model's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - A short description of the Model.
            returned: on success
            type: str
            sample: description_example
        model_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                version:
                    description:
                        - Optional if nothing specified latest base model will be used for training. Supported versions can be found at /modelTypes/{modelType}
                    returned: on success
                    type: str
                    sample: version_example
                language_code:
                    description:
                        - supported language default value is en
                    returned: on success
                    type: str
                    sample: language_code_example
                model_type:
                    description:
                        - Model type
                    returned: on success
                    type: str
                    sample: NAMED_ENTITY_RECOGNITION
                classification_mode:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        classification_mode:
                            description:
                                - classification Modes
                            returned: on success
                            type: str
                            sample: MULTI_CLASS
                        version:
                            description:
                                - Optional if nothing specified latest base model will be used for training. Supported versions can be found at
                                  /modelTypes/{modelType}
                            returned: on success
                            type: str
                            sample: version_example
        time_created:
            description:
                - The time the the model was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the model was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The state of the model.
            returned: on success
            type: str
            sample: DELETING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        training_dataset:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                dataset_id:
                    description:
                        - Data Science Labelling Service OCID
                    returned: on success
                    type: str
                    sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                dataset_type:
                    description:
                        - Possible data sets
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                location_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        location_type:
                            description:
                                - Possible object storage location types
                            returned: on success
                            type: str
                            sample: OBJECT_LIST
                        namespace_name:
                            description:
                                - Object storage namespace
                            returned: on success
                            type: str
                            sample: namespace_name_example
                        bucket_name:
                            description:
                                - Object storage bucket name
                            returned: on success
                            type: str
                            sample: bucket_name_example
                        object_names:
                            description:
                                - Array of files which need to be processed in the bucket
                            returned: on success
                            type: list
                            sample: []
        evaluation_results:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                entity_metrics:
                    description:
                        - List of entity metrics
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Entity label
                            returned: on success
                            type: str
                            sample: label_example
                        f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                model_type:
                    description:
                        - Model type
                    returned: on success
                    type: str
                    sample: NAMED_ENTITY_RECOGNITION
                metrics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        micro_f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        micro_precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        micro_recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                        macro_f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        macro_precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        macro_recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                        weighted_f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        weighted_precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        weighted_recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                        accuracy:
                            description:
                                - The fraction of the labels that were correctly recognised .
                            returned: on success
                            type: float
                            sample: 3.4
                class_metrics:
                    description:
                        - List of text classification metrics
                    returned: on success
                    type: complex
                    contains:
                        label:
                            description:
                                - Text classification label
                            returned: on success
                            type: str
                            sample: label_example
                        f1:
                            description:
                                - F1-score, is a measure of a model's accuracy on a dataset
                            returned: on success
                            type: float
                            sample: 3.4
                        precision:
                            description:
                                - Precision refers to the number of true positives divided by the total number of positive predictions (i.e., the number of true
                                  positives plus the number of false positives)
                            returned: on success
                            type: float
                            sample: 3.4
                        recall:
                            description:
                                - Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what
                                  was actually tagged. The recall metric reveals how many of the predicted classes are correct.
                            returned: on success
                            type: float
                            sample: 3.4
                        support:
                            description:
                                - number of samples in the test set
                            returned: on success
                            type: float
                            sample: 3.4
                confusion_matrix:
                    description:
                        - class level confusion matrix
                    returned: on success
                    type: complex
                    contains:
                        matrix:
                            description:
                                - confusion matrix data
                            returned: on success
                            type: dict
                            sample: {}
                labels:
                    description:
                        - labels
                    returned: on success
                    type: list
                    sample: []
        test_strategy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                strategy_type:
                    description:
                        - This information will define the test strategy
                          different datasets for test and validation(optional) dataset.
                    returned: on success
                    type: str
                    sample: TEST_AND_VALIDATION_DATASET
                testing_dataset:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        dataset_id:
                            description:
                                - Data Science Labelling Service OCID
                            returned: on success
                            type: str
                            sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                        dataset_type:
                            description:
                                - Possible data sets
                            returned: on success
                            type: str
                            sample: OBJECT_STORAGE
                        location_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                location_type:
                                    description:
                                        - Possible object storage location types
                                    returned: on success
                                    type: str
                                    sample: OBJECT_LIST
                                namespace_name:
                                    description:
                                        - Object storage namespace
                                    returned: on success
                                    type: str
                                    sample: namespace_name_example
                                bucket_name:
                                    description:
                                        - Object storage bucket name
                                    returned: on success
                                    type: str
                                    sample: bucket_name_example
                                object_names:
                                    description:
                                        - Array of files which need to be processed in the bucket
                                    returned: on success
                                    type: list
                                    sample: []
                validation_dataset:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        dataset_id:
                            description:
                                - Data Science Labelling Service OCID
                            returned: on success
                            type: str
                            sample: "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx"
                        dataset_type:
                            description:
                                - Possible data sets
                            returned: on success
                            type: str
                            sample: OBJECT_STORAGE
                        location_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                location_type:
                                    description:
                                        - Possible object storage location types
                                    returned: on success
                                    type: str
                                    sample: OBJECT_LIST
                                namespace_name:
                                    description:
                                        - Object storage namespace
                                    returned: on success
                                    type: str
                                    sample: namespace_name_example
                                bucket_name:
                                    description:
                                        - Object storage bucket name
                                    returned: on success
                                    type: str
                                    sample: bucket_name_example
                                object_names:
                                    description:
                                        - Array of files which need to be processed in the bucket
                                    returned: on success
                                    type: list
                                    sample: []
        version:
            description:
                - "For pre trained models this will identify model type version used for model creation
                  For custom identifying the model by model id is difficult. This param provides ease of use for end customer.
                  <<service>>::<<service-name>>_<<model-type-version>>::<<custom model on which this training has to be done>>
                  ex: ai-lang::NER_V1::CUSTOM-V0"
            returned: on success
            type: str
            sample: version_example
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{ \\"orcl-cloud\\": { \\"free-tier-retained\\": \\"true\\" } }`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "model_details": {
            "version": "version_example",
            "language_code": "language_code_example",
            "model_type": "NAMED_ENTITY_RECOGNITION",
            "classification_mode": {
                "classification_mode": "MULTI_CLASS",
                "version": "version_example"
            }
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "DELETING",
        "lifecycle_details": "lifecycle_details_example",
        "training_dataset": {
            "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
            "dataset_type": "OBJECT_STORAGE",
            "location_details": {
                "location_type": "OBJECT_LIST",
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example",
                "object_names": []
            }
        },
        "evaluation_results": {
            "entity_metrics": [{
                "label": "label_example",
                "f1": 3.4,
                "precision": 3.4,
                "recall": 3.4
            }],
            "model_type": "NAMED_ENTITY_RECOGNITION",
            "metrics": {
                "micro_f1": 3.4,
                "micro_precision": 3.4,
                "micro_recall": 3.4,
                "macro_f1": 3.4,
                "macro_precision": 3.4,
                "macro_recall": 3.4,
                "weighted_f1": 3.4,
                "weighted_precision": 3.4,
                "weighted_recall": 3.4,
                "accuracy": 3.4
            },
            "class_metrics": [{
                "label": "label_example",
                "f1": 3.4,
                "precision": 3.4,
                "recall": 3.4,
                "support": 3.4
            }],
            "confusion_matrix": {
                "matrix": {}
            },
            "labels": []
        },
        "test_strategy": {
            "strategy_type": "TEST_AND_VALIDATION_DATASET",
            "testing_dataset": {
                "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
                "dataset_type": "OBJECT_STORAGE",
                "location_details": {
                    "location_type": "OBJECT_LIST",
                    "namespace_name": "namespace_name_example",
                    "bucket_name": "bucket_name_example",
                    "object_names": []
                }
            },
            "validation_dataset": {
                "dataset_id": "ocid1.dataset.oc1..xxxxxxEXAMPLExxxxxx",
                "dataset_type": "OBJECT_STORAGE",
                "location_details": {
                    "location_type": "OBJECT_LIST",
                    "namespace_name": "namespace_name_example",
                    "bucket_name": "bucket_name_example",
                    "object_names": []
                }
            }
        },
        "version": "version_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ai_language import AIServiceLanguageClient
    from oci.ai_language.models import CreateModelDetails
    from oci.ai_language.models import UpdateModelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiLanguageModelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AiLanguageModelHelperGen, self).get_possible_entity_types() + [
            "ailanguagemodelpre",
            "ailanguagemodelpres",
            "aiLanguageailanguagemodelpre",
            "aiLanguageailanguagemodelpres",
            "ailanguagemodelpreresource",
            "ailanguagemodelpresresource",
            "model",
            "models",
            "aiLanguagemodel",
            "aiLanguagemodels",
            "modelresource",
            "modelsresource",
            "ailanguage",
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
        optional_list_method_params = ["model_id", "project_id", "display_name"]

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
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
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
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_model,
            call_fn_args=(),
            call_fn_kwargs=dict(model_id=self.module.params.get("model_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AiLanguageModelHelperCustom = get_custom_class("AiLanguageModelHelperCustom")


class ResourceHelper(AiLanguageModelHelperCustom, AiLanguageModelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            model_details=dict(
                type="dict",
                options=dict(
                    classification_mode=dict(
                        type="dict",
                        options=dict(
                            classification_mode=dict(
                                type="str",
                                required=True,
                                choices=["MULTI_CLASS", "MULTI_LABEL"],
                            ),
                            version=dict(type="str"),
                        ),
                    ),
                    language_code=dict(type="str"),
                    model_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "PRE_TRAINED_KEYPHRASE_EXTRACTION",
                            "PRE_TRAINED_HEALTH_NLU",
                            "PRE_TRAINED_UNIVERSAL",
                            "NAMED_ENTITY_RECOGNITION",
                            "PRE_TRAINED_LANGUAGE_DETECTION",
                            "PRE_TRAINED_NAMED_ENTITY_RECOGNITION",
                            "PRE_TRAINED_SENTIMENT_ANALYSIS",
                            "PRE_TRAINED_PHI",
                            "PRE_TRAINED_TEXT_CLASSIFICATION",
                            "TEXT_CLASSIFICATION",
                            "PRE_TRAINED_SUMMARIZATION",
                            "PRE_TRAINED_PII",
                        ],
                    ),
                    version=dict(type="str"),
                ),
            ),
            training_dataset=dict(
                type="dict",
                options=dict(
                    dataset_id=dict(type="str"),
                    dataset_type=dict(
                        type="str",
                        required=True,
                        choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                    ),
                    location_details=dict(
                        type="dict",
                        options=dict(
                            location_type=dict(
                                type="str", required=True, choices=["OBJECT_LIST"]
                            ),
                            namespace_name=dict(type="str", required=True),
                            bucket_name=dict(type="str", required=True),
                            object_names=dict(
                                type="list", elements="str", required=True
                            ),
                        ),
                    ),
                ),
            ),
            test_strategy=dict(
                type="dict",
                options=dict(
                    strategy_type=dict(
                        type="str",
                        required=True,
                        choices=["TEST_AND_VALIDATION_DATASET"],
                    ),
                    testing_dataset=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            dataset_id=dict(type="str"),
                            dataset_type=dict(
                                type="str",
                                required=True,
                                choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                            ),
                            location_details=dict(
                                type="dict",
                                options=dict(
                                    location_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["OBJECT_LIST"],
                                    ),
                                    namespace_name=dict(type="str", required=True),
                                    bucket_name=dict(type="str", required=True),
                                    object_names=dict(
                                        type="list", elements="str", required=True
                                    ),
                                ),
                            ),
                        ),
                    ),
                    validation_dataset=dict(
                        type="dict",
                        options=dict(
                            dataset_id=dict(type="str"),
                            dataset_type=dict(
                                type="str",
                                required=True,
                                choices=["DATA_SCIENCE_LABELING", "OBJECT_STORAGE"],
                            ),
                            location_details=dict(
                                type="dict",
                                options=dict(
                                    location_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["OBJECT_LIST"],
                                    ),
                                    namespace_name=dict(type="str", required=True),
                                    bucket_name=dict(type="str", required=True),
                                    object_names=dict(
                                        type="list", elements="str", required=True
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            model_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="model",
        service_client_class=AIServiceLanguageClient,
        namespace="ai_language",
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
