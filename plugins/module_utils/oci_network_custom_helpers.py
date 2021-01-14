# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict
    from oci.core.models import (
        AddedNetworkSecurityGroupSecurityRules,
        UpdatedNetworkSecurityGroupSecurityRules,
        BulkAddVirtualCircuitPublicPrefixesDetails,
        BulkDeleteVirtualCircuitPublicPrefixesDetails,
    )
    from oci.core.models.get_public_ip_by_private_ip_id_details import (
        GetPublicIpByPrivateIpIdDetails,
    )
    from oci.core.models.get_public_ip_by_ip_address_details import (
        GetPublicIpByIpAddressDetails,
    )

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


logger = oci_common_utils.get_logger("oci_network_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class NetworkSecurityGroupSecurityRuleActionsHelperCustom:
    ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES_ACTION = "add"
    UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES_ACTION = "update"
    REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES_ACTION = "remove"

    def _add_network_security_group_rules_idempotency_check(self):
        existing_security_rules = self.list_security_rules()
        provided_security_rules = self.module.params.get("security_rules", [])
        provided_security_rules_to_add = []

        existing_security_rules_as_dicts = [
            to_dict(security_rule) for security_rule in existing_security_rules
        ]

        for provided_security_rule in provided_security_rules:
            if not oci_common_utils.is_in_list(
                existing_security_rules_as_dicts, element=provided_security_rule
            ):
                provided_security_rules_to_add.append(provided_security_rule)

        if len(provided_security_rules_to_add) == 0:
            resource = AddedNetworkSecurityGroupSecurityRules(
                security_rules=self.list_security_rules()
            )
            return oci_common_utils.get_result(
                changed=False,
                resource_type=self.resource_type,
                resource=to_dict(resource),
            )
        else:
            self.module.params["security_rules"] = provided_security_rules_to_add

    def _update_network_security_group_rules_idempotency_check(self):
        existing_security_rules = self.list_security_rules()
        provided_security_rules = self.module.params.get("security_rules", [])

        existing_security_rules_as_dicts = [
            to_dict(security_rule) for security_rule in existing_security_rules
        ]

        all_rules_to_update_already_exist_and_match = True
        for provided_security_rule in provided_security_rules:
            if not oci_common_utils.is_in_list(
                existing_security_rules_as_dicts, element=provided_security_rule
            ):
                all_rules_to_update_already_exist_and_match = False

        if all_rules_to_update_already_exist_and_match:
            resource = UpdatedNetworkSecurityGroupSecurityRules(
                security_rules=self.list_security_rules()
            )
            return oci_common_utils.get_result(
                changed=False,
                resource_type=self.resource_type,
                resource=to_dict(resource),
            )

    def _remove_network_security_group_rules_idempotency_check(self):
        existing_security_rules = self.list_security_rules()
        provided_security_rule_ids_to_delete = self.module.params.get(
            "security_rule_ids", []
        )
        security_rule_ids_to_delete = []
        for existing_security_rule in existing_security_rules:
            if existing_security_rule.id in provided_security_rule_ids_to_delete:
                security_rule_ids_to_delete.append(existing_security_rule.id)

        if len(security_rule_ids_to_delete) == 0:
            # RemoveNetworkSecurityGroupSecurityRules returns nothing, but in order to keep return type consistent
            # across add / remove / delete, we choose to return UpdatedNetworkSecurityGroupSecurityRules with an
            # empty 'security_rules' list
            resource = UpdatedNetworkSecurityGroupSecurityRules(
                security_rules=self.list_security_rules()
            )
            return oci_common_utils.get_result(
                changed=False,
                resource_type=self.resource_type,
                resource=to_dict(resource),
            )
        else:
            self.module.params["security_rule_ids"] = security_rule_ids_to_delete

    def perform_action(self, action):

        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))

        # the idempotency checks for these actions are custom since we aren't doing the regular
        # check for existence, we are checking if a requested resource is present within a list
        if action == self.ADD_NETWORK_SECURITY_GROUP_SECURITY_RULES_ACTION:
            action_idempotency_checks_fn = (
                self._add_network_security_group_rules_idempotency_check
            )
            check_mode_response_resource = to_dict(
                AddedNetworkSecurityGroupSecurityRules(security_rules=[])
            )
        elif action == self.UPDATE_NETWORK_SECURITY_GROUP_SECURITY_RULES_ACTION:
            action_idempotency_checks_fn = (
                self._update_network_security_group_rules_idempotency_check
            )
            check_mode_response_resource = to_dict(
                UpdatedNetworkSecurityGroupSecurityRules(security_rules=[])
            )
        elif action == self.REMOVE_NETWORK_SECURITY_GROUP_SECURITY_RULES_ACTION:
            action_idempotency_checks_fn = (
                self._remove_network_security_group_rules_idempotency_check
            )
            # RemoveNetworkSecurityGroupSecurityRules returns nothing, but in order to keep return type consistent
            # across add / remove / delete, we choose to return UpdatedNetworkSecurityGroupSecurityRules with an
            # empty 'security_rules' list
            check_mode_response_resource = to_dict(
                UpdatedNetworkSecurityGroupSecurityRules(security_rules=[])
            )
        else:
            self.module.fail_json(
                msg="Performing action failed for unrecognized action: {0}".format(
                    action
                )
            )

        result = action_idempotency_checks_fn()
        if result:
            return result

        if self.check_mode:
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=check_mode_response_resource,
            )

        try:
            action_fn()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            # - the individual action operations return the rules that were acted on (except REMOVE which returns nothing)
            #   to keep consistent with patterns in other modules, we override here to return the current set of all rules
            # - in order to return the same format as the generated docs for actions operations (result.security_rule.security_rules)
            #    we use AddedNetworkSecurityGroupSecurityRules here as a wrapper
            resource = AddedNetworkSecurityGroupSecurityRules(
                security_rules=self.list_security_rules()
            )
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(resource),
            )

    def list_security_rules(self):
        optional_list_method_params = ["direction", "sort_by", "sort_order"]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_network_security_group_security_rules,
            network_security_group_id=self.module.params.get(
                "network_security_group_id"
            ),
            **optional_kwargs
        )


