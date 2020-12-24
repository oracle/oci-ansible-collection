.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.oracle.oci.oci_network_security_group_security_rule_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_network_security_group_security_rule_actions -- Perform actions on a NetworkSecurityGroupSecurityRule resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 2.12.0).

    To install it use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_network_security_group_security_rule_actions`.

.. version_added

.. versionadded:: 2.9 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on a NetworkSecurityGroupSecurityRule resource in Oracle Cloud Infrastructure
- For *action=add*, adds one or more security rules to the specified network security group.
- For *action=remove*, removes one or more security rules from the specified network security group.
- For *action=update*, updates one or more security rules in the specified network security group.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.7
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>add</li>
                                                                                                                                                                                                <li>remove</li>
                                                                                                                                                                                                <li>update</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the NetworkSecurityGroupSecurityRule.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-api_user"></div>
                    <b>api_user</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_ID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user&#x27;s OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_fingerprint"></div>
                    <b>api_user_fingerprint</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_fingerprint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair&#x27;s fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_key_file"></div>
                    <b>api_user_key_file</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_key_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_key_pass_phrase"></div>
                    <b>api_user_key_pass_phrase</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_key_pass_phrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-auth_type"></div>
                    <b>auth_type</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                                                                                                                                <li>instance_obo_user</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-config_file_location"></div>
                    <b>config_file_location</b>
                    <a class="ansibleOptionLink" href="#parameter-config_file_location" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-config_profile_name"></div>
                    <b>config_profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-config_profile_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-network_security_group_id"></div>
                    <b>network_security_group_id</b>
                    <a class="ansibleOptionLink" href="#parameter-network_security_group_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the network security group.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#parameter-region" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-security_rule_ids"></div>
                    <b>security_rule_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rule_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Oracle-assigned ID of each <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/SecurityRule/'>SecurityRule</a> to be deleted.</div>
                                            <div>Applicable only for <em>action=remove</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules"></div>
                    <b>security_rules</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The NSG security rules to add.</div>
                                            <div>Applicable only for <em>action=add</em><em>action=update</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An optional description of your choice for the rule. Avoid entering confidential information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/destination"></div>
                    <b>destination</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/destination" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Conceptually, this is the range of IP addresses that a packet originating from the instance can go to.</div>
                                            <div>Allowed values:</div>
                                            <div>* An IP address range in CIDR notation. For example: `192.168.1.0/24`</div>
                                            <div>* The `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Service/'>Service</a>, if you&#x27;re setting up a security rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.</div>
                                            <div>* The OCID of a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a> in the same VCN. The value can be the NSG that the rule belongs to if the rule&#x27;s intent is to control traffic between VNICs in the same NSG.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/destination_type"></div>
                    <b>destination_type</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/destination_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CIDR_BLOCK</li>
                                                                                                                                                                                                <li>SERVICE_CIDR_BLOCK</li>
                                                                                                                                                                                                <li>NETWORK_SECURITY_GROUP</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of destination for the rule. Required if `direction` = `EGRESS`.</div>
                                            <div>Allowed values:</div>
                                            <div>* `CIDR_BLOCK`: If the rule&#x27;s `destination` is an IP address range in CIDR notation.</div>
                                            <div>* `SERVICE_CIDR_BLOCK`: If the rule&#x27;s `destination` is the `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Service/'>Service</a> (the rule is for traffic destined for a particular `Service` through a service gateway).</div>
                                            <div>* `NETWORK_SECURITY_GROUP`: If the rule&#x27;s `destination` is the OCID of a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/direction"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/direction" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>EGRESS</li>
                                                                                                                                                                                                <li>INGRESS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/icmp_options"></div>
                    <b>icmp_options</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/icmp_options" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code as defined in: - <a href='http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml'>ICMP Parameters</a> - <a href='https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml'>ICMPv6 Parameters</a></div>
                                            <div>If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and codes are allowed. If you do provide this object, the type is required and the code is optional. To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (&quot;Destination Unreachable&quot;) code 4 (&quot;Fragmentation Needed and Don&#x27;t Fragment was Set&quot;). If you need to specify multiple codes for a single type, create a separate security list rule for each.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/icmp_options/code"></div>
                    <b>code</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/icmp_options/code" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ICMP code (optional).</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/icmp_options/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/icmp_options/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ICMP type.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Oracle-assigned ID of the security rule that you want to update. You can&#x27;t change this value.</div>
                                            <div>Example: `04ABEC`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/is_stateless"></div>
                    <b>is_stateless</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/is_stateless" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The transport protocol. Specify either `all` or an IPv4 protocol number as defined in <a href='http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml'>Protocol Numbers</a>. Options are supported only for ICMP (&quot;1&quot;), TCP (&quot;6&quot;), UDP (&quot;17&quot;), and ICMPv6 (&quot;58&quot;).</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/source"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Conceptually, this is the range of IP addresses that a packet coming into the instance can come from.</div>
                                            <div>Allowed values:</div>
                                            <div>* An IP address range in CIDR notation. For example: `192.168.1.0/24`</div>
                                            <div>* The `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Service/'>Service</a>, if you&#x27;re setting up a security rule for traffic coming from a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.</div>
                                            <div>* The OCID of a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a> in the same VCN. The value can be the NSG that the rule belongs to if the rule&#x27;s intent is to control traffic between VNICs in the same NSG.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/source_type"></div>
                    <b>source_type</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/source_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CIDR_BLOCK</li>
                                                                                                                                                                                                <li>SERVICE_CIDR_BLOCK</li>
                                                                                                                                                                                                <li>NETWORK_SECURITY_GROUP</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of source for the rule. Required if `direction` = `INGRESS`.</div>
                                            <div>* `CIDR_BLOCK`: If the rule&#x27;s `source` is an IP address range in CIDR notation.</div>
                                            <div>* `SERVICE_CIDR_BLOCK`: If the rule&#x27;s `source` is the `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Service/'>Service</a> (the rule is for traffic coming from a particular `Service` through a service gateway).</div>
                                            <div>* `NETWORK_SECURITY_GROUP`: If the rule&#x27;s `source` is the OCID of a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/tcp_options"></div>
                    <b>tcp_options</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/tcp_options" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Optional and valid only for TCP. Use to specify particular destination ports for TCP rules. If you specify TCP as the protocol but omit this object, then all destination ports are allowed.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/tcp_options/destination_port_range"></div>
                    <b>destination_port_range</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/tcp_options/destination_port_range" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/tcp_options/destination_port_range/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/tcp_options/destination_port_range/max" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/tcp_options/destination_port_range/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/tcp_options/destination_port_range/min" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/tcp_options/source_port_range"></div>
                    <b>source_port_range</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/tcp_options/source_port_range" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/tcp_options/source_port_range/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/tcp_options/source_port_range/max" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/tcp_options/source_port_range/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/tcp_options/source_port_range/min" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/udp_options"></div>
                    <b>udp_options</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/udp_options" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Optional and valid only for UDP. Use to specify particular destination ports for UDP rules. If you specify UDP as the protocol but omit this object, then all destination ports are allowed.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/udp_options/destination_port_range"></div>
                    <b>destination_port_range</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/udp_options/destination_port_range" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/udp_options/destination_port_range/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/udp_options/destination_port_range/max" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/udp_options/destination_port_range/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/udp_options/destination_port_range/min" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/udp_options/source_port_range"></div>
                    <b>source_port_range</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/udp_options/source_port_range" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/udp_options/source_port_range/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/udp_options/source_port_range/max" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_rules/udp_options/source_port_range/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#parameter-security_rules/udp_options/source_port_range/min" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-tenancy"></div>
                    <b>tenancy</b>
                    <a class="ansibleOptionLink" href="#parameter-tenancy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes

Notes
-----

.. note::
   - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Perform action add on network_security_group_security_rule
      oci_network_security_group_security_rule_actions:
        network_security_group_id: ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx
        security_rules:
        - description: Example ingress security rule
          source_type: CIDR_BLOCK
          source: 10.0.0.0/16
          direction: INGRESS
          protocol: all
        - description: Example egress security rule
          destination_type: CIDR_BLOCK
          destination: 10.0.0.0/16
          direction: EGRESS
          protocol: all
        action: add

    - name: Perform action remove on network_security_group_security_rule
      oci_network_security_group_security_rule_actions:
        network_security_group_id: ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx
        security_rule_ids:
        - 880233
        - 203597
        action: remove

    - name: Perform action update on network_security_group_security_rule
      oci_network_security_group_security_rule_actions:
        network_security_group_id: ocid1.networksecuritygroup.oc1..xxxxxxEXAMPLExxxxxx
        security_rules:
        - description: Example ingress security rule - updated
          id: 203597
          source_type: CIDR_BLOCK
          source: 10.0.0.0/24
          direction: INGRESS
          protocol: all
        - description: Example egress security rule - updated
          destination_type: CIDR_BLOCK
          destination: 10.0.0.0/24
          direction: EGRESS
          id: 880233
          protocol: all
        action: update





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule"></div>
                    <b>network_security_group_security_rule</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the NetworkSecurityGroupSecurityRule resource acted upon by the current operation</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;security_rules&#x27;: [{&#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;destination&#x27;: &#x27;destination_example&#x27;, &#x27;destination_type&#x27;: &#x27;CIDR_BLOCK&#x27;, &#x27;direction&#x27;: &#x27;EGRESS&#x27;, &#x27;icmp_options&#x27;: {&#x27;code&#x27;: 56, &#x27;type&#x27;: 56}, &#x27;id&#x27;: &#x27;04ABEC&#x27;, &#x27;is_stateless&#x27;: True, &#x27;is_valid&#x27;: True, &#x27;protocol&#x27;: &#x27;protocol_example&#x27;, &#x27;source&#x27;: &#x27;source_example&#x27;, &#x27;source_type&#x27;: &#x27;CIDR_BLOCK&#x27;, &#x27;tcp_options&#x27;: {&#x27;destination_port_range&#x27;: {&#x27;max&#x27;: 56, &#x27;min&#x27;: 56}, &#x27;source_port_range&#x27;: {&#x27;max&#x27;: 56, &#x27;min&#x27;: 56}}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;udp_options&#x27;: {&#x27;destination_port_range&#x27;: {&#x27;max&#x27;: 56, &#x27;min&#x27;: 56}, &#x27;source_port_range&#x27;: {&#x27;max&#x27;: 56, &#x27;min&#x27;: 56}}}]}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules"></div>
                    <b>security_rules</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The NSG security rules that were added.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An optional description of your choice for the rule.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/destination"></div>
                    <b>destination</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/destination" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Conceptually, this is the range of IP addresses that a packet originating from the instance can go to.</div>
                                            <div>Allowed values:</div>
                                            <div>* An IP address range in CIDR notation. For example: `192.168.1.0/24`</div>
                                            <div>* The `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Service/'>Service</a>, if you&#x27;re setting up a security rule for traffic destined for a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.</div>
                                            <div>* The OCID of a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a> in the same VCN. The value can be the NSG that the rule belongs to if the rule&#x27;s intent is to control traffic between VNICs in the same NSG.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">destination_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/destination_type"></div>
                    <b>destination_type</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/destination_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of destination for the rule. Required if `direction` = `EGRESS`.</div>
                                            <div>Allowed values:</div>
                                            <div>* `CIDR_BLOCK`: If the rule&#x27;s `destination` is an IP address range in CIDR notation.</div>
                                            <div>* `SERVICE_CIDR_BLOCK`: If the rule&#x27;s `destination` is the `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Service/'>Service</a> (the rule is for traffic destined for a particular `Service` through a service gateway).</div>
                                            <div>* `NETWORK_SECURITY_GROUP`: If the rule&#x27;s `destination` is the OCID of a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CIDR_BLOCK</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/direction"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/direction" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">EGRESS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/icmp_options"></div>
                    <b>icmp_options</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/icmp_options" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code as defined in: - <a href='http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml'>ICMP Parameters</a> - <a href='https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml'>ICMPv6 Parameters</a></div>
                                            <div>If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and codes are allowed. If you do provide this object, the type is required and the code is optional. To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (&quot;Destination Unreachable&quot;) code 4 (&quot;Fragmentation Needed and Don&#x27;t Fragment was Set&quot;). If you need to specify multiple codes for a single type, create a separate security rule for each.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/icmp_options/code"></div>
                    <b>code</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/icmp_options/code" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The ICMP code (optional).</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/icmp_options/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/icmp_options/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The ICMP type.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An Oracle-assigned identifier for the security rule. You specify this ID when you want to update or delete the rule.</div>
                                            <div>Example: `04ABEC`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">04ABEC</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/is_stateless"></div>
                    <b>is_stateless</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/is_stateless" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/is_valid"></div>
                    <b>is_valid</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/is_valid" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the rule is valid. The value is `True` when the rule is first created. If the rule&#x27;s `source` or `destination` is a network security group, the value changes to `False` if that network security group is deleted.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The transport protocol. Specify either `all` or an IPv4 protocol number as defined in <a href='http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml'>Protocol Numbers</a>. Options are supported only for ICMP (&quot;1&quot;), TCP (&quot;6&quot;), UDP (&quot;17&quot;), and ICMPv6 (&quot;58&quot;).</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">protocol_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/source"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/source" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Conceptually, this is the range of IP addresses that a packet coming into the instance can come from.</div>
                                            <div>Allowed values:</div>
                                            <div>* An IP address range in CIDR notation. For example: `192.168.1.0/24`</div>
                                            <div>* The `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Service/'>Service</a>, if you&#x27;re setting up a security rule for traffic coming from a particular `Service` through a service gateway. For example: `oci-phx-objectstorage`.</div>
                                            <div>* The OCID of a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a> in the same VCN. The value can be the NSG that the rule belongs to if the rule&#x27;s intent is to control traffic between VNICs in the same NSG.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">source_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/source_type"></div>
                    <b>source_type</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/source_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of source for the rule. Required if `direction` = `INGRESS`.</div>
                                            <div>* `CIDR_BLOCK`: If the rule&#x27;s `source` is an IP address range in CIDR notation.</div>
                                            <div>* `SERVICE_CIDR_BLOCK`: If the rule&#x27;s `source` is the `cidrBlock` value for a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Service/'>Service</a> (the rule is for traffic coming from a particular `Service` through a service gateway).</div>
                                            <div>* `NETWORK_SECURITY_GROUP`: If the rule&#x27;s `source` is the OCID of a <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CIDR_BLOCK</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/tcp_options"></div>
                    <b>tcp_options</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/tcp_options" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Optional and valid only for TCP. Use to specify particular destination ports for TCP rules. If you specify TCP as the protocol but omit this object, then all destination ports are allowed.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/tcp_options/destination_port_range"></div>
                    <b>destination_port_range</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/tcp_options/destination_port_range" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/tcp_options/destination_port_range/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/tcp_options/destination_port_range/max" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/tcp_options/destination_port_range/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/tcp_options/destination_port_range/min" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/tcp_options/source_port_range"></div>
                    <b>source_port_range</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/tcp_options/source_port_range" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/tcp_options/source_port_range/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/tcp_options/source_port_range/max" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/tcp_options/source_port_range/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/tcp_options/source_port_range/min" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the security rule was created. Format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/udp_options"></div>
                    <b>udp_options</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/udp_options" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Optional and valid only for UDP. Use to specify particular destination ports for UDP rules. If you specify UDP as the protocol but omit this object, then all destination ports are allowed.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/udp_options/destination_port_range"></div>
                    <b>destination_port_range</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/udp_options/destination_port_range" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/udp_options/destination_port_range/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/udp_options/destination_port_range/max" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/udp_options/destination_port_range/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/udp_options/destination_port_range/min" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/udp_options/source_port_range"></div>
                    <b>source_port_range</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/udp_options/source_port_range" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/udp_options/source_port_range/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/udp_options/source_port_range/max" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-network_security_group_security_rule/security_rules/udp_options/source_port_range/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#return-network_security_group_security_rule/security_rules/udp_options/source_port_range/min" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The minimum port number. Must not be greater than the maximum port number.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                    
                    
                    
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Oracle (@oracle)



.. Parsing errors

