# Copyright (c) 2020 Oracle and/or its affiliates.
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

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class SecurityRuleActionsHelperCustom:
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
        if action == "add_network_security_group_security_rules":
            action_idempotency_checks_fn = (
                self._add_network_security_group_rules_idempotency_check
            )
            check_mode_response_resource = to_dict(
                AddedNetworkSecurityGroupSecurityRules(security_rules=[])
            )
        elif action == "update_network_security_group_security_rules":
            action_idempotency_checks_fn = (
                self._update_network_security_group_rules_idempotency_check
            )
            check_mode_response_resource = to_dict(
                UpdatedNetworkSecurityGroupSecurityRules(security_rules=[])
            )
        elif action == "remove_network_security_group_security_rules":
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
    def is_action_necessary(self, action):
        service_id = self.module.params.get("service_id")
        if not service_id:
            return False
        existing_service_ids = [
            service.service_id for service in self.get_resource().data.services
        ]
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
    def is_action_necessary(self, action):
        this_lpg = self.get_resource().data
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
    def is_action_necessary(self, action):
        this_rpc = self.get_resource().data
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
                resource=to_dict(existing_public_prefixes),
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
                resource=to_dict(existing_public_prefixes),
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
