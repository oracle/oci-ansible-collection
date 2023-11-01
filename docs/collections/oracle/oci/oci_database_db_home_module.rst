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

.. _ansible_collections.oracle.oci.oci_database_db_home_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_database_db_home -- Manage a DbHome resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.33.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_database_db_home`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a DbHome resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new Database Home in the specified database system based on the request parameters you provide. Applies to bare metal DB systems, Exadata systems, and Exadata Cloud@Customer systems.


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
                                                                                                                                                                                                <li>security_token</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                            <div>The compartment <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-database"></div>
                    <b>database</b>
                    <a class="ansibleOptionLink" href="#parameter-database" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when source is one of [&#x27;VM_CLUSTER_BACKUP&#x27;, &#x27;DATABASE&#x27;, &#x27;DB_BACKUP&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/admin_password"></div>
                    <b>admin_password</b>
                    <a class="ansibleOptionLink" href="#parameter-database/admin_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/backup_id"></div>
                    <b>backup_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database/backup_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The backup <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>.</div>
                                            <div>Required when source is one of [&#x27;VM_CLUSTER_BACKUP&#x27;, &#x27;DB_BACKUP&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/backup_tde_password"></div>
                    <b>backup_tde_password</b>
                    <a class="ansibleOptionLink" href="#parameter-database/backup_tde_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The password to open the TDE wallet.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_BACKUP&#x27;, &#x27;DATABASE&#x27;, &#x27;DB_BACKUP&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/character_set"></div>
                    <b>character_set</b>
                    <a class="ansibleOptionLink" href="#parameter-database/character_set" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The character set for the database.  The default is AL32UTF8. Allowed values are:</div>
                                            <div>AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/database_id"></div>
                    <b>database_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database/database_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The database <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>.</div>
                                            <div>Required when source is &#x27;DATABASE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/database_software_image_id"></div>
                    <b>database_software_image_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database/database_software_image_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The database software image <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a></div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config"></div>
                    <b>db_backup_config</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/auto_backup_enabled"></div>
                    <b>auto_backup_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/auto_backup_enabled" title="Permalink to this option"></a>
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
                                            <div>If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/auto_backup_window"></div>
                    <b>auto_backup_window</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/auto_backup_window" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SLOT_ONE</li>
                                                                                                                                                                                                <li>SLOT_TWO</li>
                                                                                                                                                                                                <li>SLOT_THREE</li>
                                                                                                                                                                                                <li>SLOT_FOUR</li>
                                                                                                                                                                                                <li>SLOT_FIVE</li>
                                                                                                                                                                                                <li>SLOT_SIX</li>
                                                                                                                                                                                                <li>SLOT_SEVEN</li>
                                                                                                                                                                                                <li>SLOT_EIGHT</li>
                                                                                                                                                                                                <li>SLOT_NINE</li>
                                                                                                                                                                                                <li>SLOT_TEN</li>
                                                                                                                                                                                                <li>SLOT_ELEVEN</li>
                                                                                                                                                                                                <li>SLOT_TWELVE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time windows. If no option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM (exclusive).</div>
                                            <div>Example: `SLOT_TWO`</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/auto_full_backup_day"></div>
                    <b>auto_full_backup_day</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/auto_full_backup_day" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SUNDAY</li>
                                                                                                                                                                                                <li>MONDAY</li>
                                                                                                                                                                                                <li>TUESDAY</li>
                                                                                                                                                                                                <li>WEDNESDAY</li>
                                                                                                                                                                                                <li>THURSDAY</li>
                                                                                                                                                                                                <li>FRIDAY</li>
                                                                                                                                                                                                <li>SATURDAY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Day of the week the full backup should be applied on the database system. If no option is selected, the value is null and we will default to Sunday.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/auto_full_backup_window"></div>
                    <b>auto_full_backup_window</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/auto_full_backup_window" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SLOT_ONE</li>
                                                                                                                                                                                                <li>SLOT_TWO</li>
                                                                                                                                                                                                <li>SLOT_THREE</li>
                                                                                                                                                                                                <li>SLOT_FOUR</li>
                                                                                                                                                                                                <li>SLOT_FIVE</li>
                                                                                                                                                                                                <li>SLOT_SIX</li>
                                                                                                                                                                                                <li>SLOT_SEVEN</li>
                                                                                                                                                                                                <li>SLOT_EIGHT</li>
                                                                                                                                                                                                <li>SLOT_NINE</li>
                                                                                                                                                                                                <li>SLOT_TEN</li>
                                                                                                                                                                                                <li>SLOT_ELEVEN</li>
                                                                                                                                                                                                <li>SLOT_TWELVE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Time window selected for initiating full backup for the database system. There are twelve available two-hour time windows. If no option is selected, the value is null and a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM (exclusive).</div>
                                            <div>Example: `SLOT_TWO`</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/backup_deletion_policy"></div>
                    <b>backup_deletion_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/backup_deletion_policy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DELETE_IMMEDIATELY</li>
                                                                                                                                                                                                <li>DELETE_AFTER_RETENTION_PERIOD</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>This defines when the backups will be deleted. - IMMEDIATE option keep the backup for predefined time i.e 72 hours and then delete permanently... - RETAIN will keep the backups as per the policy defined for database backups.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/backup_destination_details"></div>
                    <b>backup_destination_details</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/backup_destination_details" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Backup destination details.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/backup_destination_details/dbrs_policy_id"></div>
                    <b>dbrs_policy_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/backup_destination_details/dbrs_policy_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the DBRS policy used for backup.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/backup_destination_details/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/backup_destination_details/id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the backup destination.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/backup_destination_details/internet_proxy"></div>
                    <b>internet_proxy</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/backup_destination_details/internet_proxy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Proxy URL to connect to object store.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/backup_destination_details/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/backup_destination_details/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>NFS</li>
                                                                                                                                                                                                <li>RECOVERY_APPLIANCE</li>
                                                                                                                                                                                                <li>OBJECT_STORE</li>
                                                                                                                                                                                                <li>LOCAL</li>
                                                                                                                                                                                                <li>DBRS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of the database backup destination.</div>
                                            <div>Required when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/backup_destination_details/vpc_password"></div>
                    <b>vpc_password</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/backup_destination_details/vpc_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/backup_destination_details/vpc_user"></div>
                    <b>vpc_user</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/backup_destination_details/vpc_user" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/recovery_window_in_days"></div>
                    <b>recovery_window_in_days</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/recovery_window_in_days" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of days between the current and the earliest point of recoverability covered by automatic backups. This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window. When the value is updated, it is applied to all existing automatic backups.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_backup_config/run_immediate_full_backup"></div>
                    <b>run_immediate_full_backup</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_backup_config/run_immediate_full_backup" title="Permalink to this option"></a>
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
                                            <div>If set to true, configures automatic full backups in the local region (the region of the DB system) for the first backup run immediately.</div>
                                            <div>Applicable when source is &#x27;NONE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_name"></div>
                    <b>db_name</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.</div>
                                            <div>Required when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_unique_name"></div>
                    <b>db_unique_name</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_unique_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The `DB_UNIQUE_NAME` of the Oracle Database being backed up.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/db_workload"></div>
                    <b>db_workload</b>
                    <a class="ansibleOptionLink" href="#parameter-database/db_workload" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OLTP</li>
                                                                                                                                                                                                <li>DSS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>**Deprecated.** The dbWorkload field has been deprecated for Exadata Database Service on Dedicated Infrastructure, Exadata Database Service on Cloud@Customer, and Base Database Service. Support for this attribute will end in November 2023. You may choose to update your custom scripts to exclude the dbWorkload attribute. After November 2023 if you pass a value to the dbWorkload attribute, it will be ignored.</div>
                                            <div>The database workload type.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-database/defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-database/freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see <a href='https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm'>Resource Tags</a>.</div>
                                            <div>Example: `{&quot;Department&quot;: &quot;Finance&quot;}`</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/kms_key_id"></div>
                    <b>kms_key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database/kms_key_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/kms_key_version_id"></div>
                    <b>kms_key_version_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database/kms_key_version_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/ncharacter_set"></div>
                    <b>ncharacter_set</b>
                    <a class="ansibleOptionLink" href="#parameter-database/ncharacter_set" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The national character set for the database.  The default is AL16UTF16. Allowed values are: AL16UTF16 or UTF8.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/pdb_name"></div>
                    <b>pdb_name</b>
                    <a class="ansibleOptionLink" href="#parameter-database/pdb_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/sid_prefix"></div>
                    <b>sid_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-database/sid_prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies a prefix for the `Oracle SID` of the database to be created.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_BACKUP&#x27;, &#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;, &#x27;DB_BACKUP&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/tde_wallet_password"></div>
                    <b>tde_wallet_password</b>
                    <a class="ansibleOptionLink" href="#parameter-database/tde_wallet_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The optional password to open the TDE wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, #, or -.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/time_stamp_for_point_in_time_recovery"></div>
                    <b>time_stamp_for_point_in_time_recovery</b>
                    <a class="ansibleOptionLink" href="#parameter-database/time_stamp_for_point_in_time_recovery" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The point in time of the original database from which the new database is created. If not specifed, the latest backup is used to create the database.</div>
                                            <div>Applicable when source is &#x27;DATABASE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-database/vault_id"></div>
                    <b>vault_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database/vault_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Oracle Cloud Infrastructure <a href='https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts'>vault</a>.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-database_software_image_id"></div>
                    <b>database_software_image_id</b>
                    <a class="ansibleOptionLink" href="#parameter-database_software_image_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The database software image <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a></div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-db_home_id"></div>
                    <b>db_home_id</b>
                    <a class="ansibleOptionLink" href="#parameter-db_home_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Database Home <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a>.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-db_system_id"></div>
                    <b>db_system_id</b>
                    <a class="ansibleOptionLink" href="#parameter-db_system_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the DB system.</div>
                                            <div>Required when source is one of [&#x27;DATABASE&#x27;, &#x27;NONE&#x27;, &#x27;DB_BACKUP&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-db_version"></div>
                    <b>db_version</b>
                    <a class="ansibleOptionLink" href="#parameter-db_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.</div>
                                            <div>This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier.</div>
                                            <div>Applicable when source is one of [&#x27;VM_CLUSTER_NEW&#x27;, &#x27;NONE&#x27;]</div>
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
                                            <div>The user-provided name of the Database Home.</div>
                                            <div>Required for create, update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-is_desupported_version"></div>
                    <b>is_desupported_version</b>
                    <a class="ansibleOptionLink" href="#parameter-is_desupported_version" title="Permalink to this option"></a>
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
                                            <div>If true, the customer acknowledges that the specified Oracle Database software is an older release that is not currently supported by OCI.</div>
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
                                            <div>The list of attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource are used to uniquely identify a resource.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                            <div>The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-kms_key_version_id"></div>
                    <b>kms_key_version_id</b>
                    <a class="ansibleOptionLink" href="#parameter-kms_key_version_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-one_off_patches"></div>
                    <b>one_off_patches</b>
                    <a class="ansibleOptionLink" href="#parameter-one_off_patches" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of one-off patches for Database Homes.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-patch_details"></div>
                    <b>patch_details</b>
                    <a class="ansibleOptionLink" href="#parameter-patch_details" title="Permalink to this option"></a>
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
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-patch_details/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-patch_details/action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>APPLY</li>
                                                                                                                                                                                                <li>PRECHECK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The action to perform on the patch.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-patch_details/database_software_image_id"></div>
                    <b>database_software_image_id</b>
                    <a class="ansibleOptionLink" href="#parameter-patch_details/database_software_image_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the database software image.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-patch_details/patch_id"></div>
                    <b>patch_id</b>
                    <a class="ansibleOptionLink" href="#parameter-patch_details/patch_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the patch.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-perform_final_backup"></div>
                    <b>perform_final_backup</b>
                    <a class="ansibleOptionLink" href="#parameter-perform_final_backup" title="Permalink to this option"></a>
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
                                            <div>Whether to perform a final backup of the database or not. Default is false.</div>
                                            <div>If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.</div>
                                            <div>This parameter is used in multiple APIs. Refer to the API description for details on how the operation uses it.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                    <div class="ansibleOptionAnchor" id="parameter-source"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-source" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DATABASE</li>
                                                                                                                                                                                                <li>DB_BACKUP</li>
                                                                                                                                                                                                <li>VM_CLUSTER_BACKUP</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>NONE</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>VM_CLUSTER_NEW</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The source of database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a database backup.</div>
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
                                            <div>The state of the DbHome.</div>
                                            <div>Use <em>state=present</em> to create or update a DbHome.</div>
                                            <div>Use <em>state=absent</em> to delete a DbHome.</div>
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
                    <div class="ansibleOptionAnchor" id="parameter-vm_cluster_id"></div>
                    <b>vm_cluster_id</b>
                    <a class="ansibleOptionLink" href="#parameter-vm_cluster_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VM cluster.</div>
                                            <div>Required when source is one of [&#x27;VM_CLUSTER_BACKUP&#x27;, &#x27;VM_CLUSTER_NEW&#x27;]</div>
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

    
    - name: Create db_home with source = DATABASE
      oci_database_db_home:
        # required
        db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        source: DATABASE
        database:
          # required
          admin_password: example-password

          # optional
          database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
          time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
          backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
          backup_tde_password: example-password
          db_name: db_name_example
          db_unique_name: db_unique_name_example
          database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
          pdb_name: pdb_name_example
          tde_wallet_password: example-password
          character_set: character_set_example
          ncharacter_set: ncharacter_set_example
          db_workload: OLTP
          db_backup_config:
            # optional
            auto_backup_enabled: true
            recovery_window_in_days: 56
            auto_backup_window: SLOT_ONE
            auto_full_backup_window: SLOT_ONE
            auto_full_backup_day: SUNDAY
            run_immediate_full_backup: true
            backup_destination_details:
            - # required
              type: NFS

              # optional
              id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
              vpc_user: vpc_user_example
              vpc_password: example-password
              internet_proxy: internet_proxy_example
              dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
            backup_deletion_policy: DELETE_IMMEDIATELY
          freeform_tags: {'Department': 'Finance'}
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
          kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          sid_prefix: sid_prefix_example

        # optional
        display_name: display_name_example
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        is_desupported_version: true

    - name: Create db_home with source = DB_BACKUP
      oci_database_db_home:
        # required
        db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        source: DB_BACKUP
        database:
          # required
          admin_password: example-password

          # optional
          database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
          time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
          backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
          backup_tde_password: example-password
          db_name: db_name_example
          db_unique_name: db_unique_name_example
          database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
          pdb_name: pdb_name_example
          tde_wallet_password: example-password
          character_set: character_set_example
          ncharacter_set: ncharacter_set_example
          db_workload: OLTP
          db_backup_config:
            # optional
            auto_backup_enabled: true
            recovery_window_in_days: 56
            auto_backup_window: SLOT_ONE
            auto_full_backup_window: SLOT_ONE
            auto_full_backup_day: SUNDAY
            run_immediate_full_backup: true
            backup_destination_details:
            - # required
              type: NFS

              # optional
              id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
              vpc_user: vpc_user_example
              vpc_password: example-password
              internet_proxy: internet_proxy_example
              dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
            backup_deletion_policy: DELETE_IMMEDIATELY
          freeform_tags: {'Department': 'Finance'}
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
          kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          sid_prefix: sid_prefix_example

        # optional
        display_name: display_name_example
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        is_desupported_version: true

    - name: Create db_home with source = VM_CLUSTER_BACKUP
      oci_database_db_home:
        # required
        source: VM_CLUSTER_BACKUP
        vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        database:
          # required
          admin_password: example-password

          # optional
          database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
          time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
          backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
          backup_tde_password: example-password
          db_name: db_name_example
          db_unique_name: db_unique_name_example
          database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
          pdb_name: pdb_name_example
          tde_wallet_password: example-password
          character_set: character_set_example
          ncharacter_set: ncharacter_set_example
          db_workload: OLTP
          db_backup_config:
            # optional
            auto_backup_enabled: true
            recovery_window_in_days: 56
            auto_backup_window: SLOT_ONE
            auto_full_backup_window: SLOT_ONE
            auto_full_backup_day: SUNDAY
            run_immediate_full_backup: true
            backup_destination_details:
            - # required
              type: NFS

              # optional
              id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
              vpc_user: vpc_user_example
              vpc_password: example-password
              internet_proxy: internet_proxy_example
              dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
            backup_deletion_policy: DELETE_IMMEDIATELY
          freeform_tags: {'Department': 'Finance'}
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
          kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          sid_prefix: sid_prefix_example

        # optional
        display_name: display_name_example
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        is_desupported_version: true

    - name: Create db_home with source = NONE
      oci_database_db_home:
        # required
        db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        source: NONE
        is_desupported_version: true
        db_version: db_version_example
        database:
          # required
          admin_password: example-password

          # optional
          database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
          time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
          backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
          backup_tde_password: example-password
          db_name: db_name_example
          db_unique_name: db_unique_name_example
          database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
          pdb_name: pdb_name_example
          tde_wallet_password: example-password
          character_set: character_set_example
          ncharacter_set: ncharacter_set_example
          db_workload: OLTP
          db_backup_config:
            # optional
            auto_backup_enabled: true
            recovery_window_in_days: 56
            auto_backup_window: SLOT_ONE
            auto_full_backup_window: SLOT_ONE
            auto_full_backup_day: SUNDAY
            run_immediate_full_backup: true
            backup_destination_details:
            - # required
              type: NFS

              # optional
              id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
              vpc_user: vpc_user_example
              vpc_password: example-password
              internet_proxy: internet_proxy_example
              dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
            backup_deletion_policy: DELETE_IMMEDIATELY
          freeform_tags: {'Department': 'Finance'}
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
          kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          sid_prefix: sid_prefix_example

    - name: Create db_home with source = VM_CLUSTER_NEW
      oci_database_db_home:
        # required
        source: VM_CLUSTER_NEW
        vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example
        kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        is_desupported_version: true
        db_version: db_version_example
        database:
          # required
          admin_password: example-password

          # optional
          database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
          time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
          backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
          backup_tde_password: example-password
          db_name: db_name_example
          db_unique_name: db_unique_name_example
          database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
          pdb_name: pdb_name_example
          tde_wallet_password: example-password
          character_set: character_set_example
          ncharacter_set: ncharacter_set_example
          db_workload: OLTP
          db_backup_config:
            # optional
            auto_backup_enabled: true
            recovery_window_in_days: 56
            auto_backup_window: SLOT_ONE
            auto_full_backup_window: SLOT_ONE
            auto_full_backup_day: SUNDAY
            run_immediate_full_backup: true
            backup_destination_details:
            - # required
              type: NFS

              # optional
              id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
              vpc_user: vpc_user_example
              vpc_password: example-password
              internet_proxy: internet_proxy_example
              dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
            backup_deletion_policy: DELETE_IMMEDIATELY
          freeform_tags: {'Department': 'Finance'}
          defined_tags: {'Operations': {'CostCenter': 'US'}}
          kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
          kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
          vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
          sid_prefix: sid_prefix_example

    - name: Update db_home
      oci_database_db_home:
        # required
        db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        patch_details:
          # optional
          patch_id: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
          database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
          action: APPLY
        one_off_patches: [ "one_off_patches_example" ]

    - name: Update db_home using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_database_db_home:
        # required
        display_name: display_name_example
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        patch_details:
          # optional
          patch_id: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
          database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
          action: APPLY
        one_off_patches: [ "one_off_patches_example" ]

    - name: Delete db_home
      oci_database_db_home:
        # required
        db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

        # optional
        perform_final_backup: true

    - name: Delete db_home using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_database_db_home:
        # required
        display_name: display_name_example
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent





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
                    <div class="ansibleOptionAnchor" id="return-db_home"></div>
                    <b>db_home</b>
                    <a class="ansibleOptionLink" href="#return-db_home" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the DbHome resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;database_software_image_id&#x27;: &#x27;ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;db_home_location&#x27;: &#x27;db_home_location_example&#x27;, &#x27;db_system_id&#x27;: &#x27;ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;db_version&#x27;: &#x27;db_version_example&#x27;, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;kms_key_id&#x27;: &#x27;ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;last_patch_history_entry_id&#x27;: &#x27;ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;PROVISIONING&#x27;, &#x27;one_off_patches&#x27;: [], &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;vm_cluster_id&#x27;: &#x27;ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-db_home/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/database_software_image_id"></div>
                    <b>database_software_image_id</b>
                    <a class="ansibleOptionLink" href="#return-db_home/database_software_image_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The database software image <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/db_home_location"></div>
                    <b>db_home_location</b>
                    <a class="ansibleOptionLink" href="#return-db_home/db_home_location" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The location of the Oracle Database Home.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">db_home_location_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/db_system_id"></div>
                    <b>db_system_id</b>
                    <a class="ansibleOptionLink" href="#return-db_home/db_system_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the DB system.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/db_version"></div>
                    <b>db_version</b>
                    <a class="ansibleOptionLink" href="#return-db_home/db_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Oracle Database version.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">db_version_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-db_home/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The user-provided name for the Database Home. The name does not need to be unique.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-db_home/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the Database Home.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/kms_key_id"></div>
                    <b>kms_key_id</b>
                    <a class="ansibleOptionLink" href="#return-db_home/kms_key_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/last_patch_history_entry_id"></div>
                    <b>last_patch_history_entry_id</b>
                    <a class="ansibleOptionLink" href="#return-db_home/last_patch_history_entry_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the last patch history. This value is updated as soon as a patch operation is started.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-db_home/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Additional information about the current lifecycle state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-db_home/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the Database Home.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">PROVISIONING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/one_off_patches"></div>
                    <b>one_off_patches</b>
                    <a class="ansibleOptionLink" href="#return-db_home/one_off_patches" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of one-off patches for Database Homes.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-db_home/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the Database Home was created.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-db_home/vm_cluster_id"></div>
                    <b>vm_cluster_id</b>
                    <a class="ansibleOptionLink" href="#return-db_home/vm_cluster_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the VM cluster.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx</div>
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