class ServiceGatewayActionsHelperCustom:
    def is_action_necessary(self, action, resource):
        service_id = self.module.params.get("service_id")
        if not service_id:
            return False
        existing_service_ids = [service.service_id for service in resource.services]
        if action == "attach_service_id":
            if service_id in existing_service_ids:
                return False
            return True
        elif action == "detach_service_id":
            if service_id not in existing_service_ids:
                return False
            return True
        return True


class LocalPeeringGatewayActionsHelperCustom:
    def is_action_necessary(self, action, resource):
        this_lpg = resource
        peer_lpg = self.client.get_local_peering_gateway(
            local_peering_gateway_id=self.module.params.get("peer_id")
        ).data

        this_vcn = self.client.get_vcn(vcn_id=this_lpg.vcn_id).data
        peer_vcn = self.client.get_vcn(vcn_id=peer_lpg.vcn_id).data

        if (
            this_lpg.peering_status == "PEERED"
            and this_lpg.peer_advertised_cidr == peer_vcn.cidr_block
        ) and (
            peer_lpg.peering_status == "PEERED"
            and peer_lpg.peer_advertised_cidr == this_vcn.cidr_block
        ):
            return False

        return True


class RemotePeeringConnectionActionsHelperCustom:
    def is_action_necessary(self, action, resource):
        this_rpc = resource
        if (
            this_rpc.peering_status == "PEERED"
            and this_rpc.peer_id == self.module.params.get("peer_id")
        ):
            return False
        return True


class CrossConnectGroupHelperCustom:
    # The cross connect group does not come to an active state. So override the end states for create operation.
    def get_resource_active_states(self):
        return ["INACTIVE", "PROVISIONED"]


class CrossConnectHelperCustom:
    def get_resource_active_states(self):
        return ["PENDING_CUSTOMER", "PENDING_PROVIDER", "PROVISIONED"]


class VirtualCircuitHelperCustom:
    def get_exclude_attributes(self):
        return super(VirtualCircuitHelperCustom, self).get_exclude_attributes() + [
            "public_prefixes",
        ]


