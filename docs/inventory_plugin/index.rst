OCI Ansible Collection - Inventory Plugin
=========================================

.. contents::
  :depth: 1
  :local:
  :backlinks: none

Introduction
------------

Ansible tracks configuration resources by preserving lists, called
inventory lists, as simple files (also sometimes called a hostfile).
These inventory lists can be static or dynamic. Dynamic lists can
automatically update when inventory resources are added, deleted, or
moved.

Because many Oracle Cloud Infrastructure (OCI) resources are added and
deleted over time, static inventory lists can easily become obsolete.
Tools such as Terraform or the OCI SDKs also may affect your resources.

Oracle Cloud Infrastructure provides a dynamic inventory plugin for
maintaining accurate Ansible inventory.

For more information about Ansible inventory files, see `Working with
Inventory <https://docs.ansible.com/ansible/devel/user_guide/intro_inventory.html>`_
and `Working with Dynamic
Inventory <https://docs.ansible.com/ansible/devel/user_guide/intro_dynamic_inventory.html#intro-dynamic-inventory>`_.

Enabling the Inventory Plugin
-----------------------------

If you have an existing ansible.cfg file and that configuration already
enables plugins using ``enable_plugins``, you must enable the OCI
inventory plugin by adding it as well. For example:

.. code:: yaml

   [inventory]
   enable_plugins = oracle.oci.oci

If you do not already have an ``ansible.cfg`` file that contains
``enable_plugins``, you do not need to add the OCI inventory plugin to
the configuration.

Configuring the Inventory Plugin
--------------------------------

The only requirement for using the OCI inventory plugin after it is
enabled is to provide an inventory source you have permissions to parse.
Inventory sources are defined in a YAML configuration file. See :ref:`User
Permissions <user-permission-label>`
for more information.

To start using the inventory plugin with a YAML configuration source,
create a file with with one of the following accepted filenames:

-  <filename>.oci.yml
-  <filename>.oci.yaml

Add ``plugin: oracle.oci.oci`` to the YAML configuration file.

The minimum inventory source file needed to run the OCI inventory plugin
looks like this, for example:

.. code:: yaml

   # demo.oci.yml
   plugin: oracle.oci.oci

   # Optional fields to specify oci connection config:
   config_file: ~/.oci/config
   config_profile: DEFAULT

This example uses the ``config_file`` and ``config_profile`` parameters
so the plugin can use authentication information that is outlined in the
`SDK and CLI Configuration
File <https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File>`_.
Some parameters can also be provided as environment variables.

For a complete list of parameters and environment variables that the
plugin supports, see `OCI Inventory
Plugin <https://oci-ansible-collection.readthedocs.io/en/latest/collections/oracle/oci/oci_inventory.html#parameters>`_.

.. important::
   By default, the OCI inventory plugin discovers and
   lists only compute instances that have a public IP address. See
   Hostname Format Preferences for more information.

Order of Precedence
-------------------

The inventory plugin uses the following order of precedence when an
option is provided in more than one location:

1. YAML file settings.
2. Environment variables.
3. Configuration settings in the selected profile in your OCI
   configuration file.

Using the Inventory Plugin
--------------------------

Ansible inventory plugins allow you to define the data sources used to
compile an inventory of hosts that Ansible uses to target tasks. These
data sources are accessed by using either the ``-i /path/to/file`` or
the ``-i 'host1, host2'`` command line parameters, or from other
configuration sources.

You can run the inventory with this command, for example:

.. code:: bash

   ansible-inventory -i <filename>.oci.yml --graph

This produces output similar to the following:

::

   @all:
   |--@oci:
   |  |--compute_instance1
   |  |--compute_instance2
   |–@ungrouped:

.. important::

   By default, the inventory is generated for all the
   compartments in the tenancy. You must have ``COMPARTMENT_INSPECT``
   permission on the root compartment for this script to be able to
   access all compartments. However, when ``compartment_ocid`` is
   specified, the inventory is generated for only the specific
   compartment, so you only need ``COMPARTMENT_INSPECT`` permission on
   the specified compartment. For more information, see `How Policies
   Work <https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work>`_.
   To fetch all instance details, you must also have permission to list
   and read instances and VNICs, and read VCNs and subnets. See :ref:`User
   Permissions <user-permission-label>`
   for more information.

