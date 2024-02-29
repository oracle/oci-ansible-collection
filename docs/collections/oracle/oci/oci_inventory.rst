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

.. _ansible_collections.oracle.oci.oci_inventory:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci -- Oracle Cloud Infrastructure (OCI) inventory plugin
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.42.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Get inventory hosts from oci.
- Uses a <name>.oci.yaml (or <name>.oci.yml) YAML configuration file.


.. Aliases


.. Requirements


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                            <th>Configuration</th>
                        <th width="100%">Comments</th>
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
                                                                            <div>
                                env:OCI_USER_KEY_FILE
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Full path and filename of the private key (in PEM format). If the key is encrypted with a pass-phrase, the pass_phrase option must also be provided. Preference order is .oci.yml &gt; OCI_USER_KEY_FILE environment variable &gt; settings from config file This option is required if the private key is not specified through a configuration file (See config_file)</div>
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
                                                                            <div>
                                env:OCI_USER_KEY_PASS_PHRASE
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Passphrase used by the key referenced in api_user_key_file, if it is encrypted. Preference order is .oci.yml &gt; OCI_USER_KEY_PASS_PHRASE environment variable &gt; settings from config file This option is required if the passphrase is not specified through a configuration file (See config_file)</div>
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
                                                                            <div>
                                env:OCI_ANSIBLE_AUTH_TYPE
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-cache"></div>
                    <b>cache</b>
                    <a class="ansibleOptionLink" href="#parameter-cache" title="Permalink to this option"></a>
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
                                                    <div> ini entries:
                                                                    <p>
                                        [inventory]<br>cache = no
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_INVENTORY_CACHE
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Toggle to enable/disable the caching of the inventory&#x27;s source data, requires a cache plugin setup to work.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-cache_connection"></div>
                    <b>cache_connection</b>
                    <a class="ansibleOptionLink" href="#parameter-cache_connection" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [defaults]<br>fact_caching_connection = None
                                                                                	
                                    </p>
                                                                    <p>
                                        [inventory]<br>cache_connection = None
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_CACHE_PLUGIN_CONNECTION
                                                                	
                            </div>
                                                    <div>
                                env:ANSIBLE_INVENTORY_CACHE_CONNECTION
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Cache connection data or path, read cache plugin documentation for specifics.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-cache_plugin"></div>
                    <b>cache_plugin</b>
                    <a class="ansibleOptionLink" href="#parameter-cache_plugin" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"memory"</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [defaults]<br>fact_caching = memory
                                                                                	
                                    </p>
                                                                    <p>
                                        [inventory]<br>cache_plugin = memory
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_CACHE_PLUGIN
                                                                	
                            </div>
                                                    <div>
                                env:ANSIBLE_INVENTORY_CACHE_PLUGIN
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Cache plugin to use for the inventory&#x27;s source data.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-cache_prefix"></div>
                    <b>cache_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-cache_prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"ansible_inventory_"</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [default]<br>fact_caching_prefix = ansible_inventory_
                                                                                		<div>
	  	    Removed in: version 2.16
	  	  	    of ansible.builtin
	  	  <br>
	  Why: Fixes typing error in INI section name
	  <br>
	  Alternative: Use the &#39;defaults&#39; section instead
	</div>
	
                                    </p>
                                                                    <p>
                                        [defaults]<br>fact_caching_prefix = ansible_inventory_
                                                                                	
                                    </p>
                                                                    <p>
                                        [inventory]<br>cache_prefix = ansible_inventory_
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_CACHE_PLUGIN_PREFIX
                                                                	
                            </div>
                                                    <div>
                                env:ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Prefix to use for cache plugin files/tables</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-cache_timeout"></div>
                    <b>cache_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-cache_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">3600</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [defaults]<br>fact_caching_timeout = 3600
                                                                                	
                                    </p>
                                                                    <p>
                                        [inventory]<br>cache_timeout = 3600
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_CACHE_PLUGIN_TIMEOUT
                                                                	
                            </div>
                                                    <div>
                                env:ANSIBLE_INVENTORY_CACHE_TIMEOUT
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Cache duration in seconds</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-compartments"></div>
                    <b>compartments</b>
                    <a class="ansibleOptionLink" href="#parameter-compartments" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A dictionary of compartment identifier to obtain list of hosts. This config parameter is optional. If compartment is not specified, the plugin fetches all compartments from the tenancy.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-compartments/compartment_name"></div>
                    <b>compartment_name</b>
                    <a class="ansibleOptionLink" href="#parameter-compartments/compartment_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Name of the compartment. If None and `compartment_ocid` is not set, all the compartments including the root compartment are returned.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-compartments/compartment_ocid"></div>
                    <b>compartment_ocid</b>
                    <a class="ansibleOptionLink" href="#parameter-compartments/compartment_ocid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>OCID of the compartment. If None, root compartment is assumed to be the default value.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-compartments/fetch_hosts_from_subcompartments"></div>
                    <b>fetch_hosts_from_subcompartments</b>
                    <a class="ansibleOptionLink" href="#parameter-compartments/fetch_hosts_from_subcompartments" title="Permalink to this option"></a>
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
                                                                                                                    </td>
                                                <td>
                                            <div>Flag used to fetch hosts from subcompartments. Default value is set to True</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-compartments/parent_compartment_ocid"></div>
                    <b>parent_compartment_ocid</b>
                    <a class="ansibleOptionLink" href="#parameter-compartments/parent_compartment_ocid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>This option is not needed when the compartment_ocid option is used, it is needed when compartment_name is used. OCID of the parent compartment. If None, root compartment is assumed to be parent.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-compose"></div>
                    <b>compose</b>
                    <a class="ansibleOptionLink" href="#parameter-compose" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Create vars from jinja2 expressions.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-config_file"></div>
                    <b>config_file</b>
                    <a class="ansibleOptionLink" href="#parameter-config_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"~/.oci/config"</div>
                                    </td>
                                                    <td>
                                                                            <div>
                                env:OCI_CONFIG_FILE
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>The oci config path. Either pass the &#x27;/full/path/to/config/file&#x27; in inventory plugin configuration file. Or pass the &#x27;relative/path/to/config/file&#x27; with respect to the directory from where inventory command is executed. Relative path should not be relative with respect to inventory plugin configuration file.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-config_profile"></div>
                    <b>config_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-config_profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"DEFAULT"</div>
                                    </td>
                                                    <td>
                                                                            <div>
                                env:OCI_CONFIG_PROFILE
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>The config profile to use.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-debug"></div>
                    <b>debug</b>
                    <a class="ansibleOptionLink" href="#parameter-debug" title="Permalink to this option"></a>
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
                                                                                                                    </td>
                                                <td>
                                            <div>Parameter to enable logs while running the inventory plugin. Default value is set to False</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups"></div>
                    <b>default_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>OCI Inventory plugin creates some groups by default based on these properties [&quot;availability_domain&quot;, &quot;compartment_name&quot;, &quot;region&quot;, &quot;freeform_tags&quot;, &quot;defined_tags&quot;]. If you don&#x27;t want OCI inventory plugin to create these default groups, you can use this option to configure which of these default groups should be created. This option takes a list of properties of inventory hosts based on which the groups will be created. The supported properties are - &quot;availability_domain&quot; - &quot;compartment_name&quot; - &quot;region&quot; - &quot;freeform_tags&quot; - &quot;defined_tags&quot; if empty list is passed to this option, none of the default groups are created. default_groups and default_groups_preferences cannot be used together We recommend to use default_groups_preferences parameter as we will deprecate default_groups parameter in our next major upgrade</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences"></div>
                    <b>default_groups_preferences</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>OCI Inventory plugin creates some groups by default based on these properties [&quot;availability_domain&quot;, &quot;compartment_name&quot;, &quot;region&quot;, &quot;freeform_tags&quot;, &quot;defined_tags&quot;]. If you don&#x27;t want OCI inventory plugin to create these default groups, you can use this option to configure which of these default groups should be created. This option takes a dict of properties of inventory hosts based on which the groups will be created. You can also pass a list of jinja2 expressions under include and exclude if you want to include specific groups to be included/excluded based on these criteria if empty list is passed to this option, none of the default groups are created. default_groups and default_groups_preferences cannot be used together</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/availability_domain"></div>
                    <b>availability_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/availability_domain" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Add groups based on the availability_domain</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/availability_domain/exclude"></div>
                    <b>exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/availability_domain/exclude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, none of the availability_domain will be excluded. if any group is present in both include and exclude, then that group will be excluded.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/availability_domain/include"></div>
                    <b>include</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/availability_domain/include" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, all availability_domain will be included which are not in exclude list</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/compartment_name"></div>
                    <b>compartment_name</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/compartment_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Add groups based on the compartment_name</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/compartment_name/exclude"></div>
                    <b>exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/compartment_name/exclude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, none of the compartment_name will be excluded. if any group is present in both include and exclude, then that group will be excluded.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/compartment_name/include"></div>
                    <b>include</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/compartment_name/include" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, all compartment_name will be included which are not in exclude list</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Add groups based on the defined_tags</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/defined_tags/exclude"></div>
                    <b>exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/defined_tags/exclude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, none of the defined_tags will be excluded. if any group is present in both include and exclude, then that group will be excluded.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/defined_tags/include"></div>
                    <b>include</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/defined_tags/include" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, all defined_tags will be included which are not in exclude list</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Add groups based on the freeform_tags</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/freeform_tags/exclude"></div>
                    <b>exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/freeform_tags/exclude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, none of the freeform_tags will be excluded. if any group is present in both include and exclude, then that group will be excluded.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/freeform_tags/include"></div>
                    <b>include</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/freeform_tags/include" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, all freeform_tags will be included which are not in exclude list</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/region" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Add groups based on the region</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/region/exclude"></div>
                    <b>exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/region/exclude" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, none of the regions will be excluded. if any group is present in both include and exclude, then that group will be excluded.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-default_groups_preferences/region/include"></div>
                    <b>include</b>
                    <a class="ansibleOptionLink" href="#parameter-default_groups_preferences/region/include" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of jinja2 expressions. if this option is not used or empty, all regions will be included which are not in exclude list</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-delegation_token_file"></div>
                    <b>delegation_token_file</b>
                    <a class="ansibleOptionLink" href="#parameter-delegation_token_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                            <div>
                                env:OCI_DELEGATION_TOKEN_FILE
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Path to delegation_token file. If not set then the value of the OCI_DELEGATION_TOKEN_FILE environment variable, if any, is used. Otherwise, defaults to config_file.</div>
                                            <div>This parameter is only applicable when <code>auth_type=instance_obo_user</code> is set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-enable_ipv6"></div>
                    <b>enable_ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-enable_ipv6" title="Permalink to this option"></a>
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
                                                                                                                    </td>
                                                <td>
                                            <div>Fetch IPv6 address information from VNICs. Default value set to True.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-enable_parallel_processing"></div>
                    <b>enable_parallel_processing</b>
                    <a class="ansibleOptionLink" href="#parameter-enable_parallel_processing" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">"yes"</div>
                                    </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Use multiple threads to speedup lookup. Default is set to True</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_compartments"></div>
                    <b>exclude_compartments</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_compartments" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A dictionary of compartment identifier to filter the compartments from which  hosts should be listed from. This config parameter is optional. Suboption is not considered when both compartment_ocid, compartment_name are None</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_compartments/compartment_name"></div>
                    <b>compartment_name</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_compartments/compartment_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Name of the compartment. If None and `compartment_ocid` is not set, this option is not considered for filtering the compartments. If both compartment_ocid and compartment_name are passed, compartment_ocid is considered</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_compartments/compartment_ocid"></div>
                    <b>compartment_ocid</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_compartments/compartment_ocid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>OCID of the compartment.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_compartments/parent_compartment_ocid"></div>
                    <b>parent_compartment_ocid</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_compartments/parent_compartment_ocid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>This option is not needed when the compartment_ocid option is used, it is needed when compartment_name is used. OCID of the parent compartment. If None, root compartment is assumed to be parent.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_compartments/skip_subcompartments"></div>
                    <b>skip_subcompartments</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_compartments/skip_subcompartments" title="Permalink to this option"></a>
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
                                                                                                                    </td>
                                                <td>
                                            <div>Flag used to skip the sub-compartments. Default value is set to True</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-exclude_host_filters"></div>
                    <b>exclude_host_filters</b>
                    <a class="ansibleOptionLink" href="#parameter-exclude_host_filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of Jinja2 conditional expressions. Each expression in the list is evaluated for each host; when any of the expressions is evaluated to Truthy value, the host is excluded from the inventory. exclude_host_filters take priority over the include_host_filters and filters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-fetch_compute_hosts"></div>
                    <b>fetch_compute_hosts</b>
                    <a class="ansibleOptionLink" href="#parameter-fetch_compute_hosts" title="Permalink to this option"></a>
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
                                                                                                                    </td>
                                                <td>
                                            <div>When set, the compute nodes are fetched. Default value set to True.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-fetch_db_hosts"></div>
                    <b>fetch_db_hosts</b>
                    <a class="ansibleOptionLink" href="#parameter-fetch_db_hosts" title="Permalink to this option"></a>
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
                                                                                                                    </td>
                                                <td>
                                            <div>When set, the db nodes are also fetched. Default value set to False.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-filters"></div>
                    <b>filters</b>
                    <a class="ansibleOptionLink" href="#parameter-filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A dictionary of filter value pairs.</div>
                                            <div>Available filters are display_name, lifecycle_state, availability_domain, defined_tags, freeform_tags.</div>
                                            <div>Note: defined_tags and freeform_tags filters are not supported for db hosts. The db hosts will not be returned when you use either of these filters.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-groups"></div>
                    <b>groups</b>
                    <a class="ansibleOptionLink" href="#parameter-groups" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Add hosts to group based on Jinja2 conditionals.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-hostname_format"></div>
                    <b>hostname_format</b>
                    <a class="ansibleOptionLink" href="#parameter-hostname_format" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                            <div>
                                env:OCI_HOSTNAME_FORMAT
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Host naming format to use. Use &#x27;fqdn&#x27; to list hosts using the instance&#x27;s Fully Qualified Domain Name (FQDN). These FQDNs are resolvable within the VCN using the VCN resolver specified through the subnet&#x27;s DHCP options. Please see https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm for more details. Use &#x27;public_ip&#x27; to list hosts using public IP address. Use &#x27;private_ip&#x27; to list hosts using private IP address. Use &#x27;display_name&#x27; to list hosts using display_name of the Instances. &#x27;display_name&#x27; cannot be used when fetch_db_hosts is True. By default, hosts are listed using public IP address. hostname_format_preferences and hostname_format cannot be used together</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-hostname_format_preferences"></div>
                    <b>hostname_format_preferences</b>
                    <a class="ansibleOptionLink" href="#parameter-hostname_format_preferences" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of Jinja2 expressions in order of precedence to compose inventory_hostname. Ignores expression if result is an empty string or None value. hostname_format_preferences and hostname_format cannot be used together. The instance is ignored if none of the hostname_format_preferences resulted in a non-empty value</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-hostnames"></div>
                    <b>hostnames</b>
                    <a class="ansibleOptionLink" href="#parameter-hostnames" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of hostnames to search for.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-include_host_filters"></div>
                    <b>include_host_filters</b>
                    <a class="ansibleOptionLink" href="#parameter-include_host_filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of Jinja2 conditional expressions. Each expression in the list is evaluated for each host; when any of the expressions is evaluated to Truthy value, the host is included in the inventory. include_host_filters and filters options cannot be used together.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-instance_principal_authentication"></div>
                    <b>instance_principal_authentication</b>
                    <a class="ansibleOptionLink" href="#parameter-instance_principal_authentication" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>This parameter is DEPRECATED. Please use auth_type instead.</div>
                                            <div>Use instance principal based authentication. If not set, the API key in your config will be used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups"></div>
                    <b>keyed_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Add hosts to group based on the values of a variable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups/default_value"></div>
                    <b>default_value</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups/default_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.12 of ansible.builtin
                      </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>The default value when the host variable&#x27;s value is an empty string.</div>
                                            <div>This option is mutually exclusive with <code>trailing_separator</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>The key from input dictionary used to generate groups</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups/parent_group"></div>
                    <b>parent_group</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups/parent_group" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>parent group for keyed group</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups/prefix"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups/prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">""</div>
                                    </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A keyed group name will start with this prefix</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups/separator"></div>
                    <b>separator</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups/separator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"_"</div>
                                    </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>separator used to build the keyed group name</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups/trailing_separator"></div>
                    <b>trailing_separator</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups/trailing_separator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.12 of ansible.builtin
                      </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Set this option to <em>False</em> to omit the <code>separator</code> after the host variable when the value is an empty string.</div>
                                            <div>This option is mutually exclusive with <code>default_value</code>.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-leading_separator"></div>
                    <b>leading_separator</b>
                    <a class="ansibleOptionLink" href="#parameter-leading_separator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.11 of ansible.builtin
                      </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>Use in conjunction with keyed_groups.</div>
                                            <div>By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.</div>
                                            <div>This is because the default prefix is &quot;&quot; and the default separator is &quot;_&quot;.</div>
                                            <div>Set this option to False to omit the leading underscore (or other separator) if no prefix is given.</div>
                                            <div>If the group name is derived from a mapping the separator is still used to concatenate the items.</div>
                                            <div>To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-plugin"></div>
                    <b>plugin</b>
                    <a class="ansibleOptionLink" href="#parameter-plugin" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>oracle.oci.oci</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>token that ensures this is a source file for the &#x27;oci&#x27; plugin.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-primary_vnic_only"></div>
                    <b>primary_vnic_only</b>
                    <a class="ansibleOptionLink" href="#parameter-primary_vnic_only" title="Permalink to this option"></a>
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
                                                                            <div>
                                env:OCI_PRIMARY_VNIC_ONLY
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>The default behavior of the plugin is to process all VNIC&#x27;s attached to a compute instance. This might result in instance having multiple entries. When this parameter is set to True, the plugin will only process the primary VNIC and thus having only a single entry for each compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-regions"></div>
                    <b>regions</b>
                    <a class="ansibleOptionLink" href="#parameter-regions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                    </td>
                                                <td>
                                            <div>A list of regions to search. If not specified, the region is read from config file. Use &#x27;all&#x27; to generate inventory from all subscribed regions.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-strict"></div>
                    <b>strict</b>
                    <a class="ansibleOptionLink" href="#parameter-strict" title="Permalink to this option"></a>
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
                                                                                                                    </td>
                                                <td>
                                            <div>If <code>yes</code> make invalid entries a fatal error, otherwise skip and continue.</div>
                                            <div>Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-use_extra_vars"></div>
                    <b>use_extra_vars</b>
                    <a class="ansibleOptionLink" href="#parameter-use_extra_vars" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                          <div style="font-style: italic; font-size: small; color: darkgreen">
                        added in 2.11 of ansible.builtin
                      </div>
                                                              	
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>
                                        [inventory_plugins]<br>use_extra_vars = no
                                                                                	
                                    </p>
                                                            </div>
                                                                            <div>
                                env:ANSIBLE_INVENTORY_USE_EXTRA_VARS
                                                                	
                            </div>
                                                                                            </td>
                                                <td>
                                            <div>Merge extra vars into the available variables for composition (highest precedence).</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    # Please check https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansibleinventoryintro.htm
    # for more scenario based examples.

    # Fetch all hosts
    plugin: oci

    # Optional fields:
    config_file: ~/.oci/config
    config_profile: DEFAULT

    # Example select regions
    regions:
      - us-ashburn-1
      - us-phoenix-1

    # Enable threads to speedup lookup
    enable_parallel_processing: yes

    # Select compartment by ocid or name
    compartments:
      - compartment_ocid: ocid1.compartment.oc1..xxxxxx
        fetch_hosts_from_subcompartments: false

      - compartment_name: "test_compartment"
        parent_compartment_ocid: ocid1.tenancy.oc1..xxxxxx

    # Sets the inventory_hostname to either "display_name+'.oci.com'" or id or hostname_label
    # "'display_name+'.oci.com'" has more preference than id
    hostname_format_preferences:
      - "display_name+'.oci.com'"
      - "id"
      - "hostname_label"

    # Excludes host that is not in the region 'iad' from the inventory
    exclude_host_filters:
      - "region not in ['iad']"

    # Includes only the hosts that has display_name ending with '.oci.com' in the inventory
    include_host_filters:
      - "display_name is match('.*.oci.com')"

    # Example group results by key
    keyed_groups:
      - key: availability_domain

    # Example to create and modify a host variable
    compose:
      ansible_host: display_name+'.oracle.com'

    # Example to use_extra_vars and pass the value of extra_vars variable with inventory command
    # This requires ansible v2.11 or higher
    use_extra_vars: true
    compose:
      example: " 'Hello' +  extra_vars"
    # pass the value of extra_vars variable with ansible-inventory command using -e option
    # ansible-inventory -i /path/to/demo.oci.yml --list -e "extra_vars=ANSIBLE"

    # Environment variable can also be used to pass the value of extra_vars variable.
    # export TEMP_ENV="ANSIBLE"
    # ansible-inventory -i /path/to/demo.oci.yml --list -e "extra_vars='$TEMP_ENV'"

    # Example flag to turn on debug mode
    debug: true

    # Enable Cache
    cache: yes
    cache_plugin: jsonfile
    cache_timeout: 7200
    cache_connection: /tmp/oci-cache
    cache_prefix: oci_

    # DB Hosts
    fetch_db_hosts: True

    # Compute Hosts (bool type)
    fetch_compute_hosts: True

    # Process only the primary vnic of a compute instance
    primary_vnic_only: True

    # Fetch IPv6 address information from VNICs.
    enable_ipv6: True

    # Select compartment by ocid or name
    exclude_compartments:
      - compartment_ocid: ocid1.compartment.oc1..xxxxxx
        skip_subcompartments: false

      - compartment_name: "test_skip_compartment"
        parent_compartment_ocid: ocid1.tenancy.oc1..xxxxxx

    # Create groups based on properties
    default_groups_preferences:
      region:
        include:
            - region=="us-ashburn-1"
      compartment_name:
        exclude:
            - name=="dev_tests"
      availability_domain:
      freeform_tags:
      defined_tags:
        include:
            - <jinja_expression>
            - namespace=="mynamespace" and namespace.key =="mykey"
            - namespace=="mynamespace2" and namespace.key =="mykey2"
        exclude:
            - <jinja_expression>
            - namespace=="mynamespace3" and namespace.key =="mykey3"





.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors



.. Parsing errors

