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
module: oci_devops_trigger
short_description: Manage a Trigger resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Trigger resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new trigger.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The OCID of the DevOps project to which the trigger belongs to.
            - Required for create using I(state=present).
        type: str
    repository_id:
        description:
            - The OCID of the DevOps code repository.
            - This parameter is updatable.
            - Applicable when trigger_source is 'DEVOPS_CODE_REPOSITORY'
        type: str
    display_name:
        description:
            - Trigger display name. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Optional description about the trigger.
            - This parameter is updatable.
        type: str
    trigger_source:
        description:
            - Source of the trigger. Allowed values are, GITHUB and GITLAB.
            - Required for create using I(state=present), update using I(state=present) with trigger_id present.
        type: str
        choices:
            - "GITHUB"
            - "VBS"
            - "DEVOPS_CODE_REPOSITORY"
            - "BITBUCKET_CLOUD"
            - "GITLAB_SERVER"
            - "GITLAB"
            - "BITBUCKET_SERVER"
    actions:
        description:
            - The list of actions that are to be performed for this trigger.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when trigger_source is one of ['DEVOPS_CODE_REPOSITORY', 'BITBUCKET_SERVER', 'VBS', 'BITBUCKET_CLOUD', 'GITHUB', 'GITLAB_SERVER',
              'GITLAB']
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - The type of action that will be taken. Allowed value is TRIGGER_BUILD_PIPELINE.
                type: str
                choices:
                    - "TRIGGER_BUILD_PIPELINE"
                required: true
            filter:
                description:
                    - ""
                type: dict
                suboptions:
                    trigger_source:
                        description:
                            - Source of the trigger. Allowed values are, GITHUB and GITLAB.
                        type: str
                        choices:
                            - "VBS"
                            - "DEVOPS_CODE_REPOSITORY"
                            - "BITBUCKET_CLOUD"
                            - "BITBUCKET_SERVER"
                            - "GITLAB"
                            - "GITHUB"
                            - "GITLAB_SERVER"
                        required: true
                    events:
                        description:
                            - The events, for example, PUSH, PULL_REQUEST_MERGE.
                        type: list
                        elements: str
                        choices:
                            - "PUSH"
                            - "MERGE_REQUEST_CREATED"
                            - "MERGE_REQUEST_UPDATED"
                            - "MERGE_REQUEST_MERGED"
                            - "PULL_REQUEST_CREATED"
                            - "PULL_REQUEST_UPDATED"
                            - "PULL_REQUEST_MERGED"
                            - "PULL_REQUEST_OPENED"
                            - "PULL_REQUEST_MODIFIED"
                            - "PULL_REQUEST_REOPENED"
                    include:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            repository_name:
                                description:
                                    - The repository name for trigger events.
                                    - Applicable when trigger_source is 'VBS'
                                type: str
                            head_ref:
                                description:
                                    - Branch for push event; source branch for pull requests.
                                type: str
                            base_ref:
                                description:
                                    - The target branch for pull requests; not applicable for push requests.
                                    - Applicable when trigger_source is one of ['BITBUCKET_SERVER', 'VBS', 'BITBUCKET_CLOUD', 'GITHUB', 'GITLAB_SERVER',
                                      'GITLAB']
                                type: str
                            file_filter:
                                description:
                                    - ""
                                    - Applicable when trigger_source is one of ['DEVOPS_CODE_REPOSITORY', 'VBS', 'BITBUCKET_CLOUD', 'GITHUB', 'GITLAB_SERVER',
                                      'GITLAB']
                                type: dict
                                suboptions:
                                    file_paths:
                                        description:
                                            - The file paths/glob pattern for files.
                                            - Applicable when trigger_source is 'VBS'
                                        type: list
                                        elements: str
                    exclude:
                        description:
                            - ""
                            - Applicable when trigger_source is one of ['DEVOPS_CODE_REPOSITORY', 'VBS', 'BITBUCKET_CLOUD', 'GITHUB', 'GITLAB_SERVER', 'GITLAB']
                        type: dict
                        suboptions:
                            file_filter:
                                description:
                                    - ""
                                    - Applicable when trigger_source is one of ['DEVOPS_CODE_REPOSITORY', 'VBS', 'BITBUCKET_CLOUD', 'GITHUB', 'GITLAB_SERVER',
                                      'GITLAB']
                                type: dict
                                suboptions:
                                    file_paths:
                                        description:
                                            - The file paths/glob pattern for files.
                                            - Applicable when trigger_source is 'VBS'
                                        type: list
                                        elements: str
            build_pipeline_id:
                description:
                    - The OCID of the build pipeline to be triggered.
                type: str
                required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    connection_id:
        description:
            - The OCID of the connection resource used to get details for triggered events.
            - This parameter is updatable.
            - Applicable when trigger_source is one of ['VBS', 'BITBUCKET_CLOUD', 'GITHUB', 'GITLAB']
        type: str
    trigger_id:
        description:
            - Unique trigger identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Trigger.
            - Use I(state=present) to create or update a Trigger.
            - Use I(state=absent) to delete a Trigger.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create trigger with trigger_source = GITHUB
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: GITHUB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create trigger with trigger_source = VBS
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: VBS

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create trigger with trigger_source = DEVOPS_CODE_REPOSITORY
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: DEVOPS_CODE_REPOSITORY

    # optional
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create trigger with trigger_source = BITBUCKET_CLOUD
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: BITBUCKET_CLOUD

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create trigger with trigger_source = GITLAB_SERVER
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: GITLAB_SERVER

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create trigger with trigger_source = GITLAB
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: GITLAB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create trigger with trigger_source = BITBUCKET_SERVER
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: BITBUCKET_SERVER

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger with trigger_source = GITHUB
  oci_devops_trigger:
    # required
    trigger_source: GITHUB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger with trigger_source = VBS
  oci_devops_trigger:
    # required
    trigger_source: VBS

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger with trigger_source = DEVOPS_CODE_REPOSITORY
  oci_devops_trigger:
    # required
    trigger_source: DEVOPS_CODE_REPOSITORY

    # optional
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger with trigger_source = BITBUCKET_CLOUD
  oci_devops_trigger:
    # required
    trigger_source: BITBUCKET_CLOUD

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger with trigger_source = GITLAB_SERVER
  oci_devops_trigger:
    # required
    trigger_source: GITLAB_SERVER

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger with trigger_source = GITLAB
  oci_devops_trigger:
    # required
    trigger_source: GITLAB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger with trigger_source = BITBUCKET_SERVER
  oci_devops_trigger:
    # required
    trigger_source: BITBUCKET_SERVER

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = GITHUB
  oci_devops_trigger:
    # required
    trigger_source: GITHUB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = VBS
  oci_devops_trigger:
    # required
    trigger_source: VBS

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = DEVOPS_CODE_REPOSITORY
  oci_devops_trigger:
    # required
    trigger_source: DEVOPS_CODE_REPOSITORY

    # optional
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = BITBUCKET_CLOUD
  oci_devops_trigger:
    # required
    trigger_source: BITBUCKET_CLOUD

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = GITLAB_SERVER
  oci_devops_trigger:
    # required
    trigger_source: GITLAB_SERVER

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = GITLAB
  oci_devops_trigger:
    # required
    trigger_source: GITLAB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = BITBUCKET_SERVER
  oci_devops_trigger:
    # required
    trigger_source: BITBUCKET_SERVER

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: VBS

        # optional
        events: [ "PUSH" ]
        include:
          # optional
          repository_name: repository_name_example
          head_ref: head_ref_example
          base_ref: base_ref_example
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
        exclude:
          # optional
          file_filter:
            # optional
            file_paths: [ "file_paths_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete trigger
  oci_devops_trigger:
    # required
    trigger_id: "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_trigger:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
trigger:
    description:
        - Details of the Trigger resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        repository_id:
            description:
                - The OCID of the DevOps code repository.
            returned: on success
            type: str
            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Trigger display name. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description about the trigger.
            returned: on success
            type: str
            sample: description_example
        project_id:
            description:
                - The OCID of the DevOps project to which the trigger belongs to.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the trigger.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source:
            description:
                - Source of the trigger.
            returned: on success
            type: str
            sample: GITHUB
        time_created:
            description:
                - The time the trigger was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the trigger was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the trigger.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        actions:
            description:
                - The list of actions that are to be performed for this trigger.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of action that will be taken. Allowed value is TRIGGER_BUILD_PIPELINE.
                    returned: on success
                    type: str
                    sample: TRIGGER_BUILD_PIPELINE
                filter:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        trigger_source:
                            description:
                                - Source of the trigger. Allowed values are, GITHUB and GITLAB.
                            returned: on success
                            type: str
                            sample: BITBUCKET_CLOUD
                        events:
                            description:
                                - The events, for example, PUSH, PULL_REQUEST_MERGE.
                            returned: on success
                            type: list
                            sample: []
                        include:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                head_ref:
                                    description:
                                        - Branch for push event; source branch for pull requests.
                                    returned: on success
                                    type: str
                                    sample: head_ref_example
                                base_ref:
                                    description:
                                        - The target branch for pull requests; not applicable for push requests.
                                    returned: on success
                                    type: str
                                    sample: base_ref_example
                                file_filter:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        file_paths:
                                            description:
                                                - The file paths/glob pattern for files.
                                            returned: on success
                                            type: list
                                            sample: []
                                repository_name:
                                    description:
                                        - The repository name for trigger events.
                                    returned: on success
                                    type: str
                                    sample: repository_name_example
                        exclude:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                file_filter:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        file_paths:
                                            description:
                                                - The file paths/glob pattern for files.
                                            returned: on success
                                            type: list
                                            sample: []
                build_pipeline_id:
                    description:
                        - The OCID of the build pipeline to be triggered.
                    returned: on success
                    type: str
                    sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        trigger_url:
            description:
                - The endpoint that listens to trigger events.
            returned: on success
            type: str
            sample: trigger_url_example
        connection_id:
            description:
                - The OCID of the connection resource used to get details for triggered events.
            returned: on success
            type: str
            sample: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "trigger_source": "GITHUB",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "actions": [{
            "type": "TRIGGER_BUILD_PIPELINE",
            "filter": {
                "trigger_source": "BITBUCKET_CLOUD",
                "events": [],
                "include": {
                    "head_ref": "head_ref_example",
                    "base_ref": "base_ref_example",
                    "file_filter": {
                        "file_paths": []
                    },
                    "repository_name": "repository_name_example"
                },
                "exclude": {
                    "file_filter": {
                        "file_paths": []
                    }
                }
            },
            "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "trigger_url": "trigger_url_example",
        "connection_id": "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.devops import DevopsClient
    from oci.devops.models import CreateTriggerDetails
    from oci.devops.models import UpdateTriggerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TriggerHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TriggerHelperGen, self).get_possible_entity_types() + [
            "trigger",
            "triggers",
            "devopstrigger",
            "devopstriggers",
            "triggerresource",
            "triggersresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "trigger_id"

    def get_module_resource_id(self):
        return self.module.params.get("trigger_id")

    def get_get_fn(self):
        return self.client.get_trigger

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_trigger, trigger_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_trigger, trigger_id=self.module.params.get("trigger_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

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
        return oci_common_utils.list_all_resources(self.client.list_triggers, **kwargs)

    def get_create_model_class(self):
        return CreateTriggerDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(create_trigger_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateTriggerDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(
                trigger_id=self.module.params.get("trigger_id"),
                update_trigger_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(trigger_id=self.module.params.get("trigger_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


TriggerHelperCustom = get_custom_class("TriggerHelperCustom")


class ResourceHelper(TriggerHelperCustom, TriggerHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            repository_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            trigger_source=dict(
                type="str",
                choices=[
                    "GITHUB",
                    "VBS",
                    "DEVOPS_CODE_REPOSITORY",
                    "BITBUCKET_CLOUD",
                    "GITLAB_SERVER",
                    "GITLAB",
                    "BITBUCKET_SERVER",
                ],
            ),
            actions=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(
                        type="str", required=True, choices=["TRIGGER_BUILD_PIPELINE"]
                    ),
                    filter=dict(
                        type="dict",
                        options=dict(
                            trigger_source=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "VBS",
                                    "DEVOPS_CODE_REPOSITORY",
                                    "BITBUCKET_CLOUD",
                                    "BITBUCKET_SERVER",
                                    "GITLAB",
                                    "GITHUB",
                                    "GITLAB_SERVER",
                                ],
                            ),
                            events=dict(
                                type="list",
                                elements="str",
                                choices=[
                                    "PUSH",
                                    "MERGE_REQUEST_CREATED",
                                    "MERGE_REQUEST_UPDATED",
                                    "MERGE_REQUEST_MERGED",
                                    "PULL_REQUEST_CREATED",
                                    "PULL_REQUEST_UPDATED",
                                    "PULL_REQUEST_MERGED",
                                    "PULL_REQUEST_OPENED",
                                    "PULL_REQUEST_MODIFIED",
                                    "PULL_REQUEST_REOPENED",
                                ],
                            ),
                            include=dict(
                                type="dict",
                                options=dict(
                                    repository_name=dict(type="str"),
                                    head_ref=dict(type="str"),
                                    base_ref=dict(type="str"),
                                    file_filter=dict(
                                        type="dict",
                                        options=dict(
                                            file_paths=dict(type="list", elements="str")
                                        ),
                                    ),
                                ),
                            ),
                            exclude=dict(
                                type="dict",
                                options=dict(
                                    file_filter=dict(
                                        type="dict",
                                        options=dict(
                                            file_paths=dict(type="list", elements="str")
                                        ),
                                    )
                                ),
                            ),
                        ),
                    ),
                    build_pipeline_id=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            connection_id=dict(type="str"),
            trigger_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="trigger",
        service_client_class=DevopsClient,
        namespace="devops",
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
