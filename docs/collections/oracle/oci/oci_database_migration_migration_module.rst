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

.. _ansible_collections.oracle.oci.oci_database_migration_migration_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_database_migration_migration -- Manage a Migration resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 5.5.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_database_migration_migration`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a Migration resource in Oracle Cloud Infrastructure
- For *state=present*, create a Migration resource that contains all the details to perform the database migration operation, such as source and destination database details, credentials, etc.
- This resource has the following action operations in the :ref:`oracle.oci.oci_database_migration_migration_actions <ansible_collections.oracle.oci.oci_database_migration_migration_actions_module>` module: add_migration_objects, change_compartment, remove_migration_objects.


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
                    <div class="ansibleOptionAnchor" id="parameter-advanced_parameters"></div>
                    <b>advanced_parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-advanced_parameters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of Migration Parameter objects.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-advanced_parameters/data_type"></div>
                    <b>data_type</b>
                    <a class="ansibleOptionLink" href="#parameter-advanced_parameters/data_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STRING</li>
                                                                                                                                                                                                <li>INTEGER</li>
                                                                                                                                                                                                <li>FLOAT</li>
                                                                                                                                                                                                <li>BOOLEAN</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Parameter data type.</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-advanced_parameters/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-advanced_parameters/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Parameter name.</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-advanced_parameters/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-advanced_parameters/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>If a STRING data type then the value should be an array of characters, if a INTEGER data type then the value should be an integer value, if a FLOAT data type then the value should be an float value, if a BOOLEAN data type then the value should be TRUE or FALSE.</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-advisor_settings"></div>
                    <b>advisor_settings</b>
                    <a class="ansibleOptionLink" href="#parameter-advisor_settings" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-advisor_settings/is_ignore_errors"></div>
                    <b>is_ignore_errors</b>
                    <a class="ansibleOptionLink" href="#parameter-advisor_settings/is_ignore_errors" title="Permalink to this option"></a>
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
                                            <div>True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-advisor_settings/is_skip_advisor"></div>
                    <b>is_skip_advisor</b>
                    <a class="ansibleOptionLink" href="#parameter-advisor_settings/is_skip_advisor" title="Permalink to this option"></a>
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
                                            <div>True to skip the Pre-Migration Advisor execution. Default is false.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
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
                                                                                                                                                                                                <li>security_token</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-bulk_include_exclude_data"></div>
                    <b>bulk_include_exclude_data</b>
                    <a class="ansibleOptionLink" href="#parameter-bulk_include_exclude_data" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the database objects to be excluded from the migration in bulk. The definition accepts input in a CSV format, newline separated for each entry. More details can be found in the documentation.</div>
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
                                            <div>The OCID of the resource being referenced.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>Required for delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details"></div>
                    <b>data_transfer_medium_details</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/access_key_id"></div>
                    <b>access_key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/access_key_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>AWS access key credentials identifier Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;AWS_S3&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;DBLINK&#x27;, &#x27;AWS_S3&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/object_storage_bucket"></div>
                    <b>object_storage_bucket</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/object_storage_bucket" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/object_storage_bucket/bucket_name"></div>
                    <b>bucket_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/object_storage_bucket/bucket_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Bucket name.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;OBJECT_STORAGE&#x27;, &#x27;DBLINK&#x27;, &#x27;NFS&#x27;]</div>
                                            <div>Required when type is one of [&#x27;OBJECT_STORAGE&#x27;, &#x27;AWS_S3&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/object_storage_bucket/namespace_name"></div>
                    <b>namespace_name</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/object_storage_bucket/namespace_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Namespace name of the object store bucket.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;OBJECT_STORAGE&#x27;, &#x27;DBLINK&#x27;, &#x27;NFS&#x27;]</div>
                                            <div>Required when type is one of [&#x27;OBJECT_STORAGE&#x27;, &#x27;AWS_S3&#x27;]</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/region" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>AWS region code where the S3 bucket is located. Region code should match the documented available regions: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;AWS_S3&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/secret_access_key"></div>
                    <b>secret_access_key</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/secret_access_key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>AWS secret access key credentials Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;AWS_S3&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/shared_storage_mount_target_id"></div>
                    <b>shared_storage_mount_target_id</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/shared_storage_mount_target_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>OCID of the shared storage mount target</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;NFS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/source"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when type is one of [&#x27;OBJECT_STORAGE&#x27;, &#x27;NFS&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/source/kind"></div>
                    <b>kind</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/source/kind" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OCI_CLI</li>
                                                                                                                                                                                                <li>CURL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of dump transfer to use during migration in source or target host. Default kind is CURL</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/source/oci_home"></div>
                    <b>oci_home</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/source/oci_home" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Path to the OCI CLI installation in the node.</div>
                                            <div>Applicable when kind is &#x27;OCI_CLI&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/source/wallet_location"></div>
                    <b>wallet_location</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/source/wallet_location" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Directory path to OCI SSL wallet location on Db server node.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/target"></div>
                    <b>target</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/target" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when type is one of [&#x27;OBJECT_STORAGE&#x27;, &#x27;NFS&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/target/kind"></div>
                    <b>kind</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/target/kind" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OCI_CLI</li>
                                                                                                                                                                                                <li>CURL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of dump transfer to use during migration in source or target host. Default kind is CURL</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/target/oci_home"></div>
                    <b>oci_home</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/target/oci_home" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Path to the OCI CLI installation in the node.</div>
                                            <div>Applicable when kind is &#x27;OCI_CLI&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/target/wallet_location"></div>
                    <b>wallet_location</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/target/wallet_location" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Directory path to OCI SSL wallet location on Db server node.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-data_transfer_medium_details/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-data_transfer_medium_details/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OBJECT_STORAGE</li>
                                                                                                                                                                                                <li>DBLINK</li>
                                                                                                                                                                                                <li>NFS</li>
                                                                                                                                                                                                <li>AWS_S3</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the data transfer medium to use.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database_combination"></div>
                    <b>database_combination</b>
                    <a class="ansibleOptionLink" href="#parameter-database_combination" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>MYSQL</li>
                                                                                                                                                                                                <li>ORACLE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The combination of source and target databases participating in a migration. Example: ORACLE means the migration is meant for migrating Oracle source and target databases.</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with migration_id present.</div>
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
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                            <div>This parameter is updatable.</div>
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
                                            <div>A user-friendly description. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
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
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                            <div>Required for create, update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_objects"></div>
                    <b>exclude_objects</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_objects" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Database objects to exclude from migration, cannot be specified alongside &#x27;includeObjects&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_objects/is_omit_excluded_table_from_replication"></div>
                    <b>is_omit_excluded_table_from_replication</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_objects/is_omit_excluded_table_from_replication" title="Permalink to this option"></a>
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
                                            <div>Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and object status EXCLUDE.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_objects/object_name"></div>
                    <b>object_name</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_objects/object_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the object (regular expression is allowed)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_objects/owner"></div>
                    <b>owner</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_objects/owner" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Owner of the object (regular expression is allowed)</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_objects/schema"></div>
                    <b>schema</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_objects/schema" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Schema of the object (regular expression is allowed)</div>
                                            <div>Required when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_objects/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_objects/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Type of object to exclude. If not specified, matching owners and object names of type TABLE would be excluded.</div>
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
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see Resource Tags. Example: {&quot;Department&quot;: &quot;Finance&quot;}</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-ggs_details"></div>
                    <b>ggs_details</b>
                    <a class="ansibleOptionLink" href="#parameter-ggs_details" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ggs_details/acceptable_lag"></div>
                    <b>acceptable_lag</b>
                    <a class="ansibleOptionLink" href="#parameter-ggs_details/acceptable_lag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ggs_details/extract"></div>
                    <b>extract</b>
                    <a class="ansibleOptionLink" href="#parameter-ggs_details/extract" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ggs_details/extract/long_trans_duration"></div>
                    <b>long_trans_duration</b>
                    <a class="ansibleOptionLink" href="#parameter-ggs_details/extract/long_trans_duration" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running. If not specified, Extract will not generate a warning on long-running transactions.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ggs_details/extract/performance_profile"></div>
                    <b>performance_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-ggs_details/extract/performance_profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>LOW</li>
                                                                                                                                                                                                <li>MEDIUM</li>
                                                                                                                                                                                                <li>HIGH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Extract performance.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ggs_details/replicat"></div>
                    <b>replicat</b>
                    <a class="ansibleOptionLink" href="#parameter-ggs_details/replicat" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-ggs_details/replicat/performance_profile"></div>
                    <b>performance_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-ggs_details/replicat/performance_profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>LOW</li>
                                                                                                                                                                                                <li>HIGH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Replicat performance.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details"></div>
                    <b>hub_details</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/acceptable_lag"></div>
                    <b>acceptable_lag</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/acceptable_lag" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/compute_id"></div>
                    <b>compute_id</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/compute_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/extract"></div>
                    <b>extract</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/extract" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/extract/long_trans_duration"></div>
                    <b>long_trans_duration</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/extract/long_trans_duration" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running. If not specified, Extract will not generate a warning on long-running transactions.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/extract/performance_profile"></div>
                    <b>performance_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/extract/performance_profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>LOW</li>
                                                                                                                                                                                                <li>MEDIUM</li>
                                                                                                                                                                                                <li>HIGH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Extract performance.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/key_id"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/key_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/replicat"></div>
                    <b>replicat</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/replicat" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/replicat/performance_profile"></div>
                    <b>performance_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/replicat/performance_profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>LOW</li>
                                                                                                                                                                                                <li>HIGH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Replicat performance.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/rest_admin_credentials"></div>
                    <b>rest_admin_credentials</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/rest_admin_credentials" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/rest_admin_credentials/password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/rest_admin_credentials/password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Administrator password</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/rest_admin_credentials/username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/rest_admin_credentials/username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Administrator username</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/url"></div>
                    <b>url</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Endpoint URL.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hub_details/vault_id"></div>
                    <b>vault_id</b>
                    <a class="ansibleOptionLink" href="#parameter-hub_details/vault_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-include_objects"></div>
                    <b>include_objects</b>
                    <a class="ansibleOptionLink" href="#parameter-include_objects" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Database objects to include from migration, cannot be specified alongside &#x27;excludeObjects&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-include_objects/is_omit_excluded_table_from_replication"></div>
                    <b>is_omit_excluded_table_from_replication</b>
                    <a class="ansibleOptionLink" href="#parameter-include_objects/is_omit_excluded_table_from_replication" title="Permalink to this option"></a>
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
                                            <div>Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and object status EXCLUDE.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-include_objects/object_name"></div>
                    <b>object_name</b>
                    <a class="ansibleOptionLink" href="#parameter-include_objects/object_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the object (regular expression is allowed)</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-include_objects/owner"></div>
                    <b>owner</b>
                    <a class="ansibleOptionLink" href="#parameter-include_objects/owner" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Owner of the object (regular expression is allowed)</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-include_objects/schema"></div>
                    <b>schema</b>
                    <a class="ansibleOptionLink" href="#parameter-include_objects/schema" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Schema of the object (regular expression is allowed)</div>
                                            <div>Required when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-include_objects/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-include_objects/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Type of object to exclude. If not specified, matching owners and object names of type TABLE would be excluded.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings"></div>
                    <b>initial_load_settings</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings" title="Permalink to this option"></a>
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
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/compatibility"></div>
                    <b>compatibility</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/compatibility" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Apply the specified requirements for compatibility with MySQL Database Service for all tables in the dump output, altering the dump files as necessary.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/data_pump_parameters"></div>
                    <b>data_pump_parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/data_pump_parameters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/data_pump_parameters/estimate"></div>
                    <b>estimate</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/data_pump_parameters/estimate" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>BLOCKS</li>
                                                                                                                                                                                                <li>STATISTICS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Estimate size of dumps that will be generated.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/data_pump_parameters/exclude_parameters"></div>
                    <b>exclude_parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/data_pump_parameters/exclude_parameters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Exclude paratemers for Export and Import.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/data_pump_parameters/export_parallelism_degree"></div>
                    <b>export_parallelism_degree</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/data_pump_parameters/export_parallelism_degree" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum number of worker processes that can be used for a Data Pump Export job.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/data_pump_parameters/import_parallelism_degree"></div>
                    <b>import_parallelism_degree</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/data_pump_parameters/import_parallelism_degree" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum number of worker processes that can be used for a Data Pump Import job. For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/data_pump_parameters/is_cluster"></div>
                    <b>is_cluster</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/data_pump_parameters/is_cluster" title="Permalink to this option"></a>
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
                                            <div>Set to false to force Data Pump worker process to run on one instance.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/data_pump_parameters/table_exists_action"></div>
                    <b>table_exists_action</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/data_pump_parameters/table_exists_action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>TRUNCATE</li>
                                                                                                                                                                                                <li>REPLACE</li>
                                                                                                                                                                                                <li>APPEND</li>
                                                                                                                                                                                                <li>SKIP</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/export_directory_object"></div>
                    <b>export_directory_object</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/export_directory_object" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/export_directory_object/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/export_directory_object/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of directory object in database</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/export_directory_object/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/export_directory_object/path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Absolute path of directory on database server</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/handle_grant_errors"></div>
                    <b>handle_grant_errors</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/handle_grant_errors" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ABORT</li>
                                                                                                                                                                                                <li>DROP_ACCOUNT</li>
                                                                                                                                                                                                <li>IGNORE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action taken in the event of errors related to GRANT or REVOKE errors.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/import_directory_object"></div>
                    <b>import_directory_object</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/import_directory_object" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/import_directory_object/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/import_directory_object/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of directory object in database</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/import_directory_object/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/import_directory_object/path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Absolute path of directory on database server</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/is_consistent"></div>
                    <b>is_consistent</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/is_consistent" title="Permalink to this option"></a>
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
                                            <div>Enable (true) or disable (false) consistent data dumps by locking the instance for backup during the dump.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/is_ignore_existing_objects"></div>
                    <b>is_ignore_existing_objects</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/is_ignore_existing_objects" title="Permalink to this option"></a>
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
                                            <div>Import the dump even if it contains objects that already exist in the target schema in the MySQL instance.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/is_tz_utc"></div>
                    <b>is_tz_utc</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/is_tz_utc" title="Permalink to this option"></a>
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
                                            <div>Include a statement at the start of the dump to set the time zone to UTC.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/job_mode"></div>
                    <b>job_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/job_mode" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>FULL</li>
                                                                                                                                                                                                <li>SCHEMA</li>
                                                                                                                                                                                                <li>TABLE</li>
                                                                                                                                                                                                <li>TABLESPACE</li>
                                                                                                                                                                                                <li>TRANSPORTABLE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>MySql Job Mode</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/metadata_remaps"></div>
                    <b>metadata_remaps</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/metadata_remaps" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defines remapping to be applied to objects as they are processed.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/metadata_remaps/new_value"></div>
                    <b>new_value</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/metadata_remaps/new_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the new value that oldValue should be translated into.</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/metadata_remaps/old_value"></div>
                    <b>old_value</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/metadata_remaps/old_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the value which needs to be reset.</div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/metadata_remaps/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/metadata_remaps/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SCHEMA</li>
                                                                                                                                                                                                <li>TABLESPACE</li>
                                                                                                                                                                                                <li>DATAFILE</li>
                                                                                                                                                                                                <li>TABLE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of remap. Refer to <a href='https://docs.oracle.com/en/database/oracle/oracle- database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D'>METADATA_REMAP Procedure </a></div>
                                            <div>Required when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/primary_key_compatibility"></div>
                    <b>primary_key_compatibility</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/primary_key_compatibility" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NONE</li>
                                                                                                                                                                                                <li>IGNORE_MISSING_PKS</li>
                                                                                                                                                                                                <li>CREATE_INVISIBLE_PKS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Primary key compatibility option</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;MYSQL&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/tablespace_details"></div>
                    <b>tablespace_details</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/tablespace_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/tablespace_details/block_size_in_kbs"></div>
                    <b>block_size_in_kbs</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/tablespace_details/block_size_in_kbs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SIZE_8K</li>
                                                                                                                                                                                                <li>SIZE_16K</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Size of Oracle database blocks in KB.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when target_type is one of [&#x27;ADB_D_AUTOCREATE&#x27;, &#x27;NON_ADB_AUTOCREATE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/tablespace_details/extend_size_in_mbs"></div>
                    <b>extend_size_in_mbs</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/tablespace_details/extend_size_in_mbs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Size of extend in MB. Can only be specified if &#x27;isBigFile&#x27; property is set to true.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when target_type is one of [&#x27;ADB_D_AUTOCREATE&#x27;, &#x27;NON_ADB_AUTOCREATE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/tablespace_details/is_auto_create"></div>
                    <b>is_auto_create</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/tablespace_details/is_auto_create" title="Permalink to this option"></a>
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
                                            <div>True to auto-create tablespace in the target Database.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when target_type is one of [&#x27;ADB_D_AUTOCREATE&#x27;, &#x27;NON_ADB_AUTOCREATE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/tablespace_details/is_big_file"></div>
                    <b>is_big_file</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/tablespace_details/is_big_file" title="Permalink to this option"></a>
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
                                            <div>True set tablespace to big file.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when target_type is one of [&#x27;ADB_D_AUTOCREATE&#x27;, &#x27;NON_ADB_AUTOCREATE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/tablespace_details/remap_target"></div>
                    <b>remap_target</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/tablespace_details/remap_target" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of tablespace at target to which the source database tablespace need to be remapped.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when target_type is one of [&#x27;ADB_D_REMAP&#x27;, &#x27;NON_ADB_REMAP&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-initial_load_settings/tablespace_details/target_type"></div>
                    <b>target_type</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_load_settings/tablespace_details/target_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NON_ADB_AUTOCREATE</li>
                                                                                                                                                                                                <li>NON_ADB_REMAP</li>
                                                                                                                                                                                                <li>ADB_D_REMAP</li>
                                                                                                                                                                                                <li>ADB_S_REMAP</li>
                                                                                                                                                                                                <li>ADB_D_AUTOCREATE</li>
                                                                                                                                                                                                <li>TARGET_DEFAULTS_REMAP</li>
                                                                                                                                                                                                <li>TARGET_DEFAULTS_AUTOCREATE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of Database Base Migration Target.</div>
                                            <div>This parameter is updatable.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-migration_id"></div>
                    <b>migration_id</b>
                    <a class="ansibleOptionLink" href="#parameter-migration_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the migration</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                    <div class="ansibleOptionAnchor" id="parameter-source_container_database_connection_id"></div>
                    <b>source_container_database_connection_id</b>
                    <a class="ansibleOptionLink" href="#parameter-source_container_database_connection_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is &#x27;ORACLE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-source_database_connection_id"></div>
                    <b>source_database_connection_id</b>
                    <a class="ansibleOptionLink" href="#parameter-source_database_connection_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is one of [&#x27;MYSQL&#x27;, &#x27;ORACLE&#x27;]</div>
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
                                            <div>The state of the Migration.</div>
                                            <div>Use <em>state=present</em> to create or update a Migration.</div>
                                            <div>Use <em>state=absent</em> to delete a Migration.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-target_database_connection_id"></div>
                    <b>target_database_connection_id</b>
                    <a class="ansibleOptionLink" href="#parameter-target_database_connection_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is one of [&#x27;MYSQL&#x27;, &#x27;ORACLE&#x27;]</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ONLINE</li>
                                                                                                                                                                                                <li>OFFLINE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of the migration to be performed. Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when database_combination is one of [&#x27;MYSQL&#x27;, &#x27;ORACLE&#x27;]</div>
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

    
    - name: Create migration with database_combination = MYSQL
      oci_database_migration_migration:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_combination: MYSQL

        # optional
        exclude_objects:
        - # required
          object_name: object_name_example

          # optional
          schema: schema_example
          owner: owner_example
          type: type_example
          is_omit_excluded_table_from_replication: true
        include_objects:
        - # required
          object_name: object_name_example

          # optional
          schema: schema_example
          owner: owner_example
          type: type_example
          is_omit_excluded_table_from_replication: true
        bulk_include_exclude_data: bulk_include_exclude_data_example
        description: description_example
        type: ONLINE
        display_name: display_name_example
        source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        data_transfer_medium_details:
          # required
          type: OBJECT_STORAGE

          # optional
          source:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          target:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          object_storage_bucket:
            # optional
            namespace_name: namespace_name_example
            bucket_name: bucket_name_example
        initial_load_settings:
          # required
          job_mode: FULL

          # optional
          is_consistent: true
          is_tz_utc: true
          compatibility: [ "compatibility_example" ]
          primary_key_compatibility: NONE
          is_ignore_existing_objects: true
          handle_grant_errors: ABORT
          data_pump_parameters:
            # optional
            is_cluster: true
            estimate: BLOCKS
            table_exists_action: TRUNCATE
            exclude_parameters: [ "exclude_parameters_example" ]
            import_parallelism_degree: 56
            export_parallelism_degree: 56
          tablespace_details:
            # required
            target_type: NON_ADB_AUTOCREATE

            # optional
            is_auto_create: true
            is_big_file: true
            extend_size_in_mbs: 56
            block_size_in_kbs: SIZE_8K
          export_directory_object:
            # optional
            name: name_example
            path: path_example
          import_directory_object:
            # optional
            name: name_example
            path: path_example
          metadata_remaps:
          - # required
            type: SCHEMA
            old_value: old_value_example
            new_value: new_value_example
        advisor_settings:
          # optional
          is_skip_advisor: true
          is_ignore_errors: true
        hub_details:
          # optional
          rest_admin_credentials:
            # optional
            username: username_example
            password: example-password
          url: url_example
          compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        ggs_details:
          # optional
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56

    - name: Create migration with database_combination = ORACLE
      oci_database_migration_migration:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_combination: ORACLE

        # optional
        exclude_objects:
        - # required
          object_name: object_name_example

          # optional
          schema: schema_example
          owner: owner_example
          type: type_example
          is_omit_excluded_table_from_replication: true
        include_objects:
        - # required
          object_name: object_name_example

          # optional
          schema: schema_example
          owner: owner_example
          type: type_example
          is_omit_excluded_table_from_replication: true
        bulk_include_exclude_data: bulk_include_exclude_data_example
        description: description_example
        type: ONLINE
        display_name: display_name_example
        source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        data_transfer_medium_details:
          # required
          type: OBJECT_STORAGE

          # optional
          source:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          target:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          object_storage_bucket:
            # optional
            namespace_name: namespace_name_example
            bucket_name: bucket_name_example
        initial_load_settings:
          # required
          job_mode: FULL

          # optional
          is_consistent: true
          is_tz_utc: true
          compatibility: [ "compatibility_example" ]
          primary_key_compatibility: NONE
          is_ignore_existing_objects: true
          handle_grant_errors: ABORT
          data_pump_parameters:
            # optional
            is_cluster: true
            estimate: BLOCKS
            table_exists_action: TRUNCATE
            exclude_parameters: [ "exclude_parameters_example" ]
            import_parallelism_degree: 56
            export_parallelism_degree: 56
          tablespace_details:
            # required
            target_type: NON_ADB_AUTOCREATE

            # optional
            is_auto_create: true
            is_big_file: true
            extend_size_in_mbs: 56
            block_size_in_kbs: SIZE_8K
          export_directory_object:
            # optional
            name: name_example
            path: path_example
          import_directory_object:
            # optional
            name: name_example
            path: path_example
          metadata_remaps:
          - # required
            type: SCHEMA
            old_value: old_value_example
            new_value: new_value_example
        advisor_settings:
          # optional
          is_skip_advisor: true
          is_ignore_errors: true
        hub_details:
          # optional
          rest_admin_credentials:
            # optional
            username: username_example
            password: example-password
          url: url_example
          compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        ggs_details:
          # optional
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        advanced_parameters:
        - # required
          value: value_example
          name: name_example
          data_type: STRING
        source_container_database_connection_id: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update migration with database_combination = MYSQL
      oci_database_migration_migration:
        # required
        database_combination: MYSQL

        # optional
        description: description_example
        type: ONLINE
        display_name: display_name_example
        source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        data_transfer_medium_details:
          # required
          type: OBJECT_STORAGE

          # optional
          source:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          target:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          object_storage_bucket:
            # optional
            namespace_name: namespace_name_example
            bucket_name: bucket_name_example
        initial_load_settings:
          # required
          job_mode: FULL

          # optional
          is_consistent: true
          is_tz_utc: true
          compatibility: [ "compatibility_example" ]
          primary_key_compatibility: NONE
          is_ignore_existing_objects: true
          handle_grant_errors: ABORT
          data_pump_parameters:
            # optional
            is_cluster: true
            estimate: BLOCKS
            table_exists_action: TRUNCATE
            exclude_parameters: [ "exclude_parameters_example" ]
            import_parallelism_degree: 56
            export_parallelism_degree: 56
          tablespace_details:
            # required
            target_type: NON_ADB_AUTOCREATE

            # optional
            is_auto_create: true
            is_big_file: true
            extend_size_in_mbs: 56
            block_size_in_kbs: SIZE_8K
          export_directory_object:
            # optional
            name: name_example
            path: path_example
          import_directory_object:
            # optional
            name: name_example
            path: path_example
          metadata_remaps:
          - # required
            type: SCHEMA
            old_value: old_value_example
            new_value: new_value_example
        advisor_settings:
          # optional
          is_skip_advisor: true
          is_ignore_errors: true
        hub_details:
          # optional
          rest_admin_credentials:
            # optional
            username: username_example
            password: example-password
          url: url_example
          compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        ggs_details:
          # optional
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56

    - name: Update migration with database_combination = ORACLE
      oci_database_migration_migration:
        # required
        database_combination: ORACLE

        # optional
        description: description_example
        type: ONLINE
        display_name: display_name_example
        source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        data_transfer_medium_details:
          # required
          type: OBJECT_STORAGE

          # optional
          source:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          target:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          object_storage_bucket:
            # optional
            namespace_name: namespace_name_example
            bucket_name: bucket_name_example
        initial_load_settings:
          # required
          job_mode: FULL

          # optional
          is_consistent: true
          is_tz_utc: true
          compatibility: [ "compatibility_example" ]
          primary_key_compatibility: NONE
          is_ignore_existing_objects: true
          handle_grant_errors: ABORT
          data_pump_parameters:
            # optional
            is_cluster: true
            estimate: BLOCKS
            table_exists_action: TRUNCATE
            exclude_parameters: [ "exclude_parameters_example" ]
            import_parallelism_degree: 56
            export_parallelism_degree: 56
          tablespace_details:
            # required
            target_type: NON_ADB_AUTOCREATE

            # optional
            is_auto_create: true
            is_big_file: true
            extend_size_in_mbs: 56
            block_size_in_kbs: SIZE_8K
          export_directory_object:
            # optional
            name: name_example
            path: path_example
          import_directory_object:
            # optional
            name: name_example
            path: path_example
          metadata_remaps:
          - # required
            type: SCHEMA
            old_value: old_value_example
            new_value: new_value_example
        advisor_settings:
          # optional
          is_skip_advisor: true
          is_ignore_errors: true
        hub_details:
          # optional
          rest_admin_credentials:
            # optional
            username: username_example
            password: example-password
          url: url_example
          compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        ggs_details:
          # optional
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        advanced_parameters:
        - # required
          value: value_example
          name: name_example
          data_type: STRING
        source_container_database_connection_id: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Update migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with database_combination = MYSQL
      oci_database_migration_migration:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_combination: MYSQL

        # optional
        description: description_example
        type: ONLINE
        display_name: display_name_example
        source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        data_transfer_medium_details:
          # required
          type: OBJECT_STORAGE

          # optional
          source:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          target:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          object_storage_bucket:
            # optional
            namespace_name: namespace_name_example
            bucket_name: bucket_name_example
        initial_load_settings:
          # required
          job_mode: FULL

          # optional
          is_consistent: true
          is_tz_utc: true
          compatibility: [ "compatibility_example" ]
          primary_key_compatibility: NONE
          is_ignore_existing_objects: true
          handle_grant_errors: ABORT
          data_pump_parameters:
            # optional
            is_cluster: true
            estimate: BLOCKS
            table_exists_action: TRUNCATE
            exclude_parameters: [ "exclude_parameters_example" ]
            import_parallelism_degree: 56
            export_parallelism_degree: 56
          tablespace_details:
            # required
            target_type: NON_ADB_AUTOCREATE

            # optional
            is_auto_create: true
            is_big_file: true
            extend_size_in_mbs: 56
            block_size_in_kbs: SIZE_8K
          export_directory_object:
            # optional
            name: name_example
            path: path_example
          import_directory_object:
            # optional
            name: name_example
            path: path_example
          metadata_remaps:
          - # required
            type: SCHEMA
            old_value: old_value_example
            new_value: new_value_example
        advisor_settings:
          # optional
          is_skip_advisor: true
          is_ignore_errors: true
        hub_details:
          # optional
          rest_admin_credentials:
            # optional
            username: username_example
            password: example-password
          url: url_example
          compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        ggs_details:
          # optional
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56

    - name: Update migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with database_combination = ORACLE
      oci_database_migration_migration:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        database_combination: ORACLE

        # optional
        description: description_example
        type: ONLINE
        display_name: display_name_example
        source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        data_transfer_medium_details:
          # required
          type: OBJECT_STORAGE

          # optional
          source:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          target:
            # required
            kind: OCI_CLI

            # optional
            oci_home: oci_home_example
            wallet_location: wallet_location_example
          object_storage_bucket:
            # optional
            namespace_name: namespace_name_example
            bucket_name: bucket_name_example
        initial_load_settings:
          # required
          job_mode: FULL

          # optional
          is_consistent: true
          is_tz_utc: true
          compatibility: [ "compatibility_example" ]
          primary_key_compatibility: NONE
          is_ignore_existing_objects: true
          handle_grant_errors: ABORT
          data_pump_parameters:
            # optional
            is_cluster: true
            estimate: BLOCKS
            table_exists_action: TRUNCATE
            exclude_parameters: [ "exclude_parameters_example" ]
            import_parallelism_degree: 56
            export_parallelism_degree: 56
          tablespace_details:
            # required
            target_type: NON_ADB_AUTOCREATE

            # optional
            is_auto_create: true
            is_big_file: true
            extend_size_in_mbs: 56
            block_size_in_kbs: SIZE_8K
          export_directory_object:
            # optional
            name: name_example
            path: path_example
          import_directory_object:
            # optional
            name: name_example
            path: path_example
          metadata_remaps:
          - # required
            type: SCHEMA
            old_value: old_value_example
            new_value: new_value_example
        advisor_settings:
          # optional
          is_skip_advisor: true
          is_ignore_errors: true
        hub_details:
          # optional
          rest_admin_credentials:
            # optional
            username: username_example
            password: example-password
          url: url_example
          compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        ggs_details:
          # optional
          extract:
            # optional
            performance_profile: LOW
            long_trans_duration: 56
          replicat:
            # optional
            performance_profile: LOW
          acceptable_lag: 56
        advanced_parameters:
        - # required
          value: value_example
          name: name_example
          data_type: STRING
        source_container_database_connection_id: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"

    - name: Delete migration
      oci_database_migration_migration:
        # required
        migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

    - name: Delete migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_database_migration_migration:
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
            <th colspan="4">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-migration"></div>
                    <b>migration</b>
                    <a class="ansibleOptionLink" href="#return-migration" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Migration resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;advanced_parameters&#x27;: [{&#x27;data_type&#x27;: &#x27;STRING&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}], &#x27;advisor_settings&#x27;: {&#x27;is_ignore_errors&#x27;: True, &#x27;is_skip_advisor&#x27;: True}, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;data_transfer_medium_details&#x27;: {&#x27;access_key_id&#x27;: &#x27;ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;object_storage_bucket&#x27;: {&#x27;bucket_name&#x27;: &#x27;bucket_name_example&#x27;, &#x27;namespace_name&#x27;: &#x27;namespace_name_example&#x27;}, &#x27;region&#x27;: &#x27;us-phoenix-1&#x27;, &#x27;secret_access_key&#x27;: &#x27;secret_access_key_example&#x27;, &#x27;shared_storage_mount_target_id&#x27;: &#x27;ocid1.sharedstoragemounttarget.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;source&#x27;: {&#x27;kind&#x27;: &#x27;CURL&#x27;, &#x27;oci_home&#x27;: &#x27;oci_home_example&#x27;, &#x27;wallet_location&#x27;: &#x27;wallet_location_example&#x27;}, &#x27;target&#x27;: {&#x27;kind&#x27;: &#x27;CURL&#x27;, &#x27;oci_home&#x27;: &#x27;oci_home_example&#x27;, &#x27;wallet_location&#x27;: &#x27;wallet_location_example&#x27;}, &#x27;type&#x27;: &#x27;OBJECT_STORAGE&#x27;}, &#x27;database_combination&#x27;: &#x27;MYSQL&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;executing_job_id&#x27;: &#x27;ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;ggs_details&#x27;: {&#x27;acceptable_lag&#x27;: 56, &#x27;extract&#x27;: {&#x27;long_trans_duration&#x27;: 56, &#x27;performance_profile&#x27;: &#x27;LOW&#x27;}, &#x27;ggs_deployment&#x27;: {&#x27;deployment_id&#x27;: &#x27;ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;ggs_admin_credentials_secret_id&#x27;: &#x27;ocid1.ggsadmincredentialssecret.oc1..xxxxxxEXAMPLExxxxxx&#x27;}, &#x27;replicat&#x27;: {&#x27;performance_profile&#x27;: &#x27;LOW&#x27;}}, &#x27;hub_details&#x27;: {&#x27;acceptable_lag&#x27;: 56, &#x27;compute_id&#x27;: &#x27;ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;extract&#x27;: {&#x27;long_trans_duration&#x27;: 56, &#x27;performance_profile&#x27;: &#x27;LOW&#x27;}, &#x27;key_id&#x27;: &#x27;ocid1.key.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;replicat&#x27;: {&#x27;performance_profile&#x27;: &#x27;LOW&#x27;}, &#x27;rest_admin_credentials&#x27;: {&#x27;username&#x27;: &#x27;username_example&#x27;}, &#x27;url&#x27;: &#x27;url_example&#x27;, &#x27;vault_id&#x27;: &#x27;ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;initial_load_settings&#x27;: {&#x27;compatibility&#x27;: [], &#x27;data_pump_parameters&#x27;: {&#x27;estimate&#x27;: &#x27;BLOCKS&#x27;, &#x27;exclude_parameters&#x27;: [], &#x27;export_parallelism_degree&#x27;: 56, &#x27;import_parallelism_degree&#x27;: 56, &#x27;is_cluster&#x27;: True, &#x27;table_exists_action&#x27;: &#x27;TRUNCATE&#x27;}, &#x27;export_directory_object&#x27;: {&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;path&#x27;: &#x27;path_example&#x27;}, &#x27;handle_grant_errors&#x27;: &#x27;ABORT&#x27;, &#x27;import_directory_object&#x27;: {&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;path&#x27;: &#x27;path_example&#x27;}, &#x27;is_consistent&#x27;: True, &#x27;is_ignore_existing_objects&#x27;: True, &#x27;is_tz_utc&#x27;: True, &#x27;job_mode&#x27;: &#x27;FULL&#x27;, &#x27;metadata_remaps&#x27;: [{&#x27;new_value&#x27;: &#x27;new_value_example&#x27;, &#x27;old_value&#x27;: &#x27;old_value_example&#x27;, &#x27;type&#x27;: &#x27;SCHEMA&#x27;}], &#x27;primary_key_compatibility&#x27;: &#x27;NONE&#x27;, &#x27;tablespace_details&#x27;: {&#x27;block_size_in_kbs&#x27;: &#x27;SIZE_8K&#x27;, &#x27;extend_size_in_mbs&#x27;: 56, &#x27;is_auto_create&#x27;: True, &#x27;is_big_file&#x27;: True, &#x27;remap_target&#x27;: &#x27;remap_target_example&#x27;, &#x27;target_type&#x27;: &#x27;ADB_S_REMAP&#x27;}}, &#x27;lifecycle_details&#x27;: &#x27;READY&#x27;, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;source_container_database_connection_id&#x27;: &#x27;ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;source_database_connection_id&#x27;: &#x27;ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;system_tags&#x27;: {}, &#x27;target_database_connection_id&#x27;: &#x27;ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_last_migration&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;type&#x27;: &#x27;ONLINE&#x27;, &#x27;wait_after&#x27;: &#x27;ODMS_VALIDATE_TGT&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/advanced_parameters"></div>
                    <b>advanced_parameters</b>
                    <a class="ansibleOptionLink" href="#return-migration/advanced_parameters" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of Migration Parameter objects.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/advanced_parameters/data_type"></div>
                    <b>data_type</b>
                    <a class="ansibleOptionLink" href="#return-migration/advanced_parameters/data_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Parameter data type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">STRING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/advanced_parameters/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-migration/advanced_parameters/name" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/advanced_parameters/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-migration/advanced_parameters/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>If a STRING data type then the value should be an array of characters, if a INTEGER data type then the value should be an integer value, if a FLOAT data type then the value should be an float value, if a BOOLEAN data type then the value should be TRUE or FALSE.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/advisor_settings"></div>
                    <b>advisor_settings</b>
                    <a class="ansibleOptionLink" href="#return-migration/advisor_settings" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/advisor_settings/is_ignore_errors"></div>
                    <b>is_ignore_errors</b>
                    <a class="ansibleOptionLink" href="#return-migration/advisor_settings/is_ignore_errors" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/advisor_settings/is_skip_advisor"></div>
                    <b>is_skip_advisor</b>
                    <a class="ansibleOptionLink" href="#return-migration/advisor_settings/is_skip_advisor" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>True to skip the Pre-Migration Advisor execution. Default is false.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details"></div>
                    <b>data_transfer_medium_details</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/access_key_id"></div>
                    <b>access_key_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/access_key_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>AWS access key credentials identifier Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>S3 bucket name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/object_storage_bucket"></div>
                    <b>object_storage_bucket</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/object_storage_bucket" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/object_storage_bucket/bucket_name"></div>
                    <b>bucket_name</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/object_storage_bucket/bucket_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Bucket name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">bucket_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/object_storage_bucket/namespace_name"></div>
                    <b>namespace_name</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/object_storage_bucket/namespace_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Namespace name of the object store bucket.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">namespace_name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/region" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>AWS region code where the S3 bucket is located. Region code should match the documented available regions: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">us-phoenix-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/secret_access_key"></div>
                    <b>secret_access_key</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/secret_access_key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>AWS secret access key credentials Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">secret_access_key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/shared_storage_mount_target_id"></div>
                    <b>shared_storage_mount_target_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/shared_storage_mount_target_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>OCID of the shared storage mount target</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.sharedstoragemounttarget.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/source"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/source" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/source/kind"></div>
                    <b>kind</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/source/kind" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of dump transfer to use during migration in source or target host. Default kind is CURL</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CURL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/source/oci_home"></div>
                    <b>oci_home</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/source/oci_home" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Path to the OCI CLI installation in the node.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">oci_home_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/source/wallet_location"></div>
                    <b>wallet_location</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/source/wallet_location" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Directory path to OCI SSL wallet location on Db server node.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">wallet_location_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/target"></div>
                    <b>target</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/target" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/target/kind"></div>
                    <b>kind</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/target/kind" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of dump transfer to use during migration in source or target host. Default kind is CURL</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CURL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/target/oci_home"></div>
                    <b>oci_home</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/target/oci_home" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Path to the OCI CLI installation in the node.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">oci_home_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/target/wallet_location"></div>
                    <b>wallet_location</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/target/wallet_location" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Directory path to OCI SSL wallet location on Db server node.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">wallet_location_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/data_transfer_medium_details/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-migration/data_transfer_medium_details/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the data transfer medium to use.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">OBJECT_STORAGE</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/database_combination"></div>
                    <b>database_combination</b>
                    <a class="ansibleOptionLink" href="#return-migration/database_combination" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The combination of source and target databases participating in a migration. Example: ORACLE means the migration is meant for migrating Oracle source and target databases.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">MYSQL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-migration/defined_tags" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-migration/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly description. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-migration/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/executing_job_id"></div>
                    <b>executing_job_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/executing_job_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-migration/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see Resource Tags. Example: {&quot;Department&quot;: &quot;Finance&quot;}</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details"></div>
                    <b>ggs_details</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/acceptable_lag"></div>
                    <b>acceptable_lag</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/acceptable_lag" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/extract"></div>
                    <b>extract</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/extract" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/extract/long_trans_duration"></div>
                    <b>long_trans_duration</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/extract/long_trans_duration" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running. If not specified, Extract will not generate a warning on long-running transactions.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/extract/performance_profile"></div>
                    <b>performance_profile</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/extract/performance_profile" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Extract performance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">LOW</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/ggs_deployment"></div>
                    <b>ggs_deployment</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/ggs_deployment" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/ggs_deployment/deployment_id"></div>
                    <b>deployment_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/ggs_deployment/deployment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/ggs_deployment/ggs_admin_credentials_secret_id"></div>
                    <b>ggs_admin_credentials_secret_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/ggs_deployment/ggs_admin_credentials_secret_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.ggsadmincredentialssecret.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/replicat"></div>
                    <b>replicat</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/replicat" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/ggs_details/replicat/performance_profile"></div>
                    <b>performance_profile</b>
                    <a class="ansibleOptionLink" href="#return-migration/ggs_details/replicat/performance_profile" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Replicat performance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">LOW</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details"></div>
                    <b>hub_details</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/acceptable_lag"></div>
                    <b>acceptable_lag</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/acceptable_lag" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/compute_id"></div>
                    <b>compute_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/compute_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/extract"></div>
                    <b>extract</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/extract" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/extract/long_trans_duration"></div>
                    <b>long_trans_duration</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/extract/long_trans_duration" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is long-running. If not specified, Extract will not generate a warning on long-running transactions.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/extract/performance_profile"></div>
                    <b>performance_profile</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/extract/performance_profile" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Extract performance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">LOW</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/key_id"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/key_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.key.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/replicat"></div>
                    <b>replicat</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/replicat" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/replicat/performance_profile"></div>
                    <b>performance_profile</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/replicat/performance_profile" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Replicat performance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">LOW</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/rest_admin_credentials"></div>
                    <b>rest_admin_credentials</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/rest_admin_credentials" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/rest_admin_credentials/username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/rest_admin_credentials/username" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Administrator username</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">username_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/url"></div>
                    <b>url</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Endpoint URL.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/hub_details/vault_id"></div>
                    <b>vault_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/hub_details/vault_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-migration/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings"></div>
                    <b>initial_load_settings</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/compatibility"></div>
                    <b>compatibility</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/compatibility" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Apply the specified requirements for compatibility with MySQL Database Service for all tables in the dump output, altering the dump files as necessary.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/data_pump_parameters"></div>
                    <b>data_pump_parameters</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/data_pump_parameters" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/data_pump_parameters/estimate"></div>
                    <b>estimate</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/data_pump_parameters/estimate" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Estimate size of dumps that will be generated.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">BLOCKS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/data_pump_parameters/exclude_parameters"></div>
                    <b>exclude_parameters</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/data_pump_parameters/exclude_parameters" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Exclude paratemers for Export and Import.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/data_pump_parameters/export_parallelism_degree"></div>
                    <b>export_parallelism_degree</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/data_pump_parameters/export_parallelism_degree" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum number of worker processes that can be used for a Data Pump Export job.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/data_pump_parameters/import_parallelism_degree"></div>
                    <b>import_parallelism_degree</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/data_pump_parameters/import_parallelism_degree" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum number of worker processes that can be used for a Data Pump Import job. For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/data_pump_parameters/is_cluster"></div>
                    <b>is_cluster</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/data_pump_parameters/is_cluster" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Set to false to force Data Pump worker process to run on one instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/data_pump_parameters/table_exists_action"></div>
                    <b>table_exists_action</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/data_pump_parameters/table_exists_action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>IMPORT: Specifies the action to be performed when data is loaded into a preexisting table.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">TRUNCATE</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/export_directory_object"></div>
                    <b>export_directory_object</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/export_directory_object" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/export_directory_object/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/export_directory_object/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of directory object in database</div>
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
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/export_directory_object/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/export_directory_object/path" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Absolute path of directory on database server</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/handle_grant_errors"></div>
                    <b>handle_grant_errors</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/handle_grant_errors" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The action taken in the event of errors related to GRANT or REVOKE errors.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ABORT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/import_directory_object"></div>
                    <b>import_directory_object</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/import_directory_object" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/import_directory_object/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/import_directory_object/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of directory object in database</div>
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
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/import_directory_object/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/import_directory_object/path" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Absolute path of directory on database server</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/is_consistent"></div>
                    <b>is_consistent</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/is_consistent" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enable (true) or disable (false) consistent data dumps by locking the instance for backup during the dump.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/is_ignore_existing_objects"></div>
                    <b>is_ignore_existing_objects</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/is_ignore_existing_objects" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Import the dump even if it contains objects that already exist in the target schema in the MySQL instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/is_tz_utc"></div>
                    <b>is_tz_utc</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/is_tz_utc" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Include a statement at the start of the dump to set the time zone to UTC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/job_mode"></div>
                    <b>job_mode</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/job_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>MySql Job Mode</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FULL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/metadata_remaps"></div>
                    <b>metadata_remaps</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/metadata_remaps" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defines remapping to be applied to objects as they are processed.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/metadata_remaps/new_value"></div>
                    <b>new_value</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/metadata_remaps/new_value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies the new value that oldValue should be translated into.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">new_value_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/metadata_remaps/old_value"></div>
                    <b>old_value</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/metadata_remaps/old_value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies the value which needs to be reset.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">old_value_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/metadata_remaps/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/metadata_remaps/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of remap. Refer to <a href='https://docs.oracle.com/en/database/oracle/oracle- database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D'>METADATA_REMAP Procedure </a></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SCHEMA</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/primary_key_compatibility"></div>
                    <b>primary_key_compatibility</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/primary_key_compatibility" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Primary key compatibility option</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NONE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/tablespace_details"></div>
                    <b>tablespace_details</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/tablespace_details" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/tablespace_details/block_size_in_kbs"></div>
                    <b>block_size_in_kbs</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/tablespace_details/block_size_in_kbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Size of Oracle database blocks in KB.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SIZE_8K</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/tablespace_details/extend_size_in_mbs"></div>
                    <b>extend_size_in_mbs</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/tablespace_details/extend_size_in_mbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Size to extend the tablespace in MB. Note: Only applicable if &#x27;isBigFile&#x27; property is set to true.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/tablespace_details/is_auto_create"></div>
                    <b>is_auto_create</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/tablespace_details/is_auto_create" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Set this property to true to auto-create tablespaces in the target Database. Note: This is not applicable for Autonomous Database Serverless databases.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/tablespace_details/is_big_file"></div>
                    <b>is_big_file</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/tablespace_details/is_big_file" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Set this property to true to enable tablespace of the type big file.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/tablespace_details/remap_target"></div>
                    <b>remap_target</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/tablespace_details/remap_target" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the tablespace on the target database to which the source database tablespace is to be remapped.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">remap_target_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-migration/initial_load_settings/tablespace_details/target_type"></div>
                    <b>target_type</b>
                    <a class="ansibleOptionLink" href="#return-migration/initial_load_settings/tablespace_details/target_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of Database Base Migration Target.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ADB_S_REMAP</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-migration/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Additional status related to the execution and current state of the Migration.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">READY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-migration/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the Migration resource.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/source_container_database_connection_id"></div>
                    <b>source_container_database_connection_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/source_container_database_connection_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/source_database_connection_id"></div>
                    <b>source_database_connection_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/source_database_connection_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-migration/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{&quot;orcl-cloud&quot;: {&quot;free-tier-retained&quot;: &quot;true&quot;}}`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/target_database_connection_id"></div>
                    <b>target_database_connection_id</b>
                    <a class="ansibleOptionLink" href="#return-migration/target_database_connection_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the resource being referenced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-migration/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/time_last_migration"></div>
                    <b>time_last_migration</b>
                    <a class="ansibleOptionLink" href="#return-migration/time_last_migration" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-migration/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-migration/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of the migration to be performed. Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ONLINE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-migration/wait_after"></div>
                    <b>wait_after</b>
                    <a class="ansibleOptionLink" href="#return-migration/wait_after" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>You can optionally pause a migration after a job phase. This property allows you to optionally specify the phase after which you can pause the migration.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ODMS_VALIDATE_TGT</div>
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

