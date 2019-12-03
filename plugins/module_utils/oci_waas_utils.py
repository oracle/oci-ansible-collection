# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.oracle import oci_utils

try:
    from oci.util import to_dict
    from oci.waas.models import (
        CreateWaasPolicyDetails,
        Origin,
        Header,
        PolicyConfig,
        WafConfigDetails,
        WafConfig,
        AccessRule,
        AccessRuleCriteria,
        AddressRateLimiting,
        Captcha,
        DeviceFingerprintChallenge,
        GoodBot,
        BlockChallengeSettings,
        HumanInteractionChallenge,
        JsChallenge,
        ProtectionRule,
        ProtectionRuleExclusion,
        ProtectionSettings,
        Whitelist,
        ThreatFeed,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = oci_utils.get_logger("oci_waas_utils")


def get_waas_origins(module):
    if not module.params.get("origins"):
        return None
    origins = dict()
    for origin_name in module.params["origins"]:
        origin_dict = module.params["origins"][origin_name]
        origin = get_model_from_dict(
            Origin, origin_dict, ["http_port", "https_port", "uri"]
        )
        if origin_dict.get("custom_headers"):
            origin.custom_headers = []
            for header_dict in origin_dict["custom_headers"]:
                header = get_model_from_dict(Header, header_dict, ["name", "value"])
                origin.custom_headers.append(header)

        origins[origin_name] = origin
    return origins


def get_waas_policy_config(module):
    if not module.params.get("policy_config"):
        return None
    return get_model_from_dict(
        PolicyConfig,
        module.params.get("policy_config"),
        ["certificate_id", "is_https_enabled", "is_https_forced"],
    )


def get_waf_config_access_rules(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("access_rules"):
        return None
    waf_config_dict_access_rules = waf_config_dict["access_rules"]
    access_rules = []
    for access_rule_dict in waf_config_dict_access_rules:
        access_rule = get_model_from_dict(
            AccessRule,
            access_rule_dict,
            [
                "name",
                "action",
                "block_action",
                "block_response_code",
                "block_error_page_message",
                "block_error_page_code",
                "block_error_page_description",
            ],
        )
        if "criteria" in access_rule_dict and access_rule_dict["criteria"]:
            criteria = []
            for access_rule_criteria_dict in access_rule_dict["criteria"]:
                access_rule_criteria = get_model_from_dict(
                    AccessRuleCriteria,
                    access_rule_criteria_dict,
                    ["condition", "value"],
                )
                criteria.append(access_rule_criteria)
            setattr(access_rule, "criteria", criteria)
        access_rules.append(access_rule)
    return access_rules


def get_waf_config_address_rate_limiting(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("address_rate_limiting"):
        return None
    return get_model_from_dict(
        AddressRateLimiting,
        waf_config_dict["address_rate_limiting"],
        [
            "allowed_rate_per_address",
            "block_response_code",
            "is_enabled",
            "max_delayed_count_per_address",
        ],
    )


def get_waf_config_captchas(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("captchas"):
        return None
    waf_config_dict_captchas = waf_config_dict["captchas"]
    captchas = []
    for captcha_dict in waf_config_dict_captchas:
        captcha = get_model_from_dict(
            Captcha,
            captcha_dict,
            [
                "url",
                "session_expiration_in_seconds",
                "title",
                "header_text",
                "footer_text",
                "failure_message",
                "submit_label",
            ],
        )
        captchas.append(captcha)
    return captchas


def get_waf_config_device_fingerprint_challenge(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("device_fingerprint_challenge"):
        return None
    device_fingerprint_challenge_dict = waf_config_dict["device_fingerprint_challenge"]
    device_fingerprint_challenge = get_model_from_dict(
        DeviceFingerprintChallenge,
        device_fingerprint_challenge_dict,
        [
            "is_enabled",
            "action",
            "failure_threshold",
            "action_expiration_in_seconds",
            "failure_threshold_expiration_in_seconds",
            "max_address_count",
            "max_address_count_expiration_in_seconds",
        ],
    )
    if (
        "challenge_settings" in device_fingerprint_challenge_dict
        and device_fingerprint_challenge_dict["challenge_settings"]
    ):
        challenge_settings_dict = device_fingerprint_challenge_dict[
            "challenge_settings"
        ]
        challenge_settings = get_model_from_dict(
            BlockChallengeSettings,
            challenge_settings_dict,
            [
                "block_action",
                "block_response_code",
                "block_error_page_message",
                "block_error_page_description",
                "block_error_page_code",
                "captcha_title",
                "captcha_header",
                "captcha_footer",
                "captcha_submit_label",
            ],
        )
        setattr(device_fingerprint_challenge, "challenge_settings", challenge_settings)
    return device_fingerprint_challenge


def get_waf_config_good_bots(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("good_bots"):
        return None
    waf_config_dict_good_bots = waf_config_dict["good_bots"]
    good_bots = []
    for good_bot_dict in waf_config_dict_good_bots:
        good_bot = get_model_from_dict(
            GoodBot, good_bot_dict, ["description", "is_enabled", "key", "name"]
        )
        good_bots.append(good_bot)
    return good_bots


def get_waf_config_human_interaction_challenge(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("human_interaction_challenge"):
        return None
    human_interaction_challenge_dict = waf_config_dict["human_interaction_challenge"]
    human_interaction_challenge = get_model_from_dict(
        HumanInteractionChallenge,
        human_interaction_challenge_dict,
        [
            "is_enabled",
            "action",
            "failure_threshold",
            "action_expiration_in_seconds",
            "failure_threshold_expiration_in_seconds",
            "interaction_threshold",
            "recording_period_in_seconds",
        ],
    )
    if (
        "set_http_header" in human_interaction_challenge_dict
        and human_interaction_challenge_dict["set_http_header"]
    ):
        set_http_header_dict = human_interaction_challenge_dict["set_http_header"]
        set_http_header = get_model_from_dict(
            Header, set_http_header_dict, ["name", "value"]
        )
        setattr(human_interaction_challenge, "set_http_header", set_http_header)
    if (
        "challenge_settings" in human_interaction_challenge_dict
        and human_interaction_challenge_dict["challenge_settings"]
    ):
        challenge_settings_dict = human_interaction_challenge_dict["challenge_settings"]
        challenge_settings = get_model_from_dict(
            BlockChallengeSettings,
            challenge_settings_dict,
            [
                "block_action",
                "block_response_code",
                "block_error_page_message",
                "block_error_page_description",
                "block_error_page_code",
                "captcha_title",
                "captcha_header",
                "captcha_footer",
                "captcha_submit_label",
            ],
        )
        setattr(human_interaction_challenge, "challenge_settings", challenge_settings)
    return human_interaction_challenge


def get_waf_config_js_challenge(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("js_challenge"):
        return None
    js_challenge_dict = waf_config_dict["js_challenge"]
    js_challenge = get_model_from_dict(
        JsChallenge,
        js_challenge_dict,
        ["is_enabled", "action", "failure_threshold", "action_expiration_in_seconds"],
    )
    if "set_http_header" in js_challenge_dict and js_challenge_dict["set_http_header"]:
        set_http_header_dict = js_challenge_dict["set_http_header"]
        set_http_header = get_model_from_dict(
            Header, set_http_header_dict, ["name", "value"]
        )
        setattr(js_challenge, "set_http_header", set_http_header)
    if (
        "challenge_settings" in js_challenge_dict
        and js_challenge_dict["challenge_settings"]
    ):
        challenge_settings_dict = js_challenge_dict["challenge_settings"]
        challenge_settings = get_model_from_dict(
            BlockChallengeSettings,
            challenge_settings_dict,
            [
                "block_action",
                "block_response_code",
                "block_error_page_message",
                "block_error_page_description",
                "block_error_page_code",
                "captcha_title",
                "captcha_header",
                "captcha_footer",
                "captcha_submit_label",
            ],
        )
        setattr(js_challenge, "challenge_settings", challenge_settings)
    return js_challenge


def get_waf_config_origin(waf_config_dict):
    if not waf_config_dict:
        return None
    return waf_config_dict.get("origin")


def get_waf_config_protection_rules(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("protection_rules"):
        return None
    waf_config_dict_protection_rules = waf_config_dict["protection_rules"]
    protection_rules = []
    for protection_rule_dict in waf_config_dict_protection_rules:
        protection_rule = get_model_from_dict(
            ProtectionRule,
            protection_rule_dict,
            ["key", "mod_security_rule_ids", "name", "description", "action", "labels"],
        )
        if "exclusions" in protection_rule_dict:
            exclusions = []
            for exclusion_dict in protection_rule_dict["exclusions"]:
                exclusion = get_model_from_dict(
                    ProtectionRuleExclusion, exclusion_dict, ["target", "exclusions"]
                )
                exclusions.append(exclusion)
            setattr(protection_rule, "exclusions", exclusions)
        protection_rules.append(protection_rule)
    return protection_rules


def get_waf_config_protection_settings(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("protection_settings"):
        return None
    protection_settings_dict = waf_config_dict["protection_settings"]
    protection_settings = get_model_from_dict(
        ProtectionSettings,
        protection_settings_dict,
        [
            "block_action",
            "block_response_code",
            "block_error_page_message",
            "block_error_page_code",
            "block_error_page_description",
            "max_argument_count",
            "max_name_length_per_argument",
            "max_total_name_length_of_arguments",
            "recommendations_period_in_days",
            "is_response_inspected",
            "max_response_size_in_ki_b",
            "allowed_http_methods",
            "media_types",
        ],
    )
    return protection_settings


def get_waf_config_whitelists(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("whitelists"):
        return None
    waf_config_dict_whitelists = waf_config_dict["whitelists"]
    whitelists = []
    for whitelist_dict in waf_config_dict_whitelists:
        whitelist = get_model_from_dict(
            Whitelist, whitelist_dict, ["addresses", "name"]
        )
        whitelists.append(whitelist)
    return whitelists


def get_waf_config_threat_feeds(waf_config_dict):
    if not waf_config_dict:
        return None
    if not waf_config_dict.get("threat_feeds"):
        return None
    waf_config_dict_threat_feeds = waf_config_dict["threat_feeds"]
    threat_feeds = []
    for threat_feed_dict in waf_config_dict_threat_feeds:
        threat_feed = get_model_from_dict(
            ThreatFeed, threat_feed_dict, ["key", "name", "action", "description"]
        )
        threat_feeds.append(threat_feed)
    return threat_feeds


def get_waf_config(module):
    if not module.params.get("waf_config"):
        return None
    waf_config_details = WafConfigDetails()
    setattr(
        waf_config_details,
        "access_rules",
        get_waf_config_access_rules(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "address_rate_limiting",
        get_waf_config_address_rate_limiting(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "captchas",
        get_waf_config_captchas(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "device_fingerprint_challenge",
        get_waf_config_device_fingerprint_challenge(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "human_interaction_challenge",
        get_waf_config_human_interaction_challenge(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "js_challenge",
        get_waf_config_js_challenge(module.params["waf_config"]),
    )
    setattr(
        waf_config_details, "origin", get_waf_config_origin(module.params["waf_config"])
    )
    setattr(
        waf_config_details,
        "protection_settings",
        get_waf_config_protection_settings(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "whitelists",
        get_waf_config_whitelists(module.params["waf_config"]),
    )
    return waf_config_details


def get_waf_config_for_update(module):
    if not module.params.get("waf_config"):
        return None
    waf_config_details = WafConfig()
    setattr(
        waf_config_details,
        "access_rules",
        get_waf_config_access_rules(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "address_rate_limiting",
        get_waf_config_address_rate_limiting(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "captchas",
        get_waf_config_captchas(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "device_fingerprint_challenge",
        get_waf_config_device_fingerprint_challenge(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "good_bots",
        get_waf_config_good_bots(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "human_interaction_challenge",
        get_waf_config_human_interaction_challenge(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "js_challenge",
        get_waf_config_js_challenge(module.params["waf_config"]),
    )
    setattr(
        waf_config_details, "origin", get_waf_config_origin(module.params["waf_config"])
    )
    setattr(
        waf_config_details,
        "protection_rules",
        get_waf_config_protection_rules(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "protection_settings",
        get_waf_config_protection_settings(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "threat_feeds",
        get_waf_config_threat_feeds(module.params["waf_config"]),
    )
    setattr(
        waf_config_details,
        "whitelists",
        get_waf_config_whitelists(module.params["waf_config"]),
    )
    return waf_config_details


def get_waas_policy_create_model(module):
    create_waas_policy_details = get_model_from_dict(
        CreateWaasPolicyDetails,
        module.params,
        [
            "compartment_id",
            "display_name",
            "domain",
            "additional_domains",
            "freeform_tags",
            "defined_tags",
        ],
    )

    setattr(create_waas_policy_details, "origins", get_waas_origins(module))
    setattr(create_waas_policy_details, "policy_config", get_waas_policy_config(module))
    setattr(create_waas_policy_details, "waf_config", get_waf_config(module))
    return create_waas_policy_details


def get_resource_identifier_from_waas_work_request_response(
    work_request_response, entity_type="waas", action_type="CREATED"
):
    if not work_request_response:
        return None
    for work_request_resource in work_request_response.data.resources:
        if (
            work_request_resource.entity_type == entity_type
            and work_request_resource.action_type == action_type
        ):
            return work_request_resource.identifier
    return None


def get_model_from_dict(model_class, params, attrs):
    model = model_class()
    if not (attrs and params):
        return model
    for attr in attrs:
        if params.get(attr):
            setattr(model, attr, params[attr])
    return model


def get_waas_policy_id_from_work_request_response(
    work_request_response, entity_type="waas", action_type="CREATED"
):
    if not work_request_response:
        return None
    logger.debug("Work request response: %s", to_dict(work_request_response.data))
    for work_request_resource in work_request_response.data.resources:
        if (
            work_request_resource.entity_type == entity_type
            and work_request_resource.action_type == action_type
        ):
            return work_request_resource.identifier
    return None


def get_waas_policy_from_work_request_response(work_request_response, module, client):
    waas_policy_id = get_waas_policy_id_from_work_request_response(
        work_request_response
    )
    if not waas_policy_id:
        module.fail_json(msg="Cound not get the waas policy id from the work request.")
    logger.debug("WAAS policy id from the work request response: %s", waas_policy_id)
    waas_policy = oci_utils.call_with_backoff(
        client.get_waas_policy, waas_policy_id=waas_policy_id
    ).data
    if not waas_policy:
        module.fail_json("Could not get the waas policy resource after creation.")
    if waas_policy.lifecycle_state in oci_utils.DEAD_STATES:
        module.fail_json(
            msg="WAAS policy created but in {0} state.".format(
                waas_policy.lifecycle_state
            )
        )
    return to_dict(waas_policy)


def get_waas_policy_from_summary_resource(waas_policy_summary, waas_client=None):
    logger.debug("Waas policy summary resource: %s", waas_policy_summary)
    if not waas_policy_summary:
        return None
    if not waas_client:
        raise Exception(
            "waas client required to get waas policy from summary resource."
        )
    if isinstance(waas_policy_summary, dict):
        waas_policy_id = waas_policy_summary.get("id")
    else:
        waas_policy_id = getattr(waas_policy_summary, "id", None)
    if not waas_policy_id:
        raise Exception("The waas policy summary resource does not have a valid id.")
    return oci_utils.call_with_backoff(
        waas_client.get_waas_policy, waas_policy_id=waas_policy_id
    ).data


def get_waas_certificate_from_summary_resource(
    waas_certificate_summary, waas_client=None
):
    logger.debug("Waas certificate summary resource: %s", waas_certificate_summary)
    if not waas_certificate_summary:
        return None
    if not waas_client:
        raise Exception(
            "waas client required to get waas certificate from summary resource."
        )
    if isinstance(waas_certificate_summary, dict):
        waas_certificate_id = waas_certificate_summary.get("id")
    else:
        waas_certificate_id = getattr(waas_certificate_summary, "id", None)
    if not waas_certificate_id:
        raise Exception(
            "The waas certificate summary resource does not have a valid id."
        )
    return oci_utils.call_with_backoff(
        waas_client.get_certificate, certificate_id=waas_certificate_id
    ).data


def list_waas_policies(waas_client, module):
    return [
        oci_utils.call_with_backoff(
            waas_client.get_waas_policy, waas_policy_id=waas_policy_summary.id
        ).data
        for waas_policy_summary in oci_utils.list_all_resources(
            waas_client.list_waas_policies,
            compartment_id=module.params.get("compartment_id"),
        )
    ]


def list_certificates(waas_client, module):
    return [
        oci_utils.call_with_backoff(
            waas_client.get_certificate, certificate_id=waas_certificate_summary.id
        )
        for waas_certificate_summary in oci_utils.list_all_resources(
            waas_client.list_certificates,
            compartment_id=module.params.get("compartment_id"),
        )
    ]
