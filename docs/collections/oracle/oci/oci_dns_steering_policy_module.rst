.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.oracle.oci.oci_dns_steering_policy_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_dns_steering_policy -- Manage a SteeringPolicy resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 2.29.0).

    To install it use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_dns_steering_policy`.

.. version_added

.. versionadded:: 2.9 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a SteeringPolicy resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new steering policy in the specified compartment. For more information on creating policies with templates, see `Traffic Management API Guide <https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm>`_.
- This resource has the following action operations in the :ref:`oci_steering_policy_actions <ansible_collections.oci_steering_policy_actions_module>` module: change_compartment.


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
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-answers"></div>
                    <b>answers</b>
                    <a class="ansibleOptionLink" href="#parameter-answers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The set of all answers that can potentially issue from the steering policy.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-answers/is_disabled"></div>
                    <b>is_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-answers/is_disabled" title="Permalink to this option"></a>
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
                                            <div>Set this property to `true` to indicate that the answer is administratively disabled, such as when the corresponding server is down for maintenance. An answer&#x27;s `isDisabled` property can be referenced in `answerCondition` properties in rules using `answer.isDisabled`.</div>
                                            <div>&quot;**Example:**
      \&quot;rules\&quot;: [
        {
          \&quot;ruleType\&quot;: \&quot;FILTER\&quot;,
          \&quot;defaultAnswerData\&quot;: [
            {
              \&quot;answerCondition\&quot;: \&quot;answer.isDisabled != true\&quot;,
              \&quot;shouldKeep\&quot;: true
            }
          ]
        },&quot;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-answers/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-answers/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name for the answer, unique within the steering policy. An answer&#x27;s `name` property can be referenced in `answerCondition` properties of rules using `answer.name`.</div>
                                            <div>**Example:**</div>
                                            <div>&quot; \&quot;rules\&quot;: [
        {
          \&quot;ruleType\&quot;: \&quot;FILTER\&quot;,
          \&quot;defaultAnswerData\&quot;:  [
            {
              \&quot;answerCondition\&quot;: \&quot;answer.name == &#x27;server 1&#x27;\&quot;,
              \&quot;shouldKeep\&quot;: true
            }
          ]
        }
      ]&quot;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-answers/pool"></div>
                    <b>pool</b>
                    <a class="ansibleOptionLink" href="#parameter-answers/pool" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The freeform name of a group of one or more records in which this record is included, such as &quot;LAX data center&quot;. An answer&#x27;s `pool` property can be referenced in `answerCondition` properties of rules using `answer.pool`.</div>
                                            <div>**Example:**</div>
                                            <div>&quot; \&quot;rules\&quot;: [
        {
          \&quot;ruleType\&quot;: \&quot;FILTER\&quot;,
          \&quot;defaultAnswerData\&quot;:  [
            {
              \&quot;answerCondition\&quot;: \&quot;answer.pool == &#x27;US East Servers&#x27;\&quot;,
              \&quot;shouldKeep\&quot;: true
            }
          ]
        }
      ]&quot;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-answers/rdata"></div>
                    <b>rdata</b>
                    <a class="ansibleOptionLink" href="#parameter-answers/rdata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The record&#x27;s data, as whitespace-delimited tokens in type-specific presentation format. All RDATA is normalized and the returned presentation of your RDATA may differ from its initial input. For more information about RDATA, see <a href='https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm'>Supported DNS Resource Record Types</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-answers/rtype"></div>
                    <b>rtype</b>
                    <a class="ansibleOptionLink" href="#parameter-answers/rtype" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of DNS record, such as A or CNAME. Only A, AAAA, and CNAME are supported. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm'>Supported DNS Resource Record Types</a>.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                            <div>The OCID of the compartment containing the steering policy.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>Required for delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                            <div>**Example:** `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                            <div>A user-friendly name for the steering policy. Does not have to be unique and can be changed. Avoid entering confidential information.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                            <div>**Example:** `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-health_check_monitor_id"></div>
                    <b>health_check_monitor_id</b>
                    <a class="ansibleOptionLink" href="#parameter-health_check_monitor_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `rdata` not matching any monitored endpoint will be assumed healthy.</div>
                                            <div>**Note:** To use the Health Check monitoring feature in a steering policy, a monitor must be created using the Health Checks service first. For more information on how to create a monitor, please see <a href='https://docs.cloud.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm'>Managing Health Checks</a>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-if_unmodified_since"></div>
                    <b>if_unmodified_since</b>
                    <a class="ansibleOptionLink" href="#parameter-if_unmodified_since" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The `If-Unmodified-Since` header field makes the request method conditional on the selected representation&#x27;s last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The series of rules that will be processed in sequence to reduce the pool of answers to a response for any given request.</div>
                                            <div>The first rule receives a shuffled list of all answers, and every other rule receives the list of answers emitted by the one preceding it. The last rule populates the response.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rules/cases"></div>
                    <b>cases</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/cases" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate configurations for how it should behave during processing for any given DNS query. When a rule has no sequence of `cases`, it is always evaluated with the same configuration during processing. When a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a non-empty sequence of `cases`, its behavior during processing is configured by the first matching `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression evaluates to true for the given query.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/cases/answer_data"></div>
                    <b>answer_data</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/cases/answer_data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of `SteeringPolicyFilterAnswerData` objects.</div>
                                            <div>Applicable when rule_type is one of [&#x27;FILTER&#x27;, &#x27;WEIGHTED&#x27;, &#x27;PRIORITY&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-rules/cases/answer_data/answer_condition"></div>
                    <b>answer_condition</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/cases/answer_data/answer_condition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.</div>
                                            <div>Applicable when rule_type is one of [&#x27;FILTER&#x27;, &#x27;WEIGHTED&#x27;, &#x27;PRIORITY&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-rules/cases/answer_data/should_keep"></div>
                    <b>should_keep</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/cases/answer_data/should_keep" title="Permalink to this option"></a>
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
                                            <div>Keeps the answer only if the value is `true`.</div>
                                            <div>Applicable when rule_type is &#x27;FILTER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-rules/cases/answer_data/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/cases/answer_data/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The weight assigned to the set of selected answers. Answers with a higher weight will be served more frequently. Answers can be given a value between `0` and `255`.</div>
                                            <div>Required when rule_type is one of [&#x27;WEIGHTED&#x27;, &#x27;PRIORITY&#x27;]</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/cases/case_condition"></div>
                    <b>case_condition</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/cases/case_condition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An expression that uses conditions at the time of a DNS query to indicate whether a case matches. Conditions may include the geographical location, IP subnet, or ASN the DNS query originated. **Example:** If you have an office that uses the subnet `192.0.2.0/24` you could use a `caseCondition` expression `query.client.subnet in (&#x27;192.0.2.0/24&#x27;)` to define a case that matches queries from that office.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/cases/count"></div>
                    <b>count</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/cases/count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of answers allowed to remain after the limit rule has been processed, keeping only the first of the remaining answers in the list. Example: If the `count` property is set to `2` and four answers remain before the limit rule is processed, only the first two answers in the list will remain after the limit rule has been processed.</div>
                                            <div>Required when rule_type is &#x27;LIMIT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rules/default_answer_data"></div>
                    <b>default_answer_data</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/default_answer_data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defines a default set of answer conditions and values that are applied to an answer when `cases` is not defined for the rule, or a matching case does not have any matching `answerCondition`s in its `answerData`. `defaultAnswerData` is not applied if `cases` is defined and there are no matching cases. In this scenario, the next rule will be processed.</div>
                                            <div>Applicable when rule_type is one of [&#x27;FILTER&#x27;, &#x27;WEIGHTED&#x27;, &#x27;PRIORITY&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/default_answer_data/answer_condition"></div>
                    <b>answer_condition</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/default_answer_data/answer_condition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.</div>
                                            <div>Applicable when rule_type is one of [&#x27;FILTER&#x27;, &#x27;WEIGHTED&#x27;, &#x27;PRIORITY&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/default_answer_data/should_keep"></div>
                    <b>should_keep</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/default_answer_data/should_keep" title="Permalink to this option"></a>
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
                                            <div>Keeps the answer only if the value is `true`.</div>
                                            <div>Applicable when rule_type is &#x27;FILTER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/default_answer_data/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/default_answer_data/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The weight assigned to the set of selected answers. Answers with a higher weight will be served more frequently. Answers can be given a value between `0` and `255`.</div>
                                            <div>Required when rule_type is one of [&#x27;WEIGHTED&#x27;, &#x27;PRIORITY&#x27;]</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rules/default_count"></div>
                    <b>default_count</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/default_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defines a default count if `cases` is not defined for the rule or a matching case does not define `count`. `defaultCount` is **not** applied if `cases` is defined and there are no matching cases. In this scenario, the next rule will be processed. If no rules remain to be processed, the answer will be chosen from the remaining list of answers.</div>
                                            <div>Applicable when rule_type is &#x27;LIMIT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rules/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-defined description of the rule&#x27;s purpose or behavior.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rules/rule_type"></div>
                    <b>rule_type</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/rule_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>FILTER</li>
                                                                                                                                                                                                <li>WEIGHTED</li>
                                                                                                                                                                                                <li>LIMIT</li>
                                                                                                                                                                                                <li>HEALTH</li>
                                                                                                                                                                                                <li>PRIORITY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of a rule determines its sorting/filtering behavior. * `FILTER` - Filters the list of answers based on their defined boolean data. Answers remain only if their `shouldKeep` value is `true`.</div>
                                            <div>* `HEALTH` - Removes answers from the list if their `rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.</div>
                                            <div>* `WEIGHTED` - Uses a number between 0 and 255 to determine how often an answer will be served in relation to other answers. Anwers with a higher weight will be served more frequently.</div>
                                            <div>* `PRIORITY` - Uses a defined rank value of answers to determine which answer to serve, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value. Answers can be given a value between `0` and `255`.</div>
                                            <div>* `LIMIT` - Filters answers that are too far down the list. Parameter `defaultCount` specifies how many answers to keep. **Example:** If `defaultCount` has a value of `2` and there are five answers left, when the `LIMIT` rule is processed, only the first two answers will remain in the list.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-scope"></div>
                    <b>scope</b>
                    <a class="ansibleOptionLink" href="#parameter-scope" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GLOBAL</li>
                                                                                                                                                                                                <li>PRIVATE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies to operate only on resources that have a matching DNS scope.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                            <div>The state of the SteeringPolicy.</div>
                                            <div>Use <em>state=present</em> to create or update a SteeringPolicy.</div>
                                            <div>Use <em>state=absent</em> to delete a SteeringPolicy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-steering_policy_id"></div>
                    <b>steering_policy_id</b>
                    <a class="ansibleOptionLink" href="#parameter-steering_policy_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the target steering policy.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-template"></div>
                    <b>template</b>
                    <a class="ansibleOptionLink" href="#parameter-template" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>FAILOVER</li>
                                                                                                                                                                                                <li>LOAD_BALANCE</li>
                                                                                                                                                                                                <li>ROUTE_BY_GEO</li>
                                                                                                                                                                                                <li>ROUTE_BY_ASN</li>
                                                                                                                                                                                                <li>ROUTE_BY_IP</li>
                                                                                                                                                                                                <li>CUSTOM</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>A set of predefined rules based on the desired purpose of the steering policy. Each template utilizes Traffic Management&#x27;s rules in a different order to produce the desired results when answering DNS queries.</div>
                                            <div>**Example:** The `FAILOVER` template determines answers by filtering the policy&#x27;s answers using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`, and `LIMIT`. This gives the domain dynamic failover capability.</div>
                                            <div>It is **strongly recommended** to use a template other than `CUSTOM` when creating a steering policy.</div>
                                            <div>All templates require the rule order to begin with an unconditional `FILTER` rule that keeps answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`. The last rule of a template must must be a `LIMIT` rule. For more information about templates and code examples, see <a href='https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm'>Traffic Management API Guide</a>.</div>
                                            <div>**Template Types**</div>
                                            <div>* `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers to serve. If an endpoint fails a health check, the answer for that endpoint will be removed from the list of available answers until the endpoint is detected as healthy.</div>
                                            <div>* `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights.</div>
                                            <div>* `ROUTE_BY_GEO` - Answers DNS queries based on the query&#x27;s geographic location. For a list of geographic locations to route by, see <a href='https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm'>Traffic Management Geographic Locations</a>.</div>
                                            <div>* `ROUTE_BY_ASN` - Answers DNS queries based on the query&#x27;s originating ASN.</div>
                                            <div>* `ROUTE_BY_IP` - Answers DNS queries based on the query&#x27;s IP address.</div>
                                            <div>* `CUSTOM` - Allows a customized configuration of rules.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-ttl"></div>
                    <b>ttl</b>
                    <a class="ansibleOptionLink" href="#parameter-ttl" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Time To Live (TTL) for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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

    
    - name: Create steering_policy
      oci_dns_steering_policy:
        compartment_id: "ocid1.compartment.oc1.."
        display_name: "failover between endpoints"
        ttl: 30
        health_check_monitor_id: "ocid1.httpmonitor.oc1.."
        template: "FAILOVER"
        answers:
        - name: "server-primary"
          rtype: "A"
          rdata: "192.0.2.0"
          pool: "primary"
        - name: "server-secondary"
          rtype: "A"
          rdata: "192.0.4.6"
          pool: "secondary"
        rules:
        - rule_type: "FILTER"
          default_answer_data:
          - answer_condition: "answer.isDisabled != true"
            should_keep: true
        - rule_type: "HEALTH"
        - rule_type: "PRIORITY"
          default_answer_data:
          - answer_condition: "answer.pool == 'primary'"
            value: 1
          - answer_condition: "answer.pool == 'secondary'"
            value: 99
        - rule_type: "LIMIT"
          default_count: 1

    - name: Update steering_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_dns_steering_policy:
        compartment_id: "ocid1.compartment.oc1.."
        display_name: "LA data center failover"
        ttl: 30
        health_check_monitor_id: "ocid1.httpmonitor.oc1.."
        template: "FAILOVER"
        answers:
        - name: "server-primary"
          rtype: "A"
          rdata: "192.0.2.0"
          pool: "primary"
        - name: "server-secondary"
          rtype: "A"
          rdata: "192.0.4.1"
          pool: "secondary"
        rules:
        - rule_type: "FILTER"
          default_answer_data:
          - answer_condition: "answer.isDisabled != true"
            should_keep: true
        - rule_type: "HEALTH"
        - rule_type: "PRIORITY"
          default_answer_data:
          - answer_condition: "answer.pool == 'primary'"
            value: 1
          - answer_condition: "answer.pool == 'secondary'"
            value: 99
        - rule_type: "LIMIT"
          default_count: 1

    - name: Update steering_policy
      oci_dns_steering_policy:
        steering_policy_id: "ocid1.steeringpolicy.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Delete steering_policy
      oci_dns_steering_policy:
        steering_policy_id: "ocid1.steeringpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

    - name: Delete steering_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_dns_steering_policy:
        compartment_id: "ocid1.compartment.oc1.."
        display_name: failover between endpoints
        state: absent





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-steering_policy"></div>
                    <b>steering_policy</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the SteeringPolicy resource acted upon by the current operation</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;_self&#x27;: &#x27;_self_example&#x27;, &#x27;answers&#x27;: [{&#x27;is_disabled&#x27;: True, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;pool&#x27;: &#x27;pool_example&#x27;, &#x27;rdata&#x27;: &#x27;rdata_example&#x27;, &#x27;rtype&#x27;: &#x27;rtype_example&#x27;}], &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;health_check_monitor_id&#x27;: &#x27;ocid1.healthcheckmonitor.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;lifecycle_state&#x27;: &#x27;ACTIVE&#x27;, &#x27;rules&#x27;: [{&#x27;cases&#x27;: [{&#x27;answer_data&#x27;: [{&#x27;answer_condition&#x27;: &quot;answer.pool == &#x27;A&#x27;&quot;, &#x27;should_keep&#x27;: True, &#x27;value&#x27;: 56}], &#x27;case_condition&#x27;: &quot;query.client.address in (subnet &#x27;198.51.100.0/24&#x27;)&quot;, &#x27;count&#x27;: 56}], &#x27;default_answer_data&#x27;: [{&#x27;answer_condition&#x27;: &quot;answer.pool == &#x27;A&#x27;&quot;, &#x27;should_keep&#x27;: True, &#x27;value&#x27;: 56}], &#x27;default_count&#x27;: 56, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;rule_type&#x27;: &#x27;FILTER&#x27;}], &#x27;template&#x27;: &#x27;FAILOVER&#x27;, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;ttl&#x27;: 56}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/_self"></div>
                    <b>_self</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/_self" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The canonical absolute URL of the resource.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">_self_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/answers"></div>
                    <b>answers</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/answers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The set of all answers that can potentially issue from the steering policy.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/answers/is_disabled"></div>
                    <b>is_disabled</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/answers/is_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Set this property to `true` to indicate that the answer is administratively disabled, such as when the corresponding server is down for maintenance. An answer&#x27;s `isDisabled` property can be referenced in `answerCondition` properties in rules using `answer.isDisabled`.</div>
                                            <div>&quot;**Example:**
      \&quot;rules\&quot;: [
        {
          \&quot;ruleType\&quot;: \&quot;FILTER\&quot;,
          \&quot;defaultAnswerData\&quot;: [
            {
              \&quot;answerCondition\&quot;: \&quot;answer.isDisabled != true\&quot;,
              \&quot;shouldKeep\&quot;: true
            }
          ]
        },&quot;</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/answers/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/answers/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name for the answer, unique within the steering policy. An answer&#x27;s `name` property can be referenced in `answerCondition` properties of rules using `answer.name`.</div>
                                            <div>**Example:**</div>
                                            <div>&quot; \&quot;rules\&quot;: [
        {
          \&quot;ruleType\&quot;: \&quot;FILTER\&quot;,
          \&quot;defaultAnswerData\&quot;:  [
            {
              \&quot;answerCondition\&quot;: \&quot;answer.name == &#x27;server 1&#x27;\&quot;,
              \&quot;shouldKeep\&quot;: true
            }
          ]
        }
      ]&quot;</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/answers/pool"></div>
                    <b>pool</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/answers/pool" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The freeform name of a group of one or more records in which this record is included, such as &quot;LAX data center&quot;. An answer&#x27;s `pool` property can be referenced in `answerCondition` properties of rules using `answer.pool`.</div>
                                            <div>**Example:**</div>
                                            <div>&quot; \&quot;rules\&quot;: [
        {
          \&quot;ruleType\&quot;: \&quot;FILTER\&quot;,
          \&quot;defaultAnswerData\&quot;:  [
            {
              \&quot;answerCondition\&quot;: \&quot;answer.pool == &#x27;US East Servers&#x27;\&quot;,
              \&quot;shouldKeep\&quot;: true
            }
          ]
        }
      ]&quot;</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">pool_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/answers/rdata"></div>
                    <b>rdata</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/answers/rdata" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The record&#x27;s data, as whitespace-delimited tokens in type-specific presentation format. All RDATA is normalized and the returned presentation of your RDATA may differ from its initial input. For more information about RDATA, see <a href='https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm'>Supported DNS Resource Record Types</a>.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">rdata_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/answers/rtype"></div>
                    <b>rtype</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/answers/rtype" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of DNS record, such as A or CNAME. Only A, AAAA, and CNAME are supported. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm'>Supported DNS Resource Record Types</a>.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">rtype_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the compartment containing the steering policy.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>**Example:** `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name for the steering policy. Does not have to be unique and can be changed. Avoid entering confidential information.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>**Example:** `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/health_check_monitor_id"></div>
                    <b>health_check_monitor_id</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/health_check_monitor_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `rdata` not matching any monitored endpoint will be assumed healthy.</div>
                                            <div>**Note:** To use the Health Check monitoring feature in a steering policy, a monitor must be created using the Health Checks service first. For more information on how to create a monitor, please see <a href='https://docs.cloud.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm'>Managing Health Checks</a>.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.healthcheckmonitor.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the resource.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACTIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The series of rules that will be processed in sequence to reduce the pool of answers to a response for any given request.</div>
                                            <div>The first rule receives a shuffled list of all answers, and every other rule receives the list of answers emitted by the one preceding it. The last rule populates the response.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/cases"></div>
                    <b>cases</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/cases" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of `caseConditions`. A rule may optionally include a sequence of cases defining alternate configurations for how it should behave during processing for any given DNS query. When a rule has no sequence of `cases`, it is always evaluated with the same configuration during processing. When a rule has an empty sequence of `cases`, it is always ignored during processing. When a rule has a non-empty sequence of `cases`, its behavior during processing is configured by the first matching `case` in the sequence. When a rule has no matching cases the rule is ignored. A rule case with no `caseCondition` always matches. A rule case with a `caseCondition` matches only when that expression evaluates to true for the given query.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/cases/answer_data"></div>
                    <b>answer_data</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/cases/answer_data" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of `SteeringPolicyFilterAnswerData` objects.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/cases/answer_data/answer_condition"></div>
                    <b>answer_condition</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/cases/answer_data/answer_condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">answer.pool == &#x27;A&#x27;</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/cases/answer_data/should_keep"></div>
                    <b>should_keep</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/cases/answer_data/should_keep" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Keeps the answer only if the value is `true`.</div>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/cases/answer_data/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/cases/answer_data/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The rank assigned to the set of answers that match the expression in `answerCondition`. Answers with the lowest values move to the beginning of the list without changing the relative order of those with the same value. Answers can be given a value between `0` and `255`.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/cases/case_condition"></div>
                    <b>case_condition</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/cases/case_condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An expression that uses conditions at the time of a DNS query to indicate whether a case matches. Conditions may include the geographical location, IP subnet, or ASN the DNS query originated. **Example:** If you have an office that uses the subnet `192.0.2.0/24` you could use a `caseCondition` expression `query.client.subnet in (&#x27;192.0.2.0/24&#x27;)` to define a case that matches queries from that office.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">query.client.address in (subnet &#x27;198.51.100.0/24&#x27;)</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/cases/count"></div>
                    <b>count</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/cases/count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of answers allowed to remain after the limit rule has been processed, keeping only the first of the remaining answers in the list. Example: If the `count` property is set to `2` and four answers remain before the limit rule is processed, only the first two answers in the list will remain after the limit rule has been processed.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/default_answer_data"></div>
                    <b>default_answer_data</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/default_answer_data" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defines a default set of answer conditions and values that are applied to an answer when `cases` is not defined for the rule, or a matching case does not have any matching `answerCondition`s in its `answerData`. `defaultAnswerData` is not applied if `cases` is defined and there are no matching cases. In this scenario, the next rule will be processed.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/default_answer_data/answer_condition"></div>
                    <b>answer_condition</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/default_answer_data/answer_condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">answer.pool == &#x27;A&#x27;</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/default_answer_data/should_keep"></div>
                    <b>should_keep</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/default_answer_data/should_keep" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Keeps the answer only if the value is `true`.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/default_answer_data/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/default_answer_data/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The rank assigned to the set of answers that match the expression in `answerCondition`. Answers with the lowest values move to the beginning of the list without changing the relative order of those with the same value. Answers can be given a value between `0` and `255`.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/default_count"></div>
                    <b>default_count</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/default_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defines a default count if `cases` is not defined for the rule or a matching case does not define `count`. `defaultCount` is **not** applied if `cases` is defined and there are no matching cases. In this scenario, the next rule will be processed. If no rules remain to be processed, the answer will be chosen from the remaining list of answers.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-defined description of the rule&#x27;s purpose or behavior.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/rules/rule_type"></div>
                    <b>rule_type</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/rules/rule_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of a rule determines its sorting/filtering behavior. * `FILTER` - Filters the list of answers based on their defined boolean data. Answers remain only if their `shouldKeep` value is `true`.</div>
                                            <div>* `HEALTH` - Removes answers from the list if their `rdata` matches a target in the health check monitor referenced by the steering policy and the target is reported down.</div>
                                            <div>* `WEIGHTED` - Uses a number between 0 and 255 to determine how often an answer will be served in relation to other answers. Anwers with a higher weight will be served more frequently.</div>
                                            <div>* `PRIORITY` - Uses a defined rank value of answers to determine which answer to serve, moving those with the lowest values to the beginning of the list without changing the relative order of those with the same value. Answers can be given a value between `0` and `255`.</div>
                                            <div>* `LIMIT` - Filters answers that are too far down the list. Parameter `defaultCount` specifies how many answers to keep. **Example:** If `defaultCount` has a value of `2` and there are five answers left, when the `LIMIT` rule is processed, only the first two answers will remain in the list.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FILTER</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/template"></div>
                    <b>template</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/template" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A set of predefined rules based on the desired purpose of the steering policy. Each template utilizes Traffic Management&#x27;s rules in a different order to produce the desired results when answering DNS queries.</div>
                                            <div>**Example:** The `FAILOVER` template determines answers by filtering the policy&#x27;s answers using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`, and `LIMIT`. This gives the domain dynamic failover capability.</div>
                                            <div>It is **strongly recommended** to use a template other than `CUSTOM` when creating a steering policy.</div>
                                            <div>All templates require the rule order to begin with an unconditional `FILTER` rule that keeps answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`. The last rule of a template must must be a `LIMIT` rule. For more information about templates and code examples, see <a href='https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm'>Traffic Management API Guide</a>.</div>
                                            <div>**Template Types**</div>
                                            <div>* `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers to serve. If an endpoint fails a health check, the answer for that endpoint will be removed from the list of available answers until the endpoint is detected as healthy.</div>
                                            <div>* `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights.</div>
                                            <div>* `ROUTE_BY_GEO` - Answers DNS queries based on the query&#x27;s geographic location. For a list of geographic locations to route by, see <a href='https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm'>Traffic Management Geographic Locations</a>.</div>
                                            <div>* `ROUTE_BY_ASN` - Answers DNS queries based on the query&#x27;s originating ASN.</div>
                                            <div>* `ROUTE_BY_IP` - Answers DNS queries based on the query&#x27;s IP address.</div>
                                            <div>* `CUSTOM` - Allows a customized configuration of rules.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FAILOVER</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the resource was created, expressed in RFC 3339 timestamp format.</div>
                                            <div>**Example:** `2016-07-22T17:23:59:60Z`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-steering_policy/ttl"></div>
                    <b>ttl</b>
                    <a class="ansibleOptionLink" href="#return-steering_policy/ttl" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Time To Live (TTL) for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
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

