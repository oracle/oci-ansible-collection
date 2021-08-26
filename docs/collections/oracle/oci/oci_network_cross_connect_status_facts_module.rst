.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.oracle.oci.oci_network_cross_connect_status_facts_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_network_cross_connect_status_facts -- Fetches details about a CrossConnectStatus resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 2.29.0).

    To install it use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_network_cross_connect_status_facts`.

.. version_added

.. versionadded:: 2.9 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Fetches details about a CrossConnectStatus resource in Oracle Cloud Infrastructure
- Gets the status of the specified cross-connect.


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
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-cross_connect_id"></div>
                    <b>cross_connect_id</b>
                    <a class="ansibleOptionLink" href="#parameter-cross_connect_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the cross-connect.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
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

    
    - name: Get a specific cross_connect_status
      oci_network_cross_connect_status_facts:
        cross_connect_id: "ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx"





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
                    <div class="ansibleOptionAnchor" id="return-cross_connect_status"></div>
                    <b>cross_connect_status</b>
                    <a class="ansibleOptionLink" href="#return-cross_connect_status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>CrossConnectStatus resource</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;cross_connect_id&#x27;: &#x27;ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;interface_state&#x27;: &#x27;UP&#x27;, &#x27;light_level_ind_bm&#x27;: 14.0, &#x27;light_level_indicator&#x27;: &#x27;NO_LIGHT&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-cross_connect_status/cross_connect_id"></div>
                    <b>cross_connect_id</b>
                    <a class="ansibleOptionLink" href="#return-cross_connect_status/cross_connect_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the cross-connect.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.crossconnect.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-cross_connect_status/interface_state"></div>
                    <b>interface_state</b>
                    <a class="ansibleOptionLink" href="#return-cross_connect_status/interface_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether Oracle&#x27;s side of the interface is up or down.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">UP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-cross_connect_status/light_level_ind_bm"></div>
                    <b>light_level_ind_bm</b>
                    <a class="ansibleOptionLink" href="#return-cross_connect_status/light_level_ind_bm" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The light level of the cross-connect (in dBm).</div>
                                            <div>Example: `14.0`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">14.0</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-cross_connect_status/light_level_indicator"></div>
                    <b>light_level_indicator</b>
                    <a class="ansibleOptionLink" href="#return-cross_connect_status/light_level_indicator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Status indicator corresponding to the light level.</div>
                                            <div>* **NO_LIGHT:** No measurable light</div>
                                            <div>* **LOW_WARN:** There&#x27;s measurable light but it&#x27;s too low</div>
                                            <div>* **HIGH_WARN:** Light level is too high</div>
                                            <div>* **BAD:** There&#x27;s measurable light but the signal-to-noise ratio is bad</div>
                                            <div>* **GOOD:** Good light level</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NO_LIGHT</div>
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

