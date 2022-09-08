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

.. _ansible_collections.oracle.oci.oci_apigateway_deployment_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_apigateway_deployment -- Manage a Deployment resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 3.1.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_apigateway_deployment`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a Deployment resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new deployment.
- This resource has the following action operations in the :ref:`oracle.oci.oci_apigateway_deployment_actions <ansible_collections.oracle.oci.oci_apigateway_deployment_actions_module>` module: change_compartment.


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
            <th colspan="7">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment in which the resource is created.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>Required for delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-deployment_id"></div>
                    <b>deployment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-deployment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ocid of the deployment.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="7">
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
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                            <div>Example: `My new resource`</div>
                                            <div>Required for create, update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-gateway_id"></div>
                    <b>gateway_id</b>
                    <a class="ansibleOptionLink" href="#parameter-gateway_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the resource.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="7">
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
                                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-path_prefix"></div>
                    <b>path_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-path_prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A path on which to deploy all routes contained in the API deployment specification. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm'>Deploying an API on an API Gateway by Creating an API Deployment</a>.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="7">
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
                                                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="parameter-specification"></div>
                    <b>specification</b>
                    <a class="ansibleOptionLink" href="#parameter-specification" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-specification/logging_policies"></div>
                    <b>logging_policies</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/logging_policies" title="Permalink to this option"></a>
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
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/logging_policies/access_log"></div>
                    <b>access_log</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/logging_policies/access_log" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/logging_policies/access_log/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/logging_policies/access_log/is_enabled" title="Permalink to this option"></a>
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
                                            <div>Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to &#x27;access&#x27; in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/logging_policies/execution_log"></div>
                    <b>execution_log</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/logging_policies/execution_log" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/logging_policies/execution_log/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/logging_policies/execution_log/is_enabled" title="Permalink to this option"></a>
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
                                            <div>Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to &#x27;execution&#x27; in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/logging_policies/execution_log/log_level"></div>
                    <b>log_level</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/logging_policies/execution_log/log_level" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>INFO</li>
                                                                                                                                                                                                <li>WARN</li>
                                                                                                                                                                                                <li>ERROR</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies the log level used to control logging output of execution logs. Enabling logging at a given level also enables logging at all higher levels.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies"></div>
                    <b>request_policies</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies" title="Permalink to this option"></a>
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
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication"></div>
                    <b>authentication</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/audiences"></div>
                    <b>audiences</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/audiences" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of intended recipients for the token.</div>
                                            <div>Required when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/function_id"></div>
                    <b>function_id</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/function_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Oracle Functions function resource.</div>
                                            <div>Required when type is &#x27;CUSTOM_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/is_anonymous_access_allowed"></div>
                    <b>is_anonymous_access_allowed</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/is_anonymous_access_allowed" title="Permalink to this option"></a>
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
                                            <div>Whether an unauthenticated user may access the API. Must be &quot;true&quot; to enable ANONYMOUS route authorization.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/issuers"></div>
                    <b>issuers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/issuers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of parties that could have issued the token.</div>
                                            <div>Required when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/max_clock_skew_in_seconds"></div>
                    <b>max_clock_skew_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/max_clock_skew_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum expected time difference between the system clocks of the token issuer and the API Gateway.</div>
                                            <div>Applicable when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys"></div>
                    <b>public_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/is_ssl_verify_disabled"></div>
                    <b>is_ssl_verify_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/is_ssl_verify_disabled" title="Permalink to this option"></a>
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
                                            <div>Defines whether or not to uphold SSL verification.</div>
                                            <div>Applicable when type is &#x27;REMOTE_JWKS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys"></div>
                    <b>keys</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The set of static public keys.</div>
                                            <div>Applicable when type is &#x27;STATIC_KEYS&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/alg"></div>
                    <b>alg</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/alg" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The algorithm intended for use with this key.</div>
                                            <div>Required when format is &#x27;JSON_WEB_KEY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/e"></div>
                    <b>e</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/e" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The base64 url encoded exponent of the RSA public key represented by this key.</div>
                                            <div>Required when format is &#x27;JSON_WEB_KEY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/format"></div>
                    <b>format</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/format" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>JSON_WEB_KEY</li>
                                                                                                                                                                                                <li>PEM</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The format of the public key.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The content of the PEM-encoded public key.</div>
                                            <div>Required when format is &#x27;PEM&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/key_ops"></div>
                    <b>key_ops</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/key_ops" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>verify</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The operations for which this key is to be used.</div>
                                            <div>Applicable when format is &#x27;JSON_WEB_KEY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/kid"></div>
                    <b>kid</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/kid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A unique key ID. This key will be used to verify the signature of a JWT with matching &quot;kid&quot;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/kty"></div>
                    <b>kty</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/kty" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>RSA</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The key type.</div>
                                            <div>Required when format is &#x27;JSON_WEB_KEY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/n"></div>
                    <b>n</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/n" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The base64 url encoded modulus of the RSA public key represented by this key.</div>
                                            <div>Required when format is &#x27;JSON_WEB_KEY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/keys/use"></div>
                    <b>use</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/keys/use" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>sig</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The intended use of the public key.</div>
                                            <div>Applicable when format is &#x27;JSON_WEB_KEY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/max_cache_duration_in_hours"></div>
                    <b>max_cache_duration_in_hours</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/max_cache_duration_in_hours" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The duration for which the JWKS should be cached before it is fetched again.</div>
                                            <div>Applicable when type is &#x27;REMOTE_JWKS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STATIC_KEYS</li>
                                                                                                                                                                                                <li>REMOTE_JWKS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the public key set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/public_keys/uri"></div>
                    <b>uri</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/public_keys/uri" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The uri from which to retrieve the key. It must be accessible without authentication.</div>
                                            <div>Required when type is &#x27;REMOTE_JWKS&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/token_auth_scheme"></div>
                    <b>token_auth_scheme</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/token_auth_scheme" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The authentication scheme that is to be used when authenticating the token. This must to be provided if &quot;tokenHeader&quot; is specified.</div>
                                            <div>Applicable when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/token_header"></div>
                    <b>token_header</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/token_header" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the header containing the authentication token.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/token_query_param"></div>
                    <b>token_query_param</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/token_query_param" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the query parameter containing the authentication token.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>JWT_AUTHENTICATION</li>
                                                                                                                                                                                                <li>CUSTOM_AUTHENTICATION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the authentication policy to use.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/verify_claims"></div>
                    <b>verify_claims</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/verify_claims" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of claims which should be validated to consider the token valid.</div>
                                            <div>Applicable when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/verify_claims/is_required"></div>
                    <b>is_required</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/verify_claims/is_required" title="Permalink to this option"></a>
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
                                            <div>Whether the claim is required to be present in the JWT or not. If set to &quot;false&quot;, the claim values will be matched only if the claim is present in the JWT.</div>
                                            <div>Applicable when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/verify_claims/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/verify_claims/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the claim.</div>
                                            <div>Required when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/authentication/verify_claims/values"></div>
                    <b>values</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/authentication/verify_claims/values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of acceptable values for a given claim. If this value is &quot;null&quot; or empty and &quot;isRequired&quot; set to &quot;true&quot;, then the presence of this claim in the JWT is validated.</div>
                                            <div>Applicable when type is &#x27;JWT_AUTHENTICATION&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/cors"></div>
                    <b>cors</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/cors" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/cors/allowed_headers"></div>
                    <b>allowed_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/cors/allowed_headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header. &#x27;*&#x27; will allow all headers.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/cors/allowed_methods"></div>
                    <b>allowed_methods</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/cors/allowed_methods" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the Access-Control-Allow-Methods header. &#x27;*&#x27; will allow all methods.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/cors/allowed_origins"></div>
                    <b>allowed_origins</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/cors/allowed_origins" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will send the Access-Control-Allow-Origin header with the best origin match for the circumstances. &#x27;*&#x27; will match any origins, and &#x27;null&#x27; will match queries from &#x27;file:&#x27; origins. All other origins must be qualified with the scheme, full hostname, and port if necessary.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/cors/exposed_headers"></div>
                    <b>exposed_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/cors/exposed_headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers that the client will be allowed to see from the response as indicated by the Access-Control-Expose-Headers header. &#x27;*&#x27; will expose all headers.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/cors/is_allow_credentials_enabled"></div>
                    <b>is_allow_credentials_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/cors/is_allow_credentials_enabled" title="Permalink to this option"></a>
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
                                            <div>Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/cors/max_age_in_seconds"></div>
                    <b>max_age_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/cors/max_age_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age if greater than 0.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/mutual_tls"></div>
                    <b>mutual_tls</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/mutual_tls" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/mutual_tls/allowed_sans"></div>
                    <b>allowed_sans</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/mutual_tls/allowed_sans" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Allowed list of CN or SAN which will be used for verification of certificate.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/mutual_tls/is_verified_certificate_required"></div>
                    <b>is_verified_certificate_required</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/mutual_tls/is_verified_certificate_required" title="Permalink to this option"></a>
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
                                            <div>Determines whether to enable client verification when API Consumer makes connection to the gateway.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/rate_limiting"></div>
                    <b>rate_limiting</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/rate_limiting" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/rate_limiting/rate_in_requests_per_second"></div>
                    <b>rate_in_requests_per_second</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/rate_limiting/rate_in_requests_per_second" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum number of requests per second to allow.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/rate_limiting/rate_key"></div>
                    <b>rate_key</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/rate_limiting/rate_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CLIENT_IP</li>
                                                                                                                                                                                                <li>TOTAL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The key used to group requests together.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/usage_plans"></div>
                    <b>usage_plans</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/usage_plans" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/request_policies/usage_plans/token_locations"></div>
                    <b>token_locations</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/request_policies/usage_plans/token_locations" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of context variables specifying where API tokens may be located in a request. Example locations: - &quot;request.headers[token]&quot; - &quot;request.query[token]&quot; - &quot;request.auth[Token]&quot; - &quot;request.path[TOKEN]&quot;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes"></div>
                    <b>routes</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of routes that this API exposes.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend"></div>
                    <b>backend</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/body"></div>
                    <b>body</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/body" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The body of the stock response from the mock backend.</div>
                                            <div>Applicable when type is &#x27;STOCK_RESPONSE_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/connect_timeout_in_seconds"></div>
                    <b>connect_timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/connect_timeout_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defines a timeout for establishing a connection with a proxied server.</div>
                                            <div>Applicable when type is &#x27;HTTP_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/function_id"></div>
                    <b>function_id</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/function_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Oracle Functions function resource.</div>
                                            <div>Required when type is &#x27;ORACLE_FUNCTIONS_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/headers"></div>
                    <b>headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The headers of the stock response from the mock backend.</div>
                                            <div>Applicable when type is &#x27;STOCK_RESPONSE_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/headers/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/headers/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the header.</div>
                                            <div>Applicable when type is &#x27;STOCK_RESPONSE_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/headers/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/headers/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value of the header.</div>
                                            <div>Applicable when type is &#x27;STOCK_RESPONSE_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/is_ssl_verify_disabled"></div>
                    <b>is_ssl_verify_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/is_ssl_verify_disabled" title="Permalink to this option"></a>
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
                                            <div>Defines whether or not to uphold SSL verification.</div>
                                            <div>Applicable when type is &#x27;HTTP_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/read_timeout_in_seconds"></div>
                    <b>read_timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/read_timeout_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defines a timeout for reading a response from the proxied server.</div>
                                            <div>Applicable when type is &#x27;HTTP_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/send_timeout_in_seconds"></div>
                    <b>send_timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/send_timeout_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defines a timeout for transmitting a request to the proxied server.</div>
                                            <div>Applicable when type is &#x27;HTTP_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/status" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The status code of the stock response from the mock backend.</div>
                                            <div>Required when type is &#x27;STOCK_RESPONSE_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>HTTP_BACKEND</li>
                                                                                                                                                                                                <li>ORACLE_FUNCTIONS_BACKEND</li>
                                                                                                                                                                                                <li>STOCK_RESPONSE_BACKEND</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the API backend.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/backend/url"></div>
                    <b>url</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/backend/url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when type is &#x27;HTTP_BACKEND&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/logging_policies"></div>
                    <b>logging_policies</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/logging_policies" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/logging_policies/access_log"></div>
                    <b>access_log</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/logging_policies/access_log" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/logging_policies/access_log/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/logging_policies/access_log/is_enabled" title="Permalink to this option"></a>
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
                                            <div>Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to &#x27;access&#x27; in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/logging_policies/execution_log"></div>
                    <b>execution_log</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/logging_policies/execution_log" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/logging_policies/execution_log/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/logging_policies/execution_log/is_enabled" title="Permalink to this option"></a>
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
                                            <div>Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to &#x27;execution&#x27; in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/logging_policies/execution_log/log_level"></div>
                    <b>log_level</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/logging_policies/execution_log/log_level" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>INFO</li>
                                                                                                                                                                                                <li>WARN</li>
                                                                                                                                                                                                <li>ERROR</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies the log level used to control logging output of execution logs. Enabling logging at a given level also enables logging at all higher levels.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/methods"></div>
                    <b>methods</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/methods" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ANY</li>
                                                                                                                                                                                                <li>HEAD</li>
                                                                                                                                                                                                <li>GET</li>
                                                                                                                                                                                                <li>POST</li>
                                                                                                                                                                                                <li>PUT</li>
                                                                                                                                                                                                <li>PATCH</li>
                                                                                                                                                                                                <li>DELETE</li>
                                                                                                                                                                                                <li>OPTIONS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>A list of allowed methods on this route.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A URL path pattern that must be matched on this route. The path pattern may contain a subset of RFC 6570 identifiers to allow wildcard and parameterized matching.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies"></div>
                    <b>request_policies</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/authorization"></div>
                    <b>authorization</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/authorization" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/authorization/allowed_scope"></div>
                    <b>allowed_scope</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/authorization/allowed_scope" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user whose scope includes any of these access ranges is allowed on this route. Access ranges are case-sensitive.</div>
                                            <div>Required when type is &#x27;ANY_OF&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/authorization/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/authorization/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ANY_OF</li>
                                                                                                                                                                                                <li>ANONYMOUS</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>AUTHENTICATION_ONLY</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Indicates how authorization should be applied. For a type of ANY_OF, an &quot;allowedScope&quot; property must also be specified. Otherwise, only a type is required. For a type of ANONYMOUS, an authenticated API must have the &quot;isAnonymousAccessAllowed&quot; property set to &quot;true&quot; in the authentication policy.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/body_validation"></div>
                    <b>body_validation</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/body_validation" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/body_validation/content"></div>
                    <b>content</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/body_validation/content" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The content of the request body. The key is a <a href='https://tools.ietf.org/html/rfc7231#appendix-D'>media type range</a> subset restricted to the following schema</div>
                                            <div>key ::= ( / (  &quot;*&quot; &quot;/&quot; &quot;*&quot; ) / ( type &quot;/&quot; &quot;*&quot; ) / ( type &quot;/&quot; subtype ) )</div>
                                            <div>For requests that match multiple keys, only the most specific key is applicable. e.g. `text/plain` overrides `text/*`</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/body_validation/content/validation_type"></div>
                    <b>validation_type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/body_validation/content/validation_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>NONE</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Validation type defines the content validation method.</div>
                                            <div>Make the validation to first parse the body as the respective format.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/body_validation/required"></div>
                    <b>required</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/body_validation/required" title="Permalink to this option"></a>
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
                                            <div>Determines if the request body is required in the request.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/body_validation/validation_mode"></div>
                    <b>validation_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/body_validation/validation_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ENFORCING</li>
                                                                                                                                                                                                <li>PERMISSIVE</li>
                                                                                                                                                                                                <li>DISABLED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Validation behavior mode.</div>
                                            <div>In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend.</div>
                                            <div>In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path.</div>
                                            <div>`DISABLED` type turns the validation off.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/cors"></div>
                    <b>cors</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/cors" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/cors/allowed_headers"></div>
                    <b>allowed_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/cors/allowed_headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header. &#x27;*&#x27; will allow all headers.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/cors/allowed_methods"></div>
                    <b>allowed_methods</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/cors/allowed_methods" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the Access-Control-Allow-Methods header. &#x27;*&#x27; will allow all methods.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/cors/allowed_origins"></div>
                    <b>allowed_origins</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/cors/allowed_origins" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will send the Access-Control-Allow-Origin header with the best origin match for the circumstances. &#x27;*&#x27; will match any origins, and &#x27;null&#x27; will match queries from &#x27;file:&#x27; origins. All other origins must be qualified with the scheme, full hostname, and port if necessary.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/cors/exposed_headers"></div>
                    <b>exposed_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/cors/exposed_headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers that the client will be allowed to see from the response as indicated by the Access-Control-Expose-Headers header. &#x27;*&#x27; will expose all headers.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/cors/is_allow_credentials_enabled"></div>
                    <b>is_allow_credentials_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/cors/is_allow_credentials_enabled" title="Permalink to this option"></a>
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
                                            <div>Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/cors/max_age_in_seconds"></div>
                    <b>max_age_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/cors/max_age_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age if greater than 0.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations"></div>
                    <b>header_transformations</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/filter_headers"></div>
                    <b>filter_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/filter_headers" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/filter_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/filter_headers/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/filter_headers/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/filter_headers/items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/filter_headers/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/filter_headers/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ALLOW</li>
                                                                                                                                                                                                <li>BLOCK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW permits only the headers in the list and removes all others, so it acts as an inclusion list.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/rename_headers"></div>
                    <b>rename_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/rename_headers" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/rename_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/rename_headers/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/rename_headers/items/_from"></div>
                    <b>_from</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/rename_headers/items/_from" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The original case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/rename_headers/items/to"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/rename_headers/items/to" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The new name of the header.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/set_headers"></div>
                    <b>set_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/set_headers" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/set_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/set_headers/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/set_headers/items/if_exists"></div>
                    <b>if_exists</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/set_headers/items/if_exists" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OVERWRITE</li>
                                                                                                                                                                                                <li>APPEND</li>
                                                                                                                                                                                                <li>SKIP</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If a header with the same name already exists in the request, OVERWRITE will overwrite the value, APPEND will append to the existing value, or SKIP will keep the existing value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/set_headers/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/set_headers/items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_transformations/set_headers/items/values"></div>
                    <b>values</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_transformations/set_headers/items/values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of new values.  Each value can be a constant or may include one or more expressions enclosed within ${} delimiters.</div>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_validations"></div>
                    <b>header_validations</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_validations" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_validations/headers"></div>
                    <b>headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_validations/headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_validations/headers/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_validations/headers/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Parameter name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_validations/headers/required"></div>
                    <b>required</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_validations/headers/required" title="Permalink to this option"></a>
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
                                            <div>Determines if the header is required in the request.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/header_validations/validation_mode"></div>
                    <b>validation_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/header_validations/validation_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ENFORCING</li>
                                                                                                                                                                                                <li>PERMISSIVE</li>
                                                                                                                                                                                                <li>DISABLED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Validation behavior mode.</div>
                                            <div>In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend.</div>
                                            <div>In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path.</div>
                                            <div>`DISABLED` type turns the validation off.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations"></div>
                    <b>query_parameter_transformations</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/filter_query_parameters"></div>
                    <b>filter_query_parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/filter_query_parameters" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of query parameters.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The case-sensitive name of the query parameter.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ALLOW</li>
                                                                                                                                                                                                <li>BLOCK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list.  ALLOW permits only the parameters in the list and removes all others, so it acts as an inclusion list.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/rename_query_parameters"></div>
                    <b>rename_query_parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/rename_query_parameters" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of query parameters.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items/_from"></div>
                    <b>_from</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items/_from" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The original case-sensitive name of the query parameter.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items/to"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items/to" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The new name of the query parameter.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters"></div>
                    <b>set_query_parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of query parameters.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/if_exists"></div>
                    <b>if_exists</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/if_exists" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OVERWRITE</li>
                                                                                                                                                                                                <li>APPEND</li>
                                                                                                                                                                                                <li>SKIP</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If a query parameter with the same name already exists in the request, OVERWRITE will overwrite the value, APPEND will append to the existing value, or SKIP will keep the existing value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The case-sensitive name of the query parameter.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/values"></div>
                    <b>values</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of new values.  Each value can be a constant or may include one or more expressions enclosed within ${} delimiters.</div>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_validations"></div>
                    <b>query_parameter_validations</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_validations" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_validations/parameters"></div>
                    <b>parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_validations/parameters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_validations/parameters/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_validations/parameters/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Parameter name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_validations/parameters/required"></div>
                    <b>required</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_validations/parameters/required" title="Permalink to this option"></a>
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
                                            <div>Determines if the parameter is required in the request.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/query_parameter_validations/validation_mode"></div>
                    <b>validation_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/query_parameter_validations/validation_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ENFORCING</li>
                                                                                                                                                                                                <li>PERMISSIVE</li>
                                                                                                                                                                                                <li>DISABLED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Validation behavior mode.</div>
                                            <div>In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend.</div>
                                            <div>In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path.</div>
                                            <div>`DISABLED` type turns the validation off.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/response_cache_lookup"></div>
                    <b>response_cache_lookup</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/response_cache_lookup" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/response_cache_lookup/cache_key_additions"></div>
                    <b>cache_key_additions</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/response_cache_lookup/cache_key_additions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of context expressions whose values will be added to the base cache key. Values should contain an expression enclosed within ${} delimiters. Only the request context is available.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/response_cache_lookup/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/response_cache_lookup/is_enabled" title="Permalink to this option"></a>
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
                                            <div>Whether this policy is currently enabled.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/response_cache_lookup/is_private_caching_enabled"></div>
                    <b>is_private_caching_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/response_cache_lookup/is_private_caching_enabled" title="Permalink to this option"></a>
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
                                            <div>Set true to allow caching responses where the request has an Authorization header. Ensure you have configured your cache key additions to get the level of isolation across authenticated requests that you require.</div>
                                            <div>When false, any request with an Authorization header will not be stored in the Response Cache.</div>
                                            <div>If using the CustomAuthenticationPolicy then the tokenHeader/tokenQueryParam are also subject to this check.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/request_policies/response_cache_lookup/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/request_policies/response_cache_lookup/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SIMPLE_LOOKUP_POLICY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the Response Cache Store Policy.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies"></div>
                    <b>response_policies</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies" title="Permalink to this option"></a>
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
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations"></div>
                    <b>header_transformations</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/filter_headers"></div>
                    <b>filter_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/filter_headers" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/filter_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/filter_headers/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/filter_headers/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/filter_headers/items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/filter_headers/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/filter_headers/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ALLOW</li>
                                                                                                                                                                                                <li>BLOCK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW permits only the headers in the list and removes all others, so it acts as an inclusion list.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/rename_headers"></div>
                    <b>rename_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/rename_headers" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/rename_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/rename_headers/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/rename_headers/items/_from"></div>
                    <b>_from</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/rename_headers/items/_from" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The original case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/rename_headers/items/to"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/rename_headers/items/to" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The new name of the header.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/set_headers"></div>
                    <b>set_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/set_headers" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/set_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/set_headers/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of headers.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/set_headers/items/if_exists"></div>
                    <b>if_exists</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/set_headers/items/if_exists" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OVERWRITE</li>
                                                                                                                                                                                                <li>APPEND</li>
                                                                                                                                                                                                <li>SKIP</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If a header with the same name already exists in the request, OVERWRITE will overwrite the value, APPEND will append to the existing value, or SKIP will keep the existing value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/set_headers/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/set_headers/items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/header_transformations/set_headers/items/values"></div>
                    <b>values</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/header_transformations/set_headers/items/values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of new values.  Each value can be a constant or may include one or more expressions enclosed within ${} delimiters.</div>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/response_cache_store"></div>
                    <b>response_cache_store</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/response_cache_store" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/response_cache_store/time_to_live_in_seconds"></div>
                    <b>time_to_live_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/response_cache_store/time_to_live_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Sets the number of seconds for a response from a backend being stored in the Response Cache before it expires.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-specification/routes/response_policies/response_cache_store/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-specification/routes/response_policies/response_cache_store/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>FIXED_TTL_STORE_POLICY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the Response Cache Store Policy.</div>
                                                        </td>
            </tr>
                    
                    
                    
                    
                                <tr>
                                                                <td colspan="7">
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
                                            <div>The state of the Deployment.</div>
                                            <div>Use <em>state=present</em> to create or update a Deployment.</div>
                                            <div>Use <em>state=absent</em> to delete a Deployment.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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
                                                                <td colspan="7">
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

    
    - name: Create deployment
      oci_apigateway_deployment:
        # required
        gateway_id: "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        path_prefix: path_prefix_example
        specification:
          # optional
          request_policies:
            # optional
            authentication:
              # required
              issuers: [ "issuers_example" ]
              audiences: [ "audiences_example" ]
              public_keys:
                # required
                type: STATIC_KEYS

                # optional
                keys:
                - # required
                  kty: RSA
                  alg: alg_example
                  n: n_example
                  e: e_example
                  kid: kid_example
                  format: JSON_WEB_KEY

                  # optional
                  use: sig
                  key_ops: [ "verify" ]
              type: JWT_AUTHENTICATION

                  # optional
              token_auth_scheme: token_auth_scheme_example
              verify_claims:
              - # required
                key: key_example

                # optional
                values: [ "values_example" ]
                is_required: true
              max_clock_skew_in_seconds: 3.4
              is_anonymous_access_allowed: true
              token_header: token_header_example
              token_query_param: token_query_param_example
            rate_limiting:
              # required
              rate_in_requests_per_second: 56
              rate_key: CLIENT_IP
            cors:
              # required
              allowed_origins: [ "allowed_origins_example" ]

              # optional
              allowed_methods: [ "allowed_methods_example" ]
              allowed_headers: [ "allowed_headers_example" ]
              exposed_headers: [ "exposed_headers_example" ]
              is_allow_credentials_enabled: true
              max_age_in_seconds: 56
            mutual_tls:
              # optional
              is_verified_certificate_required: true
              allowed_sans: [ "allowed_sans_example" ]
            usage_plans:
              # required
              token_locations: [ "token_locations_example" ]
          logging_policies:
            # optional
            access_log:
              # optional
              is_enabled: true
            execution_log:
              # optional
              is_enabled: true
              log_level: INFO
          routes:
          - # required
            path: path_example
            backend:
              # required
              url: url_example
              type: HTTP_BACKEND

              # optional
              connect_timeout_in_seconds: 3.4
              read_timeout_in_seconds: 3.4
              send_timeout_in_seconds: 3.4
              is_ssl_verify_disabled: true

            # optional
            methods: [ "ANY" ]
            request_policies:
              # optional
              authorization:
                # required
                allowed_scope: [ "allowed_scope_example" ]
                type: ANY_OF
              cors:
                # required
                allowed_origins: [ "allowed_origins_example" ]

                # optional
                allowed_methods: [ "allowed_methods_example" ]
                allowed_headers: [ "allowed_headers_example" ]
                exposed_headers: [ "exposed_headers_example" ]
                is_allow_credentials_enabled: true
                max_age_in_seconds: 56
              query_parameter_validations:
                # optional
                parameters:
                - # required
                  name: name_example

                  # optional
                  required: true
                validation_mode: ENFORCING
              header_validations:
                # optional
                headers:
                - # required
                  name: name_example

                  # optional
                  required: true
                validation_mode: ENFORCING
              body_validation:
                # required
                content:
                  # optional
                  validation_type: NONE
                  # optional
                required: true
                validation_mode: ENFORCING
              header_transformations:
                # optional
                set_headers:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_headers:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_headers:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              query_parameter_transformations:
                # optional
                set_query_parameters:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_query_parameters:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_query_parameters:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              response_cache_lookup:
                # required
                type: SIMPLE_LOOKUP_POLICY

                # optional
                is_enabled: true
                is_private_caching_enabled: true
                cache_key_additions: [ "cache_key_additions_example" ]
            response_policies:
              # optional
              header_transformations:
                # optional
                set_headers:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_headers:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_headers:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              response_cache_store:
                # required
                type: FIXED_TTL_STORE_POLICY
                time_to_live_in_seconds: 56
            logging_policies:
              # optional
              access_log:
                # optional
                is_enabled: true
              execution_log:
                # optional
                is_enabled: true
                log_level: INFO

        # optional
        display_name: display_name_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deployment
      oci_apigateway_deployment:
        # required
        deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example
        specification:
          # optional
          request_policies:
            # optional
            authentication:
              # required
              issuers: [ "issuers_example" ]
              audiences: [ "audiences_example" ]
              public_keys:
                # required
                type: STATIC_KEYS

                # optional
                keys:
                - # required
                  kty: RSA
                  alg: alg_example
                  n: n_example
                  e: e_example
                  kid: kid_example
                  format: JSON_WEB_KEY

                  # optional
                  use: sig
                  key_ops: [ "verify" ]
              type: JWT_AUTHENTICATION

                  # optional
              token_auth_scheme: token_auth_scheme_example
              verify_claims:
              - # required
                key: key_example

                # optional
                values: [ "values_example" ]
                is_required: true
              max_clock_skew_in_seconds: 3.4
              is_anonymous_access_allowed: true
              token_header: token_header_example
              token_query_param: token_query_param_example
            rate_limiting:
              # required
              rate_in_requests_per_second: 56
              rate_key: CLIENT_IP
            cors:
              # required
              allowed_origins: [ "allowed_origins_example" ]

              # optional
              allowed_methods: [ "allowed_methods_example" ]
              allowed_headers: [ "allowed_headers_example" ]
              exposed_headers: [ "exposed_headers_example" ]
              is_allow_credentials_enabled: true
              max_age_in_seconds: 56
            mutual_tls:
              # optional
              is_verified_certificate_required: true
              allowed_sans: [ "allowed_sans_example" ]
            usage_plans:
              # required
              token_locations: [ "token_locations_example" ]
          logging_policies:
            # optional
            access_log:
              # optional
              is_enabled: true
            execution_log:
              # optional
              is_enabled: true
              log_level: INFO
          routes:
          - # required
            path: path_example
            backend:
              # required
              url: url_example
              type: HTTP_BACKEND

              # optional
              connect_timeout_in_seconds: 3.4
              read_timeout_in_seconds: 3.4
              send_timeout_in_seconds: 3.4
              is_ssl_verify_disabled: true

            # optional
            methods: [ "ANY" ]
            request_policies:
              # optional
              authorization:
                # required
                allowed_scope: [ "allowed_scope_example" ]
                type: ANY_OF
              cors:
                # required
                allowed_origins: [ "allowed_origins_example" ]

                # optional
                allowed_methods: [ "allowed_methods_example" ]
                allowed_headers: [ "allowed_headers_example" ]
                exposed_headers: [ "exposed_headers_example" ]
                is_allow_credentials_enabled: true
                max_age_in_seconds: 56
              query_parameter_validations:
                # optional
                parameters:
                - # required
                  name: name_example

                  # optional
                  required: true
                validation_mode: ENFORCING
              header_validations:
                # optional
                headers:
                - # required
                  name: name_example

                  # optional
                  required: true
                validation_mode: ENFORCING
              body_validation:
                # required
                content:
                  # optional
                  validation_type: NONE
                  # optional
                required: true
                validation_mode: ENFORCING
              header_transformations:
                # optional
                set_headers:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_headers:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_headers:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              query_parameter_transformations:
                # optional
                set_query_parameters:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_query_parameters:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_query_parameters:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              response_cache_lookup:
                # required
                type: SIMPLE_LOOKUP_POLICY

                # optional
                is_enabled: true
                is_private_caching_enabled: true
                cache_key_additions: [ "cache_key_additions_example" ]
            response_policies:
              # optional
              header_transformations:
                # optional
                set_headers:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_headers:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_headers:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              response_cache_store:
                # required
                type: FIXED_TTL_STORE_POLICY
                time_to_live_in_seconds: 56
            logging_policies:
              # optional
              access_log:
                # optional
                is_enabled: true
              execution_log:
                # optional
                is_enabled: true
                log_level: INFO
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_apigateway_deployment:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example

        # optional
        specification:
          # optional
          request_policies:
            # optional
            authentication:
              # required
              issuers: [ "issuers_example" ]
              audiences: [ "audiences_example" ]
              public_keys:
                # required
                type: STATIC_KEYS

                # optional
                keys:
                - # required
                  kty: RSA
                  alg: alg_example
                  n: n_example
                  e: e_example
                  kid: kid_example
                  format: JSON_WEB_KEY

                  # optional
                  use: sig
                  key_ops: [ "verify" ]
              type: JWT_AUTHENTICATION

                  # optional
              token_auth_scheme: token_auth_scheme_example
              verify_claims:
              - # required
                key: key_example

                # optional
                values: [ "values_example" ]
                is_required: true
              max_clock_skew_in_seconds: 3.4
              is_anonymous_access_allowed: true
              token_header: token_header_example
              token_query_param: token_query_param_example
            rate_limiting:
              # required
              rate_in_requests_per_second: 56
              rate_key: CLIENT_IP
            cors:
              # required
              allowed_origins: [ "allowed_origins_example" ]

              # optional
              allowed_methods: [ "allowed_methods_example" ]
              allowed_headers: [ "allowed_headers_example" ]
              exposed_headers: [ "exposed_headers_example" ]
              is_allow_credentials_enabled: true
              max_age_in_seconds: 56
            mutual_tls:
              # optional
              is_verified_certificate_required: true
              allowed_sans: [ "allowed_sans_example" ]
            usage_plans:
              # required
              token_locations: [ "token_locations_example" ]
          logging_policies:
            # optional
            access_log:
              # optional
              is_enabled: true
            execution_log:
              # optional
              is_enabled: true
              log_level: INFO
          routes:
          - # required
            path: path_example
            backend:
              # required
              url: url_example
              type: HTTP_BACKEND

              # optional
              connect_timeout_in_seconds: 3.4
              read_timeout_in_seconds: 3.4
              send_timeout_in_seconds: 3.4
              is_ssl_verify_disabled: true

            # optional
            methods: [ "ANY" ]
            request_policies:
              # optional
              authorization:
                # required
                allowed_scope: [ "allowed_scope_example" ]
                type: ANY_OF
              cors:
                # required
                allowed_origins: [ "allowed_origins_example" ]

                # optional
                allowed_methods: [ "allowed_methods_example" ]
                allowed_headers: [ "allowed_headers_example" ]
                exposed_headers: [ "exposed_headers_example" ]
                is_allow_credentials_enabled: true
                max_age_in_seconds: 56
              query_parameter_validations:
                # optional
                parameters:
                - # required
                  name: name_example

                  # optional
                  required: true
                validation_mode: ENFORCING
              header_validations:
                # optional
                headers:
                - # required
                  name: name_example

                  # optional
                  required: true
                validation_mode: ENFORCING
              body_validation:
                # required
                content:
                  # optional
                  validation_type: NONE
                  # optional
                required: true
                validation_mode: ENFORCING
              header_transformations:
                # optional
                set_headers:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_headers:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_headers:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              query_parameter_transformations:
                # optional
                set_query_parameters:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_query_parameters:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_query_parameters:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              response_cache_lookup:
                # required
                type: SIMPLE_LOOKUP_POLICY

                # optional
                is_enabled: true
                is_private_caching_enabled: true
                cache_key_additions: [ "cache_key_additions_example" ]
            response_policies:
              # optional
              header_transformations:
                # optional
                set_headers:
                  # required
                  items:
                  - # required
                    name: name_example
                    values: [ "values_example" ]

                    # optional
                    if_exists: OVERWRITE
                rename_headers:
                  # required
                  items:
                  - # required
                    _from: _from_example
                    to: to_example
                filter_headers:
                  # required
                  type: ALLOW
                  items:
                  - # required
                    name: name_example
              response_cache_store:
                # required
                type: FIXED_TTL_STORE_POLICY
                time_to_live_in_seconds: 56
            logging_policies:
              # optional
              access_log:
                # optional
                is_enabled: true
              execution_log:
                # optional
                is_enabled: true
                log_level: INFO
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Delete deployment
      oci_apigateway_deployment:
        # required
        deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

    - name: Delete deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_apigateway_deployment:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
            <th colspan="8">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="8">
                    <div class="ansibleOptionAnchor" id="return-deployment"></div>
                    <b>deployment</b>
                    <a class="ansibleOptionLink" href="#return-deployment" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Deployment resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;endpoint&#x27;: &#x27;endpoint_example&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;gateway_id&#x27;: &#x27;ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;path_prefix&#x27;: &#x27;path_prefix_example&#x27;, &#x27;specification&#x27;: {&#x27;logging_policies&#x27;: {&#x27;access_log&#x27;: {&#x27;is_enabled&#x27;: True}, &#x27;execution_log&#x27;: {&#x27;is_enabled&#x27;: True, &#x27;log_level&#x27;: &#x27;INFO&#x27;}}, &#x27;request_policies&#x27;: {&#x27;authentication&#x27;: {&#x27;audiences&#x27;: [], &#x27;function_id&#x27;: &#x27;ocid1.function.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;is_anonymous_access_allowed&#x27;: True, &#x27;issuers&#x27;: [], &#x27;max_clock_skew_in_seconds&#x27;: 3.4, &#x27;public_keys&#x27;: {&#x27;is_ssl_verify_disabled&#x27;: True, &#x27;keys&#x27;: [{&#x27;alg&#x27;: &#x27;alg_example&#x27;, &#x27;e&#x27;: &#x27;e_example&#x27;, &#x27;format&#x27;: &#x27;JSON_WEB_KEY&#x27;, &#x27;key&#x27;: &#x27;key_example&#x27;, &#x27;key_ops&#x27;: [], &#x27;kid&#x27;: &#x27;kid_example&#x27;, &#x27;kty&#x27;: &#x27;RSA&#x27;, &#x27;n&#x27;: &#x27;n_example&#x27;, &#x27;use&#x27;: &#x27;sig&#x27;}], &#x27;max_cache_duration_in_hours&#x27;: 56, &#x27;type&#x27;: &#x27;STATIC_KEYS&#x27;, &#x27;uri&#x27;: &#x27;uri_example&#x27;}, &#x27;token_auth_scheme&#x27;: &#x27;token_auth_scheme_example&#x27;, &#x27;token_header&#x27;: &#x27;token_header_example&#x27;, &#x27;token_query_param&#x27;: &#x27;token_query_param_example&#x27;, &#x27;type&#x27;: &#x27;CUSTOM_AUTHENTICATION&#x27;, &#x27;verify_claims&#x27;: [{&#x27;is_required&#x27;: True, &#x27;key&#x27;: &#x27;key_example&#x27;, &#x27;values&#x27;: []}]}, &#x27;cors&#x27;: {&#x27;allowed_headers&#x27;: [], &#x27;allowed_methods&#x27;: [], &#x27;allowed_origins&#x27;: [], &#x27;exposed_headers&#x27;: [], &#x27;is_allow_credentials_enabled&#x27;: True, &#x27;max_age_in_seconds&#x27;: 56}, &#x27;mutual_tls&#x27;: {&#x27;allowed_sans&#x27;: [], &#x27;is_verified_certificate_required&#x27;: True}, &#x27;rate_limiting&#x27;: {&#x27;rate_in_requests_per_second&#x27;: 56, &#x27;rate_key&#x27;: &#x27;CLIENT_IP&#x27;}, &#x27;usage_plans&#x27;: {&#x27;token_locations&#x27;: []}}, &#x27;routes&#x27;: [{&#x27;backend&#x27;: {&#x27;body&#x27;: &#x27;body_example&#x27;, &#x27;connect_timeout_in_seconds&#x27;: 3.4, &#x27;function_id&#x27;: &#x27;ocid1.function.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;headers&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}], &#x27;is_ssl_verify_disabled&#x27;: True, &#x27;read_timeout_in_seconds&#x27;: 3.4, &#x27;send_timeout_in_seconds&#x27;: 3.4, &#x27;status&#x27;: 56, &#x27;type&#x27;: &#x27;ORACLE_FUNCTIONS_BACKEND&#x27;, &#x27;url&#x27;: &#x27;url_example&#x27;}, &#x27;logging_policies&#x27;: {&#x27;access_log&#x27;: {&#x27;is_enabled&#x27;: True}, &#x27;execution_log&#x27;: {&#x27;is_enabled&#x27;: True, &#x27;log_level&#x27;: &#x27;INFO&#x27;}}, &#x27;methods&#x27;: [], &#x27;path&#x27;: &#x27;path_example&#x27;, &#x27;request_policies&#x27;: {&#x27;authorization&#x27;: {&#x27;allowed_scope&#x27;: [], &#x27;type&#x27;: &#x27;ANONYMOUS&#x27;}, &#x27;body_validation&#x27;: {&#x27;content&#x27;: {&#x27;validation_type&#x27;: &#x27;NONE&#x27;}, &#x27;required&#x27;: True, &#x27;validation_mode&#x27;: &#x27;ENFORCING&#x27;}, &#x27;cors&#x27;: {&#x27;allowed_headers&#x27;: [], &#x27;allowed_methods&#x27;: [], &#x27;allowed_origins&#x27;: [], &#x27;exposed_headers&#x27;: [], &#x27;is_allow_credentials_enabled&#x27;: True, &#x27;max_age_in_seconds&#x27;: 56}, &#x27;header_transformations&#x27;: {&#x27;filter_headers&#x27;: {&#x27;items&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;}], &#x27;type&#x27;: &#x27;ALLOW&#x27;}, &#x27;rename_headers&#x27;: {&#x27;items&#x27;: [{&#x27;_from&#x27;: &#x27;_from_example&#x27;, &#x27;to&#x27;: &#x27;to_example&#x27;}]}, &#x27;set_headers&#x27;: {&#x27;items&#x27;: [{&#x27;if_exists&#x27;: &#x27;OVERWRITE&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;values&#x27;: []}]}}, &#x27;header_validations&#x27;: {&#x27;headers&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;required&#x27;: True}], &#x27;validation_mode&#x27;: &#x27;ENFORCING&#x27;}, &#x27;query_parameter_transformations&#x27;: {&#x27;filter_query_parameters&#x27;: {&#x27;items&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;}], &#x27;type&#x27;: &#x27;ALLOW&#x27;}, &#x27;rename_query_parameters&#x27;: {&#x27;items&#x27;: [{&#x27;_from&#x27;: &#x27;_from_example&#x27;, &#x27;to&#x27;: &#x27;to_example&#x27;}]}, &#x27;set_query_parameters&#x27;: {&#x27;items&#x27;: [{&#x27;if_exists&#x27;: &#x27;OVERWRITE&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;values&#x27;: []}]}}, &#x27;query_parameter_validations&#x27;: {&#x27;parameters&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;required&#x27;: True}], &#x27;validation_mode&#x27;: &#x27;ENFORCING&#x27;}, &#x27;response_cache_lookup&#x27;: {&#x27;cache_key_additions&#x27;: [], &#x27;is_enabled&#x27;: True, &#x27;is_private_caching_enabled&#x27;: True, &#x27;type&#x27;: &#x27;SIMPLE_LOOKUP_POLICY&#x27;}}, &#x27;response_policies&#x27;: {&#x27;header_transformations&#x27;: {&#x27;filter_headers&#x27;: {&#x27;items&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;}], &#x27;type&#x27;: &#x27;ALLOW&#x27;}, &#x27;rename_headers&#x27;: {&#x27;items&#x27;: [{&#x27;_from&#x27;: &#x27;_from_example&#x27;, &#x27;to&#x27;: &#x27;to_example&#x27;}]}, &#x27;set_headers&#x27;: {&#x27;items&#x27;: [{&#x27;if_exists&#x27;: &#x27;OVERWRITE&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;values&#x27;: []}]}}, &#x27;response_cache_store&#x27;: {&#x27;time_to_live_in_seconds&#x27;: 56, &#x27;type&#x27;: &#x27;FIXED_TTL_STORE_POLICY&#x27;}}}]}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-deployment/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment in which the resource is created.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-deployment/defined_tags" title="Permalink to this return value"></a>
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
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                            <div>Example: `My new resource`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/endpoint"></div>
                    <b>endpoint</b>
                    <a class="ansibleOptionLink" href="#return-deployment/endpoint" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The endpoint to access this deployment on the gateway.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">endpoint_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-deployment/freeform_tags" title="Permalink to this return value"></a>
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
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/gateway_id"></div>
                    <b>gateway_id</b>
                    <a class="ansibleOptionLink" href="#return-deployment/gateway_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-deployment/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-deployment/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-deployment/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the deployment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/path_prefix"></div>
                    <b>path_prefix</b>
                    <a class="ansibleOptionLink" href="#return-deployment/path_prefix" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A path on which to deploy all routes contained in the API deployment specification. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm'>Deploying an API on an API Gateway by Creating an API Deployment</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_prefix_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification"></div>
                    <b>specification</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification" title="Permalink to this return value"></a>
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
                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/logging_policies"></div>
                    <b>logging_policies</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/logging_policies" title="Permalink to this return value"></a>
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
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/logging_policies/access_log"></div>
                    <b>access_log</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/logging_policies/access_log" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/logging_policies/access_log/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/logging_policies/access_log/is_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to &#x27;access&#x27; in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/logging_policies/execution_log"></div>
                    <b>execution_log</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/logging_policies/execution_log" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/logging_policies/execution_log/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/logging_policies/execution_log/is_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to &#x27;execution&#x27; in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/logging_policies/execution_log/log_level"></div>
                    <b>log_level</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/logging_policies/execution_log/log_level" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies the log level used to control logging output of execution logs. Enabling logging at a given level also enables logging at all higher levels.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">INFO</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies"></div>
                    <b>request_policies</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies" title="Permalink to this return value"></a>
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
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication"></div>
                    <b>authentication</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/audiences"></div>
                    <b>audiences</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/audiences" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of intended recipients for the token.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/function_id"></div>
                    <b>function_id</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/function_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Oracle Functions function resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.function.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/is_anonymous_access_allowed"></div>
                    <b>is_anonymous_access_allowed</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/is_anonymous_access_allowed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether an unauthenticated user may access the API. Must be &quot;true&quot; to enable ANONYMOUS route authorization.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/issuers"></div>
                    <b>issuers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/issuers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of parties that could have issued the token.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/max_clock_skew_in_seconds"></div>
                    <b>max_clock_skew_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/max_clock_skew_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum expected time difference between the system clocks of the token issuer and the API Gateway.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys"></div>
                    <b>public_keys</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/is_ssl_verify_disabled"></div>
                    <b>is_ssl_verify_disabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/is_ssl_verify_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defines whether or not to uphold SSL verification.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys"></div>
                    <b>keys</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The set of static public keys.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/alg"></div>
                    <b>alg</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/alg" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The algorithm intended for use with this key.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">alg_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/e"></div>
                    <b>e</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/e" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The base64 url encoded exponent of the RSA public key represented by this key.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">e_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/format"></div>
                    <b>format</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/format" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The format of the public key.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">JSON_WEB_KEY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The content of the PEM-encoded public key.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/key_ops"></div>
                    <b>key_ops</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/key_ops" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The operations for which this key is to be used.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/kid"></div>
                    <b>kid</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/kid" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A unique key ID. This key will be used to verify the signature of a JWT with matching &quot;kid&quot;.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">kid_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/kty"></div>
                    <b>kty</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/kty" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The key type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">RSA</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/n"></div>
                    <b>n</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/n" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The base64 url encoded modulus of the RSA public key represented by this key.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">n_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/keys/use"></div>
                    <b>use</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/keys/use" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The intended use of the public key.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">sig</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/max_cache_duration_in_hours"></div>
                    <b>max_cache_duration_in_hours</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/max_cache_duration_in_hours" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The duration for which the JWKS should be cached before it is fetched again.</div>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the public key set.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">STATIC_KEYS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/public_keys/uri"></div>
                    <b>uri</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/public_keys/uri" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The uri from which to retrieve the key. It must be accessible without authentication.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">uri_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/token_auth_scheme"></div>
                    <b>token_auth_scheme</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/token_auth_scheme" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The authentication scheme that is to be used when authenticating the token. This must to be provided if &quot;tokenHeader&quot; is specified.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">token_auth_scheme_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/token_header"></div>
                    <b>token_header</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/token_header" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the header containing the authentication token.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">token_header_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/token_query_param"></div>
                    <b>token_query_param</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/token_query_param" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the query parameter containing the authentication token.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">token_query_param_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the authentication policy to use.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CUSTOM_AUTHENTICATION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/verify_claims"></div>
                    <b>verify_claims</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/verify_claims" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of claims which should be validated to consider the token valid.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/verify_claims/is_required"></div>
                    <b>is_required</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/verify_claims/is_required" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the claim is required to be present in the JWT or not. If set to &quot;false&quot;, the claim values will be matched only if the claim is present in the JWT.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/verify_claims/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/verify_claims/key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the claim.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/authentication/verify_claims/values"></div>
                    <b>values</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/authentication/verify_claims/values" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of acceptable values for a given claim. If this value is &quot;null&quot; or empty and &quot;isRequired&quot; set to &quot;true&quot;, then the presence of this claim in the JWT is validated.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/cors"></div>
                    <b>cors</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/cors" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/cors/allowed_headers"></div>
                    <b>allowed_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/cors/allowed_headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header. &#x27;*&#x27; will allow all headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/cors/allowed_methods"></div>
                    <b>allowed_methods</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/cors/allowed_methods" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the Access-Control-Allow-Methods header. &#x27;*&#x27; will allow all methods.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/cors/allowed_origins"></div>
                    <b>allowed_origins</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/cors/allowed_origins" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will send the Access-Control-Allow-Origin header with the best origin match for the circumstances. &#x27;*&#x27; will match any origins, and &#x27;null&#x27; will match queries from &#x27;file:&#x27; origins. All other origins must be qualified with the scheme, full hostname, and port if necessary.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/cors/exposed_headers"></div>
                    <b>exposed_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/cors/exposed_headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers that the client will be allowed to see from the response as indicated by the Access-Control-Expose-Headers header. &#x27;*&#x27; will expose all headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/cors/is_allow_credentials_enabled"></div>
                    <b>is_allow_credentials_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/cors/is_allow_credentials_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/cors/max_age_in_seconds"></div>
                    <b>max_age_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/cors/max_age_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age if greater than 0.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/mutual_tls"></div>
                    <b>mutual_tls</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/mutual_tls" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/mutual_tls/allowed_sans"></div>
                    <b>allowed_sans</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/mutual_tls/allowed_sans" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Allowed list of CN or SAN which will be used for verification of certificate.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/mutual_tls/is_verified_certificate_required"></div>
                    <b>is_verified_certificate_required</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/mutual_tls/is_verified_certificate_required" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Determines whether to enable client verification when API Consumer makes connection to the gateway.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/rate_limiting"></div>
                    <b>rate_limiting</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/rate_limiting" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/rate_limiting/rate_in_requests_per_second"></div>
                    <b>rate_in_requests_per_second</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/rate_limiting/rate_in_requests_per_second" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum number of requests per second to allow.</div>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/rate_limiting/rate_key"></div>
                    <b>rate_key</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/rate_limiting/rate_key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The key used to group requests together.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CLIENT_IP</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/usage_plans"></div>
                    <b>usage_plans</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/usage_plans" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/request_policies/usage_plans/token_locations"></div>
                    <b>token_locations</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/request_policies/usage_plans/token_locations" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of context variables specifying where API tokens may be located in a request. Example locations: - &quot;request.headers[token]&quot; - &quot;request.query[token]&quot; - &quot;request.auth[Token]&quot; - &quot;request.path[TOKEN]&quot;</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes"></div>
                    <b>routes</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of routes that this API exposes.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend"></div>
                    <b>backend</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/body"></div>
                    <b>body</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/body" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The body of the stock response from the mock backend.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">body_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/connect_timeout_in_seconds"></div>
                    <b>connect_timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/connect_timeout_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defines a timeout for establishing a connection with a proxied server.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/function_id"></div>
                    <b>function_id</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/function_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Oracle Functions function resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.function.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/headers"></div>
                    <b>headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The headers of the stock response from the mock backend.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/headers/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/headers/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the header.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/headers/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/headers/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Value of the header.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/is_ssl_verify_disabled"></div>
                    <b>is_ssl_verify_disabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/is_ssl_verify_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defines whether or not to uphold SSL verification.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/read_timeout_in_seconds"></div>
                    <b>read_timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/read_timeout_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defines a timeout for reading a response from the proxied server.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/send_timeout_in_seconds"></div>
                    <b>send_timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/send_timeout_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defines a timeout for transmitting a request to the proxied server.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The status code of the stock response from the mock backend.</div>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the API backend.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ORACLE_FUNCTIONS_BACKEND</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/backend/url"></div>
                    <b>url</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/backend/url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">url_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/logging_policies"></div>
                    <b>logging_policies</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/logging_policies" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/logging_policies/access_log"></div>
                    <b>access_log</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/logging_policies/access_log" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/logging_policies/access_log/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/logging_policies/access_log/is_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to &#x27;access&#x27; in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/logging_policies/execution_log"></div>
                    <b>execution_log</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/logging_policies/execution_log" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/logging_policies/execution_log/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/logging_policies/execution_log/is_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs for an API Deployment. If there is an active log object for the API Deployment and its category is set to &#x27;execution&#x27; in OCI Logging service, the logs will not be uploaded to the legacy OCI Object Storage log archival bucket.</div>
                                            <div>Please note that the functionality to push to the legacy OCI Object Storage log archival bucket has been deprecated and will be removed in the future.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/logging_policies/execution_log/log_level"></div>
                    <b>log_level</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/logging_policies/execution_log/log_level" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies the log level used to control logging output of execution logs. Enabling logging at a given level also enables logging at all higher levels.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">INFO</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/methods"></div>
                    <b>methods</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/methods" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of allowed methods on this route.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/path" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A URL path pattern that must be matched on this route. The path pattern may contain a subset of RFC 6570 identifiers to allow wildcard and parameterized matching.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies"></div>
                    <b>request_policies</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/authorization"></div>
                    <b>authorization</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/authorization" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/authorization/allowed_scope"></div>
                    <b>allowed_scope</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/authorization/allowed_scope" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user whose scope includes any of these access ranges is allowed on this route. Access ranges are case-sensitive.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/authorization/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/authorization/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates how authorization should be applied. For a type of ANY_OF, an &quot;allowedScope&quot; property must also be specified. Otherwise, only a type is required. For a type of ANONYMOUS, an authenticated API must have the &quot;isAnonymousAccessAllowed&quot; property set to &quot;true&quot; in the authentication policy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ANONYMOUS</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/body_validation"></div>
                    <b>body_validation</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/body_validation" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/body_validation/content"></div>
                    <b>content</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/body_validation/content" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The content of the request body. The key is a <a href='https://tools.ietf.org/html/rfc7231#appendix-D'>media type range</a> subset restricted to the following schema</div>
                                            <div>key ::= ( / (  &quot;*&quot; &quot;/&quot; &quot;*&quot; ) / ( type &quot;/&quot; &quot;*&quot; ) / ( type &quot;/&quot; subtype ) )</div>
                                            <div>For requests that match multiple keys, only the most specific key is applicable. e.g. `text/plain` overrides `text/*`</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/body_validation/content/validation_type"></div>
                    <b>validation_type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/body_validation/content/validation_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Validation type defines the content validation method.</div>
                                            <div>Make the validation to first parse the body as the respective format.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NONE</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/body_validation/required"></div>
                    <b>required</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/body_validation/required" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Determines if the request body is required in the request.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/body_validation/validation_mode"></div>
                    <b>validation_mode</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/body_validation/validation_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Validation behavior mode.</div>
                                            <div>In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend.</div>
                                            <div>In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path.</div>
                                            <div>`DISABLED` type turns the validation off.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ENFORCING</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/cors"></div>
                    <b>cors</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/cors" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/cors/allowed_headers"></div>
                    <b>allowed_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/cors/allowed_headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header. &#x27;*&#x27; will allow all headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/cors/allowed_methods"></div>
                    <b>allowed_methods</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/cors/allowed_methods" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the Access-Control-Allow-Methods header. &#x27;*&#x27; will allow all methods.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/cors/allowed_origins"></div>
                    <b>allowed_origins</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/cors/allowed_origins" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will send the Access-Control-Allow-Origin header with the best origin match for the circumstances. &#x27;*&#x27; will match any origins, and &#x27;null&#x27; will match queries from &#x27;file:&#x27; origins. All other origins must be qualified with the scheme, full hostname, and port if necessary.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/cors/exposed_headers"></div>
                    <b>exposed_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/cors/exposed_headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers that the client will be allowed to see from the response as indicated by the Access-Control-Expose-Headers header. &#x27;*&#x27; will expose all headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/cors/is_allow_credentials_enabled"></div>
                    <b>is_allow_credentials_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/cors/is_allow_credentials_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/cors/max_age_in_seconds"></div>
                    <b>max_age_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/cors/max_age_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age if greater than 0.</div>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations"></div>
                    <b>header_transformations</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/filter_headers"></div>
                    <b>filter_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/filter_headers" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/filter_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/filter_headers/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/filter_headers/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/filter_headers/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/filter_headers/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/filter_headers/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW permits only the headers in the list and removes all others, so it acts as an inclusion list.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ALLOW</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/rename_headers"></div>
                    <b>rename_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/rename_headers" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/rename_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/rename_headers/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/rename_headers/items/_from"></div>
                    <b>_from</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/rename_headers/items/_from" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The original case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">_from_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/rename_headers/items/to"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/rename_headers/items/to" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The new name of the header.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">to_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/set_headers"></div>
                    <b>set_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/set_headers" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/set_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/set_headers/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/set_headers/items/if_exists"></div>
                    <b>if_exists</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/set_headers/items/if_exists" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>If a header with the same name already exists in the request, OVERWRITE will overwrite the value, APPEND will append to the existing value, or SKIP will keep the existing value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">OVERWRITE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/set_headers/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/set_headers/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_transformations/set_headers/items/values"></div>
                    <b>values</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_transformations/set_headers/items/values" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of new values.  Each value can be a constant or may include one or more expressions enclosed within ${} delimiters.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_validations"></div>
                    <b>header_validations</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_validations" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_validations/headers"></div>
                    <b>headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_validations/headers" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_validations/headers/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_validations/headers/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Parameter name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_validations/headers/required"></div>
                    <b>required</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_validations/headers/required" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Determines if the header is required in the request.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/header_validations/validation_mode"></div>
                    <b>validation_mode</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/header_validations/validation_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Validation behavior mode.</div>
                                            <div>In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend.</div>
                                            <div>In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path.</div>
                                            <div>`DISABLED` type turns the validation off.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ENFORCING</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations"></div>
                    <b>query_parameter_transformations</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/filter_query_parameters"></div>
                    <b>filter_query_parameters</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/filter_query_parameters" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of query parameters.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The case-sensitive name of the query parameter.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/filter_query_parameters/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list. ALLOW permits only the parameters in the list and removes all others, so it acts as an inclusion list.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ALLOW</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/rename_query_parameters"></div>
                    <b>rename_query_parameters</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/rename_query_parameters" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of query parameters.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items/_from"></div>
                    <b>_from</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items/_from" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The original case-sensitive name of the query parameter.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">_from_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items/to"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/rename_query_parameters/items/to" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The new name of the query parameter.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">to_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters"></div>
                    <b>set_query_parameters</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of query parameters.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/if_exists"></div>
                    <b>if_exists</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/if_exists" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>If a query parameter with the same name already exists in the request, OVERWRITE will overwrite the value, APPEND will append to the existing value, or SKIP will keep the existing value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">OVERWRITE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The case-sensitive name of the query parameter.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/values"></div>
                    <b>values</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_transformations/set_query_parameters/items/values" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of new values.  Each value can be a constant or may include one or more expressions enclosed within ${} delimiters.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_validations"></div>
                    <b>query_parameter_validations</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_validations" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_validations/parameters"></div>
                    <b>parameters</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_validations/parameters" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_validations/parameters/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_validations/parameters/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Parameter name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_validations/parameters/required"></div>
                    <b>required</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_validations/parameters/required" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Determines if the parameter is required in the request.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/query_parameter_validations/validation_mode"></div>
                    <b>validation_mode</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/query_parameter_validations/validation_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Validation behavior mode.</div>
                                            <div>In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response and not sent to the backend.</div>
                                            <div>In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request will follow the normal path.</div>
                                            <div>`DISABLED` type turns the validation off.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ENFORCING</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/response_cache_lookup"></div>
                    <b>response_cache_lookup</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/response_cache_lookup" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/response_cache_lookup/cache_key_additions"></div>
                    <b>cache_key_additions</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/response_cache_lookup/cache_key_additions" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of context expressions whose values will be added to the base cache key. Values should contain an expression enclosed within ${} delimiters. Only the request context is available.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/response_cache_lookup/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/response_cache_lookup/is_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether this policy is currently enabled.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/response_cache_lookup/is_private_caching_enabled"></div>
                    <b>is_private_caching_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/response_cache_lookup/is_private_caching_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Set true to allow caching responses where the request has an Authorization header. Ensure you have configured your cache key additions to get the level of isolation across authenticated requests that you require.</div>
                                            <div>When false, any request with an Authorization header will not be stored in the Response Cache.</div>
                                            <div>If using the CustomAuthenticationPolicy then the tokenHeader/tokenQueryParam are also subject to this check.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/request_policies/response_cache_lookup/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/request_policies/response_cache_lookup/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the Response Cache Store Policy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SIMPLE_LOOKUP_POLICY</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies"></div>
                    <b>response_policies</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations"></div>
                    <b>header_transformations</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/filter_headers"></div>
                    <b>filter_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/filter_headers" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/filter_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/filter_headers/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/filter_headers/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/filter_headers/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/filter_headers/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/filter_headers/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW permits only the headers in the list and removes all others, so it acts as an inclusion list.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ALLOW</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/rename_headers"></div>
                    <b>rename_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/rename_headers" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/rename_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/rename_headers/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/rename_headers/items/_from"></div>
                    <b>_from</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/rename_headers/items/_from" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The original case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">_from_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/rename_headers/items/to"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/rename_headers/items/to" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The new name of the header.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">to_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/set_headers"></div>
                    <b>set_headers</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/set_headers" title="Permalink to this return value"></a>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/set_headers/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/set_headers/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of headers.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/set_headers/items/if_exists"></div>
                    <b>if_exists</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/set_headers/items/if_exists" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>If a header with the same name already exists in the request, OVERWRITE will overwrite the value, APPEND will append to the existing value, or SKIP will keep the existing value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">OVERWRITE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/set_headers/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/set_headers/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The case-insensitive name of the header.  This name must be unique across transformation policies.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/header_transformations/set_headers/items/values"></div>
                    <b>values</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/header_transformations/set_headers/items/values" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of new values.  Each value can be a constant or may include one or more expressions enclosed within ${} delimiters.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/response_cache_store"></div>
                    <b>response_cache_store</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/response_cache_store" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/response_cache_store/time_to_live_in_seconds"></div>
                    <b>time_to_live_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/response_cache_store/time_to_live_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Sets the number of seconds for a response from a backend being stored in the Response Cache before it expires.</div>
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
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deployment/specification/routes/response_policies/response_cache_store/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-deployment/specification/routes/response_policies/response_cache_store/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the Response Cache Store Policy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FIXED_TTL_STORE_POLICY</div>
                                    </td>
            </tr>
                    
                    
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-deployment/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time this resource was created. An RFC3339 formatted datetime string.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="7">
                    <div class="ansibleOptionAnchor" id="return-deployment/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-deployment/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time this resource was last updated. An RFC3339 formatted datetime string.</div>
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

