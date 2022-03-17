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
module: oci_analytics_instance_actions
short_description: Perform actions on an AnalyticsInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AnalyticsInstance resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), change the compartment of an Analytics instance. The operation is long-running
      and creates a new WorkRequest.
    - For I(action=change_analytics_instance_network_endpoint), change an Analytics instance network endpoint. The operation is long-running
      and creates a new WorkRequest.
    - For I(action=scale), scale an Analytics instance up or down. The operation is long-running
      and creates a new WorkRequest.
    - For I(action=set_kms_key), encrypts the customer data of this Analytics instance using either a customer OCI Vault Key or Oracle managed default key.
    - For I(action=start), starts the specified Analytics instance. The operation is long-running
      and creates a new WorkRequest.
    - For I(action=stop), stop the specified Analytics instance. The operation is long-running
      and creates a new WorkRequest.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    analytics_instance_id:
        description:
            - The OCID of the AnalyticsInstance.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the new compartment.
            - Required for I(action=change_compartment).
        type: str
    network_endpoint_details:
        description:
            - ""
            - Required for I(action=change_analytics_instance_network_endpoint).
        type: dict
        suboptions:
            network_endpoint_type:
                description:
                    - The type of network endpoint.
                type: str
                choices:
                    - "PRIVATE"
                    - "PUBLIC"
                required: true
            vcn_id:
                description:
                    - The VCN OCID for the private endpoint.
                    - Required when network_endpoint_type is 'PRIVATE'
                type: str
            subnet_id:
                description:
                    - The subnet OCID for the private endpoint.
                    - Required when network_endpoint_type is 'PRIVATE'
                type: str
            whitelisted_ips:
                description:
                    - Source IP addresses or IP address ranges igress rules.
                    - Applicable when network_endpoint_type is 'PUBLIC'
                type: list
                elements: str
            whitelisted_vcns:
                description:
                    - Virtual Cloud Networks allowed to access this network endpoint.
                    - Applicable when network_endpoint_type is 'PUBLIC'
                type: list
                elements: dict
                suboptions:
                    id:
                        description:
                            - The Virtual Cloud Network OCID.
                            - Required when network_endpoint_type is 'PUBLIC'
                        type: str
                        required: true
                    whitelisted_ips:
                        description:
                            - Source IP addresses or IP address ranges igress rules.
                            - Applicable when network_endpoint_type is 'PUBLIC'
                        type: list
                        elements: str
    capacity:
        description:
            - ""
            - Required for I(action=scale).
        type: dict
        suboptions:
            capacity_type:
                description:
                    - The capacity model to use.
                type: str
                choices:
                    - "OLPU_COUNT"
                    - "USER_COUNT"
                required: true
            capacity_value:
                description:
                    - "The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the
                      number of CPUs, amount of memory or other resources allocated to the instance."
                type: int
                required: true
    kms_key_id:
        description:
            - OCID of the OCI Vault Key encrypting the customer data stored in this Analytics instance. An empty value indicates Oracle managed default
              encryption (null is not supported in this API).
            - Required for I(action=set_kms_key).
        type: str
    action:
        description:
            - The action to perform on the AnalyticsInstance.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "change_analytics_instance_network_endpoint"
            - "scale"
            - "set_kms_key"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on analytics_instance
  oci_analytics_instance_actions:
    # required
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action change_analytics_instance_network_endpoint on analytics_instance
  oci_analytics_instance_actions:
    # required
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    network_endpoint_details:
      # required
      network_endpoint_type: PRIVATE
      vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_analytics_instance_network_endpoint

- name: Perform action scale on analytics_instance
  oci_analytics_instance_actions:
    # required
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    capacity:
      # required
      capacity_type: OLPU_COUNT
      capacity_value: 56
    action: scale

- name: Perform action set_kms_key on analytics_instance
  oci_analytics_instance_actions:
    # required
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    action: set_kms_key

