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
module: oci_oda_package_facts
short_description: Fetches details about one or multiple Package resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Package resources in Oracle Cloud Infrastructure
    - Returns a page of summaries for packages that are available for import. The optional odaInstanceId query
      parameter can be used to filter packages that are available for import by a specific instance. If odaInstanceId
      query parameter is not provided, the returned list will
      include packages available within the region indicated by the request URL. The optional resourceType query
      param may be specified to filter packages that contain the indicated resource type. If no resourceType query
      param is given, packages containing all resource types will be returned. The optional name query parameter can
      be used to limit the list to packages whose name matches the given name. The optional displayName query
      parameter can be used to limit the list to packages whose displayName matches the given name. The optional
      isLatestVersionOnly query parameter can be used to limit the returned list to include only the latest version
      of any given package. If not specified, all versions of any otherwise matching package will be returned.
    - If the `opc-next-page` header appears in the response, then
      there are more items to retrieve. To get the next page in the subsequent
      GET request, include the header's value as the `page` query parameter.
    - If I(package_id) is specified, the details of a single Package will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    package_id:
        description:
            - Unique Digital Assistant package identifier.
            - Required to get a specific package.
        type: str
        aliases: ["id"]
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
            - Required to get a specific package.
        type: str
    resource_type:
        description:
            - Resource type identifier. Used to limit query results to the items which are applicable to the given type.
        type: str
    name:
        description:
            - List only the information for the package with this name. Package names are unique to a publisher and may not change.
            - "Example: `My Package`"
        type: str
    display_name:
        description:
            - List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change.
            - "Example: `My new resource`"
        type: str
    is_latest_skill_only:
        description:
            - Should we return only the latest version of a package (instead of all versions)?
        type: bool
    sort_order:
        description:
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`.
            - The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific package
  oci_oda_package_facts:
    # required
    package_id: "ocid1.package.oc1..xxxxxxEXAMPLExxxxxx"
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List packages
  oci_oda_package_facts:

    # optional
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    resource_type: resource_type_example
    name: name_example
    display_name: display_name_example
    is_latest_skill_only: true
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
packages:
    description:
        - List of Package resources
    returned: on success
    type: complex
    contains:
        time_uploaded:
            description:
                - When the package was uploaded. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        import_contract:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                import_contract:
                    description:
                        - A list of resource type specific import contracts, one for each resource type listed in the package definition.
                    returned: on success
                    type: complex
                    contains:
                        resource_type:
                            description:
                                - The type of resource to which this resourceType-specific contract applies
                            returned: on success
                            type: str
                            sample: resource_type_example
                        parameters:
                            description:
                                - A list of definitions for parameters that are required to import this package into a target instance.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the parameter
                                    returned: on success
                                    type: str
                                    sample: name_example
                                type:
                                    description:
                                        - Enumerated parameter type.
                                    returned: on success
                                    type: str
                                    sample: STRING
                                description:
                                    description:
                                        - Description of the parameter.
                                    returned: on success
                                    type: str
                                    sample: description_example
                                is_required:
                                    description:
                                        - Is this parameter required. Ignored for parameters with direction = OUTPUT.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_sensitive:
                                    description:
                                        - Is the data for this parameter sensitive (e.g. should the data be hidden in UI, encrypted if stored, etc.)
                                    returned: on success
                                    type: bool
                                    sample: true
                                default_value:
                                    description:
                                        - Default value for the parameter.
                                    returned: on success
                                    type: str
                                    sample: default_value_example
                                min_length:
                                    description:
                                        - Used for character string types such as STRING to constrain the length of the value
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_length:
                                    description:
                                        - Used for character string types such as STRING to constrain the length of the value
                                    returned: on success
                                    type: int
                                    sample: 56
                                pattern:
                                    description:
                                        - Regular expression used to validate the value of a string type such as STRING
                                    returned: on success
                                    type: str
                                    sample: pattern_example
                                direction:
                                    description:
                                        - Is this parameter an input parameter, output parameter, or both?
                                    returned: on success
                                    type: str
                                    sample: INPUT
                                ui_placement_hint:
                                    description:
                                        - A forward-slash-delimited 'path' in an imaginary hierarchy, at which this parameter's UI widgets should be placed
                                    returned: on success
                                    type: str
                                    sample: ui_placement_hint_example
                                resource_type_metadata:
                                    description:
                                        - Any configuration needed to help the resource type process this parameter (e.g. link to manifest, etc.).
                                    returned: on success
                                    type: dict
                                    sample: {}
        default_parameter_values:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                resource_types_default_parameter_values:
                    description:
                        - A list of resource type specific default parameter values, one set for each resource type listed in the package definition.
                    returned: on success
                    type: complex
                    contains:
                        resource_type:
                            description:
                                - The type of resource to which these resourceType-specific parameter values apply
                            returned: on success
                            type: str
                            sample: resource_type_example
                        parameter_values:
                            description:
                                - A list of parameter values used to import the package.
                            returned: on success
                            type: dict
                            sample: {}
        id:
            description:
                - Unique immutable identifier that was assigned when the Package was registered.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        publisher_id:
            description:
                - ID of the publisher providing the package.
            returned: on success
            type: str
            sample: "ocid1.publisher.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Name of package.
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Display name for the package (displayed in UI and user-facing applications).
            returned: on success
            type: str
            sample: display_name_example
        version:
            description:
                - Version of the package.
            returned: on success
            type: str
            sample: version_example
        time_published:
            description:
                - When the package was last published. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        description:
            description:
                - Description of the package.
            returned: on success
            type: str
            sample: description_example
        resource_types:
            description:
                - A list of resource types describing the content of the package.
            returned: on success
            type: list
            sample: []
        resource_types_metadata:
            description:
                - "A map of resource type to metadata key/value map that further describes the content for the resource types in this package.. Keys are
                  resource type names, values are a map of name/value pairs per resource type."
            returned: on success
            type: complex
            contains:
                resource_type:
                    description:
                        - The type of the resource described by this metadata object.
                    returned: on success
                    type: str
                    sample: resource_type_example
                properties:
                    description:
                        - Any properties needed to describe the content and its usage for this resource type, and within the containing package.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of property.
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - Value for the property.
                            returned: on success
                            type: str
                            sample: value_example
        publisher_metadata:
            description:
                - A map of metadata key/value pairs that further describes the publisher and the platform in which the package might be used.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of property.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - Value for the property.
                    returned: on success
                    type: str
                    sample: value_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "time_uploaded": "2013-10-20T19:20:30+01:00",
        "import_contract": {
            "import_contract": [{
                "resource_type": "resource_type_example",
                "parameters": [{
                    "name": "name_example",
                    "type": "STRING",
                    "description": "description_example",
                    "is_required": true,
                    "is_sensitive": true,
                    "default_value": "default_value_example",
                    "min_length": 56,
                    "max_length": 56,
                    "pattern": "pattern_example",
                    "direction": "INPUT",
                    "ui_placement_hint": "ui_placement_hint_example",
                    "resource_type_metadata": {}
                }]
            }]
        },
        "default_parameter_values": {
            "resource_types_default_parameter_values": [{
                "resource_type": "resource_type_example",
                "parameter_values": {}
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "publisher_id": "ocid1.publisher.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "display_name": "display_name_example",
        "version": "version_example",
        "time_published": "2013-10-20T19:20:30+01:00",
        "description": "description_example",
        "resource_types": [],
        "resource_types_metadata": [{
            "resource_type": "resource_type_example",
            "properties": [{
                "name": "name_example",
                "value": "value_example"
            }]
        }],
        "publisher_metadata": [{
            "name": "name_example",
            "value": "value_example"
        }],
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
    from oci.oda import OdapackageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
            "package_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_package,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            package_id=self.module.params.get("package_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "oda_instance_id",
            "resource_type",
            "name",
            "display_name",
            "is_latest_skill_only",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_packages, **optional_kwargs
        )


PackageFactsHelperCustom = get_custom_class("PackageFactsHelperCustom")


class ResourceFactsHelper(PackageFactsHelperCustom, PackageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            package_id=dict(aliases=["id"], type="str"),
            oda_instance_id=dict(type="str"),
            resource_type=dict(type="str"),
            name=dict(type="str"),
            display_name=dict(type="str"),
            is_latest_skill_only=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="package",
        service_client_class=OdapackageClient,
        namespace="oda",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(packages=result)


if __name__ == "__main__":
    main()
