# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_config_utils,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False
import logging

logger = logging.getLogger(__name__)


class WaasCertificateHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            WaasCertificateHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # ignore the fields that are not available in the get model. The get model keeps the values parsed from the
        # certificate data and it might not be worth it to get into the certificate parsing in the ansible modules.
        for key in [
            "certificate_data",
            "private_key_data",
            "is_trust_verification_disabled",
        ]:
            create_model_dict.pop(key, None)
        return create_model_dict


class HttpRedirectHelperCustom:
    def get_waiter_client(self):
        # http_redirect resource has a separate client class but still uses WaasClient for work requests. Override
        # waiter client to use WaasClient.
        return oci_config_utils.create_service_client(self.module, WaasClient)


class WaasPolicyHelperCustom:
    def get_existing_resource_dict_for_update(self):
        existing_resource_dict = super(
            WaasPolicyHelperCustom, self
        ).get_existing_resource_dict_for_update()
        # good_bots, threat_feeds and protection_rules update works differently from other resources with list
        # attributes. In general, when a list attribute is updated the existing list is overwritten by the update but
        # in this case, update allows only a subset of items to be updated. Rest of the items will stay the same. But
        # the idempotence logic compares for exact match causing mismatches. So only compare the items which are being
        # updated.
        if (
            self.module.params.get("waf_config")
            and self.module.params.get("waf_config").get("good_bots")
            and existing_resource_dict.get("waf_config")
            and existing_resource_dict.get("waf_config").get("good_bots")
        ):
            good_bots_keys = [
                good_bot.get("key")
                for good_bot in self.module.params["waf_config"]["good_bots"]
            ]
            existing_resource_dict["waf_config"]["good_bots"] = [
                existing_resource
                for existing_resource in existing_resource_dict["waf_config"][
                    "good_bots"
                ]
                if existing_resource.get("key") in good_bots_keys
            ]
        if (
            self.module.params.get("waf_config")
            and self.module.params.get("waf_config").get("threat_feeds")
            and existing_resource_dict.get("waf_config")
            and existing_resource_dict.get("waf_config").get("threat_feeds")
        ):
            threat_feeds_keys = [
                threat_feed.get("key")
                for threat_feed in self.module.params["waf_config"]["threat_feeds"]
            ]
            existing_resource_dict["waf_config"]["threat_feeds"] = [
                existing_resource
                for existing_resource in existing_resource_dict["waf_config"][
                    "threat_feeds"
                ]
                if existing_resource.get("key") in threat_feeds_keys
            ]
        if (
            self.module.params.get("waf_config")
            and self.module.params.get("waf_config").get("protection_rules")
            and existing_resource_dict.get("waf_config")
            and existing_resource_dict.get("waf_config").get("protection_rules")
        ):
            protection_rules_keys = [
                protection_rule.get("key")
                for protection_rule in self.module.params["waf_config"][
                    "protection_rules"
                ]
            ]
            existing_resource_dict["waf_config"]["protection_rules"] = [
                existing_resource
                for existing_resource in existing_resource_dict["waf_config"][
                    "protection_rules"
                ]
                if existing_resource.get("key") in protection_rules_keys
            ]
        return existing_resource_dict


class WaasPolicyActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action == "accept_recommendations":
            if self.module.params.get("protection_rule_keys") is None:
                self.module.fail_json(
                    msg="protection_rule_keys required for accept_recommendations action"
                )
            if not self.module.params.get("protection_rule_keys"):
                return False
            if not resource.waf_config or not resource.waf_config.protection_rules:
                return True
            existing_protection_rules = resource.waf_config.protection_rules
            recommendations = oci_common_utils.call_with_backoff(
                self.client.list_recommendations, waas_policy_id=resource.id
            ).data
            for protection_rule_key in self.module.params.get("protection_rule_keys"):
                existing_protection_rule_for_key = None
                for existing_protection_rule in existing_protection_rules:
                    if existing_protection_rule.key == protection_rule_key:
                        existing_protection_rule_for_key = existing_protection_rule
                if not existing_protection_rule_for_key:
                    self.module.fail_json(
                        msg="Protection rule key {protection_rule_key} not found".format(
                            protection_rule_key=protection_rule_key
                        )
                    )
                recommendation_for_key = None
                for recommendation in recommendations:
                    if recommendation.key == protection_rule_key:
                        recommendation_for_key = recommendation
                        break
                if not recommendation_for_key:
                    # May be the recommendation is already accepted and it is not available. I have seen them lying
                    # around even when they are accepted. But not really sure how long they would be present in the
                    # recommendations once they are accepted. So depend on the service to do the right thing because
                    # without the recommendation we cannot really check if the existing state matches the intended
                    # state.
                    return True
                if (
                    recommendation_for_key.recommended_action
                    != existing_protection_rule_for_key.action
                ):
                    return True
            return False
        elif action == "purge_cache":
            if not resource.waf_config or not resource.waf_config.caching_rules:
                return False
            return True
        return super(WaasPolicyActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class WafConfigHelperCustom:
    def get_existing_resource_dict_for_update(self):
        existing_resource_dict = super(
            WafConfigHelperCustom, self
        ).get_existing_resource_dict_for_update()
        # good_bots, threat_feeds and protection_rules update works differently from other resources with list
        # attributes. In general, when a list attribute is updated the existing list is overwritten by the update but
        # in this case, update allows only a subset of items to be updated. Rest of the items will stay the same. But
        # the idempotence logic compares for exact match causing mismatches. So only compare the items which are being
        # updated.
        if self.module.params.get("good_bots") and existing_resource_dict.get(
            "good_bots"
        ):
            good_bots_keys = [
                good_bot.get("key") for good_bot in self.module.params["good_bots"]
            ]
            existing_resource_dict["good_bots"] = [
                existing_resource
                for existing_resource in existing_resource_dict["good_bots"]
                if existing_resource.get("key") in good_bots_keys
            ]
        if self.module.params.get("threat_feeds") and existing_resource_dict.get(
            "threat_feeds"
        ):
            threat_feeds_keys = [
                threat_feed.get("key")
                for threat_feed in self.module.params["threat_feeds"]
            ]
            existing_resource_dict["threat_feeds"] = [
                existing_resource
                for existing_resource in existing_resource_dict["threat_feeds"]
                if existing_resource.get("key") in threat_feeds_keys
            ]
        if self.module.params.get("protection_rules") and existing_resource_dict.get(
            "protection_rules"
        ):
            protection_rules_keys = [
                protection_rule.get("key")
                for protection_rule in self.module.params["protection_rules"]
            ]
            existing_resource_dict["protection_rules"] = [
                existing_resource
                for existing_resource in existing_resource_dict["protection_rules"]
                if existing_resource.get("key") in protection_rules_keys
            ]
        return existing_resource_dict


# Base class assume that the update model is a dictionary but most of the sub-resources (access_rules, captchas) operate
# on a list of items instead. So update necessary methods to handle list of items instead of a single item.
# TODO: Check if these can be handled in the base class
class AccessRulesHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            self.list_resources()
        )

    def is_update_necessary(self, existing_resources):
        update_model = self.get_update_model()
        access_rules = self.get_update_model_dict_for_idempotence_check(update_model)
        update_is_necessary = not oci_common_utils.compare_lists(
            access_rules, existing_resources
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.get_response_field_name(),
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary


class CaptchasHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            self.list_resources()
        )

    def is_update_necessary(self, existing_resources):
        update_model = self.get_update_model()
        captchas = self.get_update_model_dict_for_idempotence_check(update_model)
        update_is_necessary = not oci_common_utils.compare_lists(
            captchas, existing_resources
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.get_response_field_name(),
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary


class CachingRulesHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            self.list_resources()
        )

    def is_update_necessary(self, existing_resources):
        update_model = self.get_update_model()
        caching_rules = self.get_update_model_dict_for_idempotence_check(update_model)
        update_is_necessary = not oci_common_utils.compare_lists(
            caching_rules, existing_resources
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.resource_type,
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary


class GoodBotsHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            self.list_resources()
        )

    def is_update_necessary(self, existing_resources):
        update_model = self.get_update_model()
        good_bots = self.get_update_model_dict_for_idempotence_check(update_model)
        # Oracle has a pre-defined set of resources already defined. Update can only edit only some of them. So compare
        # only with the resources that are being modified.
        if existing_resources:
            good_bots_keys = [good_bot.get("key") for good_bot in good_bots]
            existing_resources = [
                existing_resource
                for existing_resource in existing_resources
                if existing_resource.get("key") in good_bots_keys
            ]
        update_is_necessary = not oci_common_utils.compare_lists(
            good_bots, existing_resources
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.resource_type,
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary


class ThreatFeedsHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            self.list_resources()
        )

    def is_update_necessary(self, existing_resources):
        update_model = self.get_update_model()
        threat_feeds = self.get_update_model_dict_for_idempotence_check(update_model)
        # Oracle has a pre-defined set of resources already defined. Update can only edit only some of them. So compare
        # only with the resources that are being modified.
        if existing_resources:
            threat_feeds_keys = [threat_feed.get("key") for threat_feed in threat_feeds]
            existing_resources = [
                existing_resource
                for existing_resource in existing_resources
                if existing_resource.get("key") in threat_feeds_keys
            ]
        update_is_necessary = not oci_common_utils.compare_lists(
            threat_feeds, existing_resources
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.resource_type,
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary


class ProtectionRulesFactsHelperCustom:
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_protection_rule,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            protection_rule_key=self.module.params.get("protection_rule_key"),
        )


class ProtectionRulesHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            self.list_resources()
        )

    def is_update_necessary(self, existing_resources):
        update_model = self.get_update_model()
        protection_rules = self.get_update_model_dict_for_idempotence_check(
            update_model
        )
        # Oracle has a pre-defined set of resources already defined. Update can only edit only some of them. So compare
        # only with the resources that are being modified.
        if existing_resources:
            protection_rules_keys = [
                protection_rule.get("key") for protection_rule in protection_rules
            ]
            existing_resources = [
                existing_resource
                for existing_resource in existing_resources
                if existing_resource.get("key") in protection_rules_keys
            ]
        update_is_necessary = not oci_common_utils.compare_lists(
            protection_rules, existing_resources
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.resource_type,
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary


class WaasPolicyCustomProtectionRulesHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            self.list_resources()
        )

    def is_update_necessary(self, existing_resources):
        update_model = self.get_update_model()
        custom_protection_rules = self.get_update_model_dict_for_idempotence_check(
            update_model
        )
        update_is_necessary = not oci_common_utils.compare_lists(
            custom_protection_rules, existing_resources
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.resource_type,
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary


class WhitelistsHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            self.list_resources()
        )

    def is_update_necessary(self, existing_resources):
        update_model = self.get_update_model()
        whitelists = self.get_update_model_dict_for_idempotence_check(update_model)
        update_is_necessary = not oci_common_utils.compare_lists(
            whitelists, existing_resources
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.resource_type,
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary
