#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_file_storage_mount_target
short_description: Manage a MountTarget resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a MountTarget resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new mount target in the specified compartment and
      subnet. You can associate a file system with a mount
      target only when they exist in the same availability domain. Instances
      can connect to mount targets in another availablity domain, but
      you might see higher latency than with instances in the same
      availability domain as the mount target.
    - Mount targets have one or more private IP addresses that you can
      provide as the host portion of remote target parameters in
      client mount commands. These private IP addresses are listed
      in the privateIpIds property of the mount target and are highly available. Mount
      targets also consume additional IP addresses in their subnet.
      Do not use /30 or smaller subnets for mount target creation because they
      do not have sufficient available IP addresses.
      Allow at least three IP addresses for each mount target.
    - For information about access control and compartments, see
      L(Overview of the IAM
      Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
    - For information about availability domains, see L(Regions and
      Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm).
      To get a list of availability domains, use the
      `ListAvailabilityDomains` operation in the Identity and Access
      Management Service API.
    - All Oracle Cloud Infrastructure Services resources, including
      mount targets, get an Oracle-assigned, unique ID called an
      Oracle Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
      When you create a resource, you can find its OCID in the response.
      You can also retrieve a resource's OCID by using a List API operation on that resource
      type, or by viewing the resource in the Console.
    - "This resource has the following action operations in the M(oracle.oci.oci_file_storage_mount_target_actions) module: change_compartment,
      validate_key_tabs."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain in which to create the mount target.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to create the mount target.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    hostname_label:
        description:
            - The hostname for the mount target's IP address, used for
              DNS resolution. The value is the hostname portion of the private IP
              address's fully qualified domain name (FQDN). For example,
              `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`.
              Must be unique across all VNICs in the subnet and comply
              with L(RFC 952,https://tools.ietf.org/html/rfc952)
              and L(RFC 1123,https://tools.ietf.org/html/rfc1123).
            - "Note: This attribute value is stored in the L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/) resource,
              not in the `mountTarget` resource.
              To update the `hostnameLabel`, use `GetMountTarget` to obtain the
              L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the mount target's
              private IPs (`privateIpIds`). Then, you can use
              L(UpdatePrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/UpdatePrivateIp)
              to update the `hostnameLabel` value."
            - For more information, see
              L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm).
            - "Example: `files-1`"
        type: str
    ip_address:
        description:
            - A private IP address of your choice. Must be an available IP address within
              the subnet's CIDR. If you don't specify a value, Oracle automatically
              assigns a private IP address from the subnet.
            - "Note: This attribute value is stored in the L(PrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/) resource,
              not in the `mountTarget` resource.
              To update the `ipAddress`, use `GetMountTarget` to obtain the
              L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the mount target's
              private IPs (`privateIpIds`). Then, you can use
              L(UpdatePrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/UpdatePrivateIp)
              to update the `ipAddress` value."
            - "Example: `10.0.3.3`"
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet in which to create the mount target.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - "Example: `My mount target`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    idmap_type:
        description:
            - The method used to map a Unix UID to secondary groups, if any.
            - This parameter is updatable.
        type: str
    ldap_idmap:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            schema_type:
                description:
                    - Schema type of the LDAP account.
                    - This parameter is updatable.
                type: str
                choices:
                    - "RFC2307"
            cache_refresh_interval_seconds:
                description:
                    - The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry.
                    - This parameter is updatable.
                type: int
            cache_lifetime_seconds:
                description:
                    - The maximum amount of time the mount target is allowed to use a cached entry.
                    - This parameter is updatable.
                type: int
            negative_cache_lifetime_seconds:
                description:
                    - The amount of time that a mount target will maintain information that a user is not found in the ID mapping configuration.
                    - This parameter is updatable.
                type: int
            user_search_base:
                description:
                    - All LDAP searches are recursive starting at this user.
                    - "Example: `CN=User,DC=domain,DC=com`"
                    - This parameter is updatable.
                type: str
            group_search_base:
                description:
                    - All LDAP searches are recursive starting at this group.
                    - "Example: `CN=Group,DC=domain,DC=com`"
                    - This parameter is updatable.
                type: str
            outbound_connector1_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the first connector to use to communicate with the
                      LDAP server.
                    - This parameter is updatable.
                type: str
            outbound_connector2_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the second connector to use to communicate with the
                      LDAP server.
                    - This parameter is updatable.
                type: str
    nsg_ids:
        description:
            - A list of Network Security Group L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated with this mount
              target.
              A maximum of 5 is allowed.
              Setting this to an empty array after the list is created removes the mount target from all NSGs.
              For more information about NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
            - This parameter is updatable.
        type: list
        elements: str
    kerberos:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            kerberos_realm:
                description:
                    - The Kerberos realm that the mount target will join.
                    - This parameter is updatable.
                type: str
            key_tab_secret_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the keytab Secret in the Vault.
                    - This parameter is updatable.
                type: str
            current_key_tab_secret_version:
                description:
                    - Version of the keytab Secret in the Vault to use.
                    - This parameter is updatable.
                type: int
            backup_key_tab_secret_version:
                description:
                    - Version of the keytab Secret in the Vault to use as a backup.
                    - This parameter is updatable.
                type: int
            is_kerberos_enabled:
                description:
                    - Specifies whether to enable or disable Kerberos.
                    - This parameter is updatable.
                type: bool
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair
               with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    mount_target_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the mount target.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the MountTarget.
            - Use I(state=present) to create or update a MountTarget.
            - Use I(state=absent) to delete a MountTarget.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create mount_target
  oci_file_storage_mount_target:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    hostname_label: hostname_label_example
    ip_address: ip_address_example
    display_name: display_name_example
    idmap_type: idmap_type_example
    ldap_idmap:
      # optional
      schema_type: RFC2307
      cache_refresh_interval_seconds: 56
      cache_lifetime_seconds: 56
      negative_cache_lifetime_seconds: 56
      user_search_base: user_search_base_example
      group_search_base: group_search_base_example
      outbound_connector1_id: "ocid1.outboundconnector1.oc1..xxxxxxEXAMPLExxxxxx"
      outbound_connector2_id: "ocid1.outboundconnector2.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    kerberos:
      # optional
      kerberos_realm: kerberos_realm_example
      key_tab_secret_id: "ocid1.keytabsecret.oc1..xxxxxxEXAMPLExxxxxx"
      current_key_tab_secret_version: 56
      backup_key_tab_secret_version: 56
      is_kerberos_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update mount_target
  oci_file_storage_mount_target:
    # required
    mount_target_id: "ocid1.mounttarget.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    idmap_type: idmap_type_example
    ldap_idmap:
      # optional
      schema_type: RFC2307
      cache_refresh_interval_seconds: 56
      cache_lifetime_seconds: 56
      negative_cache_lifetime_seconds: 56
      user_search_base: user_search_base_example
      group_search_base: group_search_base_example
      outbound_connector1_id: "ocid1.outboundconnector1.oc1..xxxxxxEXAMPLExxxxxx"
      outbound_connector2_id: "ocid1.outboundconnector2.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    kerberos:
      # optional
      kerberos_realm: kerberos_realm_example
      key_tab_secret_id: "ocid1.keytabsecret.oc1..xxxxxxEXAMPLExxxxxx"
      current_key_tab_secret_version: 56
      backup_key_tab_secret_version: 56
      is_kerberos_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update mount_target using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_mount_target:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    idmap_type: idmap_type_example
    ldap_idmap:
      # optional
      schema_type: RFC2307
      cache_refresh_interval_seconds: 56
      cache_lifetime_seconds: 56
      negative_cache_lifetime_seconds: 56
      user_search_base: user_search_base_example
      group_search_base: group_search_base_example
      outbound_connector1_id: "ocid1.outboundconnector1.oc1..xxxxxxEXAMPLExxxxxx"
      outbound_connector2_id: "ocid1.outboundconnector2.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    kerberos:
      # optional
      kerberos_realm: kerberos_realm_example
      key_tab_secret_id: "ocid1.keytabsecret.oc1..xxxxxxEXAMPLExxxxxx"
      current_key_tab_secret_version: 56
      backup_key_tab_secret_version: 56
      is_kerberos_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete mount_target
  oci_file_storage_mount_target:
    # required
    mount_target_id: "ocid1.mounttarget.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete mount_target using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_mount_target:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
mount_target:
    description:
        - Details of the MountTarget resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the mount target is in. May be unset
                  as a blank or NULL value.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the mount target.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My mount target`"
            returned: on success
            type: str
            sample: display_name_example
        export_set_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated export set. Controls what file
                  systems will be exported through Network File System (NFS) protocol on this
                  mount target.
            returned: on success
            type: str
            sample: "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the mount target.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_details:
            description:
                - Additional information about the current 'lifecycleState'.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the mount target.
            returned: on success
            type: str
            sample: CREATING
        private_ip_ids:
            description:
                - The OCIDs of the private IP addresses associated with this mount target.
            returned: on success
            type: list
            sample: []
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the mount target is in.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        idmap_type:
            description:
                - The method used to map a Unix UID to secondary groups. If NONE, the mount target will not use the Unix UID for ID mapping.
            returned: on success
            type: str
            sample: LDAP
        ldap_idmap:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                schema_type:
                    description:
                        - Schema type of the LDAP account.
                    returned: on success
                    type: str
                    sample: RFC2307
                cache_refresh_interval_seconds:
                    description:
                        - The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry.
                    returned: on success
                    type: int
                    sample: 56
                cache_lifetime_seconds:
                    description:
                        - The maximum amount of time the mount target is allowed to use a cached entry.
                    returned: on success
                    type: int
                    sample: 56
                negative_cache_lifetime_seconds:
                    description:
                        - The amount of time that a mount target will maintain information that a user is not found in the ID mapping configuration.
                    returned: on success
                    type: int
                    sample: 56
                user_search_base:
                    description:
                        - All LDAP searches are recursive starting at this user.
                        - "Example: `CN=User,DC=domain,DC=com`"
                    returned: on success
                    type: str
                    sample: user_search_base_example
                group_search_base:
                    description:
                        - All LDAP searches are recursive starting at this group.
                        - "Example: `CN=Group,DC=domain,DC=com`"
                    returned: on success
                    type: str
                    sample: group_search_base_example
                outbound_connector1_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the first connector to use to communicate with
                          the LDAP server.
                    returned: on success
                    type: str
                    sample: "ocid1.outboundconnector1.oc1..xxxxxxEXAMPLExxxxxx"
                outbound_connector2_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the second connector to use to communicate with
                          the LDAP server.
                    returned: on success
                    type: str
                    sample: "ocid1.outboundconnector2.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - A list of Network Security Group L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated with this mount
                  target.
                  A maximum of 5 is allowed.
                  Setting this to an empty array after the list is created removes the mount target from all NSGs.
                  For more information about NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
            returned: on success
            type: list
            sample: []
        kerberos:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                kerberos_realm:
                    description:
                        - The Kerberos realm that the mount target will join.
                    returned: on success
                    type: str
                    sample: kerberos_realm_example
                key_tab_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the keytab secret in the Vault.
                    returned: on success
                    type: str
                    sample: "ocid1.keytabsecret.oc1..xxxxxxEXAMPLExxxxxx"
                current_key_tab_secret_version:
                    description:
                        - Version of the keytab secret in the Vault to use.
                    returned: on success
                    type: int
                    sample: 56
                backup_key_tab_secret_version:
                    description:
                        - Version of the keytab secert in the Vault to use as a backup.
                    returned: on success
                    type: int
                    sample: 56
                is_kerberos_enabled:
                    description:
                        - Specifies whether to enable or disable Kerberos.
                    returned: on success
                    type: bool
                    sample: true
        time_created:
            description:
                - The date and time the mount target was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "export_set_id": "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "CREATING",
        "private_ip_ids": [],
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "idmap_type": "LDAP",
        "ldap_idmap": {
            "schema_type": "RFC2307",
            "cache_refresh_interval_seconds": 56,
            "cache_lifetime_seconds": 56,
            "negative_cache_lifetime_seconds": 56,
            "user_search_base": "user_search_base_example",
            "group_search_base": "group_search_base_example",
            "outbound_connector1_id": "ocid1.outboundconnector1.oc1..xxxxxxEXAMPLExxxxxx",
            "outbound_connector2_id": "ocid1.outboundconnector2.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "nsg_ids": [],
        "kerberos": {
            "kerberos_realm": "kerberos_realm_example",
            "key_tab_secret_id": "ocid1.keytabsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "current_key_tab_secret_version": 56,
            "backup_key_tab_secret_version": 56,
            "is_kerberos_enabled": true
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import CreateMountTargetDetails
    from oci.file_storage.models import UpdateMountTargetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MountTargetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MountTargetHelperGen, self).get_possible_entity_types() + [
            "mounttarget",
            "mounttargets",
            "fileStoragemounttarget",
            "fileStoragemounttargets",
            "mounttargetresource",
            "mounttargetsresource",
            "filestorage",
        ]

    def get_module_resource_id_param(self):
        return "mount_target_id"

    def get_module_resource_id(self):
        return self.module.params.get("mount_target_id")

    def get_get_fn(self):
        return self.client.get_mount_target

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_mount_target, mount_target_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_mount_target,
            mount_target_id=self.module.params.get("mount_target_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "availability_domain",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_mount_targets, **kwargs
        )

    def get_create_model_class(self):
        return CreateMountTargetDetails

    def get_exclude_attributes(self):
        return ["ip_address", "hostname_label"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_mount_target,
            call_fn_args=(),
            call_fn_kwargs=dict(create_mount_target_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateMountTargetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_mount_target,
            call_fn_args=(),
            call_fn_kwargs=dict(
                mount_target_id=self.module.params.get("mount_target_id"),
                update_mount_target_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_mount_target,
            call_fn_args=(),
            call_fn_kwargs=dict(
                mount_target_id=self.module.params.get("mount_target_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MountTargetHelperCustom = get_custom_class("MountTargetHelperCustom")


class ResourceHelper(MountTargetHelperCustom, MountTargetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            hostname_label=dict(type="str"),
            ip_address=dict(type="str"),
            subnet_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            idmap_type=dict(type="str"),
            ldap_idmap=dict(
                type="dict",
                options=dict(
                    schema_type=dict(type="str", choices=["RFC2307"]),
                    cache_refresh_interval_seconds=dict(type="int"),
                    cache_lifetime_seconds=dict(type="int"),
                    negative_cache_lifetime_seconds=dict(type="int"),
                    user_search_base=dict(type="str"),
                    group_search_base=dict(type="str"),
                    outbound_connector1_id=dict(type="str"),
                    outbound_connector2_id=dict(type="str"),
                ),
            ),
            nsg_ids=dict(type="list", elements="str"),
            kerberos=dict(
                type="dict",
                options=dict(
                    kerberos_realm=dict(type="str"),
                    key_tab_secret_id=dict(type="str"),
                    current_key_tab_secret_version=dict(type="int", no_log=True),
                    backup_key_tab_secret_version=dict(type="int", no_log=True),
                    is_kerberos_enabled=dict(type="bool"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            mount_target_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="mount_target",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