You can add inventory plugins to your plugin path and set the default
inventory path to simplify your commands. Add the default inventory path
to the ``[defaults]`` section of your ``ansible.cfg`` file, or use the
``ANSIBLE_INVENTORY`` environment variable to point your inventory
sources. You can then run the following command to yield the same output
as when you pass your YAML configuration sources directly:

.. code:: bash

   ansible-inventory --graph

Inventory plugins normally only execute at the start of a run, before
playbooks, plays, and roles are loaded. You can 're-execute' a plugin by
using the ``meta: refresh_inventory`` task, which clears out the
existing inventory and rebuilds it.

Fetching Database Hosts
~~~~~~~~~~~~~~~~~~~~~~~

By default, the OCI inventory plugin discovers and lists only compute
instances. Database nodes are servers running database software.
Database nodes are fetched by setting the option ``fetch_db_hosts`` to
``true``. For example:

.. code:: yaml

   # demo.oci.yml
   # DB Hosts
   plugin: oracle.oci.oci
   fetch_db_hosts: true

Inventory Output
~~~~~~~~~~~~~~~~

The inventory list that is generated by the inventory plugin is grouped
using the following attributes:

-  The region in which the compute instance resides
-  The name of the compartment the compute instance belongs to
-  The Availability Domain the compute instance is in
-  The ``vcn_id`` of the VCN the compute instance is in
-  The ``subnet_id`` of the subnet the compute instance is in
-  The ``security_list_ids`` of the subnet the compute instance is in
-  The ``image_id`` of the image used to launch the compute instance
-  Shape of the compute instance
-  The compute instance's free-form tags, with the group name set to
   ``tag_<tag_name>=<tag_value>``
-  The compute instance's defined tags, with the group name set to
   ``<tag_namespace>#<tag_name>=<tag_value>``
-  OCI compute instance metadata (key-value pairs), with the group name
   set to ``<metadata-key>=<metadata-value>``
-  OCI compute instance extended metadata (key-value pairs), with the
   group name set to ``<metadata-key>=<metadata-value>``

.. _hostname-format-preferences-label:

Hostname Format Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The inventory generated by the OCI inventory plugin contains only
instances that have a public IP address by default. This is useful in
cases where the Ansible controller node is outside of the VCN, since
Ansible can only reach instances that have public IP addresses.

You can configure the ``inventory_hostname`` to ``private_ip`` or any
custom hostname by passing `Jinja2
expressions <https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html>`_
as a list to the ``hostname_format_preferences`` option. The
``hostname_format_preferences`` option takes a list of Jinja2
expressions in order of precedence to compose ``inventory_hostname``.
The inventory plugin ignores expressions if the result is an empty
string or "None" value. The instance is ignored if none of the
``hostname_format_preferences`` expressions result in a non-empty value.

The following example sets the inventory_hostname to either
``"display_name+'.oci.com'"`` or ``"private_ip"`` or ``"public_ip"``:

.. code:: yaml

   hostname_format_preferences:
   - "display_name+'.oci.com'"
   - "private_ip"
   - "public_ip"

Expressions are evaluated on ``host_vars`` of every instance. Evaluation
respects the order of precedence in your configuration to compose
``inventory_hostname``. In the preceding example,
``"display_name+'.oci.com'"`` is evaluated before ``"private_ip"`` and
``"public_ip"``.

.. _filtering-hosts-label:

Filtering Hosts
~~~~~~~~~~~~~~~

The OCI inventory plugin comes with various filtering options to filter
the hosts returned by the plugin.

Exclude Hosts from Inventory
++++++++++++++++++++++++++++

You can pass a list of `Jinja2 conditional
expressions <https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html>`_
to the ``exclude_host_filters`` parameter. Each expression in the list
is evaluated for each host. When the expression is true, the host is
excluded from the inventory. The ``exclude_host_filters`` parameter
takes priority over the ``include_host_filters`` and ``filters``
options.

The following example excludes hosts that are not in the region 'iad'
from the inventory:

.. code:: yaml

   exclude_host_filters:
   - "region not in ['iad']"