class VirtualCircuitActionsHelperCustom:
    def _bulk_add_virtual_circuit_public_prefixes_idempotency_check(self):
        existing_public_prefixes = self.list_public_prefixes()
        existing_public_prefix_cidrs = [
            existing_public_prefix.cidr_block
            for existing_public_prefix in existing_public_prefixes
        ]
        provided_public_prefixes = self.module.params.get("public_prefixes", [])
        public_prefixes_to_add = [
            public_prefix
            for public_prefix in provided_public_prefixes
            if public_prefix.get("cidr_block") not in existing_public_prefix_cidrs
        ]

        if len(public_prefixes_to_add) == 0:
            return oci_common_utils.get_result(
                changed=False,
                resource_type=self.resource_type,
                resource=to_dict(
                    BulkAddVirtualCircuitPublicPrefixesDetails(
                        public_prefixes=existing_public_prefixes
                    )
                ),
            )
        else:
            self.module.params["public_prefixes"] = public_prefixes_to_add

    def _bulk_delete_virtual_circuit_public_prefixes_idempotency_check(self):
        existing_public_prefixes = self.list_public_prefixes()
        existing_public_prefix_cidrs = [
            existing_public_prefix.cidr_block
            for existing_public_prefix in existing_public_prefixes
        ]
        provided_public_prefixes = self.module.params.get("public_prefixes", [])
        public_prefixes_to_delete = [
            public_prefix
            for public_prefix in provided_public_prefixes
            if public_prefix.get("cidr_block") in existing_public_prefix_cidrs
        ]

        if len(public_prefixes_to_delete) == 0:
            return oci_common_utils.get_result(
                changed=False,
                resource_type=self.resource_type,
                resource=to_dict(
                    BulkAddVirtualCircuitPublicPrefixesDetails(
                        public_prefixes=existing_public_prefixes
                    )
                ),
            )
        else:
            self.module.params["public_prefixes"] = public_prefixes_to_delete

    def perform_action(self, action):

        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))

        # the idempotency checks for these actions are custom since we aren't doing the regular
        # check for existence, we are checking if a requested resource is present within a list
        if action == "bulk_add_virtual_circuit_public_prefixes":
            action_idempotency_checks_fn = (
                self._bulk_add_virtual_circuit_public_prefixes_idempotency_check
            )
            check_mode_response_resource = to_dict(
                BulkAddVirtualCircuitPublicPrefixesDetails(public_prefixes=[])
            )
        elif action == "bulk_delete_virtual_circuit_public_prefixes":
            action_idempotency_checks_fn = (
                self._bulk_delete_virtual_circuit_public_prefixes_idempotency_check
            )
            check_mode_response_resource = to_dict(
                BulkDeleteVirtualCircuitPublicPrefixesDetails(public_prefixes=[])
            )
        else:
            self.module.fail_json(
                msg="Performing action failed for unrecognized action: {0}".format(
                    action
                )
            )

        result = action_idempotency_checks_fn()
        if result:
            return result

        if self.check_mode:
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=check_mode_response_resource,
            )

        try:
            action_fn()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            # the individual action operations return None. So get the final list of public prefixes
            # and return them.
            resource = BulkAddVirtualCircuitPublicPrefixesDetails(
                public_prefixes=self.list_public_prefixes()
            )
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(resource),
            )

    def list_public_prefixes(self):
        return oci_common_utils.list_all_resources(
            self.client.list_virtual_circuit_public_prefixes,
            virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
        )


class IpSecConnectionTunnelHelperCustom:
    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            IpSecConnectionTunnelHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        key_mapping = (
            lambda arg: "bgp_session_info" if arg == "bgp_session_config" else arg
        )
        return dict((key_mapping(k), v) for k, v in update_model_dict.items())


class PublicIpFactsHelperCustom:
    def is_get(self):
        if super(PublicIpFactsHelperCustom, self).is_get():
            return True
        if self.module.params["private_ip_id"] or self.module.params["ip_address"]:
            return True
        return False

    def get_resource(self):
        if self.module.params["public_ip_id"]:
            return super(PublicIpFactsHelperCustom, self).get_resource()
        # Getting public_ip using private_ip_id and ip_address in the API are action operations. But it is a little
        # twisted to think of them as action operations in ansible context (also in general as well). So adding those to
        # the facts module where they really belong.
        if self.module.params["private_ip_id"]:
            return oci_common_utils.call_with_backoff(
                self.client.get_public_ip_by_private_ip_id,
                get_public_ip_by_private_ip_id_details=oci_common_utils.convert_input_data_to_model_class(
                    self.module.params, GetPublicIpByPrivateIpIdDetails
                ),
            )
        if self.module.params["ip_address"]:
            return oci_common_utils.call_with_backoff(
                self.client.get_public_ip_by_ip_address,
                get_public_ip_by_ip_address_details=oci_common_utils.convert_input_data_to_model_class(
                    self.module.params, GetPublicIpByIpAddressDetails
                ),
            )


