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

.. _ansible_collections.oracle.oci.oci_devops_trigger_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_devops_trigger -- Manage a Trigger resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.34.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_devops_trigger`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a Trigger resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new trigger.


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
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-actions"></div>
                    <b>actions</b>
                    <a class="ansibleOptionLink" href="#parameter-actions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of actions that are to be performed for this trigger.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when trigger_source is one of [&#x27;DEVOPS_CODE_REPOSITORY&#x27;, &#x27;BITBUCKET_SERVER&#x27;, &#x27;VBS&#x27;, &#x27;BITBUCKET_CLOUD&#x27;, &#x27;GITHUB&#x27;, &#x27;GITLAB_SERVER&#x27;, &#x27;GITLAB&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-actions/build_pipeline_id"></div>
                    <b>build_pipeline_id</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/build_pipeline_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the build pipeline to be triggered.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter"></div>
                    <b>filter</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/events"></div>
                    <b>events</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/events" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>PUSH</li>
                                                                                                                                                                                                <li>MERGE_REQUEST_CREATED</li>
                                                                                                                                                                                                <li>MERGE_REQUEST_UPDATED</li>
                                                                                                                                                                                                <li>MERGE_REQUEST_MERGED</li>
                                                                                                                                                                                                <li>PULL_REQUEST_CREATED</li>
                                                                                                                                                                                                <li>PULL_REQUEST_UPDATED</li>
                                                                                                                                                                                                <li>PULL_REQUEST_MERGED</li>
                                                                                                                                                                                                <li>PULL_REQUEST_OPENED</li>
                                                                                                                                                                                                <li>PULL_REQUEST_MODIFIED</li>
                                                                                                                                                                                                <li>PULL_REQUEST_REOPENED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The events, for example, PUSH, PULL_REQUEST_MERGE.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/exclude"></div>
                    <b>exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/exclude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when trigger_source is one of [&#x27;DEVOPS_CODE_REPOSITORY&#x27;, &#x27;VBS&#x27;, &#x27;BITBUCKET_CLOUD&#x27;, &#x27;GITHUB&#x27;, &#x27;GITLAB_SERVER&#x27;, &#x27;GITLAB&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/exclude/file_filter"></div>
                    <b>file_filter</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/exclude/file_filter" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when trigger_source is one of [&#x27;DEVOPS_CODE_REPOSITORY&#x27;, &#x27;VBS&#x27;, &#x27;BITBUCKET_CLOUD&#x27;, &#x27;GITHUB&#x27;, &#x27;GITLAB_SERVER&#x27;, &#x27;GITLAB&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/exclude/file_filter/file_paths"></div>
                    <b>file_paths</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/exclude/file_filter/file_paths" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The file paths/glob pattern for files.</div>
                                            <div>Applicable when trigger_source is &#x27;VBS&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/include"></div>
                    <b>include</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/include" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/include/base_ref"></div>
                    <b>base_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/include/base_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The target branch for pull requests; not applicable for push requests.</div>
                                            <div>Applicable when trigger_source is one of [&#x27;BITBUCKET_SERVER&#x27;, &#x27;VBS&#x27;, &#x27;BITBUCKET_CLOUD&#x27;, &#x27;GITHUB&#x27;, &#x27;GITLAB_SERVER&#x27;, &#x27;GITLAB&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/include/file_filter"></div>
                    <b>file_filter</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/include/file_filter" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when trigger_source is one of [&#x27;DEVOPS_CODE_REPOSITORY&#x27;, &#x27;VBS&#x27;, &#x27;BITBUCKET_CLOUD&#x27;, &#x27;GITHUB&#x27;, &#x27;GITLAB_SERVER&#x27;, &#x27;GITLAB&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/include/file_filter/file_paths"></div>
                    <b>file_paths</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/include/file_filter/file_paths" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The file paths/glob pattern for files.</div>
                                            <div>Applicable when trigger_source is &#x27;VBS&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/include/head_ref"></div>
                    <b>head_ref</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/include/head_ref" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Branch for push event; source branch for pull requests.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/include/repository_name"></div>
                    <b>repository_name</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/include/repository_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The repository name for trigger events.</div>
                                            <div>Applicable when trigger_source is &#x27;VBS&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-actions/filter/trigger_source"></div>
                    <b>trigger_source</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/filter/trigger_source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>VBS</li>
                                                                                                                                                                                                <li>DEVOPS_CODE_REPOSITORY</li>
                                                                                                                                                                                                <li>BITBUCKET_CLOUD</li>
                                                                                                                                                                                                <li>BITBUCKET_SERVER</li>
                                                                                                                                                                                                <li>GITLAB</li>
                                                                                                                                                                                                <li>GITHUB</li>
                                                                                                                                                                                                <li>GITLAB_SERVER</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Source of the trigger. Allowed values are, GITHUB and GITLAB.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-actions/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>TRIGGER_BUILD_PIPELINE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of action that will be taken. Allowed value is TRIGGER_BUILD_PIPELINE.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-connection_id"></div>
                    <b>connection_id</b>
                    <a class="ansibleOptionLink" href="#parameter-connection_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the connection resource used to get details for triggered events.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when trigger_source is one of [&#x27;VBS&#x27;, &#x27;BITBUCKET_CLOUD&#x27;, &#x27;GITHUB&#x27;, &#x27;GITLAB&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. See <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Optional description about the trigger.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                            <div>Trigger display name. Avoid entering confidential information.</div>
                                            <div>Required for create, update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                            <div>Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>. Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-project_id"></div>
                    <b>project_id</b>
                    <a class="ansibleOptionLink" href="#parameter-project_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the DevOps project to which the trigger belongs to.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-repository_id"></div>
                    <b>repository_id</b>
                    <a class="ansibleOptionLink" href="#parameter-repository_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the DevOps code repository.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when trigger_source is &#x27;DEVOPS_CODE_REPOSITORY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                            <div>The state of the Trigger.</div>
                                            <div>Use <em>state=present</em> to create or update a Trigger.</div>
                                            <div>Use <em>state=absent</em> to delete a Trigger.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-trigger_id"></div>
                    <b>trigger_id</b>
                    <a class="ansibleOptionLink" href="#parameter-trigger_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique trigger identifier.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-trigger_source"></div>
                    <b>trigger_source</b>
                    <a class="ansibleOptionLink" href="#parameter-trigger_source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GITHUB</li>
                                                                                                                                                                                                <li>VBS</li>
                                                                                                                                                                                                <li>DEVOPS_CODE_REPOSITORY</li>
                                                                                                                                                                                                <li>BITBUCKET_CLOUD</li>
                                                                                                                                                                                                <li>GITLAB_SERVER</li>
                                                                                                                                                                                                <li>GITLAB</li>
                                                                                                                                                                                                <li>BITBUCKET_SERVER</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Source of the trigger. Allowed values are, GITHUB and GITLAB.</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with trigger_id present.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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

    
    - name: Create trigger with trigger_source = GITHUB
      oci_devops_trigger:
        # required
        project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source: GITHUB

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Create trigger with trigger_source = VBS
      oci_devops_trigger:
        # required
        project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source: VBS

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Create trigger with trigger_source = DEVOPS_CODE_REPOSITORY
      oci_devops_trigger:
        # required
        project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create trigger with trigger_source = BITBUCKET_CLOUD
      oci_devops_trigger:
        # required
        project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source: BITBUCKET_CLOUD

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Create trigger with trigger_source = GITLAB_SERVER
      oci_devops_trigger:
        # required
        project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source: GITLAB_SERVER

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create trigger with trigger_source = GITLAB
      oci_devops_trigger:
        # required
        project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source: GITLAB

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Create trigger with trigger_source = BITBUCKET_SERVER
      oci_devops_trigger:
        # required
        project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source: BITBUCKET_SERVER

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update trigger with trigger_source = GITHUB
      oci_devops_trigger:
        # required
        trigger_source: GITHUB

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update trigger with trigger_source = VBS
      oci_devops_trigger:
        # required
        trigger_source: VBS

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update trigger with trigger_source = DEVOPS_CODE_REPOSITORY
      oci_devops_trigger:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update trigger with trigger_source = BITBUCKET_CLOUD
      oci_devops_trigger:
        # required
        trigger_source: BITBUCKET_CLOUD

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update trigger with trigger_source = GITLAB_SERVER
      oci_devops_trigger:
        # required
        trigger_source: GITLAB_SERVER

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update trigger with trigger_source = GITLAB
      oci_devops_trigger:
        # required
        trigger_source: GITLAB

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update trigger with trigger_source = BITBUCKET_SERVER
      oci_devops_trigger:
        # required
        trigger_source: BITBUCKET_SERVER

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = GITHUB
      oci_devops_trigger:
        # required
        trigger_source: GITHUB

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = VBS
      oci_devops_trigger:
        # required
        trigger_source: VBS

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = DEVOPS_CODE_REPOSITORY
      oci_devops_trigger:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = BITBUCKET_CLOUD
      oci_devops_trigger:
        # required
        trigger_source: BITBUCKET_CLOUD

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = GITLAB_SERVER
      oci_devops_trigger:
        # required
        trigger_source: GITLAB_SERVER

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = GITLAB
      oci_devops_trigger:
        # required
        trigger_source: GITLAB

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = BITBUCKET_SERVER
      oci_devops_trigger:
        # required
        trigger_source: BITBUCKET_SERVER

        # optional
        display_name: display_name_example
        description: description_example
        actions:
        - # required
          type: TRIGGER_BUILD_PIPELINE
          build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

          # optional
          filter:
            # required
            trigger_source: VBS

            # optional
            events: [ "PUSH" ]
            include:
              # optional
              repository_name: repository_name_example
              head_ref: head_ref_example
              base_ref: base_ref_example
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
            exclude:
              # optional
              file_filter:
                # optional
                file_paths: [ "file_paths_example" ]
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Delete trigger
      oci_devops_trigger:
        # required
        trigger_id: "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

    - name: Delete trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_devops_trigger:
        # required
        display_name: display_name_example
        state: absent





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="6">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="return-trigger"></div>
                    <b>trigger</b>
                    <a class="ansibleOptionLink" href="#return-trigger" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Trigger resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;actions&#x27;: [{&#x27;build_pipeline_id&#x27;: &#x27;ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;filter&#x27;: {&#x27;events&#x27;: [], &#x27;exclude&#x27;: {&#x27;file_filter&#x27;: {&#x27;file_paths&#x27;: []}}, &#x27;include&#x27;: {&#x27;base_ref&#x27;: &#x27;base_ref_example&#x27;, &#x27;file_filter&#x27;: {&#x27;file_paths&#x27;: []}, &#x27;head_ref&#x27;: &#x27;head_ref_example&#x27;, &#x27;repository_name&#x27;: &#x27;repository_name_example&#x27;}, &#x27;trigger_source&#x27;: &#x27;BITBUCKET_CLOUD&#x27;}, &#x27;type&#x27;: &#x27;TRIGGER_BUILD_PIPELINE&#x27;}], &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;connection_id&#x27;: &#x27;ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;ACTIVE&#x27;, &#x27;project_id&#x27;: &#x27;ocid1.project.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;repository_id&#x27;: &#x27;ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;system_tags&#x27;: {}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;trigger_source&#x27;: &#x27;GITHUB&#x27;, &#x27;trigger_url&#x27;: &#x27;trigger_url_example&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions"></div>
                    <b>actions</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of actions that are to be performed for this trigger.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/build_pipeline_id"></div>
                    <b>build_pipeline_id</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/build_pipeline_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the build pipeline to be triggered.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter"></div>
                    <b>filter</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/events"></div>
                    <b>events</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/events" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The events, for example, PUSH, PULL_REQUEST_MERGE.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/exclude"></div>
                    <b>exclude</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/exclude" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/exclude/file_filter"></div>
                    <b>file_filter</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/exclude/file_filter" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/exclude/file_filter/file_paths"></div>
                    <b>file_paths</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/exclude/file_filter/file_paths" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The file paths/glob pattern for files.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/include"></div>
                    <b>include</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/include" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/include/base_ref"></div>
                    <b>base_ref</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/include/base_ref" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The target branch for pull requests; not applicable for push requests.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">base_ref_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/include/file_filter"></div>
                    <b>file_filter</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/include/file_filter" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/include/file_filter/file_paths"></div>
                    <b>file_paths</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/include/file_filter/file_paths" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The file paths/glob pattern for files.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/include/head_ref"></div>
                    <b>head_ref</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/include/head_ref" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Branch for push event; source branch for pull requests.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">head_ref_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/include/repository_name"></div>
                    <b>repository_name</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/include/repository_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The repository name for trigger events.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">repository_name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/filter/trigger_source"></div>
                    <b>trigger_source</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/filter/trigger_source" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Source of the trigger. Allowed values are, GITHUB and GITLAB.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">BITBUCKET_CLOUD</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-trigger/actions/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-trigger/actions/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of action that will be taken. Allowed value is TRIGGER_BUILD_PIPELINE.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">TRIGGER_BUILD_PIPELINE</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-trigger/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the compartment that contains the trigger.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/connection_id"></div>
                    <b>connection_id</b>
                    <a class="ansibleOptionLink" href="#return-trigger/connection_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the connection resource used to get details for triggered events.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-trigger/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. See <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-trigger/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Description about the trigger.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-trigger/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Trigger display name. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-trigger/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>. Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-trigger/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Unique identifier that is immutable on creation.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-trigger/lifecycle_details" title="Permalink to this return value"></a>
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
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-trigger/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the trigger.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACTIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/project_id"></div>
                    <b>project_id</b>
                    <a class="ansibleOptionLink" href="#return-trigger/project_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the DevOps project to which the trigger belongs to.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.project.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/repository_id"></div>
                    <b>repository_id</b>
                    <a class="ansibleOptionLink" href="#return-trigger/repository_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the DevOps code repository.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-trigger/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Usage of system tag keys. These predefined keys are scoped to namespaces. See <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>. Example: `{&quot;orcl-cloud&quot;: {&quot;free-tier-retained&quot;: &quot;true&quot;}}`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-trigger/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the trigger was created. Format defined by <a href='https://datatracker.ietf.org/doc/html/rfc3339'>RFC3339</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-trigger/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the trigger was updated. Format defined by <a href='https://datatracker.ietf.org/doc/html/rfc3339'>RFC3339</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/trigger_source"></div>
                    <b>trigger_source</b>
                    <a class="ansibleOptionLink" href="#return-trigger/trigger_source" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Source of the trigger.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GITHUB</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-trigger/trigger_url"></div>
                    <b>trigger_url</b>
                    <a class="ansibleOptionLink" href="#return-trigger/trigger_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The endpoint that listens to trigger events.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">trigger_url_example</div>
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