Exclude Hosts Using Freeform Tags
+++++++++++++++++++++++++++++++++

To exclude a host from the inventory using freeform tags, you can use
the following syntax:

.. code:: yaml

   exclude_host_filters:
   # filter the hosts with freeform tag with key <tag_key> which has value <tag_value>
   - "'<tag_value>' == freeform_tags.<tag_key>"
   # filter the hosts which has <tag_key> freeform tag
   - "'<tag_key>' in freefrom_tags"

For example:

.. code:: yaml

   exclude_host_filters:
   - "'operating_system' in freeform_tags"
   - "'linux' == freeform_tags.operating_system"

Exclude Hosts Using Defined Tags
++++++++++++++++++++++++++++++++

To exclude a host from the inventory using defined tags, you can use the
following syntax:

.. code:: yaml

   exclude_host_filters:
   #filter the hosts with defined tag in <namespace> with <tag_key> and <tag_value>
   - "'<tag_value>' == defined_tags.<namespace>.<tag_key>"
   # filter the hosts with <tag_key> in the <namespace> in defined tags
   - "'<tag_key>' in defined_tags.<namespace>"

For example:

.. code:: yaml

   exclude_host_filters:
   - "'ansible' == defined_tags.ansible_collections_tag_namespace.managed_by"
   - "'managed_by' in defined_tags.ansible_collections_tag_namespace"

Include Hosts in Inventory
++++++++++++++++++++++++++

You can pass a list of `Jinja2 conditional
expressions <https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html>`_
to the ``include_host_filters`` parameter. Each expression in the list
is evaluated for each host. When the expression is true, the host is
included in the inventory.

The following example includes only the hosts that have a
``display_name`` ending with '.oci.com' in the inventory:

.. code:: yaml

   include_host_filters:
   - "display_name is match('.*.oci.com')"

.. note::
   The include_host_filters and filters options cannot be used
   together.

Include Hosts Using Freeform Tags
++++++++++++++++++++++++++++++++++

To include a host from the inventory using freeform tags, you can use
the following syntax:

.. code:: yaml

   include_host_filters:
   # filter the hosts with freeform tag with key <tag_key> which has value <tag_value>
   - "'<tag_value>' == freeform_tags.<tag_key>"
   # filter the hosts which has <tag_key> freeform tag
   - "'<tag_key>' in freefrom_tags"

For example:

.. code:: yaml

   include_host_filters:
   - "'operating_system' in freeform_tags"
   - "'linux' == freeform_tags.operating_system"

Include Hosts Using Defined Tags
++++++++++++++++++++++++++++++++

To include a host from the inventory using defined tags, you can use the
following syntax:

.. code:: yaml

   include_host_filters:
   #filter the hosts with defined tag in <namespace> with <tag_key> and <tag_value>
   - "'<tag_value>' == defined_tags.<namespace>.<tag_key>"
   # filter the hosts with <tag_key> in the <namespace> in defined tags
   - "'<tag_key>' in defined_tags.<namespace>"

For example:

.. code:: yaml

   include_host_filters:
   -  "'ansible' == defined_tags.ansible_collections_tag_namespace.managed_by"
   -  "'managed_by' in defined_tags.ansible_collections_tag_namespace"

Enabling Caching
~~~~~~~~~~~~~~~~

Caching can be enabled to speed lookups. You can set caching options for
an individual YAML configuration source or for multiple inventory
sources using environment variables or Ansible configuration files. If
you enable caching for an inventory plugin without providing
inventory-specific caching options, the inventory plugin uses
fact-caching options.

Here is an example of enabling caching for an individual YAML
configuration file:

.. code:: yaml

   # demo.oci.yml
   plugin: oracle.oci.oci
   cache: yes
   cache_plugin: jsonfile
   cache_timeout: 7200
   cache_connection: /tmp/oci_inventory
   cache_prefix: oci

Using Dynamic Groups
~~~~~~~~~~~~~~~~~~~~

You can create dynamic groups using host variables with the constructed
keyed_groups option. The option groups can also be used to create groups
and create and modify host variables. Syntax for keyed groups and groups
that use tags follows:

.. code:: yaml

   keyed_groups:
   - key: freeform_tags.<tag key>
     prefix: <my_prefix>
   - key: defined_tags.<namespace>.<tag key>
     prefix: <my_prefix>

