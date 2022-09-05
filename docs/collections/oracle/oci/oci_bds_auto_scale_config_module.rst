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

.. _ansible_collections.oracle.oci.oci_bds_auto_scale_config_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_bds_auto_scale_config -- Manage a BdsAutoScaleConfig resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 3.0.1).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_bds_auto_scale_config`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a BdsAutoScaleConfig resource in Oracle Cloud Infrastructure
- For *state=present*, add an autoscale configuration to the cluster.


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
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-auto_scaling_configuration_id"></div>
                    <b>auto_scaling_configuration_id</b>
                    <a class="ansibleOptionLink" href="#parameter-auto_scaling_configuration_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique Oracle-assigned identifier of the autoscale configuration.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-bds_instance_id"></div>
                    <b>bds_instance_id</b>
                    <a class="ansibleOptionLink" href="#parameter-bds_instance_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the cluster.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-cluster_admin_password"></div>
                    <b>cluster_admin_password</b>
                    <a class="ansibleOptionLink" href="#parameter-cluster_admin_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Base-64 encoded password for the cluster (and Cloudera Manager) admin user.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for delete using <em>state=absent</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                            <div>The OCID of the compartment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>Required for delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
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
                                            <div>A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_enabled" title="Permalink to this option"></a>
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
                                            <div>Whether the autoscale configuration is enabled.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-node_type"></div>
                    <b>node_type</b>
                    <a class="ansibleOptionLink" href="#parameter-node_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-policy"></div>
                    <b>policy</b>
                    <a class="ansibleOptionLink" href="#parameter-policy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/policy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>THRESHOLD_BASED</li>
                                                                                                                                                                                                <li>SCHEDULE_BASED</li>
                                                                                                                                                                                                <li>NONE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Types of autoscale policies. Options are SCHEDULE-BASED or THRESHOLD-BASED. (Only THRESHOLD-BASED is supported in this release.)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of rules for autoscaling. If an action has multiple rules, the last rule in the array will be applied.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy/rules/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/rules/action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CHANGE_SHAPE_SCALE_UP</li>
                                                                                                                                                                                                <li>CHANGE_SHAPE_SCALE_DOWN</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The valid value are CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy/rules/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/rules/metric" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy/rules/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/rules/metric/metric_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CPU_UTILIZATION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy/rules/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/rules/metric/threshold" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy/rules/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/rules/metric/threshold/duration_in_minutes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy/rules/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/rules/metric/threshold/operator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GT</li>
                                                                                                                                                                                                <li>LT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy/rules/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-policy/rules/metric/threshold/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                                        </td>
            </tr>
                    
                    
                    
                    
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details"></div>
                    <b>policy_details</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/policy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>METRIC_BASED_HORIZONTAL_SCALING_POLICY</li>
                                                                                                                                                                                                <li>SCHEDULE_BASED_VERTICAL_SCALING_POLICY</li>
                                                                                                                                                                                                <li>SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY</li>
                                                                                                                                                                                                <li>METRIC_BASED_VERTICAL_SCALING_POLICY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of autoscaling policy.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config"></div>
                    <b>scale_down_config</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/memory_step_size"></div>
                    <b>memory_step_size</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/memory_step_size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the size of memory in GBs to remove from each node during a scale-down event. This value is not used for nodes with fixed compute shapes.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/metric" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/metric/metric_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CPU_UTILIZATION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/metric/threshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/metric/threshold/duration_in_minutes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/metric/threshold/operator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GT</li>
                                                                                                                                                                                                <li>LT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/metric/threshold/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/min_memory_per_node"></div>
                    <b>min_memory_per_node</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/min_memory_per_node" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the minimum memory in GBs each node can be scaled-down to. This value is not used for nodes with fixed compute shapes.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/min_ocpus_per_node"></div>
                    <b>min_ocpus_per_node</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/min_ocpus_per_node" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the minimum number of OCPUs each node can be scaled-down to. This value is not used for nodes with fixed compute shapes.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_down_config/ocpu_step_size"></div>
                    <b>ocpu_step_size</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_down_config/ocpu_step_size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the number of OCPUs to remove from each node during a scale-down event. This value is not used for nodes with fixed compute shapes.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config"></div>
                    <b>scale_in_config</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config/metric" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config/metric/metric_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CPU_UTILIZATION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config/metric/threshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config/metric/threshold/duration_in_minutes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config/metric/threshold/operator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GT</li>
                                                                                                                                                                                                <li>LT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config/metric/threshold/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config/min_node_count"></div>
                    <b>min_node_count</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config/min_node_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the minimum number of nodes the cluster can be scaled-in to.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_in_config/step_size"></div>
                    <b>step_size</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_in_config/step_size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the number of nodes to remove during a scale-in event.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config"></div>
                    <b>scale_out_config</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config/max_node_count"></div>
                    <b>max_node_count</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config/max_node_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the maximum number of nodes the cluster can be scaled-out to.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config/metric" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config/metric/metric_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CPU_UTILIZATION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config/metric/threshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config/metric/threshold/duration_in_minutes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config/metric/threshold/operator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GT</li>
                                                                                                                                                                                                <li>LT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config/metric/threshold/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_out_config/step_size"></div>
                    <b>step_size</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_out_config/step_size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the number of nodes to add during a scale-out event.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_HORIZONTAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config"></div>
                    <b>scale_up_config</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/max_memory_per_node"></div>
                    <b>max_memory_per_node</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/max_memory_per_node" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the maximum memory in GBs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/max_ocpus_per_node"></div>
                    <b>max_ocpus_per_node</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/max_ocpus_per_node" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the maximum number of OCPUs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/memory_step_size"></div>
                    <b>memory_step_size</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/memory_step_size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the size of memory in GBs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/metric" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/metric/metric_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CPU_UTILIZATION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/metric/threshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/metric/threshold/duration_in_minutes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/metric/threshold/operator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GT</li>
                                                                                                                                                                                                <li>LT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/metric/threshold/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                            <div>Required when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/scale_up_config/ocpu_step_size"></div>
                    <b>ocpu_step_size</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/scale_up_config/ocpu_step_size" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the number of OCPUs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.</div>
                                            <div>Applicable when policy_type is &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details"></div>
                    <b>schedule_details</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when policy_type is one of [&#x27;SCHEDULE_BASED_VERTICAL_SCALING_POLICY&#x27;, &#x27;SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/schedule_type"></div>
                    <b>schedule_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/schedule_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DAY_BASED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of schedule.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/time_and_horizontal_scaling_config"></div>
                    <b>time_and_horizontal_scaling_config</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/time_and_horizontal_scaling_config" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/time_and_horizontal_scaling_config/target_node_count"></div>
                    <b>target_node_count</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/time_and_horizontal_scaling_config/target_node_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This value is the desired number of nodes in the cluster.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/time_and_horizontal_scaling_config/time_recurrence"></div>
                    <b>time_recurrence</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/time_and_horizontal_scaling_config/time_recurrence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE fields. Other fields are not supported.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/time_and_vertical_scaling_config"></div>
                    <b>time_and_vertical_scaling_config</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/time_and_vertical_scaling_config" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/time_and_vertical_scaling_config/target_memory_per_node"></div>
                    <b>target_memory_per_node</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/time_and_vertical_scaling_config/target_memory_per_node" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster- plan-shape'>flexible compute shapes</a>, this value is the desired memory in GBs on each node. This value is not used for nodes with fixed compute shapes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/time_and_vertical_scaling_config/target_ocpus_per_node"></div>
                    <b>target_ocpus_per_node</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/time_and_vertical_scaling_config/target_ocpus_per_node" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster- plan-shape'>flexible compute shapes</a>, this value is the desired OCPUs count on each node. This value is not used for nodes with fixed compute shapes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/time_and_vertical_scaling_config/target_shape"></div>
                    <b>target_shape</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/time_and_vertical_scaling_config/target_shape" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>fixed compute shapes</a>, this value is the desired shape of each node. This value is not used for nodes with flexible compute shapes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/schedule_details/time_and_vertical_scaling_config/time_recurrence"></div>
                    <b>time_recurrence</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/schedule_details/time_and_vertical_scaling_config/time_recurrence" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE fields. Other fields are not supported.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy_details/timezone"></div>
                    <b>timezone</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_details/timezone" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The time zone of the execution schedule, in IANA time zone database name format</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when policy_type is one of [&#x27;SCHEDULE_BASED_VERTICAL_SCALING_POLICY&#x27;, &#x27;SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY&#x27;]</div>
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
                                            <div>The state of the BdsAutoScaleConfig.</div>
                                            <div>Use <em>state=present</em> to create or update a BdsAutoScaleConfig.</div>
                                            <div>Use <em>state=absent</em> to delete a BdsAutoScaleConfig.</div>
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

    
    - name: Create bds_auto_scale_config
      oci_bds_auto_scale_config:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        node_type: node_type_example
        is_enabled: true
        bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_admin_password: example-password

        # optional
        display_name: display_name_example
        policy:
          # required
          policy_type: THRESHOLD_BASED
          rules:
          - # required
            action: CHANGE_SHAPE_SCALE_UP
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
        policy_details:
          # required
          policy_type: METRIC_BASED_HORIZONTAL_SCALING_POLICY

          # optional
          scale_out_config:
            # optional
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
            max_node_count: 56
            step_size: 56
          scale_in_config:
            # optional
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
            min_node_count: 56
            step_size: 56

    - name: Update bds_auto_scale_config
      oci_bds_auto_scale_config:
        # required
        bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
        auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example
        is_enabled: true
        policy:
          # required
          policy_type: THRESHOLD_BASED
          rules:
          - # required
            action: CHANGE_SHAPE_SCALE_UP
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
        policy_details:
          # required
          policy_type: METRIC_BASED_HORIZONTAL_SCALING_POLICY

          # optional
          scale_out_config:
            # optional
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
            max_node_count: 56
            step_size: 56
          scale_in_config:
            # optional
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
            min_node_count: 56
            step_size: 56
        cluster_admin_password: example-password

    - name: Update bds_auto_scale_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_bds_auto_scale_config:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        is_enabled: true
        policy:
          # required
          policy_type: THRESHOLD_BASED
          rules:
          - # required
            action: CHANGE_SHAPE_SCALE_UP
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
        policy_details:
          # required
          policy_type: METRIC_BASED_HORIZONTAL_SCALING_POLICY

          # optional
          scale_out_config:
            # optional
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
            max_node_count: 56
            step_size: 56
          scale_in_config:
            # optional
            metric:
              # required
              metric_type: CPU_UTILIZATION
              threshold:
                # required
                duration_in_minutes: 56
                operator: GT
                value: 56
            min_node_count: 56
            step_size: 56
        cluster_admin_password: example-password

    - name: Delete bds_auto_scale_config
      oci_bds_auto_scale_config:
        # required
        bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
        auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_admin_password: example-password
        state: absent

    - name: Delete bds_auto_scale_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_bds_auto_scale_config:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config"></div>
                    <b>bds_auto_scale_config</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the BdsAutoScaleConfig resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;node_type&#x27;: &#x27;node_type_example&#x27;, &#x27;policy&#x27;: {&#x27;policy_type&#x27;: &#x27;THRESHOLD_BASED&#x27;, &#x27;rules&#x27;: [{&#x27;action&#x27;: &#x27;CHANGE_SHAPE_SCALE_UP&#x27;, &#x27;metric&#x27;: {&#x27;metric_type&#x27;: &#x27;CPU_UTILIZATION&#x27;, &#x27;threshold&#x27;: {&#x27;duration_in_minutes&#x27;: 56, &#x27;operator&#x27;: &#x27;GT&#x27;, &#x27;value&#x27;: 56}}}]}, &#x27;policy_details&#x27;: {&#x27;action_type&#x27;: &#x27;VERTICAL_SCALING&#x27;, &#x27;policy_type&#x27;: &#x27;METRIC_BASED_VERTICAL_SCALING_POLICY&#x27;, &#x27;scale_down_config&#x27;: {&#x27;memory_step_size&#x27;: 56, &#x27;metric&#x27;: {&#x27;metric_type&#x27;: &#x27;CPU_UTILIZATION&#x27;, &#x27;threshold&#x27;: {&#x27;duration_in_minutes&#x27;: 56, &#x27;operator&#x27;: &#x27;GT&#x27;, &#x27;value&#x27;: 56}}, &#x27;min_memory_per_node&#x27;: 56, &#x27;min_ocpus_per_node&#x27;: 56, &#x27;ocpu_step_size&#x27;: 56}, &#x27;scale_in_config&#x27;: {&#x27;metric&#x27;: {&#x27;metric_type&#x27;: &#x27;CPU_UTILIZATION&#x27;, &#x27;threshold&#x27;: {&#x27;duration_in_minutes&#x27;: 56, &#x27;operator&#x27;: &#x27;GT&#x27;, &#x27;value&#x27;: 56}}, &#x27;min_node_count&#x27;: 56, &#x27;step_size&#x27;: 56}, &#x27;scale_out_config&#x27;: {&#x27;max_node_count&#x27;: 56, &#x27;metric&#x27;: {&#x27;metric_type&#x27;: &#x27;CPU_UTILIZATION&#x27;, &#x27;threshold&#x27;: {&#x27;duration_in_minutes&#x27;: 56, &#x27;operator&#x27;: &#x27;GT&#x27;, &#x27;value&#x27;: 56}}, &#x27;step_size&#x27;: 56}, &#x27;scale_up_config&#x27;: {&#x27;max_memory_per_node&#x27;: 56, &#x27;max_ocpus_per_node&#x27;: 56, &#x27;memory_step_size&#x27;: 56, &#x27;metric&#x27;: {&#x27;metric_type&#x27;: &#x27;CPU_UTILIZATION&#x27;, &#x27;threshold&#x27;: {&#x27;duration_in_minutes&#x27;: 56, &#x27;operator&#x27;: &#x27;GT&#x27;, &#x27;value&#x27;: 56}}, &#x27;ocpu_step_size&#x27;: 56}, &#x27;schedule_details&#x27;: [{&#x27;schedule_type&#x27;: &#x27;DAY_BASED&#x27;, &#x27;time_and_horizontal_scaling_config&#x27;: [{&#x27;target_node_count&#x27;: 56, &#x27;time_recurrence&#x27;: &#x27;time_recurrence_example&#x27;}], &#x27;time_and_vertical_scaling_config&#x27;: [{&#x27;target_memory_per_node&#x27;: 56, &#x27;target_ocpus_per_node&#x27;: 56, &#x27;target_shape&#x27;: &#x27;target_shape_example&#x27;, &#x27;time_recurrence&#x27;: &#x27;time_recurrence_example&#x27;}]}], &#x27;timezone&#x27;: &#x27;timezone_example&#x27;, &#x27;trigger_type&#x27;: &#x27;METRIC_BASED&#x27;}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The unique identifier for the autoscale configuration.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The state of the autoscale configuration.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/node_type"></div>
                    <b>node_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/node_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">node_type_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy"></div>
                    <b>policy</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/policy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Types of autoscale policies. Options are SCHEDULE-BASED or THRESHOLD-BASED. (Only THRESHOLD-BASED is supported in this release.)</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">THRESHOLD_BASED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of rules for autoscaling. If an action has multiple rules, the last rule in the array will be applied.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/rules/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/rules/action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The valid value are CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CHANGE_SHAPE_SCALE_UP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/rules/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/rules/metric" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/rules/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/rules/metric/metric_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CPU_UTILIZATION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/rules/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/rules/metric/threshold" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/rules/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/rules/metric/threshold/duration_in_minutes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/rules/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/rules/metric/threshold/operator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy/rules/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy/rules/metric/threshold/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                    
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details"></div>
                    <b>policy_details</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details" title="Permalink to this return value"></a>
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
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/action_type"></div>
                    <b>action_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/action_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of autoscaling action to take.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">VERTICAL_SCALING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/policy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of autoscaling policy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">METRIC_BASED_VERTICAL_SCALING_POLICY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config"></div>
                    <b>scale_down_config</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/memory_step_size"></div>
                    <b>memory_step_size</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/memory_step_size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the size of memory in GBs to remove from each node during a scale-down event. This value is not used for nodes with fixed compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/metric" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/metric/metric_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CPU_UTILIZATION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/metric/threshold" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/metric/threshold/duration_in_minutes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/metric/threshold/operator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/metric/threshold/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/min_memory_per_node"></div>
                    <b>min_memory_per_node</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/min_memory_per_node" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the minimum memory in GBs each node can be scaled-down to. This value is not used for nodes with fixed compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/min_ocpus_per_node"></div>
                    <b>min_ocpus_per_node</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/min_ocpus_per_node" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the minimum number of OCPUs each node can be scaled-down to. This value is not used for nodes with fixed compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_down_config/ocpu_step_size"></div>
                    <b>ocpu_step_size</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_down_config/ocpu_step_size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the number of OCPUs to remove from each node during a scale-down event. This value is not used for nodes with fixed compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config"></div>
                    <b>scale_in_config</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config/metric" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config/metric/metric_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CPU_UTILIZATION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config/metric/threshold" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config/metric/threshold/duration_in_minutes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config/metric/threshold/operator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config/metric/threshold/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config/min_node_count"></div>
                    <b>min_node_count</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config/min_node_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the minimum number of nodes the cluster can be scaled-in to.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_in_config/step_size"></div>
                    <b>step_size</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_in_config/step_size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the number of nodes to remove during a scale-in event.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config"></div>
                    <b>scale_out_config</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config/max_node_count"></div>
                    <b>max_node_count</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config/max_node_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the maximum number of nodes the cluster can be scaled-out to.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config/metric" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config/metric/metric_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CPU_UTILIZATION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config/metric/threshold" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config/metric/threshold/duration_in_minutes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config/metric/threshold/operator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config/metric/threshold/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_out_config/step_size"></div>
                    <b>step_size</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_out_config/step_size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the number of nodes to add during a scale-out event.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config"></div>
                    <b>scale_up_config</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/max_memory_per_node"></div>
                    <b>max_memory_per_node</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/max_memory_per_node" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the maximum memory in GBs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/max_ocpus_per_node"></div>
                    <b>max_ocpus_per_node</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/max_ocpus_per_node" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the maximum number of OCPUs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/memory_step_size"></div>
                    <b>memory_step_size</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/memory_step_size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the size of memory in GBs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/metric" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/metric/metric_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Allowed value is CPU_UTILIZATION.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CPU_UTILIZATION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/metric/threshold" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/metric/threshold/duration_in_minutes"></div>
                    <b>duration_in_minutes</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/metric/threshold/duration_in_minutes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the minimum period of time the metric value exceeds the threshold value before the action is triggered. The value is in minutes.</div>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/metric/threshold/operator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The comparison operator to use. Options are greater than (GT) or less than (LT).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/metric/threshold/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Integer non-negative value. 0 &lt; value &lt; 100</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/scale_up_config/ocpu_step_size"></div>
                    <b>ocpu_step_size</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/scale_up_config/ocpu_step_size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan- shape'>flexible compute shapes</a>, this value is the number of OCPUs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details"></div>
                    <b>schedule_details</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/schedule_type"></div>
                    <b>schedule_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/schedule_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of schedule.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">DAY_BASED</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/time_and_horizontal_scaling_config"></div>
                    <b>time_and_horizontal_scaling_config</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/time_and_horizontal_scaling_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/time_and_horizontal_scaling_config/target_node_count"></div>
                    <b>target_node_count</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/time_and_horizontal_scaling_config/target_node_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>This value is the desired number of nodes in the cluster.</div>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/time_and_horizontal_scaling_config/time_recurrence"></div>
                    <b>time_recurrence</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/time_and_horizontal_scaling_config/time_recurrence" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE fields. Other fields are not supported.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">time_recurrence_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config"></div>
                    <b>time_and_vertical_scaling_config</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config/target_memory_per_node"></div>
                    <b>target_memory_per_node</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config/target_memory_per_node" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create- cluster.htm#cluster-plan-shape'>flexible compute shapes</a>, this value is the desired memory in GBs on each node. This value is not used for nodes with fixed compute shapes.</div>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config/target_ocpus_per_node"></div>
                    <b>target_ocpus_per_node</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config/target_ocpus_per_node" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create- cluster.htm#cluster-plan-shape'>flexible compute shapes</a>, this value is the desired OCPUs count on each node. This value is not used for nodes with fixed compute shapes.</div>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config/target_shape"></div>
                    <b>target_shape</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config/target_shape" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For nodes with <a href='https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster- plan-shape'>fixed compute shapes</a>, this value is the desired shape of each node. This value is not used for nodes with flexible compute shapes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">target_shape_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config/time_recurrence"></div>
                    <b>time_recurrence</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/schedule_details/time_and_vertical_scaling_config/time_recurrence" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE fields. Other fields are not supported.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">time_recurrence_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/timezone"></div>
                    <b>timezone</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/timezone" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time zone of the execution schedule, in IANA time zone database name format</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">timezone_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/policy_details/trigger_type"></div>
                    <b>trigger_type</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/policy_details/trigger_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of autoscaling trigger.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">METRIC_BASED</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the cluster was created, shown as an RFC 3339 formatted datetime string.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-bds_auto_scale_config/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-bds_auto_scale_config/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the autoscale configuration was updated, shown as an RFC 3339 formatted datetime string.</div>
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

