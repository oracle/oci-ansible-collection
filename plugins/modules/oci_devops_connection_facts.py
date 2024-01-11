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
module: oci_devops_connection_facts
short_description: Fetches details about one or multiple Connection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Connection resources in Oracle Cloud Infrastructure
    - Returns a list of connections.
    - If I(connection_id) is specified, the details of a single Connection will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_id:
        description:
            - Unique connection identifier.
            - Required to get a specific connection.
        type: str
        aliases: ["id"]
    project_id:
        description:
            - unique project identifier
        type: str
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only connections that matches the given lifecycle state.
        type: str
        choices:
            - "ACTIVE"
            - "DELETING"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    connection_type:
        description:
            - A filter to return only resources that match the given connection type.
        type: str
        choices:
            - "GITHUB_ACCESS_TOKEN"
            - "GITLAB_ACCESS_TOKEN"
            - "GITLAB_SERVER_ACCESS_TOKEN"
            - "BITBUCKET_SERVER_ACCESS_TOKEN"
            - "BITBUCKET_CLOUD_APP_PASSWORD"
            - "VBS_ACCESS_TOKEN"
    sort_order:
        description:
            - The sort order to use. Use either ascending or descending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is
              ascending. If no value is specified, then the default time created value is considered.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific connection
  oci_devops_connection_facts:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

- name: List connections
  oci_devops_connection_facts:

    # optional
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    display_name: display_name_example
    connection_type: GITHUB_ACCESS_TOKEN
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
connections:
    description:
        - List of Connection resources
    returned: on success
    type: complex
    contains:
        username:
            description:
                - Public Bitbucket Cloud Username in plain text
                - Returned for get operation
            returned: on success
            type: str
            sample: username_example
        app_password:
            description:
                - OCID of personal Bitbucket Cloud AppPassword saved in secret store
                - Returned for get operation
            returned: on success
            type: str
            sample: example-password
        tls_verify_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                tls_verify_mode:
                    description:
                        - The type of TLS verification.
                    returned: on success
                    type: str
                    sample: CA_CERTIFICATE_VERIFY
                ca_certificate_bundle_id:
                    description:
                        - The OCID of OCI certificate service CA bundle.
                    returned: on success
                    type: str
                    sample: "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"
        access_token:
            description:
                - The OCID of personal access token saved in secret store.
                - Returned for get operation
            returned: on success
            type: str
            sample: access_token_example
        base_url:
            description:
                - The Base URL of the hosted BitbucketServer.
                - Returned for get operation
            returned: on success
            type: str
            sample: base_url_example
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Connection display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Optional description about the connection.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment containing the connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The OCID of the DevOps project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        connection_type:
            description:
                - The type of connection.
            returned: on success
            type: str
            sample: GITHUB_ACCESS_TOKEN
        time_created:
            description:
                - The time the connection was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the connection was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        last_connection_validation_result:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                result:
                    description:
                        - The latest result of whether the credentials pass the validation.
                    returned: on success
                    type: str
                    sample: PASS
                time_validated:
                    description:
                        - The latest timestamp when the connection was validated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                message:
                    description:
                        - A message describing the result of connection validation in more detail.
                    returned: on success
                    type: str
                    sample: message_example
        lifecycle_details:
            description:
                - A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the connection.
            returned: on success
            type: str
            sample: ACTIVE
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
    sample: [{
        "username": "username_example",
        "app_password": "example-password",
        "tls_verify_config": {
            "tls_verify_mode": "CA_CERTIFICATE_VERIFY",
            "ca_certificate_bundle_id": "ocid1.cacertificatebundle.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "access_token": "access_token_example",
        "base_url": "base_url_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_type": "GITHUB_ACCESS_TOKEN",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "last_connection_validation_result": {
            "result": "PASS",
            "time_validated": "2013-10-20T19:20:30+01:00",
            "message": "message_example"
        },
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "connection_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_id=self.module.params.get("connection_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "project_id",
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "connection_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_connections, **optional_kwargs
        )


DevopsConnectionFactsHelperCustom = get_custom_class(
    "DevopsConnectionFactsHelperCustom"
)


class ResourceFactsHelper(
    DevopsConnectionFactsHelperCustom, DevopsConnectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            connection_id=dict(aliases=["id"], type="str"),
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETING"]),
            display_name=dict(aliases=["name"], type="str"),
            connection_type=dict(
                type="str",
                choices=[
                    "GITHUB_ACCESS_TOKEN",
                    "GITLAB_ACCESS_TOKEN",
                    "GITLAB_SERVER_ACCESS_TOKEN",
                    "BITBUCKET_SERVER_ACCESS_TOKEN",
                    "BITBUCKET_CLOUD_APP_PASSWORD",
                    "VBS_ACCESS_TOKEN",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="connection",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(connections=result)


if __name__ == "__main__":
    main()