.. code:: yaml

   groups:
   <group_name>: "'<tag_value>' == freeform_tags.<tag_key>"
   <group_name>: "'<tag_value>' == defined_tags.<namespace>.<tag_key>"
   <group_name>: "'<tag_key>' in defined_tags.<namespace>"

For example:

.. code:: yaml

   # demo.oci.yml
   plugin: oracle.oci.oci
   regions:
     - us-phoenix-1
     - us-ashburn-1
   keyed_groups:
     # add hosts to tag_Name_value groups for each oci host's tags.Name variable
     - key: tags.Name
       prefix: tag_Name_
   groups:
     # add hosts to the group development if any of the
     # dictionary's keys or values is the word 'devel'
     development: "'devel' in (tags|list)"
     # add hosts with freefrom_tags that has 'operating_system'
     # key and 'linux' value to 'linux' group
     linux: "'linux' == freeform_tags.operating_system"
     # add hosts with freefrom tags that has 'operating_system' key to os group
     os: "'operating_system' in freeform_tags"
     # add hosts with defined tags in the namespace
     # 'ansible_collections_tag_namespace' with tag 'managed_by' and value 'ansible'
     ansible_managed: "'ansible' == defined_tags.ansible_collections_tag_namespace.managed_by"
     # add hosts with defined tags in the namespace
     # 'ansible_collections_tag_namespace' with tag 'managed_by'
     cm_managed_hosts: "'managed_by' in defined_tags.ansible_collections_tag_namespace"

This example produces output similar to the following:

::

   @all:
   |--@development:
   |  |--compute_instance1
   |  |--compute_instance2
   |--@linux:
   |  |--compute_instance1
   |--@os:
   |  |--compute_instance1
   |  |--compute_instance2
   |--@ansible_managed:
   |  |--compute_instance1
   |--@cm_managed_hosts:
   |  |--compute_instance2
   |--@ungrouped

If a host does not have the variables specified in the configuration,
the host is not added to groups other than those that the inventory
plugin creates and the ``ansible_host`` host variable is not modified.

Examples
--------

The following sections include configuration examples that cover common
inventory scenarios.

Fetch All Compute Hosts
~~~~~~~~~~~~~~~~~~~~~~~

To fetch all hosts, your configuration can be as simple as the following
example:

.. code:: yaml

   plugin: oracle.oci.oci

Fetch Only DB Hosts
~~~~~~~~~~~~~~~~~~~

To fetch all nodes hosting database software while excluding Compute
hosts, your configuration would look like the following example:

.. code:: yaml

   plugin: oracle.oci.oci

   # fetch databse hosts
   fetch_db_hosts: true
   # don't fetch Compute hosts
   fetch_compute_hosts: False

Fetch Hosts from Specific Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fetch hosts only in specified regions, your configuration would look
similar to the following example:

.. code:: yaml

   plugin: oracle.oci.oci

   # Fetch only the hosts in the regions us-ashburn-1, us-phoenix-1
   regions:
     - us-ashburn-1
     - us-phoenix-1

Set Inventory Hostname
~~~~~~~~~~~~~~~~~~~~~~

To set the format of the inventory hostname used in the inventory, your
configuration would include a section similar to the following example:

.. code:: yaml

   plugin: oracle.oci.oci

   # Sets the inventory_hostname to either "display_name+'.oci.com'", "public_ip", "private_ip", or "id"
   # "display_name+'.oci.com'" has more preference than "public_ip", "private_ip", "id".
   hostname_format_preferences:
     - "display_name+'.oci.com'"
     - "public_ip"
     - "private_ip"
     - "id"

See :ref:`Hostname Format
Preferences <hostname-format-preferences-label>`
for more information.

Exclude Hosts from Inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use a `Jinja2 conditional
expression <https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html>`_
to exclude hosts from the inventory, your configuration would include a
section similar to the following example:

.. code:: yaml

   plugin: oracle.oci.oci

   # Includes only the hosts that have a display_name ending with '.oci.com' in the inventory
   include_host_filters:
     - "display_name is match('.*.oci.com')"

See :ref:`Filtering Hosts <filtering-hosts-label>`
for more information.

