#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_network_firewall_policy
short_description: Manage a NetworkFirewallPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NetworkFirewallPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Network Firewall Policy.
    - "This resource has the following action operations in the M(oracle.oci.oci_network_firewall_policy_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the NetworkFirewall Policy.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly optional name for the firewall policy. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    mapped_secrets:
        description:
            - "Map defining secrets of the policy.
              The value of an entry is a \\"mapped secret\\" consisting of a purpose and source.
              The associated key is the identifier by which the mapped secret is referenced."
            - This parameter is updatable.
        type: dict
        suboptions:
            source:
                description:
                    - Source of the secrets, where the secrets are stored.
                type: str
                choices:
                    - "OCI_VAULT"
                required: true
            type:
                description:
                    - Type of the secrets mapped based on the policy.
                    - "* `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic.
                       * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection."
                type: str
                choices:
                    - "SSL_INBOUND_INSPECTION"
                    - "SSL_FORWARD_PROXY"
                required: true
            vault_secret_id:
                description:
                    - OCID for the Vault Secret to be used.
                type: str
                required: true
            version_number:
                description:
                    - Version number of the secret to be used.
                type: int
                required: true
    application_lists:
        description:
            - "Map defining application lists of the policy.
              The value of an entry is a list of \\"applications\\", each consisting of a protocol identifier (such as TCP, UDP, or ICMP) and protocol-specific
              parameters (such as a port range).
              The associated key is the identifier by which the application list is referenced."
            - This parameter is updatable.
        type: dict
    url_lists:
        description:
            - Map defining URL pattern lists of the policy.
              The value of an entry is a list of URL patterns.
              The associated key is the identifier by which the URL pattern list is referenced.
            - This parameter is updatable.
        type: dict
    ip_address_lists:
        description:
            - Map defining IP address lists of the policy.
              The value of an entry is a list of IP addresses or prefixes in CIDR notation.
              The associated key is the identifier by which the IP address list is referenced.
            - This parameter is updatable.
        type: dict
    security_rules:
        description:
            - List of Security Rules defining the behavior of the policy.
              The first rule with a matching condition determines the action taken upon network traffic.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - Name for the Security rule, must be unique within the policy.
                type: str
                required: true
            condition:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    sources:
                        description:
                            - An array of IP address list names to be evaluated against the traffic source address.
                        type: list
                        elements: str
                    destinations:
                        description:
                            - An array of IP address list names to be evaluated against the traffic destination address.
                        type: list
                        elements: str
                    applications:
                        description:
                            - An array of application list names to be evaluated against the traffic protocol and protocol-specific parameters.
                        type: list
                        elements: str
                    urls:
                        description:
                            - An array of URL pattern list names to be evaluated against the HTTP(S) request target.
                        type: list
                        elements: str
            action:
                description:
                    - Types of Action on the Traffic flow.
                    - " * ALLOW - Allows the traffic.
                        * DROP - Silently drops the traffic, e.g. without sending a TCP reset.
                        * REJECT - Rejects the traffic, sending a TCP reset to client and/or server as applicable.
                        * INSPECT - Inspects traffic for vulnerability as specified in `inspection`, which may result in rejection."
                type: str
                choices:
                    - "ALLOW"
                    - "DROP"
                    - "REJECT"
                    - "INSPECT"
                required: true
            inspection:
                description:
                    - Type of inspection to affect the Traffic flow. This is only applicable if action is INSPECT.
                    - " * INTRUSION_DETECTION - Intrusion Detection.
                        * INTRUSION_PREVENTION - Intrusion Detection and Prevention. Traffic classified as potentially malicious will be rejected as described
                        in `type`."
                type: str
                choices:
                    - "INTRUSION_DETECTION"
                    - "INTRUSION_PREVENTION"
    decryption_rules:
        description:
            - List of Decryption Rules defining the behavior of the policy.
              The first rule with a matching condition determines the action taken upon network traffic.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - Name for the decryption rule, must be unique within the policy.
                type: str
                required: true
            condition:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    sources:
                        description:
                            - An array of IP address list names to be evaluated against the traffic source address.
                        type: list
                        elements: str
                    destinations:
                        description:
                            - An array of IP address list names to be evaluated against the traffic destination address.
                        type: list
                        elements: str
            action:
                description:
                    - "Action:"
                    - "* NO_DECRYPT - Matching traffic is not decrypted.
                      * DECRYPT - Matching traffic is decrypted with the specified `secret` according to the specified `decryptionProfile`."
                type: str
                choices:
                    - "NO_DECRYPT"
                    - "DECRYPT"
                required: true
            decryption_profile:
                description:
                    - The name of the decryption profile to use.
                type: str
            secret:
                description:
                    - The name of a mapped secret. Its `type` must match that of the specified decryption profile.
                type: str
    decryption_profiles:
        description:
            - Map defining decryption profiles of the policy.
              The value of an entry is a decryption profile.
              The associated key is the identifier by which the decryption profile is referenced.
            - This parameter is updatable.
        type: dict
        suboptions:
            type:
                description:
                    - Describes the type of Decryption Profile SslForwardProxy or SslInboundInspection.
                type: str
                choices:
                    - "SSL_INBOUND_INSPECTION"
                    - "SSL_FORWARD_PROXY"
                required: true
            is_expired_certificate_blocked:
                description:
                    - Whether to block sessions if server's certificate is expired.
                    - Required when type is 'SSL_FORWARD_PROXY'
                type: bool
            is_untrusted_issuer_blocked:
                description:
                    - Whether to block sessions if server's certificate is issued by an untrusted certificate authority (CA).
                    - Required when type is 'SSL_FORWARD_PROXY'
                type: bool
            is_revocation_status_timeout_blocked:
                description:
                    - Whether to block sessions if the revocation status check for server's certificate
                      does not succeed within the maximum allowed time (defaulting to 5 seconds).
                    - Required when type is 'SSL_FORWARD_PROXY'
                type: bool
            is_unsupported_version_blocked:
                description:
                    - Whether to block sessions if SSL version is not supported.
                type: bool
                required: true
            is_unsupported_cipher_blocked:
                description:
                    - Whether to block sessions if SSL cipher suite is not supported.
                type: bool
                required: true
            is_unknown_revocation_status_blocked:
                description:
                    - "Whether to block sessions if the revocation status check for server's certificate results in \\"unknown\\"."
                    - Required when type is 'SSL_FORWARD_PROXY'
                type: bool
            are_certificate_extensions_restricted:
                description:
                    - Whether to block sessions if the server's certificate uses extensions other than key usage and/or extended key usage.
                    - Required when type is 'SSL_FORWARD_PROXY'
                type: bool
            is_auto_include_alt_name:
                description:
                    - Whether to automatically append SAN to impersonating certificate if server certificate is missing SAN.
                    - Required when type is 'SSL_FORWARD_PROXY'
                type: bool
            is_out_of_capacity_blocked:
                description:
                    - Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.
                type: bool
                required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    network_firewall_policy_id:
        description:
            - Unique Network Firewall Policy identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NetworkFirewallPolicy.
            - Use I(state=present) to create or update a NetworkFirewallPolicy.
            - Use I(state=absent) to delete a NetworkFirewallPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create network_firewall_policy
  oci_network_firewall_policy:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    mapped_secrets:
      # required
      source: OCI_VAULT
      type: SSL_INBOUND_INSPECTION
      vault_secret_id: "ocid1.vaultsecret.oc1..xxxxxxEXAMPLExxxxxx"
      version_number: 56
    application_lists: null
    url_lists: null
    ip_address_lists: null
    security_rules:
    - # required
      name: name_example
      condition:
        # optional
        sources: [ "sources_example" ]
        destinations: [ "destinations_example" ]
        applications: [ "applications_example" ]
        urls: [ "urls_example" ]
      action: ALLOW
    - # optional
      inspection: INTRUSION_DETECTION
    decryption_rules:
    - # required
      name: name_example
      condition:
        # optional
        sources: [ "sources_example" ]
        destinations: [ "destinations_example" ]
      action: NO_DECRYPT
    - # optional
      decryption_profile: decryption_profile_example
      secret: secret_example
    decryption_profiles:
      # required
      type: SSL_INBOUND_INSPECTION
      is_unsupported_version_blocked: true
      is_unsupported_cipher_blocked: true
      is_out_of_capacity_blocked: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update network_firewall_policy
  oci_network_firewall_policy:
    # required
    network_firewall_policy_id: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    mapped_secrets:
      # required
      source: OCI_VAULT
      type: SSL_INBOUND_INSPECTION
      vault_secret_id: "ocid1.vaultsecret.oc1..xxxxxxEXAMPLExxxxxx"
      version_number: 56
    application_lists: null
    url_lists: null
    ip_address_lists: null
    security_rules:
    - # required
      name: name_example
      condition:
        # optional
        sources: [ "sources_example" ]
        destinations: [ "destinations_example" ]
        applications: [ "applications_example" ]
        urls: [ "urls_example" ]
      action: ALLOW
    - # optional
      inspection: INTRUSION_DETECTION
    decryption_rules:
    - # required
      name: name_example
      condition:
        # optional
        sources: [ "sources_example" ]
        destinations: [ "destinations_example" ]
      action: NO_DECRYPT
    - # optional
      decryption_profile: decryption_profile_example
      secret: secret_example
    decryption_profiles:
      # required
      type: SSL_INBOUND_INSPECTION
      is_unsupported_version_blocked: true
      is_unsupported_cipher_blocked: true
      is_out_of_capacity_blocked: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update network_firewall_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_firewall_policy:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    mapped_secrets:
      # required
      source: OCI_VAULT
      type: SSL_INBOUND_INSPECTION
      vault_secret_id: "ocid1.vaultsecret.oc1..xxxxxxEXAMPLExxxxxx"
      version_number: 56
    application_lists: null
    url_lists: null
    ip_address_lists: null
    security_rules:
    - # required
      name: name_example
      condition:
        # optional
        sources: [ "sources_example" ]
        destinations: [ "destinations_example" ]
        applications: [ "applications_example" ]
        urls: [ "urls_example" ]
      action: ALLOW
    - # optional
      inspection: INTRUSION_DETECTION
    decryption_rules:
    - # required
      name: name_example
      condition:
        # optional
        sources: [ "sources_example" ]
        destinations: [ "destinations_example" ]
      action: NO_DECRYPT
    - # optional
      decryption_profile: decryption_profile_example
      secret: secret_example
    decryption_profiles:
      # required
      type: SSL_INBOUND_INSPECTION
      is_unsupported_version_blocked: true
      is_unsupported_cipher_blocked: true
      is_out_of_capacity_blocked: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete network_firewall_policy
  oci_network_firewall_policy:
    # required
    network_firewall_policy_id: "ocid1.networkfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete network_firewall_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_firewall_policy:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.network_firewall import NetworkFirewallClient
    from oci.network_firewall.models import CreateNetworkFirewallPolicyDetails
    from oci.network_firewall.models import UpdateNetworkFirewallPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkFirewallPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            NetworkFirewallPolicyHelperGen, self
        ).get_possible_entity_types() + [
            "networkfirewallpolicy",
            "networkfirewallpolicies",
            "networkFirewallnetworkfirewallpolicy",
            "networkFirewallnetworkfirewallpolicies",
            "networkfirewallpolicyresource",
            "networkfirewallpoliciesresource",
            "networkfirewall",
        ]

    def get_module_resource_id_param(self):
        return "network_firewall_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_firewall_policy_id")

    def get_get_fn(self):
        return self.client.get_network_firewall_policy

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_firewall_policy,
            network_firewall_policy_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_firewall_policy,
            network_firewall_policy_id=self.module.params.get(
                "network_firewall_policy_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_network_firewall_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateNetworkFirewallPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_network_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(create_network_firewall_policy_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateNetworkFirewallPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_network_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_firewall_policy_id=self.module.params.get(
                    "network_firewall_policy_id"
                ),
                update_network_firewall_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_network_firewall_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_firewall_policy_id=self.module.params.get(
                    "network_firewall_policy_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkFirewallPolicyHelperCustom = get_custom_class(
    "NetworkFirewallPolicyHelperCustom"
)


class ResourceHelper(NetworkFirewallPolicyHelperCustom, NetworkFirewallPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            mapped_secrets=dict(type="dict", no_log=True),
            application_lists=dict(type="dict"),
            url_lists=dict(type="dict"),
            ip_address_lists=dict(type="dict"),
            security_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    condition=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            sources=dict(type="list", elements="str"),
                            destinations=dict(type="list", elements="str"),
                            applications=dict(type="list", elements="str"),
                            urls=dict(type="list", elements="str"),
                        ),
                    ),
                    action=dict(
                        type="str",
                        required=True,
                        choices=["ALLOW", "DROP", "REJECT", "INSPECT"],
                    ),
                    inspection=dict(
                        type="str",
                        choices=["INTRUSION_DETECTION", "INTRUSION_PREVENTION"],
                    ),
                ),
            ),
            decryption_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    condition=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            sources=dict(type="list", elements="str"),
                            destinations=dict(type="list", elements="str"),
                        ),
                    ),
                    action=dict(
                        type="str", required=True, choices=["NO_DECRYPT", "DECRYPT"]
                    ),
                    decryption_profile=dict(type="str"),
                    secret=dict(type="str", no_log=True),
                ),
            ),
            decryption_profiles=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            network_firewall_policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