class SecurityListHelperCustom:
    def __init__(self, *args, **kwargs):
        super(SecurityListHelperCustom, self).__init__(*args, **kwargs)
        try:
            # since the purge and delete options have default values we cannot check directly if a user has provided
            # value for it or not. _load_params returns only the params that user has provided.
            from ansible.module_utils.basic import _load_params

            user_provided_params = _load_params()
            if (
                user_provided_params.get("purge_security_rules") is not None
                and user_provided_params.get("delete_security_rules") is not None
            ):
                self.module.fail_json(
                    msg="purge_security_rules and delete_security_rules are mutually exclusive"
                )
        except Exception as ex:
            _debug(
                "Error checking the load params for purge and delete validation: {0}. Skipping validation.".format(
                    str(ex)
                )
            )
            pass

    def get_update_model(self):
        update_model = super(SecurityListHelperCustom, self).get_update_model()
        existing_security_list = self.get_resource().data
        existing_ingress_security_rules = existing_security_list.ingress_security_rules
        existing_ingress_security_rules_dict = to_dict(existing_ingress_security_rules)
        existing_egress_security_rules = existing_security_list.egress_security_rules
        existing_egress_security_rules_dict = to_dict(existing_egress_security_rules)
        if self.module.params.get("purge_security_rules") is False:
            if existing_ingress_security_rules:
                update_model.ingress_security_rules = (
                    update_model.ingress_security_rules or []
                )
                update_model.ingress_security_rules = (
                    existing_ingress_security_rules
                    + [
                        security_rule
                        for security_rule in update_model.ingress_security_rules
                        if not oci_common_utils.is_in_list(
                            existing_ingress_security_rules_dict, to_dict(security_rule)
                        )
                    ]
                )
            if existing_egress_security_rules:
                update_model.egress_security_rules = (
                    update_model.egress_security_rules or []
                )
                update_model.egress_security_rules = existing_egress_security_rules + [
                    security_rule
                    for security_rule in update_model.egress_security_rules
                    if not oci_common_utils.is_in_list(
                        existing_egress_security_rules_dict, to_dict(security_rule)
                    )
                ]
        elif self.module.params.get("delete_security_rules") is True:
            if update_model.ingress_security_rules is None:
                update_model.ingress_security_rules = existing_ingress_security_rules
            else:
                existing_ingress_security_rules = existing_ingress_security_rules or []
                update_model.ingress_security_rules = [
                    existing_security_rule
                    for existing_security_rule in existing_ingress_security_rules
                    if not any(
                        [
                            oci_common_utils.compare_dicts(
                                to_dict(security_rule), to_dict(existing_security_rule)
                            )
                            for security_rule in update_model.ingress_security_rules
                        ]
                    )
                ]
            if update_model.egress_security_rules is None:
                update_model.egress_security_rules = existing_egress_security_rules
            else:
                existing_egress_security_rules = existing_egress_security_rules or []
                update_model.egress_security_rules = [
                    existing_security_rule
                    for existing_security_rule in existing_egress_security_rules
                    if not any(
                        [
                            oci_common_utils.compare_dicts(
                                to_dict(security_rule), to_dict(existing_security_rule)
                            )
                            for security_rule in update_model.egress_security_rules
                        ]
                    )
                ]
        return update_model


def patch_base_client_call_api(client):
    if not client:
        return
    if not hasattr(client, "base_client"):
        return
    if not hasattr(client.base_client, "call_api"):
        return
    original_call_api = client.base_client.call_api

    def call_api(*args, **kwargs):
        header_params = kwargs.pop("header_params", {})
        _debug(header_params)
        for header_key in header_params:
            if (
                header_key == "accept"
                and header_params[header_key] == "text/plain; charset&#x3D;utf-8"
            ):
                header_params[header_key] = "*/*"
        _debug(header_params)
        return original_call_api(*args, header_params=header_params, **kwargs)

    client.base_client.call_api = call_api


