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
module: oci_golden_gate_deployment_version_facts
short_description: Fetches details about one or multiple DeploymentVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DeploymentVersion resources in Oracle Cloud Infrastructure
    - Returns the list of available deployment versions.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that contains the work request. Work requests should be scoped
              to the same compartment as the resource the work request affects. If the work request concerns
              multiple resources, and those resources are not in the same compartment, it is up to the service team
              to pick the primary resource whose compartment should be used.
        type: str
        required: true
    deployment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment in which to list resources.
        type: str
    deployment_type:
        description:
            - The type of deployment, the value determines the exact 'type' of the service executed in the deployment. Default value is DATABASE_ORACLE.
        type: str
        choices:
            - "OGG"
            - "DATABASE_ORACLE"
            - "BIGDATA"
            - "DATABASE_MICROSOFT_SQLSERVER"
            - "DATABASE_MYSQL"
            - "DATABASE_POSTGRESQL"
            - "DATABASE_DB2ZOS"
            - "GGSA"
            - "DATA_TRANSFORMS"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is
              descending.  Default order for 'displayName' is ascending. If no value is specified
              timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List deployment_versions
  oci_golden_gate_deployment_version_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_type: OGG
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
deployment_versions:
    description:
        - List of DeploymentVersion resources
    returned: on success
    type: complex
    contains:
        ogg_version:
            description:
                - Version of OGG
            returned: on success
            type: str
            sample: ogg_version_example
        deployment_type:
            description:
                - "The type of deployment, which can be any one of the Allowed values.
                  NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
                      Its use is discouraged in favor of 'DATABASE_ORACLE'."
            returned: on success
            type: str
            sample: OGG
        time_released:
            description:
                - The time the resource was released. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        release_type:
            description:
                - The type of release.
            returned: on success
            type: str
            sample: MAJOR
        is_security_fix:
            description:
                - Indicates if OGG release contains security fix.
            returned: on success
            type: bool
            sample: true
        time_supported_until:
            description:
                - The time until OGG version is supported. After this date has passed OGG version will not be available anymore. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "ogg_version": "ogg_version_example",
        "deployment_type": "OGG",
        "time_released": "2013-10-20T19:20:30+01:00",
        "release_type": "MAJOR",
        "is_security_fix": true,
        "time_supported_until": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.golden_gate import GoldenGateClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "deployment_id",
            "deployment_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_deployment_versions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DeploymentVersionFactsHelperCustom = get_custom_class(
    "DeploymentVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    DeploymentVersionFactsHelperCustom, DeploymentVersionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            deployment_id=dict(type="str"),
            deployment_type=dict(
                type="str",
                choices=[
                    "OGG",
                    "DATABASE_ORACLE",
                    "BIGDATA",
                    "DATABASE_MICROSOFT_SQLSERVER",
                    "DATABASE_MYSQL",
                    "DATABASE_POSTGRESQL",
                    "DATABASE_DB2ZOS",
                    "GGSA",
                    "DATA_TRANSFORMS",
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
        resource_type="deployment_version",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(deployment_versions=result)


if __name__ == "__main__":
    main()