- name: Perform action start on analytics_instance
  oci_analytics_instance_actions:
    # required
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on analytics_instance
  oci_analytics_instance_actions:
    # required
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
analytics_instance:
    description:
        - Details of the AnalyticsInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The resource OCID.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Optional description.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of an instance.
            returned: on success
            type: str
            sample: ACTIVE
        feature_set:
            description:
                - Analytics feature set.
            returned: on success
            type: str
            sample: SELF_SERVICE_ANALYTICS
        capacity:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                capacity_type:
                    description:
                        - The capacity model to use.
                    returned: on success
                    type: str
                    sample: OLPU_COUNT
                capacity_value:
                    description:
                        - "The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the
                          number of CPUs, amount of memory or other resources allocated to the instance."
                    returned: on success
                    type: int
                    sample: 56
        license_type:
            description:
                - The license used for the service.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        email_notification:
            description:
                - Email address receiving notifications.
            returned: on success
            type: str
            sample: email_notification_example
        network_endpoint_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                vcn_id:
                    description:
                        - The VCN OCID for the private endpoint.
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - The subnet OCID for the private endpoint.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                network_endpoint_type:
                    description:
                        - The type of network endpoint.
                    returned: on success
                    type: str
                    sample: PUBLIC
                whitelisted_ips:
                    description:
                        - Source IP addresses or IP address ranges igress rules.
                    returned: on success
                    type: list
                    sample: []
                whitelisted_vcns:
                    description:
                        - Virtual Cloud Networks allowed to access this network endpoint.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The Virtual Cloud Network OCID.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        whitelisted_ips:
                            description:
                                - Source IP addresses or IP address ranges igress rules.
                            returned: on success
                            type: list
                            sample: []
        private_access_channels:
            description:
                - Map of PrivateAccessChannel unique identifier key as KEY and PrivateAccessChannel Object as VALUE.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Private Access Channel unique identifier key.
                    returned: on success
                    type: str
                    sample: key_example
                display_name:
                    description:
                        - Display Name of the Private Access Channel.
                    returned: on success
                    type: str
                    sample: display_name_example
                vcn_id:
                    description:
                        - OCID of the customer VCN peered with private access channel.
                    returned: on success
                    type: str
                    sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
                subnet_id:
                    description:
                        - OCID of the customer subnet connected to private access channel.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                ip_address:
                    description:
                        - IP Address of the Private Access channel.
                    returned: on success
                    type: str
                    sample: ip_address_example
                egress_source_ip_addresses:
                    description:
                        - The list of IP addresses from the customer subnet connected to private access channel, used as a source Ip by Private Access Channel
                          for network traffic from the AnalyticsInstance to Private Sources.
                    returned: on success
                    type: list
                    sample: []
                private_source_dns_zones:
                    description:
                        - List of Private Source DNS zones registered with Private Access Channel,
                          where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance.
                          Min of 1 is required and Max of 30 Private Source DNS zones can be registered.
                    returned: on success
                    type: complex
                    contains:
                        dns_zone:
                            description:
                                - "Private Source DNS Zone. Ex: example-vcn.oraclevcn.com, corp.example.com."
                            returned: on success
                            type: str
                            sample: dns_zone_example
                        description:
                            description:
                                - Description of private source dns zone.
                            returned: on success
                            type: str
                            sample: description_example
        vanity_url_details:
            description:
                - Map of VanityUrl unique identifier key as KEY and VanityUrl Object as VALUE.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - The vanity url unique identifier key.
                    returned: on success
                    type: str
                    sample: key_example
                description:
                    description:
                        - Description of the vanity url.
                    returned: on success
                    type: str
                    sample: description_example
                urls:
                    description:
                        - List of urls supported by this vanity URL definition (max of 3).
                    returned: on success
                    type: list
                    sample: []
                hosts:
                    description:
                        - List of fully qualified hostnames supported by this vanity URL definition (max of 3).
                    returned: on success
                    type: list
                    sample: []
                public_certificate:
                    description:
                        - PEM certificate for HTTPS connections.
                    returned: on success
                    type: str
                    sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        service_url:
            description:
                - URL of the Analytics service.
            returned: on success
            type: str
            sample: service_url_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        kms_key_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the OCI Vault Key encrypting the customer data stored in
                  this Analytics instance. A null value indicates Oracle managed default encryption.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the instance was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the instance was last updated (in the format defined by RFC3339).
                  This timestamp represents updates made through this API. External events do not
                  influence it.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "feature_set": "SELF_SERVICE_ANALYTICS",
        "capacity": {
            "capacity_type": "OLPU_COUNT",
            "capacity_value": 56
        },
        "license_type": "LICENSE_INCLUDED",
        "email_notification": "email_notification_example",
        "network_endpoint_details": {
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "network_endpoint_type": "PUBLIC",
            "whitelisted_ips": [],
            "whitelisted_vcns": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "whitelisted_ips": []
            }]
        },
        "private_access_channels": {
            "key": "key_example",
            "display_name": "display_name_example",
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "ip_address": "ip_address_example",
            "egress_source_ip_addresses": [],
            "private_source_dns_zones": [{
                "dns_zone": "dns_zone_example",
                "description": "description_example"
            }]
        },
        "vanity_url_details": {
            "key": "key_example",
            "description": "description_example",
            "urls": [],
            "hosts": [],
            "public_certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        },
        "service_url": "service_url_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.analytics import AnalyticsClient
    from oci.analytics.models import ChangeCompartmentDetails
    from oci.analytics.models import ChangeAnalyticsInstanceNetworkEndpointDetails
    from oci.analytics.models import ScaleAnalyticsInstanceDetails
    from oci.analytics.models import SetKmsKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnalyticsInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        change_analytics_instance_network_endpoint
        scale
        set_kms_key
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "analytics_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("analytics_instance_id")

    def get_get_fn(self):
        return self.client.get_analytics_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_analytics_instance,
            analytics_instance_id=self.module.params.get("analytics_instance_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_analytics_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                change_compartment_details=action_details,
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

    def change_analytics_instance_network_endpoint(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAnalyticsInstanceNetworkEndpointDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_analytics_instance_network_endpoint,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                change_analytics_instance_network_endpoint_details=action_details,
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

    def scale(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScaleAnalyticsInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.scale_analytics_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                scale_analytics_instance_details=action_details,
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

    def set_kms_key(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SetKmsKeyDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.set_kms_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                set_kms_key_details=action_details,
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
            call_fn=self.client.start_analytics_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
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
            call_fn=self.client.stop_analytics_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
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


AnalyticsInstanceActionsHelperCustom = get_custom_class(
    "AnalyticsInstanceActionsHelperCustom"
)


class ResourceHelper(
    AnalyticsInstanceActionsHelperCustom, AnalyticsInstanceActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            analytics_instance_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            network_endpoint_details=dict(
                type="dict",
                options=dict(
                    network_endpoint_type=dict(
                        type="str", required=True, choices=["PRIVATE", "PUBLIC"]
                    ),
                    vcn_id=dict(type="str"),
                    subnet_id=dict(type="str"),
                    whitelisted_ips=dict(type="list", elements="str"),
                    whitelisted_vcns=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            id=dict(type="str", required=True),
                            whitelisted_ips=dict(type="list", elements="str"),
                        ),
                    ),
                ),
            ),
            capacity=dict(
                type="dict",
                options=dict(
                    capacity_type=dict(
                        type="str", required=True, choices=["OLPU_COUNT", "USER_COUNT"]
                    ),
                    capacity_value=dict(type="int", required=True),
                ),
            ),
            kms_key_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "change_analytics_instance_network_endpoint",
                    "scale",
                    "set_kms_key",
                    "start",
                    "stop",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="analytics_instance",
        service_client_class=AnalyticsClient,
        namespace="analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