class CpeConfigContentFactsHelperCustom:
    def __init__(self, *args, **kwargs):
        super(CpeConfigContentFactsHelperCustom, self).__init__(*args, **kwargs)
        # Currently the server throws an error with the default Accept header added by the SDK. But if we remove the
        # charset parameter from the header, it works fine.
        # TODO: Remove this once the issue with API is fixed
        patch_base_client_call_api(self.client)


class IpSecConnectionCpeConfigContentFactsHelperCustom:
    def __init__(self, *args, **kwargs):
        super(IpSecConnectionCpeConfigContentFactsHelperCustom, self).__init__(
            *args, **kwargs
        )
        # Currently the server throws an error with the default Accept header added by the SDK. But if we remove the
        # charset parameter from the header, it works fine.
        # TODO: Remove this once the issue with API is fixed
        patch_base_client_call_api(self.client)


class IpSecConnectionTunnelCpeDeviceConfigHelperCustom:
    def get_update_model_dict_for_idempotence_check(self, update_model):
        # The device config param has different names in update model (tunnel_cpe_device_config) and get model
        # (tunnel_cpe_device_config_parameter). So update the name in the update model for idempotence logic to work.
        update_model_dict = to_dict(update_model)
        update_model_dict["tunnel_cpe_device_config_parameter"] = update_model_dict.pop(
            "tunnel_cpe_device_config", None
        )
        return update_model_dict


class IpSecConnectionTunnelCpeDeviceConfigContentFactsHelperCustom:
    def __init__(self, *args, **kwargs):
        super(
            IpSecConnectionTunnelCpeDeviceConfigContentFactsHelperCustom, self
        ).__init__(*args, **kwargs)
        # Currently the server throws an error with the default Accept header added by the SDK. But if we remove the
        # charset parameter from the header, it works fine.
        # TODO: Remove this once the issue with API is fixed
        patch_base_client_call_api(self.client)


class PublicIpPoolActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action == "add_public_ip_pool_capacity":
            if (
                resource.cidr_blocks
                and self.module.params.get("cidr_block") in resource.cidr_blocks
            ):
                return False
            return True
        elif action == "remove_public_ip_pool_capacity":
            if (
                resource.cidr_blocks
                and self.module.params.get("cidr_block") in resource.cidr_blocks
            ):
                return True
            return False
        return super(PublicIpPoolActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class ByoipRangeActionsHelperCustom:
    LIFECYCLE_DETAILS_ACTIVE = "ACTIVE"
    LIFECYCLE_DETAILS_PROVISIONED = "PROVISIONED"

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action == "advertise":
            if (
                resource.lifecycle_state == self.LIFECYCLE_DETAILS_ACTIVE
                and resource.lifecycle_details == self.LIFECYCLE_DETAILS_ACTIVE
            ):
                return False
            return True
        elif action == "withdraw":
            if (
                resource.lifecycle_state == self.LIFECYCLE_DETAILS_ACTIVE
                and resource.lifecycle_details == self.LIFECYCLE_DETAILS_ACTIVE
            ):
                return True
            return False
        elif action == "validate":
            if (
                resource.lifecycle_state == self.LIFECYCLE_DETAILS_ACTIVE
                and resource.lifecycle_details == self.LIFECYCLE_DETAILS_PROVISIONED
            ):
                return False
            return False
        super(ByoipRangeActionsHelperCustom, self).is_action_necessary(action, resource)


class VcnActionsHelperCustom:
    ADD_VCN_CIDR_ACTION = "add_vcn_cidr"
    MODIFY_VCN_CIDR_ACTION = "modify_vcn_cidr"
    REMOVE_VCN_CIDR_ACTION = "remove_vcn_cidr"

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action == self.ADD_VCN_CIDR_ACTION:
            if self.module.params.get("cidr_block") in resource.cidr_blocks:
                return False
            return True
        elif action == self.MODIFY_VCN_CIDR_ACTION:
            if (
                self.module.params.get("original_cidr_block")
                not in resource.cidr_blocks
                and self.module.params.get("new_cidr_block") in resource.cidr_blocks
            ):
                return False
            return True
        elif action == self.REMOVE_VCN_CIDR_ACTION:
            if self.module.params.get("cidr_block") not in resource.cidr_blocks:
                return False
            return True

        return super(VcnActionsHelperCustom, self).is_action_necessary(action, resource)
