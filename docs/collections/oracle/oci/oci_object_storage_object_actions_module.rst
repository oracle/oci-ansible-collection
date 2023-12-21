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

.. _ansible_collections.oracle.oci.oci_object_storage_object_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_object_storage_object_actions -- Perform actions on an Object resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.39.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_object_storage_object_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on an Object resource in Oracle Cloud Infrastructure
- For *action=copy*, creates a request to copy an object within a region or to another region. See `Object Names <https://docs.cloud.oracle.com/Content/Object/Tasks/managingobjects.htm#namerequirements>`_ for object naming requirements.
- For *action=reencrypt*, re-encrypts the data encryption keys that encrypt the object and its chunks. By default, when you create a bucket, the Object Storage service manages the master encryption key used to encrypt each object's data encryption keys. The encryption mechanism that you specify for the bucket applies to the objects it contains. You can alternatively employ one of these encryption strategies for an object: - You can assign a key that you created and control through the Oracle Cloud Infrastructure Vault service. - You can encrypt an object using your own encryption key. The key you supply is known as a customer-provided encryption key (SSE-C).
- For *action=rename*, rename an object in the given Object Storage namespace. See `Object Names <https://docs.cloud.oracle.com/Content/Object/Tasks/managingobjects.htm#namerequirements>`_ for object naming requirements.
- For *action=restore*, restores one or more objects specified by the objectName parameter. By default objects will be restored for 24 hours. Duration can be configured using the hours parameter.
- For *action=update_object_storage_tier*, changes the storage tier of the object specified by the objectName parameter.


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
                                                                                                                                                                <li>copy</li>
                                                                                                                                                                                                <li>reencrypt</li>
                                                                                                                                                                                                <li>rename</li>
                                                                                                                                                                                                <li>restore</li>
                                                                                                                                                                                                <li>update_object_storage_tier</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the Object.</div>
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
                                                                                                                                                                                                <li>security_token</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-bucket_name"></div>
                    <b>bucket_name</b>
                    <a class="ansibleOptionLink" href="#parameter-bucket_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-destination_bucket"></div>
                    <b>destination_bucket</b>
                    <a class="ansibleOptionLink" href="#parameter-destination_bucket" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The destination bucket the object will be copied to.</div>
                                            <div>Required for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-destination_namespace"></div>
                    <b>destination_namespace</b>
                    <a class="ansibleOptionLink" href="#parameter-destination_namespace" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The destination Object Storage namespace the object will be copied to.</div>
                                            <div>Required for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-destination_object_if_match_e_tag"></div>
                    <b>destination_object_if_match_e_tag</b>
                    <a class="ansibleOptionLink" href="#parameter-destination_object_if_match_e_tag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The entity tag (ETag) to match against that of the destination object (an object intended to be overwritten). Used to confirm that the destination object stored under a given name is the version of that object storing a specified entity tag.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-destination_object_if_none_match_e_tag"></div>
                    <b>destination_object_if_none_match_e_tag</b>
                    <a class="ansibleOptionLink" href="#parameter-destination_object_if_none_match_e_tag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The entity tag (ETag) to avoid matching. The only valid value is &#x27;*&#x27;, which indicates that the request should fail if the object already exists in the destination bucket.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-destination_object_metadata"></div>
                    <b>destination_object_metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-destination_object_metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in &quot;opc-meta-*&quot; format. Avoid entering confidential information. Metadata key-value pairs entered in this field are assigned to the destination object. If you enter no metadata values, the destination object will inherit any existing metadata values associated with the source object.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-destination_object_name"></div>
                    <b>destination_object_name</b>
                    <a class="ansibleOptionLink" href="#parameter-destination_object_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the destination object resulting from the copy operation. Avoid entering confidential information.</div>
                                            <div>Required for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-destination_object_storage_tier"></div>
                    <b>destination_object_storage_tier</b>
                    <a class="ansibleOptionLink" href="#parameter-destination_object_storage_tier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>Standard</li>
                                                                                                                                                                                                <li>InfrequentAccess</li>
                                                                                                                                                                                                <li>Archive</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The storage tier that the object should be stored in. If not specified, the object will be stored in the same storage tier as the bucket.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-destination_region"></div>
                    <b>destination_region</b>
                    <a class="ansibleOptionLink" href="#parameter-destination_region" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The destination region the object will be copied to, for example &quot;us-ashburn-1&quot;.</div>
                                            <div>Required for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hours"></div>
                    <b>hours</b>
                    <a class="ansibleOptionLink" href="#parameter-hours" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of hours for which this object will be restored. By default objects will be restored for 24 hours. You can instead configure the duration using the hours parameter.</div>
                                            <div>Applicable only for <em>action=restore</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-kms_key_id"></div>
                    <b>kms_key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-kms_key_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the master encryption key used to call the Vault service to re-encrypt the data encryption keys associated with the object and its chunks. If the kmsKeyId value is empty, whether null or an empty string, the API will perform re-encryption by using the kmsKeyId associated with the bucket or the master encryption key managed by Oracle, depending on the bucket encryption mechanism.</div>
                                            <div>Applicable only for <em>action=reencrypt</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-namespace_name"></div>
                    <b>namespace_name</b>
                    <a class="ansibleOptionLink" href="#parameter-namespace_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Object Storage namespace used for the request.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-new_name"></div>
                    <b>new_name</b>
                    <a class="ansibleOptionLink" href="#parameter-new_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The new name of the source object. Avoid entering confidential information.</div>
                                            <div>Required for <em>action=rename</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-new_obj_if_match_e_tag"></div>
                    <b>new_obj_if_match_e_tag</b>
                    <a class="ansibleOptionLink" href="#parameter-new_obj_if_match_e_tag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The if-match entity tag (ETag) of the new object.</div>
                                            <div>Applicable only for <em>action=rename</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-new_obj_if_none_match_e_tag"></div>
                    <b>new_obj_if_none_match_e_tag</b>
                    <a class="ansibleOptionLink" href="#parameter-new_obj_if_none_match_e_tag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The if-none-match entity tag (ETag) of the new object. The only valid value is &#x27;*&#x27;, which indicates request should fail if the new object already exists.</div>
                                            <div>Applicable only for <em>action=rename</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-object_name"></div>
                    <b>object_name</b>
                    <a class="ansibleOptionLink" href="#parameter-object_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the object. Avoid entering confidential information. Example: `test/object1.log`</div>
                                            <div>Required for <em>action=reencrypt</em>, <em>action=restore</em>, <em>action=update_object_storage_tier</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-opc_source_sse_customer_algorithm"></div>
                    <b>opc_source_sse_customer_algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-opc_source_sse_customer_algorithm" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The optional header that specifies &quot;AES256&quot; as the encryption algorithm to use to decrypt the source object. For more information, see <a href='https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm'>Using Your Own Keys for Server-Side Encryption</a>.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-opc_source_sse_customer_key"></div>
                    <b>opc_source_sse_customer_key</b>
                    <a class="ansibleOptionLink" href="#parameter-opc_source_sse_customer_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The optional header that specifies the base64-encoded 256-bit encryption key to use to decrypt the source object. For more information, see <a href='https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm'>Using Your Own Keys for Server-Side Encryption</a>.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-opc_source_sse_customer_key_sha256"></div>
                    <b>opc_source_sse_customer_key_sha256</b>
                    <a class="ansibleOptionLink" href="#parameter-opc_source_sse_customer_key_sha256" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The optional header that specifies the base64-encoded SHA256 hash of the encryption key used to decrypt the source object. This value is used to check the integrity of the encryption key. For more information, see <a href='https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm'>Using Your Own Keys for Server-Side Encryption</a>.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-opc_sse_customer_algorithm"></div>
                    <b>opc_sse_customer_algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-opc_sse_customer_algorithm" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The optional header that specifies &quot;AES256&quot; as the encryption algorithm. For more information, see <a href='https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm'>Using Your Own Keys for Server-Side Encryption</a>.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-opc_sse_customer_key"></div>
                    <b>opc_sse_customer_key</b>
                    <a class="ansibleOptionLink" href="#parameter-opc_sse_customer_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data. For more information, see <a href='https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm'>Using Your Own Keys for Server-Side Encryption</a>.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-opc_sse_customer_key_sha256"></div>
                    <b>opc_sse_customer_key_sha256</b>
                    <a class="ansibleOptionLink" href="#parameter-opc_sse_customer_key_sha256" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key. For more information, see <a href='https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm'>Using Your Own Keys for Server-Side Encryption</a>.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-opc_sse_kms_key_id"></div>
                    <b>opc_sse_kms_key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-opc_sse_kms_key_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of a master encryption key used to call the Key Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                    <div class="ansibleOptionAnchor" id="parameter-source_name"></div>
                    <b>source_name</b>
                    <a class="ansibleOptionLink" href="#parameter-source_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the source object to be renamed.</div>
                                            <div>Required for <em>action=rename</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-source_object_if_match_e_tag"></div>
                    <b>source_object_if_match_e_tag</b>
                    <a class="ansibleOptionLink" href="#parameter-source_object_if_match_e_tag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The entity tag (ETag) to match against that of the source object. Used to confirm that the source object with a given name is the version of that object storing a specified ETag.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-source_object_name"></div>
                    <b>source_object_name</b>
                    <a class="ansibleOptionLink" href="#parameter-source_object_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the object to be copied.</div>
                                            <div>Required for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-source_sse_customer_key"></div>
                    <b>source_sse_customer_key</b>
                    <a class="ansibleOptionLink" href="#parameter-source_sse_customer_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable only for <em>action=reencrypt</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-source_sse_customer_key/algorithm"></div>
                    <b>algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-source_sse_customer_key/algorithm" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>AES256</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies the encryption algorithm. The only supported value is &quot;AES256&quot;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-source_sse_customer_key/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-source_sse_customer_key/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the object data.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-source_sse_customer_key/key_sha256"></div>
                    <b>key_sha256</b>
                    <a class="ansibleOptionLink" href="#parameter-source_sse_customer_key/key_sha256" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-source_version_id"></div>
                    <b>source_version_id</b>
                    <a class="ansibleOptionLink" href="#parameter-source_version_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>VersionId of the object to copy. If not provided then current version is copied by default.</div>
                                            <div>Applicable only for <em>action=copy</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-src_obj_if_match_e_tag"></div>
                    <b>src_obj_if_match_e_tag</b>
                    <a class="ansibleOptionLink" href="#parameter-src_obj_if_match_e_tag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The if-match entity tag (ETag) of the source object.</div>
                                            <div>Applicable only for <em>action=rename</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-sse_customer_key"></div>
                    <b>sse_customer_key</b>
                    <a class="ansibleOptionLink" href="#parameter-sse_customer_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable only for <em>action=reencrypt</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sse_customer_key/algorithm"></div>
                    <b>algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-sse_customer_key/algorithm" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>AES256</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specifies the encryption algorithm. The only supported value is &quot;AES256&quot;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sse_customer_key/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-sse_customer_key/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the object data.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sse_customer_key/key_sha256"></div>
                    <b>key_sha256</b>
                    <a class="ansibleOptionLink" href="#parameter-sse_customer_key/key_sha256" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity of the encryption key.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-storage_tier"></div>
                    <b>storage_tier</b>
                    <a class="ansibleOptionLink" href="#parameter-storage_tier" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>Standard</li>
                                                                                                                                                                                                <li>InfrequentAccess</li>
                                                                                                                                                                                                <li>Archive</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The storage tier that the object should be moved to.</div>
                                            <div>Required for <em>action=update_object_storage_tier</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-version_id"></div>
                    <b>version_id</b>
                    <a class="ansibleOptionLink" href="#parameter-version_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>VersionId used to identify a particular version of the object</div>
                                            <div>Applicable only for <em>action=reencrypt</em><em>action=restore</em><em>action=update_object_storage_tier</em>.</div>
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

    
    - name: Perform action copy on object
      oci_object_storage_object_actions:
        # required
        source_object_name: source_object_name_example
        destination_region: us-phoenix-1
        destination_namespace: destination_namespace_example
        destination_bucket: destination_bucket_example
        destination_object_name: destination_object_name_example
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
        action: copy

        # optional
        source_object_if_match_e_tag: source_object_if_match_e_tag_example
        source_version_id: "ocid1.sourceversion.oc1..xxxxxxEXAMPLExxxxxx"
        destination_object_if_match_e_tag: destination_object_if_match_e_tag_example
        destination_object_if_none_match_e_tag: destination_object_if_none_match_e_tag_example
        destination_object_metadata: null
        destination_object_storage_tier: Standard
        opc_sse_customer_algorithm: opc_sse_customer_algorithm_example
        opc_sse_customer_key: opc_sse_customer_key_example
        opc_sse_customer_key_sha256: opc_sse_customer_key_sha256_example
        opc_source_sse_customer_algorithm: opc_source_sse_customer_algorithm_example
        opc_source_sse_customer_key: opc_source_sse_customer_key_example
        opc_source_sse_customer_key_sha256: opc_source_sse_customer_key_sha256_example
        opc_sse_kms_key_id: "ocid1.opcssekmskey.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Perform action reencrypt on object
      oci_object_storage_object_actions:
        # required
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
        object_name: object_name_example
        action: reencrypt

        # optional
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        sse_customer_key:
          # required
          algorithm: AES256
          key: key_example
          key_sha256: key_sha256_example
        source_sse_customer_key:
          # required
          algorithm: AES256
          key: key_example
          key_sha256: key_sha256_example
        version_id: "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Perform action rename on object
      oci_object_storage_object_actions:
        # required
        source_name: source_name_example
        new_name: new_name_example
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
        action: rename

        # optional
        src_obj_if_match_e_tag: src_obj_if_match_e_tag_example
        new_obj_if_match_e_tag: new_obj_if_match_e_tag_example
        new_obj_if_none_match_e_tag: new_obj_if_none_match_e_tag_example

    - name: Perform action restore on object
      oci_object_storage_object_actions:
        # required
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
        object_name: object_name_example
        action: restore

        # optional
        hours: 56
        version_id: "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Perform action update_object_storage_tier on object
      oci_object_storage_object_actions:
        # required
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
        object_name: object_name_example
        storage_tier: Standard
        action: update_object_storage_tier

        # optional
        version_id: "ocid1.version.oc1..xxxxxxEXAMPLExxxxxx"





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
                    <div class="ansibleOptionAnchor" id="return-object"></div>
                    <b>object</b>
                    <a class="ansibleOptionLink" href="#return-object" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Object resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;archival_state&#x27;: &#x27;Archived&#x27;, &#x27;etag&#x27;: &#x27;etag_example&#x27;, &#x27;headers&#x27;: {&#x27;Content-Length&#x27;: &#x27;37&#x27;, &#x27;opc-meta-key1&#x27;: &#x27;value1&#x27;}, &#x27;md5&#x27;: &#x27;md5_example&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;size&#x27;: 56, &#x27;storage_tier&#x27;: &#x27;Standard&#x27;, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_modified&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/archival_state"></div>
                    <b>archival_state</b>
                    <a class="ansibleOptionLink" href="#return-object/archival_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Archival state of an object. This field is set only for objects in Archive tier.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Archived</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/etag"></div>
                    <b>etag</b>
                    <a class="ansibleOptionLink" href="#return-object/etag" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current entity tag (ETag) for the object.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">etag_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/headers"></div>
                    <b>headers</b>
                    <a class="ansibleOptionLink" href="#return-object/headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>response headers for the object</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Content-Length&#x27;: &#x27;37&#x27;, &#x27;opc-meta-key1&#x27;: &#x27;value1&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/md5"></div>
                    <b>md5</b>
                    <a class="ansibleOptionLink" href="#return-object/md5" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Base64-encoded MD5 hash of the object data.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">md5_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-object/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the object. Avoid entering confidential information. Example: test/object1.log</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/size"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#return-object/size" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Size of the object in bytes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/storage_tier"></div>
                    <b>storage_tier</b>
                    <a class="ansibleOptionLink" href="#return-object/storage_tier" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The storage tier that the object is stored in.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Standard</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-object/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the object was created, as described in <a href='https://tools.ietf.org/html/rfc2616#section-14.29'>RFC 2616</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object/time_modified"></div>
                    <b>time_modified</b>
                    <a class="ansibleOptionLink" href="#return-object/time_modified" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the object was modified, as described in <a href='https://tools.ietf.org/rfc/rfc2616'>RFC 2616</a>, section 14.29.</div>
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

