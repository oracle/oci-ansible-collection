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
module: oci_functions_application
short_description: Manage an Application resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Application resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new application.
    - "This resource has the following action operations in the M(oracle.oci.oci_functions_application_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to create the application within.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The display name of the application. The display name must be unique within the compartment containing the application. Avoid entering
              confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    subnet_ids:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the subnets in which to run functions in the
              application.
            - Required for create using I(state=present).
        type: list
        elements: str
    config:
        description:
            - Application configuration. These values are passed on to the function as environment variables, functions may override application configuration.
              Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values
              should be limited to printable unicode characters.
            - "Example: `{\\"MY_FUNCTION_CONFIG\\": \\"ConfVal\\"}`"
            - The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key
              and value in UTF-8.
            - This parameter is updatable.
        type: dict
    network_security_group_ids:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the Network Security Groups to add the application to.
            - This parameter is updatable.
        type: list
        elements: str
    syslog_url:
        description:
            - "A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
              The syslog URL must be reachable from all of the subnets configured for the application.
              Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging
              service, and not to the syslog URL."
            - "Example: `tcp://logserver.myserver:1234`"
            - This parameter is updatable.
        type: str
    trace_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_enabled:
                description:
                    - Define if tracing is enabled for the resource.
                type: bool
            domain_id:
                description:
                    - The OCID of the collector (e.g. an APM Domain) trace events will be sent to.
                type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    image_policy_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_policy_enabled:
                description:
                    - Define if image signature verification policy is enabled for the application.
                type: bool
                required: true
            key_details:
                description:
                    - A list of KMS key details.
                type: list
                elements: dict
                suboptions:
                    kms_key_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the KMS key that will be used to
                              verify the image signature.
                        type: str
                        required: true
    application_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this application.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Application.
            - Use I(state=present) to create or update an Application.
            - Use I(state=absent) to delete an Application.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create application
  oci_functions_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    subnet_ids: [ "subnet_ids_example" ]

    # optional
    config: null
    network_security_group_ids: [ "network_security_group_ids_example" ]
    syslog_url: syslog_url_example
    trace_config:
      # optional
      is_enabled: true
      domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    image_policy_config:
      # required
      is_policy_enabled: true

      # optional
      key_details:
      - # required
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update application
  oci_functions_application:
    # required
    application_id: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    config: null
    network_security_group_ids: [ "network_security_group_ids_example" ]
    syslog_url: syslog_url_example
    trace_config:
      # optional
      is_enabled: true
      domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    image_policy_config:
      # required
      is_policy_enabled: true

      # optional
      key_details:
      - # required
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update application using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_functions_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    config: null
    network_security_group_ids: [ "network_security_group_ids_example" ]
    syslog_url: syslog_url_example
    trace_config:
      # optional
      is_enabled: true
      domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    image_policy_config:
      # required
      is_policy_enabled: true

      # optional
      key_details:
      - # required
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete application
  oci_functions_application:
    # required
    application_id: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete application using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_functions_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
application:
    description:
        - Details of the Application resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the application.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the application.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the application. The display name is unique within the compartment containing the application.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the application.
            returned: on success
            type: str
            sample: CREATING
        config:
            description:
                - Application configuration for functions in this application (passed as environment variables). Can be overridden by function configuration.
                  Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values
                  should be limited to printable unicode characters.
                - "Example: `{\\"MY_FUNCTION_CONFIG\\": \\"ConfVal\\"}`"
                - The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each
                  key and value in UTF-8.
            returned: on success
            type: dict
            sample: {}
        subnet_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the subnets in which to run functions in the
                  application.
            returned: on success
            type: list
            sample: []
        network_security_group_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the Network Security Groups to add the application
                  to.
            returned: on success
            type: list
            sample: []
        syslog_url:
            description:
                - "A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
                  The syslog URL must be reachable from all of the subnets configured for the application.
                  Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging
                  service, and not to the syslog URL."
                - "Example: `tcp://logserver.myserver:1234`"
            returned: on success
            type: str
            sample: syslog_url_example
        trace_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - Define if tracing is enabled for the resource.
                    returned: on success
                    type: bool
                    sample: true
                domain_id:
                    description:
                        - The OCID of the collector (e.g. an APM Domain) trace events will be sent to.
                    returned: on success
                    type: str
                    sample: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        time_created:
            description:
                - The time the application was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time the application was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        image_policy_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_policy_enabled:
                    description:
                        - Define if image signature verification policy is enabled for the application.
                    returned: on success
                    type: bool
                    sample: true
                key_details:
                    description:
                        - A list of KMS key details.
                    returned: on success
                    type: complex
                    contains:
                        kms_key_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the KMS key that will be used to
                                  verify the image signature.
                            returned: on success
                            type: str
                            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "config": {},
        "subnet_ids": [],
        "network_security_group_ids": [],
        "syslog_url": "syslog_url_example",
        "trace_config": {
            "is_enabled": true,
            "domain_id": "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "image_policy_config": {
            "is_policy_enabled": true,
            "key_details": [{
                "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.functions import FunctionsManagementClient
    from oci.functions.models import CreateApplicationDetails
    from oci.functions.models import UpdateApplicationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApplicationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ApplicationHelperGen, self).get_possible_entity_types() + [
            "application",
            "applications",
            "functionsapplication",
            "functionsapplications",
            "applicationresource",
            "applicationsresource",
            "functions",
        ]

    def get_module_resource_id_param(self):
        return "application_id"

    def get_module_resource_id(self):
        return self.module.params.get("application_id")

    def get_get_fn(self):
        return self.client.get_application

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_application, application_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_application,
            application_id=self.module.params.get("application_id"),
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
        return oci_common_utils.list_all_resources(
            self.client.list_applications, **kwargs
        )

    def get_create_model_class(self):
        return CreateApplicationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_application,
            call_fn_args=(),
            call_fn_kwargs=dict(create_application_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateApplicationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_application,
            call_fn_args=(),
            call_fn_kwargs=dict(
                application_id=self.module.params.get("application_id"),
                update_application_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_application,
            call_fn_args=(),
            call_fn_kwargs=dict(
                application_id=self.module.params.get("application_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ApplicationHelperCustom = get_custom_class("ApplicationHelperCustom")


class ResourceHelper(ApplicationHelperCustom, ApplicationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            subnet_ids=dict(type="list", elements="str"),
            config=dict(type="dict"),
            network_security_group_ids=dict(type="list", elements="str"),
            syslog_url=dict(type="str"),
            trace_config=dict(
                type="dict",
                options=dict(is_enabled=dict(type="bool"), domain_id=dict(type="str")),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            image_policy_config=dict(
                type="dict",
                options=dict(
                    is_policy_enabled=dict(type="bool", required=True),
                    key_details=dict(
                        type="list",
                        elements="dict",
                        no_log=False,
                        options=dict(kms_key_id=dict(type="str", required=True)),
                    ),
                ),
            ),
            application_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="application",
        service_client_class=FunctionsManagementClient,
        namespace="functions",
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
