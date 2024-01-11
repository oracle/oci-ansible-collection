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
module: oci_visual_builder_vb_instance_actions
short_description: Perform actions on a VbInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VbInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), change the compartment for an vb instance
    - For I(action=start), start an vb instance that was previously in an INACTIVE state. If the previous state is not
      INACTIVE, then the state of the vbInstance will not be changed and a 409 response returned.
    - For I(action=stop), stop an vb instance that was previously in an ACTIVE state. If the previous state is not
      ACTIVE, then the state of the vbInstance will not be changed and a 409 response returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier.
            - Required for I(action=change_compartment).
        type: str
    vb_instance_id:
        description:
            - Unique Vb Instance identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the VbInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on vb_instance
  oci_visual_builder_vb_instance_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vb_instance_id: "ocid1.vbinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action start on vb_instance
  oci_visual_builder_vb_instance_actions:
    # required
    vb_instance_id: "ocid1.vbinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on vb_instance
  oci_visual_builder_vb_instance_actions:
    # required
    vb_instance_id: "ocid1.vbinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
vb_instance:
    description:
        - Details of the VbInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Vb Instance Identifier, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the VbInstance was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the VbInstance was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the vb instance.
            returned: on success
            type: str
            sample: CREATING
        state_message:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        instance_url:
            description:
                - The Vb Instance URL.
            returned: on success
            type: str
            sample: instance_url_example
        node_count:
            description:
                - The number of Nodes
            returned: on success
            type: int
            sample: 56
        is_visual_builder_enabled:
            description:
                - Visual Builder is enabled or not.
            returned: on success
            type: bool
            sample: true
        custom_endpoint:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the vb instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
        alternate_custom_endpoints:
            description:
                - A list of alternate custom endpoints used for the vb instance URL.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - A custom hostname to be used for the vb instance URL, in FQDN format.
                    returned: on success
                    type: str
                    sample: hostname_example
                certificate_secret_id:
                    description:
                        - Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.
                    returned: on success
                    type: str
                    sample: "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx"
                certificate_secret_version:
                    description:
                        - The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
                    returned: on success
                    type: int
                    sample: 56
        consumption_model:
            description:
                - The entitlement used for billing purposes.
            returned: on success
            type: str
            sample: UCM
        idcs_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                idcs_app_location_url:
                    description:
                        - URL for the location of the IDCS Application (used by IDCS APIs)
                    returned: on success
                    type: str
                    sample: idcs_app_location_url_example
                idcs_app_display_name:
                    description:
                        - The IDCS application display name associated with the instance
                    returned: on success
                    type: str
                    sample: idcs_app_display_name_example
                idcs_app_id:
                    description:
                        - The IDCS application ID associated with the instance
                    returned: on success
                    type: str
                    sample: "ocid1.idcsapp.oc1..xxxxxxEXAMPLExxxxxx"
                idcs_app_name:
                    description:
                        - The IDCS application name associated with the instance
                    returned: on success
                    type: str
                    sample: idcs_app_name_example
                instance_primary_audience_url:
                    description:
                        - "The URL used as the primary audience for visual builder flows in this instance
                          type: string"
                    returned: on success
                    type: str
                    sample: instance_primary_audience_url_example
        attachments:
            description:
                - A list of associated attachments to other services
            returned: on success
            type: complex
            contains:
                target_role:
                    description:
                        - "The role of the target attachment.
                             * `PARENT` - The target instance is the parent of this attachment.
                             * `CHILD` - The target instance is the child of this attachment."
                    returned: on success
                    type: str
                    sample: PARENT
                is_implicit:
                    description:
                        - "* If role == `PARENT`, the attached instance was created by this service instance
                          * If role == `CHILD`, this instance was created from attached instance on behalf of a user"
                    returned: on success
                    type: bool
                    sample: true
                target_id:
                    description:
                        - The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.
                    returned: on success
                    type: str
                    sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
                target_instance_url:
                    description:
                        - The dataplane instance URL of the attached instance
                    returned: on success
                    type: str
                    sample: target_instance_url_example
                target_service_type:
                    description:
                        - "The type of the target instance, such as \\"FUSION\\"."
                    returned: on success
                    type: str
                    sample: target_service_type_example
        service_nat_gateway_ip:
            description:
                - The NAT gateway IP address for the VB service VCN
            returned: on success
            type: str
            sample: service_nat_gateway_ip_example
        management_nat_gateway_ip:
            description:
                - The NAT gateway IP address for the VB management VCN
            returned: on success
            type: str
            sample: management_nat_gateway_ip_example
        service_vcn_id:
            description:
                - The Oracle Cloud ID (OCID) of the Visual Builder service VCN
            returned: on success
            type: str
            sample: "ocid1.servicevcn.oc1..xxxxxxEXAMPLExxxxxx"
        management_vcn_id:
            description:
                - The Oracle Cloud ID (OCID) of the Visual Builder management VCN
            returned: on success
            type: str
            sample: "ocid1.managementvcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "state_message": "state_message_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "instance_url": "instance_url_example",
        "node_count": 56,
        "is_visual_builder_enabled": true,
        "custom_endpoint": {
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56
        },
        "alternate_custom_endpoints": [{
            "hostname": "hostname_example",
            "certificate_secret_id": "ocid1.certificatesecret.oc1..xxxxxxEXAMPLExxxxxx",
            "certificate_secret_version": 56
        }],
        "consumption_model": "UCM",
        "idcs_info": {
            "idcs_app_location_url": "idcs_app_location_url_example",
            "idcs_app_display_name": "idcs_app_display_name_example",
            "idcs_app_id": "ocid1.idcsapp.oc1..xxxxxxEXAMPLExxxxxx",
            "idcs_app_name": "idcs_app_name_example",
            "instance_primary_audience_url": "instance_primary_audience_url_example"
        },
        "attachments": [{
            "target_role": "PARENT",
            "is_implicit": true,
            "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
            "target_instance_url": "target_instance_url_example",
            "target_service_type": "target_service_type_example"
        }],
        "service_nat_gateway_ip": "service_nat_gateway_ip_example",
        "management_nat_gateway_ip": "management_nat_gateway_ip_example",
        "service_vcn_id": "ocid1.servicevcn.oc1..xxxxxxEXAMPLExxxxxx",
        "management_vcn_id": "ocid1.managementvcn.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.visual_builder import VbInstanceClient
    from oci.visual_builder.models import ChangeVbInstanceCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VbInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "vb_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("vb_instance_id")

    def get_get_fn(self):
        return self.client.get_vb_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vb_instance,
            vb_instance_id=self.module.params.get("vb_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVbInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_vb_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vb_instance_id=self.module.params.get("vb_instance_id"),
                change_vb_instance_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_vb_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vb_instance_id=self.module.params.get("vb_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_vb_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vb_instance_id=self.module.params.get("vb_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VbInstanceActionsHelperCustom = get_custom_class("VbInstanceActionsHelperCustom")


class ResourceHelper(VbInstanceActionsHelperCustom, VbInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            vb_instance_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "start", "stop"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vb_instance",
        service_client_class=VbInstanceClient,
        namespace="visual_builder",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
