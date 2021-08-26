.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.oracle.oci.oci_service_catalog_application_facts_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_service_catalog_application_facts -- Fetches details about one or multiple Application resources in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 2.29.0).

    To install it use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_service_catalog_application_facts`.

.. version_added

.. versionadded:: 2.9 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Fetches details about one or multiple Application resources in Oracle Cloud Infrastructure
- Lists all the applications in a service catalog or a tenancy. If no parameter is specified, all catalogs from all compartments in the tenancy will be scanned for any type of content.


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
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                            <div>The unique identifier for the compartment.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                                                <td colspan="1">
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
                                            <div>Exact match name filter.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-entity_id"></div>
                    <b>entity_id</b>
                    <a class="ansibleOptionLink" href="#parameter-entity_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique identifier of the entity associated with service catalog.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-entity_type"></div>
                    <b>entity_type</b>
                    <a class="ansibleOptionLink" href="#parameter-entity_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The type of the application in the service catalog.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-is_featured"></div>
                    <b>is_featured</b>
                    <a class="ansibleOptionLink" href="#parameter-is_featured" title="Permalink to this option"></a>
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
                                            <div>Indicates whether to show only featured resources. If this is set to `false` or is omitted, then all resources will be returned.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-package_type"></div>
                    <b>package_type</b>
                    <a class="ansibleOptionLink" href="#parameter-package_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STACK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Name of the package type. If multiple package types are provided, then any resource with one or more matching package types will be returned.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-pricing"></div>
                    <b>pricing</b>
                    <a class="ansibleOptionLink" href="#parameter-pricing" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>FREE</li>
                                                                                                                                                                                                <li>BYOL</li>
                                                                                                                                                                                                <li>PAYGO</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Name of the pricing type. If multiple pricing types are provided, then any resource with one or more matching pricing models will be returned.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-publisher_id"></div>
                    <b>publisher_id</b>
                    <a class="ansibleOptionLink" href="#parameter-publisher_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Limit results to just this publisher.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-service_catalog_id"></div>
                    <b>service_catalog_id</b>
                    <a class="ansibleOptionLink" href="#parameter-service_catalog_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique identifier for the service catalog.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sort_order"></div>
                    <b>sort_order</b>
                    <a class="ansibleOptionLink" href="#parameter-sort_order" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ASC</li>
                                                                                                                                                                                                <li>DESC</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
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

    
    - name: List applications
      oci_service_catalog_application_facts:
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"





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
                    <div class="ansibleOptionAnchor" id="return-applications"></div>
                    <b>applications</b>
                    <a class="ansibleOptionLink" href="#return-applications" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of Application resources</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;entity_id&#x27;: &#x27;ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;entity_type&#x27;: &#x27;entity_type_example&#x27;, &#x27;is_featured&#x27;: True, &#x27;logo&#x27;: {&#x27;content_url&#x27;: &#x27;content_url_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;mime_type&#x27;: &#x27;mime_type_example&#x27;}, &#x27;package_type&#x27;: &#x27;STACK&#x27;, &#x27;pricing_type&#x27;: &#x27;FREE&#x27;, &#x27;publisher&#x27;: {&#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;}, &#x27;short_description&#x27;: &#x27;short_description_example&#x27;}]</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-applications/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name that service catalog should use to display this application.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/entity_id"></div>
                    <b>entity_id</b>
                    <a class="ansibleOptionLink" href="#return-applications/entity_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Identifier of the application from a service catalog.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/entity_type"></div>
                    <b>entity_type</b>
                    <a class="ansibleOptionLink" href="#return-applications/entity_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of an application in the service catalog.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">entity_type_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/is_featured"></div>
                    <b>is_featured</b>
                    <a class="ansibleOptionLink" href="#return-applications/is_featured" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether the application is featured.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/logo"></div>
                    <b>logo</b>
                    <a class="ansibleOptionLink" href="#return-applications/logo" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-applications/logo/content_url"></div>
                    <b>content_url</b>
                    <a class="ansibleOptionLink" href="#return-applications/logo/content_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The content URL of the uploaded data.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">content_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-applications/logo/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-applications/logo/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name used to refer to the uploaded data.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-applications/logo/mime_type"></div>
                    <b>mime_type</b>
                    <a class="ansibleOptionLink" href="#return-applications/logo/mime_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The MIME type of the uploaded data.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">mime_type_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/package_type"></div>
                    <b>package_type</b>
                    <a class="ansibleOptionLink" href="#return-applications/package_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of the packages withing the application.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">STACK</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/pricing_type"></div>
                    <b>pricing_type</b>
                    <a class="ansibleOptionLink" href="#return-applications/pricing_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Summary of the pricing types available across all packages in the application.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">FREE</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/publisher"></div>
                    <b>publisher</b>
                    <a class="ansibleOptionLink" href="#return-applications/publisher" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-applications/publisher/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-applications/publisher/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the publisher.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-applications/publisher/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-applications/publisher/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The unique identifier for the publisher.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-applications/short_description"></div>
                    <b>short_description</b>
                    <a class="ansibleOptionLink" href="#return-applications/short_description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A short description of the application.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">short_description_example</div>
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

