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

.. _ansible_collections.oracle.oci.oci_devops_deploy_stage_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_devops_deploy_stage -- Manage a DeployStage resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.13.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_devops_deploy_stage`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a DeployStage resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new deployment stage.


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
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-approval_policy"></div>
                    <b>approval_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-approval_policy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL&#x27;, &#x27;MANUAL_APPROVAL&#x27;, &#x27;OKE_CANARY_APPROVAL&#x27;]</div>
                                            <div>Required when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL&#x27;, &#x27;MANUAL_APPROVAL&#x27;, &#x27;OKE_CANARY_APPROVAL&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-approval_policy/approval_policy_type"></div>
                    <b>approval_policy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-approval_policy/approval_policy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>COUNT_BASED_APPROVAL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Approval policy type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-approval_policy/number_of_approvals_required"></div>
                    <b>number_of_approvals_required</b>
                    <a class="ansibleOptionLink" href="#parameter-approval_policy/number_of_approvals_required" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A minimum number of approvals required for stage to proceed.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-are_hooks_enabled"></div>
                    <b>are_hooks_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-are_hooks_enabled" title="Permalink to this option"></a>
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
                                            <div>Disable pre/post upgrade hooks. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-blue_backend_ips"></div>
                    <b>blue_backend_ips</b>
                    <a class="ansibleOptionLink" href="#parameter-blue_backend_ips" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-blue_backend_ips/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-blue_backend_ips/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IP address of the backend server. A server could be a compute instance or a load balancer.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-blue_green_strategy"></div>
                    <b>blue_green_strategy</b>
                    <a class="ansibleOptionLink" href="#parameter-blue_green_strategy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_BLUE_GREEN_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-blue_green_strategy/ingress_name"></div>
                    <b>ingress_name</b>
                    <a class="ansibleOptionLink" href="#parameter-blue_green_strategy/ingress_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the Ingress resource.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-blue_green_strategy/namespace_a"></div>
                    <b>namespace_a</b>
                    <a class="ansibleOptionLink" href="#parameter-blue_green_strategy/namespace_a" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Namespace A for deployment. Example: namespaceA - first Namespace name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-blue_green_strategy/namespace_b"></div>
                    <b>namespace_b</b>
                    <a class="ansibleOptionLink" href="#parameter-blue_green_strategy/namespace_b" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Namespace B for deployment. Example: namespaceB - second Namespace name.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-blue_green_strategy/strategy_type"></div>
                    <b>strategy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-blue_green_strategy/strategy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NGINX_BLUE_GREEN_STRATEGY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Blue-Green strategy type.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-canary_strategy"></div>
                    <b>canary_strategy</b>
                    <a class="ansibleOptionLink" href="#parameter-canary_strategy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_CANARY_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-canary_strategy/ingress_name"></div>
                    <b>ingress_name</b>
                    <a class="ansibleOptionLink" href="#parameter-canary_strategy/ingress_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the Ingress resource.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-canary_strategy/namespace"></div>
                    <b>namespace</b>
                    <a class="ansibleOptionLink" href="#parameter-canary_strategy/namespace" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Canary namespace to be used for Kubernetes canary deployment. Example: canary - Name of the Canary namespace.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-canary_strategy/strategy_type"></div>
                    <b>strategy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-canary_strategy/strategy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NGINX_CANARY_STRATEGY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Canary strategy type.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-command_spec_deploy_artifact_id"></div>
                    <b>command_spec_deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#parameter-command_spec_deploy_artifact_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the artifact that contains the command specification.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;SHELL&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;SHELL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-compute_instance_group_blue_green_deployment_deploy_stage_id"></div>
                    <b>compute_instance_group_blue_green_deployment_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compute_instance_group_blue_green_deployment_deploy_stage_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-compute_instance_group_canary_deploy_stage_id"></div>
                    <b>compute_instance_group_canary_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compute_instance_group_canary_deploy_stage_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A compute instance group canary stage OCID for load balancer.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-compute_instance_group_canary_traffic_shift_deploy_stage_id"></div>
                    <b>compute_instance_group_canary_traffic_shift_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compute_instance_group_canary_traffic_shift_deploy_stage_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A compute instance group canary traffic shift stage OCID for load balancer.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-compute_instance_group_deploy_environment_id"></div>
                    <b>compute_instance_group_deploy_environment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compute_instance_group_deploy_environment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A compute instance group environment OCID for Canary deployment.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;</div>
                                            <div>Required when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-config"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User provided key and value pair configuration, which is assigned through constants or parameter.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;DEPLOY_FUNCTION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-container_config"></div>
                    <b>container_config</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;SHELL&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;SHELL&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/availability_domain"></div>
                    <b>availability_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/availability_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Availability domain where the ContainerInstance will be created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the compartment where the ContainerInstance will be created.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/container_config_type"></div>
                    <b>container_config_type</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/container_config_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CONTAINER_INSTANCE_CONFIG</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Container configuration type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/network_channel"></div>
                    <b>network_channel</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/network_channel" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/network_channel/network_channel_type"></div>
                    <b>network_channel_type</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/network_channel/network_channel_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SERVICE_VNIC_CHANNEL</li>
                                                                                                                                                                                                <li>PRIVATE_ENDPOINT_CHANNEL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Network channel type.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/network_channel/nsg_ids"></div>
                    <b>nsg_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/network_channel/nsg_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of network security group OCIDs.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/network_channel/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/network_channel/subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the subnet where private resources exist.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/shape_config"></div>
                    <b>shape_config</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/shape_config" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/shape_config/memory_in_gbs"></div>
                    <b>memory_in_gbs</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/shape_config/memory_in_gbs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The total amount of memory available to the instance, in gigabytes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/shape_config/ocpus"></div>
                    <b>ocpus</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/shape_config/ocpus" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The total number of OCPUs available to the instance.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-container_config/shape_name"></div>
                    <b>shape_name</b>
                    <a class="ansibleOptionLink" href="#parameter-container_config/shape_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The shape of the ContainerInstance. The shape determines the resources available to the ContainerInstance.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_artifact_id"></div>
                    <b>deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_artifact_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage&#x27;s execution. If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace the placeholders in the artifact content.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;INVOKE_FUNCTION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_artifact_ids"></div>
                    <b>deploy_artifact_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_artifact_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of file artifact OCIDs to deploy.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_environment_id_a"></div>
                    <b>deploy_environment_id_a</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_environment_id_a" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>First compute instance group environment OCID for deployment.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_environment_id_b"></div>
                    <b>deploy_environment_id_b</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_environment_id_b" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Second compute instance group environment OCID for deployment.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_pipeline_id"></div>
                    <b>deploy_pipeline_id</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_pipeline_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of a pipeline.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_stage_id"></div>
                    <b>deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_stage_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique stage identifier.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_stage_predecessor_collection"></div>
                    <b>deploy_stage_predecessor_collection</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_stage_predecessor_collection" title="Permalink to this option"></a>
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
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT&#x27;, &#x27;OKE_BLUE_GREEN_TRAFFIC_SHIFT&#x27;, &#x27;SHELL&#x27;, &#x27;OKE_DEPLOYMENT&#x27;, &#x27;DEPLOY_FUNCTION&#x27;, &#x27;OKE_CANARY_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;, &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;, &#x27;OKE_BLUE_GREEN_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT&#x27;, &#x27;OKE_CANARY_APPROVAL&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;, &#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL&#x27;, &#x27;MANUAL_APPROVAL&#x27;, &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;, &#x27;WAIT&#x27;, &#x27;INVOKE_FUNCTION&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_stage_predecessor_collection/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_stage_predecessor_collection/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of stage predecessors for a stage.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_stage_predecessor_collection/items/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_stage_predecessor_collection/items/id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline&#x27;s OCID.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deploy_stage_type"></div>
                    <b>deploy_stage_type</b>
                    <a class="ansibleOptionLink" href="#parameter-deploy_stage_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OKE_CANARY_TRAFFIC_SHIFT</li>
                                                                                                                                                                                                <li>OKE_BLUE_GREEN_TRAFFIC_SHIFT</li>
                                                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT</li>
                                                                                                                                                                                                <li>WAIT</li>
                                                                                                                                                                                                <li>LOAD_BALANCER_TRAFFIC_SHIFT</li>
                                                                                                                                                                                                <li>SHELL</li>
                                                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT</li>
                                                                                                                                                                                                <li>OKE_BLUE_GREEN_DEPLOYMENT</li>
                                                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT</li>
                                                                                                                                                                                                <li>INVOKE_FUNCTION</li>
                                                                                                                                                                                                <li>DEPLOY_FUNCTION</li>
                                                                                                                                                                                                <li>OKE_CANARY_DEPLOYMENT</li>
                                                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT</li>
                                                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL</li>
                                                                                                                                                                                                <li>OKE_HELM_CHART_DEPLOYMENT</li>
                                                                                                                                                                                                <li>MANUAL_APPROVAL</li>
                                                                                                                                                                                                <li>OKE_DEPLOYMENT</li>
                                                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT</li>
                                                                                                                                                                                                <li>OKE_CANARY_APPROVAL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Deployment stage type.</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with deploy_stage_id present.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-deployment_spec_deploy_artifact_id"></div>
                    <b>deployment_spec_deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#parameter-deployment_spec_deploy_artifact_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the artifact that contains the deployment specification.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                            <div>Required when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                            <div>Optional description about the deployment stage.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                            <div>Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.</div>
                                            <div>Required for create, update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-docker_image_deploy_artifact_id"></div>
                    <b>docker_image_deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#parameter-docker_image_deploy_artifact_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A Docker image artifact OCID.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;DEPLOY_FUNCTION&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;DEPLOY_FUNCTION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-failure_policy"></div>
                    <b>failure_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-failure_policy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-failure_policy/failure_count"></div>
                    <b>failure_count</b>
                    <a class="ansibleOptionLink" href="#parameter-failure_policy/failure_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The threshold count of failed instances in the group, which when reached or exceeded sets the stage as Failed.</div>
                                            <div>Required when policy_type is &#x27;COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-failure_policy/failure_percentage"></div>
                    <b>failure_percentage</b>
                    <a class="ansibleOptionLink" href="#parameter-failure_policy/failure_percentage" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The failure percentage threshold, which when reached or exceeded sets the stage as Failed. Percentage is computed as the ceiling value of the number of failed instances over the total count of the instances in the group.</div>
                                            <div>Required when policy_type is &#x27;COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-failure_policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-failure_policy/policy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE</li>
                                                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies if the failure instance size is given by absolute number or by percentage.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-function_deploy_environment_id"></div>
                    <b>function_deploy_environment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-function_deploy_environment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Function environment OCID.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;DEPLOY_FUNCTION&#x27;, &#x27;INVOKE_FUNCTION&#x27;]</div>
                                            <div>Required when deploy_stage_type is one of [&#x27;DEPLOY_FUNCTION&#x27;, &#x27;INVOKE_FUNCTION&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-function_timeout_in_seconds"></div>
                    <b>function_timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-function_timeout_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Timeout for execution of the Function. Value in seconds.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;DEPLOY_FUNCTION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-green_backend_ips"></div>
                    <b>green_backend_ips</b>
                    <a class="ansibleOptionLink" href="#parameter-green_backend_ips" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-green_backend_ips/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-green_backend_ips/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IP address of the backend server. A server could be a compute instance or a load balancer.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-helm_chart_deploy_artifact_id"></div>
                    <b>helm_chart_deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#parameter-helm_chart_deploy_artifact_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Helm chart artifact OCID.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-is_async"></div>
                    <b>is_async</b>
                    <a class="ansibleOptionLink" href="#parameter-is_async" title="Permalink to this option"></a>
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
                                            <div>A boolean flag specifies whether this stage executes asynchronously.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;INVOKE_FUNCTION&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;INVOKE_FUNCTION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-is_debug_enabled"></div>
                    <b>is_debug_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_debug_enabled" title="Permalink to this option"></a>
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
                                            <div>Enables helm --debug option to stream output to tf stdout. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-is_force_enabled"></div>
                    <b>is_force_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_force_enabled" title="Permalink to this option"></a>
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
                                            <div>Force resource update through delete; or if required, recreate. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-is_validation_enabled"></div>
                    <b>is_validation_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_validation_enabled" title="Permalink to this option"></a>
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
                                            <div>A boolean flag specifies whether the invoked function should be validated.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;INVOKE_FUNCTION&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;INVOKE_FUNCTION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-kubernetes_manifest_deploy_artifact_ids"></div>
                    <b>kubernetes_manifest_deploy_artifact_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-kubernetes_manifest_deploy_artifact_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of Kubernetes manifest artifact OCIDs.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;OKE_DEPLOYMENT&#x27;, &#x27;OKE_CANARY_DEPLOYMENT&#x27;, &#x27;OKE_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                            <div>Required when deploy_stage_type is one of [&#x27;OKE_DEPLOYMENT&#x27;, &#x27;OKE_CANARY_DEPLOYMENT&#x27;, &#x27;OKE_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-load_balancer_config"></div>
                    <b>load_balancer_config</b>
                    <a class="ansibleOptionLink" href="#parameter-load_balancer_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;]</div>
                                            <div>Required when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-load_balancer_config/backend_port"></div>
                    <b>backend_port</b>
                    <a class="ansibleOptionLink" href="#parameter-load_balancer_config/backend_port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Listen port for the backend server.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-load_balancer_config/listener_name"></div>
                    <b>listener_name</b>
                    <a class="ansibleOptionLink" href="#parameter-load_balancer_config/listener_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the load balancer listener.</div>
                                            <div>Required when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-load_balancer_config/load_balancer_id"></div>
                    <b>load_balancer_id</b>
                    <a class="ansibleOptionLink" href="#parameter-load_balancer_config/load_balancer_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the load balancer.</div>
                                            <div>Required when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-max_history"></div>
                    <b>max_history</b>
                    <a class="ansibleOptionLink" href="#parameter-max_history" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Limit the maximum number of revisions saved per release. Use 0 for no limit. Set to 10 by default</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-max_memory_in_mbs"></div>
                    <b>max_memory_in_mbs</b>
                    <a class="ansibleOptionLink" href="#parameter-max_memory_in_mbs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum usable memory for the Function (in MB).</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;DEPLOY_FUNCTION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-namespace"></div>
                    <b>namespace</b>
                    <a class="ansibleOptionLink" href="#parameter-namespace" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Default namespace to be used for Kubernetes deployment when not specified in the manifest.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;OKE_DEPLOYMENT&#x27;, &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-oke_blue_green_deploy_stage_id"></div>
                    <b>oke_blue_green_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#parameter-oke_blue_green_deploy_stage_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the upstream OKE blue-green deployment stage in this pipeline.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_BLUE_GREEN_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-oke_canary_deploy_stage_id"></div>
                    <b>oke_canary_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#parameter-oke_canary_deploy_stage_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of an upstream OKE canary deployment stage in this pipeline.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-oke_canary_traffic_shift_deploy_stage_id"></div>
                    <b>oke_canary_traffic_shift_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#parameter-oke_canary_traffic_shift_deploy_stage_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_CANARY_APPROVAL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-oke_cluster_deploy_environment_id"></div>
                    <b>oke_cluster_deploy_environment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-oke_cluster_deploy_environment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Kubernetes cluster environment OCID for deployment.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;OKE_DEPLOYMENT&#x27;, &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;]</div>
                                            <div>Required when deploy_stage_type is one of [&#x27;OKE_DEPLOYMENT&#x27;, &#x27;OKE_CANARY_DEPLOYMENT&#x27;, &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;, &#x27;OKE_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-production_load_balancer_config"></div>
                    <b>production_load_balancer_config</b>
                    <a class="ansibleOptionLink" href="#parameter-production_load_balancer_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-production_load_balancer_config/backend_port"></div>
                    <b>backend_port</b>
                    <a class="ansibleOptionLink" href="#parameter-production_load_balancer_config/backend_port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Listen port for the backend server.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-production_load_balancer_config/listener_name"></div>
                    <b>listener_name</b>
                    <a class="ansibleOptionLink" href="#parameter-production_load_balancer_config/listener_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the load balancer listener.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-production_load_balancer_config/load_balancer_id"></div>
                    <b>load_balancer_id</b>
                    <a class="ansibleOptionLink" href="#parameter-production_load_balancer_config/load_balancer_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the load balancer.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-release_name"></div>
                    <b>release_name</b>
                    <a class="ansibleOptionLink" href="#parameter-release_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Default name of the chart instance. Must be unique within a Kubernetes namespace.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rollback_policy"></div>
                    <b>rollback_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-rollback_policy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;OKE_DEPLOYMENT&#x27;, &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;, &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rollback_policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-rollback_policy/policy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NO_STAGE_ROLLBACK_POLICY</li>
                                                                                                                                                                                                <li>AUTOMATED_STAGE_ROLLBACK_POLICY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies type of the deployment stage rollback policy.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rollout_policy"></div>
                    <b>rollout_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-rollout_policy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;, &#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;, &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;]</div>
                                            <div>Required when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;, &#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;, &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rollout_policy/batch_count"></div>
                    <b>batch_count</b>
                    <a class="ansibleOptionLink" href="#parameter-rollout_policy/batch_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies number of batches for this stage.</div>
                                            <div>Required when deploy_stage_type is one of [&#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rollout_policy/batch_delay_in_seconds"></div>
                    <b>batch_delay_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-rollout_policy/batch_delay_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies delay in seconds between batches. The default delay is 1 minute.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rollout_policy/batch_percentage"></div>
                    <b>batch_percentage</b>
                    <a class="ansibleOptionLink" href="#parameter-rollout_policy/batch_percentage" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The percentage that will be used to determine how many instances will be deployed concurrently.</div>
                                            <div>Required when policy_type is &#x27;COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rollout_policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-rollout_policy/policy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE</li>
                                                                                                                                                                                                <li>COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of policy used for rolling out a deployment stage.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rollout_policy/ramp_limit_percent"></div>
                    <b>ramp_limit_percent</b>
                    <a class="ansibleOptionLink" href="#parameter-rollout_policy/ramp_limit_percent" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Indicates the criteria to stop.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_CANARY_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-set_string"></div>
                    <b>set_string</b>
                    <a class="ansibleOptionLink" href="#parameter-set_string" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-set_string/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-set_string/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of parameters defined to set helm value.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-set_string/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-set_string/items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the parameter (case-sensitive).</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-set_string/items/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-set_string/items/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value of the parameter.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-set_values"></div>
                    <b>set_values</b>
                    <a class="ansibleOptionLink" href="#parameter-set_values" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-set_values/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-set_values/items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of parameters defined to set helm value.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-set_values/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-set_values/items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the parameter (case-sensitive).</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-set_values/items/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-set_values/items/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Value of the parameter.</div>
                                            <div>Required when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-should_cleanup_on_fail"></div>
                    <b>should_cleanup_on_fail</b>
                    <a class="ansibleOptionLink" href="#parameter-should_cleanup_on_fail" title="Permalink to this option"></a>
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
                                            <div>Allow deletion of new resources created during when an upgrade fails. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-should_not_wait"></div>
                    <b>should_not_wait</b>
                    <a class="ansibleOptionLink" href="#parameter-should_not_wait" title="Permalink to this option"></a>
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
                                            <div>Does not wait until all the resources are in a ready state to mark the release as successful if set to true. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-should_reset_values"></div>
                    <b>should_reset_values</b>
                    <a class="ansibleOptionLink" href="#parameter-should_reset_values" title="Permalink to this option"></a>
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
                                            <div>During upgrade, reset the values to the ones built into the chart. It overrides shouldReuseValues. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-should_reuse_values"></div>
                    <b>should_reuse_values</b>
                    <a class="ansibleOptionLink" href="#parameter-should_reuse_values" title="Permalink to this option"></a>
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
                                            <div>During upgrade, reuse the values of the last release and merge overrides from the command line. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-should_skip_crds"></div>
                    <b>should_skip_crds</b>
                    <a class="ansibleOptionLink" href="#parameter-should_skip_crds" title="Permalink to this option"></a>
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
                                            <div>If set, no CRDs are installed. By default, CRDs are installed only if they are not present already. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-should_skip_render_subchart_notes"></div>
                    <b>should_skip_render_subchart_notes</b>
                    <a class="ansibleOptionLink" href="#parameter-should_skip_render_subchart_notes" title="Permalink to this option"></a>
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
                                            <div>If set, renders subchart notes along with the parent. Set to false by default.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                            <div>The state of the DeployStage.</div>
                                            <div>Use <em>state=present</em> to create or update a DeployStage.</div>
                                            <div>Use <em>state=absent</em> to delete a DeployStage.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-test_load_balancer_config"></div>
                    <b>test_load_balancer_config</b>
                    <a class="ansibleOptionLink" href="#parameter-test_load_balancer_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;, &#x27;COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-test_load_balancer_config/backend_port"></div>
                    <b>backend_port</b>
                    <a class="ansibleOptionLink" href="#parameter-test_load_balancer_config/backend_port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Listen port for the backend server.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-test_load_balancer_config/listener_name"></div>
                    <b>listener_name</b>
                    <a class="ansibleOptionLink" href="#parameter-test_load_balancer_config/listener_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the load balancer listener.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-test_load_balancer_config/load_balancer_id"></div>
                    <b>load_balancer_id</b>
                    <a class="ansibleOptionLink" href="#parameter-test_load_balancer_config/load_balancer_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the load balancer.</div>
                                            <div>Required when deploy_stage_type is &#x27;COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-timeout_in_seconds"></div>
                    <b>timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-timeout_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Time to wait for execution of a shell stage. Defaults to 36000 seconds.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is one of [&#x27;SHELL&#x27;, &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-traffic_shift_target"></div>
                    <b>traffic_shift_target</b>
                    <a class="ansibleOptionLink" href="#parameter-traffic_shift_target" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs ser as per rolloutPolicy.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;LOAD_BALANCER_TRAFFIC_SHIFT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-values_artifact_ids"></div>
                    <b>values_artifact_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-values_artifact_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of values.yaml file artifact OCIDs.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;OKE_HELM_CHART_DEPLOYMENT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-wait_criteria"></div>
                    <b>wait_criteria</b>
                    <a class="ansibleOptionLink" href="#parameter-wait_criteria" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when deploy_stage_type is &#x27;WAIT&#x27;</div>
                                            <div>Required when deploy_stage_type is &#x27;WAIT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wait_criteria/wait_duration"></div>
                    <b>wait_duration</b>
                    <a class="ansibleOptionLink" href="#parameter-wait_criteria/wait_duration" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can be up to 2 days.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-wait_criteria/wait_type"></div>
                    <b>wait_type</b>
                    <a class="ansibleOptionLink" href="#parameter-wait_criteria/wait_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ABSOLUTE_WAIT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Wait criteria type.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
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

    
    - name: Create deploy_stage with deploy_stage_type = OKE_CANARY_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        oke_canary_deploy_stage_id: "ocid1.okecanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_CANARY_TRAFFIC_SHIFT

        # optional
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = OKE_BLUE_GREEN_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        oke_blue_green_deploy_stage_id: "ocid1.okebluegreendeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_BLUE_GREEN_TRAFFIC_SHIFT

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        production_load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT

        # optional
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        test_load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = WAIT
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: WAIT

        # optional
        wait_criteria:
          # required
          wait_type: ABSOLUTE_WAIT
          wait_duration: wait_duration_example
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT

        # optional
        blue_backend_ips:
          # optional
          items: [ "items_example" ]
        green_backend_ips:
          # optional
          items: [ "items_example" ]
        traffic_shift_target: traffic_shift_target_example
        load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = SHELL
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: SHELL

        # optional
        container_config:
          # required
          container_config_type: CONTAINER_INSTANCE_CONFIG
          shape_name: shape_name_example
          shape_config:
            # required
            ocpus: 3.4

            # optional
            memory_in_gbs: 3.4
          network_channel:
            # required
            network_channel_type: SERVICE_VNIC_CHANNEL
            subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

            # optional
            nsg_ids: [ "nsg_ids_example" ]

            # optional
          compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
          availability_domain: Uocm:PHX-AD-1
        command_spec_deploy_artifact_id: "ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        timeout_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        compute_instance_group_blue_green_deployment_deploy_stage_id: "ocid1.computeinstancegroupbluegreendeploymentdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = OKE_BLUE_GREEN_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        blue_green_strategy:
          # required
          strategy_type: NGINX_BLUE_GREEN_STRATEGY
          namespace_a: namespace_a_example
          namespace_b: namespace_b_example
          ingress_name: ingress_name_example
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_BLUE_GREEN_DEPLOYMENT

        # optional
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT

        # optional
        compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        failure_policy:
          # required
          failure_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = INVOKE_FUNCTION
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: INVOKE_FUNCTION

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        is_async: true
        is_validation_enabled: true

    - name: Create deploy_stage with deploy_stage_type = DEPLOY_FUNCTION
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: DEPLOY_FUNCTION

        # optional
        docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        config: null
        max_memory_in_mbs: 56
        function_timeout_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Create deploy_stage with deploy_stage_type = OKE_CANARY_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        canary_strategy:
          # required
          strategy_type: NGINX_CANARY_STRATEGY
          namespace: namespace_example
          ingress_name: ingress_name_example
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_CANARY_DEPLOYMENT

        # optional
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        compute_instance_group_canary_deploy_stage_id: "ocid1.computeinstancegroupcanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT

        # optional
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL
      oci_devops_deploy_stage:
        # required
        compute_instance_group_canary_traffic_shift_deploy_stage_id: "ocid1.computeinstancegroupcanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = OKE_HELM_CHART_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_HELM_CHART_DEPLOYMENT

        # optional
        helm_chart_deploy_artifact_id: "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        values_artifact_ids: [ "values_artifact_ids_example" ]
        release_name: release_name_example
        set_values:
          # required
          items:
          - # required
            name: name_example
            value: value_example
        set_string:
          # required
          items:
          - # required
            name: name_example
            value: value_example
        are_hooks_enabled: true
        should_reuse_values: true
        should_reset_values: true
        is_force_enabled: true
        should_cleanup_on_fail: true
        max_history: 56
        should_skip_crds: true
        should_skip_render_subchart_notes: true
        should_not_wait: true
        is_debug_enabled: true
        timeout_in_seconds: 56
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace: namespace_example
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = MANUAL_APPROVAL
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: MANUAL_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = OKE_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_DEPLOYMENT

        # optional
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace: namespace_example
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_environment_id_a: deploy_environment_id_a_example
        deploy_environment_id_b: deploy_environment_id_b_example
        production_load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT

        # optional
        failure_policy:
          # required
          failure_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        test_load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Create deploy_stage with deploy_stage_type = OKE_CANARY_APPROVAL
      oci_devops_deploy_stage:
        # required
        deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        oke_canary_traffic_shift_deploy_stage_id: "ocid1.okecanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_CANARY_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = OKE_CANARY_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_CANARY_TRAFFIC_SHIFT

        # optional
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = OKE_BLUE_GREEN_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_BLUE_GREEN_TRAFFIC_SHIFT

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT

        # optional
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        test_load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = WAIT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: WAIT

        # optional
        wait_criteria:
          # required
          wait_type: ABSOLUTE_WAIT
          wait_duration: wait_duration_example
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT

        # optional
        blue_backend_ips:
          # optional
          items: [ "items_example" ]
        green_backend_ips:
          # optional
          items: [ "items_example" ]
        traffic_shift_target: traffic_shift_target_example
        load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = SHELL
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: SHELL

        # optional
        container_config:
          # required
          container_config_type: CONTAINER_INSTANCE_CONFIG
          shape_name: shape_name_example
          shape_config:
            # required
            ocpus: 3.4

            # optional
            memory_in_gbs: 3.4
          network_channel:
            # required
            network_channel_type: SERVICE_VNIC_CHANNEL
            subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

            # optional
            nsg_ids: [ "nsg_ids_example" ]

            # optional
          compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
          availability_domain: Uocm:PHX-AD-1
        command_spec_deploy_artifact_id: "ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        timeout_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = OKE_BLUE_GREEN_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_BLUE_GREEN_DEPLOYMENT

        # optional
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT

        # optional
        compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        failure_policy:
          # required
          failure_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = INVOKE_FUNCTION
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: INVOKE_FUNCTION

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        is_async: true
        is_validation_enabled: true

    - name: Update deploy_stage with deploy_stage_type = DEPLOY_FUNCTION
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: DEPLOY_FUNCTION

        # optional
        docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        config: null
        max_memory_in_mbs: 56
        function_timeout_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update deploy_stage with deploy_stage_type = OKE_CANARY_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_CANARY_DEPLOYMENT

        # optional
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT

        # optional
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = OKE_HELM_CHART_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_HELM_CHART_DEPLOYMENT

        # optional
        helm_chart_deploy_artifact_id: "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        values_artifact_ids: [ "values_artifact_ids_example" ]
        release_name: release_name_example
        set_values:
          # required
          items:
          - # required
            name: name_example
            value: value_example
        set_string:
          # required
          items:
          - # required
            name: name_example
            value: value_example
        are_hooks_enabled: true
        should_reuse_values: true
        should_reset_values: true
        is_force_enabled: true
        should_cleanup_on_fail: true
        max_history: 56
        should_skip_crds: true
        should_skip_render_subchart_notes: true
        should_not_wait: true
        is_debug_enabled: true
        timeout_in_seconds: 56
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace: namespace_example
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = MANUAL_APPROVAL
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: MANUAL_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = OKE_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_DEPLOYMENT

        # optional
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace: namespace_example
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT

        # optional
        failure_policy:
          # required
          failure_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        test_load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage with deploy_stage_type = OKE_CANARY_APPROVAL
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_CANARY_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_CANARY_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_CANARY_TRAFFIC_SHIFT

        # optional
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_BLUE_GREEN_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_BLUE_GREEN_TRAFFIC_SHIFT

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: >
        Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
        with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT

        # optional
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        test_load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = WAIT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: WAIT

        # optional
        wait_criteria:
          # required
          wait_type: ABSOLUTE_WAIT
          wait_duration: wait_duration_example
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT

        # optional
        blue_backend_ips:
          # optional
          items: [ "items_example" ]
        green_backend_ips:
          # optional
          items: [ "items_example" ]
        traffic_shift_target: traffic_shift_target_example
        load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = SHELL
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: SHELL

        # optional
        container_config:
          # required
          container_config_type: CONTAINER_INSTANCE_CONFIG
          shape_name: shape_name_example
          shape_config:
            # required
            ocpus: 3.4

            # optional
            memory_in_gbs: 3.4
          network_channel:
            # required
            network_channel_type: SERVICE_VNIC_CHANNEL
            subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

            # optional
            nsg_ids: [ "nsg_ids_example" ]

            # optional
          compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
          availability_domain: Uocm:PHX-AD-1
        command_spec_deploy_artifact_id: "ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        timeout_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: >
        Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
        with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_BLUE_GREEN_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_BLUE_GREEN_DEPLOYMENT

        # optional
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: >
        Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
        with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT

        # optional
        compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        failure_policy:
          # required
          failure_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = INVOKE_FUNCTION
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: INVOKE_FUNCTION

        # optional
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        is_async: true
        is_validation_enabled: true

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = DEPLOY_FUNCTION
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: DEPLOY_FUNCTION

        # optional
        docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        config: null
        max_memory_in_mbs: 56
        function_timeout_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_CANARY_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_type: OKE_CANARY_DEPLOYMENT

        # optional
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: >
        Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
        with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT

        # optional
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: >
        Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
        with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_HELM_CHART_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_HELM_CHART_DEPLOYMENT

        # optional
        helm_chart_deploy_artifact_id: "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        values_artifact_ids: [ "values_artifact_ids_example" ]
        release_name: release_name_example
        set_values:
          # required
          items:
          - # required
            name: name_example
            value: value_example
        set_string:
          # required
          items:
          - # required
            name: name_example
            value: value_example
        are_hooks_enabled: true
        should_reuse_values: true
        should_reset_values: true
        is_force_enabled: true
        should_cleanup_on_fail: true
        max_history: 56
        should_skip_crds: true
        should_skip_render_subchart_notes: true
        should_not_wait: true
        is_debug_enabled: true
        timeout_in_seconds: 56
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace: namespace_example
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = MANUAL_APPROVAL
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: MANUAL_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_DEPLOYMENT

        # optional
        oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace: namespace_example
        rollback_policy:
          # required
          policy_type: NO_STAGE_ROLLBACK_POLICY
        kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: >
        Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
        with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT

        # optional
        failure_policy:
          # required
          failure_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
        deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
        test_load_balancer_config:
          # required
          load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
          listener_name: listener_name_example

          # optional
          backend_port: 56
        rollout_policy:
          # required
          batch_percentage: 56
          policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

          # optional
          batch_delay_in_seconds: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_CANARY_APPROVAL
      oci_devops_deploy_stage:
        # required
        deploy_stage_type: OKE_CANARY_APPROVAL

        # optional
        approval_policy:
          # required
          approval_policy_type: COUNT_BASED_APPROVAL
          number_of_approvals_required: 56
        description: description_example
        display_name: display_name_example
        deploy_stage_predecessor_collection:
          # required
          items:
          - # required
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Delete deploy_stage
      oci_devops_deploy_stage:
        # required
        deploy_stage_id: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

    - name: Delete deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_devops_deploy_stage:
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
            <th colspan="4">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage"></div>
                    <b>deploy_stage</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the DeployStage resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;approval_policy&#x27;: {&#x27;approval_policy_type&#x27;: &#x27;COUNT_BASED_APPROVAL&#x27;, &#x27;number_of_approvals_required&#x27;: 56}, &#x27;are_hooks_enabled&#x27;: True, &#x27;blue_backend_ips&#x27;: {&#x27;items&#x27;: []}, &#x27;blue_green_strategy&#x27;: {&#x27;ingress_name&#x27;: &#x27;ingress_name_example&#x27;, &#x27;namespace_a&#x27;: &#x27;namespace_a_example&#x27;, &#x27;namespace_b&#x27;: &#x27;namespace_b_example&#x27;, &#x27;strategy_type&#x27;: &#x27;NGINX_BLUE_GREEN_STRATEGY&#x27;}, &#x27;canary_strategy&#x27;: {&#x27;ingress_name&#x27;: &#x27;ingress_name_example&#x27;, &#x27;namespace&#x27;: &#x27;namespace_example&#x27;, &#x27;strategy_type&#x27;: &#x27;NGINX_CANARY_STRATEGY&#x27;}, &#x27;command_spec_deploy_artifact_id&#x27;: &#x27;ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compute_instance_group_blue_green_deployment_deploy_stage_id&#x27;: &#x27;ocid1.computeinstancegroupbluegreendeploymentdeploystage.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compute_instance_group_canary_deploy_stage_id&#x27;: &#x27;ocid1.computeinstancegroupcanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compute_instance_group_canary_traffic_shift_deploy_stage_id&#x27;: &#x27;ocid1.computeinstancegroupcanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compute_instance_group_deploy_environment_id&#x27;: &#x27;ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;config&#x27;: {}, &#x27;container_config&#x27;: {&#x27;availability_domain&#x27;: &#x27;Uocm:PHX-AD-1&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;container_config_type&#x27;: &#x27;CONTAINER_INSTANCE_CONFIG&#x27;, &#x27;network_channel&#x27;: {&#x27;network_channel_type&#x27;: &#x27;PRIVATE_ENDPOINT_CHANNEL&#x27;, &#x27;nsg_ids&#x27;: [], &#x27;subnet_id&#x27;: &#x27;ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx&#x27;}, &#x27;shape_config&#x27;: {&#x27;memory_in_gbs&#x27;: 3.4, &#x27;ocpus&#x27;: 3.4}, &#x27;shape_name&#x27;: &#x27;shape_name_example&#x27;}, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;deploy_artifact_id&#x27;: &#x27;ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;deploy_artifact_ids&#x27;: [], &#x27;deploy_environment_id_a&#x27;: &#x27;deploy_environment_id_a_example&#x27;, &#x27;deploy_environment_id_b&#x27;: &#x27;deploy_environment_id_b_example&#x27;, &#x27;deploy_pipeline_id&#x27;: &#x27;ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;deploy_stage_predecessor_collection&#x27;: {&#x27;items&#x27;: [{&#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;}]}, &#x27;deploy_stage_type&#x27;: &#x27;WAIT&#x27;, &#x27;deployment_spec_deploy_artifact_id&#x27;: &#x27;ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;docker_image_deploy_artifact_id&#x27;: &#x27;ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;failure_policy&#x27;: {&#x27;failure_count&#x27;: 56, &#x27;failure_percentage&#x27;: 56, &#x27;policy_type&#x27;: &#x27;COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT&#x27;}, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;function_deploy_environment_id&#x27;: &#x27;ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;function_timeout_in_seconds&#x27;: 56, &#x27;green_backend_ips&#x27;: {&#x27;items&#x27;: []}, &#x27;helm_chart_deploy_artifact_id&#x27;: &#x27;ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;is_async&#x27;: True, &#x27;is_debug_enabled&#x27;: True, &#x27;is_force_enabled&#x27;: True, &#x27;is_validation_enabled&#x27;: True, &#x27;kubernetes_manifest_deploy_artifact_ids&#x27;: [], &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;load_balancer_config&#x27;: {&#x27;backend_port&#x27;: 56, &#x27;listener_name&#x27;: &#x27;listener_name_example&#x27;, &#x27;load_balancer_id&#x27;: &#x27;ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx&#x27;}, &#x27;max_history&#x27;: 56, &#x27;max_memory_in_mbs&#x27;: 56, &#x27;namespace&#x27;: &#x27;namespace_example&#x27;, &#x27;oke_blue_green_deploy_stage_id&#x27;: &#x27;ocid1.okebluegreendeploystage.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;oke_canary_deploy_stage_id&#x27;: &#x27;ocid1.okecanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;oke_canary_traffic_shift_deploy_stage_id&#x27;: &#x27;ocid1.okecanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;oke_cluster_deploy_environment_id&#x27;: &#x27;ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;production_load_balancer_config&#x27;: {&#x27;backend_port&#x27;: 56, &#x27;listener_name&#x27;: &#x27;listener_name_example&#x27;, &#x27;load_balancer_id&#x27;: &#x27;ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx&#x27;}, &#x27;project_id&#x27;: &#x27;ocid1.project.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;release_name&#x27;: &#x27;release_name_example&#x27;, &#x27;rollback_policy&#x27;: {&#x27;policy_type&#x27;: &#x27;AUTOMATED_STAGE_ROLLBACK_POLICY&#x27;}, &#x27;rollout_policy&#x27;: {&#x27;batch_count&#x27;: 56, &#x27;batch_delay_in_seconds&#x27;: 56, &#x27;batch_percentage&#x27;: 56, &#x27;policy_type&#x27;: &#x27;COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT&#x27;, &#x27;ramp_limit_percent&#x27;: 3.4}, &#x27;set_string&#x27;: {&#x27;items&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}]}, &#x27;set_values&#x27;: {&#x27;items&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}]}, &#x27;should_cleanup_on_fail&#x27;: True, &#x27;should_not_wait&#x27;: True, &#x27;should_reset_values&#x27;: True, &#x27;should_reuse_values&#x27;: True, &#x27;should_skip_crds&#x27;: True, &#x27;should_skip_render_subchart_notes&#x27;: True, &#x27;system_tags&#x27;: {}, &#x27;test_load_balancer_config&#x27;: {&#x27;backend_port&#x27;: 56, &#x27;listener_name&#x27;: &#x27;listener_name_example&#x27;, &#x27;load_balancer_id&#x27;: &#x27;ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx&#x27;}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;timeout_in_seconds&#x27;: 56, &#x27;traffic_shift_target&#x27;: &#x27;AUTO_SELECT&#x27;, &#x27;values_artifact_ids&#x27;: [], &#x27;wait_criteria&#x27;: {&#x27;wait_duration&#x27;: &#x27;wait_duration_example&#x27;, &#x27;wait_type&#x27;: &#x27;ABSOLUTE_WAIT&#x27;}}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/approval_policy"></div>
                    <b>approval_policy</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/approval_policy" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/approval_policy/approval_policy_type"></div>
                    <b>approval_policy_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/approval_policy/approval_policy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Approval policy type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">COUNT_BASED_APPROVAL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/approval_policy/number_of_approvals_required"></div>
                    <b>number_of_approvals_required</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/approval_policy/number_of_approvals_required" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A minimum number of approvals required for stage to proceed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/are_hooks_enabled"></div>
                    <b>are_hooks_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/are_hooks_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Disable pre/post upgrade hooks. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/blue_backend_ips"></div>
                    <b>blue_backend_ips</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/blue_backend_ips" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/blue_backend_ips/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/blue_backend_ips/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IP address of the backend server. A server could be a compute instance or a load balancer.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/blue_green_strategy"></div>
                    <b>blue_green_strategy</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/blue_green_strategy" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/blue_green_strategy/ingress_name"></div>
                    <b>ingress_name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/blue_green_strategy/ingress_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the Ingress resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ingress_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/blue_green_strategy/namespace_a"></div>
                    <b>namespace_a</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/blue_green_strategy/namespace_a" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Namespace A for deployment. Example: namespaceA - first Namespace name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">namespace_a_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/blue_green_strategy/namespace_b"></div>
                    <b>namespace_b</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/blue_green_strategy/namespace_b" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Namespace B for deployment. Example: namespaceB - second Namespace name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">namespace_b_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/blue_green_strategy/strategy_type"></div>
                    <b>strategy_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/blue_green_strategy/strategy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Blue-Green strategy type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NGINX_BLUE_GREEN_STRATEGY</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/canary_strategy"></div>
                    <b>canary_strategy</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/canary_strategy" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/canary_strategy/ingress_name"></div>
                    <b>ingress_name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/canary_strategy/ingress_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the Ingress resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ingress_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/canary_strategy/namespace"></div>
                    <b>namespace</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/canary_strategy/namespace" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Canary namespace to be used for Kubernetes canary deployment. Example: canary - Name of the Canary namespace.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">namespace_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/canary_strategy/strategy_type"></div>
                    <b>strategy_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/canary_strategy/strategy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Canary strategy type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NGINX_CANARY_STRATEGY</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/command_spec_deploy_artifact_id"></div>
                    <b>command_spec_deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/command_spec_deploy_artifact_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the artifact that contains the command specification.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of a compartment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/compute_instance_group_blue_green_deployment_deploy_stage_id"></div>
                    <b>compute_instance_group_blue_green_deployment_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/compute_instance_group_blue_green_deployment_deploy_stage_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.computeinstancegroupbluegreendeploymentdeploystage.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/compute_instance_group_canary_deploy_stage_id"></div>
                    <b>compute_instance_group_canary_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/compute_instance_group_canary_deploy_stage_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of an upstream compute instance group canary deployment stage ID in this pipeline.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.computeinstancegroupcanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/compute_instance_group_canary_traffic_shift_deploy_stage_id"></div>
                    <b>compute_instance_group_canary_traffic_shift_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/compute_instance_group_canary_traffic_shift_deploy_stage_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A compute instance group canary traffic shift stage OCID for load balancer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.computeinstancegroupcanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/compute_instance_group_deploy_environment_id"></div>
                    <b>compute_instance_group_deploy_environment_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/compute_instance_group_deploy_environment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A compute instance group environment OCID for Canary deployment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/config"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/config" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>User provided key and value pair configuration, which is assigned through constants or parameter.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config"></div>
                    <b>container_config</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/availability_domain"></div>
                    <b>availability_domain</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/availability_domain" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Availability domain where the ContainerInstance will be created.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Uocm:PHX-AD-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the compartment where the ContainerInstance will be created.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/container_config_type"></div>
                    <b>container_config_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/container_config_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Container configuration type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CONTAINER_INSTANCE_CONFIG</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/network_channel"></div>
                    <b>network_channel</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/network_channel" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/network_channel/network_channel_type"></div>
                    <b>network_channel_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/network_channel/network_channel_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Network channel type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PRIVATE_ENDPOINT_CHANNEL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/network_channel/nsg_ids"></div>
                    <b>nsg_ids</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/network_channel/nsg_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of network security group OCIDs.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/network_channel/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/network_channel/subnet_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the subnet where VNIC resources will be created for private endpoint.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/shape_config"></div>
                    <b>shape_config</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/shape_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/shape_config/memory_in_gbs"></div>
                    <b>memory_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/shape_config/memory_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The total amount of memory available to the instance, in gigabytes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/shape_config/ocpus"></div>
                    <b>ocpus</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/shape_config/ocpus" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The total number of OCPUs available to the instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/container_config/shape_name"></div>
                    <b>shape_name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/container_config/shape_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The shape of the ContainerInstance. The shape determines the resources available to the ContainerInstance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">shape_name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/defined_tags" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_artifact_id"></div>
                    <b>deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_artifact_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage&#x27;s execution. If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace the placeholders in the artifact content.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_artifact_ids"></div>
                    <b>deploy_artifact_ids</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_artifact_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of file artifact OCIDs to deploy.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_environment_id_a"></div>
                    <b>deploy_environment_id_a</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_environment_id_a" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>First compute instance group environment OCID for deployment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">deploy_environment_id_a_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_environment_id_b"></div>
                    <b>deploy_environment_id_b</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_environment_id_b" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Second compute instance group environment OCID for deployment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">deploy_environment_id_b_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_pipeline_id"></div>
                    <b>deploy_pipeline_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_pipeline_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of a pipeline.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_stage_predecessor_collection"></div>
                    <b>deploy_stage_predecessor_collection</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_stage_predecessor_collection" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_stage_predecessor_collection/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_stage_predecessor_collection/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of stage predecessors for a stage.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_stage_predecessor_collection/items/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_stage_predecessor_collection/items/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deploy_stage_type"></div>
                    <b>deploy_stage_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deploy_stage_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Deployment stage type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">WAIT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/deployment_spec_deploy_artifact_id"></div>
                    <b>deployment_spec_deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/deployment_spec_deploy_artifact_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the artifact that contains the deployment specification.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Optional description about the deployment stage.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/docker_image_deploy_artifact_id"></div>
                    <b>docker_image_deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/docker_image_deploy_artifact_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A Docker image artifact OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/failure_policy"></div>
                    <b>failure_policy</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/failure_policy" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/failure_policy/failure_count"></div>
                    <b>failure_count</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/failure_policy/failure_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The threshold count of failed instances in the group, which when reached or exceeded sets the stage as Failed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/failure_policy/failure_percentage"></div>
                    <b>failure_percentage</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/failure_policy/failure_percentage" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The failure percentage threshold, which when reached or exceeded sets the stage as Failed. Percentage is computed as the ceiling value of the number of failed instances over the total count of the instances in the group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/failure_policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/failure_policy/policy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies if the failure instance size is given by absolute number or by percentage.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/freeform_tags" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/function_deploy_environment_id"></div>
                    <b>function_deploy_environment_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/function_deploy_environment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Function environment OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/function_timeout_in_seconds"></div>
                    <b>function_timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/function_timeout_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Timeout for execution of the Function. Value in seconds.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/green_backend_ips"></div>
                    <b>green_backend_ips</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/green_backend_ips" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/green_backend_ips/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/green_backend_ips/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IP address of the backend server. A server could be a compute instance or a load balancer.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/helm_chart_deploy_artifact_id"></div>
                    <b>helm_chart_deploy_artifact_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/helm_chart_deploy_artifact_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Helm chart artifact OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/id" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/is_async"></div>
                    <b>is_async</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/is_async" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A boolean flag specifies whether this stage executes asynchronously.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/is_debug_enabled"></div>
                    <b>is_debug_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/is_debug_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enables helm --debug option to stream output to tf stdout. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/is_force_enabled"></div>
                    <b>is_force_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/is_force_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Force resource update through delete; or if required, recreate. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/is_validation_enabled"></div>
                    <b>is_validation_enabled</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/is_validation_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A boolean flag specifies whether the invoked function must be validated.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/kubernetes_manifest_deploy_artifact_ids"></div>
                    <b>kubernetes_manifest_deploy_artifact_ids</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/kubernetes_manifest_deploy_artifact_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of Kubernetes manifest artifact OCIDs</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/lifecycle_details" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the deployment stage.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/load_balancer_config"></div>
                    <b>load_balancer_config</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/load_balancer_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/load_balancer_config/backend_port"></div>
                    <b>backend_port</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/load_balancer_config/backend_port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Listen port for the backend server.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/load_balancer_config/listener_name"></div>
                    <b>listener_name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/load_balancer_config/listener_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the load balancer listener.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">listener_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/load_balancer_config/load_balancer_id"></div>
                    <b>load_balancer_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/load_balancer_config/load_balancer_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the load balancer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/max_history"></div>
                    <b>max_history</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/max_history" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Limit the maximum number of revisions saved per release. Use 0 for no limit. Set to 10 by default</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/max_memory_in_mbs"></div>
                    <b>max_memory_in_mbs</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/max_memory_in_mbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum usable memory for the Function (in MB).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/namespace"></div>
                    <b>namespace</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/namespace" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Default namespace to be used for Kubernetes deployment when not specified in the manifest.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">namespace_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/oke_blue_green_deploy_stage_id"></div>
                    <b>oke_blue_green_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/oke_blue_green_deploy_stage_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the upstream OKE blue-green deployment stage in this pipeline.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.okebluegreendeploystage.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/oke_canary_deploy_stage_id"></div>
                    <b>oke_canary_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/oke_canary_deploy_stage_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of an upstream OKE canary deployment stage in this pipeline.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.okecanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/oke_canary_traffic_shift_deploy_stage_id"></div>
                    <b>oke_canary_traffic_shift_deploy_stage_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/oke_canary_traffic_shift_deploy_stage_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.okecanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/oke_cluster_deploy_environment_id"></div>
                    <b>oke_cluster_deploy_environment_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/oke_cluster_deploy_environment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Kubernetes cluster environment OCID for deployment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/production_load_balancer_config"></div>
                    <b>production_load_balancer_config</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/production_load_balancer_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/production_load_balancer_config/backend_port"></div>
                    <b>backend_port</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/production_load_balancer_config/backend_port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Listen port for the backend server.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/production_load_balancer_config/listener_name"></div>
                    <b>listener_name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/production_load_balancer_config/listener_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the load balancer listener.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">listener_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/production_load_balancer_config/load_balancer_id"></div>
                    <b>load_balancer_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/production_load_balancer_config/load_balancer_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the load balancer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/project_id"></div>
                    <b>project_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/project_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of a project.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.project.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/release_name"></div>
                    <b>release_name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/release_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Release name of the Helm chart.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">release_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/rollback_policy"></div>
                    <b>rollback_policy</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/rollback_policy" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/rollback_policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/rollback_policy/policy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies type of the deployment stage rollback policy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">AUTOMATED_STAGE_ROLLBACK_POLICY</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/rollout_policy"></div>
                    <b>rollout_policy</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/rollout_policy" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/rollout_policy/batch_count"></div>
                    <b>batch_count</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/rollout_policy/batch_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number that will be used to determine how many instances will be deployed concurrently.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/rollout_policy/batch_delay_in_seconds"></div>
                    <b>batch_delay_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/rollout_policy/batch_delay_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The duration of delay between batch rollout. The default delay is 1 minute.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/rollout_policy/batch_percentage"></div>
                    <b>batch_percentage</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/rollout_policy/batch_percentage" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The percentage that will be used to determine how many instances will be deployed concurrently.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/rollout_policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/rollout_policy/policy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of policy used for rolling out a deployment stage.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/rollout_policy/ramp_limit_percent"></div>
                    <b>ramp_limit_percent</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/rollout_policy/ramp_limit_percent" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates the criteria to stop.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/set_string"></div>
                    <b>set_string</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/set_string" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/set_string/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/set_string/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of parameters defined to set helm value.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/set_string/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/set_string/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the parameter (case-sensitive).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/set_string/items/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/set_string/items/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Value of the parameter.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/set_values"></div>
                    <b>set_values</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/set_values" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/set_values/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/set_values/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of parameters defined to set helm value.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/set_values/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/set_values/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the parameter (case-sensitive).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/set_values/items/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/set_values/items/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Value of the parameter.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/should_cleanup_on_fail"></div>
                    <b>should_cleanup_on_fail</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/should_cleanup_on_fail" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Allow deletion of new resources created during when an upgrade fails. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/should_not_wait"></div>
                    <b>should_not_wait</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/should_not_wait" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Waits until all the resources are in a ready state to mark the release as successful. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/should_reset_values"></div>
                    <b>should_reset_values</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/should_reset_values" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>During upgrade, reset the values to the ones built into the chart. It overrides shouldReuseValues. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/should_reuse_values"></div>
                    <b>should_reuse_values</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/should_reuse_values" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>During upgrade, reuse the values of the last release and merge overrides from the command line. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/should_skip_crds"></div>
                    <b>should_skip_crds</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/should_skip_crds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>If set, no CRDs are installed. By default, CRDs are installed only if they are not present already. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/should_skip_render_subchart_notes"></div>
                    <b>should_skip_render_subchart_notes</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/should_skip_render_subchart_notes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>If set, renders subchart notes along with the parent. Set to false by default.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/system_tags" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/test_load_balancer_config"></div>
                    <b>test_load_balancer_config</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/test_load_balancer_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/test_load_balancer_config/backend_port"></div>
                    <b>backend_port</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/test_load_balancer_config/backend_port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Listen port for the backend server.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/test_load_balancer_config/listener_name"></div>
                    <b>listener_name</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/test_load_balancer_config/listener_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the load balancer listener.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">listener_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/test_load_balancer_config/load_balancer_id"></div>
                    <b>load_balancer_id</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/test_load_balancer_config/load_balancer_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the load balancer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Time the deployment stage was created. Format defined by <a href='https://datatracker.ietf.org/doc/html/rfc3339'>RFC3339</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Time the deployment stage was updated. Format defined by <a href='https://datatracker.ietf.org/doc/html/rfc3339'>RFC3339</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/timeout_in_seconds"></div>
                    <b>timeout_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/timeout_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Time to wait for execution of a helm stage. Defaults to 300 seconds.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/traffic_shift_target"></div>
                    <b>traffic_shift_target</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/traffic_shift_target" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to green Backend IPs as per rolloutPolicy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">AUTO_SELECT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/values_artifact_ids"></div>
                    <b>values_artifact_ids</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/values_artifact_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of values.yaml file artifact OCIDs.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/wait_criteria"></div>
                    <b>wait_criteria</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/wait_criteria" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/wait_criteria/wait_duration"></div>
                    <b>wait_duration</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/wait_criteria/wait_duration" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can be up to 2 days.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">wait_duration_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-deploy_stage/wait_criteria/wait_type"></div>
                    <b>wait_type</b>
                    <a class="ansibleOptionLink" href="#return-deploy_stage/wait_criteria/wait_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Wait criteria type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ABSOLUTE_WAIT</div>
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

