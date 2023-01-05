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
module: oci_analytics_instance_facts
short_description: Fetches details about one or multiple AnalyticsInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AnalyticsInstance resources in Oracle Cloud Infrastructure
    - List Analytics instances.
    - If I(analytics_instance_id) is specified, the details of a single AnalyticsInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    analytics_instance_id:
        description:
            - The OCID of the AnalyticsInstance.
            - Required to get a specific analytics_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple analytics_instances.
        type: str
    name:
        description:
            - A filter to return only resources that match the given name exactly.
        type: str
    capacity_type:
        description:
            - A filter to only return resources matching the capacity type enum. Values are
              case-insensitive.
        type: str
        choices:
            - "OLPU_COUNT"
            - "USER_COUNT"
    feature_set:
        description:
            - A filter to only return resources matching the feature set. Values are
              case-insensitive.
        type: str
        choices:
            - "SELF_SERVICE_ANALYTICS"
            - "ENTERPRISE_ANALYTICS"
    lifecycle_state:
        description:
            - A filter to only return resources matching the lifecycle state. The state
              value is case-insensitive.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "DELETED"
            - "DELETING"
            - "FAILED"
            - "INACTIVE"
            - "UPDATING"
    sort_by:
        description:
            - The field to sort by (one column only). Default sort order is
              ascending exception of `timeCreated` column (descending).
        type: str
        choices:
            - "capacityType"
            - "capacityValue"
            - "featureSet"
            - "lifecycleState"
            - "name"
            - "timeCreated"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific analytics_instance
  oci_analytics_instance_facts:
    # required
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List analytics_instances
  oci_analytics_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    capacity_type: OLPU_COUNT
    feature_set: SELF_SERVICE_ANALYTICS
    lifecycle_state: ACTIVE
    sort_by: capacityType
    sort_order: ASC

"""

RETURN = """
analytics_instances:
    description:
        - List of AnalyticsInstance resources
    returned: on success
    type: complex
    contains:
        private_access_channels:
            description:
                - Map of PrivateAccessChannel unique identifier key as KEY and PrivateAccessChannel Object as VALUE.
                - Returned for get operation
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
        vanity_url_details:
            description:
                - Map of VanityUrl unique identifier key as KEY and VanityUrl Object as VALUE.
                - Returned for get operation
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
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        kms_key_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the OCI Vault Key encrypting the customer data stored in
                  this Analytics instance. A null value indicates Oracle managed default encryption.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
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
                network_security_group_ids:
                    description:
                        - Network Security Group OCIDs for an Analytics instance.
                    returned: on success
                    type: list
                    sample: []
                network_endpoint_type:
                    description:
                        - The type of network endpoint.
                    returned: on success
                    type: str
                    sample: PUBLIC
                whitelisted_ips:
                    description:
                        - Source IP addresses or IP address ranges in ingress rules.
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
                                - Source IP addresses or IP address ranges in ingress rules.
                            returned: on success
                            type: list
                            sample: []
                whitelisted_services:
                    description:
                        - Oracle Cloud Services that are allowed to access this Analytics instance.
                    returned: on success
                    type: list
                    sample: []
        service_url:
            description:
                - URL of the Analytics service.
            returned: on success
            type: str
            sample: service_url_example
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
    sample: [{
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
            }],
            "private_source_scan_hosts": [{
                "scan_hostname": "scan_hostname_example",
                "scan_port": 56,
                "description": "description_example"
            }],
            "network_security_group_ids": []
        },
        "vanity_url_details": {
            "key": "key_example",
            "description": "description_example",
            "urls": [],
            "hosts": [],
            "public_certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        },
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
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
            "network_security_group_ids": [],
            "network_endpoint_type": "PUBLIC",
            "whitelisted_ips": [],
            "whitelisted_vcns": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "whitelisted_ips": []
            }],
            "whitelisted_services": []
        },
        "service_url": "service_url_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.analytics import AnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AnalyticsInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "analytics_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_analytics_instance,
            analytics_instance_id=self.module.params.get("analytics_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "capacity_type",
            "feature_set",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_analytics_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AnalyticsInstanceFactsHelperCustom = get_custom_class(
    "AnalyticsInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    AnalyticsInstanceFactsHelperCustom, AnalyticsInstanceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            analytics_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            capacity_type=dict(type="str", choices=["OLPU_COUNT", "USER_COUNT"]),
            feature_set=dict(
                type="str", choices=["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]
            ),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "DELETED",
                    "DELETING",
                    "FAILED",
                    "INACTIVE",
                    "UPDATING",
                ],
            ),
            sort_by=dict(
                type="str",
                choices=[
                    "capacityType",
                    "capacityValue",
                    "featureSet",
                    "lifecycleState",
                    "name",
                    "timeCreated",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="analytics_instance",
        service_client_class=AnalyticsClient,
        namespace="analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(analytics_instances=result)


if __name__ == "__main__":
    main()
