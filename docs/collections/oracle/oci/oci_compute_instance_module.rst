.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.oracle.oci.oci_compute_instance_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_compute_instance -- Manage an Instance resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_.

    To install it use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_compute_instance`.

.. version_added

.. versionadded:: 2.9 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete an Instance resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new instance in the specified compartment and the specified availability domain. For general information about instances, see `Overview of the Compute Service <https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm>`_.
- For information about access control and compartments, see `Overview of the IAM Service <https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm>`_.
- For information about availability domains, see `Regions and Availability Domains <https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm>`_. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.
- All Oracle Cloud Infrastructure resources, including instances, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.
- To launch an instance using an image or a boot volume use the `sourceDetails` parameter in `LaunchInstanceDetails <https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/20160918/LaunchInstanceDetails>`_.
- When you launch an instance, it is automatically attached to a virtual network interface card (VNIC), called the *primary VNIC*. The VNIC has a private IP address from the subnet's CIDR. You can either assign a private IP address of your choice or let Oracle automatically assign one. You can choose whether the instance has a public IP address. To retrieve the addresses, use the `ListVnicAttachments <https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/VnicAttachment/ListVnicAttachments>`_ operation to get the VNIC ID for the instance, and then call `GetVnic <https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vnic/GetVnic>`_ with the VNIC ID.
- You can later add secondary VNICs to an instance. For more information, see L(Virtual Network Interface Cards (VNICs),https://docs.cloud.oracle.com/Content/Network/Tasks/managingVNICs.htm).
- To launch an instance from a Marketplace image listing, you must provide the image ID of the listing resource version that you want, but you also must subscribe to the listing before you try to launch the instance. To subscribe to the listing, use the `GetAppCatalogListingAgreements <https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements>`_ operation to get the signature for the terms of use agreement for the desired listing resource version. Then, call `CreateAppCatalogSubscription <https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription>`_ with the signature. To get the image ID for the LaunchInstance operation, call `GetAppCatalogListingResourceVersion <https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion>`_.
- This resource has the following action operations in the :ref:`oci_instance_actions <ansible_collections.oci_instance_actions_module>` module: stop, start, softreset, reset, softstop.

.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.7
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
                    <div class="ansibleOptionAnchor" id="parameter-agent_config"></div>
                    <b>agent_config</b>
                    <a class="ansibleOptionLink" href="#parameter-agent_config" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-agent_config/is_management_disabled"></div>
                    <b>is_management_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-agent_config/is_management_disabled" title="Permalink to this option"></a>
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
                                            <div>Whether the agent running on the instance can run all the available management plugins. Default value is false.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-agent_config/is_monitoring_disabled"></div>
                    <b>is_monitoring_disabled</b>
                    <a class="ansibleOptionLink" href="#parameter-agent_config/is_monitoring_disabled" title="Permalink to this option"></a>
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
                                            <div>Whether the agent running on the instance can gather performance metrics and monitor the instance. Default value is false.</div>
                                            <div>This parameter is updatable.</div>
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
                                            <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_OCID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user&#x27;s OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
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
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-availability_config"></div>
                    <b>availability_config</b>
                    <a class="ansibleOptionLink" href="#parameter-availability_config" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-availability_config/recovery_action"></div>
                    <b>recovery_action</b>
                    <a class="ansibleOptionLink" href="#parameter-availability_config/recovery_action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>RESTORE_INSTANCE</li>
                                                                                                                                                                                                <li>STOP_INSTANCE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Actions customers can specify that would be applied to their instances after scheduled or unexpected host maintenance. * `RESTORE_INSTANCE` - This would be the default action if recoveryAction is not set. VM instances will be restored to the power state it was in before maintenance. * `STOP_INSTANCE` - This action allow customers to have their VM instances be stopped after maintenance.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-availability_domain"></div>
                    <b>availability_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-availability_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The availability domain of the instance.</div>
                                            <div>Example: `Uocm:PHX-AD-1`</div>
                                            <div>Required for create using <em>state=present</em>.</div>
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
                                            <div>The OCID of the compartment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>Required for delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details"></div>
                    <b>create_vnic_details</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Details for the primary VNIC, which is automatically created and attached when the instance is launched.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/assign_public_ip"></div>
                    <b>assign_public_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/assign_public_ip" title="Permalink to this option"></a>
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
                                            <div>Whether the VNIC should be assigned a public IP address. Defaults to whether the subnet is public or private. If not set and the VNIC is being created in a private subnet (that is, where `prohibitPublicIpOnVnic` = true in the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Subnet/'>Subnet</a>), then no public IP address is assigned. If not set and the subnet is public (`prohibitPublicIpOnVnic` = false), then a public IP address is assigned. If set to true and `prohibitPublicIpOnVnic` = true, an error is returned.</div>
                                            <div>**Note:** This public IP address is associated with the primary private IP on the VNIC. For more information, see <a href='https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPaddresses.htm'>IP Addresses</a>.</div>
                                            <div>**Note:** There&#x27;s a limit to the number of <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PublicIp/'>public IPs</a> a VNIC or instance can have. If you try to create a secondary VNIC with an assigned public IP for an instance that has already reached its public IP limit, an error is returned. For information about the public IP limits, see <a href='https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm'>Public IP Addresses</a>.</div>
                                            <div>Example: `false`</div>
                                            <div>If you specify a `vlanId`, the `assignPublicIp` is required to be set to false. See <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan'>Vlan</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Operations&quot;: {&quot;CostCenter&quot;: &quot;42&quot;}}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/hostname_label"></div>
                    <b>hostname_label</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/hostname_label" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The hostname for the VNIC&#x27;s primary private IP. Used for DNS. The value is the hostname portion of the primary private IP&#x27;s fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with <a href='https://tools.ietf.org/html/rfc952'>RFC 952</a> and <a href='https://tools.ietf.org/html/rfc1123'>RFC 1123</a>. The value appears in the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vnic/'>Vnic</a> object and also the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/'>PrivateIp</a> object returned by <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/ListPrivateIps'>ListPrivateIps</a> and <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/GetPrivateIp'>GetPrivateIp</a>.</div>
                                            <div>For more information, see <a href='https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm'>DNS in Your Virtual Cloud Network</a>.</div>
                                            <div>When launching an instance, use this `hostnameLabel` instead of the deprecated `hostnameLabel` in <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/requests/LaunchInstanceDetails'>LaunchInstanceDetails</a>. If you provide both, the values must match.</div>
                                            <div>Example: `bminstance-1`</div>
                                            <div>If you specify a `vlanId`, the `hostnameLabel` cannot be specified. vnics on a Vlan can not be assigned a hostname  See <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan'>Vlan</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/nsg_ids"></div>
                    <b>nsg_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/nsg_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more information about NSGs, see <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/'>NetworkSecurityGroup</a>.</div>
                                            <div>If a `vlanId` is specified, the `nsgIds` cannot be specified. The `vlanId` indicates that the VNIC will belong to a VLAN instead of a subnet. With VLANs, all VNICs in the VLAN belong to the NSGs that are associated with the VLAN. See <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan'>Vlan</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/private_ip"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/private_ip" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A private IP address of your choice to assign to the VNIC. Must be an available IP address within the subnet&#x27;s CIDR. If you don&#x27;t specify a value, Oracle automatically assigns a private IP address from the subnet. This is the VNIC&#x27;s *primary* private IP address. The value appears in the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vnic/'>Vnic</a> object and also the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/'>PrivateIp</a> object returned by <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/ListPrivateIps'>ListPrivateIps</a> and <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/GetPrivateIp'>GetPrivateIp</a>.</div>
                                            <div>If you specify a `vlanId`, the `privateIp` cannot be specified. See <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan'>Vlan</a>.</div>
                                            <div>Example: `10.0.3.3`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/skip_source_dest_check"></div>
                    <b>skip_source_dest_check</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/skip_source_dest_check" title="Permalink to this option"></a>
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
                                            <div>Whether the source/destination check is disabled on the VNIC. Defaults to `false`, which means the check is performed. For information about why you would skip the source/destination check, see <a href='https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm#privateip'>Using a Private IP as a Route Target</a>.</div>
                                            <div>If you specify a `vlanId`, the `skipSourceDestCheck` cannot be specified because the source/destination check is always disabled for VNICs in a VLAN. See <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan'>Vlan</a>.</div>
                                            <div>Example: `true`</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the subnet to create the VNIC in. When launching an instance, use this `subnetId` instead of the deprecated `subnetId` in <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/requests/LaunchInstanceDetails'>LaunchInstanceDetails</a>. At least one of them is required; if you provide both, the values must match.</div>
                                            <div>If you are an Oracle Cloud VMware Solution customer and creating a secondary VNIC in a VLAN instead of a subnet, provide a `vlanId` instead of a `subnetId`. If you provide both a `vlanId` and `subnetId`, the request fails.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-create_vnic_details/vlan_id"></div>
                    <b>vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-create_vnic_details/vlan_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Provide this attribute only if you are an Oracle Cloud VMware Solution customer and creating a secondary VNIC in a VLAN. The value is the OCID of the VLAN. See <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Vlan'>Vlan</a>.</div>
                                            <div>Provide a `vlanId` instead of a `subnetId`. If you provide both a `vlanId` and `subnetId`, the request fails.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-dedicated_vm_host_id"></div>
                    <b>dedicated_vm_host_id</b>
                    <a class="ansibleOptionLink" href="#parameter-dedicated_vm_host_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the dedicated VM host.</div>
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
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                            <div>Example: `My bare metal instance`</div>
                                            <div>Required for create, update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-extended_metadata"></div>
                    <b>extended_metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-extended_metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.</div>
                                            <div>They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).</div>
                                            <div>The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-fault_domain"></div>
                    <b>fault_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-fault_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.</div>
                                            <div>If you do not specify the fault domain, the system selects one for you.</div>
                                            <div>To get a list of fault domains, use the <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/FaultDomain/ListFaultDomains'>ListFaultDomains</a> operation in the Identity and Access Management Service API.</div>
                                            <div>Example: `FAULT-DOMAIN-1`</div>
                                            <div>This parameter is updatable.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-hostname_label"></div>
                    <b>hostname_label</b>
                    <a class="ansibleOptionLink" href="#parameter-hostname_label" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Deprecated. Instead use `hostnameLabel` in <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/'>CreateVnicDetails</a>. If you provide both, the values must match.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#parameter-image_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Deprecated. Use `sourceDetails` with <a href='https://docs.cloud.oracle.com/en- us/iaas/api/#/en/iaas/latest/requests/InstanceSourceViaImageDetails'>InstanceSourceViaImageDetails</a> source type instead. If you specify values for both, the values must match.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>
                    <b>instance_id</b>
                    <a class="ansibleOptionLink" href="#parameter-instance_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the instance.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-ipxe_script"></div>
                    <b>ipxe_script</b>
                    <a class="ansibleOptionLink" href="#parameter-ipxe_script" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>This is an advanced option.</div>
                                            <div>When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.</div>
                                            <div>If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots; however, you should be aware that the same iPXE script will run every time an instance boots; not only after the initial LaunchInstance call.</div>
                                            <div>The default iPXE script connects to the instance&#x27;s local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance&#x27;s local boot volume over iSCSI the same way as the default iPXE script, you should use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot.</div>
                                            <div>For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see <a href='https://docs.cloud.oracle.com/Content/Compute/References/bringyourownimage.htm'>Bring Your Own Image</a>.</div>
                                            <div>For more information about iPXE, see http://ipxe.org.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-is_pv_encryption_in_transit_enabled"></div>
                    <b>is_pv_encryption_in_transit_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_pv_encryption_in_transit_enabled" title="Permalink to this option"></a>
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
                                            <div>Whether to enable in-transit encryption for the data volume&#x27;s paravirtualized attachment. The default value is false.</div>
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
                                            <div>The list of comma-separated attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource are used to uniquely identify a resource.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-launch_options"></div>
                    <b>launch_options</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_options" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_options/boot_volume_type"></div>
                    <b>boot_volume_type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_options/boot_volume_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ISCSI</li>
                                                                                                                                                                                                <li>SCSI</li>
                                                                                                                                                                                                <li>IDE</li>
                                                                                                                                                                                                <li>VFIO</li>
                                                                                                                                                                                                <li>PARAVIRTUALIZED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Emulation type for the boot volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data volumes on Oracle-provided images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on Oracle-provided images.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_options/firmware"></div>
                    <b>firmware</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_options/firmware" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>BIOS</li>
                                                                                                                                                                                                <li>UEFI_64</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Firmware used to boot VM.  Select the option that matches your operating system. * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders. * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the default for Oracle-provided images.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_options/is_consistent_volume_naming_enabled"></div>
                    <b>is_consistent_volume_naming_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_options/is_consistent_volume_naming_enabled" title="Permalink to this option"></a>
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
                                            <div>Whether to enable consistent volume naming feature. Defaults to false.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_options/is_pv_encryption_in_transit_enabled"></div>
                    <b>is_pv_encryption_in_transit_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_options/is_pv_encryption_in_transit_enabled" title="Permalink to this option"></a>
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
                                            <div>Deprecated. Instead use `isPvEncryptionInTransitEnabled` in <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/datatypes/LaunchInstanceDetails'>LaunchInstanceDetails</a>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_options/network_type"></div>
                    <b>network_type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_options/network_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>E1000</li>
                                                                                                                                                                                                <li>VFIO</li>
                                                                                                                                                                                                <li>PARAVIRTUALIZED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Emulation type for the physical network interface card (NIC). * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver. * `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-launch_options/remote_data_volume_type"></div>
                    <b>remote_data_volume_type</b>
                    <a class="ansibleOptionLink" href="#parameter-launch_options/remote_data_volume_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ISCSI</li>
                                                                                                                                                                                                <li>SCSI</li>
                                                                                                                                                                                                <li>IDE</li>
                                                                                                                                                                                                <li>VFIO</li>
                                                                                                                                                                                                <li>PARAVIRTUALIZED</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Emulation type for volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data volumes on Oracle-provided images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on Oracle-provided images.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-metadata"></div>
                    <b>metadata</b>
                    <a class="ansibleOptionLink" href="#parameter-metadata" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Custom metadata key/value pairs that you provide, such as the SSH public key required to connect to the instance.</div>
                                            <div>A metadata service runs on every launched instance. The service is an HTTP endpoint listening on 169.254.169.254. You can use the service to:</div>
                                            <div>* Provide information to <a href='https://cloudinit.readthedocs.org/en/latest/'>Cloud-Init</a> to be used for various system initialization tasks.</div>
                                            <div>* Get information about the instance, including the custom metadata that you provide when you launch the instance.</div>
                                            <div>**Providing Cloud-Init Metadata**</div>
                                            <div>You can use the following metadata key names to provide information to Cloud-Init:</div>
                                            <div>**&quot;ssh_authorized_keys&quot;** - Provide one or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for the default user on the instance. Use a newline character to separate multiple keys. The SSH keys must be in the format necessary for the `authorized_keys` file, as shown in the example below.</div>
                                            <div>**&quot;user_data&quot;** - Provide your own base64-encoded data to be used by Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For information about how to take advantage of user data, see the <a href='http://cloudinit.readthedocs.org/en/latest/topics/format.html'>Cloud-Init Documentation</a>.</div>
                                            <div>**Metadata Example**</div>
                                            <div>&quot;metadata&quot; : { &quot;quake_bot_level&quot; : &quot;Severe&quot;, &quot;ssh_authorized_keys&quot; : &quot;ssh-rsa &lt;your_public_SSH_key&gt;== rsa-key-20160227&quot;, &quot;user_data&quot; : &quot;&lt;your_public_SSH_key&gt;==&quot; } **Getting Metadata on the Instance**</div>
                                            <div>To get information about your instance, connect to the instance using SSH and issue any of the following GET requests:</div>
                                            <div>curl -H &quot;Authorization: Bearer Oracle&quot; http://169.254.169.254/opc/v2/instance/ curl -H &quot;Authorization: Bearer Oracle&quot; http://169.254.169.254/opc/v2/instance/metadata/ curl -H &quot;Authorization: Bearer Oracle&quot; http://169.254.169.254/opc/v2/instance/metadata/&lt;any-key-name&gt;</div>
                                            <div>You&#x27;ll get back a response that includes all the instance information; only the metadata information; or the metadata information for the specified key name, respectively.</div>
                                            <div>The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-preserve_boot_volume"></div>
                    <b>preserve_boot_volume</b>
                    <a class="ansibleOptionLink" href="#parameter-preserve_boot_volume" title="Permalink to this option"></a>
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
                                            <div>Specifies whether to delete or preserve the boot volume when terminating an instance. The default value is false.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-shape"></div>
                    <b>shape</b>
                    <a class="ansibleOptionLink" href="#parameter-shape" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The shape of an instance. The shape determines the number of CPUs, amount of memory, and other resources allocated to the instance.</div>
                                            <div>You can enumerate all available shapes by calling <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/ListShapes'>ListShapes</a>.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-shape_config"></div>
                    <b>shape_config</b>
                    <a class="ansibleOptionLink" href="#parameter-shape_config" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-shape_config/ocpus"></div>
                    <b>ocpus</b>
                    <a class="ansibleOptionLink" href="#parameter-shape_config/ocpus" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The total number of OCPUs available to the instance.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-source_details"></div>
                    <b>source_details</b>
                    <a class="ansibleOptionLink" href="#parameter-source_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Details for creating an instance. Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-source_details/boot_volume_id"></div>
                    <b>boot_volume_id</b>
                    <a class="ansibleOptionLink" href="#parameter-source_details/boot_volume_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the boot volume used to boot the instance.</div>
                                            <div>Required when source_type is &#x27;bootVolume&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-source_details/boot_volume_size_in_gbs"></div>
                    <b>boot_volume_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#parameter-source_details/boot_volume_size_in_gbs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB).</div>
                                            <div>Applicable when source_type is &#x27;image&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-source_details/image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#parameter-source_details/image_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the image used to boot the instance.</div>
                                            <div>Required when source_type is &#x27;image&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-source_details/kms_key_id"></div>
                    <b>kms_key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-source_details/kms_key_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the Key Management key to assign as the master encryption key for the boot volume.</div>
                                            <div>Applicable when source_type is &#x27;image&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-source_details/source_type"></div>
                    <b>source_type</b>
                    <a class="ansibleOptionLink" href="#parameter-source_details/source_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>image</li>
                                                                                                                                                                                                <li>bootVolume</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.</div>
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
                                            <div>The state of the Instance.</div>
                                            <div>Use <em>state=present</em> to create or update an Instance.</div>
                                            <div>Use <em>state=absent</em> to delete an Instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-subnet_id"></div>
                    <b>subnet_id</b>
                    <a class="ansibleOptionLink" href="#parameter-subnet_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Deprecated. Instead use `subnetId` in <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/CreateVnicDetails/'>CreateVnicDetails</a>. At least one of them is required; if you provide both, the values must match.</div>
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

    
    - name: Create instance
      oci_compute_instance:
        display_name: myinstance1
        availability_domain: Uocm:PHX-AD-1
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
        shape: VM.Standard2.1
        metadata:
          foo: bar
          baz: quux
        source_details:
          source_type: image
          image_id: ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx
        create_vnic_details:
          hostname_label: myinstance1
          private_ip: 10.0.0.5
          subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa

    - name: Create instance
      oci_compute_instance:
        display_name: myinstance1
        availability_domain: Uocm:PHX-AD-1
        fault_domain: FAULT-DOMAIN-2
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
        shape: VM.Standard2.1
        source_details:
          source_type: bootVolume
          boot_volume_id: ocid1.bootvolume.oc1.iad.xxxxxEXAMPLExxxxx
        create_vnic_details:
          hostname_label: myinstance1
          private_ip: 10.0.0.5
          subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa

    - name: Create instance
      oci_compute_instance:
        display_name: myinstance1
        availability_domain: Uocm:PHX-AD-1
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
        shape: VM.Standard2.1
        source_details:
          source_type: image
          image_id: ocid1.image.oc1.phx.xxxxxEXAMPLExxxxx
          boot_volume_size_in_gbs: 100
        create_vnic_details:
          hostname_label: myinstance1
          subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...5iddusmpqpaoa

    - name: Update instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_compute_instance:
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        display_name: myinstance1
        fault_domain: FAULT-DOMAIN-2
        freeform_tags: {'Department': 'Finance'}
        shape: VM.Standard2.1

    - name: Update instance
      oci_compute_instance:
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        display_name: myinstance1
        instance_id: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx

    - name: Delete instance
      oci_compute_instance:
        instance_id: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
        state: absent

    - name: Delete instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_compute_instance:
        compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq
        display_name: myinstance1
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
                    <div class="ansibleOptionAnchor" id="return-instance"></div>
                    <b>instance</b>
                    <a class="ansibleOptionLink" href="#return-instance" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Instance resource acted upon by the current operation</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;agent_config&#x27;: {&#x27;is_management_disabled&#x27;: True, &#x27;is_monitoring_disabled&#x27;: True}, &#x27;availability_config&#x27;: {&#x27;recovery_action&#x27;: &#x27;RESTORE_INSTANCE&#x27;}, &#x27;availability_domain&#x27;: &#x27;Uocm:PHX-AD-1&#x27;, &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;dedicated_vm_host_id&#x27;: &#x27;ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;display_name&#x27;: &#x27;My bare metal instance&#x27;, &#x27;extended_metadata&#x27;: {}, &#x27;fault_domain&#x27;: &#x27;FAULT-DOMAIN-1&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;image_id&#x27;: &#x27;ocid1.image.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;ipxe_script&#x27;: &#x27;ipxe_script_example&#x27;, &#x27;launch_mode&#x27;: &#x27;NATIVE&#x27;, &#x27;launch_options&#x27;: {&#x27;boot_volume_type&#x27;: &#x27;ISCSI&#x27;, &#x27;firmware&#x27;: &#x27;BIOS&#x27;, &#x27;is_consistent_volume_naming_enabled&#x27;: True, &#x27;is_pv_encryption_in_transit_enabled&#x27;: True, &#x27;network_type&#x27;: &#x27;E1000&#x27;, &#x27;remote_data_volume_type&#x27;: &#x27;ISCSI&#x27;}, &#x27;lifecycle_state&#x27;: &#x27;MOVING&#x27;, &#x27;metadata&#x27;: {}, &#x27;primary_private_ip&#x27;: &#x27;10.0.0.10&#x27;, &#x27;primary_public_ip&#x27;: &#x27;140.34.93.209&#x27;, &#x27;region&#x27;: &#x27;region_example&#x27;, &#x27;shape&#x27;: &#x27;shape_example&#x27;, &#x27;shape_config&#x27;: {&#x27;gpu_description&#x27;: &#x27;gpu_description_example&#x27;, &#x27;gpus&#x27;: 56, &#x27;local_disk_description&#x27;: &#x27;local_disk_description_example&#x27;, &#x27;local_disks&#x27;: 56, &#x27;local_disks_total_size_in_gbs&#x27;: 3.4, &#x27;max_vnic_attachments&#x27;: 56, &#x27;memory_in_gbs&#x27;: 3.4, &#x27;networking_bandwidth_in_gbps&#x27;: 3.4, &#x27;ocpus&#x27;: 3.4, &#x27;processor_description&#x27;: &#x27;processor_description_example&#x27;}, &#x27;source_details&#x27;: {&#x27;boot_volume_id&#x27;: &#x27;ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;boot_volume_size_in_gbs&#x27;: 56, &#x27;image_id&#x27;: &#x27;ocid1.image.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;kms_key_id&#x27;: &#x27;ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;source_type&#x27;: &#x27;source_type_example&#x27;}, &#x27;system_tags&#x27;: {}, &#x27;time_created&#x27;: &#x27;2016-08-25T21:10:29.600Z&#x27;, &#x27;time_maintenance_reboot_due&#x27;: &#x27;2018-05-25T21:10:29.600Z&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config"></div>
                    <b>agent_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config/is_management_disabled"></div>
                    <b>is_management_disabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config/is_management_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the agent running on the instance can run all the available management plugins.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/agent_config/is_monitoring_disabled"></div>
                    <b>is_monitoring_disabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/agent_config/is_monitoring_disabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the agent running on the instance can gather performance metrics and monitor the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/availability_config"></div>
                    <b>availability_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/availability_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-instance/availability_config/recovery_action"></div>
                    <b>recovery_action</b>
                    <a class="ansibleOptionLink" href="#return-instance/availability_config/recovery_action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Actions customers can specify that would be applied to their instances after scheduled or unexpected host maintenance. * `RESTORE_INSTANCE` - This would be the default action if recoveryAction is not set. VM instances will be restored to the power state it was in before maintenance. * `STOP_INSTANCE` - This action allow customers to have their VM instances be stopped after maintenance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">RESTORE_INSTANCE</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/availability_domain"></div>
                    <b>availability_domain</b>
                    <a class="ansibleOptionLink" href="#return-instance/availability_domain" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The availability domain the instance is running in.</div>
                                            <div>Example: `Uocm:PHX-AD-1`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Uocm:PHX-AD-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the compartment that contains the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/dedicated_vm_host_id"></div>
                    <b>dedicated_vm_host_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/dedicated_vm_host_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of dedicated VM host.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.dedicatedvmhost.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-instance/defined_tags" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-instance/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-instance/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                            <div>Example: `My bare metal instance`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">My bare metal instance</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/extended_metadata"></div>
                    <b>extended_metadata</b>
                    <a class="ansibleOptionLink" href="#return-instance/extended_metadata" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the `metadata` object.</div>
                                            <div>They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps only).</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/fault_domain"></div>
                    <b>fault_domain</b>
                    <a class="ansibleOptionLink" href="#return-instance/fault_domain" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the fault domain the instance is running in.</div>
                                            <div>A fault domain is a grouping of hardware and infrastructure within an availability domain. Each availability domain contains three fault domains. Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or Compute hardware maintenance that affects one fault domain does not affect instances in other fault domains.</div>
                                            <div>If you do not specify the fault domain, the system selects one for you.</div>
                                            <div>Example: `FAULT-DOMAIN-1`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FAULT-DOMAIN-1</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-instance/freeform_tags" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-instance/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-instance/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/image_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Deprecated. Use `sourceDetails` instead.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.image.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/ipxe_script"></div>
                    <b>ipxe_script</b>
                    <a class="ansibleOptionLink" href="#return-instance/ipxe_script" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>When a bare metal or virtual machine instance boots, the iPXE firmware that runs on the instance is configured to run an iPXE script to continue the boot process.</div>
                                            <div>If you want more control over the boot process, you can provide your own custom iPXE script that will run when the instance boots; however, you should be aware that the same iPXE script will run every time an instance boots; not only after the initial LaunchInstance call.</div>
                                            <div>The default iPXE script connects to the instance&#x27;s local boot volume over iSCSI and performs a network boot. If you use a custom iPXE script and want to network-boot from the instance&#x27;s local boot volume over iSCSI the same way as the default iPXE script, you should use the following iSCSI IP address: 169.254.0.2, and boot volume IQN: iqn.2015-02.oracle.boot.</div>
                                            <div>For more information about the Bring Your Own Image feature of Oracle Cloud Infrastructure, see <a href='https://docs.cloud.oracle.com/Content/Compute/References/bringyourownimage.htm'>Bring Your Own Image</a>.</div>
                                            <div>For more information about iPXE, see http://ipxe.org.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ipxe_script_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_mode"></div>
                    <b>launch_mode</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_mode" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are: * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images. * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers. * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NATIVE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options"></div>
                    <b>launch_options</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Options for tuning the compatibility and performance of VM shapes. The values that you specify override any default values.</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/boot_volume_type"></div>
                    <b>boot_volume_type</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/boot_volume_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Emulation type for the boot volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data volumes on Oracle-provided images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on Oracle-provided images.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ISCSI</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/firmware"></div>
                    <b>firmware</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/firmware" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Firmware used to boot VM.  Select the option that matches your operating system. * `BIOS` - Boot VM using BIOS style firmware.  This is compatible with both 32 bit and 64 bit operating systems that boot using MBR style bootloaders. * `UEFI_64` - Boot VM using UEFI style firmware compatible with 64 bit operating systems.  This is the default for Oracle-provided images.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">BIOS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/is_consistent_volume_naming_enabled"></div>
                    <b>is_consistent_volume_naming_enabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/is_consistent_volume_naming_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether to enable consistent volume naming feature. Defaults to false.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/is_pv_encryption_in_transit_enabled"></div>
                    <b>is_pv_encryption_in_transit_enabled</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/is_pv_encryption_in_transit_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Deprecated. Instead use `isPvEncryptionInTransitEnabled` in <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/datatypes/LaunchInstanceDetails'>LaunchInstanceDetails</a>.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/network_type"></div>
                    <b>network_type</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/network_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Emulation type for the physical network interface card (NIC). * `E1000` - Emulated Gigabit ethernet controller.  Compatible with Linux e1000 network driver. * `VFIO` - Direct attached Virtual Function network controller. This is the networking type when you launch an instance using hardware-assisted (SR-IOV) networking. * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">E1000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/launch_options/remote_data_volume_type"></div>
                    <b>remote_data_volume_type</b>
                    <a class="ansibleOptionLink" href="#return-instance/launch_options/remote_data_volume_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Emulation type for volume. * `ISCSI` - ISCSI attached block storage device. * `SCSI` - Emulated SCSI disk. * `IDE` - Emulated IDE disk. * `VFIO` - Direct attached Virtual Function storage.  This is the default option for local data volumes on Oracle-provided images. * `PARAVIRTUALIZED` - Paravirtualized disk. This is the default for boot volumes and remote block storage volumes on Oracle-provided images.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ISCSI</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-instance/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">MOVING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/metadata"></div>
                    <b>metadata</b>
                    <a class="ansibleOptionLink" href="#return-instance/metadata" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Custom metadata that you provide.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/primary_private_ip"></div>
                    <b>primary_private_ip</b>
                    <a class="ansibleOptionLink" href="#return-instance/primary_private_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The private IP of the primary VNIC attached to this instance</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">10.0.0.10</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/primary_public_ip"></div>
                    <b>primary_public_ip</b>
                    <a class="ansibleOptionLink" href="#return-instance/primary_public_ip" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The public IP of the primary VNIC attached to this instance</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">140.34.93.209</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#return-instance/region" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The region that contains the availability domain the instance is running in.</div>
                                            <div>For the us-phoenix-1 and us-ashburn-1 regions, `phx` and `iad` are returned, respectively. For all other regions, the full region name is returned.</div>
                                            <div>Examples: `phx`, `eu-frankfurt-1`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">region_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape"></div>
                    <b>shape</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance. You can enumerate all available shapes by calling <a href='https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/ListShapes'>ListShapes</a>.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">shape_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config"></div>
                    <b>shape_config</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/gpu_description"></div>
                    <b>gpu_description</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/gpu_description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A short description of the instance&#x27;s graphics processing unit (GPU).</div>
                                            <div>If the instance does not have any GPUs, this field is `null`.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">gpu_description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/gpus"></div>
                    <b>gpus</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/gpus" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of GPUs available to the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/local_disk_description"></div>
                    <b>local_disk_description</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/local_disk_description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A short description of the local disks available to this instance.</div>
                                            <div>If the instance does not have any local disks, this field is `null`.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">local_disk_description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/local_disks"></div>
                    <b>local_disks</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/local_disks" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of local disks available to the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/local_disks_total_size_in_gbs"></div>
                    <b>local_disks_total_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/local_disks_total_size_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The aggregate size of all local disks, in gigabytes.</div>
                                            <div>If the instance does not have any local disks, this field is `null`.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/max_vnic_attachments"></div>
                    <b>max_vnic_attachments</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/max_vnic_attachments" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum number of VNIC attachments for the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/memory_in_gbs"></div>
                    <b>memory_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/memory_in_gbs" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/networking_bandwidth_in_gbps"></div>
                    <b>networking_bandwidth_in_gbps</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/networking_bandwidth_in_gbps" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">float</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The networking bandwidth available to the instance, in gigabits per second.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">3.4</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/ocpus"></div>
                    <b>ocpus</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/ocpus" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/shape_config/processor_description"></div>
                    <b>processor_description</b>
                    <a class="ansibleOptionLink" href="#return-instance/shape_config/processor_description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A short description of the instance&#x27;s processor (CPU).</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">processor_description_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details"></div>
                    <b>source_details</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details for creating an instance</div>
                                        <br/>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/boot_volume_id"></div>
                    <b>boot_volume_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/boot_volume_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the boot volume used to boot the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/boot_volume_size_in_gbs"></div>
                    <b>boot_volume_size_in_gbs</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/boot_volume_size_in_gbs" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB).</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/image_id"></div>
                    <b>image_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/image_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the image used to boot the instance.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.image.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/kms_key_id"></div>
                    <b>kms_key_id</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/kms_key_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the Key Management key to assign as the master encryption key for the boot volume.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance/source_details/source_type"></div>
                    <b>source_type</b>
                    <a class="ansibleOptionLink" href="#return-instance/source_details/source_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The source type for the instance. Use `image` when specifying the image OCID. Use `bootVolume` when specifying the boot volume OCID.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">source_type_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-instance/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-instance/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the instance was created, in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2016-08-25T21:10:29.600000</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-instance/time_maintenance_reboot_due"></div>
                    <b>time_maintenance_reboot_due</b>
                    <a class="ansibleOptionLink" href="#return-instance/time_maintenance_reboot_due" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the instance is expected to be stopped / started,  in the format defined by <a href='https://tools.ietf.org/html/rfc3339'>RFC3339</a>. After that time if instance hasn&#x27;t been rebooted, Oracle will reboot the instance within 24 hours of the due time. Regardless of how the instance was stopped, the flag will be reset to empty as soon as instance reaches Stopped state. Example: `2018-05-25T21:10:29.600Z`</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2018-05-25T21:10:29.600000</div>
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

