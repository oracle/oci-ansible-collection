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
module: oci_database_application_vip
short_description: Manage an ApplicationVip resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an ApplicationVip resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new application virtual IP (VIP) address in the specified cloud VM cluster based on the request parameters you provide.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    hostname_label:
        description:
            - The hostname of the application virtual IP (VIP) address.
            - Required for create using I(state=present).
        type: str
    db_node_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB node associated with the application virtual IP (VIP)
              address.
        type: str
    cloud_vm_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud VM cluster associated with the application virtual
              IP (VIP) address.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet associated with the application virtual IP (VIP)
              address.
            - Required for create using I(state=present).
        type: str
    ip_address:
        description:
            - The application virtual IP (VIP) address.
        type: str
    application_vip_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the application virtual IP (VIP) address.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the ApplicationVip.
            - Use I(state=present) to create an ApplicationVip.
            - Use I(state=absent) to delete an ApplicationVip.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create application_vip
  oci_database_application_vip:
    # required
    hostname_label: hostname_label_example
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_node_id: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"
    ip_address: ip_address_example

- name: Delete application_vip
  oci_database_application_vip:
    # required
    application_vip_id: "ocid1.applicationvip.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
application_vip:
    description:
        - Details of the ApplicationVip resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        cloud_vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud VM cluster associated with the application
                  virtual IP (VIP) address.
            returned: on success
            type: str
            sample: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet associated with the application virtual IP
                  (VIP) address.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: ip_address_example
        hostname_label:
            description:
                - The hostname of the application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: hostname_label_example
        lifecycle_state:
            description:
                - The current lifecycle state of the application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_assigned:
            description:
                - The date and time when the create operation for the application virtual IP (VIP) address completed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "cloud_vm_cluster_id": "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "ip_address_example",
        "hostname_label": "hostname_label_example",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_assigned": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateApplicationVipDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApplicationVipHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ApplicationVipHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    def get_possible_entity_types(self):
        return super(ApplicationVipHelperGen, self).get_possible_entity_types() + [
            "applicationvip",
            "applicationvips",
            "databaseapplicationvip",
            "databaseapplicationvips",
            "applicationvipresource",
            "applicationvipsresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "application_vip_id"

    def get_module_resource_id(self):
        return self.module.params.get("application_vip_id")

    def get_get_fn(self):
        return self.client.get_application_vip

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_application_vip, application_vip_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_application_vip,
            application_vip_id=self.module.params.get("application_vip_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "cloud_vm_cluster_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_application_vips, **kwargs
        )

    def get_create_model_class(self):
        return CreateApplicationVipDetails

    def get_exclude_attributes(self):
        return ["db_node_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_application_vip,
            call_fn_args=(),
            call_fn_kwargs=dict(create_application_vip_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_application_vip,
            call_fn_args=(),
            call_fn_kwargs=dict(
                application_vip_id=self.module.params.get("application_vip_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ApplicationVipHelperCustom = get_custom_class("ApplicationVipHelperCustom")


class ResourceHelper(ApplicationVipHelperCustom, ApplicationVipHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            hostname_label=dict(type="str"),
            db_node_id=dict(type="str"),
            cloud_vm_cluster_id=dict(type="str"),
            subnet_id=dict(type="str"),
            ip_address=dict(type="str"),
            application_vip_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="application_vip",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
