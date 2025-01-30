#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_ai_document_analyze_document_result_actions
short_description: Perform actions on an AnalyzeDocumentResult resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AnalyzeDocumentResult resource in Oracle Cloud Infrastructure
    - For I(action=analyze_document), perform different types of document analysis.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    features:
        description:
            - The types of document analysis requested.
        type: list
        elements: dict
        required: true
        suboptions:
            model_id:
                description:
                    - The custom model ID.
                    - Applicable when feature_type is one of ['KEY_VALUE_EXTRACTION', 'DOCUMENT_CLASSIFICATION']
                type: str
            tenancy_id:
                description:
                    - The custom model tenancy ID when modelId represents aliasName.
                    - Applicable when feature_type is one of ['KEY_VALUE_EXTRACTION', 'DOCUMENT_CLASSIFICATION']
                type: str
            max_results:
                description:
                    - The maximum number of results to return.
                    - Applicable when feature_type is one of ['DOCUMENT_CLASSIFICATION', 'LANGUAGE_CLASSIFICATION']
                type: int
            generate_searchable_pdf:
                description:
                    - Whether or not to generate a searchable PDF file.
                    - Applicable when feature_type is 'TEXT_EXTRACTION'
                type: bool
            feature_type:
                description:
                    - "The type of document analysis requested.
                      The allowed values are:
                      - `LANGUAGE_CLASSIFICATION`: Detect the language.
                      - `TEXT_EXTRACTION`: Recognize text.
                      - `TABLE_EXTRACTION`: Detect and extract data in tables.
                      - `KEY_VALUE_EXTRACTION`: Extract form fields.
                      - `DOCUMENT_CLASSIFICATION`: Identify the type of document."
                type: str
                choices:
                    - "DOCUMENT_CLASSIFICATION"
                    - "KEY_VALUE_EXTRACTION"
                    - "LANGUAGE_CLASSIFICATION"
                    - "TEXT_EXTRACTION"
                    - "TABLE_EXTRACTION"
                required: true
    document:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            namespace_name:
                description:
                    - The Object Storage namespace.
                    - Required when source is 'OBJECT_STORAGE'
                type: str
            bucket_name:
                description:
                    - The Object Storage bucket name.
                    - Required when source is 'OBJECT_STORAGE'
                type: str
            object_name:
                description:
                    - The Object Storage object name.
                    - Required when source is 'OBJECT_STORAGE'
                type: str
            source:
                description:
                    - "The location of the document data.
                      The allowed values are:
                      - `INLINE`: The data is included directly in the request payload.
                      - `OBJECT_STORAGE`: The document is in OCI Object Storage."
                type: str
                choices:
                    - "OBJECT_STORAGE"
                    - "INLINE"
                required: true
            data:
                description:
                    - Raw document data with Base64 encoding.
                    - Required when source is 'INLINE'
                type: str
    compartment_id:
        description:
            - The compartment identifier.
        type: str
    output_location:
        description:
            - ""
        type: dict
        suboptions:
            namespace_name:
                description:
                    - The Object Storage namespace.
                type: str
                required: true
            bucket_name:
                description:
                    - The Object Storage bucket name.
                type: str
                required: true
            prefix:
                description:
                    - The Object Storage folder name.
                type: str
                required: true
    language:
        description:
            - The document language, abbreviated according to the BCP 47 syntax.
        type: str
    document_type:
        description:
            - The document type.
        type: str
        choices:
            - "INVOICE"
            - "RECEIPT"
            - "RESUME"
            - "TAX_FORM"
            - "DRIVER_LICENSE"
            - "PASSPORT"
            - "BANK_STATEMENT"
            - "CHECK"
            - "PAYSLIP"
            - "OTHERS"
    ocr_data:
        description:
            - ""
        type: dict
        suboptions:
            document_metadata:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    page_count:
                        description:
                            - Teh number of pages in the document.
                        type: int
                        required: true
                    mime_type:
                        description:
                            - The result data format.
                        type: str
                        required: true
            pages:
                description:
                    - The array of a Page.
                type: list
                elements: dict
                required: true
                suboptions:
                    page_number:
                        description:
                            - The document page number.
                        type: int
                        required: true
                    dimensions:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            width:
                                description:
                                    - the width of a page.
                                type: float
                                required: true
                            height:
                                description:
                                    - The height of a page.
                                type: float
                                required: true
                            unit:
                                description:
                                    - The unit of length.
                                type: str
                                choices:
                                    - "PIXEL"
                                    - "INCH"
                                required: true
                    detected_document_types:
                        description:
                            - An array of detected document types.
                        type: list
                        elements: dict
                        suboptions:
                            document_type:
                                description:
                                    - The document type.
                                type: str
                                required: true
                            document_id:
                                description:
                                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Key-Value Extraction model
                                      that was used to extract the key-value pairs.
                                type: str
                            confidence:
                                description:
                                    - The confidence score between 0 and 1.
                                type: float
                                required: true
                    detected_languages:
                        description:
                            - An array of detected languages.
                        type: list
                        elements: dict
                        suboptions:
                            language:
                                description:
                                    - The document language, abbreviated according to the BCP 47 syntax.
                                type: str
                                required: true
                            confidence:
                                description:
                                    - The confidence score between 0 and 1.
                                type: float
                                required: true
                    words:
                        description:
                            - The words detected on the page.
                        type: list
                        elements: dict
                        suboptions:
                            text:
                                description:
                                    - The string of text characters in the word.
                                type: str
                                required: true
                            confidence:
                                description:
                                    - the confidence score between 0 and 1.
                                type: float
                                required: true
                            bounding_polygon:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    normalized_vertices:
                                        description:
                                            - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent
                                              points and between the first and last point.
                                              Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0},
                                              {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                        type: list
                                        elements: dict
                                        required: true
                                        suboptions:
                                            x:
                                                description:
                                                    - The X-axis normalized coordinate.
                                                type: float
                                                required: true
                                            y:
                                                description:
                                                    - The Y-axis normalized coordinate.
                                                type: float
                                                required: true
                    lines:
                        description:
                            - The lines of text detected on the page.
                        type: list
                        elements: dict
                        suboptions:
                            text:
                                description:
                                    - The text recognized.
                                type: str
                                required: true
                            confidence:
                                description:
                                    - The confidence score between 0 and 1.
                                type: float
                                required: true
                            bounding_polygon:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    normalized_vertices:
                                        description:
                                            - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent
                                              points and between the first and last point.
                                              Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0},
                                              {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                        type: list
                                        elements: dict
                                        required: true
                                        suboptions:
                                            x:
                                                description:
                                                    - The X-axis normalized coordinate.
                                                type: float
                                                required: true
                                            y:
                                                description:
                                                    - The Y-axis normalized coordinate.
                                                type: float
                                                required: true
                            word_indexes:
                                description:
                                    - The array of words.
                                type: list
                                elements: int
                                required: true
                    tables:
                        description:
                            - The tables detected on the page.
                        type: list
                        elements: dict
                        suboptions:
                            row_count:
                                description:
                                    - The number of rows.
                                type: int
                                required: true
                            column_count:
                                description:
                                    - The number of columns.
                                type: int
                                required: true
                            header_rows:
                                description:
                                    - The header rows.
                                type: list
                                elements: dict
                                required: true
                                suboptions:
                                    cells:
                                        description:
                                            - The cells in the row.
                                        type: list
                                        elements: dict
                                        required: true
                                        suboptions:
                                            text:
                                                description:
                                                    - The text recognized in the cell.
                                                type: str
                                                required: true
                                            row_index:
                                                description:
                                                    - The index of the cell inside the row.
                                                type: int
                                                required: true
                                            column_index:
                                                description:
                                                    - The index of the cell inside the column.
                                                type: int
                                                required: true
                                            confidence:
                                                description:
                                                    - The confidence score between 0 and 1.
                                                type: float
                                                required: true
                                            bounding_polygon:
                                                description:
                                                    - ""
                                                type: dict
                                                required: true
                                                suboptions:
                                                    normalized_vertices:
                                                        description:
                                                            - "An array of normalized points defining the polygon's perimeter, with an implicit segment between
                                                              subsequent points and between the first and last point.
                                                              Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1,
                                                              \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of
                                                              an image."
                                                        type: list
                                                        elements: dict
                                                        required: true
                                                        suboptions:
                                                            x:
                                                                description:
                                                                    - The X-axis normalized coordinate.
                                                                type: float
                                                                required: true
                                                            y:
                                                                description:
                                                                    - The Y-axis normalized coordinate.
                                                                type: float
                                                                required: true
                                            word_indexes:
                                                description:
                                                    - The words detected in the cell.
                                                type: list
                                                elements: int
                                                required: true
                            body_rows:
                                description:
                                    - The body rows.
                                type: list
                                elements: dict
                                required: true
                                suboptions:
                                    cells:
                                        description:
                                            - The cells in the row.
                                        type: list
                                        elements: dict
                                        required: true
                                        suboptions:
                                            text:
                                                description:
                                                    - The text recognized in the cell.
                                                type: str
                                                required: true
                                            row_index:
                                                description:
                                                    - The index of the cell inside the row.
                                                type: int
                                                required: true
                                            column_index:
                                                description:
                                                    - The index of the cell inside the column.
                                                type: int
                                                required: true
                                            confidence:
                                                description:
                                                    - The confidence score between 0 and 1.
                                                type: float
                                                required: true
                                            bounding_polygon:
                                                description:
                                                    - ""
                                                type: dict
                                                required: true
                                                suboptions:
                                                    normalized_vertices:
                                                        description:
                                                            - "An array of normalized points defining the polygon's perimeter, with an implicit segment between
                                                              subsequent points and between the first and last point.
                                                              Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1,
                                                              \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of
                                                              an image."
                                                        type: list
                                                        elements: dict
                                                        required: true
                                                        suboptions:
                                                            x:
                                                                description:
                                                                    - The X-axis normalized coordinate.
                                                                type: float
                                                                required: true
                                                            y:
                                                                description:
                                                                    - The Y-axis normalized coordinate.
                                                                type: float
                                                                required: true
                                            word_indexes:
                                                description:
                                                    - The words detected in the cell.
                                                type: list
                                                elements: int
                                                required: true
                            footer_rows:
                                description:
                                    - the footer rows.
                                type: list
                                elements: dict
                                required: true
                                suboptions:
                                    cells:
                                        description:
                                            - The cells in the row.
                                        type: list
                                        elements: dict
                                        required: true
                                        suboptions:
                                            text:
                                                description:
                                                    - The text recognized in the cell.
                                                type: str
                                                required: true
                                            row_index:
                                                description:
                                                    - The index of the cell inside the row.
                                                type: int
                                                required: true
                                            column_index:
                                                description:
                                                    - The index of the cell inside the column.
                                                type: int
                                                required: true
                                            confidence:
                                                description:
                                                    - The confidence score between 0 and 1.
                                                type: float
                                                required: true
                                            bounding_polygon:
                                                description:
                                                    - ""
                                                type: dict
                                                required: true
                                                suboptions:
                                                    normalized_vertices:
                                                        description:
                                                            - "An array of normalized points defining the polygon's perimeter, with an implicit segment between
                                                              subsequent points and between the first and last point.
                                                              Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1,
                                                              \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of
                                                              an image."
                                                        type: list
                                                        elements: dict
                                                        required: true
                                                        suboptions:
                                                            x:
                                                                description:
                                                                    - The X-axis normalized coordinate.
                                                                type: float
                                                                required: true
                                                            y:
                                                                description:
                                                                    - The Y-axis normalized coordinate.
                                                                type: float
                                                                required: true
                                            word_indexes:
                                                description:
                                                    - The words detected in the cell.
                                                type: list
                                                elements: int
                                                required: true
                            confidence:
                                description:
                                    - The confidence score between 0 and 1.
                                type: float
                                required: true
                            bounding_polygon:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    normalized_vertices:
                                        description:
                                            - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent
                                              points and between the first and last point.
                                              Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0},
                                              {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                        type: list
                                        elements: dict
                                        required: true
                                        suboptions:
                                            x:
                                                description:
                                                    - The X-axis normalized coordinate.
                                                type: float
                                                required: true
                                            y:
                                                description:
                                                    - The Y-axis normalized coordinate.
                                                type: float
                                                required: true
                    document_fields:
                        description:
                            - The form fields detected on the page.
                        type: list
                        elements: dict
                        suboptions:
                            field_type:
                                description:
                                    - The field type.
                                type: str
                                choices:
                                    - "LINE_ITEM_GROUP"
                                    - "LINE_ITEM"
                                    - "LINE_ITEM_FIELD"
                                    - "KEY_VALUE"
                                required: true
                            field_label:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    name:
                                        description:
                                            - The name of the field label.
                                        type: str
                                        required: true
                                    confidence:
                                        description:
                                            - The confidence score between 0 and 1.
                                        type: float
                            field_name:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    name:
                                        description:
                                            - The name of the field.
                                        type: str
                                        required: true
                                    confidence:
                                        description:
                                            - The confidence score between 0 and 1.
                                        type: float
                                    bounding_polygon:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            normalized_vertices:
                                                description:
                                                    - "An array of normalized points defining the polygon's perimeter, with an implicit segment between
                                                      subsequent points and between the first and last point.
                                                      Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\":
                                                      0}, {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    x:
                                                        description:
                                                            - The X-axis normalized coordinate.
                                                        type: float
                                                        required: true
                                                    y:
                                                        description:
                                                            - The Y-axis normalized coordinate.
                                                        type: float
                                                        required: true
                                    word_indexes:
                                        description:
                                            - The indexes of the words in the field name.
                                        type: list
                                        elements: int
                            field_value:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    value:
                                        description:
                                            - The time field value as yyyy-mm-dd hh-mm-ss.
                                            - Required when value_type is one of ['DATE', 'NUMBER', 'STRING', 'TIME', 'PHONE_NUMBER', 'INTEGER']
                                        type: str
                                    value_type:
                                        description:
                                            - The type of data detected.
                                        type: str
                                        choices:
                                            - "TIME"
                                            - "INTEGER"
                                            - "DATE"
                                            - "NUMBER"
                                            - "STRING"
                                            - "PHONE_NUMBER"
                                            - "ARRAY"
                                        required: true
                                    text:
                                        description:
                                            - The detected text of a field.
                                        type: str
                                    confidence:
                                        description:
                                            - The confidence score between 0 and 1.
                                        type: float
                                        required: true
                                    bounding_polygon:
                                        description:
                                            - ""
                                        type: dict
                                        required: true
                                        suboptions:
                                            normalized_vertices:
                                                description:
                                                    - "An array of normalized points defining the polygon's perimeter, with an implicit segment between
                                                      subsequent points and between the first and last point.
                                                      Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\":
                                                      0}, {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                                    - Required when value_type is 'TIME'
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    x:
                                                        description:
                                                            - The X-axis normalized coordinate.
                                                            - Required when value_type is 'TIME'
                                                        type: float
                                                        required: true
                                                    y:
                                                        description:
                                                            - The Y-axis normalized coordinate.
                                                            - Required when value_type is 'TIME'
                                                        type: float
                                                        required: true
                                    word_indexes:
                                        description:
                                            - The indexes of the words in the field value.
                                        type: list
                                        elements: int
                                        required: true
                                    items:
                                        description:
                                            - The array of values.
                                            - Required when value_type is 'ARRAY'
                                        type: list
                                        elements: dict
                                        suboptions:
                                            field_type:
                                                description:
                                                    - The field type.
                                                type: str
                                                choices:
                                                    - "LINE_ITEM_GROUP"
                                                    - "LINE_ITEM"
                                                    - "LINE_ITEM_FIELD"
                                                    - "KEY_VALUE"
                                                required: true
                                            field_label:
                                                description:
                                                    - ""
                                                type: dict
                                            field_name:
                                                description:
                                                    - ""
                                                type: dict
                                            field_value:
                                                description:
                                                    - ""
                                                type: dict
                                                required: true
            detected_document_types:
                description:
                    - An array of detected document types.
                type: list
                elements: dict
                suboptions:
                    document_type:
                        description:
                            - The document type.
                        type: str
                        required: true
                    document_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Key-Value Extraction model that was
                              used to extract the key-value pairs.
                        type: str
                    confidence:
                        description:
                            - The confidence score between 0 and 1.
                        type: float
                        required: true
            detected_languages:
                description:
                    - An array of detected languages.
                type: list
                elements: dict
                suboptions:
                    language:
                        description:
                            - The document language, abbreviated according to the BCP 47 syntax.
                        type: str
                        required: true
                    confidence:
                        description:
                            - The confidence score between 0 and 1.
                        type: float
                        required: true
            document_classification_model_version:
                description:
                    - The document classification model version.
                type: str
            language_classification_model_version:
                description:
                    - The document language classification model version.
                type: str
            text_extraction_model_version:
                description:
                    - The document text extraction model version.
                type: str
            key_value_extraction_model_version:
                description:
                    - The document keyValue extraction model version.
                type: str
            table_extraction_model_version:
                description:
                    - The document table extraction model version.
                type: str
            errors:
                description:
                    - The errors encountered during document analysis.
                type: list
                elements: dict
                suboptions:
                    code:
                        description:
                            - The error code.
                        type: str
                        required: true
                    message:
                        description:
                            - The error message.
                        type: str
                        required: true
            searchable_pdf:
                description:
                    - The searchable PDF file that was generated.
                type: str
    action:
        description:
            - The action to perform on the AnalyzeDocumentResult.
        type: str
        required: true
        choices:
            - "analyze_document"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action analyze_document on analyze_document_result
  oci_ai_document_analyze_document_result_actions:
    # required
    features:
    - # required
      feature_type: DOCUMENT_CLASSIFICATION

      # optional
      model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
      tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
      max_results: 56
    document:
      # required
      namespace_name: namespace_name_example
      bucket_name: bucket_name_example
      object_name: object_name_example
      source: OBJECT_STORAGE
    action: analyze_document

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    output_location:
      # required
      namespace_name: namespace_name_example
      bucket_name: bucket_name_example
      prefix: prefix_example
    language: language_example
    document_type: INVOICE
    ocr_data:
      # required
      document_metadata:
        # required
        page_count: 56
        mime_type: mime_type_example
      pages:
      - # required
        page_number: 56

        # optional
        dimensions:
          # required
          width: 3.4
          height: 3.4
          unit: PIXEL
        detected_document_types:
        - # required
          document_type: document_type_example
          confidence: 3.4

          # optional
          document_id: "ocid1.document.oc1..xxxxxxEXAMPLExxxxxx"
        detected_languages:
        - # required
          language: language_example
          confidence: 3.4
        words:
        - # required
          text: text_example
          confidence: 3.4
          bounding_polygon:
            # required
            normalized_vertices:
            - # required
              x: 3.4
              y: 3.4
        lines:
        - # required
          text: text_example
          confidence: 3.4
          bounding_polygon:
            # required
            normalized_vertices:
            - # required
              x: 3.4
              y: 3.4
          word_indexes: [ "word_indexes_example" ]
        tables:
        - # required
          row_count: 56
          column_count: 56
          header_rows:
          - # required
            cells:
            - # required
              text: text_example
              row_index: 56
              column_index: 56
              confidence: 3.4
              bounding_polygon:
                # required
                normalized_vertices:
                - # required
                  x: 3.4
                  y: 3.4
              word_indexes: [ "word_indexes_example" ]
          body_rows:
          - # required
            cells:
            - # required
              text: text_example
              row_index: 56
              column_index: 56
              confidence: 3.4
              bounding_polygon:
                # required
                normalized_vertices:
                - # required
                  x: 3.4
                  y: 3.4
              word_indexes: [ "word_indexes_example" ]
          footer_rows:
          - # required
            cells:
            - # required
              text: text_example
              row_index: 56
              column_index: 56
              confidence: 3.4
              bounding_polygon:
                # required
                normalized_vertices:
                - # required
                  x: 3.4
                  y: 3.4
              word_indexes: [ "word_indexes_example" ]
          confidence: 3.4
          bounding_polygon:
            # required
            normalized_vertices:
            - # required
              x: 3.4
              y: 3.4
        document_fields:
        - # required
          field_type: LINE_ITEM_GROUP
          field_value:
            # required
            value: value_example
            value_type: TIME
            confidence: 3.4
            bounding_polygon:
              # required
              normalized_vertices:
              - # required
                x: 3.4
                y: 3.4
            word_indexes: [ "word_indexes_example" ]

                # optional
            text: text_example

          # optional
          field_label:
            # required
            name: name_example

            # optional
            confidence: 3.4
          field_name:
            # required
            name: name_example

            # optional
            confidence: 3.4
            bounding_polygon:
              # required
              normalized_vertices:
              - # required
                x: 3.4
                y: 3.4
            word_indexes: [ "word_indexes_example" ]

                # optional
      detected_document_types:
      - # required
        document_type: document_type_example
        confidence: 3.4

        # optional
        document_id: "ocid1.document.oc1..xxxxxxEXAMPLExxxxxx"
      detected_languages:
      - # required
        language: language_example
        confidence: 3.4
      document_classification_model_version: document_classification_model_version_example
      language_classification_model_version: language_classification_model_version_example
      text_extraction_model_version: text_extraction_model_version_example
      key_value_extraction_model_version: key_value_extraction_model_version_example
      table_extraction_model_version: table_extraction_model_version_example
      errors:
      - # required
        code: code_example
        message: message_example
      searchable_pdf: searchable_pdf_example

"""

RETURN = """
analyze_document_result:
    description:
        - Details of the AnalyzeDocumentResult resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        document_metadata:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                page_count:
                    description:
                        - Teh number of pages in the document.
                    returned: on success
                    type: int
                    sample: 56
                mime_type:
                    description:
                        - The result data format.
                    returned: on success
                    type: str
                    sample: mime_type_example
        pages:
            description:
                - The array of a Page.
            returned: on success
            type: complex
            contains:
                page_number:
                    description:
                        - The document page number.
                    returned: on success
                    type: int
                    sample: 56
                dimensions:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        width:
                            description:
                                - the width of a page.
                            returned: on success
                            type: float
                            sample: 1.2
                        height:
                            description:
                                - The height of a page.
                            returned: on success
                            type: float
                            sample: 1.2
                        unit:
                            description:
                                - The unit of length.
                            returned: on success
                            type: str
                            sample: PIXEL
                detected_document_types:
                    description:
                        - An array of detected document types.
                    returned: on success
                    type: complex
                    contains:
                        document_type:
                            description:
                                - The document type.
                            returned: on success
                            type: str
                            sample: document_type_example
                        document_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Key-Value Extraction model that
                                  was used to extract the key-value pairs.
                            returned: on success
                            type: str
                            sample: "ocid1.document.oc1..xxxxxxEXAMPLExxxxxx"
                        confidence:
                            description:
                                - The confidence score between 0 and 1.
                            returned: on success
                            type: float
                            sample: 3.4
                detected_languages:
                    description:
                        - An array of detected languages.
                    returned: on success
                    type: complex
                    contains:
                        language:
                            description:
                                - The document language, abbreviated according to the BCP 47 syntax.
                            returned: on success
                            type: str
                            sample: language_example
                        confidence:
                            description:
                                - The confidence score between 0 and 1.
                            returned: on success
                            type: float
                            sample: 3.4
                words:
                    description:
                        - The words detected on the page.
                    returned: on success
                    type: complex
                    contains:
                        text:
                            description:
                                - The string of text characters in the word.
                            returned: on success
                            type: str
                            sample: text_example
                        confidence:
                            description:
                                - the confidence score between 0 and 1.
                            returned: on success
                            type: float
                            sample: 3.4
                        bounding_polygon:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                normalized_vertices:
                                    description:
                                        - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent points
                                          and between the first and last point.
                                          Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0}, {\\"x\\":
                                          1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                    returned: on success
                                    type: complex
                                    contains:
                                        x:
                                            description:
                                                - The X-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                                        y:
                                            description:
                                                - The Y-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                lines:
                    description:
                        - The lines of text detected on the page.
                    returned: on success
                    type: complex
                    contains:
                        text:
                            description:
                                - The text recognized.
                            returned: on success
                            type: str
                            sample: text_example
                        confidence:
                            description:
                                - The confidence score between 0 and 1.
                            returned: on success
                            type: float
                            sample: 3.4
                        bounding_polygon:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                normalized_vertices:
                                    description:
                                        - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent points
                                          and between the first and last point.
                                          Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0}, {\\"x\\":
                                          1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                    returned: on success
                                    type: complex
                                    contains:
                                        x:
                                            description:
                                                - The X-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                                        y:
                                            description:
                                                - The Y-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                        word_indexes:
                            description:
                                - The array of words.
                            returned: on success
                            type: list
                            sample: []
                tables:
                    description:
                        - The tables detected on the page.
                    returned: on success
                    type: complex
                    contains:
                        row_count:
                            description:
                                - The number of rows.
                            returned: on success
                            type: int
                            sample: 56
                        column_count:
                            description:
                                - The number of columns.
                            returned: on success
                            type: int
                            sample: 56
                        header_rows:
                            description:
                                - The header rows.
                            returned: on success
                            type: complex
                            contains:
                                cells:
                                    description:
                                        - The cells in the row.
                                    returned: on success
                                    type: complex
                                    contains:
                                        text:
                                            description:
                                                - The text recognized in the cell.
                                            returned: on success
                                            type: str
                                            sample: text_example
                                        row_index:
                                            description:
                                                - The index of the cell inside the row.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        column_index:
                                            description:
                                                - The index of the cell inside the column.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        confidence:
                                            description:
                                                - The confidence score between 0 and 1.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                                        bounding_polygon:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                normalized_vertices:
                                                    description:
                                                        - "An array of normalized points defining the polygon's perimeter, with an implicit segment between
                                                          subsequent points and between the first and last point.
                                                          Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1,
                                                          \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an
                                                          image."
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        x:
                                                            description:
                                                                - The X-axis normalized coordinate.
                                                            returned: on success
                                                            type: float
                                                            sample: 1.2
                                                        y:
                                                            description:
                                                                - The Y-axis normalized coordinate.
                                                            returned: on success
                                                            type: float
                                                            sample: 1.2
                                        word_indexes:
                                            description:
                                                - The words detected in the cell.
                                            returned: on success
                                            type: list
                                            sample: []
                        body_rows:
                            description:
                                - The body rows.
                            returned: on success
                            type: complex
                            contains:
                                cells:
                                    description:
                                        - The cells in the row.
                                    returned: on success
                                    type: complex
                                    contains:
                                        text:
                                            description:
                                                - The text recognized in the cell.
                                            returned: on success
                                            type: str
                                            sample: text_example
                                        row_index:
                                            description:
                                                - The index of the cell inside the row.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        column_index:
                                            description:
                                                - The index of the cell inside the column.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        confidence:
                                            description:
                                                - The confidence score between 0 and 1.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                                        bounding_polygon:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                normalized_vertices:
                                                    description:
                                                        - "An array of normalized points defining the polygon's perimeter, with an implicit segment between
                                                          subsequent points and between the first and last point.
                                                          Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1,
                                                          \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an
                                                          image."
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        x:
                                                            description:
                                                                - The X-axis normalized coordinate.
                                                            returned: on success
                                                            type: float
                                                            sample: 1.2
                                                        y:
                                                            description:
                                                                - The Y-axis normalized coordinate.
                                                            returned: on success
                                                            type: float
                                                            sample: 1.2
                                        word_indexes:
                                            description:
                                                - The words detected in the cell.
                                            returned: on success
                                            type: list
                                            sample: []
                        footer_rows:
                            description:
                                - the footer rows.
                            returned: on success
                            type: complex
                            contains:
                                cells:
                                    description:
                                        - The cells in the row.
                                    returned: on success
                                    type: complex
                                    contains:
                                        text:
                                            description:
                                                - The text recognized in the cell.
                                            returned: on success
                                            type: str
                                            sample: text_example
                                        row_index:
                                            description:
                                                - The index of the cell inside the row.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        column_index:
                                            description:
                                                - The index of the cell inside the column.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        confidence:
                                            description:
                                                - The confidence score between 0 and 1.
                                            returned: on success
                                            type: float
                                            sample: 3.4
                                        bounding_polygon:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                normalized_vertices:
                                                    description:
                                                        - "An array of normalized points defining the polygon's perimeter, with an implicit segment between
                                                          subsequent points and between the first and last point.
                                                          Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1,
                                                          \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an
                                                          image."
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        x:
                                                            description:
                                                                - The X-axis normalized coordinate.
                                                            returned: on success
                                                            type: float
                                                            sample: 1.2
                                                        y:
                                                            description:
                                                                - The Y-axis normalized coordinate.
                                                            returned: on success
                                                            type: float
                                                            sample: 1.2
                                        word_indexes:
                                            description:
                                                - The words detected in the cell.
                                            returned: on success
                                            type: list
                                            sample: []
                        confidence:
                            description:
                                - The confidence score between 0 and 1.
                            returned: on success
                            type: float
                            sample: 3.4
                        bounding_polygon:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                normalized_vertices:
                                    description:
                                        - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent points
                                          and between the first and last point.
                                          Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0}, {\\"x\\":
                                          1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                    returned: on success
                                    type: complex
                                    contains:
                                        x:
                                            description:
                                                - The X-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                                        y:
                                            description:
                                                - The Y-axis normalized coordinate.
                                            returned: on success
                                            type: float
                                            sample: 1.2
                document_fields:
                    description:
                        - The form fields detected on the page.
                    returned: on success
                    type: complex
                    contains:
                        field_type:
                            description:
                                - The field type.
                            returned: on success
                            type: str
                            sample: LINE_ITEM_GROUP
                        field_label:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the field label.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                confidence:
                                    description:
                                        - The confidence score between 0 and 1.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                        field_name:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the field.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                confidence:
                                    description:
                                        - The confidence score between 0 and 1.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                bounding_polygon:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        normalized_vertices:
                                            description:
                                                - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent
                                                  points and between the first and last point.
                                                  Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0},
                                                  {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                            returned: on success
                                            type: complex
                                            contains:
                                                x:
                                                    description:
                                                        - The X-axis normalized coordinate.
                                                    returned: on success
                                                    type: float
                                                    sample: 1.2
                                                y:
                                                    description:
                                                        - The Y-axis normalized coordinate.
                                                    returned: on success
                                                    type: float
                                                    sample: 1.2
                                word_indexes:
                                    description:
                                        - The indexes of the words in the field name.
                                    returned: on success
                                    type: list
                                    sample: []
                        field_value:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - The array of values.
                                    returned: on success
                                    type: complex
                                    contains:
                                        field_type:
                                            description:
                                                - The field type.
                                            returned: on success
                                            type: str
                                            sample: LINE_ITEM_GROUP
                                        field_label:
                                            description:
                                                - ""
                                            returned: on success
                                            type: FieldLabel
                                            sample: "null"

                                        field_name:
                                            description:
                                                - ""
                                            returned: on success
                                            type: FieldName
                                            sample: "null"

                                        field_value:
                                            description:
                                                - ""
                                            returned: on success
                                            type: FieldValue
                                            sample: "null"

                                value_type:
                                    description:
                                        - The type of data detected.
                                    returned: on success
                                    type: str
                                    sample: STRING
                                text:
                                    description:
                                        - The detected text of a field.
                                    returned: on success
                                    type: str
                                    sample: text_example
                                confidence:
                                    description:
                                        - The confidence score between 0 and 1.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                bounding_polygon:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        normalized_vertices:
                                            description:
                                                - "An array of normalized points defining the polygon's perimeter, with an implicit segment between subsequent
                                                  points and between the first and last point.
                                                  Rectangles are defined with four points. For example, `[{\\"x\\": 0, \\"y\\": 0}, {\\"x\\": 1, \\"y\\": 0},
                                                  {\\"x\\": 1, \\"y\\": 0.5}, {\\"x\\": 0, \\"y\\": 0.5}]` represents the top half of an image."
                                            returned: on success
                                            type: complex
                                            contains:
                                                x:
                                                    description:
                                                        - The X-axis normalized coordinate.
                                                    returned: on success
                                                    type: float
                                                    sample: 1.2
                                                y:
                                                    description:
                                                        - The Y-axis normalized coordinate.
                                                    returned: on success
                                                    type: float
                                                    sample: 1.2
                                word_indexes:
                                    description:
                                        - The indexes of the words in the field value.
                                    returned: on success
                                    type: list
                                    sample: []
                                value:
                                    description:
                                        - The date field value as yyyy-mm-dd.
                                    returned: on success
                                    type: str
                                    sample: "2013-10-20T19:20:30+01:00"
        detected_document_types:
            description:
                - An array of detected document types.
            returned: on success
            type: complex
            contains:
                document_type:
                    description:
                        - The document type.
                    returned: on success
                    type: str
                    sample: document_type_example
                document_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Key-Value Extraction model that was
                          used to extract the key-value pairs.
                    returned: on success
                    type: str
                    sample: "ocid1.document.oc1..xxxxxxEXAMPLExxxxxx"
                confidence:
                    description:
                        - The confidence score between 0 and 1.
                    returned: on success
                    type: float
                    sample: 3.4
        detected_languages:
            description:
                - An array of detected languages.
            returned: on success
            type: complex
            contains:
                language:
                    description:
                        - The document language, abbreviated according to the BCP 47 syntax.
                    returned: on success
                    type: str
                    sample: language_example
                confidence:
                    description:
                        - The confidence score between 0 and 1.
                    returned: on success
                    type: float
                    sample: 3.4
        document_classification_model_version:
            description:
                - The document classification model version.
            returned: on success
            type: str
            sample: document_classification_model_version_example
        language_classification_model_version:
            description:
                - The document language classification model version.
            returned: on success
            type: str
            sample: language_classification_model_version_example
        text_extraction_model_version:
            description:
                - The document text extraction model version.
            returned: on success
            type: str
            sample: text_extraction_model_version_example
        key_value_extraction_model_version:
            description:
                - The document keyValue extraction model version.
            returned: on success
            type: str
            sample: key_value_extraction_model_version_example
        table_extraction_model_version:
            description:
                - The document table extraction model version.
            returned: on success
            type: str
            sample: table_extraction_model_version_example
        errors:
            description:
                - The errors encountered during document analysis.
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - The error code.
                    returned: on success
                    type: str
                    sample: code_example
                message:
                    description:
                        - The error message.
                    returned: on success
                    type: str
                    sample: message_example
        searchable_pdf:
            description:
                - The searchable PDF file that was generated.
            returned: on success
            type: str
            sample: "null"

    sample: {
        "document_metadata": {
            "page_count": 56,
            "mime_type": "mime_type_example"
        },
        "pages": [{
            "page_number": 56,
            "dimensions": {
                "width": 1.2,
                "height": 1.2,
                "unit": "PIXEL"
            },
            "detected_document_types": [{
                "document_type": "document_type_example",
                "document_id": "ocid1.document.oc1..xxxxxxEXAMPLExxxxxx",
                "confidence": 3.4
            }],
            "detected_languages": [{
                "language": "language_example",
                "confidence": 3.4
            }],
            "words": [{
                "text": "text_example",
                "confidence": 3.4,
                "bounding_polygon": {
                    "normalized_vertices": [{
                        "x": 1.2,
                        "y": 1.2
                    }]
                }
            }],
            "lines": [{
                "text": "text_example",
                "confidence": 3.4,
                "bounding_polygon": {
                    "normalized_vertices": [{
                        "x": 1.2,
                        "y": 1.2
                    }]
                },
                "word_indexes": []
            }],
            "tables": [{
                "row_count": 56,
                "column_count": 56,
                "header_rows": [{
                    "cells": [{
                        "text": "text_example",
                        "row_index": 56,
                        "column_index": 56,
                        "confidence": 3.4,
                        "bounding_polygon": {
                            "normalized_vertices": [{
                                "x": 1.2,
                                "y": 1.2
                            }]
                        },
                        "word_indexes": []
                    }]
                }],
                "body_rows": [{
                    "cells": [{
                        "text": "text_example",
                        "row_index": 56,
                        "column_index": 56,
                        "confidence": 3.4,
                        "bounding_polygon": {
                            "normalized_vertices": [{
                                "x": 1.2,
                                "y": 1.2
                            }]
                        },
                        "word_indexes": []
                    }]
                }],
                "footer_rows": [{
                    "cells": [{
                        "text": "text_example",
                        "row_index": 56,
                        "column_index": 56,
                        "confidence": 3.4,
                        "bounding_polygon": {
                            "normalized_vertices": [{
                                "x": 1.2,
                                "y": 1.2
                            }]
                        },
                        "word_indexes": []
                    }]
                }],
                "confidence": 3.4,
                "bounding_polygon": {
                    "normalized_vertices": [{
                        "x": 1.2,
                        "y": 1.2
                    }]
                }
            }],
            "document_fields": [{
                "field_type": "LINE_ITEM_GROUP",
                "field_label": {
                    "name": "name_example",
                    "confidence": 3.4
                },
                "field_name": {
                    "name": "name_example",
                    "confidence": 3.4,
                    "bounding_polygon": {
                        "normalized_vertices": [{
                            "x": 1.2,
                            "y": 1.2
                        }]
                    },
                    "word_indexes": []
                },
                "field_value": {
                    "items": [{
                        "field_type": "LINE_ITEM_GROUP",
                        "field_label": null,
                        "field_name": null,
                        "field_value": null
                    }],
                    "value_type": "STRING",
                    "text": "text_example",
                    "confidence": 3.4,
                    "bounding_polygon": {
                        "normalized_vertices": [{
                            "x": 1.2,
                            "y": 1.2
                        }]
                    },
                    "word_indexes": [],
                    "value": "2013-10-20T19:20:30+01:00"
                }
            }]
        }],
        "detected_document_types": [{
            "document_type": "document_type_example",
            "document_id": "ocid1.document.oc1..xxxxxxEXAMPLExxxxxx",
            "confidence": 3.4
        }],
        "detected_languages": [{
            "language": "language_example",
            "confidence": 3.4
        }],
        "document_classification_model_version": "document_classification_model_version_example",
        "language_classification_model_version": "language_classification_model_version_example",
        "text_extraction_model_version": "text_extraction_model_version_example",
        "key_value_extraction_model_version": "key_value_extraction_model_version_example",
        "table_extraction_model_version": "table_extraction_model_version_example",
        "errors": [{
            "code": "code_example",
            "message": "message_example"
        }],
        "searchable_pdf": null
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
    from oci.ai_document import AIServiceDocumentClient
    from oci.ai_document.models import AnalyzeDocumentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AiDocumentAnalyzeDocumentResultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        analyze_document
    """

    def analyze_document(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AnalyzeDocumentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.analyze_document,
            call_fn_args=(),
            call_fn_kwargs=dict(analyze_document_details=action_details,),
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


AiDocumentAnalyzeDocumentResultActionsHelperCustom = get_custom_class(
    "AiDocumentAnalyzeDocumentResultActionsHelperCustom"
)


class ResourceHelper(
    AiDocumentAnalyzeDocumentResultActionsHelperCustom,
    AiDocumentAnalyzeDocumentResultActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            features=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    model_id=dict(type="str"),
                    tenancy_id=dict(type="str"),
                    max_results=dict(type="int"),
                    generate_searchable_pdf=dict(type="bool"),
                    feature_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "DOCUMENT_CLASSIFICATION",
                            "KEY_VALUE_EXTRACTION",
                            "LANGUAGE_CLASSIFICATION",
                            "TEXT_EXTRACTION",
                            "TABLE_EXTRACTION",
                        ],
                    ),
                ),
            ),
            document=dict(
                type="dict",
                required=True,
                options=dict(
                    namespace_name=dict(type="str"),
                    bucket_name=dict(type="str"),
                    object_name=dict(type="str"),
                    source=dict(
                        type="str", required=True, choices=["OBJECT_STORAGE", "INLINE"]
                    ),
                    data=dict(type="str"),
                ),
            ),
            compartment_id=dict(type="str"),
            output_location=dict(
                type="dict",
                options=dict(
                    namespace_name=dict(type="str", required=True),
                    bucket_name=dict(type="str", required=True),
                    prefix=dict(type="str", required=True),
                ),
            ),
            language=dict(type="str"),
            document_type=dict(
                type="str",
                choices=[
                    "INVOICE",
                    "RECEIPT",
                    "RESUME",
                    "TAX_FORM",
                    "DRIVER_LICENSE",
                    "PASSPORT",
                    "BANK_STATEMENT",
                    "CHECK",
                    "PAYSLIP",
                    "OTHERS",
                ],
            ),
            ocr_data=dict(
                type="dict",
                options=dict(
                    document_metadata=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            page_count=dict(type="int", required=True),
                            mime_type=dict(type="str", required=True),
                        ),
                    ),
                    pages=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            page_number=dict(type="int", required=True),
                            dimensions=dict(
                                type="dict",
                                options=dict(
                                    width=dict(type="float", required=True),
                                    height=dict(type="float", required=True),
                                    unit=dict(
                                        type="str",
                                        required=True,
                                        choices=["PIXEL", "INCH"],
                                    ),
                                ),
                            ),
                            detected_document_types=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    document_type=dict(type="str", required=True),
                                    document_id=dict(type="str"),
                                    confidence=dict(type="float", required=True),
                                ),
                            ),
                            detected_languages=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    language=dict(type="str", required=True),
                                    confidence=dict(type="float", required=True),
                                ),
                            ),
                            words=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    text=dict(type="str", required=True),
                                    confidence=dict(type="float", required=True),
                                    bounding_polygon=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            normalized_vertices=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    x=dict(type="float", required=True),
                                                    y=dict(type="float", required=True),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            ),
                            lines=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    text=dict(type="str", required=True),
                                    confidence=dict(type="float", required=True),
                                    bounding_polygon=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            normalized_vertices=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    x=dict(type="float", required=True),
                                                    y=dict(type="float", required=True),
                                                ),
                                            )
                                        ),
                                    ),
                                    word_indexes=dict(
                                        type="list", elements="int", required=True
                                    ),
                                ),
                            ),
                            tables=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    row_count=dict(type="int", required=True),
                                    column_count=dict(type="int", required=True),
                                    header_rows=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            cells=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    text=dict(
                                                        type="str", required=True
                                                    ),
                                                    row_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    column_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    confidence=dict(
                                                        type="float", required=True
                                                    ),
                                                    bounding_polygon=dict(
                                                        type="dict",
                                                        required=True,
                                                        options=dict(
                                                            normalized_vertices=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    x=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                    y=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    word_indexes=dict(
                                                        type="list",
                                                        elements="int",
                                                        required=True,
                                                    ),
                                                ),
                                            )
                                        ),
                                    ),
                                    body_rows=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            cells=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    text=dict(
                                                        type="str", required=True
                                                    ),
                                                    row_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    column_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    confidence=dict(
                                                        type="float", required=True
                                                    ),
                                                    bounding_polygon=dict(
                                                        type="dict",
                                                        required=True,
                                                        options=dict(
                                                            normalized_vertices=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    x=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                    y=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    word_indexes=dict(
                                                        type="list",
                                                        elements="int",
                                                        required=True,
                                                    ),
                                                ),
                                            )
                                        ),
                                    ),
                                    footer_rows=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            cells=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    text=dict(
                                                        type="str", required=True
                                                    ),
                                                    row_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    column_index=dict(
                                                        type="int", required=True
                                                    ),
                                                    confidence=dict(
                                                        type="float", required=True
                                                    ),
                                                    bounding_polygon=dict(
                                                        type="dict",
                                                        required=True,
                                                        options=dict(
                                                            normalized_vertices=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    x=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                    y=dict(
                                                                        type="float",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    word_indexes=dict(
                                                        type="list",
                                                        elements="int",
                                                        required=True,
                                                    ),
                                                ),
                                            )
                                        ),
                                    ),
                                    confidence=dict(type="float", required=True),
                                    bounding_polygon=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            normalized_vertices=dict(
                                                type="list",
                                                elements="dict",
                                                required=True,
                                                options=dict(
                                                    x=dict(type="float", required=True),
                                                    y=dict(type="float", required=True),
                                                ),
                                            )
                                        ),
                                    ),
                                ),
                            ),
                            document_fields=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    field_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "LINE_ITEM_GROUP",
                                            "LINE_ITEM",
                                            "LINE_ITEM_FIELD",
                                            "KEY_VALUE",
                                        ],
                                    ),
                                    field_label=dict(
                                        type="dict",
                                        options=dict(
                                            name=dict(type="str", required=True),
                                            confidence=dict(type="float"),
                                        ),
                                    ),
                                    field_name=dict(
                                        type="dict",
                                        options=dict(
                                            name=dict(type="str", required=True),
                                            confidence=dict(type="float"),
                                            bounding_polygon=dict(
                                                type="dict",
                                                options=dict(
                                                    normalized_vertices=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            x=dict(
                                                                type="float",
                                                                required=True,
                                                            ),
                                                            y=dict(
                                                                type="float",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            word_indexes=dict(
                                                type="list", elements="int"
                                            ),
                                        ),
                                    ),
                                    field_value=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            value=dict(type="str"),
                                            value_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "TIME",
                                                    "INTEGER",
                                                    "DATE",
                                                    "NUMBER",
                                                    "STRING",
                                                    "PHONE_NUMBER",
                                                    "ARRAY",
                                                ],
                                            ),
                                            text=dict(type="str"),
                                            confidence=dict(
                                                type="float", required=True
                                            ),
                                            bounding_polygon=dict(
                                                type="dict",
                                                required=True,
                                                options=dict(
                                                    normalized_vertices=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            x=dict(
                                                                type="float",
                                                                required=True,
                                                            ),
                                                            y=dict(
                                                                type="float",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            word_indexes=dict(
                                                type="list",
                                                elements="int",
                                                required=True,
                                            ),
                                            items=dict(
                                                type="list",
                                                elements="dict",
                                                options=dict(
                                                    field_type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "LINE_ITEM_GROUP",
                                                            "LINE_ITEM",
                                                            "LINE_ITEM_FIELD",
                                                            "KEY_VALUE",
                                                        ],
                                                    ),
                                                    field_label=dict(type="FieldLabel"),
                                                    field_name=dict(type="FieldName"),
                                                    field_value=dict(
                                                        type="FieldValue", required=True
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    detected_document_types=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            document_type=dict(type="str", required=True),
                            document_id=dict(type="str"),
                            confidence=dict(type="float", required=True),
                        ),
                    ),
                    detected_languages=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            language=dict(type="str", required=True),
                            confidence=dict(type="float", required=True),
                        ),
                    ),
                    document_classification_model_version=dict(type="str"),
                    language_classification_model_version=dict(type="str"),
                    text_extraction_model_version=dict(type="str"),
                    key_value_extraction_model_version=dict(type="str", no_log=True),
                    table_extraction_model_version=dict(type="str"),
                    errors=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            code=dict(type="str", required=True),
                            message=dict(type="str", required=True),
                        ),
                    ),
                    searchable_pdf=dict(type="str"),
                ),
            ),
            action=dict(type="str", required=True, choices=["analyze_document"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="analyze_document_result",
        service_client_class=AIServiceDocumentClient,
        namespace="ai_document",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
