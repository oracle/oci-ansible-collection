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

.. _ansible_collections.oracle.oci.oci_loadbalancer_load_balancer_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_loadbalancer_load_balancer_actions -- Perform actions on a LoadBalancer resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.24.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_loadbalancer_load_balancer_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on a LoadBalancer resource in Oracle Cloud Infrastructure
- For *action=change_compartment*, moves a load balancer into a different compartment within the same tenancy. For information about moving resources between compartments, see `Moving Resources to a Different Compartment <https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes>`_.


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
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>change_compartment</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the LoadBalancer.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment to move the load balancer to.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the load balancer to move.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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

    
    - name: Perform action change_compartment on load_balancer
      oci_loadbalancer_load_balancer_actions:
        # required
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        action: change_compartment





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
                    <div class="ansibleOptionAnchor" id="return-load_balancer"></div>
                    <b>load_balancer</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the LoadBalancer resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;backend_sets&#x27;: {&#x27;backends&#x27;: [{&#x27;backup&#x27;: True, &#x27;drain&#x27;: True, &#x27;ip_address&#x27;: &#x27;ip_address_example&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;offline&#x27;: True, &#x27;port&#x27;: 56, &#x27;weight&#x27;: 56}], &#x27;health_checker&#x27;: {&#x27;interval_in_millis&#x27;: 56, &#x27;port&#x27;: 56, &#x27;protocol&#x27;: &#x27;protocol_example&#x27;, &#x27;response_body_regex&#x27;: &#x27;response_body_regex_example&#x27;, &#x27;retries&#x27;: 56, &#x27;return_code&#x27;: 56, &#x27;timeout_in_millis&#x27;: 56, &#x27;url_path&#x27;: &#x27;url_path_example&#x27;}, &#x27;lb_cookie_session_persistence_configuration&#x27;: {&#x27;cookie_name&#x27;: &#x27;cookie_name_example&#x27;, &#x27;disable_fallback&#x27;: True, &#x27;domain&#x27;: &#x27;domain_example&#x27;, &#x27;is_http_only&#x27;: True, &#x27;is_secure&#x27;: True, &#x27;max_age_in_seconds&#x27;: 56, &#x27;path&#x27;: &#x27;path_example&#x27;}, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;policy&#x27;: &#x27;policy_example&#x27;, &#x27;session_persistence_configuration&#x27;: {&#x27;cookie_name&#x27;: &#x27;cookie_name_example&#x27;, &#x27;disable_fallback&#x27;: True}, &#x27;ssl_configuration&#x27;: {&#x27;certificate_ids&#x27;: [], &#x27;certificate_name&#x27;: &#x27;certificate_name_example&#x27;, &#x27;cipher_suite_name&#x27;: &#x27;cipher_suite_name_example&#x27;, &#x27;protocols&#x27;: [], &#x27;server_order_preference&#x27;: &#x27;ENABLED&#x27;, &#x27;trusted_certificate_authority_ids&#x27;: [], &#x27;verify_depth&#x27;: 56, &#x27;verify_peer_certificate&#x27;: True}}, &#x27;certificates&#x27;: {&#x27;ca_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----&#x27;, &#x27;certificate_name&#x27;: &#x27;certificate_name_example&#x27;, &#x27;public_certificate&#x27;: &#x27;-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----&#x27;}, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;hostnames&#x27;: {&#x27;hostname&#x27;: &#x27;hostname_example&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;ip_addresses&#x27;: [{&#x27;ip_address&#x27;: &#x27;ip_address_example&#x27;, &#x27;is_public&#x27;: True, &#x27;reserved_ip&#x27;: {&#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;}}], &#x27;is_private&#x27;: True, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;listeners&#x27;: {&#x27;connection_configuration&#x27;: {&#x27;backend_tcp_proxy_protocol_version&#x27;: 56, &#x27;idle_timeout&#x27;: 56}, &#x27;default_backend_set_name&#x27;: &#x27;default_backend_set_name_example&#x27;, &#x27;hostname_names&#x27;: [], &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;path_route_set_name&#x27;: &#x27;path_route_set_name_example&#x27;, &#x27;port&#x27;: 56, &#x27;protocol&#x27;: &#x27;protocol_example&#x27;, &#x27;routing_policy_name&#x27;: &#x27;routing_policy_name_example&#x27;, &#x27;rule_set_names&#x27;: [], &#x27;ssl_configuration&#x27;: {&#x27;certificate_ids&#x27;: [], &#x27;certificate_name&#x27;: &#x27;certificate_name_example&#x27;, &#x27;cipher_suite_name&#x27;: &#x27;cipher_suite_name_example&#x27;, &#x27;protocols&#x27;: [], &#x27;server_order_preference&#x27;: &#x27;ENABLED&#x27;, &#x27;trusted_certificate_authority_ids&#x27;: [], &#x27;verify_depth&#x27;: 56, &#x27;verify_peer_certificate&#x27;: True}}, &#x27;network_security_group_ids&#x27;: [], &#x27;path_route_sets&#x27;: {&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;path_routes&#x27;: [{&#x27;backend_set_name&#x27;: &#x27;backend_set_name_example&#x27;, &#x27;path&#x27;: &#x27;path_example&#x27;, &#x27;path_match_type&#x27;: {&#x27;match_type&#x27;: &#x27;EXACT_MATCH&#x27;}}]}, &#x27;routing_policies&#x27;: {&#x27;condition_language_version&#x27;: &#x27;V1&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;rules&#x27;: [{&#x27;actions&#x27;: [{&#x27;backend_set_name&#x27;: &#x27;backend_set_name_example&#x27;, &#x27;name&#x27;: &#x27;FORWARD_TO_BACKENDSET&#x27;}], &#x27;condition&#x27;: &#x27;condition_example&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;}]}, &#x27;rule_sets&#x27;: {&#x27;items&#x27;: [{&#x27;action&#x27;: &#x27;ADD_HTTP_REQUEST_HEADER&#x27;, &#x27;allowed_methods&#x27;: [], &#x27;are_invalid_characters_allowed&#x27;: True, &#x27;conditions&#x27;: [{&#x27;attribute_name&#x27;: &#x27;SOURCE_IP_ADDRESS&#x27;, &#x27;attribute_value&#x27;: &#x27;attribute_value_example&#x27;, &#x27;operator&#x27;: &#x27;EXACT_MATCH&#x27;}], &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;header&#x27;: &#x27;header_example&#x27;, &#x27;http_large_header_size_in_kb&#x27;: 56, &#x27;prefix&#x27;: &#x27;prefix_example&#x27;, &#x27;redirect_uri&#x27;: {&#x27;host&#x27;: &#x27;host_example&#x27;, &#x27;path&#x27;: &#x27;path_example&#x27;, &#x27;port&#x27;: 56, &#x27;protocol&#x27;: &#x27;protocol_example&#x27;, &#x27;query&#x27;: &#x27;query_example&#x27;}, &#x27;response_code&#x27;: 56, &#x27;status_code&#x27;: 56, &#x27;suffix&#x27;: &#x27;suffix_example&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}], &#x27;name&#x27;: &#x27;name_example&#x27;}, &#x27;shape_details&#x27;: {&#x27;maximum_bandwidth_in_mbps&#x27;: 56, &#x27;minimum_bandwidth_in_mbps&#x27;: 56}, &#x27;shape_name&#x27;: &#x27;shape_name_example&#x27;, &#x27;ssl_cipher_suites&#x27;: {&#x27;ciphers&#x27;: [], &#x27;name&#x27;: &#x27;name_example&#x27;}, &#x27;subnet_ids&#x27;: [], &#x27;system_tags&#x27;: {}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets"></div>
                    <b>backend_sets</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/backends"></div>
                    <b>backends</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/backends" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/backends/backup"></div>
                    <b>backup</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/backends/backup" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress traffic to this backend server unless all other backend servers not marked as &quot;backup&quot; fail the health check policy.</div>
                                            <div>**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy.</div>
                                            <div>Example: `false`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/backends/drain"></div>
                    <b>drain</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/backends/drain" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the load balancer should drain this server. Servers marked &quot;drain&quot; receive no new incoming traffic.</div>
                                            <div>Example: `false`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/backends/ip_address"></div>
                    <b>ip_address</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/backends/ip_address" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IP address of the backend server.</div>
                                            <div>Example: `10.0.0.3`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ip_address_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/backends/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/backends/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A read-only field showing the IP address and port that uniquely identify this backend server in the backend set.</div>
                                            <div>Example: `10.0.0.3:8080`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/backends/offline"></div>
                    <b>offline</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/backends/offline" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the load balancer should treat this server as offline. Offline servers receive no incoming traffic.</div>
                                            <div>Example: `false`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/backends/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/backends/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The communication port for the backend server.</div>
                                            <div>Example: `8080`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/backends/weight"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/backends/weight" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger proportion of incoming traffic. For example, a server weighted &#x27;3&#x27; receives 3 times the number of new connections as a server weighted &#x27;1&#x27;. For more information on load balancing policies, see <a href='https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm'>How Load Balancing Policies Work</a>.</div>
                                            <div>Example: `3`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker"></div>
                    <b>health_checker</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker/interval_in_millis"></div>
                    <b>interval_in_millis</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker/interval_in_millis" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The interval between health checks, in milliseconds. The default is 10000 (10 seconds).</div>
                                            <div>Example: `10000`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The backend server port against which to run the health check. If the port is not specified, the load balancer uses the port information from the `Backend` object.</div>
                                            <div>Example: `8080`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker/protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The protocol the health check must use; either HTTP or TCP.</div>
                                            <div>Example: `HTTP`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">protocol_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker/response_body_regex"></div>
                    <b>response_body_regex</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker/response_body_regex" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A regular expression for parsing the response body from the backend server.</div>
                                            <div>Example: `^((?!false).|\s)*$`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">response_body_regex_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker/retries"></div>
                    <b>retries</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker/retries" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of retries to attempt before a backend server is considered &quot;unhealthy&quot;. This number also applies when recovering a server to the &quot;healthy&quot; state. Defaults to 3.</div>
                                            <div>Example: `3`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker/return_code"></div>
                    <b>return_code</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker/return_code" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol, you can use common HTTP status codes such as &quot;200&quot;.</div>
                                            <div>Example: `200`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker/timeout_in_millis"></div>
                    <b>timeout_in_millis</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker/timeout_in_millis" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. Defaults to 3000 (3 seconds).</div>
                                            <div>Example: `3000`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/health_checker/url_path"></div>
                    <b>url_path</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/health_checker/url_path" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The path against which to run the health check.</div>
                                            <div>Example: `/healthcheck`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">url_path_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration"></div>
                    <b>lb_cookie_session_persistence_configuration</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/cookie_name"></div>
                    <b>cookie_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/cookie_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the cookie inserted by the load balancer. If this field is not configured, the cookie name defaults to &quot;X-Oracle-BMC-LBS-Route&quot;.</div>
                                            <div>Example: `example_cookie`</div>
                                            <div>**Notes:**</div>
                                            <div>*  Ensure that the cookie name used at the backend application servers is different from the cookie name used at the load balancer. To minimize the chance of name collision, Oracle recommends that you use a prefix such as &quot;X-Oracle-OCI-&quot; for this field.</div>
                                            <div>*  If a backend server and the load balancer both insert cookies with the same name, the client or browser behavior can vary depending on the domain and path values associated with the cookie. If the name, domain, and path values of the `Set-cookie` generated by a backend server and the `Set-cookie` generated by the load balancer are all the same, the client or browser treats them as one cookie and returns only one of the cookie values in subsequent requests. If both `Set-cookie` names are the same, but the domain and path names are different, the client or browser treats them as two different cookies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">cookie_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/disable_fallback"></div>
                    <b>disable_fallback</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/disable_fallback" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false.</div>
                                            <div>Example: `false`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/domain"></div>
                    <b>domain</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/domain" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The domain in which the cookie is valid. The `Set-cookie` header inserted by the load balancer contains a domain attribute with the specified value.</div>
                                            <div>This attribute has no default value. If you do not specify a value, the load balancer does not insert the domain attribute into the `Set-cookie` header.</div>
                                            <div>**Notes:**</div>
                                            <div>*  <a href='https://www.ietf.org/rfc/rfc6265.txt'>RFC 6265 - HTTP State Management Mechanism</a> describes client and browser behavior when the domain attribute is present or not present in the `Set-cookie` header.</div>
                                            <div>If the value of the `Domain` attribute is `example.com` in the `Set-cookie` header, the client includes the same cookie in the `Cookie` header when making HTTP requests to `example.com`, `www.example.com`, and `www.abc.example.com`. If the `Domain` attribute is not present, the client returns the cookie only for the domain to which the original request was made.</div>
                                            <div>*  Ensure that this attribute specifies the correct domain value. If the `Domain` attribute in the `Set-cookie` header does not include the domain to which the original request was made, the client or browser might reject the cookie. As specified in RFC 6265, the client accepts a cookie with the `Domain` attribute value `example.com` or `www.example.com` sent from `www.example.com`. It does not accept a cookie with the `Domain` attribute `abc.example.com` or `www.abc.example.com` sent from `www.example.com`.</div>
                                            <div>Example: `example.com`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">domain_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/is_http_only"></div>
                    <b>is_http_only</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/is_http_only" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the `Set-cookie` header should contain the `HttpOnly` attribute. If `true`, the `Set-cookie` header inserted by the load balancer contains the `HttpOnly` attribute, which limits the scope of the cookie to HTTP requests. This attribute directs the client or browser to omit the cookie when providing access to cookies through non-HTTP APIs. For example, it restricts the cookie from JavaScript channels.</div>
                                            <div>Example: `true`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/is_secure"></div>
                    <b>is_secure</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/is_secure" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the `Set-cookie` header should contain the `Secure` attribute. If `true`, the `Set-cookie` header inserted by the load balancer contains the `Secure` attribute, which directs the client or browser to send the cookie only using a secure protocol.</div>
                                            <div>**Note:** If you set this field to `true`, you cannot associate the corresponding backend set with an HTTP listener.</div>
                                            <div>Example: `true`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/max_age_in_seconds"></div>
                    <b>max_age_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/max_age_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The amount of time the cookie remains valid. The `Set-cookie` header inserted by the load balancer contains a `Max-Age` attribute with the specified value.</div>
                                            <div>The specified value must be at least one second. There is no default value for this attribute. If you do not specify a value, the load balancer does not include the `Max-Age` attribute in the `Set-cookie` header. In most cases, the client or browser retains the cookie until the current session ends, as defined by the client.</div>
                                            <div>Example: `3600`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/lb_cookie_session_persistence_configuration/path" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The path in which the cookie is valid. The `Set-cookie header` inserted by the load balancer contains a `Path` attribute with the specified value.</div>
                                            <div>Clients include the cookie in an HTTP request only if the path portion of the request-uri matches, or is a subdirectory of, the cookie&#x27;s `Path` attribute.</div>
                                            <div>The default value is `/`.</div>
                                            <div>Example: `/example`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A friendly name for the backend set. It must be unique and it cannot be changed.</div>
                                            <div>Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot contain spaces. Avoid entering confidential information.</div>
                                            <div>Example: `example_backend_set`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/policy"></div>
                    <b>policy</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/policy" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The load balancer policy for the backend set. To get a list of available policies, use the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerPolicy/ListPolicies'>ListPolicies</a> operation.</div>
                                            <div>Example: `LEAST_CONNECTIONS`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">policy_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/session_persistence_configuration"></div>
                    <b>session_persistence_configuration</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/session_persistence_configuration" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/session_persistence_configuration/cookie_name"></div>
                    <b>cookie_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/session_persistence_configuration/cookie_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the cookie used to detect a session initiated by the backend server. Use &#x27;*&#x27; to specify that any cookie set by the backend causes the session to persist.</div>
                                            <div>Example: `example_cookie`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">cookie_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/session_persistence_configuration/disable_fallback"></div>
                    <b>disable_fallback</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/session_persistence_configuration/disable_fallback" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the load balancer is prevented from directing traffic from a persistent session client to a different backend server if the original server is unavailable. Defaults to false.</div>
                                            <div>Example: `false`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration"></div>
                    <b>ssl_configuration</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration/certificate_ids"></div>
                    <b>certificate_ids</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration/certificate_ids" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration/certificate_name"></div>
                    <b>certificate_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration/certificate_name" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration/cipher_suite_name"></div>
                    <b>cipher_suite_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration/cipher_suite_name" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration/protocols"></div>
                    <b>protocols</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration/protocols" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration/server_order_preference"></div>
                    <b>server_order_preference</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration/server_order_preference" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration/trusted_certificate_authority_ids"></div>
                    <b>trusted_certificate_authority_ids</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration/trusted_certificate_authority_ids" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration/verify_depth"></div>
                    <b>verify_depth</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration/verify_depth" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/backend_sets/ssl_configuration/verify_peer_certificate"></div>
                    <b>verify_peer_certificate</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/backend_sets/ssl_configuration/verify_peer_certificate" title="Permalink to this return value"></a>
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
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/certificates"></div>
                    <b>certificates</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/certificates" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/certificates/ca_certificate"></div>
                    <b>ca_certificate</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/certificates/ca_certificate" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.</div>
                                            <div>Example:</div>
                                            <div>-----BEGIN CERTIFICATE----- MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy ... -----END CERTIFICATE-----</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/certificates/certificate_name"></div>
                    <b>certificate_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/certificates/certificate_name" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/certificates/public_certificate"></div>
                    <b>public_certificate</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/certificates/public_certificate" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The public certificate, in PEM format, that you received from your SSL certificate provider.</div>
                                            <div>Example:</div>
                                            <div>-----BEGIN CERTIFICATE----- MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw ... -----END CERTIFICATE-----</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment containing the load balancer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name. It does not have to be unique, and it is changeable.</div>
                                            <div>Example: `example_load_balancer`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/hostnames"></div>
                    <b>hostnames</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/hostnames" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/hostnames/hostname"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/hostnames/hostname" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A virtual hostname. For more information about virtual hostname string construction, see <a href='https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm#routing'>Managing Request Routing</a>.</div>
                                            <div>Example: `app.example.com`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">hostname_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/hostnames/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/hostnames/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential information.</div>
                                            <div>Example: `example_hostname_001`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the load balancer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/ip_addresses"></div>
                    <b>ip_addresses</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/ip_addresses" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of IP addresses.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/ip_addresses/ip_address"></div>
                    <b>ip_address</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/ip_addresses/ip_address" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An IP address.</div>
                                            <div>Example: `192.168.0.3`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ip_address_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/ip_addresses/is_public"></div>
                    <b>is_public</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/ip_addresses/is_public" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the IP address is public or private.</div>
                                            <div>If &quot;true&quot;, the IP address is public and accessible from the internet.</div>
                                            <div>If &quot;false&quot;, the IP address is private and accessible only from within the associated VCN.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/ip_addresses/reserved_ip"></div>
                    <b>reserved_ip</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/ip_addresses/reserved_ip" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/ip_addresses/reserved_ip/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/ip_addresses/reserved_ip/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/is_private"></div>
                    <b>is_private</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/is_private" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the load balancer has a VCN-local (private) IP address.</div>
                                            <div>If &quot;true&quot;, the service assigns a private IP address to the load balancer.</div>
                                            <div>If &quot;false&quot;, the service assigns a public IP address to the load balancer.</div>
                                            <div>A public load balancer is accessible from the internet, depending on your VCN&#x27;s <a href='https://docs.cloud.oracle.com/Content/Network/Concepts/securitylists.htm'>security list rules</a>. For more information about public and private load balancers, see <a href='https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-load- balancing-works'>How Load Balancing Works</a>.</div>
                                            <div>Example: `true`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the load balancer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners"></div>
                    <b>listeners</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/connection_configuration"></div>
                    <b>connection_configuration</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/connection_configuration" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/connection_configuration/backend_tcp_proxy_protocol_version"></div>
                    <b>backend_tcp_proxy_protocol_version</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/connection_configuration/backend_tcp_proxy_protocol_version" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/connection_configuration/idle_timeout"></div>
                    <b>idle_timeout</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/connection_configuration/idle_timeout" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/default_backend_set_name"></div>
                    <b>default_backend_set_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/default_backend_set_name" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/hostname_names"></div>
                    <b>hostname_names</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/hostname_names" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/name" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/path_route_set_name"></div>
                    <b>path_route_set_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/path_route_set_name" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/port" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/protocol" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/routing_policy_name"></div>
                    <b>routing_policy_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/routing_policy_name" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/rule_set_names"></div>
                    <b>rule_set_names</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/rule_set_names" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration"></div>
                    <b>ssl_configuration</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration/certificate_ids"></div>
                    <b>certificate_ids</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration/certificate_ids" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration/certificate_name"></div>
                    <b>certificate_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration/certificate_name" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration/cipher_suite_name"></div>
                    <b>cipher_suite_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration/cipher_suite_name" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration/protocols"></div>
                    <b>protocols</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration/protocols" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration/server_order_preference"></div>
                    <b>server_order_preference</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration/server_order_preference" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration/trusted_certificate_authority_ids"></div>
                    <b>trusted_certificate_authority_ids</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration/trusted_certificate_authority_ids" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration/verify_depth"></div>
                    <b>verify_depth</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration/verify_depth" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/listeners/ssl_configuration/verify_peer_certificate"></div>
                    <b>verify_peer_certificate</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/listeners/ssl_configuration/verify_peer_certificate" title="Permalink to this return value"></a>
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
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/network_security_group_ids"></div>
                    <b>network_security_group_ids</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/network_security_group_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of NSG <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCIDs</a> associated with the load balancer.</div>
                                            <div>During the load balancer&#x27;s creation, the service adds the new load balancer to the specified NSGs.</div>
                                            <div>The benefits of associating the load balancer with NSGs include:</div>
                                            <div>*  NSGs define network security rules to govern ingress and egress traffic for the load balancer.</div>
                                            <div>*  The network security rules of other resources can reference the NSGs associated with the load balancer to ensure access.</div>
                                            <div>Example: [&quot;ocid1.nsg.oc1.phx.unique_ID&quot;]</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/path_route_sets"></div>
                    <b>path_route_sets</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/path_route_sets" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/path_route_sets/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/path_route_sets/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The unique name for this set of path route rules. Avoid entering confidential information.</div>
                                            <div>Example: `example_path_route_set`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/path_route_sets/path_routes"></div>
                    <b>path_routes</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/path_route_sets/path_routes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The set of path route rules.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/path_route_sets/path_routes/backend_set_name"></div>
                    <b>backend_set_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/path_route_sets/path_routes/backend_set_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the target backend set for requests where the incoming URI matches the specified path.</div>
                                            <div>Example: `example_backend_set`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">backend_set_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/path_route_sets/path_routes/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/path_route_sets/path_routes/path" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The path string to match against the incoming URI path.</div>
                                            <div>*  Path strings are case-insensitive.</div>
                                            <div>*  Asterisk (*) wildcards are not supported.</div>
                                            <div>*  Regular expressions are not supported.</div>
                                            <div>Example: `/example/video/123`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/path_route_sets/path_routes/path_match_type"></div>
                    <b>path_match_type</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/path_route_sets/path_routes/path_match_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of matching to apply to incoming URIs.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/path_route_sets/path_routes/path_match_type/match_type"></div>
                    <b>match_type</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/path_route_sets/path_routes/path_match_type/match_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies how the load balancing service compares a <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/loadbalancer/20170115/requests/PathRoute'>PathRoute</a> object&#x27;s `path` string against the incoming URI.</div>
                                            <div>*  **EXACT_MATCH** - Looks for a `path` string that exactly matches the incoming URI path.</div>
                                            <div>*  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `path` string with the best, longest match of the beginning portion of the incoming URI path.</div>
                                            <div>*  **PREFIX_MATCH** - Looks for a `path` string that matches the beginning portion of the incoming URI path.</div>
                                            <div>*  **SUFFIX_MATCH** - Looks for a `path` string that matches the ending portion of the incoming URI path.</div>
                                            <div>For a full description of how the system handles `matchType` in a path route set containing multiple rules, see <a href='https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm'>Managing Request Routing</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">EXACT_MATCH</div>
                                    </td>
            </tr>
                    
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies"></div>
                    <b>routing_policies</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies/condition_language_version"></div>
                    <b>condition_language_version</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies/condition_language_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The version of the language in which `condition` of `rules` are composed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">V1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The unique name for this list of routing rules. Avoid entering confidential information.</div>
                                            <div>Example: `example_routing_policy`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies/rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The ordered list of routing rules.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies/rules/actions"></div>
                    <b>actions</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies/rules/actions" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of actions to be applied when conditions of the routing rule are met.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies/rules/actions/backend_set_name"></div>
                    <b>backend_set_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies/rules/actions/backend_set_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the backend set the listener will forward the traffic to.</div>
                                            <div>Example: `backendSetForImages`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">backend_set_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies/rules/actions/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies/rules/actions/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FORWARD_TO_BACKENDSET</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies/rules/condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A routing rule to evaluate defined conditions against the incoming HTTP request and perform an action.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">condition_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/routing_policies/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/routing_policies/rules/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A unique name for the routing policy rule. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets"></div>
                    <b>rule_sets</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of rules that compose the rule set.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ADD_HTTP_REQUEST_HEADER</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/allowed_methods"></div>
                    <b>allowed_methods</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/allowed_methods" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of HTTP methods allowed for this listener.</div>
                                            <div>By default, you can specify only the standard HTTP methods defined in the <a href='http://www.iana.org/assignments/http-methods/http-methods.xhtml'>HTTP Method Registry</a>. You can also see a list of supported standard HTTP methods in the Load Balancing service documentation at <a href='https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm'>Managing Rule Sets</a>.</div>
                                            <div>Your backend application must be able to handle the methods specified in this list.</div>
                                            <div>The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact <a href='http://support.oracle.com/'>My Oracle Support</a> to remove the restriction for your tenancy.</div>
                                            <div>Example: [&quot;GET&quot;, &quot;PUT&quot;, &quot;POST&quot;, &quot;PROPFIND&quot;]</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/are_invalid_characters_allowed"></div>
                    <b>are_invalid_characters_allowed</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/are_invalid_characters_allowed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether or not invalid characters in client header fields will be allowed. Valid names are composed of English letters, digits, hyphens and underscores. If &quot;true&quot;, invalid characters are allowed in the HTTP header. If &quot;false&quot;, invalid characters are not allowed in the HTTP header</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/conditions"></div>
                    <b>conditions</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/conditions" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/conditions/attribute_name"></div>
                    <b>attribute_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/conditions/attribute_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SOURCE_IP_ADDRESS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/conditions/attribute_value"></div>
                    <b>attribute_value</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/conditions/attribute_value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The path string that the redirection rule applies to.</div>
                                            <div>Example: `/example`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">attribute_value_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/conditions/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/conditions/operator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A string that specifies how to compare the PathMatchCondition object&#x27;s `attributeValue` string to the incoming URI.</div>
                                            <div>*  **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string.</div>
                                            <div>*  **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best, longest match of the beginning portion of the incoming URI path.</div>
                                            <div>*  **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the `attributeValue` string.</div>
                                            <div>*  **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue` string.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">EXACT_MATCH</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A brief description of the access control rule. Avoid entering confidential information.</div>
                                            <div>example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/header"></div>
                    <b>header</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/header" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A header name that conforms to RFC 7230.</div>
                                            <div>Example: `example_header_name`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">header_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/http_large_header_size_in_kb"></div>
                    <b>http_large_header_size_in_kb</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/http_large_header_size_in_kb" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum size of each buffer used for reading http client request header. This value indicates the maximum size allowed for each buffer. The allowed values for buffer size are 8, 16, 32 and 64.</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/prefix"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/prefix" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A string to prepend to the header value. The resulting header value must conform to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_prefix_value`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">prefix_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/redirect_uri"></div>
                    <b>redirect_uri</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/redirect_uri" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/redirect_uri/host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/redirect_uri/host" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The valid domain name (hostname) or IP address to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the incoming HTTP request URI.</div>
                                            <div>All RedirectUri tokens are valid for this property. You can use any token more than once.</div>
                                            <div>Curly braces are valid in this property only to surround tokens, such as `{host}`</div>
                                            <div>Examples:</div>
                                            <div>*  **example.com** appears as `example.com` in the redirect URI.</div>
                                            <div>*  **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the incoming HTTP request URI.</div>
                                            <div>*  **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and the port is `8081` in the incoming HTTP request URI.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">host_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/redirect_uri/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/redirect_uri/path" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The HTTP URI path to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{path}`, the service preserves the original path from the incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, &quot;&quot;.</div>
                                            <div>All RedirectUri tokens are valid for this property. You can use any token more than once.</div>
                                            <div>The path string must begin with `/` if it does not begin with the `{path}` token.</div>
                                            <div>Examples:</div>
                                            <div>*  __/example/video/123__ appears as `/example/video/123` in the redirect URI.</div>
                                            <div>*  __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __/{host}/123__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname in the incoming HTTP request URI.</div>
                                            <div>*  __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and `123` is the port in the incoming HTTP request URI.</div>
                                            <div>*  __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP request URI.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/redirect_uri/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/redirect_uri/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The communication port to use in the redirect URI.</div>
                                            <div>Valid values include integers from 1 to 65535.</div>
                                            <div>When this value is null, the service preserves the original port from the incoming HTTP request URI.</div>
                                            <div>Example: `8081`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/redirect_uri/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/redirect_uri/protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The HTTP protocol to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the incoming HTTP request URI. Allowed values are:</div>
                                            <div>*  HTTP *  HTTPS *  {protocol}</div>
                                            <div>`{protocol}` is the only valid token for this property. It can appear only once in the value string.</div>
                                            <div>Example: `HTTPS`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">protocol_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/redirect_uri/query"></div>
                    <b>query</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/redirect_uri/query" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The query string to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{query}`, the service preserves the original query parameters from the incoming HTTP request URI.</div>
                                            <div>All `RedirectUri` tokens are valid for this property. You can use any token more than once.</div>
                                            <div>If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character.</div>
                                            <div>You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand (&amp;) character. To omit all incoming query parameters from the redirect URI, set this value to an empty string, &quot;&quot;.</div>
                                            <div>If the specified query string results in a redirect URI ending with `?` or `&amp;`, the last character is truncated. For example, if the incoming URI is `http://host.com:8080/documents` and the query property value is `?lang=en&amp;{query}`, the redirect URI is `http://host.com:8080/documents?lang=en`. The system truncates the final ampersand (&amp;) because the incoming URI included no value to replace the {query} token.</div>
                                            <div>Examples: * **lang=en&amp;time_zone=PST** appears as `lang=en&amp;time_zone=PST` in the redirect URI.</div>
                                            <div>* **{query}** appears as `lang=en&amp;time_zone=PST` in the redirect URI if `lang=en&amp;time_zone=PST` is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}` token renders as an empty string.</div>
                                            <div>* **lang=en&amp;{query}&amp;time_zone=PST** appears as `lang=en&amp;country=us&amp;time_zone=PST` in the redirect URI if `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, this value renders as `lang=en&amp;time_zone=PST`.</div>
                                            <div>*  **protocol={protocol}&amp;hostname={host}** appears as `protocol=http&amp;hostname=example.com` in the redirect URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request.</div>
                                            <div>*  **port={port}&amp;hostname={host}** appears as `port=8080&amp;hostname=example.com` in the redirect URI if the port is `8080` and the hostname is `example.com` in the incoming HTTP request URI.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">query_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/response_code"></div>
                    <b>response_code</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/response_code" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The HTTP status code to return when the incoming request is redirected.</div>
                                            <div>The status line returned with the code is mapped from the standard HTTP specification. Valid response codes for redirection are:</div>
                                            <div>*  301 *  302 *  303 *  307 *  308</div>
                                            <div>The default value is `302` (Found).</div>
                                            <div>Example: `301`</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/status_code"></div>
                    <b>status_code</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/status_code" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The HTTP status code to return when the requested HTTP method is not in the list of allowed methods. The associated status line returned with the code is mapped from the standard HTTP specification. The default value is `405 (Method Not Allowed)`.</div>
                                            <div>Example: 403</div>
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
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/suffix"></div>
                    <b>suffix</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/suffix" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A string to append to the header value. The resulting header value must conform to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_suffix_value`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">suffix_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/items/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/items/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A header value that conforms to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_value`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/rule_sets/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/rule_sets/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information.</div>
                                            <div>Example: `example_rule_set`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/shape_details"></div>
                    <b>shape_details</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/shape_details" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/shape_details/maximum_bandwidth_in_mbps"></div>
                    <b>maximum_bandwidth_in_mbps</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/shape_details/maximum_bandwidth_in_mbps" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Bandwidth in Mbps that determines the maximum bandwidth (ingress plus egress) that the load balancer can achieve. This bandwidth cannot be always guaranteed. For a guaranteed bandwidth use the minimumBandwidthInMbps parameter.</div>
                                            <div>The values must be between minimumBandwidthInMbps and 8000 (8Gbps).</div>
                                            <div>Example: `1500`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/shape_details/minimum_bandwidth_in_mbps"></div>
                    <b>minimum_bandwidth_in_mbps</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/shape_details/minimum_bandwidth_in_mbps" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Bandwidth in Mbps that determines the total pre-provisioned bandwidth (ingress plus egress). The values must be between 10 and the maximumBandwidthInMbps.</div>
                                            <div>Example: `150`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/shape_name"></div>
                    <b>shape_name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/shape_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A template that determines the total pre-provisioned bandwidth (ingress plus egress). To get a list of available shapes, use the <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerShape/ListShapes'>ListShapes</a> operation.</div>
                                            <div>Example: `100Mbps`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">shape_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/ssl_cipher_suites"></div>
                    <b>ssl_cipher_suites</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/ssl_cipher_suites" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/ssl_cipher_suites/ciphers"></div>
                    <b>ciphers</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/ssl_cipher_suites/ciphers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of SSL ciphers the load balancer must support for HTTPS or SSL connections.</div>
                                            <div>The following ciphers are valid values for this property:</div>
                                            <div>*  __TLSv1.2 ciphers__</div>
                                            <div>&quot;AES128-GCM-SHA256&quot; &quot;AES128-SHA256&quot; &quot;AES256-GCM-SHA384&quot; &quot;AES256-SHA256&quot; &quot;DH-DSS-AES128-GCM-SHA256&quot; &quot;DH-DSS-AES128-SHA256&quot; &quot;DH-DSS-AES256-GCM-SHA384&quot; &quot;DH-DSS-AES256-SHA256&quot; &quot;DH-RSA-AES128-GCM-SHA256&quot; &quot;DH-RSA-AES128-SHA256&quot; &quot;DH-RSA-AES256-GCM-SHA384&quot; &quot;DH-RSA-AES256-SHA256&quot; &quot;DHE-DSS-AES128-GCM-SHA256&quot; &quot;DHE-DSS-AES128-SHA256&quot; &quot;DHE-DSS-AES256-GCM-SHA384&quot; &quot;DHE-DSS-AES256-SHA256&quot; &quot;DHE-RSA-AES128-GCM-SHA256&quot; &quot;DHE-RSA-AES128-SHA256&quot; &quot;DHE-RSA-AES256-GCM-SHA384&quot; &quot;DHE-RSA-AES256-SHA256&quot; &quot;ECDH-ECDSA-AES128-GCM-SHA256&quot; &quot;ECDH-ECDSA-AES128-SHA256&quot; &quot;ECDH-ECDSA-AES256-GCM-SHA384&quot; &quot;ECDH-ECDSA-AES256-SHA384&quot; &quot;ECDH-RSA-AES128-GCM-SHA256&quot; &quot;ECDH-RSA-AES128-SHA256&quot; &quot;ECDH-RSA-AES256-GCM-SHA384&quot; &quot;ECDH-RSA-AES256-SHA384&quot; &quot;ECDHE-ECDSA-AES128-GCM-SHA256&quot; &quot;ECDHE-ECDSA-AES128-SHA256&quot; &quot;ECDHE-ECDSA-AES256-GCM-SHA384&quot; &quot;ECDHE-ECDSA-AES256-SHA384&quot; &quot;ECDHE-RSA-AES128-GCM-SHA256&quot; &quot;ECDHE-RSA-AES128-SHA256&quot; &quot;ECDHE-RSA-AES256-GCM-SHA384&quot; &quot;ECDHE-RSA-AES256-SHA384&quot;</div>
                                            <div>*  __TLSv1 ciphers also supported by TLSv1.2__</div>
                                            <div>&quot;AES128-SHA&quot; &quot;AES256-SHA&quot; &quot;CAMELLIA128-SHA&quot; &quot;CAMELLIA256-SHA&quot; &quot;DES-CBC3-SHA&quot; &quot;DH-DSS-AES128-SHA&quot; &quot;DH-DSS-AES256-SHA&quot; &quot;DH-DSS-CAMELLIA128-SHA&quot; &quot;DH-DSS-CAMELLIA256-SHA&quot; &quot;DH-DSS-DES-CBC3-SHAv&quot; &quot;DH-DSS-SEED-SHA&quot; &quot;DH-RSA-AES128-SHA&quot; &quot;DH-RSA-AES256-SHA&quot; &quot;DH-RSA-CAMELLIA128-SHA&quot; &quot;DH-RSA-CAMELLIA256-SHA&quot; &quot;DH-RSA-DES-CBC3-SHA&quot; &quot;DH-RSA-SEED-SHA&quot; &quot;DHE-DSS-AES128-SHA&quot; &quot;DHE-DSS-AES256-SHA&quot; &quot;DHE-DSS-CAMELLIA128-SHA&quot; &quot;DHE-DSS-CAMELLIA256-SHA&quot; &quot;DHE-DSS-DES-CBC3-SHA&quot; &quot;DHE-DSS-SEED-SHA&quot; &quot;DHE-RSA-AES128-SHA&quot; &quot;DHE-RSA-AES256-SHA&quot; &quot;DHE-RSA-CAMELLIA128-SHA&quot; &quot;DHE-RSA-CAMELLIA256-SHA&quot; &quot;DHE-RSA-DES-CBC3-SHA&quot; &quot;DHE-RSA-SEED-SHA&quot; &quot;ECDH-ECDSA-AES128-SHA&quot; &quot;ECDH-ECDSA-AES256-SHA&quot; &quot;ECDH-ECDSA-DES-CBC3-SHA&quot; &quot;ECDH-ECDSA-RC4-SHA&quot; &quot;ECDH-RSA-AES128-SHA&quot; &quot;ECDH-RSA-AES256-SHA&quot; &quot;ECDH-RSA-DES-CBC3-SHA&quot; &quot;ECDH-RSA-RC4-SHA&quot; &quot;ECDHE-ECDSA-AES128-SHA&quot; &quot;ECDHE-ECDSA-AES256-SHA&quot; &quot;ECDHE-ECDSA-DES-CBC3-SHA&quot; &quot;ECDHE-ECDSA-RC4-SHA&quot; &quot;ECDHE-RSA-AES128-SHA&quot; &quot;ECDHE-RSA-AES256-SHA&quot; &quot;ECDHE-RSA-DES-CBC3-SHA&quot; &quot;ECDHE-RSA-RC4-SHA&quot; &quot;IDEA-CBC-SHA&quot; &quot;KRB5-DES-CBC3-MD5&quot; &quot;KRB5-DES-CBC3-SHA&quot; &quot;KRB5-IDEA-CBC-MD5&quot; &quot;KRB5-IDEA-CBC-SHA&quot; &quot;KRB5-RC4-MD5&quot; &quot;KRB5-RC4-SHA&quot; &quot;PSK-3DES-EDE-CBC-SHA&quot; &quot;PSK-AES128-CBC-SHA&quot; &quot;PSK-AES256-CBC-SHA&quot; &quot;PSK-RC4-SHA&quot; &quot;RC4-MD5&quot; &quot;RC4-SHA&quot; &quot;SEED-SHA&quot;</div>
                                            <div>example: `[&quot;ECDHE-RSA-AES256-GCM-SHA384&quot;,&quot;ECDHE-ECDSA-AES256-GCM-SHA384&quot;,&quot;ECDHE-RSA-AES128-GCM-SHA256&quot;]`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/ssl_cipher_suites/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/ssl_cipher_suites/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A friendly name for the SSL cipher suite. It must be unique and it cannot be changed.</div>
                                            <div>**Note:** The name of your user-defined cipher suite must not be the same as any of Oracle&#x27;s predefined or reserved SSL cipher suite names:</div>
                                            <div>* oci-default-ssl-cipher-suite-v1 * oci-modern-ssl-cipher-suite-v1 * oci-compatible-ssl-cipher-suite-v1 * oci-wider-compatible-ssl-cipher-suite-v1 * oci-customized-ssl-cipher-suite</div>
                                            <div>example: `example_cipher_suite`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/subnet_ids"></div>
                    <b>subnet_ids</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/subnet_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of subnet <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCIDs</a>.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>. System tags can be viewed by users, but can only be created by the system.</div>
                                            <div>Example: `{&quot;orcl-cloud&quot;: {&quot;free-tier-retained&quot;: &quot;true&quot;}}`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-load_balancer/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-load_balancer/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the load balancer was created, in the format defined by RFC3339.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
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

