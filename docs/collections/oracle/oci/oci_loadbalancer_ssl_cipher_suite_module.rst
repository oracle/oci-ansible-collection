.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.oracle.oci.oci_loadbalancer_ssl_cipher_suite_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_loadbalancer_ssl_cipher_suite -- Manage a SslCipherSuite resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 2.16.0).

    To install it use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_loadbalancer_ssl_cipher_suite`.

.. version_added

.. versionadded:: 2.9 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a SslCipherSuite resource in Oracle Cloud Infrastructure
- For *state=present*, creates a custom SSL cipher suite.


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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ciphers"></div>
                    <b>ciphers</b>
                    <a class="ansibleOptionLink" href="#parameter-ciphers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of SSL ciphers the load balancer must support for HTTPS or SSL connections.</div>
                                            <div>The following ciphers are valid values for this property:</div>
                                            <div>*  __TLSv1.2 ciphers__</div>
                                            <div>&quot;AES128-GCM-SHA256&quot; &quot;AES128-SHA256&quot; &quot;AES256-GCM-SHA384&quot; &quot;AES256-SHA256&quot; &quot;DH-DSS-AES128-GCM-SHA256&quot; &quot;DH-DSS-AES128-SHA256&quot; &quot;DH-DSS-AES256-GCM-SHA384&quot; &quot;DH-DSS-AES256-SHA256&quot; &quot;DH-RSA-AES128-GCM-SHA256&quot; &quot;DH-RSA-AES128-SHA256&quot; &quot;DH-RSA-AES256-GCM-SHA384&quot; &quot;DH-RSA-AES256-SHA256&quot; &quot;DHE-DSS-AES128-GCM-SHA256&quot; &quot;DHE-DSS-AES128-SHA256&quot; &quot;DHE-DSS-AES256-GCM-SHA384&quot; &quot;DHE-DSS-AES256-SHA256&quot; &quot;DHE-RSA-AES128-GCM-SHA256&quot; &quot;DHE-RSA-AES128-SHA256&quot; &quot;DHE-RSA-AES256-GCM-SHA384&quot; &quot;DHE-RSA-AES256-SHA256&quot; &quot;ECDH-ECDSA-AES128-GCM-SHA256&quot; &quot;ECDH-ECDSA-AES128-SHA256&quot; &quot;ECDH-ECDSA-AES256-GCM-SHA384&quot; &quot;ECDH-ECDSA-AES256-SHA384&quot; &quot;ECDH-RSA-AES128-GCM-SHA256&quot; &quot;ECDH-RSA-AES128-SHA256&quot; &quot;ECDH-RSA-AES256-GCM-SHA384&quot; &quot;ECDH-RSA-AES256-SHA384&quot; &quot;ECDHE-ECDSA-AES128-GCM-SHA256&quot; &quot;ECDHE-ECDSA-AES128-SHA256&quot; &quot;ECDHE-ECDSA-AES256-GCM-SHA384&quot; &quot;ECDHE-ECDSA-AES256-SHA384&quot; &quot;ECDHE-RSA-AES128-GCM-SHA256&quot; &quot;ECDHE-RSA-AES128-SHA256&quot; &quot;ECDHE-RSA-AES256-GCM-SHA384&quot; &quot;ECDHE-RSA-AES256-SHA384&quot;</div>
                                            <div>*  __TLSv1 ciphers also supported by TLSv1.2__</div>
                                            <div>&quot;AES128-SHA&quot; &quot;AES256-SHA&quot; &quot;CAMELLIA128-SHA&quot; &quot;CAMELLIA256-SHA&quot; &quot;DES-CBC3-SHA&quot; &quot;DH-DSS-AES128-SHA&quot; &quot;DH-DSS-AES256-SHA&quot; &quot;DH-DSS-CAMELLIA128-SHA&quot; &quot;DH-DSS-CAMELLIA256-SHA&quot; &quot;DH-DSS-DES-CBC3-SHAv&quot; &quot;DH-DSS-SEED-SHA&quot; &quot;DH-RSA-AES128-SHA&quot; &quot;DH-RSA-AES256-SHA&quot; &quot;DH-RSA-CAMELLIA128-SHA&quot; &quot;DH-RSA-CAMELLIA256-SHA&quot; &quot;DH-RSA-DES-CBC3-SHA&quot; &quot;DH-RSA-SEED-SHA&quot; &quot;DHE-DSS-AES128-SHA&quot; &quot;DHE-DSS-AES256-SHA&quot; &quot;DHE-DSS-CAMELLIA128-SHA&quot; &quot;DHE-DSS-CAMELLIA256-SHA&quot; &quot;DHE-DSS-DES-CBC3-SHA&quot; &quot;DHE-DSS-SEED-SHA&quot; &quot;DHE-RSA-AES128-SHA&quot; &quot;DHE-RSA-AES256-SHA&quot; &quot;DHE-RSA-CAMELLIA128-SHA&quot; &quot;DHE-RSA-CAMELLIA256-SHA&quot; &quot;DHE-RSA-DES-CBC3-SHA&quot; &quot;DHE-RSA-SEED-SHA&quot; &quot;ECDH-ECDSA-AES128-SHA&quot; &quot;ECDH-ECDSA-AES256-SHA&quot; &quot;ECDH-ECDSA-DES-CBC3-SHA&quot; &quot;ECDH-ECDSA-RC4-SHA&quot; &quot;ECDH-RSA-AES128-SHA&quot; &quot;ECDH-RSA-AES256-SHA&quot; &quot;ECDH-RSA-DES-CBC3-SHA&quot; &quot;ECDH-RSA-RC4-SHA&quot; &quot;ECDHE-ECDSA-AES128-SHA&quot; &quot;ECDHE-ECDSA-AES256-SHA&quot; &quot;ECDHE-ECDSA-DES-CBC3-SHA&quot; &quot;ECDHE-ECDSA-RC4-SHA&quot; &quot;ECDHE-RSA-AES128-SHA&quot; &quot;ECDHE-RSA-AES256-SHA&quot; &quot;ECDHE-RSA-DES-CBC3-SHA&quot; &quot;ECDHE-RSA-RC4-SHA&quot; &quot;IDEA-CBC-SHA&quot; &quot;KRB5-DES-CBC3-MD5&quot; &quot;KRB5-DES-CBC3-SHA&quot; &quot;KRB5-IDEA-CBC-MD5&quot; &quot;KRB5-IDEA-CBC-SHA&quot; &quot;KRB5-RC4-MD5&quot; &quot;KRB5-RC4-SHA&quot; &quot;PSK-3DES-EDE-CBC-SHA&quot; &quot;PSK-AES128-CBC-SHA&quot; &quot;PSK-AES256-CBC-SHA&quot; &quot;PSK-RC4-SHA&quot; &quot;RC4-MD5&quot; &quot;RC4-SHA&quot; &quot;SEED-SHA&quot;</div>
                                            <div>example: `[&quot;ECDHE-RSA-AES256-GCM-SHA384&quot;,&quot;ECDHE-ECDSA-AES256-GCM-SHA384&quot;,&quot;ECDHE-RSA-AES128-GCM-SHA256&quot;]`</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with name present.</div>
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
                                                                <td colspan="1">
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
                                            <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource are used to uniquely identify a resource.</div>
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
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A friendly name for the SSL cipher suite. It must be unique and it cannot be changed.</div>
                                            <div>**Note:** The name of your user-defined cipher suite must not be the same as any of Oracle&#x27;s predefined or reserved SSL cipher suite names:</div>
                                            <div>* oci-default-ssl-cipher-suite-v1 * oci-modern-ssl-cipher-suite-v1 * oci-compatible-ssl-cipher-suite-v1 * oci-wider-compatible-ssl-cipher-suite-v1 * oci-customized-ssl-cipher-suite</div>
                                            <div>example: `example_cipher_suite`</div>
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
                                            <div>The state of the SslCipherSuite.</div>
                                            <div>Use <em>state=present</em> to create or update a SslCipherSuite.</div>
                                            <div>Use <em>state=absent</em> to delete a SslCipherSuite.</div>
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

    
    - name: Create ssl_cipher_suite
      oci_loadbalancer_ssl_cipher_suite:
        ciphers:
        - ECDHE-RSA-AES256-GCM-SHA384
        - ECDHE-ECDSA-AES256-GCM-SHA384
        - ECDHE-RSA-AES128-GCM-SHA256
        name: example_cipher_suite
        load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

    - name: Update ssl_cipher_suite
      oci_loadbalancer_ssl_cipher_suite:
        ciphers:
        - ECDHE-ECDSA-AES128-GCM-SHA256
        - ECDHE-RSA-AES128-GCM-SHA256
        load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

    - name: Delete ssl_cipher_suite
      oci_loadbalancer_ssl_cipher_suite:
        name: example_cipher_suite
        load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
        state: absent





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
                    <div class="ansibleOptionAnchor" id="return-ssl_cipher_suite"></div>
                    <b>ssl_cipher_suite</b>
                    <a class="ansibleOptionLink" href="#return-ssl_cipher_suite" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the SslCipherSuite resource acted upon by the current operation</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;ciphers&#x27;: [], &#x27;name&#x27;: &#x27;name_example&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-ssl_cipher_suite/ciphers"></div>
                    <b>ciphers</b>
                    <a class="ansibleOptionLink" href="#return-ssl_cipher_suite/ciphers" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-ssl_cipher_suite/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-ssl_cipher_suite/name" title="Permalink to this return value"></a>
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

