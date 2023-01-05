# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

"""This module contains all the customisations for network load balancer modules."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class NetworkLoadBalancerHelperCustom:

    # adding this customization to support idempotency for create operation.
    # The api returns ip_addresses ID's inside ip_addresses attribute.
    # In the module params we have the ip_adresses ID's in reserved_ip attribute.
    # So we are copying the ip_addresses into new attribute reserved_ip for idempotency comparision.
    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        resource_dict = super(
            NetworkLoadBalancerHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)
        if self.module.params.get("reserved_ips"):
            reserved_ips = []
            for ip_address in resource_dict.get("ip_addresses"):
                reserved_ips.append(ip_address.get("reserved_ip"))
            resource_dict["reserved_ips"] = reserved_ips
        return resource_dict


class NetworkLoadBalancerBackendHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        name = module.params.get("name")
        if name is None:
            name = "{ip_address}:{port}".format(
                ip_address=module.params.get("ip_address"),
                port=module.params.get("port"),
            )
        module.params["backend_name"] = name
        module.params["name"] = name
        super(NetworkLoadBalancerBackendHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )


class NetworkLoadBalancerNetworkSecurityGroupsUpdateHelperCustom:
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_load_balancer,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
        )


# This method returns the list of resource data in the network_load_balancer for a given resource
def list_resource_from_network_load_balancer(self, resource):
    network_load_balancer = oci_common_utils.call_with_backoff(
        self.client.get_network_load_balancer,
        network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
    ).data
    resource_dict = getattr(network_load_balancer, resource, None)
    if resource_dict:
        return list(resource_dict.values())
    return []


def resource_from_network_load_balancer_as_dict(self, resource):
    network_load_balancer = oci_common_utils.call_with_backoff(
        self.client.get_network_load_balancer,
        network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
    ).data
    resource_dict = getattr(network_load_balancer, resource, None)
    return resource_dict
