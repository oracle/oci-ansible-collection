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
module: oci_application_migration_source
short_description: Manage a Source resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Source resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a source in the specified compartment. In Application Migration, a source refers to the environment from which the
      application
      is being migrated. For more information, see L(Manage Sources,https://docs.cloud.oracle.com/iaas/application-migration/manage_sources.htm).
    - All Oracle Cloud Infrastructure resources, including sources, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID).
      When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation
      on that resource type, or by viewing the resource in the Console.
    - After you send your request, a source is created in the specified compartment. The new source's lifecycle state will temporarily be
      <code>CREATING</code>. Application Migration connects to the source environment with the authentication credentials that you have provided.
      If the connection is established, the status of the source changes to <code>ACTIVE</code> and Application Migration fetches the list of
      applications that are available for migration in the source environment.
    - To track the progress of the operation, you can monitor the status of the Create Source work request by using the
      <code>L(GetWorkRequest,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/applicationmigration/20191031/WorkRequest/GetWorkRequest)</code> REST API
      operation on the work request or by viewing the status of the work request in the console.
    - Ensure that the state of the source has changed to <code>ACTIVE</code>, before you retrieve the list of applications from
      the source environment using the <code>L(ListSourceApplications,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/applicationmigration/20191031/SourceApplicationSummary/ListSourceApplications)</code> REST API call.
    - "This resource has the following action operations in the M(oracle.oci.oci_application_migration_source_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the source.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.
            - This parameter is updatable.
        type: str
    source_details:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            manifest:
                description:
                    - ""
                    - Required when type is 'IMPORT'
                type: dict
                suboptions:
                    version:
                        description:
                            - the version of the export tool that was used to generate the manifest
                            - Applicable when type is 'IMPORT'
                        type: str
                    export_type:
                        description:
                            - the type of application that the export tool was executed against to generate this manifest
                            - Applicable when type is 'IMPORT'
                        type: str
                    export_details:
                        description:
                            - application specific details as parsed from various sources of the application that was exported
                            - Applicable when type is 'IMPORT'
                        type: dict
                    timestamp:
                        description:
                            - when this manifest was generated
                            - Applicable when type is 'IMPORT'
                        type: str
                    md5:
                        description:
                            - the MD5 hash of the export artifact archive that was produced by the export tool and should be used with this manifest
                            - Applicable when type is 'IMPORT'
                        type: str
                    signature:
                        description:
                            - a sha1 hash of all the fields of this manifest (excluding the signature)
                            - Applicable when type is 'IMPORT'
                        type: str
            namespace:
                description:
                    - the object storage namespace where the bucket and uploaded object resides
                    - Required when type is 'IMPORT'
                type: str
            bucket:
                description:
                    - the bucket wherein the export archive exists in object storage
                    - Required when type is 'IMPORT'
                type: str
            object_name:
                description:
                    - the name of the archive as it exists in object storage
                    - Required when type is 'IMPORT'
                type: str
            account_name:
                description:
                    - "The identity domain ID of your traditional Oracle Cloud Infrastructure - Classic account."
                    - Required when type is 'INTERNAL_COMPUTE'
                type: str
            type:
                description:
                    - The type of source environment.
                type: str
                choices:
                    - "IMPORT"
                    - "OCC"
                    - "INTERNAL_COMPUTE"
                    - "OCIC"
                required: true
            region:
                description:
                    - "The Oracle Cloud Infrastructure - Classic region from which you want to migrate your applications. For example, uscom-east-1 or uscom-
                      central-1."
                    - Required when type is 'OCIC'
                type: str
            compute_account:
                description:
                    - If you are using an Oracle Cloud@Customer account with Identity Cloud Service (IDCS), enter the service instance ID.
                      For example, if Compute-567890123 is the account name of your Oracle Cloud@Customer Compute service entitlement,
                      then enter 567890123.
                    - Required when type is one of ['OCIC', 'OCC']
                type: str
    authorization_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            client_app_url:
                description:
                    - AuthClient app url resource that the accesstoken is for.
                    - Required when type is 'OCIC_IDCS'
                type: str
            access_token:
                description:
                    - AccessToken to access the app endpoint.
                    - Required when type is 'OCIC_IDCS'
                type: str
            type:
                description:
                    - Type of the source environment from which you are migrating applications to Oracle Cloud Infrastructure.
                type: str
                choices:
                    - "OCC"
                    - "INTERNAL_COMPUTE"
                    - "OCIC_IDCS"
                    - "OCIC"
                required: true
            username:
                description:
                    - User with Compute Operations role in Oracle Cloud@Customer.
                    - Required when type is one of ['OCIC', 'INTERNAL_COMPUTE', 'OCC']
                type: str
            password:
                description:
                    - Password for this user.
                    - Required when type is one of ['OCIC', 'INTERNAL_COMPUTE', 'OCC']
                type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"Department\\":
              \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"Operations\\":
              {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Source.
            - Use I(state=present) to create or update a Source.
            - Use I(state=absent) to delete a Source.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create source
  oci_application_migration_source:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source_details:
      # required
      manifest:
        # optional
        version: version_example
        export_type: export_type_example
        export_details: null
        timestamp: timestamp_example
        md5: md5_example
        signature: signature_example
      namespace: namespace_example
      bucket: bucket_example
      object_name: object_name_example
      type: IMPORT

    # optional
    display_name: display_name_example
    description: description_example
    authorization_details:
      # required
      type: OCC
      username: username_example
      password: example-password
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update source
  oci_application_migration_source:
    # required
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    source_details:
      # required
      manifest:
        # optional
        version: version_example
        export_type: export_type_example
        export_details: null
        timestamp: timestamp_example
        md5: md5_example
        signature: signature_example
      namespace: namespace_example
      bucket: bucket_example
      object_name: object_name_example
      type: IMPORT
    authorization_details:
      # required
      type: OCC
      username: username_example
      password: example-password
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update source using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_application_migration_source:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    source_details:
      # required
      manifest:
        # optional
        version: version_example
        export_type: export_type_example
        export_details: null
        timestamp: timestamp_example
        md5: md5_example
        signature: signature_example
      namespace: namespace_example
      bucket: bucket_example
      object_name: object_name_example
      type: IMPORT
    authorization_details:
      # required
      type: OCC
      username: username_example
      password: example-password
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete source
  oci_application_migration_source:
    # required
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete source using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_application_migration_source:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
source:
    description:
        - Details of the Source resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
        source_details:
            description:
                - ""
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.application_migration import ApplicationMigrationClient
    from oci.application_migration.models import CreateSourceDetails
    from oci.application_migration.models import UpdateSourceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SourceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(SourceHelperGen, self).get_possible_entity_types() + [
            "source",
            "sources",
            "applicationMigrationsource",
            "applicationMigrationsources",
            "sourceresource",
            "sourcesresource",
            "applicationmigration",
        ]

    def get_module_resource_id_param(self):
        return "source_id"

    def get_module_resource_id(self):
        return self.module.params.get("source_id")

    def get_get_fn(self):
        return self.client.get_source

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_source, source_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_source, source_id=self.module.params.get("source_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_sources, **kwargs)

    def get_create_model_class(self):
        return CreateSourceDetails

    def get_exclude_attributes(self):
        return ["authorization_details"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_source,
            call_fn_args=(),
            call_fn_kwargs=dict(create_source_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateSourceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                source_id=self.module.params.get("source_id"),
                update_source_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_source,
            call_fn_args=(),
            call_fn_kwargs=dict(source_id=self.module.params.get("source_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


SourceHelperCustom = get_custom_class("SourceHelperCustom")


class ResourceHelper(SourceHelperCustom, SourceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            source_details=dict(
                type="dict",
                options=dict(
                    manifest=dict(
                        type="dict",
                        options=dict(
                            version=dict(type="str"),
                            export_type=dict(type="str"),
                            export_details=dict(type="dict"),
                            timestamp=dict(type="str"),
                            md5=dict(type="str"),
                            signature=dict(type="str"),
                        ),
                    ),
                    namespace=dict(type="str"),
                    bucket=dict(type="str"),
                    object_name=dict(type="str"),
                    account_name=dict(type="str"),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["IMPORT", "OCC", "INTERNAL_COMPUTE", "OCIC"],
                    ),
                    region=dict(type="str"),
                    compute_account=dict(type="str"),
                ),
            ),
            authorization_details=dict(
                type="dict",
                options=dict(
                    client_app_url=dict(type="str"),
                    access_token=dict(type="str", no_log=True),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["OCC", "INTERNAL_COMPUTE", "OCIC_IDCS", "OCIC"],
                    ),
                    username=dict(type="str"),
                    password=dict(type="str", no_log=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            source_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="source",
        service_client_class=ApplicationMigrationClient,
        namespace="application_migration",
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
