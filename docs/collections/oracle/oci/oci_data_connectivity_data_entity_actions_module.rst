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

.. _ansible_collections.oracle.oci.oci_data_connectivity_data_entity_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_data_connectivity_data_entity_actions -- Perform actions on a DataEntity resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 3.3.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_data_connectivity_data_entity_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on a DataEntity resource in Oracle Cloud Infrastructure
- For *action=create_entity_shape*, creates the data entity shape using the shape from the data asset.


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
            <th colspan="8">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>create_entity_shape</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the DataEntity.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
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
                                                                <td colspan="8">
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
                                                                <td colspan="8">
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
                                                                <td colspan="8">
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
                                                                <td colspan="8">
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
                                                                <td colspan="8">
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
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-authorization_mode"></div>
                    <b>authorization_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-authorization_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OBO</li>
                                                                                                                                                                                                <li>USER_PRINCIPAL</li>
                                                                                                                                                                                                <li>RESOURCE_PRINCIPAL</li>
                                                                                                                                                                                                <li>INSTANCE_PRINCIPAL</li>
                                                                                                                                                                                                <li>UNDEFINED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Authorization mode for communicating with another OCI service relevant for the API.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
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
                                                                <td colspan="8">
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
                                                                <td colspan="8">
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
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-connection_key"></div>
                    <b>connection_key</b>
                    <a class="ansibleOptionLink" href="#parameter-connection_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The connection key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-data_format"></div>
                    <b>data_format</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;FILE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/compression_config"></div>
                    <b>compression_config</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/compression_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;FILE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/compression_config/codec"></div>
                    <b>codec</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/compression_config/codec" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NONE</li>
                                                                                                                                                                                                <li>AUTO</li>
                                                                                                                                                                                                <li>GZIP</li>
                                                                                                                                                                                                <li>BZIP2</li>
                                                                                                                                                                                                <li>DEFLATE</li>
                                                                                                                                                                                                <li>LZ4</li>
                                                                                                                                                                                                <li>SNAPPY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Compression algorithm</div>
                                            <div>Required when model_type is &#x27;FILE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute"></div>
                    <b>format_attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;FILE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/compression"></div>
                    <b>compression</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/compression" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The compression for the file.</div>
                                            <div>Applicable when model_type is one of [&#x27;PARQUET_FORMAT&#x27;, &#x27;AVRO_FORMAT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/delimiter"></div>
                    <b>delimiter</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/delimiter" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The delimiter for the CSV format.</div>
                                            <div>Applicable when model_type is &#x27;CSV_FORMAT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/encoding"></div>
                    <b>encoding</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/encoding" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The encoding for the file.</div>
                                            <div>Applicable when model_type is one of [&#x27;CSV_FORMAT&#x27;, &#x27;JSON_FORMAT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/escape_character"></div>
                    <b>escape_character</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/escape_character" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The escape character for the CSV format.</div>
                                            <div>Applicable when model_type is &#x27;CSV_FORMAT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/has_header"></div>
                    <b>has_header</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/has_header" title="Permalink to this option"></a>
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
                                            <div>Defines whether the file has a header row.</div>
                                            <div>Applicable when model_type is &#x27;CSV_FORMAT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/is_file_pattern"></div>
                    <b>is_file_pattern</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/is_file_pattern" title="Permalink to this option"></a>
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
                                            <div>Defines whether a file pattern is supported.</div>
                                            <div>Applicable when model_type is &#x27;CSV_FORMAT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>AVRO_FORMAT</li>
                                                                                                                                                                                                <li>JSON_FORMAT</li>
                                                                                                                                                                                                <li>CSV_FORMAT</li>
                                                                                                                                                                                                <li>PARQUET_FORMAT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the format attribute.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/quote_character"></div>
                    <b>quote_character</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/quote_character" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The quote character for the CSV format.</div>
                                            <div>Applicable when model_type is &#x27;CSV_FORMAT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/format_attribute/timestamp_format"></div>
                    <b>timestamp_format</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/format_attribute/timestamp_format" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Format for timestamp information.</div>
                                            <div>Applicable when model_type is &#x27;CSV_FORMAT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-data_format/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_format/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>JSON</li>
                                                                                                                                                                                                <li>CSV</li>
                                                                                                                                                                                                <li>PARQUET</li>
                                                                                                                                                                                                <li>AVRO</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>type</div>
                                            <div>Required when model_type is &#x27;FILE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-endpoint_id"></div>
                    <b>endpoint_id</b>
                    <a class="ansibleOptionLink" href="#parameter-endpoint_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Endpoint Id used for getDataAssetFullDetails.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-entity_properties"></div>
                    <b>entity_properties</b>
                    <a class="ansibleOptionLink" href="#parameter-entity_properties" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Map&lt;String, String&gt; for entity properties</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-entity_type"></div>
                    <b>entity_type</b>
                    <a class="ansibleOptionLink" href="#parameter-entity_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>TABLE</li>
                                                                                                                                                                                                <li>VIEW</li>
                                                                                                                                                                                                <li>FILE</li>
                                                                                                                                                                                                <li>SQL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The entity type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-external_key"></div>
                    <b>external_key</b>
                    <a class="ansibleOptionLink" href="#parameter-external_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The external key for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys"></div>
                    <b>foreign_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of foreign keys.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs"></div>
                    <b>attribute_refs</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of attribute references.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute"></div>
                    <b>attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to categorize content.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                            <div>Required when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field"></div>
                    <b>native_shape_field</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/default_value_string"></div>
                    <b>default_value_string</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/default_value_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/is_mandatory"></div>
                    <b>is_mandatory</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/is_mandatory" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the field is mandatory.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                            <div>Required when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/native_shape_field/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/native_shape_field/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type reference.</div>
                                            <div>Required when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/attribute/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/attribute/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type reference.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/attribute_refs/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/attribute_refs/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/delete_rule"></div>
                    <b>delete_rule</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/delete_rule" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The delete rule.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object key.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>FOREIGN_KEY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The key type.</div>
                                            <div>Required when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object&#x27;s model version.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key"></div>
                    <b>reference_unique_key</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs"></div>
                    <b>attribute_refs</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of attribute references.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute"></div>
                    <b>attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to categorize content.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field"></div>
                    <b>native_shape_field</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/default_value_string"></div>
                    <b>default_value_string</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/default_value_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/is_mandatory"></div>
                    <b>is_mandatory</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/is_mandatory" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the field is mandatory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/native_shape_field/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type reference.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/attribute/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type reference.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/attribute_refs/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/attribute_refs/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PRIMARY_KEY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The key type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object&#x27;s model version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/reference_unique_key/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/reference_unique_key/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-foreign_keys/update_rule"></div>
                    <b>update_rule</b>
                    <a class="ansibleOptionLink" href="#parameter-foreign_keys/update_rule" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The update rule.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DATA_STORE_ENTITY</li>
                                                                                                                                                                                                <li>TABLE_ENTITY</li>
                                                                                                                                                                                                <li>SQL_ENTITY</li>
                                                                                                                                                                                                <li>FILE_ENTITY</li>
                                                                                                                                                                                                <li>VIEW_ENTITY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The data entity type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object&#x27;s model version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
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
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-object_version"></div>
                    <b>object_version</b>
                    <a class="ansibleOptionLink" href="#parameter-object_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The version of the object that is used to track changes in the object instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-other_type_label"></div>
                    <b>other_type_label</b>
                    <a class="ansibleOptionLink" href="#parameter-other_type_label" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies other type label.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="8">
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
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-registry_id"></div>
                    <b>registry_id</b>
                    <a class="ansibleOptionLink" href="#parameter-registry_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The registry Ocid.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-resource_name"></div>
                    <b>resource_name</b>
                    <a class="ansibleOptionLink" href="#parameter-resource_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The resource name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-schema_resource_name"></div>
                    <b>schema_resource_name</b>
                    <a class="ansibleOptionLink" href="#parameter-schema_resource_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The schema resource name used for retrieving schemas.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-shape"></div>
                    <b>shape</b>
                    <a class="ansibleOptionLink" href="#parameter-shape" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                            <div>Required when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition"></div>
                    <b>config_definition</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is one of [&#x27;DATA_TYPE&#x27;, &#x27;CONFIGURED_TYPE&#x27;, &#x27;COMPOSITE_TYPE&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions"></div>
                    <b>config_parameter_definitions</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The parameter configuration details.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/class_field_name"></div>
                    <b>class_field_name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/class_field_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The parameter class field name.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/default_value"></div>
                    <b>default_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/default_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value for the parameter.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/is_class_field_value"></div>
                    <b>is_class_field_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/is_class_field_value" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the parameter is a class field or not.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/is_static"></div>
                    <b>is_static</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/is_static" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the parameter is static or not.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_name"></div>
                    <b>parameter_name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This object represents the configurable properties for an object type.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_type"></div>
                    <b>parameter_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which disciminates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/config_parameter_definitions/parameter_type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/is_contained"></div>
                    <b>is_contained</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/is_contained" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the configuration is contained or not.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_definition/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_definition/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/dt_type"></div>
                    <b>dt_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/dt_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PRIMITIVE</li>
                                                                                                                                                                                                <li>STRUCTURED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The data type.</div>
                                            <div>Applicable when model_type is &#x27;DATA_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements"></div>
                    <b>elements</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of elements.</div>
                                            <div>Applicable when model_type is &#x27;COMPOSITE_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/default_value"></div>
                    <b>default_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/default_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/default_value_string"></div>
                    <b>default_value_string</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/default_value_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value.</div>
                                            <div>Applicable when model_type is &#x27;NATIVE_SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields"></div>
                    <b>fields</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of fields.</div>
                                            <div>Applicable when model_type is one of [&#x27;INPUT_PORT&#x27;, &#x27;OUTPUT_PORT&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/fields/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/fields/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/is_input"></div>
                    <b>is_input</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/is_input" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the parameter is input value.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/is_mandatory"></div>
                    <b>is_mandatory</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/is_mandatory" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the field is mandatory.</div>
                                            <div>Applicable when model_type is &#x27;NATIVE_SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/is_output"></div>
                    <b>is_output</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/is_output" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the parameter is output value.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to categorize content.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OUTPUT_PORT</li>
                                                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>INPUT_PORT</li>
                                                                                                                                                                                                <li>PARAMETER</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field"></div>
                    <b>native_shape_field</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/default_value_string"></div>
                    <b>default_value_string</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/default_value_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/is_mandatory"></div>
                    <b>is_mandatory</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/is_mandatory" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the field is mandatory.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                            <div>Required when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                            <div>Applicable when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/native_shape_field/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/native_shape_field/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type reference.</div>
                                            <div>Required when model_type is &#x27;SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/output_aggregation_type"></div>
                    <b>output_aggregation_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/output_aggregation_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>MIN</li>
                                                                                                                                                                                                <li>MAX</li>
                                                                                                                                                                                                <li>COUNT</li>
                                                                                                                                                                                                <li>SUM</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The output aggregation type.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;OUTPUT_PORT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/port_type"></div>
                    <b>port_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/port_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DATA</li>
                                                                                                                                                                                                <li>CONTROL</li>
                                                                                                                                                                                                <li>MODEL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The port details for the data asset.Type.</div>
                                            <div>Applicable when model_type is one of [&#x27;INPUT_PORT&#x27;, &#x27;OUTPUT_PORT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                            <div>Applicable when model_type is &#x27;NATIVE_SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/root_object_default_value"></div>
                    <b>root_object_default_value</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/root_object_default_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value of the parameter which can be an object in DIS, such as a data entity.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is one of [&#x27;SHAPE&#x27;, &#x27;SHAPE_FIELD&#x27;, &#x27;PARAMETER&#x27;]</div>
                                            <div>Required when model_type is &#x27;NATIVE_SHAPE_FIELD&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which disciminates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/elements/type_name"></div>
                    <b>type_name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/elements/type_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of value the parameter was created for.</div>
                                            <div>Applicable when model_type is &#x27;PARAMETER&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which disciminates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type"></div>
                    <b>parent_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;COMPOSITE_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/config_definition"></div>
                    <b>config_definition</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/config_definition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/elements"></div>
                    <b>elements</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/elements" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of elements.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which disciminates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/parent_type/parent_type"></div>
                    <b>parent_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/parent_type/parent_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/schema"></div>
                    <b>schema</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/schema" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;STRUCTURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/schema/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/schema/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/schema/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/schema/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/schema/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/schema/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which disciminates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/schema/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/schema/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/schema/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/schema/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/schema/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/schema/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/schema/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/schema/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/type_system_name"></div>
                    <b>type_system_name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/type_system_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The data type system name.</div>
                                            <div>Applicable when model_type is &#x27;DATA_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/wrapped_type"></div>
                    <b>wrapped_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/wrapped_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;CONFIGURED_TYPE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/wrapped_type/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/wrapped_type/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/wrapped_type/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/wrapped_type/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/wrapped_type/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/wrapped_type/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which disciminates the subtypes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/wrapped_type/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/wrapped_type/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/wrapped_type/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/wrapped_type/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/wrapped_type/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/wrapped_type/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-shape/type/wrapped_type/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-shape/type/wrapped_type/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-shape_id"></div>
                    <b>shape_id</b>
                    <a class="ansibleOptionLink" href="#parameter-shape_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The shape ID.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-sql_query"></div>
                    <b>sql_query</b>
                    <a class="ansibleOptionLink" href="#parameter-sql_query" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>sqlQuery</div>
                                            <div>Applicable when model_type is &#x27;SQL_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
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
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-types"></div>
                    <b>types</b>
                    <a class="ansibleOptionLink" href="#parameter-types" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-types/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-types/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-types/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-types/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-types/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-types/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-types/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/object_version"></div>
                    <b>object_version</b>
                    <a class="ansibleOptionLink" href="#parameter-types/object_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The version of the object that is used to track changes in the object instance.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-types/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-types/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-types/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-types/types"></div>
                    <b>types</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>types</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-types/types/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user defined description for the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-types/types/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-types/types/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRUCTURED_TYPE</li>
                                                                                                                                                                                                <li>DATA_TYPE</li>
                                                                                                                                                                                                <li>CONFIGURED_TYPE</li>
                                                                                                                                                                                                <li>COMPOSITE_TYPE</li>
                                                                                                                                                                                                <li>DERIVED_TYPE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The property which disciminates the subtypes.</div>
                                            <div>Required when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-types/types/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-types/types/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-types/types/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-types/types/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-types/types/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-types/types/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                            <div>Applicable when model_type is &#x27;DATA_STORE_ENTITY&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys"></div>
                    <b>unique_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of unique keys.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs"></div>
                    <b>attribute_refs</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of attribute references.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute"></div>
                    <b>attribute</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/labels"></div>
                    <b>labels</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/labels" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to categorize content.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field"></div>
                    <b>native_shape_field</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values"></div>
                    <b>config_values</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values"></div>
                    <b>config_param_values</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The configuration parameter values.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/int_value"></div>
                    <b>int_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/int_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An integer value of the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/object_value"></div>
                    <b>object_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/object_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An object value of the parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/parameter_value"></div>
                    <b>parameter_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/parameter_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Reference to the parameter by its key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/ref_value"></div>
                    <b>ref_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/ref_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The root object reference value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/string_value"></div>
                    <b>string_value</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/config_param_values/string_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string value of the parameter.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/config_values/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/default_value_string"></div>
                    <b>default_value_string</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/default_value_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The default value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Detailed description for the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/is_mandatory"></div>
                    <b>is_mandatory</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/is_mandatory" title="Permalink to this option"></a>
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
                                            <div>Specifies whether the field is mandatory.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The key of the object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SHAPE</li>
                                                                                                                                                                                                <li>SHAPE_FIELD</li>
                                                                                                                                                                                                <li>NATIVE_SHAPE_FIELD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the types object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The model version of an object.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/native_shape_field/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/native_shape_field/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type reference.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/attribute/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/attribute/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type reference.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/attribute_refs/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/attribute_refs/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The position of the attribute.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/model_type"></div>
                    <b>model_type</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/model_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PRIMARY_KEY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The key type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/model_version"></div>
                    <b>model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The object&#x27;s model version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/object_status"></div>
                    <b>object_status</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/object_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status of an object that can be set to value 1 for shallow references across objects, other values reserved.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/parent_ref"></div>
                    <b>parent_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/parent_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-unique_keys/parent_ref/parent"></div>
                    <b>parent</b>
                    <a class="ansibleOptionLink" href="#parameter-unique_keys/parent_ref/parent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Key of the parent object.</div>
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

    
    - name: Perform action create_entity_shape on data_entity with model_type = DATA_STORE_ENTITY
      oci_data_connectivity_data_entity_actions:
        # required
        model_type: DATA_STORE_ENTITY
        name: name_example

        # optional
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        object_version: 56
        external_key: external_key_example
        shape:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          config_values:
            # optional
            config_param_values:
              # optional
              string_value: string_value_example
              int_value: 56
              object_value: null
              ref_value: null
              parameter_value: parameter_value_example
            parent_ref:
              # optional
              parent: parent_example
          object_status: 56
          name: name_example
          description: description_example
          type:
            # required
            model_type: CONFIGURED_TYPE

            # optional
            wrapped_type:
              # required
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            config_values:
              # optional
              config_param_values:
                # optional
                string_value: string_value_example
                int_value: 56
                object_value: null
                ref_value: null
                parameter_value: parameter_value_example
              parent_ref:
                # optional
                parent: parent_example
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
            config_definition:
              # optional
              key: key_example
              model_type: model_type_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              name: name_example
              is_contained: true
              object_status: 56
              config_parameter_definitions:
                # optional
                parameter_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                parameter_name: parameter_name_example
                description: description_example
                default_value: null
                class_field_name: class_field_name_example
                is_static: true
                is_class_field_value: true
        shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type: TABLE
        other_type_label: other_type_label_example
        unique_keys:
        - # required
          model_type: PRIMARY_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          object_status: 56
        foreign_keys:
        - # required
          model_type: FOREIGN_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          update_rule: 56
          delete_rule: 56
          reference_unique_key:
            # required
            model_type: PRIMARY_KEY

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            attribute_refs:
            - # optional
              position: 56
              attribute:
                # required
                model_type: SHAPE

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                type: null
                labels: [ "labels_example" ]
                native_shape_field:
                  # required
                  model_type: SHAPE
                  type: null

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref:
                    # optional
                    parent: parent_example
                  config_values:
                    # optional
                    config_param_values:
                      # optional
                      string_value: string_value_example
                      int_value: 56
                      object_value: null
                      ref_value: null
                      parameter_value: parameter_value_example
                    parent_ref:
                      # optional
                      parent: parent_example
                  object_status: 56
                  name: name_example
                  description: description_example
                  position: 56
                  default_value_string: default_value_string_example
                  is_mandatory: true
            object_status: 56
          object_status: 56
        resource_name: resource_name_example
        object_status: 56
        identifier: identifier_example
        types:
          # optional
          key: key_example
          model_type: model_type_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          description: description_example
          object_version: 56
          types:
            # required
            model_type: STRUCTURED_TYPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
          object_status: 56
          identifier: identifier_example
        entity_properties: null

    - name: Perform action create_entity_shape on data_entity with model_type = TABLE_ENTITY
      oci_data_connectivity_data_entity_actions:
        # required
        model_type: TABLE_ENTITY
        name: name_example

        # optional
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        object_version: 56
        external_key: external_key_example
        shape:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          config_values:
            # optional
            config_param_values:
              # optional
              string_value: string_value_example
              int_value: 56
              object_value: null
              ref_value: null
              parameter_value: parameter_value_example
            parent_ref:
              # optional
              parent: parent_example
          object_status: 56
          name: name_example
          description: description_example
          type:
            # required
            model_type: CONFIGURED_TYPE

            # optional
            wrapped_type:
              # required
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            config_values:
              # optional
              config_param_values:
                # optional
                string_value: string_value_example
                int_value: 56
                object_value: null
                ref_value: null
                parameter_value: parameter_value_example
              parent_ref:
                # optional
                parent: parent_example
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
            config_definition:
              # optional
              key: key_example
              model_type: model_type_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              name: name_example
              is_contained: true
              object_status: 56
              config_parameter_definitions:
                # optional
                parameter_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                parameter_name: parameter_name_example
                description: description_example
                default_value: null
                class_field_name: class_field_name_example
                is_static: true
                is_class_field_value: true
        shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type: TABLE
        other_type_label: other_type_label_example
        unique_keys:
        - # required
          model_type: PRIMARY_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          object_status: 56
        foreign_keys:
        - # required
          model_type: FOREIGN_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          update_rule: 56
          delete_rule: 56
          reference_unique_key:
            # required
            model_type: PRIMARY_KEY

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            attribute_refs:
            - # optional
              position: 56
              attribute:
                # required
                model_type: SHAPE

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                type: null
                labels: [ "labels_example" ]
                native_shape_field:
                  # required
                  model_type: SHAPE
                  type: null

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref:
                    # optional
                    parent: parent_example
                  config_values:
                    # optional
                    config_param_values:
                      # optional
                      string_value: string_value_example
                      int_value: 56
                      object_value: null
                      ref_value: null
                      parameter_value: parameter_value_example
                    parent_ref:
                      # optional
                      parent: parent_example
                  object_status: 56
                  name: name_example
                  description: description_example
                  position: 56
                  default_value_string: default_value_string_example
                  is_mandatory: true
            object_status: 56
          object_status: 56
        resource_name: resource_name_example
        object_status: 56
        identifier: identifier_example
        types:
          # optional
          key: key_example
          model_type: model_type_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          description: description_example
          object_version: 56
          types:
            # required
            model_type: STRUCTURED_TYPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
          object_status: 56
          identifier: identifier_example
        entity_properties: null

    - name: Perform action create_entity_shape on data_entity with model_type = SQL_ENTITY
      oci_data_connectivity_data_entity_actions:
        # required
        model_type: SQL_ENTITY
        name: name_example

        # optional
        sql_query: sql_query_example
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        object_version: 56
        external_key: external_key_example
        shape:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          config_values:
            # optional
            config_param_values:
              # optional
              string_value: string_value_example
              int_value: 56
              object_value: null
              ref_value: null
              parameter_value: parameter_value_example
            parent_ref:
              # optional
              parent: parent_example
          object_status: 56
          name: name_example
          description: description_example
          type:
            # required
            model_type: CONFIGURED_TYPE

            # optional
            wrapped_type:
              # required
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            config_values:
              # optional
              config_param_values:
                # optional
                string_value: string_value_example
                int_value: 56
                object_value: null
                ref_value: null
                parameter_value: parameter_value_example
              parent_ref:
                # optional
                parent: parent_example
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
            config_definition:
              # optional
              key: key_example
              model_type: model_type_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              name: name_example
              is_contained: true
              object_status: 56
              config_parameter_definitions:
                # optional
                parameter_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                parameter_name: parameter_name_example
                description: description_example
                default_value: null
                class_field_name: class_field_name_example
                is_static: true
                is_class_field_value: true
        shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type: TABLE
        other_type_label: other_type_label_example
        unique_keys:
        - # required
          model_type: PRIMARY_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          object_status: 56
        foreign_keys:
        - # required
          model_type: FOREIGN_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          update_rule: 56
          delete_rule: 56
          reference_unique_key:
            # required
            model_type: PRIMARY_KEY

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            attribute_refs:
            - # optional
              position: 56
              attribute:
                # required
                model_type: SHAPE

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                type: null
                labels: [ "labels_example" ]
                native_shape_field:
                  # required
                  model_type: SHAPE
                  type: null

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref:
                    # optional
                    parent: parent_example
                  config_values:
                    # optional
                    config_param_values:
                      # optional
                      string_value: string_value_example
                      int_value: 56
                      object_value: null
                      ref_value: null
                      parameter_value: parameter_value_example
                    parent_ref:
                      # optional
                      parent: parent_example
                  object_status: 56
                  name: name_example
                  description: description_example
                  position: 56
                  default_value_string: default_value_string_example
                  is_mandatory: true
            object_status: 56
          object_status: 56
        resource_name: resource_name_example
        object_status: 56
        identifier: identifier_example
        types:
          # optional
          key: key_example
          model_type: model_type_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          description: description_example
          object_version: 56
          types:
            # required
            model_type: STRUCTURED_TYPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
          object_status: 56
          identifier: identifier_example
        entity_properties: null

    - name: Perform action create_entity_shape on data_entity with model_type = FILE_ENTITY
      oci_data_connectivity_data_entity_actions:
        # required
        model_type: FILE_ENTITY
        name: name_example

        # optional
        data_format:
          # required
          type: JSON

          # optional
          format_attribute:
            # required
            model_type: AVRO_FORMAT

            # optional
            compression: compression_example
          compression_config:
            # required
            codec: NONE
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        object_version: 56
        external_key: external_key_example
        shape:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          config_values:
            # optional
            config_param_values:
              # optional
              string_value: string_value_example
              int_value: 56
              object_value: null
              ref_value: null
              parameter_value: parameter_value_example
            parent_ref:
              # optional
              parent: parent_example
          object_status: 56
          name: name_example
          description: description_example
          type:
            # required
            model_type: CONFIGURED_TYPE

            # optional
            wrapped_type:
              # required
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            config_values:
              # optional
              config_param_values:
                # optional
                string_value: string_value_example
                int_value: 56
                object_value: null
                ref_value: null
                parameter_value: parameter_value_example
              parent_ref:
                # optional
                parent: parent_example
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
            config_definition:
              # optional
              key: key_example
              model_type: model_type_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              name: name_example
              is_contained: true
              object_status: 56
              config_parameter_definitions:
                # optional
                parameter_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                parameter_name: parameter_name_example
                description: description_example
                default_value: null
                class_field_name: class_field_name_example
                is_static: true
                is_class_field_value: true
        shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type: TABLE
        other_type_label: other_type_label_example
        unique_keys:
        - # required
          model_type: PRIMARY_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          object_status: 56
        foreign_keys:
        - # required
          model_type: FOREIGN_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          update_rule: 56
          delete_rule: 56
          reference_unique_key:
            # required
            model_type: PRIMARY_KEY

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            attribute_refs:
            - # optional
              position: 56
              attribute:
                # required
                model_type: SHAPE

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                type: null
                labels: [ "labels_example" ]
                native_shape_field:
                  # required
                  model_type: SHAPE
                  type: null

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref:
                    # optional
                    parent: parent_example
                  config_values:
                    # optional
                    config_param_values:
                      # optional
                      string_value: string_value_example
                      int_value: 56
                      object_value: null
                      ref_value: null
                      parameter_value: parameter_value_example
                    parent_ref:
                      # optional
                      parent: parent_example
                  object_status: 56
                  name: name_example
                  description: description_example
                  position: 56
                  default_value_string: default_value_string_example
                  is_mandatory: true
            object_status: 56
          object_status: 56
        resource_name: resource_name_example
        object_status: 56
        identifier: identifier_example
        types:
          # optional
          key: key_example
          model_type: model_type_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          description: description_example
          object_version: 56
          types:
            # required
            model_type: STRUCTURED_TYPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
          object_status: 56
          identifier: identifier_example
        entity_properties: null

    - name: Perform action create_entity_shape on data_entity with model_type = VIEW_ENTITY
      oci_data_connectivity_data_entity_actions:
        # required
        model_type: VIEW_ENTITY
        name: name_example

        # optional
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        object_version: 56
        external_key: external_key_example
        shape:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          config_values:
            # optional
            config_param_values:
              # optional
              string_value: string_value_example
              int_value: 56
              object_value: null
              ref_value: null
              parameter_value: parameter_value_example
            parent_ref:
              # optional
              parent: parent_example
          object_status: 56
          name: name_example
          description: description_example
          type:
            # required
            model_type: CONFIGURED_TYPE

            # optional
            wrapped_type:
              # required
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            config_values:
              # optional
              config_param_values:
                # optional
                string_value: string_value_example
                int_value: 56
                object_value: null
                ref_value: null
                parameter_value: parameter_value_example
              parent_ref:
                # optional
                parent: parent_example
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
            config_definition:
              # optional
              key: key_example
              model_type: model_type_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              name: name_example
              is_contained: true
              object_status: 56
              config_parameter_definitions:
                # optional
                parameter_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                parameter_name: parameter_name_example
                description: description_example
                default_value: null
                class_field_name: class_field_name_example
                is_static: true
                is_class_field_value: true
        shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type: TABLE
        other_type_label: other_type_label_example
        unique_keys:
        - # required
          model_type: PRIMARY_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          object_status: 56
        foreign_keys:
        - # required
          model_type: FOREIGN_KEY

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          attribute_refs:
          - # optional
            position: 56
            attribute:
              # required
              model_type: SHAPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
              config_values:
                # optional
                config_param_values:
                  # optional
                  string_value: string_value_example
                  int_value: 56
                  object_value: null
                  ref_value: null
                  parameter_value: parameter_value_example
                parent_ref:
                  # optional
                  parent: parent_example
              object_status: 56
              name: name_example
              description: description_example
              type: null
              labels: [ "labels_example" ]
              native_shape_field:
                # required
                model_type: SHAPE
                type: null

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                position: 56
                default_value_string: default_value_string_example
                is_mandatory: true
          update_rule: 56
          delete_rule: 56
          reference_unique_key:
            # required
            model_type: PRIMARY_KEY

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            attribute_refs:
            - # optional
              position: 56
              attribute:
                # required
                model_type: SHAPE

                # optional
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                object_status: 56
                name: name_example
                description: description_example
                type: null
                labels: [ "labels_example" ]
                native_shape_field:
                  # required
                  model_type: SHAPE
                  type: null

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref:
                    # optional
                    parent: parent_example
                  config_values:
                    # optional
                    config_param_values:
                      # optional
                      string_value: string_value_example
                      int_value: 56
                      object_value: null
                      ref_value: null
                      parameter_value: parameter_value_example
                    parent_ref:
                      # optional
                      parent: parent_example
                  object_status: 56
                  name: name_example
                  description: description_example
                  position: 56
                  default_value_string: default_value_string_example
                  is_mandatory: true
            object_status: 56
          object_status: 56
        resource_name: resource_name_example
        object_status: 56
        identifier: identifier_example
        types:
          # optional
          key: key_example
          model_type: model_type_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          description: description_example
          object_version: 56
          types:
            # required
            model_type: STRUCTURED_TYPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            object_status: 56
            description: description_example
          object_status: 56
          identifier: identifier_example
        entity_properties: null





.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Oracle (@oracle)



.. Parsing errors

There were some errors parsing the documentation for this plugin.  Please file a bug with the collection.

The errors were:

* ::

        Unable to normalize oci_data_connectivity_data_entity_actions: return due to: 8 validation errors for PluginReturnSchema
        return -> data_entity -> contains -> shape -> contains -> type -> contains -> config_definition -> contains -> config_parameter_definitions -> contains -> parameter_type -> contains -> parent_ref -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> data_entity -> contains -> shape -> contains -> type -> contains -> elements -> contains -> fields -> contains -> config_values -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> data_entity -> contains -> shape -> contains -> type -> contains -> elements -> contains -> fields -> contains -> parent_ref -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> data_entity -> contains -> shape -> contains -> type -> contains -> parent_type -> contains -> config_definition -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> data_entity -> contains -> shape -> contains -> type -> contains -> parent_type -> contains -> parent_ref -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> data_entity -> contains -> shape -> contains -> type -> contains -> parent_type -> contains -> parent_type -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> data_entity -> contains -> shape -> contains -> type -> contains -> schema -> contains -> parent_ref -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> data_entity -> contains -> shape -> contains -> type -> contains -> wrapped_type -> contains -> parent_ref -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)

