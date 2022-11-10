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
module: oci_network_firewall_policy_actions
short_description: Perform actions on a NetworkFirewallPolicy resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a NetworkFirewallPolicy resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a NetworkFirewallPolicy resource from one compartment identifier to another. When provided, If-Match is checked
      against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_firewall_policy_id:
        description:
            - Unique Network Firewall Policy identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the NetworkFirewallPolicy.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on network_firewall_policy
  oci_network_firewall_policy_actions:
    # required
    network_firewall_policy_id: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
network_firewall_policy:
    description:
        - Details of the NetworkFirewallPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - "The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource - Network Firewall Policy."
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the NetworkFirewall
                  Policy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly optional name for the firewall policy. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - "The time instant at which the Network Firewall Policy was created in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The time instant at which the Network Firewall Policy was updated in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Network Firewall Policy.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        mapped_secrets:
            description:
                - "Map defining secrets of the policy.
                  The value of an entry is a \\"mapped secret\\" consisting of a purpose and source.
                  The associated key is the identifier by which the mapped secret is referenced."
            returned: on success
            type: complex
            contains:
                source:
                    description:
                        - Source of the secrets, where the secrets are stored.
                    returned: on success
                    type: str
                    sample: OCI_VAULT
                type:
                    description:
                        - Type of the secrets mapped based on the policy.
                        - "* `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic.
                           * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection."
                    returned: on success
                    type: str
                    sample: SSL_INBOUND_INSPECTION
                vault_secret_id:
                    description:
                        - OCID for the Vault Secret to be used.
                    returned: on success
                    type: str
                    sample: "ocid1.vaultsecret.oc1..xxxxxxEXAMPLExxxxxx"
                version_number:
                    description:
                        - Version number of the secret to be used.
                    returned: on success
                    type: int
                    sample: 56
        application_lists:
            description:
                - "Map defining application lists of the policy.
                  The value of an entry is a list of \\"applications\\", each consisting of a protocol identifier (such as TCP, UDP, or ICMP) and protocol-
                  specific parameters (such as a port range).
                  The associated key is the identifier by which the application list is referenced."
            returned: on success
            type: dict
            sample: {}
        url_lists:
            description:
                - Map defining URL pattern lists of the policy.
                  The value of an entry is a list of URL patterns.
                  The associated key is the identifier by which the URL pattern list is referenced.
            returned: on success
            type: dict
            sample: {}
        ip_address_lists:
            description:
                - Map defining IP address lists of the policy.
                  The value of an entry is a list of IP addresses or prefixes in CIDR notation.
                  The associated key is the identifier by which the IP address list is referenced.
            returned: on success
            type: dict
            sample: {}
        security_rules:
            description:
                - List of Security Rules defining the behavior of the policy.
                  The first rule with a matching condition determines the action taken upon network traffic.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name for the Security rule, must be unique within the policy.
                    returned: on success
                    type: str
                    sample: name_example
                condition:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        sources:
                            description:
                                - An array of IP address list names to be evaluated against the traffic source address.
                            returned: on success
                            type: list
                            sample: []
                        destinations:
                            description:
                                - An array of IP address list names to be evaluated against the traffic destination address.
                            returned: on success
                            type: list
                            sample: []
                        applications:
                            description:
                                - An array of application list names to be evaluated against the traffic protocol and protocol-specific parameters.
                            returned: on success
                            type: list
                            sample: []
                        urls:
                            description:
                                - An array of URL pattern list names to be evaluated against the HTTP(S) request target.
                            returned: on success
                            type: list
                            sample: []
                action:
                    description:
                        - Types of Action on the Traffic flow.
                        - " * ALLOW - Allows the traffic.
                            * DROP - Silently drops the traffic, e.g. without sending a TCP reset.
                            * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable.
                            * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection."
                    returned: on success
                    type: str
                    sample: ALLOW
                inspection:
                    description:
                        - Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT.
                        - " * INTRUSION_DETECTION - Intrusion Detection.
                            * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as
                            described in `type`."
                    returned: on success
                    type: str
                    sample: INTRUSION_DETECTION
        decryption_rules:
            description:
                - List of Decryption Rules defining the behavior of the policy.
                  The first rule with a matching condition determines the action taken upon network traffic.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name for the decryption rule, must be unique within the policy.
                    returned: on success
                    type: str
                    sample: name_example
                condition:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        sources:
                            description:
                                - An array of IP address list names to be evaluated against the traffic source address.
                            returned: on success
                            type: list
                            sample: []
                        destinations:
                            description:
                                - An array of IP address list names to be evaluated against the traffic destination address.
                            returned: on success
                            type: list
                            sample: []
                action:
                    description:
                        - "Action:"
                        - "* NO_DECRYPT - Matching traffic is not decrypted.
                          * DECRYPT - Matching traffic is decrypted with the specified `secret` according to the specified `decryptionProfile`."
                    returned: on success
                    type: str
                    sample: NO_DECRYPT
                decryption_profile:
                    description:
                        - The name of the decryption profile to use.
                    returned: on success
                    type: str
                    sample: decryption_profile_example
                secret:
                    description:
                        - The name of a mapped secret. Its `type` must match that of the specified decryption profile.
                    returned: on success
                    type: str
                    sample: secret_example
        decryption_profiles:
            description:
                - Map defining decryption profiles of the policy.
                  The value of an entry is a decryption profile.
                  The associated key is the identifier by which the decryption profile is referenced.
            returned: on success
            type: complex
            contains:
                is_expired_certificate_blocked:
                    description:
                        - Whether to block sessions if server's certificate is expired.
                    returned: on success
                    type: bool
                    sample: true
                is_untrusted_issuer_blocked:
                    description:
                        - Whether to block sessions if server's certificate is issued by an untrusted certificate authority (CA).
                    returned: on success
                    type: bool
                    sample: true
                is_revocation_status_timeout_blocked:
                    description:
                        - Whether to block sessions if the revocation status check for server's certificate
                          does not succeed within the maximum allowed time (defaulting to 5 seconds).
                    returned: on success
                    type: bool
                    sample: true
                is_unknown_revocation_status_blocked:
                    description:
                        - "Whether to block sessions if the revocation status check for server's certificate results in \\"unknown\\"."
                    returned: on success
                    type: bool
                    sample: true
                are_certificate_extensions_restricted:
                    description:
                        - Whether to block sessions if the server's certificate uses extensions other than key usage and/or extended key usage.
                    returned: on success
                    type: bool
                    sample: true
                is_auto_include_alt_name:
                    description:
                        - Whether to automatically append SAN to impersonating certificate if server certificate is missing SAN.
                    returned: on success
                    type: bool
                    sample: true
                type:
                    description:
                        - Describes the type of Decryption Profile SslForwardProxy or SslInboundInspection.
                    returned: on success
                    type: str
                    sample: SSL_INBOUND_INSPECTION
                is_unsupported_version_blocked:
                    description:
                        - Whether to block sessions if SSL version is not supported.
                    returned: on success
                    type: bool
                    sample: true
                is_unsupported_cipher_blocked:
                    description:
                        - Whether to block sessions if SSL cipher suite is not supported.
                    returned: on success
                    type: bool
                    sample: true
                is_out_of_capacity_blocked:
                    description:
                        - Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.
                    returned: on success
                    type: bool
                    sample: true
        is_firewall_attached:
            description:
                - To determine if any Network Firewall is associated with this Network Firewall Policy.
            returned: on success
            type: bool
            sample: true
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "mapped_secrets": {
            "source": "OCI_VAULT",
            "type": "SSL_INBOUND_INSPECTION",
            "vault_secret_id": "ocid1.vaultsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "version_number": 56
        },
        "application_lists": {},
        "url_lists": {},
        "ip_address_lists": {},
        "security_rules": [{
            "name": "name_example",
            "condition": {
                "sources": [],
                "destinations": [],
                "applications": [],
                "urls": []
            },
            "action": "ALLOW",
            "inspection": "INTRUSION_DETECTION"
        }],
        "decryption_rules": [{
            "name": "name_example",
            "condition": {
                "sources": [],
                "destinations": []
            },
            "action": "NO_DECRYPT",
            "decryption_profile": "decryption_profile_example",
            "secret": "secret_example"
        }],
        "decryption_profiles": {
            "is_expired_certificate_blocked": true,
            "is_untrusted_issuer_blocked": true,
            "is_revocation_status_timeout_blocked": true,
            "is_unknown_revocation_status_blocked": true,
            "are_certificate_extensions_restricted": true,
            "is_auto_include_alt_name": true,
            "type": "SSL_INBOUND_INSPECTION",
            "is_unsupported_version_blocked": true,
            "is_unsupported_cipher_blocked": true,
            "is_out_of_capacity_blocked": true
        },
        "is_firewall_attached": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.network_firewall import NetworkFirewallClient
    from oci.network_firewall.models import (
        ChangeNetworkFirewallPolicyCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkFirewallPolicyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "network_firewall_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_firewall_policy_id")

    def get_get_fn(self):
        return self.client.get_network_firewall_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_firewall_policy,
            network_firewall_policy_id=self.module.params.get(
                "network_firewall_policy_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeNetworkFirewallPolicyCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_network_firewall_policy_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_firewall_policy_id=self.module.params.get(
                    "network_firewall_policy_id"
                ),
                change_network_firewall_policy_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


NetworkFirewallPolicyActionsHelperCustom = get_custom_class(
    "NetworkFirewallPolicyActionsHelperCustom"
)


class ResourceHelper(
    NetworkFirewallPolicyActionsHelperCustom, NetworkFirewallPolicyActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            network_firewall_policy_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_firewall_policy",
        service_client_class=NetworkFirewallClient,
        namespace="network_firewall",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
