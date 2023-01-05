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
module: oci_data_science_notebook_session_facts
short_description: Fetches details about one or multiple NotebookSession resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NotebookSession resources in Oracle Cloud Infrastructure
    - Lists the notebook sessions in the specified compartment.
    - If I(notebook_session_id) is specified, the details of a single NotebookSession will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    notebook_session_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the notebook session.
            - Required to get a specific notebook_session.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple notebook_sessions.
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
            - "DELETED"
            - "FAILED"
            - "INACTIVE"
            - "UPDATING"
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
              By default, when you sort by `timeCreated`, the results are shown
              in descending order. When you sort by `displayName`, results are
              shown in ascending order. Sort order for the `displayName` field is case sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific notebook_session
  oci_data_science_notebook_session_facts:
    # required
    notebook_session_id: "ocid1.notebooksession.oc1..xxxxxxEXAMPLExxxxxx"

- name: List notebook_sessions
  oci_data_science_notebook_session_facts:
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
notebook_sessions:
    description:
        - List of NotebookSession resources
    returned: on success
    type: complex
    contains:
        notebook_session_runtime_config_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                custom_environment_variables:
                    description:
                        - Custom environment variables for Notebook Session. These key-value pairs will be available for customers in Notebook Sessions.
                    returned: on success
                    type: dict
                    sample: {}
                notebook_session_git_config_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        notebook_session_git_repo_config_collection:
                            description:
                                - A collection of Git repository configurations.
                            returned: on success
                            type: complex
                            contains:
                                url:
                                    description:
                                        - The repository URL
                                    returned: on success
                                    type: str
                                    sample: url_example
        lifecycle_details:
            description:
                - Details about the state of the notebook session.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the notebook session.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2019-08-25T21:10:29.41Z"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - "A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
                  Example: `My NotebookSession`"
            returned: on success
            type: str
            sample: display_name_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project associated with the notebook session.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the notebook session.
            returned: on success
            type: str
            sample: created_by_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the notebook session's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        notebook_session_configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - The shape used to launch the notebook session compute instance.  The list of available shapes in a given compartment can be retrieved
                          using the `ListNotebookSessionShapes` endpoint.
                    returned: on success
                    type: str
                    sample: shape_example
                block_storage_size_in_gbs:
                    description:
                        - A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.
                    returned: on success
                    type: int
                    sample: 56
                subnet_id:
                    description:
                        - A notebook session instance is provided with a VNIC for network access.  This specifies the
                          L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create a VNIC in.  The subnet
                          should be in a VCN with a NAT gateway for egress to the internet.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                notebook_session_shape_config_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - The total number of OCPUs available to the notebook session instance.
                            returned: on success
                            type: float
                            sample: 3.4
                        memory_in_gbs:
                            description:
                                - The total amount of memory available to the notebook session instance, in gigabytes.
                            returned: on success
                            type: float
                            sample: 3.4
        notebook_session_config_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - The shape used to launch the notebook session compute instance.  The list of available shapes in a given compartment can be retrieved
                          using the `ListNotebookSessionShapes` endpoint.
                    returned: on success
                    type: str
                    sample: shape_example
                block_storage_size_in_gbs:
                    description:
                        - A notebook session instance is provided with a block storage volume. This specifies the size of the volume in GBs.
                    returned: on success
                    type: int
                    sample: 56
                subnet_id:
                    description:
                        - A notebook session instance is provided with a VNIC for network access.  This specifies the
                          L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet to create a VNIC in.  The subnet
                          should be in a VCN with a NAT gateway for egress to the internet.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                notebook_session_shape_config_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - The total number of OCPUs available to the notebook session instance.
                            returned: on success
                            type: float
                            sample: 3.4
                        memory_in_gbs:
                            description:
                                - The total amount of memory available to the notebook session instance, in gigabytes.
                            returned: on success
                            type: float
                            sample: 3.4
        notebook_session_url:
            description:
                - The URL to interact with the notebook session.
            returned: on success
            type: str
            sample: notebook_session_url_example
        lifecycle_state:
            description:
                - The state of the notebook session.
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
        "notebook_session_runtime_config_details": {
            "custom_environment_variables": {},
            "notebook_session_git_config_details": {
                "notebook_session_git_repo_config_collection": [{
                    "url": "url_example"
                }]
            }
        },
        "lifecycle_details": "lifecycle_details_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "created_by": "created_by_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "notebook_session_configuration_details": {
            "shape": "shape_example",
            "block_storage_size_in_gbs": 56,
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "notebook_session_shape_config_details": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            }
        },
        "notebook_session_config_details": {
            "shape": "shape_example",
            "block_storage_size_in_gbs": 56,
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "notebook_session_shape_config_details": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            }
        },
        "notebook_session_url": "notebook_session_url_example",
        "lifecycle_state": "CREATING",
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
    from oci.data_science import DataScienceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataScienceNotebookSessionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "notebook_session_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_notebook_session,
            notebook_session_id=self.module.params.get("notebook_session_id"),
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
            self.client.list_notebook_sessions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataScienceNotebookSessionFactsHelperCustom = get_custom_class(
    "DataScienceNotebookSessionFactsHelperCustom"
)


class ResourceFactsHelper(
    DataScienceNotebookSessionFactsHelperCustom,
    DataScienceNotebookSessionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            notebook_session_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "INACTIVE",
                    "UPDATING",
                ],
            ),
            created_by=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="notebook_session",
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

    module.exit_json(notebook_sessions=result)


if __name__ == "__main__":
    main()
