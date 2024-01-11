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
module: oci_application_migration_source_facts
short_description: Fetches details about one or multiple Source resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Source resources in Oracle Cloud Infrastructure
    - Retrieves details of all the sources that are available in the specified compartment and match the specified query criteria.
      If you don't specify any query criteria, then details of all the sources are displayed.
      To filter the retrieved results, you can pass one or more of the following query parameters, by appending them to the URI
      as shown in the following example.
    - If I(source_id) is specified, the details of a single Source will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source.
            - Required to get a specific source.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a compartment. Retrieves details of objects in the
              specified compartment.
            - Required to list multiple sources.
        type: str
    sort_order:
        description:
            - The sort order, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the field on which to sort.
              By default, `TIMECREATED` is ordered descending.
              By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    display_name:
        description:
            - Display name on which to query.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Retrieves details of sources in the specified lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "DELETING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific source
  oci_application_migration_source_facts:
    # required
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"

- name: List sources
  oci_application_migration_source_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: TIMECREATED
    display_name: display_name_example
    lifecycle_state: CREATING

"""

RETURN = """
sources:
    description:
        - List of Source resources
    returned: on success
    type: complex
    contains:
        source_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                manifest:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        version:
                            description:
                                - the version of the export tool that was used to generate the manifest
                            returned: on success
                            type: str
                            sample: version_example
                        export_type:
                            description:
                                - the type of application that the export tool was executed against to generate this manifest
                            returned: on success
                            type: str
                            sample: export_type_example
                        export_details:
                            description:
                                - application specific details as parsed from various sources of the application that was exported
                            returned: on success
                            type: dict
                            sample: {}
                        timestamp:
                            description:
                                - when this manifest was generated
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        md5:
                            description:
                                - the MD5 hash of the export artifact archive that was produced by the export tool and should be used with this manifest
                            returned: on success
                            type: str
                            sample: md5_example
                        signature:
                            description:
                                - a sha1 hash of all the fields of this manifest (excluding the signature)
                            returned: on success
                            type: str
                            sample: signature_example
                namespace:
                    description:
                        - the object storage namespace where the bucket and uploaded object resides
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket:
                    description:
                        - the bucket wherein the export archive exists in object storage
                    returned: on success
                    type: str
                    sample: bucket_example
                object_name:
                    description:
                        - the name of the archive as it exists in object storage
                    returned: on success
                    type: str
                    sample: object_name_example
                account_name:
                    description:
                        - "The identity domain ID of your traditional Oracle Cloud Infrastructure - Classic account."
                    returned: on success
                    type: str
                    sample: account_name_example
                type:
                    description:
                        - The type of source environment.
                    returned: on success
                    type: str
                    sample: OCIC
                region:
                    description:
                        - "The Oracle Cloud Infrastructure - Classic region from which you want to migrate your applications. For example, uscom-east-1 or
                          uscom-central-1."
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                compute_account:
                    description:
                        - If you are using an Oracle Cloud@Customer account with Identity Cloud Service (IDCS), enter the service instance ID.
                          For example, if Compute-567890123 is the account name of your Oracle Cloud@Customer Compute service entitlement,
                          then enter 567890123.
                    returned: on success
                    type: str
                    sample: compute_account_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - The type of source environment.
                - Returned for list operation
            returned: on success
            type: str
            sample: OCIC
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the source.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time at which the source was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the source.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current lifecycle state of the source.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example:
                  `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example:
                  `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "source_details": {
            "manifest": {
                "version": "version_example",
                "export_type": "export_type_example",
                "export_details": {},
                "timestamp": "2013-10-20T19:20:30+01:00",
                "md5": "md5_example",
                "signature": "signature_example"
            },
            "namespace": "namespace_example",
            "bucket": "bucket_example",
            "object_name": "object_name_example",
            "account_name": "account_name_example",
            "type": "OCIC",
            "region": "us-phoenix-1",
            "compute_account": "compute_account_example"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "OCIC",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.application_migration import ApplicationMigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "source_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_source, source_id=self.module.params.get("source_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "display_name",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sources,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SourceFactsHelperCustom = get_custom_class("SourceFactsHelperCustom")


class ResourceFactsHelper(SourceFactsHelperCustom, SourceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            source_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "DELETING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="source",
        service_client_class=ApplicationMigrationClient,
        namespace="application_migration",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sources=result)


if __name__ == "__main__":
    main()
