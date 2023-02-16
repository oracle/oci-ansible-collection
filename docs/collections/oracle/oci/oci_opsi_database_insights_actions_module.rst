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

.. _ansible_collections.oracle.oci.oci_opsi_database_insights_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_opsi_database_insights_actions -- Perform actions on a DatabaseInsights resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.13.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_opsi_database_insights_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on a DatabaseInsights resource in Oracle Cloud Infrastructure
- For *action=change*, moves a DatabaseInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.
- For *action=change_pe_comanaged*, change the connection details of a co-managed  database insight. When provided, If-Match is checked against ETag values of the resource.
- For *action=disable*, disables a database in Operations Insights. Database metric collection and analysis will be stopped.
- For *action=enable*, enables a database in Operations Insights. Database metric collection and analysis will be started.
- For *action=ingest_database_configuration*, this is a generic ingest endpoint for all database configuration metrics.
- For *action=ingest_sql_bucket*, the sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline. Either databaseId or id must be specified.
- For *action=ingest_sql_plan_lines*, the SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. Either databaseId or id must be specified.
- For *action=ingest_sql_stats*, the SQL Stats endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline. Either databaseId or id must be specified.
- For *action=ingest_sql_text*, the SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. Either databaseId or id must be specified. Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.


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
                    <div class="ansibleOptionAnchor" id="parameter-action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>change</li>
                                                                                                                                                                                                <li>change_pe_comanaged</li>
                                                                                                                                                                                                <li>disable</li>
                                                                                                                                                                                                <li>enable</li>
                                                                                                                                                                                                <li>ingest_database_configuration</li>
                                                                                                                                                                                                <li>ingest_sql_bucket</li>
                                                                                                                                                                                                <li>ingest_sql_plan_lines</li>
                                                                                                                                                                                                <li>ingest_sql_stats</li>
                                                                                                                                                                                                <li>ingest_sql_text</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the DatabaseInsights.</div>
                                                        </td>
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
                                            <div>The OCID of the compartment into which the resource should be moved.</div>
                                            <div>Required for <em>action=change</em>.</div>
                                            <div>Required when $p.relatedDiscriminatorFieldName is &#x27;PE_COMANAGED_DATABASE&#x27;</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-credential_details"></div>
                    <b>credential_details</b>
                    <a class="ansibleOptionLink" href="#parameter-credential_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required for <em>action=change_pe_comanaged</em>.</div>
                                            <div>Required when $p.relatedDiscriminatorFieldName is &#x27;PE_COMANAGED_DATABASE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-credential_details/credential_source_name"></div>
                    <b>credential_source_name</b>
                    <a class="ansibleOptionLink" href="#parameter-credential_details/credential_source_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-credential_details/credential_type"></div>
                    <b>credential_type</b>
                    <a class="ansibleOptionLink" href="#parameter-credential_details/credential_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CREDENTIALS_BY_SOURCE</li>
                                                                                                                                                                                                <li>CREDENTIALS_BY_VAULT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Credential type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-credential_details/password_secret_id"></div>
                    <b>password_secret_id</b>
                    <a class="ansibleOptionLink" href="#parameter-credential_details/password_secret_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The secret <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> mapping to the database credentials.</div>
                                            <div>Applicable when credential_type is &#x27;CREDENTIALS_BY_VAULT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-credential_details/role"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#parameter-credential_details/role" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NORMAL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>database user role.</div>
                                            <div>Applicable when credential_type is &#x27;CREDENTIALS_BY_VAULT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-credential_details/user_name"></div>
                    <b>user_name</b>
                    <a class="ansibleOptionLink" href="#parameter-credential_details/user_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>database user name.</div>
                                            <div>Applicable when credential_type is &#x27;CREDENTIALS_BY_VAULT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database_id"></div>
                    <b>database_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Optional <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the associated DBaaS entity.</div>
                                            <div>Applicable only for <em>action=ingest_database_configuration</em><em>action=ingest_sql_bucket</em><em>action=ingest_sql_plan_lines</em><em>action=ingest_sql_stats</em><em>a ction=ingest_sql_text</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database_insight_id"></div>
                    <b>database_insight_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database_insight_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique database insight identifier</div>
                                            <div>Required for <em>action=change</em>, <em>action=change_pe_comanaged</em>, <em>action=disable</em>, <em>action=enable</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                            <div>Applicable only for <em>action=enable</em>.</div>
                                            <div>Applicable when entity_source is &#x27;PE_COMANAGED_DATABASE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-entity_source"></div>
                    <b>entity_source</b>
                    <a class="ansibleOptionLink" href="#parameter-entity_source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>EM_MANAGED_EXTERNAL_DATABASE</li>
                                                                                                                                                                                                <li>PE_COMANAGED_DATABASE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Source of the database entity.</div>
                                            <div>Required for <em>action=enable</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                            <div>Applicable only for <em>action=enable</em>.</div>
                                            <div>Applicable when entity_source is &#x27;PE_COMANAGED_DATABASE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div><a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the database insight resource.</div>
                                            <div>Applicable only for <em>action=ingest_database_configuration</em><em>action=ingest_sql_bucket</em><em>action=ingest_sql_plan_lines</em><em>action=ingest_sql_stats</em><em>a ction=ingest_sql_text</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Array of one or more database configuration metrics objects.</div>
                                            <div>Required for <em>action=ingest_database_configuration</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/access_predicates"></div>
                    <b>access_predicates</b>
                    <a class="ansibleOptionLink" href="#parameter-items/access_predicates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Access predicates Example: `&quot;\&quot;RESOURCE_ID\&quot;=:1 AND \&quot;QUERY_ID\&quot;=:2&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-items/action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Contains the name of the action that was executing when the SQL statement was first parsed, which is set by calling DBMS_APPLICATION_INFO.SET_ACTION</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/application_wait_time_in_us"></div>
                    <b>application_wait_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/application_wait_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Application wait time (in microseconds)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/avg_hard_parse_time_in_us"></div>
                    <b>avg_hard_parse_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/avg_hard_parse_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Average hard parse time (in microseconds) used by this cursor</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/avoided_executions"></div>
                    <b>avoided_executions</b>
                    <a class="ansibleOptionLink" href="#parameter-items/avoided_executions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of executions attempted on this object, but prevented due to the SQL statement being in quarantine</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/bucket_id"></div>
                    <b>bucket_id</b>
                    <a class="ansibleOptionLink" href="#parameter-items/bucket_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SQL Bucket ID, examples &lt;= 3 secs, 3-10 secs, 10-60 secs, 1-5 min, &gt; 5 min Example: `&quot;&lt;= 3 secs&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/buffer_gets"></div>
                    <b>buffer_gets</b>
                    <a class="ansibleOptionLink" href="#parameter-items/buffer_gets" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of Buffer Gets</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/bytes"></div>
                    <b>bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Bytes Example: `150`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/cardinality"></div>
                    <b>cardinality</b>
                    <a class="ansibleOptionLink" href="#parameter-items/cardinality" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Cardinality Example: `1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/cdb"></div>
                    <b>cdb</b>
                    <a class="ansibleOptionLink" href="#parameter-items/cdb" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Indicates if it is a CDB or not. This would be &#x27;yes&#x27; or &#x27;no&#x27;.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/child_number"></div>
                    <b>child_number</b>
                    <a class="ansibleOptionLink" href="#parameter-items/child_number" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of this child cursor</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/cluster_wait_time_in_us"></div>
                    <b>cluster_wait_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/cluster_wait_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Cluster wait time (in microseconds). This value is specific to Oracle RAC</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/command_type"></div>
                    <b>command_type</b>
                    <a class="ansibleOptionLink" href="#parameter-items/command_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Oracle command type definition</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/concurrency_wait_time_in_us"></div>
                    <b>concurrency_wait_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/concurrency_wait_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Concurrency wait time (in microseconds)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/control_file_type"></div>
                    <b>control_file_type</b>
                    <a class="ansibleOptionLink" href="#parameter-items/control_file_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Type of control file.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/cost"></div>
                    <b>cost</b>
                    <a class="ansibleOptionLink" href="#parameter-items/cost" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Cost Example: `1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/cpu_cost"></div>
                    <b>cpu_cost</b>
                    <a class="ansibleOptionLink" href="#parameter-items/cpu_cost" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>CPU cost Example: `7321`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/cpu_count"></div>
                    <b>cpu_count</b>
                    <a class="ansibleOptionLink" href="#parameter-items/cpu_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total number of CPUs allocated for the host.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/cpu_time_in_sec"></div>
                    <b>cpu_time_in_sec</b>
                    <a class="ansibleOptionLink" href="#parameter-items/cpu_time_in_sec" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total CPU time Example: `1046`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/cpu_time_in_us"></div>
                    <b>cpu_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/cpu_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>CPU time (in microseconds) used by this cursor for parsing, executing, and fetching</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/created"></div>
                    <b>created</b>
                    <a class="ansibleOptionLink" href="#parameter-items/created" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Creation time.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/database_role"></div>
                    <b>database_role</b>
                    <a class="ansibleOptionLink" href="#parameter-items/database_role" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Current role of the database.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/database_status"></div>
                    <b>database_status</b>
                    <a class="ansibleOptionLink" href="#parameter-items/database_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Status of the database.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/database_type"></div>
                    <b>database_type</b>
                    <a class="ansibleOptionLink" href="#parameter-items/database_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Operations Insights internal representation of the database type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/db_external_instance_version"></div>
                    <b>db_external_instance_version</b>
                    <a class="ansibleOptionLink" href="#parameter-items/db_external_instance_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Database version.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/delta_cpu_rank"></div>
                    <b>delta_cpu_rank</b>
                    <a class="ansibleOptionLink" href="#parameter-items/delta_cpu_rank" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rank based on CPU Consumption</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/delta_cpu_time"></div>
                    <b>delta_cpu_time</b>
                    <a class="ansibleOptionLink" href="#parameter-items/delta_cpu_time" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>CPU time (in microseconds) for the cursor since the last AWR snapshot</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/delta_execs_rank"></div>
                    <b>delta_execs_rank</b>
                    <a class="ansibleOptionLink" href="#parameter-items/delta_execs_rank" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rank based on number of execution</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/delta_execution_count"></div>
                    <b>delta_execution_count</b>
                    <a class="ansibleOptionLink" href="#parameter-items/delta_execution_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of executions for the cursor since the last AWR snapshot</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/delta_io_bytes"></div>
                    <b>delta_io_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/delta_io_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of I/O bytes exchanged between the Oracle database and the storage system for the cursor since the last AWR snapshot</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/delta_io_rank"></div>
                    <b>delta_io_rank</b>
                    <a class="ansibleOptionLink" href="#parameter-items/delta_io_rank" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rank based on I/O Consumption</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/depth"></div>
                    <b>depth</b>
                    <a class="ansibleOptionLink" href="#parameter-items/depth" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Depth Example: `3`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/direct_reads"></div>
                    <b>direct_reads</b>
                    <a class="ansibleOptionLink" href="#parameter-items/direct_reads" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of direct reads</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/direct_writes"></div>
                    <b>direct_writes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/direct_writes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of Direct writes</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/disk_reads"></div>
                    <b>disk_reads</b>
                    <a class="ansibleOptionLink" href="#parameter-items/disk_reads" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of disk reads</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/distribution"></div>
                    <b>distribution</b>
                    <a class="ansibleOptionLink" href="#parameter-items/distribution" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Distribution Example: `&quot;QC (RANDOM)&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/edition"></div>
                    <b>edition</b>
                    <a class="ansibleOptionLink" href="#parameter-items/edition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The edition of the database.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/elapsed_time_in_sec"></div>
                    <b>elapsed_time_in_sec</b>
                    <a class="ansibleOptionLink" href="#parameter-items/elapsed_time_in_sec" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total elapsed time Example: `1.2`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/elapsed_time_in_us"></div>
                    <b>elapsed_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/elapsed_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/end_of_fetch_count"></div>
                    <b>end_of_fetch_count</b>
                    <a class="ansibleOptionLink" href="#parameter-items/end_of_fetch_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of times this cursor was fully executed since the cursor was brought into the library cache</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/exact_matching_signature"></div>
                    <b>exact_matching_signature</b>
                    <a class="ansibleOptionLink" href="#parameter-items/exact_matching_signature" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>exact_matching_signature Example: `&quot;18067345456756876713&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/executions"></div>
                    <b>executions</b>
                    <a class="ansibleOptionLink" href="#parameter-items/executions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of executions</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/executions_count"></div>
                    <b>executions_count</b>
                    <a class="ansibleOptionLink" href="#parameter-items/executions_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total number of executions Example: `60`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/fetches"></div>
                    <b>fetches</b>
                    <a class="ansibleOptionLink" href="#parameter-items/fetches" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of fetches</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/filter_predicates"></div>
                    <b>filter_predicates</b>
                    <a class="ansibleOptionLink" href="#parameter-items/filter_predicates" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Filter predicates Example: `&quot;(INTERNAL_FUNCTION(\&quot;J\&quot;.\&quot;DATABASE_ROLE\&quot;) OR (\&quot;J\&quot;.\&quot;DATABASE_ROLE\&quot; IS NULL AND SYS_CONTEXT(&#x27;userenv&#x27;,&#x27;database_role&#x27;)=&#x27;PRIMARY&#x27;))&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/force_matching_signature"></div>
                    <b>force_matching_signature</b>
                    <a class="ansibleOptionLink" href="#parameter-items/force_matching_signature" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>force_matching_signature Example: `&quot;18067345456756876713&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/full_plan_hash_value"></div>
                    <b>full_plan_hash_value</b>
                    <a class="ansibleOptionLink" href="#parameter-items/full_plan_hash_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total Number of rows in SQLStats table</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/guard_status"></div>
                    <b>guard_status</b>
                    <a class="ansibleOptionLink" href="#parameter-items/guard_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Data protection policy.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/harmonic_sum"></div>
                    <b>harmonic_sum</b>
                    <a class="ansibleOptionLink" href="#parameter-items/harmonic_sum" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Harmonic sum based on ranking parameters</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/host_memory_capacity"></div>
                    <b>host_memory_capacity</b>
                    <a class="ansibleOptionLink" href="#parameter-items/host_memory_capacity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total amount of usable Physical RAM Memory available in gigabytes.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/host_name"></div>
                    <b>host_name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/host_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Host name of the database instance.</div>
                                            <div>Required when metric_name is one of [&#x27;DB_EXTERNAL_INSTANCE&#x27;, &#x27;DB_OS_CONFIG_INSTANCE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/identifier"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-items/identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Identifier Example: `3`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/instance_name"></div>
                    <b>instance_name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/instance_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the database instance.</div>
                                            <div>Required when metric_name is one of [&#x27;DB_EXTERNAL_INSTANCE&#x27;, &#x27;DB_OS_CONFIG_INSTANCE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/instance_role"></div>
                    <b>instance_role</b>
                    <a class="ansibleOptionLink" href="#parameter-items/instance_role" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Role (permissions) of the database instance.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/invalidations"></div>
                    <b>invalidations</b>
                    <a class="ansibleOptionLink" href="#parameter-items/invalidations" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of times this child cursor has been invalidated</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/io_cell_offload_eligible_bytes"></div>
                    <b>io_cell_offload_eligible_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/io_cell_offload_eligible_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of I/O bytes which can be filtered by the Exadata storage system</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/io_cell_offload_returned_bytes"></div>
                    <b>io_cell_offload_returned_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/io_cell_offload_returned_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of bytes that are returned by Exadata cell through the regular I/O path</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/io_cell_uncompressed_bytes"></div>
                    <b>io_cell_uncompressed_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/io_cell_uncompressed_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/io_cost"></div>
                    <b>io_cost</b>
                    <a class="ansibleOptionLink" href="#parameter-items/io_cost" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>IO cost Example: `1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/io_interconnect_bytes"></div>
                    <b>io_interconnect_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/io_interconnect_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of I/O bytes exchanged between Oracle Database and the storage system. Typically used for Cache Fusion or parallel queries</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/io_time_in_sec"></div>
                    <b>io_time_in_sec</b>
                    <a class="ansibleOptionLink" href="#parameter-items/io_time_in_sec" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total IO time Example: `5810`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/java_exec_time_in_us"></div>
                    <b>java_exec_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/java_exec_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Java execution time (in microseconds)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/last_active_time"></div>
                    <b>last_active_time</b>
                    <a class="ansibleOptionLink" href="#parameter-items/last_active_time" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>last_active_time Example: `&quot;0000000099CCE300&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/loads"></div>
                    <b>loads</b>
                    <a class="ansibleOptionLink" href="#parameter-items/loads" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of times the object was either loaded or reloaded</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/log_mode"></div>
                    <b>log_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-items/log_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Archive log mode.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/logins"></div>
                    <b>logins</b>
                    <a class="ansibleOptionLink" href="#parameter-items/logins" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Indicates if logins are allowed or restricted.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/metric_name"></div>
                    <b>metric_name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/metric_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DB_OS_CONFIG_INSTANCE</li>
                                                                                                                                                                                                <li>DB_EXTERNAL_INSTANCE</li>
                                                                                                                                                                                                <li>DB_EXTERNAL_PROPERTIES</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Name of the metric group.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/module"></div>
                    <b>module</b>
                    <a class="ansibleOptionLink" href="#parameter-items/module" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Module name</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the database.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/num_cp_us"></div>
                    <b>num_cp_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/num_cp_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total number of CPUs available.</div>
                                            <div>Applicable when metric_name is &#x27;DB_OS_CONFIG_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/num_cpu_cores"></div>
                    <b>num_cpu_cores</b>
                    <a class="ansibleOptionLink" href="#parameter-items/num_cpu_cores" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of CPU cores available (includes subcores of multicore CPUs as well as single-core CPUs).</div>
                                            <div>Applicable when metric_name is &#x27;DB_OS_CONFIG_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/num_cpu_sockets"></div>
                    <b>num_cpu_sockets</b>
                    <a class="ansibleOptionLink" href="#parameter-items/num_cpu_sockets" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of CPU Sockets available.</div>
                                            <div>Applicable when metric_name is &#x27;DB_OS_CONFIG_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_alias"></div>
                    <b>object_alias</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_alias" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Object Alias Example: `&quot;PLAN_LINES@SEL$1&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_instance"></div>
                    <b>object_instance</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_instance" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Object Instance Example: `37472`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_name"></div>
                    <b>object_name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Object Name Example: `&quot;PLAN_LINES_PK&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_node"></div>
                    <b>object_node</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_node" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Object Node Example: `&quot;Q4000&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_owner"></div>
                    <b>object_owner</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_owner" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Object Owner Example: `&quot;TENANT_A#SCHEMA&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_type"></div>
                    <b>object_type</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Object Type Example: `&quot;INDEX (UNIQUE)&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/obsolete_count"></div>
                    <b>obsolete_count</b>
                    <a class="ansibleOptionLink" href="#parameter-items/obsolete_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of times that a parent cursor became obsolete</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/open_mode"></div>
                    <b>open_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-items/open_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Open mode information.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/operation"></div>
                    <b>operation</b>
                    <a class="ansibleOptionLink" href="#parameter-items/operation" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Operation Example: `&quot;SELECT STATEMENT&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/optimizer"></div>
                    <b>optimizer</b>
                    <a class="ansibleOptionLink" href="#parameter-items/optimizer" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Optimizer Example: `&quot;CLUSTER&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/optimizer_cost"></div>
                    <b>optimizer_cost</b>
                    <a class="ansibleOptionLink" href="#parameter-items/optimizer_cost" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Cost of this query given by the optimizer</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/options"></div>
                    <b>options</b>
                    <a class="ansibleOptionLink" href="#parameter-items/options" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Options Example: `&quot;RANGE SCAN&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/other"></div>
                    <b>other</b>
                    <a class="ansibleOptionLink" href="#parameter-items/other" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Other Example: ``</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/other_tag"></div>
                    <b>other_tag</b>
                    <a class="ansibleOptionLink" href="#parameter-items/other_tag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Other Tag Example: `&quot;PARALLEL_COMBINED_WITH_PARENT&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/other_wait_time_in_sec"></div>
                    <b>other_wait_time_in_sec</b>
                    <a class="ansibleOptionLink" href="#parameter-items/other_wait_time_in_sec" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total other wait time Example: `24061`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/other_xml"></div>
                    <b>other_xml</b>
                    <a class="ansibleOptionLink" href="#parameter-items/other_xml" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Other SQL Example: `&quot;&lt;other_xml&gt;&lt;info type=\&quot;db_version\&quot;&gt;18.0.0.0&lt;/info&gt;&lt;info type=\&quot;parse_schema\&quot;&gt;&lt;![CDATA[\&quot;SYS\&quot;]]&gt;&lt;/info&gt;&lt;info type=\&quot;plan_hash_full\&quot;&gt;483892784&lt;/info&gt;&lt;info type=\&quot;plan_hash\&quot;&gt;2709293936&lt;/info&gt;&lt;info type=\&quot;plan_hash_2\&quot;&gt;483892784&lt;/info&gt;&lt;outline_data&gt;&lt;hint&gt;&lt;![CDATA[IGNORE_OPT IM_EMBEDDED_HINTS]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;![CDATA[OPTIMIZER_FEATURES_ENABLE(&#x27;18.1.0&#x27;)]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;![CDATA[DB_VERSION(&#x27;18.1.0&#x27;)]]&gt;&lt;/hint&gt;&lt;hint&gt; &lt;![CDATA[OPT_PARAM(&#x27;_b_tree_bitmap_plans&#x27; &#x27;false&#x27;)]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;![CDATA[OPT_PARAM(&#x27;_optim_peek_user_binds&#x27; &#x27;false&#x27;)]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;![CDATA[OPT_PARAM(&#x27;result_cache_mode&#x27; &#x27;FORCE&#x27;)]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;![CDATA[OPT_PARAM(&#x27;_fix_control&#x27; &#x27;20648883:0 27745220:1 30001331:1 30142527:1 30539126:1&#x27;)]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;![CDATA[OUTLINE_LEAF(@\&quot;SEL$1\&quot;)]]&gt;&lt;/hint&gt;&lt;hint&gt;&lt;![CDATA[INDEX(@\&quot;SEL$1\&quot; \&quot;USER$\&quot;@\&quot;SEL$1\&quot; \&quot;I_USER#\&quot;)]]&gt;&lt;/hint&gt;&lt;/outline_data&gt;&lt;/other_xml&gt;&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/parallel"></div>
                    <b>parallel</b>
                    <a class="ansibleOptionLink" href="#parameter-items/parallel" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Indicates whether the instance is mounted in cluster database mode (YES) or not (NO).</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/parent_identifier"></div>
                    <b>parent_identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-items/parent_identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Parent Identifier Example: `2`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/parse_calls"></div>
                    <b>parse_calls</b>
                    <a class="ansibleOptionLink" href="#parameter-items/parse_calls" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total integer of parse calls Example: `60`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/partition_identifier"></div>
                    <b>partition_identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-items/partition_identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Partition identifier Example: `8`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/partition_start"></div>
                    <b>partition_start</b>
                    <a class="ansibleOptionLink" href="#parameter-items/partition_start" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Partition start Example: `1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/partition_stop"></div>
                    <b>partition_stop</b>
                    <a class="ansibleOptionLink" href="#parameter-items/partition_stop" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Partition stop Example: `2`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/physical_memory_bytes"></div>
                    <b>physical_memory_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/physical_memory_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total number of bytes of physical memory.</div>
                                            <div>Applicable when metric_name is &#x27;DB_OS_CONFIG_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/physical_read_bytes"></div>
                    <b>physical_read_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/physical_read_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of bytes read from disks by the monitored SQL</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/physical_read_requests"></div>
                    <b>physical_read_requests</b>
                    <a class="ansibleOptionLink" href="#parameter-items/physical_read_requests" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of physical read I/O requests issued by the monitored SQL. The requests may not be disk reads</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/physical_write_bytes"></div>
                    <b>physical_write_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/physical_write_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of bytes written to disks by the monitored SQL</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/physical_write_requests"></div>
                    <b>physical_write_requests</b>
                    <a class="ansibleOptionLink" href="#parameter-items/physical_write_requests" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of physical write I/O requests issued by the monitored SQL</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/plan_hash"></div>
                    <b>plan_hash</b>
                    <a class="ansibleOptionLink" href="#parameter-items/plan_hash" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Plan hash value for the SQL Execution Plan</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/plan_hash_value"></div>
                    <b>plan_hash_value</b>
                    <a class="ansibleOptionLink" href="#parameter-items/plan_hash_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Plan hash value for the SQL Execution Plan</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/platform_name"></div>
                    <b>platform_name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/platform_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Platform name of the database, OS with architecture.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/plsql_exec_time_in_us"></div>
                    <b>plsql_exec_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/plsql_exec_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>PL/SQL execution time (in microseconds)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/position"></div>
                    <b>position</b>
                    <a class="ansibleOptionLink" href="#parameter-items/position" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Position Example: `1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/projection"></div>
                    <b>projection</b>
                    <a class="ansibleOptionLink" href="#parameter-items/projection" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Projection Example: `&quot;COUNT(*)[22]&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/px_servers_executions"></div>
                    <b>px_servers_executions</b>
                    <a class="ansibleOptionLink" href="#parameter-items/px_servers_executions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total number of executions performed by parallel execution servers (0 when the statement has never been executed in parallel)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/qblock_name"></div>
                    <b>qblock_name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/qblock_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Qblock Name Example: `&quot;SEL$1&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/remark"></div>
                    <b>remark</b>
                    <a class="ansibleOptionLink" href="#parameter-items/remark" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Remark Example: `&quot;&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/rows_processed"></div>
                    <b>rows_processed</b>
                    <a class="ansibleOptionLink" href="#parameter-items/rows_processed" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of row processed</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/search_columns"></div>
                    <b>search_columns</b>
                    <a class="ansibleOptionLink" href="#parameter-items/search_columns" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Search Columns Example: `3`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/serializable_aborts"></div>
                    <b>serializable_aborts</b>
                    <a class="ansibleOptionLink" href="#parameter-items/serializable_aborts" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of serializable aborts</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/service"></div>
                    <b>service</b>
                    <a class="ansibleOptionLink" href="#parameter-items/service" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Service name</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sharable_mem"></div>
                    <b>sharable_mem</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sharable_mem" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total shared memory (in bytes) currently occupied by all cursors with this SQL text and plan</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sharable_mem_rank"></div>
                    <b>sharable_mem_rank</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sharable_mem_rank" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rank based on sharable memory</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sorts"></div>
                    <b>sorts</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sorts" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of sorts that were done for the child cursor</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sql_command"></div>
                    <b>sql_command</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sql_command" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SQL command Example: `&quot;SELECT&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sql_full_text"></div>
                    <b>sql_full_text</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sql_full_text" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Full SQL Text Example: `&quot;SELECT username,profile,default_tablespace,temporary_tablespace FROM dba_users&quot;` Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sql_identifier"></div>
                    <b>sql_identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sql_identifier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique SQL_ID for a SQL Statement.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sql_patch"></div>
                    <b>sql_patch</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sql_patch" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SQL patch used for this statement, if any</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sql_plan_baseline"></div>
                    <b>sql_plan_baseline</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sql_plan_baseline" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SQL plan baseline used for this statement, if any</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/sql_profile"></div>
                    <b>sql_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-items/sql_profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>SQL profile used for this statement, if any</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/startup_time"></div>
                    <b>startup_time</b>
                    <a class="ansibleOptionLink" href="#parameter-items/startup_time" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Start up time of the database instance.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-items/status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Status of the instance.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_INSTANCE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/switchover_status"></div>
                    <b>switchover_status</b>
                    <a class="ansibleOptionLink" href="#parameter-items/switchover_status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Indicates whether switchover is allowed.</div>
                                            <div>Applicable when metric_name is &#x27;DB_EXTERNAL_PROPERTIES&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/temp_space"></div>
                    <b>temp_space</b>
                    <a class="ansibleOptionLink" href="#parameter-items/temp_space" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Time space Example: `15614000`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/time_collected"></div>
                    <b>time_collected</b>
                    <a class="ansibleOptionLink" href="#parameter-items/time_collected" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Collection timestamp Example: `&quot;2020-05-06T00:00:00.000Z&quot;`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/total_sharable_mem"></div>
                    <b>total_sharable_mem</b>
                    <a class="ansibleOptionLink" href="#parameter-items/total_sharable_mem" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total shared memory (in bytes) occupied by all cursors with this SQL text and plan if they were to be fully loaded in the shared pool (that is, cursor size)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/total_sql_count"></div>
                    <b>total_sql_count</b>
                    <a class="ansibleOptionLink" href="#parameter-items/total_sql_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total number of rows in SQLStats table</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/total_time_in_sec"></div>
                    <b>total_time_in_sec</b>
                    <a class="ansibleOptionLink" href="#parameter-items/total_time_in_sec" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Total time Example: `30917`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/type_check_mem"></div>
                    <b>type_check_mem</b>
                    <a class="ansibleOptionLink" href="#parameter-items/type_check_mem" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Typecheck memory</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/user_io_wait_time_in_us"></div>
                    <b>user_io_wait_time_in_us</b>
                    <a class="ansibleOptionLink" href="#parameter-items/user_io_wait_time_in_us" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User I/O wait time (in microseconds)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/users_executing"></div>
                    <b>users_executing</b>
                    <a class="ansibleOptionLink" href="#parameter-items/users_executing" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of users executing the statement</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/users_opening"></div>
                    <b>users_opening</b>
                    <a class="ansibleOptionLink" href="#parameter-items/users_opening" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of users that have any of the child cursors open</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-items/version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Version Example: `1`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/version_count"></div>
                    <b>version_count</b>
                    <a class="ansibleOptionLink" href="#parameter-items/version_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of cursors present in the cache with this SQL text and plan</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/wt_harmonic_sum"></div>
                    <b>wt_harmonic_sum</b>
                    <a class="ansibleOptionLink" href="#parameter-items/wt_harmonic_sum" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Weight based harmonic sum of ranking parameters</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-opsi_private_endpoint_id"></div>
                    <b>opsi_private_endpoint_id</b>
                    <a class="ansibleOptionLink" href="#parameter-opsi_private_endpoint_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the OPSI private endpoint</div>
                                            <div>Required for <em>action=change_pe_comanaged</em>.</div>
                                            <div>Required when $p.relatedDiscriminatorFieldName is &#x27;PE_COMANAGED_DATABASE&#x27;</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-service_name"></div>
                    <b>service_name</b>
                    <a class="ansibleOptionLink" href="#parameter-service_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Database service name used for connection requests.</div>
                                            <div>Required for <em>action=change_pe_comanaged</em>.</div>
                                            <div>Required when $p.relatedDiscriminatorFieldName is &#x27;PE_COMANAGED_DATABASE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-system_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;orcl-cloud&quot;: {&quot;free-tier-retained&quot;: &quot;true&quot;}}`</div>
                                            <div>Applicable only for <em>action=enable</em>.</div>
                                            <div>Applicable when entity_source is &#x27;PE_COMANAGED_DATABASE&#x27;</div>
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

    
    - name: Perform action change on database_insights
      oci_opsi_database_insights_actions:
        # required
        database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        action: change

    - name: Perform action change_pe_comanaged on database_insights
      oci_opsi_database_insights_actions:
        # required
        opsi_private_endpoint_id: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        service_name: service_name_example
        credential_details:
          # required
          credential_source_name: credential_source_name_example
          credential_type: CREDENTIALS_BY_SOURCE
        database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
        action: change_pe_comanaged

    - name: Perform action disable on database_insights
      oci_opsi_database_insights_actions:
        # required
        database_insight_id: "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx"
        action: disable

    - name: Perform action enable on database_insights with entity_source = EM_MANAGED_EXTERNAL_DATABASE
      oci_opsi_database_insights_actions:
        # required
        entity_source: EM_MANAGED_EXTERNAL_DATABASE

    - name: Perform action enable on database_insights with entity_source = PE_COMANAGED_DATABASE
      oci_opsi_database_insights_actions:
        # required
        entity_source: PE_COMANAGED_DATABASE
        opsi_private_endpoint_id: "ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        service_name: service_name_example
        credential_details:
          # required
          credential_source_name: credential_source_name_example
          credential_type: CREDENTIALS_BY_SOURCE
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        system_tags: null

    - name: Perform action ingest_database_configuration on database_insights
      oci_opsi_database_insights_actions:
        # required
        items:
        - # required
          host_name: host_name_example
          metric_name: DB_OS_CONFIG_INSTANCE
          instance_name: instance_name_example

          # optional
          num_cp_us: 56
          num_cpu_cores: 56
          num_cpu_sockets: 56
          physical_memory_bytes: 3.4
          time_collected: time_collected_example
        action: ingest_database_configuration

        # optional
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Perform action ingest_sql_bucket on database_insights
      oci_opsi_database_insights_actions:
        # required
        action: ingest_sql_bucket

        # optional
        items:
        - # required
          host_name: host_name_example
          metric_name: DB_OS_CONFIG_INSTANCE
          instance_name: instance_name_example

          # optional
          num_cp_us: 56
          num_cpu_cores: 56
          num_cpu_sockets: 56
          physical_memory_bytes: 3.4
          time_collected: time_collected_example
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Perform action ingest_sql_plan_lines on database_insights
      oci_opsi_database_insights_actions:
        # required
        action: ingest_sql_plan_lines

        # optional
        items:
        - # required
          host_name: host_name_example
          metric_name: DB_OS_CONFIG_INSTANCE
          instance_name: instance_name_example

          # optional
          num_cp_us: 56
          num_cpu_cores: 56
          num_cpu_sockets: 56
          physical_memory_bytes: 3.4
          time_collected: time_collected_example
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Perform action ingest_sql_stats on database_insights
      oci_opsi_database_insights_actions:
        # required
        action: ingest_sql_stats

        # optional
        items:
        - # required
          host_name: host_name_example
          metric_name: DB_OS_CONFIG_INSTANCE
          instance_name: instance_name_example

          # optional
          num_cp_us: 56
          num_cpu_cores: 56
          num_cpu_sockets: 56
          physical_memory_bytes: 3.4
          time_collected: time_collected_example
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Perform action ingest_sql_text on database_insights
      oci_opsi_database_insights_actions:
        # required
        action: ingest_sql_text

        # optional
        items:
        - # required
          host_name: host_name_example
          metric_name: DB_OS_CONFIG_INSTANCE
          instance_name: instance_name_example

          # optional
          num_cp_us: 56
          num_cpu_cores: 56
          num_cpu_sockets: 56
          physical_memory_bytes: 3.4
          time_collected: time_collected_example
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-database_insights"></div>
                    <b>database_insights</b>
                    <a class="ansibleOptionLink" href="#return-database_insights" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the DatabaseInsights resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;connection_credential_details&#x27;: {&#x27;credential_source_name&#x27;: &#x27;credential_source_name_example&#x27;, &#x27;credential_type&#x27;: &#x27;CREDENTIALS_BY_SOURCE&#x27;, &#x27;password_secret_id&#x27;: &#x27;ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;role&#x27;: &#x27;NORMAL&#x27;, &#x27;user_name&#x27;: &#x27;user_name_example&#x27;}, &#x27;connection_details&#x27;: {&#x27;host_name&#x27;: &#x27;host_name_example&#x27;, &#x27;hosts&#x27;: [{&#x27;host_ip&#x27;: &#x27;host_ip_example&#x27;, &#x27;port&#x27;: 56}], &#x27;port&#x27;: 56, &#x27;protocol&#x27;: &#x27;TCP&#x27;, &#x27;service_name&#x27;: &#x27;service_name_example&#x27;}, &#x27;connector_id&#x27;: &#x27;ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;credential_details&#x27;: {&#x27;credential_source_name&#x27;: &#x27;credential_source_name_example&#x27;, &#x27;credential_type&#x27;: &#x27;CREDENTIALS_BY_SOURCE&#x27;, &#x27;password_secret_id&#x27;: &#x27;ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;role&#x27;: &#x27;NORMAL&#x27;, &#x27;user_name&#x27;: &#x27;user_name_example&#x27;}, &#x27;database_connection_status_details&#x27;: &#x27;database_connection_status_details_example&#x27;, &#x27;database_display_name&#x27;: &#x27;database_display_name_example&#x27;, &#x27;database_id&#x27;: &#x27;ocid1.database.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;database_name&#x27;: &#x27;database_name_example&#x27;, &#x27;database_resource_type&#x27;: &#x27;database_resource_type_example&#x27;, &#x27;database_type&#x27;: &#x27;database_type_example&#x27;, &#x27;database_version&#x27;: &#x27;database_version_example&#x27;, &#x27;db_additional_details&#x27;: {}, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;enterprise_manager_bridge_id&#x27;: &#x27;ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;enterprise_manager_entity_display_name&#x27;: &#x27;enterprise_manager_entity_display_name_example&#x27;, &#x27;enterprise_manager_entity_identifier&#x27;: &#x27;enterprise_manager_entity_identifier_example&#x27;, &#x27;enterprise_manager_entity_name&#x27;: &#x27;enterprise_manager_entity_name_example&#x27;, &#x27;enterprise_manager_entity_type&#x27;: &#x27;enterprise_manager_entity_type_example&#x27;, &#x27;enterprise_manager_identifier&#x27;: &#x27;enterprise_manager_identifier_example&#x27;, &#x27;entity_source&#x27;: &#x27;AUTONOMOUS_DATABASE&#x27;, &#x27;exadata_insight_id&#x27;: &#x27;ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;management_agent_id&#x27;: &#x27;ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;opsi_private_endpoint_id&#x27;: &#x27;ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;processor_count&#x27;: 56, &#x27;status&#x27;: &#x27;DISABLED&#x27;, &#x27;system_tags&#x27;: {}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Compartment identifier of the database</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_credential_details"></div>
                    <b>connection_credential_details</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_credential_details" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_credential_details/credential_source_name"></div>
                    <b>credential_source_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_credential_details/credential_source_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">credential_source_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_credential_details/credential_type"></div>
                    <b>credential_type</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_credential_details/credential_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Credential type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREDENTIALS_BY_SOURCE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_credential_details/password_secret_id"></div>
                    <b>password_secret_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_credential_details/password_secret_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The secret <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> mapping to the database credentials.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_credential_details/role"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_credential_details/role" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>database user role.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NORMAL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_credential_details/user_name"></div>
                    <b>user_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_credential_details/user_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>database user name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">user_name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_details"></div>
                    <b>connection_details</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_details" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_details/host_name"></div>
                    <b>host_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_details/host_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the listener host that will be used to create the connect string to the database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">host_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_details/hosts"></div>
                    <b>hosts</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_details/hosts" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of hosts and port for private endpoint accessed database resource.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_details/hosts/host_ip"></div>
                    <b>host_ip</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_details/hosts/host_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Host IP used for connection requests for Cloud DB resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">host_ip_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_details/hosts/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_details/hosts/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Listener port number used for connection requests for rivate endpoint accessed db resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_details/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_details/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Listener port number used for connection requests.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_details/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_details/protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Protocol used for connection requests.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">TCP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connection_details/service_name"></div>
                    <b>service_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connection_details/service_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Database service name used for connection requests.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">service_name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/connector_id"></div>
                    <b>connector_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/connector_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of External Database Connector</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.connector.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/credential_details"></div>
                    <b>credential_details</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/credential_details" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/credential_details/credential_source_name"></div>
                    <b>credential_source_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/credential_details/credential_source_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">credential_source_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/credential_details/credential_type"></div>
                    <b>credential_type</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/credential_details/credential_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Credential type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREDENTIALS_BY_SOURCE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/credential_details/password_secret_id"></div>
                    <b>password_secret_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/credential_details/password_secret_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The secret <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> mapping to the database credentials.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/credential_details/role"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/credential_details/role" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>database user role.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NORMAL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-database_insights/credential_details/user_name"></div>
                    <b>user_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/credential_details/user_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>database user name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">user_name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/database_connection_status_details"></div>
                    <b>database_connection_status_details</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/database_connection_status_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A message describing the status of the database connection of this resource. For example, it can be used to provide actionable information about the permission and content validity of the database connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">database_connection_status_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/database_display_name"></div>
                    <b>database_display_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/database_display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Display name of database</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">database_display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/database_id"></div>
                    <b>database_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/database_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.database.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/database_name"></div>
                    <b>database_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/database_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of database</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">database_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/database_resource_type"></div>
                    <b>database_resource_type</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/database_resource_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>OCI database resource type</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">database_resource_type_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/database_type"></div>
                    <b>database_type</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/database_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Operations Insights internal representation of the database type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">database_type_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/database_version"></div>
                    <b>database_version</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/database_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The version of the database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">database_version_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/db_additional_details"></div>
                    <b>db_additional_details</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/db_additional_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Additional details of a database in JSON format. For autonomous databases, this is the AutonomousDatabase object serialized as a JSON string as defined in https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/. For EM, pass in null or an empty string. Note that this string needs to be escaped when specified in the curl command.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/enterprise_manager_bridge_id"></div>
                    <b>enterprise_manager_bridge_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/enterprise_manager_bridge_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>OPSI Enterprise Manager Bridge OCID</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/enterprise_manager_entity_display_name"></div>
                    <b>enterprise_manager_entity_display_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/enterprise_manager_entity_display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enterprise Manager Entity Display Name</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">enterprise_manager_entity_display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/enterprise_manager_entity_identifier"></div>
                    <b>enterprise_manager_entity_identifier</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/enterprise_manager_entity_identifier" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enterprise Manager Entity Unique Identifier</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">enterprise_manager_entity_identifier_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/enterprise_manager_entity_name"></div>
                    <b>enterprise_manager_entity_name</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/enterprise_manager_entity_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enterprise Manager Entity Name</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">enterprise_manager_entity_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/enterprise_manager_entity_type"></div>
                    <b>enterprise_manager_entity_type</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/enterprise_manager_entity_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enterprise Manager Entity Type</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">enterprise_manager_entity_type_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/enterprise_manager_identifier"></div>
                    <b>enterprise_manager_identifier</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/enterprise_manager_identifier" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enterprise Manager Unique Identifier</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">enterprise_manager_identifier_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/entity_source"></div>
                    <b>entity_source</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/entity_source" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Source of the database entity.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">AUTONOMOUS_DATABASE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/exadata_insight_id"></div>
                    <b>exadata_insight_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/exadata_insight_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the Exadata insight.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Database insight identifier</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/management_agent_id"></div>
                    <b>management_agent_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/management_agent_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the Management Agent</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/opsi_private_endpoint_id"></div>
                    <b>opsi_private_endpoint_id</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/opsi_private_endpoint_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the OPSI private endpoint</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.opsiprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/processor_count"></div>
                    <b>processor_count</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/processor_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates the status of a database insight in Operations Insights</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">DISABLED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;orcl-cloud&quot;: {&quot;free-tier-retained&quot;: &quot;true&quot;}}`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the the database insight was first enabled. An RFC3339 formatted datetime string</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-database_insights/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-database_insights/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the database insight was updated. An RFC3339 formatted datetime string</div>
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

