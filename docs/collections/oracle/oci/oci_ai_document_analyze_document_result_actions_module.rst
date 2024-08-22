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

.. _ansible_collections.oracle.oci.oci_ai_document_analyze_document_result_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_ai_document_analyze_document_result_actions -- Perform actions on an AnalyzeDocumentResult resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 5.3.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_ai_document_analyze_document_result_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on an AnalyzeDocumentResult resource in Oracle Cloud Infrastructure
- For *action=analyze_document*, perform different types of document analysis.


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
                                                                                                                                                                <li>analyze_document</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the AnalyzeDocumentResult.</div>
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
                                                                                                                                                                                                <li>security_token</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The compartment identifier.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-document"></div>
                    <b>document</b>
                    <a class="ansibleOptionLink" href="#parameter-document" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-document/bucket_name"></div>
                    <b>bucket_name</b>
                    <a class="ansibleOptionLink" href="#parameter-document/bucket_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Object Storage bucket name.</div>
                                            <div>Required when source is &#x27;OBJECT_STORAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-document/data"></div>
                    <b>data</b>
                    <a class="ansibleOptionLink" href="#parameter-document/data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Raw document data with Base64 encoding.</div>
                                            <div>Required when source is &#x27;INLINE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-document/namespace_name"></div>
                    <b>namespace_name</b>
                    <a class="ansibleOptionLink" href="#parameter-document/namespace_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Object Storage namespace.</div>
                                            <div>Required when source is &#x27;OBJECT_STORAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-document/object_name"></div>
                    <b>object_name</b>
                    <a class="ansibleOptionLink" href="#parameter-document/object_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Object Storage object name.</div>
                                            <div>Required when source is &#x27;OBJECT_STORAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-document/source"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-document/source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OBJECT_STORAGE</li>
                                                                                                                                                                                                <li>INLINE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The location of the document data. The allowed values are: - `INLINE`: The data is included directly in the request payload. - `OBJECT_STORAGE`: The document is in OCI Object Storage.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-document_type"></div>
                    <b>document_type</b>
                    <a class="ansibleOptionLink" href="#parameter-document_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>INVOICE</li>
                                                                                                                                                                                                <li>RECEIPT</li>
                                                                                                                                                                                                <li>RESUME</li>
                                                                                                                                                                                                <li>TAX_FORM</li>
                                                                                                                                                                                                <li>DRIVER_LICENSE</li>
                                                                                                                                                                                                <li>PASSPORT</li>
                                                                                                                                                                                                <li>BANK_STATEMENT</li>
                                                                                                                                                                                                <li>CHECK</li>
                                                                                                                                                                                                <li>PAYSLIP</li>
                                                                                                                                                                                                <li>OTHERS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The document type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-features"></div>
                    <b>features</b>
                    <a class="ansibleOptionLink" href="#parameter-features" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The types of document analysis requested.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-features/feature_type"></div>
                    <b>feature_type</b>
                    <a class="ansibleOptionLink" href="#parameter-features/feature_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DOCUMENT_CLASSIFICATION</li>
                                                                                                                                                                                                <li>KEY_VALUE_EXTRACTION</li>
                                                                                                                                                                                                <li>LANGUAGE_CLASSIFICATION</li>
                                                                                                                                                                                                <li>TEXT_EXTRACTION</li>
                                                                                                                                                                                                <li>TABLE_EXTRACTION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of document analysis requested. The allowed values are: - `LANGUAGE_CLASSIFICATION`: Detect the language. - `TEXT_EXTRACTION`: Recognize text. - `TABLE_EXTRACTION`: Detect and extract data in tables. - `KEY_VALUE_EXTRACTION`: Extract form fields. - `DOCUMENT_CLASSIFICATION`: Identify the type of document.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-features/generate_searchable_pdf"></div>
                    <b>generate_searchable_pdf</b>
                    <a class="ansibleOptionLink" href="#parameter-features/generate_searchable_pdf" title="Permalink to this option"></a>
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
                                            <div>Whether or not to generate a searchable PDF file.</div>
                                            <div>Applicable when feature_type is &#x27;TEXT_EXTRACTION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-features/max_results"></div>
                    <b>max_results</b>
                    <a class="ansibleOptionLink" href="#parameter-features/max_results" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum number of results to return.</div>
                                            <div>Applicable when feature_type is one of [&#x27;DOCUMENT_CLASSIFICATION&#x27;, &#x27;LANGUAGE_CLASSIFICATION&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-features/model_id"></div>
                    <b>model_id</b>
                    <a class="ansibleOptionLink" href="#parameter-features/model_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The custom model ID.</div>
                                            <div>Applicable when feature_type is one of [&#x27;KEY_VALUE_EXTRACTION&#x27;, &#x27;DOCUMENT_CLASSIFICATION&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-features/tenancy_id"></div>
                    <b>tenancy_id</b>
                    <a class="ansibleOptionLink" href="#parameter-features/tenancy_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The custom model tenancy ID when modelId represents aliasName.</div>
                                            <div>Applicable when feature_type is one of [&#x27;KEY_VALUE_EXTRACTION&#x27;, &#x27;DOCUMENT_CLASSIFICATION&#x27;]</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-language"></div>
                    <b>language</b>
                    <a class="ansibleOptionLink" href="#parameter-language" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document language, abbreviated according to the BCP 47 syntax.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data"></div>
                    <b>ocr_data</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data" title="Permalink to this option"></a>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/detected_document_types"></div>
                    <b>detected_document_types</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/detected_document_types" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of detected document types.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/detected_document_types/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/detected_document_types/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/detected_document_types/document_id"></div>
                    <b>document_id</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/detected_document_types/document_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the Key-Value Extraction model that was used to extract the key-value pairs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/detected_document_types/document_type"></div>
                    <b>document_type</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/detected_document_types/document_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document type.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/detected_languages"></div>
                    <b>detected_languages</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/detected_languages" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of detected languages.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/detected_languages/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/detected_languages/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/detected_languages/language"></div>
                    <b>language</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/detected_languages/language" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document language, abbreviated according to the BCP 47 syntax.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/document_classification_model_version"></div>
                    <b>document_classification_model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/document_classification_model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document classification model version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/document_metadata"></div>
                    <b>document_metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/document_metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/document_metadata/mime_type"></div>
                    <b>mime_type</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/document_metadata/mime_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The result data format.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/document_metadata/page_count"></div>
                    <b>page_count</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/document_metadata/page_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Teh number of pages in the document.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/errors"></div>
                    <b>errors</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/errors" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The errors encountered during document analysis.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/errors/code"></div>
                    <b>code</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/errors/code" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The error code.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/errors/message"></div>
                    <b>message</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/errors/message" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The error message.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/key_value_extraction_model_version"></div>
                    <b>key_value_extraction_model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/key_value_extraction_model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document keyValue extraction model version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/language_classification_model_version"></div>
                    <b>language_classification_model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/language_classification_model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document language classification model version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages"></div>
                    <b>pages</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The array of a Page.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/detected_document_types"></div>
                    <b>detected_document_types</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/detected_document_types" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of detected document types.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/detected_document_types/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/detected_document_types/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/detected_document_types/document_id"></div>
                    <b>document_id</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/detected_document_types/document_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the Key-Value Extraction model that was used to extract the key-value pairs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/detected_document_types/document_type"></div>
                    <b>document_type</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/detected_document_types/document_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document type.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/detected_languages"></div>
                    <b>detected_languages</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/detected_languages" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of detected languages.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/detected_languages/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/detected_languages/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/detected_languages/language"></div>
                    <b>language</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/detected_languages/language" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document language, abbreviated according to the BCP 47 syntax.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/dimensions"></div>
                    <b>dimensions</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/dimensions" title="Permalink to this option"></a>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/dimensions/height"></div>
                    <b>height</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/dimensions/height" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The height of a page.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/dimensions/unit"></div>
                    <b>unit</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/dimensions/unit" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PIXEL</li>
                                                                                                                                                                                                <li>INCH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The unit of length.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/dimensions/width"></div>
                    <b>width</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/dimensions/width" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>the width of a page.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields"></div>
                    <b>document_fields</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The form fields detected on the page.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_label"></div>
                    <b>field_label</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_label" title="Permalink to this option"></a>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_label/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_label/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_label/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_label/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the field label.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_name"></div>
                    <b>field_name</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_name" title="Permalink to this option"></a>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_name/bounding_polygon"></div>
                    <b>bounding_polygon</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_name/bounding_polygon" title="Permalink to this option"></a>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_name/bounding_polygon/normalized_vertices"></div>
                    <b>normalized_vertices</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_name/bounding_polygon/normalized_vertices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of normalized points defining the polygon&#x27;s perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{&quot;x&quot;: 0, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0.5}, {&quot;x&quot;: 0, &quot;y&quot;: 0.5}]` represents the top half of an image.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_name/bounding_polygon/normalized_vertices/x"></div>
                    <b>x</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_name/bounding_polygon/normalized_vertices/x" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The X-axis normalized coordinate.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_name/bounding_polygon/normalized_vertices/y"></div>
                    <b>y</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_name/bounding_polygon/normalized_vertices/y" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Y-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_name/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_name/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_name/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_name/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the field.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_name/word_indexes"></div>
                    <b>word_indexes</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_name/word_indexes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The indexes of the words in the field name.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_type"></div>
                    <b>field_type</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>LINE_ITEM_GROUP</li>
                                                                                                                                                                                                <li>LINE_ITEM</li>
                                                                                                                                                                                                <li>LINE_ITEM_FIELD</li>
                                                                                                                                                                                                <li>KEY_VALUE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The field type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value"></div>
                    <b>field_value</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/bounding_polygon"></div>
                    <b>bounding_polygon</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/bounding_polygon" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/bounding_polygon/normalized_vertices"></div>
                    <b>normalized_vertices</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/bounding_polygon/normalized_vertices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of normalized points defining the polygon&#x27;s perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{&quot;x&quot;: 0, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0.5}, {&quot;x&quot;: 0, &quot;y&quot;: 0.5}]` represents the top half of an image.</div>
                                            <div>Required when value_type is &#x27;TIME&#x27;</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/bounding_polygon/normalized_vertices/x"></div>
                    <b>x</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/bounding_polygon/normalized_vertices/x" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The X-axis normalized coordinate.</div>
                                            <div>Required when value_type is &#x27;TIME&#x27;</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/bounding_polygon/normalized_vertices/y"></div>
                    <b>y</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/bounding_polygon/normalized_vertices/y" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Y-axis normalized coordinate.</div>
                                            <div>Required when value_type is &#x27;TIME&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The array of values.</div>
                                            <div>Required when value_type is &#x27;ARRAY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/items/field_label"></div>
                    <b>field_label</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/items/field_label" title="Permalink to this option"></a>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/items/field_name"></div>
                    <b>field_name</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/items/field_name" title="Permalink to this option"></a>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/items/field_type"></div>
                    <b>field_type</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/items/field_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>LINE_ITEM_GROUP</li>
                                                                                                                                                                                                <li>LINE_ITEM</li>
                                                                                                                                                                                                <li>LINE_ITEM_FIELD</li>
                                                                                                                                                                                                <li>KEY_VALUE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The field type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/items/field_value"></div>
                    <b>field_value</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/items/field_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/text"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/text" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The detected text of a field.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The time field value as yyyy-mm-dd hh-mm-ss.</div>
                                            <div>Required when value_type is one of [&#x27;DATE&#x27;, &#x27;NUMBER&#x27;, &#x27;STRING&#x27;, &#x27;TIME&#x27;, &#x27;PHONE_NUMBER&#x27;, &#x27;INTEGER&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/value_type"></div>
                    <b>value_type</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/value_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>TIME</li>
                                                                                                                                                                                                <li>INTEGER</li>
                                                                                                                                                                                                <li>DATE</li>
                                                                                                                                                                                                <li>NUMBER</li>
                                                                                                                                                                                                <li>STRING</li>
                                                                                                                                                                                                <li>PHONE_NUMBER</li>
                                                                                                                                                                                                <li>ARRAY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of data detected.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/document_fields/field_value/word_indexes"></div>
                    <b>word_indexes</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/document_fields/field_value/word_indexes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The indexes of the words in the field value.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/lines"></div>
                    <b>lines</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/lines" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The lines of text detected on the page.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/lines/bounding_polygon"></div>
                    <b>bounding_polygon</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/lines/bounding_polygon" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/lines/bounding_polygon/normalized_vertices"></div>
                    <b>normalized_vertices</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/lines/bounding_polygon/normalized_vertices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of normalized points defining the polygon&#x27;s perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{&quot;x&quot;: 0, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0.5}, {&quot;x&quot;: 0, &quot;y&quot;: 0.5}]` represents the top half of an image.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/lines/bounding_polygon/normalized_vertices/x"></div>
                    <b>x</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/lines/bounding_polygon/normalized_vertices/x" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The X-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/lines/bounding_polygon/normalized_vertices/y"></div>
                    <b>y</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/lines/bounding_polygon/normalized_vertices/y" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Y-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/lines/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/lines/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/lines/text"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/lines/text" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The text recognized.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/lines/word_indexes"></div>
                    <b>word_indexes</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/lines/word_indexes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The array of words.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/page_number"></div>
                    <b>page_number</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/page_number" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document page number.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables"></div>
                    <b>tables</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The tables detected on the page.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows"></div>
                    <b>body_rows</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The body rows.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells"></div>
                    <b>cells</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The cells in the row.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/bounding_polygon"></div>
                    <b>bounding_polygon</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/bounding_polygon" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/bounding_polygon/normalized_vertices"></div>
                    <b>normalized_vertices</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/bounding_polygon/normalized_vertices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of normalized points defining the polygon&#x27;s perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{&quot;x&quot;: 0, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0.5}, {&quot;x&quot;: 0, &quot;y&quot;: 0.5}]` represents the top half of an image.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/bounding_polygon/normalized_vertices/x"></div>
                    <b>x</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/bounding_polygon/normalized_vertices/x" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The X-axis normalized coordinate.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/bounding_polygon/normalized_vertices/y"></div>
                    <b>y</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/bounding_polygon/normalized_vertices/y" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Y-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/column_index"></div>
                    <b>column_index</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/column_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The index of the cell inside the column.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/row_index"></div>
                    <b>row_index</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/row_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The index of the cell inside the row.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/text"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/text" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The text recognized in the cell.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/body_rows/cells/word_indexes"></div>
                    <b>word_indexes</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/body_rows/cells/word_indexes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The words detected in the cell.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/bounding_polygon"></div>
                    <b>bounding_polygon</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/bounding_polygon" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/bounding_polygon/normalized_vertices"></div>
                    <b>normalized_vertices</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/bounding_polygon/normalized_vertices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of normalized points defining the polygon&#x27;s perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{&quot;x&quot;: 0, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0.5}, {&quot;x&quot;: 0, &quot;y&quot;: 0.5}]` represents the top half of an image.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/bounding_polygon/normalized_vertices/x"></div>
                    <b>x</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/bounding_polygon/normalized_vertices/x" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The X-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/bounding_polygon/normalized_vertices/y"></div>
                    <b>y</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/bounding_polygon/normalized_vertices/y" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Y-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/column_count"></div>
                    <b>column_count</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/column_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of columns.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows"></div>
                    <b>footer_rows</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>the footer rows.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells"></div>
                    <b>cells</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The cells in the row.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/bounding_polygon"></div>
                    <b>bounding_polygon</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/bounding_polygon" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/bounding_polygon/normalized_vertices"></div>
                    <b>normalized_vertices</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/bounding_polygon/normalized_vertices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of normalized points defining the polygon&#x27;s perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{&quot;x&quot;: 0, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0.5}, {&quot;x&quot;: 0, &quot;y&quot;: 0.5}]` represents the top half of an image.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/bounding_polygon/normalized_vertices/x"></div>
                    <b>x</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/bounding_polygon/normalized_vertices/x" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The X-axis normalized coordinate.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/bounding_polygon/normalized_vertices/y"></div>
                    <b>y</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/bounding_polygon/normalized_vertices/y" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Y-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/column_index"></div>
                    <b>column_index</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/column_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The index of the cell inside the column.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/row_index"></div>
                    <b>row_index</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/row_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The index of the cell inside the row.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/text"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/text" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The text recognized in the cell.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/footer_rows/cells/word_indexes"></div>
                    <b>word_indexes</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/footer_rows/cells/word_indexes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The words detected in the cell.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows"></div>
                    <b>header_rows</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The header rows.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells"></div>
                    <b>cells</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The cells in the row.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/bounding_polygon"></div>
                    <b>bounding_polygon</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/bounding_polygon" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/bounding_polygon/normalized_vertices"></div>
                    <b>normalized_vertices</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/bounding_polygon/normalized_vertices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of normalized points defining the polygon&#x27;s perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{&quot;x&quot;: 0, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0.5}, {&quot;x&quot;: 0, &quot;y&quot;: 0.5}]` represents the top half of an image.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/bounding_polygon/normalized_vertices/x"></div>
                    <b>x</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/bounding_polygon/normalized_vertices/x" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The X-axis normalized coordinate.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/bounding_polygon/normalized_vertices/y"></div>
                    <b>y</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/bounding_polygon/normalized_vertices/y" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Y-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/column_index"></div>
                    <b>column_index</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/column_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The index of the cell inside the column.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/row_index"></div>
                    <b>row_index</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/row_index" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The index of the cell inside the row.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/text"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/text" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The text recognized in the cell.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/header_rows/cells/word_indexes"></div>
                    <b>word_indexes</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/header_rows/cells/word_indexes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The words detected in the cell.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/tables/row_count"></div>
                    <b>row_count</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/tables/row_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of rows.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/words"></div>
                    <b>words</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/words" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The words detected on the page.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/words/bounding_polygon"></div>
                    <b>bounding_polygon</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/words/bounding_polygon" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
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
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/words/bounding_polygon/normalized_vertices"></div>
                    <b>normalized_vertices</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/words/bounding_polygon/normalized_vertices" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of normalized points defining the polygon&#x27;s perimeter, with an implicit segment between subsequent points and between the first and last point. Rectangles are defined with four points. For example, `[{&quot;x&quot;: 0, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0}, {&quot;x&quot;: 1, &quot;y&quot;: 0.5}, {&quot;x&quot;: 0, &quot;y&quot;: 0.5}]` represents the top half of an image.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/words/bounding_polygon/normalized_vertices/x"></div>
                    <b>x</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/words/bounding_polygon/normalized_vertices/x" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The X-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/words/bounding_polygon/normalized_vertices/y"></div>
                    <b>y</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/words/bounding_polygon/normalized_vertices/y" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Y-axis normalized coordinate.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/words/confidence"></div>
                    <b>confidence</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/words/confidence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>the confidence score between 0 and 1.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/pages/words/text"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/pages/words/text" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The string of text characters in the word.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/searchable_pdf"></div>
                    <b>searchable_pdf</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/searchable_pdf" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The searchable PDF file that was generated.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/table_extraction_model_version"></div>
                    <b>table_extraction_model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/table_extraction_model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document table extraction model version.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-ocr_data/text_extraction_model_version"></div>
                    <b>text_extraction_model_version</b>
                    <a class="ansibleOptionLink" href="#parameter-ocr_data/text_extraction_model_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The document text extraction model version.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="parameter-output_location"></div>
                    <b>output_location</b>
                    <a class="ansibleOptionLink" href="#parameter-output_location" title="Permalink to this option"></a>
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
                    <div class="ansibleOptionAnchor" id="parameter-output_location/bucket_name"></div>
                    <b>bucket_name</b>
                    <a class="ansibleOptionLink" href="#parameter-output_location/bucket_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Object Storage bucket name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-output_location/namespace_name"></div>
                    <b>namespace_name</b>
                    <a class="ansibleOptionLink" href="#parameter-output_location/namespace_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Object Storage namespace.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-output_location/prefix"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-output_location/prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Object Storage folder name.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="8">
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

    
    - name: Perform action analyze_document on analyze_document_result
      oci_ai_document_analyze_document_result_actions:
        # required
        features:
        - # required
          feature_type: DOCUMENT_CLASSIFICATION

          # optional
          model_id: "ocid1.model.oc1..xxxxxxEXAMPLExxxxxx"
          tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
          max_results: 56
        document:
          # required
          namespace_name: namespace_name_example
          bucket_name: bucket_name_example
          object_name: object_name_example
          source: OBJECT_STORAGE
        action: analyze_document

        # optional
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        output_location:
          # required
          namespace_name: namespace_name_example
          bucket_name: bucket_name_example
          prefix: prefix_example
        language: language_example
        document_type: INVOICE
        ocr_data:
          # required
          document_metadata:
            # required
            page_count: 56
            mime_type: mime_type_example
          pages:
          - # required
            page_number: 56

            # optional
            dimensions:
              # required
              width: 3.4
              height: 3.4
              unit: PIXEL
            detected_document_types:
            - # required
              document_type: document_type_example
              confidence: 3.4

              # optional
              document_id: "ocid1.document.oc1..xxxxxxEXAMPLExxxxxx"
            detected_languages:
            - # required
              language: language_example
              confidence: 3.4
            words:
            - # required
              text: text_example
              confidence: 3.4
              bounding_polygon:
                # required
                normalized_vertices:
                - # required
                  x: 3.4
                  y: 3.4
            lines:
            - # required
              text: text_example
              confidence: 3.4
              bounding_polygon:
                # required
                normalized_vertices:
                - # required
                  x: 3.4
                  y: 3.4
              word_indexes: [ "word_indexes_example" ]
            tables:
            - # required
              row_count: 56
              column_count: 56
              header_rows:
              - # required
                cells:
                - # required
                  text: text_example
                  row_index: 56
                  column_index: 56
                  confidence: 3.4
                  bounding_polygon:
                    # required
                    normalized_vertices:
                    - # required
                      x: 3.4
                      y: 3.4
                  word_indexes: [ "word_indexes_example" ]
              body_rows:
              - # required
                cells:
                - # required
                  text: text_example
                  row_index: 56
                  column_index: 56
                  confidence: 3.4
                  bounding_polygon:
                    # required
                    normalized_vertices:
                    - # required
                      x: 3.4
                      y: 3.4
                  word_indexes: [ "word_indexes_example" ]
              footer_rows:
              - # required
                cells:
                - # required
                  text: text_example
                  row_index: 56
                  column_index: 56
                  confidence: 3.4
                  bounding_polygon:
                    # required
                    normalized_vertices:
                    - # required
                      x: 3.4
                      y: 3.4
                  word_indexes: [ "word_indexes_example" ]
              confidence: 3.4
              bounding_polygon:
                # required
                normalized_vertices:
                - # required
                  x: 3.4
                  y: 3.4
            document_fields:
            - # required
              field_type: LINE_ITEM_GROUP
              field_value:
                # required
                value: value_example
                value_type: TIME
                confidence: 3.4
                bounding_polygon:
                  # required
                  normalized_vertices:
                  - # required
                    x: 3.4
                    y: 3.4
                word_indexes: [ "word_indexes_example" ]

                    # optional
                text: text_example

              # optional
              field_label:
                # required
                name: name_example

                # optional
                confidence: 3.4
              field_name:
                # required
                name: name_example

                # optional
                confidence: 3.4
                bounding_polygon:
                  # required
                  normalized_vertices:
                  - # required
                    x: 3.4
                    y: 3.4
                word_indexes: [ "word_indexes_example" ]

                    # optional
          detected_document_types:
          - # required
            document_type: document_type_example
            confidence: 3.4

            # optional
            document_id: "ocid1.document.oc1..xxxxxxEXAMPLExxxxxx"
          detected_languages:
          - # required
            language: language_example
            confidence: 3.4
          document_classification_model_version: document_classification_model_version_example
          language_classification_model_version: language_classification_model_version_example
          text_extraction_model_version: text_extraction_model_version_example
          key_value_extraction_model_version: key_value_extraction_model_version_example
          table_extraction_model_version: table_extraction_model_version_example
          errors:
          - # required
            code: code_example
            message: message_example
          searchable_pdf: searchable_pdf_example





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

        Unable to normalize oci_ai_document_analyze_document_result_actions: return due to: 3 validation errors for PluginReturnSchema
        return -> analyze_document_result -> contains -> pages -> contains -> document_fields -> contains -> field_value -> contains -> items -> contains -> field_label -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> analyze_document_result -> contains -> pages -> contains -> document_fields -> contains -> field_value -> contains -> items -> contains -> field_name -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)
        return -> analyze_document_result -> contains -> pages -> contains -> document_fields -> contains -> field_value -> contains -> items -> contains -> field_value -> type
          string does not match regex "^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$" (type=value_error.str.regex; pattern=^(any|bits|bool|bytes|complex|dict|float|int|json|jsonarg|list|path|sid|str|pathspec|pathlist)$)

