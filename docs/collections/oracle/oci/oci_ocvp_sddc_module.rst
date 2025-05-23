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

.. _ansible_collections.oracle.oci.oci_ocvp_sddc_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_ocvp_sddc -- Manage a Sddc resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 5.5.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_ocvp_sddc`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a Sddc resource in Oracle Cloud Infrastructure
- For *state=present*, creates an Oracle Cloud VMware Solution software-defined data center (SDDC).
- Use the `WorkRequest <https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/WorkRequest/>`_ operations to track the creation of the SDDC.
- **Important:** You must configure the SDDC's networking resources with the security rules detailed in `Security Rules for Oracle Cloud VMware Solution SDDCs <https://docs.cloud.oracle.com/iaas/Content/VMware/Reference/ocvssecurityrules.htm>`_. Otherwise, provisioning the SDDC will fail. The rules are based on the requirements set by VMware.
- This resource has the following action operations in the :ref:`oracle.oci.oci_ocvp_sddc_actions <ansible_collections.oracle.oci.oci_ocvp_sddc_actions_module>` module: cancel_downgrade_hcx, change_compartment, downgrade_hcx, refresh_hcx_license_status, upgrade_hcx.


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
                    <div class="ansibleOptionAnchor" id="parameter-capacity_reservation_id"></div>
                    <b>capacity_reservation_id</b>
                    <a class="ansibleOptionLink" href="#parameter-capacity_reservation_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Capacity Reservation.</div>
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
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment to contain the SDDC.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>Required for delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-compute_availability_domain"></div>
                    <b>compute_availability_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-compute_availability_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The availability domain to create the SDDC&#x27;s ESXi hosts in. For multi-AD SDDC deployment, set to `multi-AD`.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-datastores"></div>
                    <b>datastores</b>
                    <a class="ansibleOptionLink" href="#parameter-datastores" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of datastore info for the SDDC. This value is required only when `initialHostShapeName` is a standard shape.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-datastores/block_volume_ids"></div>
                    <b>block_volume_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-datastores/block_volume_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>s of Block Storage Volumes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-datastores/datastore_type"></div>
                    <b>datastore_type</b>
                    <a class="ansibleOptionLink" href="#parameter-datastores/datastore_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>MANAGEMENT</li>
                                                                                                                                                                                                <li>WORKLOAD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the datastore.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                            <div>A descriptive name for the SDDC. SDDC name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the region. Avoid entering confidential information.</div>
                                            <div>Required for create, update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-esxi_hosts_count"></div>
                    <b>esxi_hosts_count</b>
                    <a class="ansibleOptionLink" href="#parameter-esxi_hosts_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of ESXi hosts to create in the SDDC. You can add more hosts later (see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>). Creating a SDDC with a ESXi host count of 1 will be considered a single ESXi host SDDC.</div>
                                            <div>**Note:** If you later delete EXSi hosts from a production SDDC to total less than 3, you are still billed for the 3 minimum recommended ESXi hosts. Also, you cannot add more VMware workloads to the SDDC until it again has at least 3 ESXi hosts.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hcx_vlan_id"></div>
                    <b>hcx_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-hcx_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN to use for the HCX component of the VMware environment. This value is required only when `isHcxEnabled` is true.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_host_ocpu_count"></div>
                    <b>initial_host_ocpu_count</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_host_ocpu_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The initial OCPU count of the SDDC&#x27;s ESXi hosts.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_host_shape_name"></div>
                    <b>initial_host_shape_name</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_host_shape_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The initial compute shape of the SDDC&#x27;s ESXi hosts. <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedHostShapes/ListSupportedHostShapes'>ListSupportedHostShapes</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-initial_sku"></div>
                    <b>initial_sku</b>
                    <a class="ansibleOptionLink" href="#parameter-initial_sku" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>HOUR</li>
                                                                                                                                                                                                <li>MONTH</li>
                                                                                                                                                                                                <li>ONE_YEAR</li>
                                                                                                                                                                                                <li>THREE_YEARS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The billing option selected during SDDC creation. <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus'>ListSupportedSkus</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-instance_display_name_prefix"></div>
                    <b>instance_display_name_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-instance_display_name_prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A prefix used in the name of each ESXi host and Compute instance in the SDDC. If this isn&#x27;t set, the SDDC&#x27;s `displayName` is used as the prefix.</div>
                                            <div>For example, if the value is `mySDDC`, the ESXi hosts are named `mySDDC-1`, `mySDDC-2`, and so on.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-is_hcx_enabled"></div>
                    <b>is_hcx_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_hcx_enabled" title="Permalink to this option"></a>
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
                                            <div>For SDDC with dense compute shapes, this parameter indicates whether to enable HCX Advanced for this SDDC. For SDDC with standard compute shapes, this parameter is equivalent to `isHcxEnterpriseEnabled`.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-is_hcx_enterprise_enabled"></div>
                    <b>is_hcx_enterprise_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_hcx_enterprise_enabled" title="Permalink to this option"></a>
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
                                            <div>Indicates whether to enable HCX Enterprise for this SDDC.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-is_shielded_instance_enabled"></div>
                    <b>is_shielded_instance_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_shielded_instance_enabled" title="Permalink to this option"></a>
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
                                            <div>Indicates whether shielded instance is enabled for this SDDC.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-is_single_host_sddc"></div>
                    <b>is_single_host_sddc</b>
                    <a class="ansibleOptionLink" href="#parameter-is_single_host_sddc" title="Permalink to this option"></a>
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
                                            <div>Indicates whether this SDDC is designated for only single ESXi host.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-nsx_edge_uplink1_vlan_id"></div>
                    <b>nsx_edge_uplink1_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-nsx_edge_uplink1_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN to use for the NSX Edge Uplink 1 component of the VMware environment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-nsx_edge_uplink2_vlan_id"></div>
                    <b>nsx_edge_uplink2_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-nsx_edge_uplink2_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN to use for the NSX Edge Uplink 2 component of the VMware environment.</div>
                                            <div>**Note:** This VLAN is reserved for future use to deploy public-facing applications on the VMware SDDC.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-nsx_edge_v_tep_vlan_id"></div>
                    <b>nsx_edge_v_tep_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-nsx_edge_v_tep_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN to use for the NSX Edge VTEP component of the VMware environment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-nsx_v_tep_vlan_id"></div>
                    <b>nsx_v_tep_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-nsx_v_tep_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN to use for the NSX VTEP component of the VMware environment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-provisioning_subnet_id"></div>
                    <b>provisioning_subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-provisioning_subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the management subnet to use for provisioning the SDDC.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-provisioning_vlan_id"></div>
                    <b>provisioning_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-provisioning_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the Provisioning component of the VMware environment.</div>
                                            <div>This parameter is updatable.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-replication_vlan_id"></div>
                    <b>replication_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-replication_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the vSphere Replication component of the VMware environment.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-sddc_id"></div>
                    <b>sddc_id</b>
                    <a class="ansibleOptionLink" href="#parameter-sddc_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the SDDC.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ssh_authorized_keys"></div>
                    <b>ssh_authorized_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-ssh_authorized_keys" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on each ESXi host. Use a newline character to separate multiple keys. The SSH keys must be in the format required for the `authorized_keys` file</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                            <div>The state of the Sddc.</div>
                                            <div>Use <em>state=present</em> to create or update a Sddc.</div>
                                            <div>Use <em>state=absent</em> to delete a Sddc.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-vmotion_vlan_id"></div>
                    <b>vmotion_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-vmotion_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN to use for the vMotion component of the VMware environment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-vmware_software_version"></div>
                    <b>vmware_software_version</b>
                    <a class="ansibleOptionLink" href="#parameter-vmware_software_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The VMware software bundle to install on the ESXi hosts in the SDDC. To get a list of the available versions, use <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/vmware/20200501/SupportedVmwareSoftwareVersionSummary/ListSupportedVmwareSoftwareVersions'>ListSupportedVmwareSoftwareVersions</a>.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-vsan_vlan_id"></div>
                    <b>vsan_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-vsan_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN to use for the vSAN component of the VMware environment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-vsphere_vlan_id"></div>
                    <b>vsphere_vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-vsphere_vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN to use for the vSphere component of the VMware environment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-workload_network_cidr"></div>
                    <b>workload_network_cidr</b>
                    <a class="ansibleOptionLink" href="#parameter-workload_network_cidr" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application workloads.</div>
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

    
    - name: Create sddc
      oci_ocvp_sddc:
        # required
        compute_availability_domain: Uocm:PHX-AD-1
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        esxi_hosts_count: 56
        provisioning_subnet_id: "ocid1.provisioningsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        vmware_software_version: vmware_software_version_example
        ssh_authorized_keys: ssh_authorized_keys_example
        vsphere_vlan_id: "ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx"
        vmotion_vlan_id: "ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx"
        vsan_vlan_id: "ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_v_tep_vlan_id: "ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_v_tep_vlan_id: "ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_uplink1_vlan_id: "ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_uplink2_vlan_id: "ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        instance_display_name_prefix: instance_display_name_prefix_example
        initial_sku: HOUR
        is_hcx_enabled: true
        is_hcx_enterprise_enabled: true
        is_single_host_sddc: true
        workload_network_cidr: workload_network_cidr_example
        initial_host_shape_name: initial_host_shape_name_example
        initial_host_ocpu_count: 3.4
        is_shielded_instance_enabled: true
        capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
        datastores:
        - # required
          block_volume_ids: [ "block_volume_ids_example" ]
          datastore_type: MANAGEMENT
        display_name: display_name_example
        replication_vlan_id: "ocid1.replicationvlan.oc1..xxxxxxEXAMPLExxxxxx"
        provisioning_vlan_id: "ocid1.provisioningvlan.oc1..xxxxxxEXAMPLExxxxxx"
        hcx_vlan_id: "ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update sddc
      oci_ocvp_sddc:
        # required
        sddc_id: "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example
        vmware_software_version: vmware_software_version_example
        ssh_authorized_keys: ssh_authorized_keys_example
        vsphere_vlan_id: "ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx"
        vmotion_vlan_id: "ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx"
        vsan_vlan_id: "ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_v_tep_vlan_id: "ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_v_tep_vlan_id: "ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_uplink1_vlan_id: "ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_uplink2_vlan_id: "ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx"
        replication_vlan_id: "ocid1.replicationvlan.oc1..xxxxxxEXAMPLExxxxxx"
        provisioning_vlan_id: "ocid1.provisioningvlan.oc1..xxxxxxEXAMPLExxxxxx"
        hcx_vlan_id: "ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Update sddc using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_ocvp_sddc:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example

        # optional
        vmware_software_version: vmware_software_version_example
        ssh_authorized_keys: ssh_authorized_keys_example
        vsphere_vlan_id: "ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx"
        vmotion_vlan_id: "ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx"
        vsan_vlan_id: "ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_v_tep_vlan_id: "ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_v_tep_vlan_id: "ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_uplink1_vlan_id: "ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_uplink2_vlan_id: "ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx"
        replication_vlan_id: "ocid1.replicationvlan.oc1..xxxxxxEXAMPLExxxxxx"
        provisioning_vlan_id: "ocid1.provisioningvlan.oc1..xxxxxxEXAMPLExxxxxx"
        hcx_vlan_id: "ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}

    - name: Delete sddc
      oci_ocvp_sddc:
        # required
        sddc_id: "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

    - name: Delete sddc using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_ocvp_sddc:
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
            <th colspan="3">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-sddc"></div>
                    <b>sddc</b>
                    <a class="ansibleOptionLink" href="#return-sddc" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Sddc resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;capacity_reservation_id&#x27;: &#x27;ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;compute_availability_domain&#x27;: &#x27;Uocm:PHX-AD-1&#x27;, &#x27;datastores&#x27;: [{&#x27;block_volume_ids&#x27;: [], &#x27;capacity&#x27;: 1.2, &#x27;datastore_type&#x27;: &#x27;MANAGEMENT&#x27;}], &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;esxi_hosts_count&#x27;: 56, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;hcx_fqdn&#x27;: &#x27;hcx_fqdn_example&#x27;, &#x27;hcx_initial_password&#x27;: &#x27;example-password&#x27;, &#x27;hcx_on_prem_key&#x27;: &#x27;hcx_on_prem_key_example&#x27;, &#x27;hcx_on_prem_licenses&#x27;: [{&#x27;activation_key&#x27;: &#x27;activation_key_example&#x27;, &#x27;status&#x27;: &#x27;AVAILABLE&#x27;, &#x27;system_name&#x27;: &#x27;system_name_example&#x27;}], &#x27;hcx_private_ip_id&#x27;: &#x27;ocid1.hcxprivateip.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;hcx_vlan_id&#x27;: &#x27;ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;initial_host_ocpu_count&#x27;: 3.4, &#x27;initial_host_shape_name&#x27;: &#x27;initial_host_shape_name_example&#x27;, &#x27;initial_sku&#x27;: &#x27;HOUR&#x27;, &#x27;instance_display_name_prefix&#x27;: &#x27;instance_display_name_prefix_example&#x27;, &#x27;is_hcx_enabled&#x27;: True, &#x27;is_hcx_enterprise_enabled&#x27;: True, &#x27;is_hcx_pending_downgrade&#x27;: True, &#x27;is_shielded_instance_enabled&#x27;: True, &#x27;is_single_host_sddc&#x27;: True, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;nsx_edge_uplink1_vlan_id&#x27;: &#x27;ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;nsx_edge_uplink2_vlan_id&#x27;: &#x27;ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;nsx_edge_uplink_ip_id&#x27;: &#x27;ocid1.nsxedgeuplinkip.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;nsx_edge_v_tep_vlan_id&#x27;: &#x27;ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;nsx_manager_fqdn&#x27;: &#x27;nsx_manager_fqdn_example&#x27;, &#x27;nsx_manager_initial_password&#x27;: &#x27;example-password&#x27;, &#x27;nsx_manager_private_ip_id&#x27;: &#x27;ocid1.nsxmanagerprivateip.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;nsx_manager_username&#x27;: &#x27;nsx_manager_username_example&#x27;, &#x27;nsx_overlay_segment_name&#x27;: &#x27;nsx_overlay_segment_name_example&#x27;, &#x27;nsx_v_tep_vlan_id&#x27;: &#x27;ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;provisioning_subnet_id&#x27;: &#x27;ocid1.provisioningsubnet.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;provisioning_vlan_id&#x27;: &#x27;ocid1.provisioningvlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;replication_vlan_id&#x27;: &#x27;ocid1.replicationvlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;ssh_authorized_keys&#x27;: &#x27;ssh_authorized_keys_example&#x27;, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_hcx_billing_cycle_end&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_hcx_license_status_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;upgrade_licenses&#x27;: [{&#x27;license_key&#x27;: &#x27;license_key_example&#x27;, &#x27;license_type&#x27;: &#x27;license_type_example&#x27;}], &#x27;vcenter_fqdn&#x27;: &#x27;vcenter_fqdn_example&#x27;, &#x27;vcenter_initial_password&#x27;: &#x27;example-password&#x27;, &#x27;vcenter_private_ip_id&#x27;: &#x27;ocid1.vcenterprivateip.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;vcenter_username&#x27;: &#x27;vcenter_username_example&#x27;, &#x27;vmotion_vlan_id&#x27;: &#x27;ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;vmware_software_version&#x27;: &#x27;vmware_software_version_example&#x27;, &#x27;vsan_vlan_id&#x27;: &#x27;ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;vsphere_upgrade_guide&#x27;: &#x27;vsphere_upgrade_guide_example&#x27;, &#x27;vsphere_upgrade_objects&#x27;: [{&#x27;download_link&#x27;: &#x27;download_link_example&#x27;, &#x27;link_description&#x27;: &#x27;link_description_example&#x27;}], &#x27;vsphere_vlan_id&#x27;: &#x27;ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;workload_network_cidr&#x27;: &#x27;workload_network_cidr_example&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/capacity_reservation_id"></div>
                    <b>capacity_reservation_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/capacity_reservation_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Capacity Reservation.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment that contains the SDDC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/compute_availability_domain"></div>
                    <b>compute_availability_domain</b>
                    <a class="ansibleOptionLink" href="#return-sddc/compute_availability_domain" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The availability domain the ESXi hosts are running in. For Multi-AD SDDC, it is `multi-AD`.</div>
                                            <div>Example: `Uocm:PHX-AD-1`, `multi-AD`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Uocm:PHX-AD-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/datastores"></div>
                    <b>datastores</b>
                    <a class="ansibleOptionLink" href="#return-sddc/datastores" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Datastores used for the Sddc.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/datastores/block_volume_ids"></div>
                    <b>block_volume_ids</b>
                    <a class="ansibleOptionLink" href="#return-sddc/datastores/block_volume_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A list of <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>s of Block Storage Volumes.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/datastores/capacity"></div>
                    <b>capacity</b>
                    <a class="ansibleOptionLink" href="#return-sddc/datastores/capacity" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Size of the Block Storage Volume in GB.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">1.2</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/datastores/datastore_type"></div>
                    <b>datastore_type</b>
                    <a class="ansibleOptionLink" href="#return-sddc/datastores/datastore_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of the datastore.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">MANAGEMENT</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-sddc/defined_tags" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-sddc/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits, whitespaces, dashes and underscores. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/esxi_hosts_count"></div>
                    <b>esxi_hosts_count</b>
                    <a class="ansibleOptionLink" href="#return-sddc/esxi_hosts_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of ESXi hosts in the SDDC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-sddc/freeform_tags" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_fqdn"></div>
                    <b>hcx_fqdn</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_fqdn" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The FQDN for HCX Manager.</div>
                                            <div>Example: `hcx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">hcx_fqdn_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_initial_password"></div>
                    <b>hcx_initial_password</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_initial_password" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The SDDC includes an administrator username and initial password for HCX Manager. Make sure to change this initial HCX Manager password to a different value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">example-password</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_on_prem_key"></div>
                    <b>hcx_on_prem_key</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_on_prem_key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The activation keys to use on the on-premises HCX Enterprise appliances you site pair with HCX Manager in your VMware Solution. The number of keys provided depends on the HCX license type. HCX Advanced provides 3 activation keys. HCX Enterprise provides 10 activation keys.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">hcx_on_prem_key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_on_prem_licenses"></div>
                    <b>hcx_on_prem_licenses</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_on_prem_licenses" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The activation licenses to use on the on-premises HCX Enterprise appliance you site pair with HCX Manager in your VMware Solution.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_on_prem_licenses/activation_key"></div>
                    <b>activation_key</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_on_prem_licenses/activation_key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>HCX on-premise license key value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">activation_key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_on_prem_licenses/status"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_on_prem_licenses/status" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>status of HCX on-premise license.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">AVAILABLE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_on_prem_licenses/system_name"></div>
                    <b>system_name</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_on_prem_licenses/system_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Name of the system that consumed the HCX on-premise license</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">system_name_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_private_ip_id"></div>
                    <b>hcx_private_ip_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_private_ip_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the `PrivateIp` object that is the virtual IP (VIP) for HCX Manager. For information about `PrivateIp` objects, see the Core Services API.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.hcxprivateip.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/hcx_vlan_id"></div>
                    <b>hcx_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/hcx_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the HCX component of the VMware environment.</div>
                                            <div>This attribute is not guaranteed to reflect the HCX VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the HCX VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the HCX component of the VMware environment, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `hcxVlanId` with that new VLAN&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the SDDC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/initial_host_ocpu_count"></div>
                    <b>initial_host_ocpu_count</b>
                    <a class="ansibleOptionLink" href="#return-sddc/initial_host_ocpu_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The initial OCPU count of the SDDC&#x27;s ESXi hosts.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/initial_host_shape_name"></div>
                    <b>initial_host_shape_name</b>
                    <a class="ansibleOptionLink" href="#return-sddc/initial_host_shape_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The initial compute shape of the SDDC&#x27;s ESXi hosts. <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedHostShapes/ListSupportedHostShapes'>ListSupportedHostShapes</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">initial_host_shape_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/initial_sku"></div>
                    <b>initial_sku</b>
                    <a class="ansibleOptionLink" href="#return-sddc/initial_sku" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The billing option selected during SDDC creation. <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus'>ListSupportedSkus</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">HOUR</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/instance_display_name_prefix"></div>
                    <b>instance_display_name_prefix</b>
                    <a class="ansibleOptionLink" href="#return-sddc/instance_display_name_prefix" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A prefix used in the name of each ESXi host and Compute instance in the SDDC. If this isn&#x27;t set, the SDDC&#x27;s `displayName` is used as the prefix.</div>
                                            <div>For example, if the value is `MySDDC`, the ESXi hosts are named `MySDDC-1`, `MySDDC-2`, and so on.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">instance_display_name_prefix_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/is_hcx_enabled"></div>
                    <b>is_hcx_enabled</b>
                    <a class="ansibleOptionLink" href="#return-sddc/is_hcx_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether HCX is enabled for this SDDC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/is_hcx_enterprise_enabled"></div>
                    <b>is_hcx_enterprise_enabled</b>
                    <a class="ansibleOptionLink" href="#return-sddc/is_hcx_enterprise_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether HCX Enterprise is enabled for this SDDC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/is_hcx_pending_downgrade"></div>
                    <b>is_hcx_pending_downgrade</b>
                    <a class="ansibleOptionLink" href="#return-sddc/is_hcx_pending_downgrade" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether SDDC is pending downgrade from HCX Enterprise to HCX Advanced.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/is_shielded_instance_enabled"></div>
                    <b>is_shielded_instance_enabled</b>
                    <a class="ansibleOptionLink" href="#return-sddc/is_shielded_instance_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether shielded instance is enabled at the SDDC level.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/is_single_host_sddc"></div>
                    <b>is_single_host_sddc</b>
                    <a class="ansibleOptionLink" href="#return-sddc/is_single_host_sddc" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether this SDDC is designated for only single ESXi host.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-sddc/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the SDDC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_edge_uplink1_vlan_id"></div>
                    <b>nsx_edge_uplink1_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_edge_uplink1_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the NSX Edge Uplink 1 component of the VMware environment.</div>
                                            <div>This attribute is not guaranteed to reflect the NSX Edge Uplink 1 VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the NSX Edge Uplink 1 VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the NSX Edge Uplink 1 component of the VMware environment, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `nsxEdgeUplink1VlanId` with that new VLAN&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_edge_uplink2_vlan_id"></div>
                    <b>nsx_edge_uplink2_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_edge_uplink2_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the NSX Edge Uplink 2 component of the VMware environment.</div>
                                            <div>This attribute is not guaranteed to reflect the NSX Edge Uplink 2 VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the NSX Edge Uplink 2 VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the NSX Edge Uplink 2 component of the VMware environment, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `nsxEdgeUplink2VlanId` with that new VLAN&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_edge_uplink_ip_id"></div>
                    <b>nsx_edge_uplink_ip_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_edge_uplink_ip_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the `PrivateIp` object that is the virtual IP (VIP) for the NSX Edge Uplink. Use this OCID as the route target for route table rules when setting up connectivity between the SDDC and other networks. For information about `PrivateIp` objects, see the Core Services API.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.nsxedgeuplinkip.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_edge_v_tep_vlan_id"></div>
                    <b>nsx_edge_v_tep_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_edge_v_tep_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the NSX Edge VTEP component of the VMware environment.</div>
                                            <div>This attribute is not guaranteed to reflect the NSX Edge VTEP VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the NSX Edge VTEP VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the NSX Edge VTEP component of the VMware environment, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `nsxEdgeVTepVlanId` with that new VLAN&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_manager_fqdn"></div>
                    <b>nsx_manager_fqdn</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_manager_fqdn" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The FQDN for NSX Manager.</div>
                                            <div>Example: `nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">nsx_manager_fqdn_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_manager_initial_password"></div>
                    <b>nsx_manager_initial_password</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_manager_initial_password" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The SDDC includes an administrator username and initial password for NSX Manager. Make sure to change this initial NSX Manager password to a different value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">example-password</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_manager_private_ip_id"></div>
                    <b>nsx_manager_private_ip_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_manager_private_ip_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the `PrivateIp` object that is the virtual IP (VIP) for NSX Manager. For information about `PrivateIp` objects, see the Core Services API.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.nsxmanagerprivateip.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_manager_username"></div>
                    <b>nsx_manager_username</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_manager_username" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The SDDC includes an administrator username and initial password for NSX Manager. You can change this initial username to a different value in NSX Manager.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">nsx_manager_username_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_overlay_segment_name"></div>
                    <b>nsx_overlay_segment_name</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_overlay_segment_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The VMware NSX overlay workload segment to host your application. Connect to workload portgroup in vCenter to access this overlay segment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">nsx_overlay_segment_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/nsx_v_tep_vlan_id"></div>
                    <b>nsx_v_tep_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/nsx_v_tep_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the NSX VTEP component of the VMware environment.</div>
                                            <div>This attribute is not guaranteed to reflect the NSX VTEP VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the NSX VTEP VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the NSX VTEP component of the VMware environment, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `nsxVTepVlanId` with that new VLAN&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/provisioning_subnet_id"></div>
                    <b>provisioning_subnet_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/provisioning_subnet_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the management subnet used to provision the SDDC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.provisioningsubnet.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/provisioning_vlan_id"></div>
                    <b>provisioning_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/provisioning_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the Provisioning component of the VMware environment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.provisioningvlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/replication_vlan_id"></div>
                    <b>replication_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/replication_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the vSphere Replication component of the VMware environment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.replicationvlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/ssh_authorized_keys"></div>
                    <b>ssh_authorized_keys</b>
                    <a class="ansibleOptionLink" href="#return-sddc/ssh_authorized_keys" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on each ESXi host. Use a newline character to separate multiple keys. The SSH keys must be in the format required for the `authorized_keys` file.</div>
                                            <div>This attribute is not guaranteed to reflect the public SSH keys currently installed on the ESXi hosts in the SDDC. The purpose of this attribute is to show the public SSH keys that Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you upgrade the existing ESXi hosts in the SDDC to use different SSH keys, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `sshAuthorizedKeys` with the new public keys.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ssh_authorized_keys_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-sddc/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the SDDC was created, in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/time_hcx_billing_cycle_end"></div>
                    <b>time_hcx_billing_cycle_end</b>
                    <a class="ansibleOptionLink" href="#return-sddc/time_hcx_billing_cycle_end" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time current HCX Enterprise billing cycle ends, in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/time_hcx_license_status_updated"></div>
                    <b>time_hcx_license_status_updated</b>
                    <a class="ansibleOptionLink" href="#return-sddc/time_hcx_license_status_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the SDDC&#x27;s HCX on-premise license status was updated, in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-sddc/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the SDDC was updated, in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/upgrade_licenses"></div>
                    <b>upgrade_licenses</b>
                    <a class="ansibleOptionLink" href="#return-sddc/upgrade_licenses" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The vSphere licenses to use when upgrading the SDDC.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/upgrade_licenses/license_key"></div>
                    <b>license_key</b>
                    <a class="ansibleOptionLink" href="#return-sddc/upgrade_licenses/license_key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>vSphere license key value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">license_key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/upgrade_licenses/license_type"></div>
                    <b>license_type</b>
                    <a class="ansibleOptionLink" href="#return-sddc/upgrade_licenses/license_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>vSphere license type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">license_type_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vcenter_fqdn"></div>
                    <b>vcenter_fqdn</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vcenter_fqdn" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The FQDN for vCenter.</div>
                                            <div>Example: `vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">vcenter_fqdn_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vcenter_initial_password"></div>
                    <b>vcenter_initial_password</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vcenter_initial_password" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The SDDC includes an administrator username and initial password for vCenter. Make sure to change this initial vCenter password to a different value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">example-password</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vcenter_private_ip_id"></div>
                    <b>vcenter_private_ip_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vcenter_private_ip_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the `PrivateIp` object that is the virtual IP (VIP) for vCenter. For information about `PrivateIp` objects, see the Core Services API.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vcenterprivateip.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vcenter_username"></div>
                    <b>vcenter_username</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vcenter_username" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The SDDC includes an administrator username and initial password for vCenter. You can change this initial username to a different value in vCenter.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">vcenter_username_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vmotion_vlan_id"></div>
                    <b>vmotion_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vmotion_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the vMotion component of the VMware environment.</div>
                                            <div>This attribute is not guaranteed to reflect the vMotion VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the vMotion VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the vMotion component of the VMware environment, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `vmotionVlanId` with that new VLAN&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vmware_software_version"></div>
                    <b>vmware_software_version</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vmware_software_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>In general, this is a specific version of bundled VMware software supported by Oracle Cloud VMware Solution (see <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/vmware/20200501/SupportedVmwareSoftwareVersionSummary/ListSupportedVmwareSoftwareVersions'>ListSupportedVmwareSoftwareVersions</a>).</div>
                                            <div>This attribute is not guaranteed to reflect the version of software currently installed on the ESXi hosts in the SDDC. The purpose of this attribute is to show the version of software that the Oracle Cloud VMware Solution will install on any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer version of bundled VMware software supported by the Oracle Cloud VMware Solution, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `vmwareSoftwareVersion` with that new version.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">vmware_software_version_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vsan_vlan_id"></div>
                    <b>vsan_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vsan_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the vSAN component of the VMware environment.</div>
                                            <div>This attribute is not guaranteed to reflect the vSAN VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the vSAN VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the vSAN component of the VMware environment, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `vsanVlanId` with that new VLAN&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vsphere_upgrade_guide"></div>
                    <b>vsphere_upgrade_guide</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vsphere_upgrade_guide" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The link to guidance for upgrading vSphere.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">vsphere_upgrade_guide_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vsphere_upgrade_objects"></div>
                    <b>vsphere_upgrade_objects</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vsphere_upgrade_objects" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The links to binary objects needed to upgrade vSphere.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/vsphere_upgrade_objects/download_link"></div>
                    <b>download_link</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vsphere_upgrade_objects/download_link" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Binary object download link.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">download_link_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-sddc/vsphere_upgrade_objects/link_description"></div>
                    <b>link_description</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vsphere_upgrade_objects/link_description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Binary object description.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">link_description_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/vsphere_vlan_id"></div>
                    <b>vsphere_vlan_id</b>
                    <a class="ansibleOptionLink" href="#return-sddc/vsphere_vlan_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VLAN used by the SDDC for the vSphere component of the VMware environment.</div>
                                            <div>This attribute is not guaranteed to reflect the vSphere VLAN currently used by the ESXi hosts in the SDDC. The purpose of this attribute is to show the vSphere VLAN that the Oracle Cloud VMware Solution will use for any new ESXi hosts that you *add to this SDDC in the future* with <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost'>CreateEsxiHost</a>.</div>
                                            <div>Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN for the vSphere component of the VMware environment, you should use <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc'>UpdateSddc</a> to update the SDDC&#x27;s `vsphereVlanId` with that new VLAN&#x27;s OCID.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-sddc/workload_network_cidr"></div>
                    <b>workload_network_cidr</b>
                    <a class="ansibleOptionLink" href="#return-sddc/workload_network_cidr" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application workloads.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">workload_network_cidr_example</div>
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

