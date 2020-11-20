# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = oci_common_utils.get_logger("oci_blockchain_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class BlockchainPlatformHelperCustom:
    def get_exclude_attributes(self):
        exclude_attributes = super(
            BlockchainPlatformHelperCustom, self
        ).get_exclude_attributes()
        # These attributes are used for authentication and not really representative of the resource itself except maybe
        # ca_cert_archive_text but it is not available in the get model and there is no way for us to compare it with
        # the existing resource.
        exclude_attributes += [
            "idcs_access_token",
            "federated_user_id",
            "ca_cert_archive_text",
        ]
        return exclude_attributes

    def get_entity_type(self):
        return "instance"

    def get_default_module_wait_timeout(self):
        return 2400


class BlockchainPlatformActionsHelperCustom:
    def get_action_idempotent_states(self, action):
        if action.upper() == "START":
            return ["ACTIVE"]
        if action.upper() == "STOP":
            return ["INACTIVE"]
        return oci_common_utils.ACTION_IDEMPOTENT_STATES.get(action.upper(), [])

    def get_action_desired_states(self, action):
        if action.upper() == "START":
            return ["ACTIVE"]
        if action.upper() == "STOP":
            return ["INACTIVE"]
        return oci_common_utils.ACTION_DESIRED_STATES.get(
            action.upper(), oci_common_utils.DEFAULT_READY_STATES
        )


class BlockchainPlatformOsnHelperCustom:
    # The create operation is not idempotent since it is valid to have multiple nodes with the given values and there is
    # no way for us to distinguish if the user wants to create another or not.
    def get_matching_resource(self):
        return None

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_osn,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            osn_id=summary_model.osn_key,
        ).data

    def get_entity_type(self):
        return "instance"

    def create_resource(self):
        # Create operation waits on work request and does not return the identifier of the osn created. So we will
        # have to compare before and after to fetch the newly created osn
        before_osns = self.list_resources()
        _debug("Osns before create: {0}".format(to_dict(before_osns)))
        super(BlockchainPlatformOsnHelperCustom, self).create_resource()
        after_osns = self.list_resources()
        _debug("Osns after create: {0}".format(to_dict(after_osns)))
        created_osn = difference(after_osns, before_osns, key="osn_key")
        if not created_osn or len(created_osn) > 1:
            self.module.fail_json(msg="Error fetching the created Osn resource.")
        return oci_common_utils.call_with_backoff(
            self.client.get_osn,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            osn_id=created_osn[0].osn_key,
        ).data

    def get_get_fn(self):
        # This is just a dummy function so that the waiting logic does not thrown an error. The work request does not
        # return the Osn resource. So we will have to fetch it by comparing the pre and post list of Osn resources.
        # That is handled in the respective operation methods.
        def get_fn(osn_id):
            return oci_common_utils.get_default_response_from_resource(resource=None)

        return get_fn


class BlockchainPlatformPeerHelperCustom:
    # The create operation is not idempotent since it is valid to have multiple nodes with the given values and there is
    # no way for us to distinguish if the user wants to create another or not.
    def get_matching_resource(self):
        return None

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_peer,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            peer_id=summary_model.peer_key,
        ).data

    def get_entity_type(self):
        return "instance"

    def create_resource(self):
        # Create operation waits on work request and does not return the identifier of the osn created. So we will
        # have to compare before and after to fetch the newly created osn
        before_peers = self.list_resources()
        _debug("Peers before create: {0}".format(to_dict(before_peers)))
        super(BlockchainPlatformPeerHelperCustom, self).create_resource()
        after_peers = self.list_resources()
        _debug("Peers after create: {0}".format(to_dict(after_peers)))
        created_peer = difference(after_peers, before_peers, key="peer_key")
        if not created_peer or len(created_peer) > 1:
            self.module.fail_json(msg="Error fetching the created Peer resource.")
        return oci_common_utils.call_with_backoff(
            self.client.get_peer,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            peer_id=created_peer[0].peer_key,
        ).data

    def get_get_fn(self):
        # This is just a dummy function so that the waiting logic does not thrown an error. The work request does not
        # return the Osn resource. So we will have to fetch it by comparing the pre and post list of Osn resources.
        # That is handled in the respective operation methods.
        def get_fn(osn_id):
            return oci_common_utils.get_default_response_from_resource(resource=None)

        return get_fn


def difference(resources, other_resources, key):
    """Compare using key and return entries from resources which are not present in other_resources"""
    other_resources_keys = [
        getattr(other_resource, key, None) for other_resource in other_resources
    ]
    return [
        resource
        for resource in resources
        if getattr(resource, key, None) not in other_resources_keys
    ]
