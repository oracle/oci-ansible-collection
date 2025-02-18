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

.. _ansible_collections.oracle.oci.oci_os_management_hub_managed_instance_group_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_os_management_hub_managed_instance_group_actions -- Perform actions on a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 5.4.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_os_management_hub_managed_instance_group_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on a ManagedInstanceGroup resource in Oracle Cloud Infrastructure
- For *action=attach_managed_instances*, adds managed instances to the specified managed instance group. After adding instances to the group, any operation applied to the group will be applied to all instances in the group.
- For *action=attach_software_sources*, attaches software sources to the specified managed instance group. The software sources must be compatible with the type of instances in the group.
- For *action=change_compartment*, moves the specified managed instance group to a different compartment within the same tenancy. For information about moving resources between compartments, see `Moving Resources to a Different Compartment <https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes>`_.
- For *action=detach_managed_instances*, removes a managed instance from the specified managed instance group.
- For *action=detach_software_sources*, detaches the specified software sources from a managed instance group.
- For *action=disable_module_stream*, disables a module stream on a managed instance group. After the stream is disabled, you can no longer install the profiles contained by the stream.  Before removing the stream, you must remove all installed profiles for the stream by using the `RemoveModuleStreamProfileFromManagedInstanceGroup <https://docs.cloud.oracle.com/en- us/iaas/api/#/en/osmh/latest//ManagedInstanceGroup/RemoveModuleStreamProfileFromManagedInstanceGroup>`_ operation.
- For *action=enable_module_stream*, enables a module stream on a managed instance group.  After the stream is enabled, you can install a module stream profile. Enabling a stream that is already enabled will succeed.  Enabling a different stream for a module that already has a stream enabled results in an error. Instead, use the `SwitchModuleStreamOnManagedInstanceGroup <https://docs.cloud.oracle.com/en- us/iaas/api/#/en/osmh/latest/ManagedInstanceGroup/SwitchModuleStreamOnManagedInstanceGroup>`_ operation.
- For *action=install_module_stream_profile*, installs a profile for an enabled module stream. If a module stream defines multiple profiles, you can install each one independently.
- For *action=install_packages*, installs the specified packages on each managed instance in a managed instance group. The package must be compatible with the instances in the group.
- For *action=install_windows_updates*, installs Windows updates on each managed instance in the managed instance group.
- For *action=manage_module_streams*, enables or disables module streams and installs or removes module stream profiles. Once complete, the state of the modules, streams, and profiles will match the state indicated in the operation. See `ManageModuleStreamsOnManagedInstanceGroupDetails <https://docs.cloud.oracle.com/en- us/iaas/api/#/en/osmh/latest/datatypes/ManageModuleStreamsOnManagedInstanceGroupDetails>`_ for more information. You can preform this operation as a dry run. For a dry run, the service evaluates the operation against the current module, stream, and profile state on the managed instance, but does not commit the changes. Instead, the service returns work request log or error entries indicating the impact of the operation.
- For *action=remove_module_stream_profile*, removes a profile for a module stream that is installed on a managed instance group. Providing the module stream name (without specifying a profile name) removes all profiles that have been installed for the module stream.
- For *action=remove_packages*, removes the specified packages from each managed instance in a managed instance group.
- For *action=switch_module_stream*, enables a new stream for a module that already has a stream enabled. If any profiles or packages from the original module are installed, switching to a new stream will remove the existing packages and install their counterparts in the new stream.
- For *action=update_all_packages*, updates all packages on each managed instance in the specified managed instance group.


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
                                                                                                                                                                <li>attach_managed_instances</li>
                                                                                                                                                                                                <li>attach_software_sources</li>
                                                                                                                                                                                                <li>change_compartment</li>
                                                                                                                                                                                                <li>detach_managed_instances</li>
                                                                                                                                                                                                <li>detach_software_sources</li>
                                                                                                                                                                                                <li>disable_module_stream</li>
                                                                                                                                                                                                <li>enable_module_stream</li>
                                                                                                                                                                                                <li>install_module_stream_profile</li>
                                                                                                                                                                                                <li>install_packages</li>
                                                                                                                                                                                                <li>install_windows_updates</li>
                                                                                                                                                                                                <li>manage_module_streams</li>
                                                                                                                                                                                                <li>remove_module_stream_profile</li>
                                                                                                                                                                                                <li>remove_packages</li>
                                                                                                                                                                                                <li>switch_module_stream</li>
                                                                                                                                                                                                <li>update_all_packages</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the ManagedInstanceGroup.</div>
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
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment to move the group to.</div>
                                            <div>Required for <em>action=change_compartment</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-disable"></div>
                    <b>disable</b>
                    <a class="ansibleOptionLink" href="#parameter-disable" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The set of module streams to disable.</div>
                                            <div>Applicable only for <em>action=manage_module_streams</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-disable/module_name"></div>
                    <b>module_name</b>
                    <a class="ansibleOptionLink" href="#parameter-disable/module_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-disable/software_source_id"></div>
                    <b>software_source_id</b>
                    <a class="ansibleOptionLink" href="#parameter-disable/software_source_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the software source that contains the module stream.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-disable/stream_name"></div>
                    <b>stream_name</b>
                    <a class="ansibleOptionLink" href="#parameter-disable/stream_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a stream of the specified module.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-enable"></div>
                    <b>enable</b>
                    <a class="ansibleOptionLink" href="#parameter-enable" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The set of module streams to enable.</div>
                                            <div>Applicable only for <em>action=manage_module_streams</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-enable/module_name"></div>
                    <b>module_name</b>
                    <a class="ansibleOptionLink" href="#parameter-enable/module_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-enable/software_source_id"></div>
                    <b>software_source_id</b>
                    <a class="ansibleOptionLink" href="#parameter-enable/software_source_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the software source that contains the module stream.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-enable/stream_name"></div>
                    <b>stream_name</b>
                    <a class="ansibleOptionLink" href="#parameter-enable/stream_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a stream of the specified module.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-install"></div>
                    <b>install</b>
                    <a class="ansibleOptionLink" href="#parameter-install" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The set of module stream profiles to install.</div>
                                            <div>Applicable only for <em>action=manage_module_streams</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-install/module_name"></div>
                    <b>module_name</b>
                    <a class="ansibleOptionLink" href="#parameter-install/module_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-install/profile_name"></div>
                    <b>profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-install/profile_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a profile of the specified module stream.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-install/software_source_id"></div>
                    <b>software_source_id</b>
                    <a class="ansibleOptionLink" href="#parameter-install/software_source_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the software source that contains the module stream.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-install/stream_name"></div>
                    <b>stream_name</b>
                    <a class="ansibleOptionLink" href="#parameter-install/stream_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a stream of the specified module.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-is_dry_run"></div>
                    <b>is_dry_run</b>
                    <a class="ansibleOptionLink" href="#parameter-is_dry_run" title="Permalink to this option"></a>
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
                                            <div>Indicates if this operation is a dry run or if the operation should be committed.  If set to true, the result of the operation will be evaluated but not committed.  If set to false, the operation is committed to the managed instance(s).  The default is false.</div>
                                            <div>Applicable only for <em>action=manage_module_streams</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-managed_instance_group_id"></div>
                    <b>managed_instance_group_id</b>
                    <a class="ansibleOptionLink" href="#parameter-managed_instance_group_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the managed instance group.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-managed_instances"></div>
                    <b>managed_instances</b>
                    <a class="ansibleOptionLink" href="#parameter-managed_instances" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of managed instance <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCIDs</a> to attach to the group.</div>
                                            <div>Required for <em>action=attach_managed_instances</em>, <em>action=detach_managed_instances</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-module_name"></div>
                    <b>module_name</b>
                    <a class="ansibleOptionLink" href="#parameter-module_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the module.</div>
                                            <div>Required for <em>action=disable_module_stream</em>, <em>action=enable_module_stream</em>, <em>action=install_module_stream_profile</em>, <em>action=remove_module_stream_profile</em>, <em>action=switch_module_stream</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-package_names"></div>
                    <b>package_names</b>
                    <a class="ansibleOptionLink" href="#parameter-package_names" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of package names.</div>
                                            <div>Required for <em>action=install_packages</em>, <em>action=remove_packages</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-profile_name"></div>
                    <b>profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-profile_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a profile of the specified module stream.</div>
                                            <div>Applicable only for <em>action=install_module_stream_profile</em><em>action=remove_module_stream_profile</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-remove"></div>
                    <b>remove</b>
                    <a class="ansibleOptionLink" href="#parameter-remove" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The set of module stream profiles to remove.</div>
                                            <div>Applicable only for <em>action=manage_module_streams</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-remove/module_name"></div>
                    <b>module_name</b>
                    <a class="ansibleOptionLink" href="#parameter-remove/module_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-remove/profile_name"></div>
                    <b>profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-remove/profile_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a profile of the specified module stream.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-remove/software_source_id"></div>
                    <b>software_source_id</b>
                    <a class="ansibleOptionLink" href="#parameter-remove/software_source_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the software source that contains the module stream.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-remove/stream_name"></div>
                    <b>stream_name</b>
                    <a class="ansibleOptionLink" href="#parameter-remove/stream_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a stream of the specified module.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-software_source_id"></div>
                    <b>software_source_id</b>
                    <a class="ansibleOptionLink" href="#parameter-software_source_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the software source that provides the module stream</div>
                                            <div>Applicable only for <em>action=disable_module_stream</em><em>action=enable_module_stream</em><em>action=install_module_stream_profile</em><em>action=remove_module_str eam_profile</em><em>action=switch_module_stream</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-software_sources"></div>
                    <b>software_sources</b>
                    <a class="ansibleOptionLink" href="#parameter-software_sources" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of software source <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCIDs</a> to attach to the group.</div>
                                            <div>Required for <em>action=attach_software_sources</em>, <em>action=detach_software_sources</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-stream_name"></div>
                    <b>stream_name</b>
                    <a class="ansibleOptionLink" href="#parameter-stream_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of a stream of the specified module.</div>
                                            <div>Required for <em>action=switch_module_stream</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-update_types"></div>
                    <b>update_types</b>
                    <a class="ansibleOptionLink" href="#parameter-update_types" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SECURITY</li>
                                                                                                                                                                                                <li>BUGFIX</li>
                                                                                                                                                                                                <li>ENHANCEMENT</li>
                                                                                                                                                                                                <li>OTHER</li>
                                                                                                                                                                                                <li>KSPLICE_KERNEL</li>
                                                                                                                                                                                                <li>KSPLICE_USERSPACE</li>
                                                                                                                                                                                                <li>ALL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of updates to be applied.</div>
                                            <div>Applicable only for <em>action=update_all_packages</em>.</div>
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
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-windows_update_types"></div>
                    <b>windows_update_types</b>
                    <a class="ansibleOptionLink" href="#parameter-windows_update_types" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SECURITY</li>
                                                                                                                                                                                                <li>BUGFIX</li>
                                                                                                                                                                                                <li>ENHANCEMENT</li>
                                                                                                                                                                                                <li>OTHER</li>
                                                                                                                                                                                                <li>ALL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of Windows updates to be applied.</div>
                                            <div>Required for <em>action=install_windows_updates</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-work_request_details"></div>
                    <b>work_request_details</b>
                    <a class="ansibleOptionLink" href="#parameter-work_request_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable only for <em>action=attach_managed_instances</em><em>action=attach_software_sources</em><em>action=detach_software_sources</em><em>action=disable_module_st ream</em><em>action=enable_module_stream</em><em>action=install_module_stream_profile</em><em>action=install_packages</em><em>action=install_windows_updates</em><em>action=mana ge_module_streams</em><em>action=remove_module_stream_profile</em><em>action=remove_packages</em><em>action=switch_module_stream</em><em>action=update_all_packages</em>.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-work_request_details/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-work_request_details/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>User-specified information about the job. Avoid entering confidential information.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-work_request_details/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-work_request_details/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name for the job. The name does not have to be unique. Avoid entering confidential information.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
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

    
    - name: Perform action attach_managed_instances on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        managed_instances: [ "managed_instances_example" ]
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: attach_managed_instances

        # optional
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action attach_software_sources on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        software_sources: [ "software_sources_example" ]
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: attach_software_sources

        # optional
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action change_compartment on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: change_compartment

    - name: Perform action detach_managed_instances on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        managed_instances: [ "managed_instances_example" ]
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: detach_managed_instances

    - name: Perform action detach_software_sources on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        software_sources: [ "software_sources_example" ]
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: detach_software_sources

        # optional
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action disable_module_stream on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        module_name: module_name_example
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: disable_module_stream

        # optional
        stream_name: stream_name_example
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action enable_module_stream on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        module_name: module_name_example
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: enable_module_stream

        # optional
        stream_name: stream_name_example
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action install_module_stream_profile on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        module_name: module_name_example
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: install_module_stream_profile

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action install_packages on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        package_names: [ "package_names_example" ]
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: install_packages

        # optional
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action install_windows_updates on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        windows_update_types: [ "SECURITY" ]
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: install_windows_updates

        # optional
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action manage_module_streams on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: manage_module_streams

        # optional
        is_dry_run: true
        enable:
        - # required
          module_name: module_name_example
          stream_name: stream_name_example

          # optional
          software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        disable:
        - # required
          module_name: module_name_example
          stream_name: stream_name_example

          # optional
          software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        install:
        - # required
          module_name: module_name_example
          stream_name: stream_name_example
          profile_name: profile_name_example

          # optional
          software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        remove:
        - # required
          module_name: module_name_example
          stream_name: stream_name_example
          profile_name: profile_name_example

          # optional
          software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action remove_module_stream_profile on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        module_name: module_name_example
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: remove_module_stream_profile

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action remove_packages on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        package_names: [ "package_names_example" ]
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: remove_packages

        # optional
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action switch_module_stream on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        module_name: module_name_example
        stream_name: stream_name_example
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: switch_module_stream

        # optional
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example

    - name: Perform action update_all_packages on managed_instance_group
      oci_os_management_hub_managed_instance_group_actions:
        # required
        managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"
        action: update_all_packages

        # optional
        update_types: [ "SECURITY" ]
        work_request_details:
          # optional
          display_name: display_name_example
          description: description_example





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group"></div>
                    <b>managed_instance_group</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the ManagedInstanceGroup resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;arch_type&#x27;: &#x27;X86_64&#x27;, &#x27;autonomous_settings&#x27;: {&#x27;is_data_collection_authorized&#x27;: True, &#x27;scheduled_job_id&#x27;: &#x27;ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx&#x27;}, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;is_managed_by_autonomous_linux&#x27;: True, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;location&#x27;: &#x27;ON_PREMISE&#x27;, &#x27;managed_instance_count&#x27;: 56, &#x27;managed_instance_ids&#x27;: [], &#x27;notification_topic_id&#x27;: &#x27;ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;os_family&#x27;: &#x27;ORACLE_LINUX_9&#x27;, &#x27;pending_job_count&#x27;: 56, &#x27;software_source_ids&#x27;: [{&#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;is_mandatory_for_autonomous_linux&#x27;: True, &#x27;software_source_type&#x27;: &#x27;VENDOR&#x27;}], &#x27;software_sources&#x27;: [{&#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;is_mandatory_for_autonomous_linux&#x27;: True, &#x27;software_source_type&#x27;: &#x27;VENDOR&#x27;}], &#x27;system_tags&#x27;: {}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_modified&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;vendor_name&#x27;: &#x27;ORACLE&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/arch_type"></div>
                    <b>arch_type</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/arch_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The CPU architecture of the instances in the managed instance group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">X86_64</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/autonomous_settings"></div>
                    <b>autonomous_settings</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/autonomous_settings" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/autonomous_settings/is_data_collection_authorized"></div>
                    <b>is_data_collection_authorized</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/autonomous_settings/is_data_collection_authorized" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether Autonomous Linux will collect crash files. This setting can be changed by the user.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/autonomous_settings/scheduled_job_id"></div>
                    <b>scheduled_job_id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/autonomous_settings/scheduled_job_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the restricted scheduled job associated with this instance. This value cannot be deleted by the user.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment that contains the managed instance group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>. Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>User-specified information about the managed instance group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name for the managed instance group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>. Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the managed instance group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/is_managed_by_autonomous_linux"></div>
                    <b>is_managed_by_autonomous_linux</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/is_managed_by_autonomous_linux" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether the Autonomous Linux service manages the group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the managed instance group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/location"></div>
                    <b>location</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/location" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The location of managed instances attached to the group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ON_PREMISE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/managed_instance_count"></div>
                    <b>managed_instance_count</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/managed_instance_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of managed instances in the group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/managed_instance_ids"></div>
                    <b>managed_instance_ids</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/managed_instance_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of managed instance <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCIDs</a> attached to the managed instance group.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/notification_topic_id"></div>
                    <b>notification_topic_id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/notification_topic_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> for the Oracle Notifications service (ONS) topic. ONS is the channel used to send notifications to the customer.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/os_family"></div>
                    <b>os_family</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/os_family" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The operating system type of the instances in the managed instance group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ORACLE_LINUX_9</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/pending_job_count"></div>
                    <b>pending_job_count</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/pending_job_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of scheduled jobs pending against the managed instance group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_source_ids"></div>
                    <b>software_source_ids</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_source_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of software source <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCIDs</a> that the managed instance group will use.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_source_ids/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_source_ids/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Software source description.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_source_ids/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_source_ids/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Software source name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_source_ids/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_source_ids/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the software source.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_source_ids/is_mandatory_for_autonomous_linux"></div>
                    <b>is_mandatory_for_autonomous_linux</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_source_ids/is_mandatory_for_autonomous_linux" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can&#x27;t unselect it.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_source_ids/software_source_type"></div>
                    <b>software_source_type</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_source_ids/software_source_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the software source.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">VENDOR</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_sources"></div>
                    <b>software_sources</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_sources" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of software sources that the managed instance group will use.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_sources/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_sources/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Software source description.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_sources/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_sources/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Software source name.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_sources/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_sources/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm'>OCID</a> of the software source.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_sources/is_mandatory_for_autonomous_linux"></div>
                    <b>is_mandatory_for_autonomous_linux</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_sources/is_mandatory_for_autonomous_linux" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether this is a required software source for Autonomous Linux instances. If true, the user can&#x27;t unselect it.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/software_sources/software_source_type"></div>
                    <b>software_source_type</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/software_sources/software_source_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the software source.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">VENDOR</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/system_tags" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the managed instance group was created (in <a href='https://tools.ietf.org/rfc/rfc3339'>RFC 3339</a> format).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/time_modified"></div>
                    <b>time_modified</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/time_modified" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the managed instance group was last modified (in <a href='https://tools.ietf.org/rfc/rfc3339'>RFC 3339</a> format).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance_group/vendor_name"></div>
                    <b>vendor_name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance_group/vendor_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The vendor of the operating system used by the managed instances in the group.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ORACLE</div>
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

