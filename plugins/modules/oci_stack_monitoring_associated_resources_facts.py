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
module: oci_stack_monitoring_associated_resources_facts
short_description: Fetches details about one or multiple AssociatedResources resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AssociatedResources resources in Oracle Cloud Infrastructure
    - List associated monitored resources.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
        type: str
        required: true
    resource_type:
        description:
            - A filter to return associated resources that match resources of type.
              Either resourceId or resourceType should be provided.
        type: str
    resource_id:
        description:
            - Monitored resource identifier for which the associated resources should be fetched.
              Either resourceId or resourceType should be provided.
        type: str
    limit_level:
        description:
            - "The field which determines the depth of hierarchy while searching for associated resources.
              Possible values - 0 for all levels. And positive number to indicate different levels.
              Default value is 1, which indicates 1st level associations."
        type: int
    association_types:
        description:
            - List of association types to be searched for finding associated resources
        type: list
        elements: str
    fields:
        description:
            - "Partial response refers to an optimization technique offered
              by the RESTful web APIs, to return only the information
              (fields) required by the client. In this mechanism, the client
              sends the required field names as the query parameters for
              an API to the server, and the server trims down the default
              response content by removing the fields that are not required
              by the client. The parameter controls which fields to
              return and should be a query string parameter called \\"fields\\" of
              an array type, provide the values as enums, and use collectionFormat."
        type: list
        elements: str
    exclude_fields:
        description:
            - "Partial response refers to an optimization technique offered
              by the RESTful web APIs, to return all the information except
              the fields requested to be excluded (excludeFields) by the client.
              In this mechanism, the client
              sends the exclude field names as the query parameters for
              an API to the server, and the server trims down the default
              response content by removing the fields that are not required
              by the client. The parameter controls which fields to
              exlude and to return and should be a query string parameter
              called \\"excludeFields\\" of an array type, provide the values
              as enums, and use collectionFormat."
        type: list
        elements: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List associated_resources
  oci_stack_monitoring_associated_resources_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    resource_type: resource_type_example
    resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    limit_level: 56
    association_types: [ "association_types_example" ]
    fields: [ "fields_example" ]
    exclude_fields: [ "exclude_fields_example" ]

"""

RETURN = """
associated_resources:
    description:
        - List of AssociatedResources resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of monitored resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Name of the monitored resource
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Monitored resource display name.
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - Type of the monitored resource
            returned: on success
            type: str
            sample: type_example
        host_name:
            description:
                - Resource Host Name
            returned: on success
            type: str
            sample: host_name_example
        external_id:
            description:
                - "External resource is any OCI resource identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
                  which is not a Stack Monitoring service resource.
                  Currently supports only following resource type identifiers - externalcontainerdatabase,
                  externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance."
            returned: on success
            type: str
            sample: "ocid1.external.oc1..xxxxxxEXAMPLExxxxxx"
        management_agent_id:
            description:
                - Management Agent Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the monitored resource.
            returned: on success
            type: str
            sample: CREATING
        associated_resources:
            description:
                - List of associated monitored resources
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of monitored resource.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - Name of the monitored resource
                    returned: on success
                    type: str
                    sample: name_example
                display_name:
                    description:
                        - Monitored resource display name.
                    returned: on success
                    type: str
                    sample: display_name_example
                type:
                    description:
                        - Type of the monitored resource
                    returned: on success
                    type: str
                    sample: type_example
                host_name:
                    description:
                        - Resource Host Name
                    returned: on success
                    type: str
                    sample: host_name_example
                external_id:
                    description:
                        - "External resource is any OCI resource identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
                          which is not a Stack Monitoring service resource.
                          Currently supports only following resource type identifiers - externalcontainerdatabase,
                          externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance."
                    returned: on success
                    type: str
                    sample: "ocid1.external.oc1..xxxxxxEXAMPLExxxxxx"
                management_agent_id:
                    description:
                        - Management Agent Identifier L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    returned: on success
                    type: str
                    sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
                lifecycle_state:
                    description:
                        - The current state of the monitored resource.
                    returned: on success
                    type: str
                    sample: CREATING
                association:
                    description:
                        - Association details of the resource
                    returned: on success
                    type: dict
                    sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "display_name": "display_name_example",
        "type": "type_example",
        "host_name": "host_name_example",
        "external_id": "ocid1.external.oc1..xxxxxxEXAMPLExxxxxx",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "associated_resources": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "display_name": "display_name_example",
            "type": "type_example",
            "host_name": "host_name_example",
            "external_id": "ocid1.external.oc1..xxxxxxEXAMPLExxxxxx",
            "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
            "lifecycle_state": "CREATING",
            "association": {}
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.stack_monitoring import StackMonitoringClient
    from oci.stack_monitoring.models import SearchAssociatedResourcesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssociatedResourcesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "fields",
            "exclude_fields",
            "name",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.search_associated_resources,
            search_associated_resources_details=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, SearchAssociatedResourcesDetails
            ),
            **optional_kwargs
        )


AssociatedResourcesFactsHelperCustom = get_custom_class(
    "AssociatedResourcesFactsHelperCustom"
)


class ResourceFactsHelper(
    AssociatedResourcesFactsHelperCustom, AssociatedResourcesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            resource_type=dict(type="str"),
            resource_id=dict(type="str"),
            limit_level=dict(type="int"),
            association_types=dict(type="list", elements="str"),
            fields=dict(type="list", elements="str"),
            exclude_fields=dict(type="list", elements="str"),
            name=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="associated_resources",
        service_client_class=StackMonitoringClient,
        namespace="stack_monitoring",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(associated_resources=result)


if __name__ == "__main__":
    main()
