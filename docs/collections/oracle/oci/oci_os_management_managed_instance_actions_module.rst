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

.. _ansible_collections.oracle.oci.oci_os_management_managed_instance_actions_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_os_management_managed_instance_actions -- Perform actions on a ManagedInstance resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 2.53.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_os_management_managed_instance_actions`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Perform actions on a ManagedInstance resource in Oracle Cloud Infrastructure
- For *action=attach_child_software_source*, adds a child software source to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance.
- For *action=attach_parent_software_source*, adds a parent software source to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance. Software sources that have this software source as a parent will be able to be added to this managed instance.
- For *action=detach_child_software_source*, removes a child software source from a managed instance. Packages will no longer be able to be installed from these software sources.
- For *action=detach_parent_software_source*, removes a software source from a managed instance. All child software sources will also be removed from the managed instance. Packages will no longer be able to be installed from these software sources.
- For *action=disable_module_stream*, disables a module stream on a managed instance.  After the stream is disabled, it is no longer possible to install the profiles that are contained by the stream.  All installed profiles must be removed prior to disabling a module stream.
- For *action=enable_module_stream*, enables a module stream on a managed instance.  After the stream is enabled, it is possible to install the profiles that are contained by the stream.  Enabling a stream that is already enabled will succeed.  Attempting to enable a different stream for a module that already has a stream enabled results in an error.
- For *action=install_all_package_updates*, install all of the available package updates for the managed instance.
- For *action=install_all_windows_updates*, install all of the available Windows updates for the managed instance.
- For *action=install_module_stream_profile*, installs a profile for an module stream.  The stream must be enabled before a profile can be installed.  If a module stream defines multiple profiles, each one can be installed independently.
- For *action=install_package*, installs a package on a managed instance.
- For *action=install_package_update*, updates a package on a managed instance.
- For *action=install_windows_update*, installs a Windows update on a managed instance.
- For *action=manage_module_streams*, perform an operation involving modules, streams, and profiles on a managed instance.  Each operation may enable or disable an arbitrary amount of module streams, and install or remove an arbitrary number of module stream profiles.  When the operation is complete, the state of the modules, streams, and profiles on the managed instance will match the state indicated in the operation. Each module stream specified in the list of module streams to enable will be in the "ENABLED" state upon completion of the operation. If there was already a stream of that module enabled, any work required to switch from the current stream to the new stream is performed implicitly. Each module stream specified in the list of module streams to disable will be in the "DISABLED" state upon completion of the operation. Any profiles that are installed for the module stream will be removed as part of the operation. Each module stream profile specified in the list of profiles to install will be in the "INSTALLED" state upon completion of the operation, indicating that any packages that are part of the profile are installed on the managed instance.  If the module stream containing the profile is not enabled, it will be enabled as part of the operation.  There is an exception when attempting to install a stream of a profile when another stream of the same module is enabled.  It is an error to attempt to install a profile of another module stream, unless enabling the new module stream is explicitly included in this operation. Each module stream profile specified in the list of profiles to remove will be in the "AVAILABLE" state upon completion of the operation. The status of packages within the profile after the operation is complete is defined by the package manager on the managed instance. Operations that contain one or more elements that are not allowed are rejected. The result of this request is a WorkRequest object.  The returned WorkRequest is the parent of a structure of other WorkRequests.  Taken as a whole, this structure indicates the entire set of work to be performed to complete the operation. This interface can also be used to perform a dry run of the operation rather than committing it to a managed instance.  If a dry run is requested, the OS Management Service will evaluate the operation against the current module, stream, and profile state on the managed instance.  It will calculate the impact of the operation on all modules, streams, and profiles on the managed instance, including those that are implicitly impacted by the operation. The WorkRequest resulting from a dry run behaves differently than a WorkRequest resulting from a committable operation.  Dry run WorkRequests are always singletons and never have children.  The impact of the operation is returned using the log and error facilities of WorkRequests.  The impact of operations that are allowed by the OS Management Service are communicated as one or more work request log entries.  Operations that are not allowed by the OS Management Service are communicated as one or more work requst error entries.  Each entry, for either logs or errors, contains a structured message containing the results of one or more operations.
- For *action=remove_module_stream_profile*, removes a profile for a module stream that is installed on a managed instance. If a module stream is provided, rather than a fully qualified profile, all profiles that have been installed for the module stream will be removed.
- For *action=remove_package*, removes an installed package from a managed instance.
- For *action=switch_module_stream*, enables a new stream for a module that already has a stream enabled. If any profiles or packages from the original module are installed, switching to a new stream will remove the existing packages and install their counterparts in the new stream.


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
                                                                                                                                                                <li>attach_child_software_source</li>
                                                                                                                                                                                                <li>attach_parent_software_source</li>
                                                                                                                                                                                                <li>detach_child_software_source</li>
                                                                                                                                                                                                <li>detach_parent_software_source</li>
                                                                                                                                                                                                <li>disable_module_stream</li>
                                                                                                                                                                                                <li>enable_module_stream</li>
                                                                                                                                                                                                <li>install_all_package_updates</li>
                                                                                                                                                                                                <li>install_all_windows_updates</li>
                                                                                                                                                                                                <li>install_module_stream_profile</li>
                                                                                                                                                                                                <li>install_package</li>
                                                                                                                                                                                                <li>install_package_update</li>
                                                                                                                                                                                                <li>install_windows_update</li>
                                                                                                                                                                                                <li>manage_module_streams</li>
                                                                                                                                                                                                <li>remove_module_stream_profile</li>
                                                                                                                                                                                                <li>remove_package</li>
                                                                                                                                                                                                <li>switch_module_stream</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the ManagedInstance.</div>
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
                                            <div>The name of a module</div>
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
                                            <div>The name of a stream of the specified module</div>
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
                                            <div>The name of a module</div>
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
                                            <div>The name of a stream of the specified module</div>
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
                                            <div>The name of a module</div>
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
                                            <div>The name of a profile of the specified module stream</div>
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
                                            <div>The name of a stream of the specified module</div>
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
                                            <div>Indicates if this operation is a dry run or if the operation should be commited.  If set to true, the result of the operation will be evaluated but not committed.  If set to false, the operation is committed to the managed instance.  The default is false.</div>
                                            <div>Applicable only for <em>action=manage_module_streams</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-managed_instance_id"></div>
                    <b>managed_instance_id</b>
                    <a class="ansibleOptionLink" href="#parameter-managed_instance_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>OCID for the managed instance</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
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
                                            <div>The name of a module.</div>
                                            <div>Required for <em>action=disable_module_stream</em>, <em>action=enable_module_stream</em>, <em>action=install_module_stream_profile</em>, <em>action=remove_module_stream_profile</em>, <em>action=switch_module_stream</em>.</div>
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
                                            <div>The name of the profile of the containing module stream</div>
                                            <div>Applicable only for <em>action=install_module_stream_profile</em><em>action=remove_module_stream_profile</em>.</div>
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
                                            <div>The name of a module</div>
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
                                            <div>The name of a profile of the specified module stream</div>
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
                                            <div>The name of a stream of the specified module</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-software_package_name"></div>
                    <b>software_package_name</b>
                    <a class="ansibleOptionLink" href="#parameter-software_package_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Package name</div>
                                            <div>Required for <em>action=install_package</em>, <em>action=install_package_update</em>, <em>action=remove_package</em>.</div>
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
                                            <div>OCID for the Software Source</div>
                                            <div>Required for <em>action=attach_child_software_source</em>, <em>action=attach_parent_software_source</em>, <em>action=detach_child_software_source</em>, <em>action=detach_parent_software_source</em>.</div>
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
                                            <div>The name of the stream of the containing module.  This parameter is required if a profileName is specified.</div>
                                            <div>Applicable only for <em>action=disable_module_stream</em><em>action=enable_module_stream</em><em>action=install_module_stream_profile</em><em>action=remove_module_str eam_profile</em><em>action=switch_module_stream</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-update_type"></div>
                    <b>update_type</b>
                    <a class="ansibleOptionLink" href="#parameter-update_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SECURITY</li>
                                                                                                                                                                                                <li>BUGFIX</li>
                                                                                                                                                                                                <li>ENHANCEMENT</li>
                                                                                                                                                                                                <li>OTHER</li>
                                                                                                                                                                                                <li>KSPLICE</li>
                                                                                                                                                                                                <li>ALL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of updates to be applied</div>
                                            <div>Applicable only for <em>action=install_all_package_updates</em><em>action=install_all_windows_updates</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-windows_update_name"></div>
                    <b>windows_update_name</b>
                    <a class="ansibleOptionLink" href="#parameter-windows_update_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique identifier for the Windows update. NOTE - This is not an OCID, but is a unique identifier assigned by Microsoft. Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`</div>
                                            <div>Required for <em>action=install_windows_update</em>.</div>
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

    
    - name: Perform action attach_child_software_source on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: attach_child_software_source

    - name: Perform action attach_parent_software_source on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: attach_parent_software_source

    - name: Perform action detach_child_software_source on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: detach_child_software_source

    - name: Perform action detach_parent_software_source on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: detach_parent_software_source

    - name: Perform action disable_module_stream on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        module_name: module_name_example
        action: disable_module_stream

        # optional
        stream_name: stream_name_example

    - name: Perform action enable_module_stream on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        module_name: module_name_example
        action: enable_module_stream

        # optional
        stream_name: stream_name_example

    - name: Perform action install_all_package_updates on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: install_all_package_updates

        # optional
        update_type: SECURITY

    - name: Perform action install_all_windows_updates on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: install_all_windows_updates

        # optional
        update_type: SECURITY

    - name: Perform action install_module_stream_profile on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        module_name: module_name_example
        action: install_module_stream_profile

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example

    - name: Perform action install_package on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        software_package_name: software_package_name_example
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: install_package

    - name: Perform action install_package_update on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        software_package_name: software_package_name_example
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: install_package_update

    - name: Perform action install_windows_update on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        windows_update_name: windows_update_name_example
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: install_windows_update

    - name: Perform action manage_module_streams on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: manage_module_streams

        # optional
        is_dry_run: true
        enable:
        - # required
          module_name: module_name_example
          stream_name: stream_name_example
        disable:
        - # required
          module_name: module_name_example
          stream_name: stream_name_example
        install:
        - # required
          module_name: module_name_example
          stream_name: stream_name_example
          profile_name: profile_name_example
        remove:
        - # required
          module_name: module_name_example
          stream_name: stream_name_example
          profile_name: profile_name_example

    - name: Perform action remove_module_stream_profile on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        module_name: module_name_example
        action: remove_module_stream_profile

        # optional
        profile_name: profile_name_example
        stream_name: stream_name_example

    - name: Perform action remove_package on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        software_package_name: software_package_name_example
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        action: remove_package

    - name: Perform action switch_module_stream on managed_instance
      oci_os_management_managed_instance_actions:
        # required
        managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        module_name: module_name_example
        action: switch_module_stream

        # optional
        stream_name: stream_name_example





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
                    <div class="ansibleOptionAnchor" id="return-managed_instance"></div>
                    <b>managed_instance</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the ManagedInstance resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;autonomous&#x27;: {&#x27;is_auto_update_enabled&#x27;: True}, &#x27;bug_updates_available&#x27;: 56, &#x27;child_software_sources&#x27;: [{&#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;}], &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;enhancement_updates_available&#x27;: 56, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;is_data_collection_authorized&#x27;: True, &#x27;is_reboot_required&#x27;: True, &#x27;ksplice_effective_kernel_version&#x27;: &#x27;ksplice_effective_kernel_version_example&#x27;, &#x27;last_boot&#x27;: &#x27;last_boot_example&#x27;, &#x27;last_checkin&#x27;: &#x27;last_checkin_example&#x27;, &#x27;managed_instance_groups&#x27;: [{&#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;}], &#x27;notification_topic_id&#x27;: &#x27;ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;os_family&#x27;: &#x27;LINUX&#x27;, &#x27;os_kernel_version&#x27;: &#x27;os_kernel_version_example&#x27;, &#x27;os_name&#x27;: &#x27;os_name_example&#x27;, &#x27;os_version&#x27;: &#x27;os_version_example&#x27;, &#x27;other_updates_available&#x27;: 56, &#x27;parent_software_source&#x27;: {&#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;}, &#x27;scheduled_job_count&#x27;: 56, &#x27;security_updates_available&#x27;: 56, &#x27;status&#x27;: &#x27;NORMAL&#x27;, &#x27;updates_available&#x27;: 56, &#x27;work_request_count&#x27;: 56}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/autonomous"></div>
                    <b>autonomous</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/autonomous" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>if present, indicates the Managed Instance is an autonomous instance. Holds all the Autonomous specific information</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/autonomous/is_auto_update_enabled"></div>
                    <b>is_auto_update_enabled</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/autonomous/is_auto_update_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>True if daily updates are enabled</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/bug_updates_available"></div>
                    <b>bug_updates_available</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/bug_updates_available" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Number of bug fix type updates available to be installed</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/child_software_sources"></div>
                    <b>child_software_sources</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/child_software_sources" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>list of child Software Sources attached to the Managed Instance</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/child_software_sources/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/child_software_sources/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>software source identifier</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/child_software_sources/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/child_software_sources/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>software source name</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>OCID for the Compartment</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Information specified by the user about the managed instance</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Managed Instance identifier</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/enhancement_updates_available"></div>
                    <b>enhancement_updates_available</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/enhancement_updates_available" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Number of enhancement type updates available to be installed</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>OCID for the managed instance</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/is_data_collection_authorized"></div>
                    <b>is_data_collection_authorized</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/is_data_collection_authorized" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>True if user allow data collection for this instance</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/is_reboot_required"></div>
                    <b>is_reboot_required</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/is_reboot_required" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether a reboot is required to complete installation of updates.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/ksplice_effective_kernel_version"></div>
                    <b>ksplice_effective_kernel_version</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/ksplice_effective_kernel_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The ksplice effective kernel version</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ksplice_effective_kernel_version_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/last_boot"></div>
                    <b>last_boot</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/last_boot" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Time at which the instance last booted</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">last_boot_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/last_checkin"></div>
                    <b>last_checkin</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/last_checkin" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Time at which the instance last checked in</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">last_checkin_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/managed_instance_groups"></div>
                    <b>managed_instance_groups</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/managed_instance_groups" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The ids of the managed instance groups of which this instance is a member.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/managed_instance_groups/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/managed_instance_groups/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>User friendly name</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/managed_instance_groups/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/managed_instance_groups/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>unique identifier that is immutable on creation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/notification_topic_id"></div>
                    <b>notification_topic_id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/notification_topic_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>OCID of the ONS topic used to send notification to users</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.notificationtopic.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/os_family"></div>
                    <b>os_family</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/os_family" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Operating System type of the managed instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">LINUX</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/os_kernel_version"></div>
                    <b>os_kernel_version</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/os_kernel_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Operating System Kernel Version</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">os_kernel_version_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/os_name"></div>
                    <b>os_name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/os_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Operating System Name</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">os_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/os_version"></div>
                    <b>os_version</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/os_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Operating System Version</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">os_version_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/other_updates_available"></div>
                    <b>other_updates_available</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/other_updates_available" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Number of non-classified updates available to be installed</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/parent_software_source"></div>
                    <b>parent_software_source</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/parent_software_source" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>the parent (base) Software Source attached to the Managed Instance</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/parent_software_source/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/parent_software_source/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>software source identifier</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/parent_software_source/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/parent_software_source/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>software source name</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/scheduled_job_count"></div>
                    <b>scheduled_job_count</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/scheduled_job_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Number of scheduled jobs associated with this instance</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/security_updates_available"></div>
                    <b>security_updates_available</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/security_updates_available" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Number of security type updates available to be installed</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>status of the managed instance.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NORMAL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/updates_available"></div>
                    <b>updates_available</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/updates_available" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Number of updates available to be installed</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-managed_instance/work_request_count"></div>
                    <b>work_request_count</b>
                    <a class="ansibleOptionLink" href="#return-managed_instance/work_request_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Number of work requests associated with this instance</div>
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

