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

.. _ansible_collections.oracle.oci.oci_database_autonomous_database_clones_facts_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_database_autonomous_database_clones_facts -- Fetches details about one or multiple AutonomousDatabaseClones resources in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.34.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_database_autonomous_database_clones_facts`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Fetches details about one or multiple AutonomousDatabaseClones resources in Oracle Cloud Infrastructure
- Lists the Autonomous Database clones for the specified Autonomous Database.


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
                    <div class="ansibleOptionAnchor" id="parameter-autonomous_database_id"></div>
                    <b>autonomous_database_id</b>
                    <a class="ansibleOptionLink" href="#parameter-autonomous_database_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The database <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-clone_type"></div>
                    <b>clone_type</b>
                    <a class="ansibleOptionLink" href="#parameter-clone_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>REFRESHABLE_CLONE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>A filter to return only resources that match the given clone type exactly.</div>
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
                                            <div>The compartment <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A filter to return only resources that match the entire display name given. The match is not case sensitive.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#parameter-lifecycle_state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PROVISIONING</li>
                                                                                                                                                                                                <li>AVAILABLE</li>
                                                                                                                                                                                                <li>STOPPING</li>
                                                                                                                                                                                                <li>STOPPED</li>
                                                                                                                                                                                                <li>STARTING</li>
                                                                                                                                                                                                <li>TERMINATING</li>
                                                                                                                                                                                                <li>TERMINATED</li>
                                                                                                                                                                                                <li>UNAVAILABLE</li>
                                                                                                                                                                                                <li>RESTORE_IN_PROGRESS</li>
                                                                                                                                                                                                <li>RESTORE_FAILED</li>
                                                                                                                                                                                                <li>BACKUP_IN_PROGRESS</li>
                                                                                                                                                                                                <li>SCALE_IN_PROGRESS</li>
                                                                                                                                                                                                <li>AVAILABLE_NEEDS_ATTENTION</li>
                                                                                                                                                                                                <li>UPDATING</li>
                                                                                                                                                                                                <li>MAINTENANCE_IN_PROGRESS</li>
                                                                                                                                                                                                <li>RESTARTING</li>
                                                                                                                                                                                                <li>RECREATING</li>
                                                                                                                                                                                                <li>ROLE_CHANGE_IN_PROGRESS</li>
                                                                                                                                                                                                <li>UPGRADING</li>
                                                                                                                                                                                                <li>INACCESSIBLE</li>
                                                                                                                                                                                                <li>STANDBY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>A filter to return only resources that match the given lifecycle state exactly.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-sort_by"></div>
                    <b>sort_by</b>
                    <a class="ansibleOptionLink" href="#parameter-sort_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NONE</li>
                                                                                                                                                                                                <li>TIMECREATED</li>
                                                                                                                                                                                                <li>DISPLAYNAME</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.</div>
                                            <div>**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sort_order"></div>
                    <b>sort_order</b>
                    <a class="ansibleOptionLink" href="#parameter-sort_order" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ASC</li>
                                                                                                                                                                                                <li>DESC</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The sort order to use, either ascending (`ASC`) or descending (`DESC`).</div>
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

    
    - name: List autonomous_database_clones
      oci_database_autonomous_database_clones_facts:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        sort_order: ASC
        display_name: display_name_example
        lifecycle_state: PROVISIONING
        sort_by: NONE
        clone_type: REFRESHABLE_CLONE





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
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones"></div>
                    <b>autonomous_database_clones</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of AutonomousDatabaseClones resources</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;actual_used_data_storage_size_in_tbs&#x27;: 1.2, &#x27;allocated_storage_size_in_tbs&#x27;: 1.2, &#x27;apex_details&#x27;: {&#x27;apex_version&#x27;: &#x27;apex_version_example&#x27;, &#x27;ords_version&#x27;: &#x27;ords_version_example&#x27;}, &#x27;are_primary_whitelisted_ips_used&#x27;: True, &#x27;autonomous_container_database_id&#x27;: &#x27;ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;autonomous_maintenance_schedule_type&#x27;: &#x27;EARLY&#x27;, &#x27;available_upgrade_versions&#x27;: [], &#x27;backup_config&#x27;: {&#x27;manual_backup_bucket_name&#x27;: &#x27;manual_backup_bucket_name_example&#x27;, &#x27;manual_backup_type&#x27;: &#x27;NONE&#x27;}, &#x27;backup_retention_period_in_days&#x27;: 56, &#x27;character_set&#x27;: &#x27;character_set_example&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compute_count&#x27;: 3.4, &#x27;compute_model&#x27;: &#x27;ECPU&#x27;, &#x27;connection_strings&#x27;: {&#x27;all_connection_strings&#x27;: {}, &#x27;dedicated&#x27;: &#x27;dedicated_example&#x27;, &#x27;high&#x27;: &#x27;high_example&#x27;, &#x27;low&#x27;: &#x27;low_example&#x27;, &#x27;medium&#x27;: &#x27;medium_example&#x27;, &#x27;profiles&#x27;: [{&#x27;consumer_group&#x27;: &#x27;HIGH&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;host_format&#x27;: &#x27;FQDN&#x27;, &#x27;protocol&#x27;: &#x27;TCP&#x27;, &#x27;session_mode&#x27;: &#x27;DIRECT&#x27;, &#x27;syntax_format&#x27;: &#x27;LONG&#x27;, &#x27;tls_authentication&#x27;: &#x27;SERVER&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}]}, &#x27;connection_urls&#x27;: {&#x27;apex_url&#x27;: &#x27;apex_url_example&#x27;, &#x27;database_transforms_url&#x27;: &#x27;database_transforms_url_example&#x27;, &#x27;graph_studio_url&#x27;: &#x27;graph_studio_url_example&#x27;, &#x27;machine_learning_notebook_url&#x27;: &#x27;machine_learning_notebook_url_example&#x27;, &#x27;machine_learning_user_management_url&#x27;: &#x27;machine_learning_user_management_url_example&#x27;, &#x27;mongo_db_url&#x27;: &#x27;mongo_db_url_example&#x27;, &#x27;ords_url&#x27;: &#x27;ords_url_example&#x27;, &#x27;sql_dev_web_url&#x27;: &#x27;sql_dev_web_url_example&#x27;}, &#x27;cpu_core_count&#x27;: 56, &#x27;customer_contacts&#x27;: [{&#x27;email&#x27;: &#x27;email_example&#x27;}], &#x27;data_safe_status&#x27;: &#x27;REGISTERING&#x27;, &#x27;data_storage_size_in_gbs&#x27;: 56, &#x27;data_storage_size_in_tbs&#x27;: 56, &#x27;database_edition&#x27;: &#x27;STANDARD_EDITION&#x27;, &#x27;database_management_status&#x27;: &#x27;ENABLING&#x27;, &#x27;dataguard_region_type&#x27;: &#x27;PRIMARY_DG_REGION&#x27;, &#x27;db_name&#x27;: &#x27;db_name_example&#x27;, &#x27;db_tools_details&#x27;: [{&#x27;compute_count&#x27;: 3.4, &#x27;is_enabled&#x27;: True, &#x27;max_idle_time_in_minutes&#x27;: 56, &#x27;name&#x27;: &#x27;APEX&#x27;}], &#x27;db_version&#x27;: &#x27;db_version_example&#x27;, &#x27;db_workload&#x27;: &#x27;OLTP&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;disaster_recovery_region_type&#x27;: &#x27;PRIMARY&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;failed_data_recovery_in_seconds&#x27;: 56, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;infrastructure_type&#x27;: &#x27;CLOUD&#x27;, &#x27;is_access_control_enabled&#x27;: True, &#x27;is_auto_scaling_enabled&#x27;: True, &#x27;is_auto_scaling_for_storage_enabled&#x27;: True, &#x27;is_data_guard_enabled&#x27;: True, &#x27;is_dedicated&#x27;: True, &#x27;is_free_tier&#x27;: True, &#x27;is_local_data_guard_enabled&#x27;: True, &#x27;is_mtls_connection_required&#x27;: True, &#x27;is_preview&#x27;: True, &#x27;is_reconnect_clone_enabled&#x27;: True, &#x27;is_refreshable_clone&#x27;: True, &#x27;is_remote_data_guard_enabled&#x27;: True, &#x27;key_history_entry&#x27;: [{&#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;kms_key_version_id&#x27;: &#x27;ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;time_activated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;vault_id&#x27;: &#x27;ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx&#x27;}], &#x27;key_store_id&#x27;: &#x27;ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;key_store_wallet_name&#x27;: &#x27;key_store_wallet_name_example&#x27;, &#x27;kms_key_id&#x27;: &#x27;ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;kms_key_lifecycle_details&#x27;: &#x27;kms_key_lifecycle_details_example&#x27;, &#x27;kms_key_version_id&#x27;: &#x27;ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;license_model&#x27;: &#x27;LICENSE_INCLUDED&#x27;, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;PROVISIONING&#x27;, &#x27;local_adg_auto_failover_max_data_loss_limit&#x27;: 56, &#x27;local_disaster_recovery_type&#x27;: &#x27;local_disaster_recovery_type_example&#x27;, &#x27;local_standby_db&#x27;: {&#x27;lag_time_in_seconds&#x27;: 56, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;PROVISIONING&#x27;, &#x27;time_data_guard_role_changed&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_disaster_recovery_role_changed&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}, &#x27;long_term_backup_schedule&#x27;: {&#x27;is_disabled&#x27;: True, &#x27;repeat_cadence&#x27;: &#x27;ONE_TIME&#x27;, &#x27;retention_period_in_days&#x27;: 56, &#x27;time_of_backup&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}, &#x27;max_cpu_core_count&#x27;: 56, &#x27;memory_per_oracle_compute_unit_in_gbs&#x27;: 56, &#x27;ncharacter_set&#x27;: &#x27;ncharacter_set_example&#x27;, &#x27;next_long_term_backup_time_stamp&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;nsg_ids&#x27;: [], &#x27;ocpu_count&#x27;: 3.4, &#x27;open_mode&#x27;: &#x27;READ_ONLY&#x27;, &#x27;operations_insights_status&#x27;: &#x27;ENABLING&#x27;, &#x27;peer_db_ids&#x27;: [], &#x27;permission_level&#x27;: &#x27;RESTRICTED&#x27;, &#x27;private_endpoint&#x27;: &#x27;private_endpoint_example&#x27;, &#x27;private_endpoint_ip&#x27;: &#x27;private_endpoint_ip_example&#x27;, &#x27;private_endpoint_label&#x27;: &#x27;private_endpoint_label_example&#x27;, &#x27;provisionable_cpus&#x27;: [], &#x27;refreshable_mode&#x27;: &#x27;AUTOMATIC&#x27;, &#x27;refreshable_status&#x27;: &#x27;REFRESHING&#x27;, &#x27;remote_disaster_recovery_configuration&#x27;: {&#x27;disaster_recovery_type&#x27;: &#x27;ADG&#x27;, &#x27;is_snapshot_standby&#x27;: True, &#x27;time_snapshot_standby_enabled_till&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}, &#x27;role&#x27;: &#x27;PRIMARY&#x27;, &#x27;scheduled_operations&#x27;: [{&#x27;day_of_week&#x27;: {&#x27;name&#x27;: &#x27;MONDAY&#x27;}, &#x27;scheduled_start_time&#x27;: &#x27;scheduled_start_time_example&#x27;, &#x27;scheduled_stop_time&#x27;: &#x27;scheduled_stop_time_example&#x27;}], &#x27;service_console_url&#x27;: &#x27;service_console_url_example&#x27;, &#x27;source_id&#x27;: &#x27;ocid1.source.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;standby_db&#x27;: {&#x27;lag_time_in_seconds&#x27;: 56, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;PROVISIONING&#x27;, &#x27;time_data_guard_role_changed&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_disaster_recovery_role_changed&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}, &#x27;standby_whitelisted_ips&#x27;: [], &#x27;subnet_id&#x27;: &#x27;ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;supported_regions_to_clone_to&#x27;: [], &#x27;system_tags&#x27;: {}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_data_guard_role_changed&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_deletion_of_free_autonomous_database&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_disaster_recovery_role_changed&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_local_data_guard_enabled&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_maintenance_begin&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_maintenance_end&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_of_last_failover&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_of_last_refresh&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_of_last_refresh_point&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_of_last_switchover&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_of_next_refresh&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_reclamation_of_free_autonomous_database&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_until_reconnect_clone_enabled&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;total_backup_storage_size_in_gbs&#x27;: 1.2, &#x27;used_data_storage_size_in_gbs&#x27;: 56, &#x27;used_data_storage_size_in_tbs&#x27;: 56, &#x27;vault_id&#x27;: &#x27;ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;whitelisted_ips&#x27;: []}]</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/actual_used_data_storage_size_in_tbs"></div>
                    <b>actual_used_data_storage_size_in_tbs</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/actual_used_data_storage_size_in_tbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current amount of storage in use for user and system data, in terabytes (TB).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">1.2</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/allocated_storage_size_in_tbs"></div>
                    <b>allocated_storage_size_in_tbs</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/allocated_storage_size_in_tbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The amount of storage currently allocated for the database tables and billed for, rounded up. When auto-scaling is not enabled, this value is equal to the `dataStorageSizeInTBs` value. You can compare this value to the `actualUsedDataStorageSizeInTBs` value to determine if a manual shrink operation is appropriate for your allocated storage.</div>
                                            <div>**Note:** Auto-scaling does not automatically decrease allocated storage when data is deleted from the database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">1.2</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/apex_details"></div>
                    <b>apex_details</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/apex_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Information about Oracle APEX Application Development.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/apex_details/apex_version"></div>
                    <b>apex_version</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/apex_details/apex_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Oracle APEX Application Development version.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">apex_version_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/apex_details/ords_version"></div>
                    <b>ords_version</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/apex_details/ords_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Oracle REST Data Services (ORDS) version.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ords_version_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/are_primary_whitelisted_ips_used"></div>
                    <b>are_primary_whitelisted_ips_used</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/are_primary_whitelisted_ips_used" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled. It&#x27;s value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby. It&#x27;s value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/autonomous_container_database_id"></div>
                    <b>autonomous_container_database_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/autonomous_container_database_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Autonomous Container Database <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/autonomous_maintenance_schedule_type"></div>
                    <b>autonomous_maintenance_schedule_type</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/autonomous_maintenance_schedule_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">EARLY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/available_upgrade_versions"></div>
                    <b>available_upgrade_versions</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/available_upgrade_versions" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/backup_config"></div>
                    <b>backup_config</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/backup_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/backup_config/manual_backup_bucket_name"></div>
                    <b>manual_backup_bucket_name</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/backup_config/manual_backup_bucket_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of <a href='https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm'>Object Storage</a> bucket to use for storing manual backups.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">manual_backup_bucket_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/backup_config/manual_backup_type"></div>
                    <b>manual_backup_type</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/backup_config/manual_backup_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The manual backup destination type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NONE</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/backup_retention_period_in_days"></div>
                    <b>backup_retention_period_in_days</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/backup_retention_period_in_days" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Retention period, in days, for long-term backups</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/character_set"></div>
                    <b>character_set</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/character_set" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The character set for the autonomous database.  The default is AL32UTF8. Allowed values are:</div>
                                            <div>AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">character_set_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/compute_count"></div>
                    <b>compute_count</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/compute_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The compute amount available to the database. Minimum and maximum values depend on the compute model and whether the database is on Shared or Dedicated infrastructure. For an Autonomous Database on Shared infrastructure, the &#x27;ECPU&#x27; compute model requires values in multiples of two. Required when using the `computeModel` parameter. When using `cpuCoreCount` parameter, it is an error to specify computeCount to a non-null value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/compute_model"></div>
                    <b>compute_model</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/compute_model" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The compute model of the Autonomous Database. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an error to specify `computeModel` to a non-null value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ECPU</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings"></div>
                    <b>connection_strings</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Database for the password value.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/all_connection_strings"></div>
                    <b>all_connection_strings</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/all_connection_strings" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Returns all connection strings that can be used to connect to the Autonomous Database. For more information, please see <a href='https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connect-predefined.html#GUID-9747539B-FD46-44F1-8FF8-F5AC650F15BE'>Predefined Database Service Names for Autonomous Transaction Processing</a></div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/dedicated"></div>
                    <b>dedicated</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/dedicated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">dedicated_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/high"></div>
                    <b>high</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/high" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but supports the fewest number of concurrent SQL statements.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">high_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/low"></div>
                    <b>low</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/low" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">low_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/medium"></div>
                    <b>medium</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/medium" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of performance, but supports more concurrent SQL statements.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">medium_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles"></div>
                    <b>profiles</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of connection string profiles to allow clients to group, filter and select connection string values based on structured metadata.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles/consumer_group"></div>
                    <b>consumer_group</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles/consumer_group" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Consumer group used by the connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">HIGH</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name for the connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles/host_format"></div>
                    <b>host_format</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles/host_format" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Host format used in connection string.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FQDN</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles/protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Protocol used by the connection.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">TCP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles/session_mode"></div>
                    <b>session_mode</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles/session_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies whether the listener performs a direct hand-off of the session, or redirects the session. In RAC deployments where SCAN is used, sessions are redirected to a Node VIP. Use `DIRECT` for direct hand-offs. Use `REDIRECT` to redirect the session.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">DIRECT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles/syntax_format"></div>
                    <b>syntax_format</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles/syntax_format" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies whether the connection string is using the long (`LONG`), Easy Connect (`EZCONNECT`), or Easy Connect Plus (`EZCONNECTPLUS`) format. Autonomous Databases on shared Exadata infrastructure always use the long format.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">LONG</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles/tls_authentication"></div>
                    <b>tls_authentication</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles/tls_authentication" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies whether the TLS handshake is using one-way (`SERVER`) or mutual (`MUTUAL`) authentication.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SERVER</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_strings/profiles/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_strings/profiles/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Connection string value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls"></div>
                    <b>connection_urls</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls/apex_url"></div>
                    <b>apex_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls/apex_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Oracle Application Express (APEX) URL.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">apex_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls/database_transforms_url"></div>
                    <b>database_transforms_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls/database_transforms_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL of the Database Transforms for the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">database_transforms_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls/graph_studio_url"></div>
                    <b>graph_studio_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls/graph_studio_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL of the Graph Studio for the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">graph_studio_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls/machine_learning_notebook_url"></div>
                    <b>machine_learning_notebook_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls/machine_learning_notebook_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL of the Oracle Machine Learning (OML) Notebook for the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">machine_learning_notebook_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls/machine_learning_user_management_url"></div>
                    <b>machine_learning_user_management_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls/machine_learning_user_management_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Oracle Machine Learning user management URL.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">machine_learning_user_management_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls/mongo_db_url"></div>
                    <b>mongo_db_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls/mongo_db_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL of the MongoDB API for the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">mongo_db_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls/ords_url"></div>
                    <b>ords_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls/ords_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Oracle REST Data Services (ORDS) URL of the Web Access for the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ords_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/connection_urls/sql_dev_web_url"></div>
                    <b>sql_dev_web_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/connection_urls/sql_dev_web_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Oracle SQL Developer Web URL.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">sql_dev_web_url_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/cpu_core_count"></div>
                    <b>cpu_core_count</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/cpu_core_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of OCPU cores to be made available to the database. When the ECPU is selected, the value for cpuCoreCount is 0. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See <a href='https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&amp;id=ATPFG- GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1'>Characteristics of Infrastructure Shapes</a> for shape details.</div>
                                            <div>**Note:** This parameter cannot be used with the `ocpuCount` parameter.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/customer_contacts"></div>
                    <b>customer_contacts</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/customer_contacts" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Customer Contacts.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/customer_contacts/email"></div>
                    <b>email</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/customer_contacts/email" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The email address used by Oracle to send notifications regarding databases and infrastructure.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">email_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/data_safe_status"></div>
                    <b>data_safe_status</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/data_safe_status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Status of the Data Safe registration for this Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">REGISTERING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/data_storage_size_in_gbs"></div>
                    <b>data_storage_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/data_storage_size_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The quantity of data in the database, in gigabytes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/data_storage_size_in_tbs"></div>
                    <b>data_storage_size_in_tbs</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/data_storage_size_in_tbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The quantity of data in the database, in terabytes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/database_edition"></div>
                    <b>database_edition</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/database_edition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Oracle Database Edition that applies to the Autonomous databases.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">STANDARD_EDITION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/database_management_status"></div>
                    <b>database_management_status</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/database_management_status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Status of Database Management for this Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ENABLING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/dataguard_region_type"></div>
                    <b>dataguard_region_type</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/dataguard_region_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Autonomous Data Guard region type of the Autonomous Database. For Autonomous Databases on shared Exadata infrastructure, Data Guard associations have designated primary and standby regions, and these region types do not change when the database changes roles. The standby regions in Data Guard associations can be the same region designated as the primary region, or they can be remote regions. Certain database administrative operations may be available only in the primary region of the Data Guard association, and cannot be performed when the database using the &quot;primary&quot; role is operating in a remote Data Guard standby region.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PRIMARY_DG_REGION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/db_name"></div>
                    <b>db_name</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/db_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The database name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">db_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/db_tools_details"></div>
                    <b>db_tools_details</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/db_tools_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of database tools details.</div>
                                            <div>This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, isLocalDataGuardEnabled, or isFreeTier.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/db_tools_details/compute_count"></div>
                    <b>compute_count</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/db_tools_details/compute_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Compute used by database tools.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/db_tools_details/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/db_tools_details/is_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether tool is enabled.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/db_tools_details/max_idle_time_in_minutes"></div>
                    <b>max_idle_time_in_minutes</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/db_tools_details/max_idle_time_in_minutes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The max idle time, in minutes, after which the VM used by database tools will be terminated.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/db_tools_details/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/db_tools_details/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of database tool.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">APEX</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/db_version"></div>
                    <b>db_version</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/db_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A valid Oracle Database version for Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">db_version_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/db_workload"></div>
                    <b>db_workload</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/db_workload" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Autonomous Database workload type. The following values are valid:</div>
                                            <div>- OLTP - indicates an Autonomous Transaction Processing database - DW - indicates an Autonomous Data Warehouse database - AJD - indicates an Autonomous JSON Database - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.</div>
                                            <div>This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">OLTP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/disaster_recovery_region_type"></div>
                    <b>disaster_recovery_region_type</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/disaster_recovery_region_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The disaster recovery (DR) region type of the Autonomous Database. For Shared Autonomous Databases, DR associations have designated primary and standby regions. These region types do not change when the database changes roles. The standby region in DR associations can be the same region as the primary region, or they can be in a remote regions. Some database administration operations may be available only in the primary region of the DR association, and cannot be performed when the database using the primary role is operating in a remote region.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PRIMARY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The user-friendly name for the Autonomous Database. The name does not have to be unique.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/failed_data_recovery_in_seconds"></div>
                    <b>failed_data_recovery_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/failed_data_recovery_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates the number of seconds of data loss for a Data Guard failover.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/freeform_tags" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/infrastructure_type"></div>
                    <b>infrastructure_type</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/infrastructure_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The infrastructure type this resource belongs to.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CLOUD</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_access_control_enabled"></div>
                    <b>is_access_control_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_access_control_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional, if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.</div>
                                            <div>This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_auto_scaling_enabled"></div>
                    <b>is_auto_scaling_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_auto_scaling_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if auto scaling is enabled for the Autonomous Database CPU core count.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_auto_scaling_for_storage_enabled"></div>
                    <b>is_auto_scaling_for_storage_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_auto_scaling_for_storage_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_data_guard_enabled"></div>
                    <b>is_data_guard_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_data_guard_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>**Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_dedicated"></div>
                    <b>is_dedicated</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_dedicated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>True if the database uses <a href='https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html'>dedicated Exadata infrastructure</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_free_tier"></div>
                    <b>is_free_tier</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_free_tier" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.</div>
                                            <div>This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isLocalDataGuardEnabled</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_local_data_guard_enabled"></div>
                    <b>is_local_data_guard_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_local_data_guard_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_mtls_connection_required"></div>
                    <b>is_mtls_connection_required</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_mtls_connection_required" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies if the Autonomous Database requires mTLS connections.</div>
                                            <div>This may not be updated in parallel with any of the following: licenseModel, databaseEdition, cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, whitelistedIps, openMode, permissionLevel, db-workload, privateEndpointLabel, nsgIds, customerContacts, dbVersion, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.</div>
                                            <div>Service Change: The default value of the isMTLSConnectionRequired attribute will change from true to false on July 1, 2023 in the following APIs: - CreateAutonomousDatabase - GetAutonomousDatabase - UpdateAutonomousDatabase Details: Prior to the July 1, 2023 change, the isMTLSConnectionRequired attribute default value was true. This applies to Autonomous Databases on shared Exadata infrastructure. Does this impact me? If you use or maintain custom scripts or Terraform scripts referencing the CreateAutonomousDatabase, GetAutonomousDatabase, or UpdateAutonomousDatabase APIs, you want to check, and possibly modify, the scripts for the changed default value of the attribute. Should you choose not to leave your scripts unchanged, the API calls containing this attribute will continue to work, but the default value will switch from true to false. How do I make this change? Using either OCI SDKs or command line tools, update your custom scripts to explicitly set the isMTLSConnectionRequired attribute to true.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_preview"></div>
                    <b>is_preview</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_preview" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if the Autonomous Database version is a preview version.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_reconnect_clone_enabled"></div>
                    <b>is_reconnect_clone_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_reconnect_clone_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if the refreshable clone can be reconnected to its source database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_refreshable_clone"></div>
                    <b>is_refreshable_clone</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_refreshable_clone" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if the Autonomous Database is a refreshable clone.</div>
                                            <div>This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/is_remote_data_guard_enabled"></div>
                    <b>is_remote_data_guard_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/is_remote_data_guard_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether the Autonomous Database has Cross Region Data Guard enabled. Not applicable to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/key_history_entry"></div>
                    <b>key_history_entry</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/key_history_entry" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Key History Entry.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/key_history_entry/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/key_history_entry/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The id of the Autonomous Database <a href='https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts'>Vault</a> service key management history entry.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/key_history_entry/kms_key_version_id"></div>
                    <b>kms_key_version_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/key_history_entry/kms_key_version_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/key_history_entry/time_activated"></div>
                    <b>time_activated</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/key_history_entry/time_activated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the kms key activated.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/key_history_entry/vault_id"></div>
                    <b>vault_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/key_history_entry/vault_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Oracle Cloud Infrastructure <a href='https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts'>vault</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/key_store_id"></div>
                    <b>key_store_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/key_store_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the key store.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/key_store_wallet_name"></div>
                    <b>key_store_wallet_name</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/key_store_wallet_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The wallet name for Oracle Key Vault.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">key_store_wallet_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/kms_key_id"></div>
                    <b>kms_key_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/kms_key_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/kms_key_lifecycle_details"></div>
                    <b>kms_key_lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/kms_key_lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>KMS key lifecycle details.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">kms_key_lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/kms_key_version_id"></div>
                    <b>kms_key_version_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/kms_key_version_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/license_model"></div>
                    <b>license_model</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/license_model" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on- premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Database service. Note that when provisioning an Autonomous Database on <a href='https://docs.oracle.com/en/cloud/paas/autonomous- database/index.html'>dedicated Exadata infrastructure</a>, this attribute must be null because the attribute is already set at the Autonomous Exadata Infrastructure level. When using <a href='https://docs.oracle.com/en/cloud/paas/autonomous- database/index.html'>shared Exadata infrastructure</a>, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.</div>
                                            <div>This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, maxCpuCoreCount, dataStorageSizeInTBs, adminPassword, isMTLSConnectionRequired, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">LICENSE_INCLUDED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Information about the current lifecycle state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PROVISIONING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/local_adg_auto_failover_max_data_loss_limit"></div>
                    <b>local_adg_auto_failover_max_data_loss_limit</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/local_adg_auto_failover_max_data_loss_limit" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Parameter that allows users to select an acceptable maximum data loss limit in seconds, up to which Automatic Failover will be triggered when necessary for a Local Autonomous Data Guard</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/local_disaster_recovery_type"></div>
                    <b>local_disaster_recovery_type</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/local_disaster_recovery_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates the local disaster recovery (DR) type of the Shared Autonomous Database. Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover. Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">local_disaster_recovery_type_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/local_standby_db"></div>
                    <b>local_standby_db</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/local_standby_db" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/local_standby_db/lag_time_in_seconds"></div>
                    <b>lag_time_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/local_standby_db/lag_time_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine the potential data loss in the event of a failover.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/local_standby_db/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/local_standby_db/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Additional information about the current lifecycle state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/local_standby_db/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/local_standby_db/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PROVISIONING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/local_standby_db/time_data_guard_role_changed"></div>
                    <b>time_data_guard_role_changed</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/local_standby_db/time_data_guard_role_changed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/local_standby_db/time_disaster_recovery_role_changed"></div>
                    <b>time_disaster_recovery_role_changed</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/local_standby_db/time_disaster_recovery_role_changed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Disaster Recovery role was switched for the standby Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/long_term_backup_schedule"></div>
                    <b>long_term_backup_schedule</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/long_term_backup_schedule" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/long_term_backup_schedule/is_disabled"></div>
                    <b>is_disabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/long_term_backup_schedule/is_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if the long-term backup schedule should be deleted. The default value is `FALSE`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/long_term_backup_schedule/repeat_cadence"></div>
                    <b>repeat_cadence</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/long_term_backup_schedule/repeat_cadence" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The frequency of the long-term backup schedule</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ONE_TIME</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/long_term_backup_schedule/retention_period_in_days"></div>
                    <b>retention_period_in_days</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/long_term_backup_schedule/retention_period_in_days" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Retention period, in days, for long-term backups</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/long_term_backup_schedule/time_of_backup"></div>
                    <b>time_of_backup</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/long_term_backup_schedule/time_of_backup" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The timestamp for the long-term backup schedule. For a MONTHLY cadence, months having fewer days than the provided date will have the backup taken on the last day of that month.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/max_cpu_core_count"></div>
                    <b>max_cpu_core_count</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/max_cpu_core_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/memory_per_oracle_compute_unit_in_gbs"></div>
                    <b>memory_per_oracle_compute_unit_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/memory_per_oracle_compute_unit_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The amount of memory (in GBs) enabled per OCPU or ECPU. See <a href='https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbak'>Compute Models in Autonomous Database on Dedicated Exadata Infrastructure</a> for more details.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/ncharacter_set"></div>
                    <b>ncharacter_set</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/ncharacter_set" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The national character set for the autonomous database.  The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ncharacter_set_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/next_long_term_backup_time_stamp"></div>
                    <b>next_long_term_backup_time_stamp</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/next_long_term_backup_time_stamp" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time when the next long-term backup would be created.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/nsg_ids"></div>
                    <b>nsg_ids</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/nsg_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCIDs</a> for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see <a href='https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm'>Security Rules</a>. **NsgIds restrictions:** - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/ocpu_count"></div>
                    <b>ocpu_count</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/ocpu_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of OCPU cores to be made available to the database.</div>
                                            <div>The following points apply: - For Autonomous Databases on dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous Databasese on shared Exadata infrastructure.) - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated Exadata infrastructure.</div>
                                            <div>For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See <a href='https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&amp;id=ATPFG- GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1'>Characteristics of Infrastructure Shapes</a> for shape details.</div>
                                            <div>**Note:** This parameter cannot be used with the `cpuCoreCount` parameter.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/open_mode"></div>
                    <b>open_mode</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/open_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates the Autonomous Database mode. The database can be opened in `READ_ONLY` or `READ_WRITE` mode.</div>
                                            <div>This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">READ_ONLY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/operations_insights_status"></div>
                    <b>operations_insights_status</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/operations_insights_status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Status of Operations Insights for this Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ENABLING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/peer_db_ids"></div>
                    <b>peer_db_ids</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/peer_db_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCIDs</a> of standby databases located in Autonomous Data Guard remote regions that are associated with the source database. Note that for shared Exadata infrastructure, standby databases located in the same region as the source primary database do not have OCIDs.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/permission_level"></div>
                    <b>permission_level</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/permission_level" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Autonomous Database permission level. Restricted mode allows access only by admin users.</div>
                                            <div>This cannot be updated in parallel with any of the following: cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, nsgIds, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">RESTRICTED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/private_endpoint"></div>
                    <b>private_endpoint</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/private_endpoint" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The private endpoint for the resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">private_endpoint_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/private_endpoint_ip"></div>
                    <b>private_endpoint_ip</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/private_endpoint_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The private endpoint Ip address for the resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">private_endpoint_ip_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/private_endpoint_label"></div>
                    <b>private_endpoint_label</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/private_endpoint_label" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The resource&#x27;s private endpoint label. Setting this to an empty string, after the creation of the private endpoint database, changes the private endpoint database to a public endpoint database.</div>
                                            <div>This setting cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, or isFreeTier.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">private_endpoint_label_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/provisionable_cpus"></div>
                    <b>provisionable_cpus</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/provisionable_cpus" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of CPU values that an Autonomous Database can be scaled to.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/refreshable_mode"></div>
                    <b>refreshable_mode</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/refreshable_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">AUTOMATIC</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/refreshable_status"></div>
                    <b>refreshable_status</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/refreshable_status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The refresh status of the clone. REFRESHING indicates that the clone is currently being refreshed with data from the source Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">REFRESHING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/remote_disaster_recovery_configuration"></div>
                    <b>remote_disaster_recovery_configuration</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/remote_disaster_recovery_configuration" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/remote_disaster_recovery_configuration/disaster_recovery_type"></div>
                    <b>disaster_recovery_type</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/remote_disaster_recovery_configuration/disaster_recovery_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates the disaster recovery (DR) type of the Shared Autonomous Database. Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover. Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ADG</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/remote_disaster_recovery_configuration/is_snapshot_standby"></div>
                    <b>is_snapshot_standby</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/remote_disaster_recovery_configuration/is_snapshot_standby" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates if user wants to convert to a snapshot standby. For example, true would set a standby database to snapshot standby database. False would set a snapshot standby database back to regular standby database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/remote_disaster_recovery_configuration/time_snapshot_standby_enabled_till"></div>
                    <b>time_snapshot_standby_enabled_till</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/remote_disaster_recovery_configuration/time_snapshot_standby_enabled_till" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Time and date stored as an RFC 3339 formatted timestamp string. For example, 2022-01-01T12:00:00.000Z would set a limit for the snapshot standby to be converted back to a cross-region standby database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/role"></div>
                    <b>role</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/role" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PRIMARY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/scheduled_operations"></div>
                    <b>scheduled_operations</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/scheduled_operations" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of scheduled operations.</div>
                                            <div>This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, dbVersion, isRefreshable, dbName, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/scheduled_operations/day_of_week"></div>
                    <b>day_of_week</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/scheduled_operations/day_of_week" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/scheduled_operations/day_of_week/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/scheduled_operations/day_of_week/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the day of the week.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">MONDAY</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/scheduled_operations/scheduled_start_time"></div>
                    <b>scheduled_start_time</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/scheduled_operations/scheduled_start_time" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>auto start time. value must be of ISO-8601 format &quot;HH:mm&quot;</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">scheduled_start_time_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/scheduled_operations/scheduled_stop_time"></div>
                    <b>scheduled_stop_time</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/scheduled_operations/scheduled_stop_time" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>auto stop time. value must be of ISO-8601 format &quot;HH:mm&quot;</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">scheduled_stop_time_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/service_console_url"></div>
                    <b>service_console_url</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/service_console_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL of the Service Console for the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">service_console_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/source_id"></div>
                    <b>source_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/source_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the source Autonomous Database that was cloned to create the current Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.source.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/standby_db"></div>
                    <b>standby_db</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/standby_db" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>**Deprecated** Autonomous Data Guard standby database details.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/standby_db/lag_time_in_seconds"></div>
                    <b>lag_time_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/standby_db/lag_time_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine the potential data loss in the event of a failover.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/standby_db/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/standby_db/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Additional information about the current lifecycle state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/standby_db/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/standby_db/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PROVISIONING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/standby_db/time_data_guard_role_changed"></div>
                    <b>time_data_guard_role_changed</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/standby_db/time_data_guard_role_changed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/standby_db/time_disaster_recovery_role_changed"></div>
                    <b>time_disaster_recovery_role_changed</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/standby_db/time_disaster_recovery_role_changed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Disaster Recovery role was switched for the standby Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/standby_whitelisted_ips"></div>
                    <b>standby_whitelisted_ips</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/standby_whitelisted_ips" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The client IP access control list (ACL). This feature is available for autonomous databases on <a href='https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html'>shared Exadata infrastructure</a> and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.</div>
                                            <div>For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID. Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[&quot;1.1.1.1&quot;,&quot;1.1.1.0/24&quot;,&quot;ocid1.vcn.oc1.sea.&lt;unique_id&gt;&quot;,&quot;ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1&quot;,&quot;ocid1.vcn.oc1.se a.&lt;unique_id2&gt;;1.1.0.0/16&quot;]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations. Example: `[&quot;1.1.1.1&quot;,&quot;1.1.1.0/24&quot;,&quot;1.1.2.25&quot;]`</div>
                                            <div>For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.</div>
                                            <div>This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/subnet_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the subnet the resource is associated with.</div>
                                            <div>**Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20. - For Autonomous Database, setting this will disable public secure access to the database.</div>
                                            <div>These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/supported_regions_to_clone_to"></div>
                    <b>supported_regions_to_clone_to</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/supported_regions_to_clone_to" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Autonomous Database was created.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_data_guard_role_changed"></div>
                    <b>time_data_guard_role_changed</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_data_guard_role_changed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Autonomous Data Guard role was switched for the Autonomous Database. For databases that have standbys in both the primary Data Guard region and a remote Data Guard standby region, this is the latest timestamp of either the database using the &quot;primary&quot; role in the primary Data Guard region, or database located in the remote Data Guard standby region.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_deletion_of_free_autonomous_database"></div>
                    <b>time_deletion_of_free_autonomous_database</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_deletion_of_free_autonomous_database" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Always Free database will be automatically deleted because of inactivity. If the database is in the STOPPED state and without activity until this time, it will be deleted.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_disaster_recovery_role_changed"></div>
                    <b>time_disaster_recovery_role_changed</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_disaster_recovery_role_changed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Disaster Recovery role was switched for the standby Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_local_data_guard_enabled"></div>
                    <b>time_local_data_guard_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_local_data_guard_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as the primary database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_maintenance_begin"></div>
                    <b>time_maintenance_begin</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_maintenance_begin" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time when maintenance will begin.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_maintenance_end"></div>
                    <b>time_maintenance_end</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_maintenance_end" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time when maintenance will end.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_of_last_failover"></div>
                    <b>time_of_last_failover</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_of_last_failover" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The timestamp of the last failover operation.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_of_last_refresh"></div>
                    <b>time_of_last_refresh</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_of_last_refresh" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time when last refresh happened.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_of_last_refresh_point"></div>
                    <b>time_of_last_refresh_point</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_of_last_refresh_point" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The refresh point timestamp (UTC). The refresh point is the time to which the database was most recently refreshed. Data created after the refresh point is not included in the refresh.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_of_last_switchover"></div>
                    <b>time_of_last_switchover</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_of_last_switchover" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The timestamp of the last switchover operation for the Autonomous Database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_of_next_refresh"></div>
                    <b>time_of_next_refresh</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_of_next_refresh" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time of next refresh.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_reclamation_of_free_autonomous_database"></div>
                    <b>time_reclamation_of_free_autonomous_database</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_reclamation_of_free_autonomous_database" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Always Free database will be stopped because of inactivity. If this time is reached without any database activity, the database will automatically be put into the STOPPED state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/time_until_reconnect_clone_enabled"></div>
                    <b>time_until_reconnect_clone_enabled</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/time_until_reconnect_clone_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time and date as an RFC3339 formatted string, e.g., 2022-01-01T12:00:00.000Z, to set the limit for a refreshable clone to be reconnected to its source database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/total_backup_storage_size_in_gbs"></div>
                    <b>total_backup_storage_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/total_backup_storage_size_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The backup storage to the database.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">1.2</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/used_data_storage_size_in_gbs"></div>
                    <b>used_data_storage_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/used_data_storage_size_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The storage space consumed by Autonomous Database in GBs.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/used_data_storage_size_in_tbs"></div>
                    <b>used_data_storage_size_in_tbs</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/used_data_storage_size_in_tbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The amount of storage that has been used, in terabytes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/vault_id"></div>
                    <b>vault_id</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/vault_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Oracle Cloud Infrastructure <a href='https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts'>vault</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-autonomous_database_clones/whitelisted_ips"></div>
                    <b>whitelisted_ips</b>
                    <a class="ansibleOptionLink" href="#return-autonomous_database_clones/whitelisted_ips" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The client IP access control list (ACL). This feature is available for autonomous databases on <a href='https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html'>shared Exadata infrastructure</a> and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.</div>
                                            <div>For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID. Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs. Example: `[&quot;1.1.1.1&quot;,&quot;1.1.1.0/24&quot;,&quot;ocid1.vcn.oc1.sea.&lt;unique_id&gt;&quot;,&quot;ocid1.vcn.oc1.sea.&lt;unique_id1&gt;;1.1.1.1&quot;,&quot;ocid1.vcn.oc1.se a.&lt;unique_id2&gt;;1.1.0.0/16&quot;]` For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations. Example: `[&quot;1.1.1.1&quot;,&quot;1.1.1.0/24&quot;,&quot;1.1.2.25&quot;]`</div>
                                            <div>For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.</div>
                                            <div>This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, dbVersion, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.</div>
                                        <br/>
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