Include Hosts in Inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~

To use a `Jinja2 conditional
expression <https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html>`_
to include hosts in inventory, your configuration would include a
section similar to the following example:

.. code:: yaml

   plugin: oracle.oci.oci

   # Includes only the hosts that have a display_name ending with '.oci.com' in the inventory
   include_host_filters:
     - "display_name is match('.*.oci.com')"

See :ref:`Filtering Hosts <filtering-hosts-label>`
for more information.

.. note::
   The ``include_host_filters`` and ``filters`` options cannot
   be used together.

Fetch Hosts from Specific Compartments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example shows how to fetch all hosts from the specified
compartments:

.. code:: yaml

   # Fetch all hosts
   plugin: oracle.oci.oci

   # Select compartment by OCID or name
   compartments:
     - compartment_ocid: <ocid1.compartment.oc1..exampleuniqueID>
       fetch_hosts_from_subcompartments: false

     - compartment_name: "<compartment_name>"
       parent_compartment_ocid: <ocid1.tenancy.oc1..exampleuniqueID>

Other Options
~~~~~~~~~~~~~

The following example configuration combines the preceding scenarios
with more configuration options:

.. code:: yaml

   # Fetch all hosts
   plugin: oracle.oci.oci

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
     - compartment_ocid: <ocid1.compartment.oc1..exampleuniqueID>
       fetch_hosts_from_subcompartments: false

     - compartment_name: "<compartment_name>"
       parent_compartment_ocid: <ocid1.tenancy.oc1..exampleuniqueID>

   # Sets the inventory_hostname. Each item is a Jinja2 expression and it gets evaluated on host_vars.
   hostname_format_preferences:
     - "display_name+'.oci.com'"
     - "private_ip"
     - "public_ip"

   # Excludes a host from the inventory when any of the Jinja2 expression evaluates to true.
   exclude_host_filters:
     - "region not in ['iad']"
     - "'<tag_key>' in freeform_tags"
     - "'<tag_value>' == freeform_tags.<tag_key>"
     - "'<tag_value>' == defined_tags.<namespace>.<tag_key>"
     - "'<tag_key>' in defined_tags.<namespace>"

   # Includes a host in the inventory when any of the Jinja2 expression evaluates to true.
   include_host_filters:
     - "display_name is match('.*.oci.com')"
     - "'<tag_key>' in freeform_tags"
     - "'<tag_value>' == freeform_tags.<tag_key>"
     - "'<tag_value>' == defined_tags.<namespace>.<tag_key>"
     - "'<tag_key>' in defined_tags.<namespace>"

   # Example group results by key
   keyed_groups
   - key: freeform_tags.<tag key>
     prefix: <my_prefix>
   - key: defined_tags.<namespace>.<tag key>
     prefix: <my_prefix>

   groups:
     <group_name>: "'<tag_value>' == freeform_tags.<tag_key>"
     <group_name>: "'<tag_value>' == defined_tags.<namespace>.<tag_key>"
     <group_name>: "'<tag_key>' in defined_tags.<namespace>"

   # Example to create and modify a host variable
   compose:
     ansible_host: display_name+'.oracle.com'

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

Permissions
-----------

If the inventory list generated by the OCI inventory plugin does not
include every compute instance in your tenancy, review the following
information.

.. _user-permission-label:

User Permissions
~~~~~~~~~~~~~~~~

Ensure that the user has the following policy permissions. The user OCID
is specified using either the ``OCI_USER`` environment variable, or the
``profile`` section in your SDK and CLI configuration file.

To see a list of permissions for API operations, see `Details for the
Core
Services <https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Details_for_the_Core_Services>`_.

The inventory plugin makes API calls for the following operations:

-  ListCompartments
-  GetCompartment
-  ListVNICAttachments
-  GetVNIC
-  GetSubnet
-  GetVLAN
-  GetVCN
-  ListInstances
-  GetInstance
-  ListDBNodes
-  ListDBSystems
-  ListRegionSubscriptions

Troubleshooting Guides
----------------------
`Inventory Plugin Troubleshooting guides <http://oci-ansible-collection.readthedocs.io/en/latest/guides/troubleshooting-guide.html#inventory-plugin-errors>`_
