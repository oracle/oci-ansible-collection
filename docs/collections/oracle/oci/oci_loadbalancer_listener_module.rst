.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na

.. Anchors

.. _ansible_collections.oracle.oci.oci_loadbalancer_listener_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_loadbalancer_listener -- Manage a Listener resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.33.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_loadbalancer_listener`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a Listener resource in Oracle Cloud Infrastructure
- For *state=present*, adds a listener to a load balancer.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 3.6
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-auth_purpose"></div>
                    <b>auth_purpose</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_purpose" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>service_principal</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The auth purpose which can be used in conjunction with &#x27;auth_type=instance_principal&#x27;. The default auth_purpose for instance_principal is None.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                                                                                                                                                <li>resource_principal</li>
                                                                                                                                                                                                <li>security_token</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cert_bundle"></div>
                    <b>cert_bundle</b>
                    <a class="ansibleOptionLink" href="#parameter-cert_bundle" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The full path to a CA certificate bundle to be used for SSL verification. This will override the default CA certificate bundle. If not set, then the value of the OCI_ANSIBLE_CERT_BUNDLE variable, if any, is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-connection_configuration"></div>
                    <b>connection_configuration</b>
                    <a class="ansibleOptionLink" href="#parameter-connection_configuration" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-connection_configuration/backend_tcp_proxy_protocol_version"></div>
                    <b>backend_tcp_proxy_protocol_version</b>
                    <a class="ansibleOptionLink" href="#parameter-connection_configuration/backend_tcp_proxy_protocol_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The backend TCP Proxy Protocol version.</div>
                                            <div>Example: `1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-connection_configuration/idle_timeout"></div>
                    <b>idle_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-connection_configuration/idle_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations.</div>
                                            <div>For more information, see <a href='https://docs.cloud.oracle.com/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration'>Connection Configuration</a>.</div>
                                            <div>Example: `1200`</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-default_backend_set_name"></div>
                    <b>default_backend_set_name</b>
                    <a class="ansibleOptionLink" href="#parameter-default_backend_set_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the associated backend set.</div>
                                            <div>Example: `example_backend_set`</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with name present.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-force_create"></div>
                    <b>force_create</b>
                    <a class="ansibleOptionLink" href="#parameter-force_create" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn&#x27;t create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hostname_names"></div>
                    <b>hostname_names</b>
                    <a class="ansibleOptionLink" href="#parameter-hostname_names" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of hostname resource names.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-key_by"></div>
                    <b>key_by</b>
                    <a class="ansibleOptionLink" href="#parameter-key_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource are used to uniquely identify a resource.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-load_balancer_id"></div>
                    <b>load_balancer_id</b>
                    <a class="ansibleOptionLink" href="#parameter-load_balancer_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the load balancer on which to add a listener.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A friendly name for the listener. It must be unique and it cannot be changed. Avoid entering confidential information.</div>
                                            <div>Example: `example_listener`</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-path_route_set_name"></div>
                    <b>path_route_set_name</b>
                    <a class="ansibleOptionLink" href="#parameter-path_route_set_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Deprecated. Please use `routingPolicies` instead.</div>
                                            <div>The name of the set of path-based routing rules, <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/'>PathRouteSet</a>, applied to this listener&#x27;s traffic.</div>
                                            <div>Example: `example_path_route_set`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The communication port for the listener.</div>
                                            <div>Example: `80`</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with name present.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols'>ListProtocols</a> operation.</div>
                                            <div>Example: `HTTP`</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with name present.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-realm_specific_endpoint_template_enabled"></div>
                    <b>realm_specific_endpoint_template_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-realm_specific_endpoint_template_enabled" title="Permalink to this option"></a>
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
                                            <div>Enable/Disable realm specific endpoint template for service client. By Default, realm specific endpoint template is disabled. If not set, then the value of the OCI_REALM_SPECIFIC_SERVICE_ENDPOINT_TEMPLATE_ENABLED variable, if any, is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-routing_policy_name"></div>
                    <b>routing_policy_name</b>
                    <a class="ansibleOptionLink" href="#parameter-routing_policy_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the routing policy applied to this listener&#x27;s traffic.</div>
                                            <div>Example: `example_routing_policy`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rule_set_names"></div>
                    <b>rule_set_names</b>
                    <a class="ansibleOptionLink" href="#parameter-rule_set_names" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The names of the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/RuleSet/'>rule sets</a> to apply to the listener.</div>
                                            <div>Example: [&quot;example_rule_set&quot;]</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration"></div>
                    <b>ssl_configuration</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration/certificate_ids"></div>
                    <b>certificate_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration/certificate_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Ids for OCI certificates service certificates. Currently only a single Id may be passed.</div>
                                            <div>Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration/certificate_name"></div>
                    <b>certificate_name</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration/certificate_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.</div>
                                            <div>Example: `example_certificate_bundle`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration/cipher_suite_name"></div>
                    <b>cipher_suite_name</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration/cipher_suite_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the cipher suite to use for HTTPS or SSL connections.</div>
                                            <div>If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`.</div>
                                            <div>**Notes:**</div>
                                            <div>*  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher suite. Clients cannot perform an SSL handshake if there is an incompatible configuration. *  You must ensure compatibility between the ciphers configured in the cipher suite and the configured certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA certificates. *  If the cipher configuration is not modified after load balancer creation, the `GET` operation returns `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners that predate this feature. *  If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET` operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for existing listeners that predate this feature. *  The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing backend sets that predate this feature. *  If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field, you must specify an appropriate predefined or custom cipher suite name when updating the resource. *  The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for this field.</div>
                                            <div>example: `example_cipher_suite`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration/protocols"></div>
                    <b>protocols</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration/protocols" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of SSL protocols the load balancer must support for HTTPS or SSL connections.</div>
                                            <div>The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure connection ensures that all data passed between the client and the server is private.</div>
                                            <div>The Load Balancing service supports the following protocols:</div>
                                            <div>*  TLSv1 *  TLSv1.1 *  TLSv1.2</div>
                                            <div>If this field is not specified, TLSv1.2 is the default.</div>
                                            <div>**Warning:** All SSL listeners created on a given port must use the same set of SSL protocols.</div>
                                            <div>**Notes:**</div>
                                            <div>*  The handshake to establish an SSL connection fails if the client supports none of the specified protocols. *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher suite. *  For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation displays a list of SSL protocols currently used by those resources.</div>
                                            <div>example: `[&quot;TLSv1.1&quot;, &quot;TLSv1.2&quot;]`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration/server_order_preference"></div>
                    <b>server_order_preference</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration/server_order_preference" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ENABLED</li>
                                                                                                                                                                                                <li>DISABLED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client ciphers.</div>
                                            <div>**Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This field is ignored when the `SSLConfiguration` object is associated with a backend set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration/trusted_certificate_authority_ids"></div>
                    <b>trusted_certificate_authority_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration/trusted_certificate_authority_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Ids for OCI certificates service CA or CA bundles for the load balancer to trust.</div>
                                            <div>Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration/verify_depth"></div>
                    <b>verify_depth</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration/verify_depth" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum depth for peer certificate chain verification.</div>
                                            <div>Example: `3`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ssl_configuration/verify_peer_certificate"></div>
                    <b>verify_peer_certificate</b>
                    <a class="ansibleOptionLink" href="#parameter-ssl_configuration/verify_peer_certificate" title="Permalink to this option"></a>
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
                                            <div>Whether the load balancer listener should verify peer certificates.</div>
                                            <div>Example: `true`</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The state of the Listener.</div>
                                            <div>Use <em>state=present</em> to create or update a Listener.</div>
                                            <div>Use <em>state=absent</em> to delete a Listener.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wait"></div>
                    <b>wait</b>
                    <a class="ansibleOptionLink" href="#parameter-wait" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to wait for create or delete operation to complete.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wait_timeout"></div>
                    <b>wait_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-wait_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Time, in seconds, to wait when <em>wait=yes</em>. Defaults to 1200 for most of the services but some services might have a longer wait timeout.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Attributes


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

    
    - name: Create listener
      oci_loadbalancer_listener:
        # required
        default_backend_set_name: default_backend_set_name_example
        port: 56
        protocol: protocol_example
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        name: name_example

        # optional
        hostname_names: [ "hostname_names_example" ]
        path_route_set_name: path_route_set_name_example
        routing_policy_name: routing_policy_name_example
        ssl_configuration:
          # optional
          verify_depth: 56
          verify_peer_certificate: true
          trusted_certificate_authority_ids: [ "trusted_certificate_authority_ids_example" ]
          certificate_ids: [ "certificate_ids_example" ]
          certificate_name: certificate_name_example
          protocols: [ "protocols_example" ]
          cipher_suite_name: cipher_suite_name_example
          server_order_preference: ENABLED
        connection_configuration:
          # required
          idle_timeout: 56

          # optional
          backend_tcp_proxy_protocol_version: 56
        rule_set_names: [ "rule_set_names_example" ]

    - name: Update listener
      oci_loadbalancer_listener:
        # required
        default_backend_set_name: default_backend_set_name_example
        port: 56
        protocol: protocol_example
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        name: name_example

        # optional
        hostname_names: [ "hostname_names_example" ]
        path_route_set_name: path_route_set_name_example
        routing_policy_name: routing_policy_name_example
        ssl_configuration:
          # optional
          verify_depth: 56
          verify_peer_certificate: true
          trusted_certificate_authority_ids: [ "trusted_certificate_authority_ids_example" ]
          certificate_ids: [ "certificate_ids_example" ]
          certificate_name: certificate_name_example
          protocols: [ "protocols_example" ]
          cipher_suite_name: cipher_suite_name_example
          server_order_preference: ENABLED
        connection_configuration:
          # required
          idle_timeout: 56

          # optional
          backend_tcp_proxy_protocol_version: 56
        rule_set_names: [ "rule_set_names_example" ]

    - name: Delete listener
      oci_loadbalancer_listener:
        # required
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        name: name_example
        state: absent





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-listener"></div>
                    <b>listener</b>
                    <a class="ansibleOptionLink" href="#return-listener" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Listener resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;connection_configuration&#x27;: {&#x27;backend_tcp_proxy_protocol_version&#x27;: 56, &#x27;idle_timeout&#x27;: 56}, &#x27;default_backend_set_name&#x27;: &#x27;default_backend_set_name_example&#x27;, &#x27;hostname_names&#x27;: [], &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;path_route_set_name&#x27;: &#x27;path_route_set_name_example&#x27;, &#x27;port&#x27;: 56, &#x27;protocol&#x27;: &#x27;protocol_example&#x27;, &#x27;routing_policy_name&#x27;: &#x27;routing_policy_name_example&#x27;, &#x27;rule_set_names&#x27;: [], &#x27;ssl_configuration&#x27;: {&#x27;certificate_ids&#x27;: [], &#x27;certificate_name&#x27;: &#x27;certificate_name_example&#x27;, &#x27;cipher_suite_name&#x27;: &#x27;cipher_suite_name_example&#x27;, &#x27;protocols&#x27;: [], &#x27;server_order_preference&#x27;: &#x27;ENABLED&#x27;, &#x27;trusted_certificate_authority_ids&#x27;: [], &#x27;verify_depth&#x27;: 56, &#x27;verify_peer_certificate&#x27;: True}}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/connection_configuration"></div>
                    <b>connection_configuration</b>
                    <a class="ansibleOptionLink" href="#return-listener/connection_configuration" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/connection_configuration/backend_tcp_proxy_protocol_version"></div>
                    <b>backend_tcp_proxy_protocol_version</b>
                    <a class="ansibleOptionLink" href="#return-listener/connection_configuration/backend_tcp_proxy_protocol_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The backend TCP Proxy Protocol version.</div>
                                            <div>Example: `1`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/connection_configuration/idle_timeout"></div>
                    <b>idle_timeout</b>
                    <a class="ansibleOptionLink" href="#return-listener/connection_configuration/idle_timeout" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum idle time, in seconds, allowed between two successive receive or two successive send operations between the client and backend servers. A send operation does not reset the timer for receive operations. A receive operation does not reset the timer for send operations.</div>
                                            <div>For more information, see <a href='https://docs.cloud.oracle.com/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration'>Connection Configuration</a>.</div>
                                            <div>Example: `1200`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/default_backend_set_name"></div>
                    <b>default_backend_set_name</b>
                    <a class="ansibleOptionLink" href="#return-listener/default_backend_set_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the associated backend set.</div>
                                            <div>Example: `example_backend_set`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">default_backend_set_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/hostname_names"></div>
                    <b>hostname_names</b>
                    <a class="ansibleOptionLink" href="#return-listener/hostname_names" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of hostname resource names.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-listener/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A friendly name for the listener. It must be unique and it cannot be changed.</div>
                                            <div>Example: `example_listener`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/path_route_set_name"></div>
                    <b>path_route_set_name</b>
                    <a class="ansibleOptionLink" href="#return-listener/path_route_set_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Deprecated. Please use `routingPolicies` instead.</div>
                                            <div>The name of the set of path-based routing rules, <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/'>PathRouteSet</a>, applied to this listener&#x27;s traffic.</div>
                                            <div>Example: `example_path_route_set`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_route_set_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-listener/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The communication port for the listener.</div>
                                            <div>Example: `80`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-listener/protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The protocol on which the listener accepts connection requests. To get a list of valid protocols, use the <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols'>ListProtocols</a> operation.</div>
                                            <div>Example: `HTTP`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">protocol_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/routing_policy_name"></div>
                    <b>routing_policy_name</b>
                    <a class="ansibleOptionLink" href="#return-listener/routing_policy_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the routing policy applied to this listener&#x27;s traffic.</div>
                                            <div>Example: `example_routing_policy_name`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">routing_policy_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/rule_set_names"></div>
                    <b>rule_set_names</b>
                    <a class="ansibleOptionLink" href="#return-listener/rule_set_names" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The names of the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/RuleSet/'>rule sets</a> to apply to the listener.</div>
                                            <div>Example: [&quot;example_rule_set&quot;]</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration"></div>
                    <b>ssl_configuration</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration/certificate_ids"></div>
                    <b>certificate_ids</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration/certificate_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Ids for OCI certificates service certificates. Currently only a single Id may be passed.</div>
                                            <div>Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration/certificate_name"></div>
                    <b>certificate_name</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration/certificate_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.</div>
                                            <div>Example: `example_certificate_bundle`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">certificate_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration/cipher_suite_name"></div>
                    <b>cipher_suite_name</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration/cipher_suite_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the cipher suite to use for HTTPS or SSL connections.</div>
                                            <div>If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`.</div>
                                            <div>**Notes:**</div>
                                            <div>*  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher suite. Clients cannot perform an SSL handshake if there is an incompatible configuration. *  You must ensure compatibility between the ciphers configured in the cipher suite and the configured certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA certificates. *  If the cipher configuration is not modified after load balancer creation, the `GET` operation returns `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners that predate this feature. *  If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET` operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for existing listeners that predate this feature. *  The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing backend sets that predate this feature. *  If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field, you must specify an appropriate predefined or custom cipher suite name when updating the resource. *  The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for this field.</div>
                                            <div>example: `example_cipher_suite`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">cipher_suite_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration/protocols"></div>
                    <b>protocols</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration/protocols" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of SSL protocols the load balancer must support for HTTPS or SSL connections.</div>
                                            <div>The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure connection ensures that all data passed between the client and the server is private.</div>
                                            <div>The Load Balancing service supports the following protocols:</div>
                                            <div>*  TLSv1 *  TLSv1.1 *  TLSv1.2</div>
                                            <div>If this field is not specified, TLSv1.2 is the default.</div>
                                            <div>**Warning:** All SSL listeners created on a given port must use the same set of SSL protocols.</div>
                                            <div>**Notes:**</div>
                                            <div>*  The handshake to establish an SSL connection fails if the client supports none of the specified protocols. *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher suite. *  For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation displays a list of SSL protocols currently used by those resources.</div>
                                            <div>example: `[&quot;TLSv1.1&quot;, &quot;TLSv1.2&quot;]`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration/server_order_preference"></div>
                    <b>server_order_preference</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration/server_order_preference" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client ciphers.</div>
                                            <div>**Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This field is ignored when the `SSLConfiguration` object is associated with a backend set.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ENABLED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration/trusted_certificate_authority_ids"></div>
                    <b>trusted_certificate_authority_ids</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration/trusted_certificate_authority_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Ids for OCI certificates service CA or CA bundles for the load balancer to trust.</div>
                                            <div>Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration/verify_depth"></div>
                    <b>verify_depth</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration/verify_depth" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum depth for peer certificate chain verification.</div>
                                            <div>Example: `3`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-listener/ssl_configuration/verify_peer_certificate"></div>
                    <b>verify_peer_certificate</b>
                    <a class="ansibleOptionLink" href="#return-listener/ssl_configuration/verify_peer_certificate" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the load balancer listener should verify peer certificates.</div>
                                            <div>Example: `true`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
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

