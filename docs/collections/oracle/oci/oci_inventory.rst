.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.oracle.oci.oci_inventory:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci -- Oracle Cloud Infrastructure (OCI) inventory plugin
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_.

    To install it use: :code:`ansible-galaxy collection install oracle.oci`.

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
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                            <th>Configuration</th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config_file"></div>
                    <b>config_file</b>
                    <a class="ansibleOptionLink" href="#parameter-config_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                            <div>
                                env:OCI_CONFIG_FILE
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>The oci config path.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config_profile"></div>
                    <b>config_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-config_profile" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-enable_parallel_processing"></div>
                    <b>enable_parallel_processing</b>
                    <a class="ansibleOptionLink" href="#parameter-enable_parallel_processing" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>Use multiple threads to speedup lookup.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-filters"></div>
                    <b>filters</b>
                    <a class="ansibleOptionLink" href="#parameter-filters" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>A dictionary of filter value pairs. Available filters  are display_name, lifecycle_state, availability_domain, defined_tags, freeform_tags.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hostnames"></div>
                    <b>hostnames</b>
                    <a class="ansibleOptionLink" href="#parameter-hostnames" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
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
                                                                <td colspan="1">
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
                                                                            <div>
                                env:OCI_ANSIBLE_AUTH_TYPE
                                                                                            </div>
                                                                    </td>
                                                <td>
                                            <div>Use instance principal based authentication. If not set, the API key in your config will be used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-keyed_groups"></div>
                    <b>keyed_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-keyed_groups" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-plugin"></div>
                    <b>plugin</b>
                    <a class="ansibleOptionLink" href="#parameter-plugin" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>oci</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>token that ensures this is a source file for the &#x27;oci&#x27; plugin.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-regions"></div>
                    <b>regions</b>
                    <a class="ansibleOptionLink" href="#parameter-regions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                            <div>A list of regions to search. If not specified, the region is read from config file.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                        </table>
    <br/>

.. Notes


.. Seealso


.. Examples

Examples
--------
.. note::
    These examples assume the ``collections`` keyword is defined in  playbook and do not use the fully qualified collection name.

.. code-block:: yaml+jinja

    
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
      - compartment_name: "test"

    # Example filtering using hostname IP
    hostnames:
      - "11.145.214.11"

    # Example group results by key
    keyed_groups:
      - key: availability_domain

    # Example using filters
    filters:
      - availability_domain: "IwGV:US-ASHBURN-AD-3"
      - display_name: "instance20190506231645"
      - lifecycle_state: "RUNNING"
      - defined_tags: {
         "ansible_tag_2": {
           "ansibletag448": "test_value"
          }
        }
      - freeform_tags: {
         "oci:compute:instanceconfiguration": "ocid1.instanceconfiguration.oc1.phx.xxxx",
         "oci:compute:instancepool": "ocid1.instancepool.oc1.phx.xxxx"
        }

    # Enable Cache
    cache: yes
    cache_plugin: jsonfile
    cache_timeout: 7200
    cache_connection: /tmp/oci-cache
    cache_prefix: oci_




.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors



.. Parsing errors

