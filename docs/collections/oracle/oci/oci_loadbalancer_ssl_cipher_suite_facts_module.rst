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

.. _ansible_collections.oracle.oci.oci_loadbalancer_ssl_cipher_suite_facts_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_loadbalancer_ssl_cipher_suite_facts -- Fetches details about one or multiple SslCipherSuite resources in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 5.2.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_loadbalancer_ssl_cipher_suite_facts`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Fetches details about one or multiple SslCipherSuite resources in Oracle Cloud Infrastructure
- Lists all SSL cipher suites associated with the specified load balancer.
- If *name* is specified, the details of a single SslCipherSuite will be returned.


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
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the associated load balancer.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the SSL cipher suite to retrieve.</div>
                                            <div>example: `example_cipher_suite`</div>
                                            <div>Required to get a specific ssl_cipher_suite.</div>
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

    
    - name: Get a specific ssl_cipher_suite
      oci_loadbalancer_ssl_cipher_suite_facts:
        # required
        name: name_example
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

    - name: List ssl_cipher_suites
      oci_loadbalancer_ssl_cipher_suite_facts:
        # required
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-ssl_cipher_suites"></div>
                    <b>ssl_cipher_suites</b>
                    <a class="ansibleOptionLink" href="#return-ssl_cipher_suites" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of SslCipherSuite resources</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;ciphers&#x27;: [], &#x27;name&#x27;: &#x27;name_example&#x27;}]</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ssl_cipher_suites/ciphers"></div>
                    <b>ciphers</b>
                    <a class="ansibleOptionLink" href="#return-ssl_cipher_suites/ciphers" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ssl_cipher_suites/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-ssl_cipher_suites/name" title="Permalink to this return value"></a>
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
                    
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Oracle (@oracle)



.. Parsing errors

