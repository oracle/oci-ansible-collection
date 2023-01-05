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
module: oci_analytics_private_access_channel
short_description: Manage a PrivateAccessChannel resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PrivateAccessChannel resource in Oracle Cloud Infrastructure
    - For I(state=present), create an Private access Channel for the Analytics instance. The operation is long-running
      and creates a new WorkRequest.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Display Name of the Private Access Channel.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        aliases: ["name"]
    vcn_id:
        description:
            - OCID of the customer VCN peered with private access channel.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    subnet_id:
        description:
            - OCID of the customer subnet connected to private access channel.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    private_source_dns_zones:
        description:
            - List of Private Source DNS zones registered with Private Access Channel,
              where datasource hostnames from these dns zones / domains will be resolved in the peered VCN for access from Analytics Instance.
              Min of 1 is required and Max of 30 Private Source DNS zones can be registered.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            dns_zone:
                description:
                    - "Private Source DNS Zone. Ex: example-vcn.oraclevcn.com, corp.example.com."
                type: str
                required: true
            description:
                description:
                    - Description of private source dns zone.
                type: str
    private_source_scan_hosts:
        description:
            - List of Private Source DB SCAN hosts registered with Private Access Channel for access from Analytics Instance.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            scan_hostname:
                description:
                    - "Private Source Scan hostname. Ex: db01-scan.corp.example.com, prd-db01-scan.mycompany.com."
                type: str
                required: true
            scan_port:
                description:
                    - Private Source Scan host port. This is the source port where SCAN protocol will get connected (e.g. 1521).
                type: int
                required: true
            description:
                description:
                    - Description of private source scan host zone.
                type: str
    network_security_group_ids:
        description:
            - Network Security Group OCIDs for an Analytics instance.
            - This parameter is updatable.
        type: list
        elements: str
    private_access_channel_key:
        description:
            - The unique identifier key of the Private Access Channel.
            - Required for update using I(state=present) with analytics_instance_id present.
            - Required for delete using I(state=absent).
        type: str
    analytics_instance_id:
        description:
            - The OCID of the AnalyticsInstance.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the PrivateAccessChannel.
            - Use I(state=present) to create or update a PrivateAccessChannel.
            - Use I(state=absent) to delete a PrivateAccessChannel.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create private_access_channel
  oci_analytics_private_access_channel:
    # required
    display_name: display_name_example
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_source_dns_zones:
    - # required
      dns_zone: dns_zone_example

      # optional
      description: description_example
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    private_source_scan_hosts:
    - # required
      scan_hostname: scan_hostname_example
      scan_port: 56

      # optional
      description: description_example
    network_security_group_ids: [ "network_security_group_ids_example" ]

- name: Update private_access_channel
  oci_analytics_private_access_channel:
    # required
    private_access_channel_key: private_access_channel_key_example
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_source_dns_zones:
    - # required
      dns_zone: dns_zone_example

      # optional
      description: description_example
    private_source_scan_hosts:
    - # required
      scan_hostname: scan_hostname_example
      scan_port: 56

      # optional
      description: description_example
    network_security_group_ids: [ "network_security_group_ids_example" ]

- name: Delete private_access_channel
  oci_analytics_private_access_channel:
    # required
    private_access_channel_key: private_access_channel_key_example
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
private_access_channel:
    description:
        - Details of the PrivateAccessChannel resource acted upon by the current operation
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
        private_source_scan_hosts:
            description:
                - List of Private Source DB SCAN hosts registered with Private Access Channel for access from Analytics Instance.
            returned: on success
            type: complex
            contains:
                scan_hostname:
                    description:
                        - "Private Source Scan hostname. Ex: db01-scan.corp.example.com, prd-db01-scan.mycompany.com."
                    returned: on success
                    type: str
                    sample: scan_hostname_example
                scan_port:
                    description:
                        - Private Source Scan host port. This is the source port where SCAN protocol will get connected (e.g. 1521).
                    returned: on success
                    type: int
                    sample: 56
                description:
                    description:
                        - Description of private source scan host zone.
                    returned: on success
                    type: str
                    sample: description_example
        network_security_group_ids:
            description:
                - Network Security Group OCIDs for an Analytics instance.
            returned: on success
            type: list
            sample: []
    sample: {
        "key": "key_example",
        "display_name": "display_name_example",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "ip_address_example",
        "egress_source_ip_addresses": [],
        "private_source_dns_zones": [{
            "dns_zone": "dns_zone_example",
            "description": "description_example"
        }],
        "private_source_scan_hosts": [{
            "scan_hostname": "scan_hostname_example",
            "scan_port": 56,
            "description": "description_example"
        }],
        "network_security_group_ids": []
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
    from oci.analytics import AnalyticsClient
    from oci.analytics.models import CreatePrivateAccessChannelDetails
    from oci.analytics.models import UpdatePrivateAccessChannelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateAccessChannelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and delete"""

    def get_default_module_wait_timeout(self):
        return 7200

    def get_possible_entity_types(self):
        return super(
            PrivateAccessChannelHelperGen, self
        ).get_possible_entity_types() + [
            "privateaccesschannel",
            "privateaccesschannels",
            "analyticsprivateaccesschannel",
            "analyticsprivateaccesschannels",
            "privateaccesschannelresource",
            "privateaccesschannelsresource",
            "analytics",
        ]

    def get_module_resource_id_param(self):
        return "analytics_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("analytics_instance_id")

    def get_get_fn(self):
        return self.client.get_private_access_channel

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_access_channel,
            private_access_channel_key=self.module.params.get(
                "private_access_channel_key"
            ),
            analytics_instance_id=self.module.params.get("analytics_instance_id"),
        )

    def get_create_model_class(self):
        return CreatePrivateAccessChannelDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_private_access_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                create_private_access_channel_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdatePrivateAccessChannelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_private_access_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_access_channel_key=self.module.params.get(
                    "private_access_channel_key"
                ),
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                update_private_access_channel_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_private_access_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                private_access_channel_key=self.module.params.get(
                    "private_access_channel_key"
                ),
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PrivateAccessChannelHelperCustom = get_custom_class("PrivateAccessChannelHelperCustom")


class ResourceHelper(PrivateAccessChannelHelperCustom, PrivateAccessChannelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            vcn_id=dict(type="str"),
            subnet_id=dict(type="str"),
            private_source_dns_zones=dict(
                type="list",
                elements="dict",
                options=dict(
                    dns_zone=dict(type="str", required=True),
                    description=dict(type="str"),
                ),
            ),
            private_source_scan_hosts=dict(
                type="list",
                elements="dict",
                options=dict(
                    scan_hostname=dict(type="str", required=True),
                    scan_port=dict(type="int", required=True),
                    description=dict(type="str"),
                ),
            ),
            network_security_group_ids=dict(type="list", elements="str"),
            private_access_channel_key=dict(type="str", no_log=True),
            analytics_instance_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="private_access_channel",
        service_client_class=AnalyticsClient,
        namespace="analytics",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
