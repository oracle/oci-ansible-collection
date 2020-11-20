#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_ocvp_sddc_facts
short_description: Fetches details about one or multiple Sddc resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Sddc resources in Oracle Cloud Infrastructure
    - Lists the SDDCs in the specified compartment. The list can be
      filtered by display name or availability domain.
    - If I(sddc_id) is specified, the details of a single Sddc will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    sddc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SDDC.
            - Required to get a specific sddc.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple sddcs.
        type: str
    compute_availability_domain:
        description:
            - The name of the availability domain that the Compute instances are running in.
            - "Example: `Uocm:PHX-AD-1`"
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    lifecycle_state:
        description:
            - The lifecycle state of the resource.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List sddcs
  oci_ocvp_sddc_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific sddc
  oci_ocvp_sddc_facts:
    sddc_id: ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
sddcs:
    description:
        - List of Sddc resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SDDC.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compute_availability_domain:
            description:
                - The availability domain the ESXi hosts are running in.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        display_name:
            description:
                - A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits,
                  whitespaces, dashes and underscores.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        instance_display_name_prefix:
            description:
                - A prefix used in the name of each ESXi host and Compute instance in the SDDC.
                  If this isn't set, the SDDC's `displayName` is used as the prefix.
                - For example, if the value is `MySDDC`, the ESXi hosts are named `MySDDC-1`,
                  `MySDDC-2`, and so on.
            returned: on success
            type: string
            sample: instance_display_name_prefix_example
        vmware_software_version:
            description:
                - In general, this is a specific version of bundled VMware software supported by
                  Oracle Cloud VMware Solution (see
                  L(ListSupportedVmwareSoftwareVersions,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/SupportedVmwareSoftwareVersionSummary/
                  ListSupportedVmwareSoftwareVersions)).
                - "This attribute is not guaranteed to reflect the version of
                  software currently installed on the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the version of software that the Oracle
                  Cloud VMware Solution will install on any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer
                  version of bundled VMware software supported by the Oracle Cloud VMware Solution, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `vmwareSoftwareVersion` with that new version.
            returned: on success
            type: string
            sample: vmware_software_version_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that
                  contains the SDDC.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        esxi_hosts_count:
            description:
                - The number of ESXi hosts in the SDDC.
            returned: on success
            type: int
            sample: 56
        vcenter_fqdn:
            description:
                - FQDN for vCenter
                - "Example: `vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com`"
            returned: on success
            type: string
            sample: vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com
        nsx_manager_fqdn:
            description:
                - FQDN for NSX Manager
                - "Example: `nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`"
            returned: on success
            type: string
            sample: nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com
        vcenter_private_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PrivateIp` object that is
                  the virtual IP (VIP) for vCenter. For information about `PrivateIp` objects, see the
                  Core Services API.
            returned: on success
            type: string
            sample: ocid1.vcenterprivateip.oc1..xxxxxxEXAMPLExxxxxx
        nsx_manager_private_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PrivateIp` object that is
                  the virtual IP (VIP) for NSX Manager. For information about `PrivateIp` objects, see the
                  Core Services API.
            returned: on success
            type: string
            sample: ocid1.nsxmanagerprivateip.oc1..xxxxxxEXAMPLExxxxxx
        vcenter_initial_password:
            description:
                - The SDDC includes an administrator username and initial password for vCenter. Make sure
                  to change this initial vCenter password to a different value.
            returned: on success
            type: string
            sample: vcenter_initial_password_example
        nsx_manager_initial_password:
            description:
                - The SDDC includes an administrator username and initial password for NSX Manager. Make sure
                  to change this initial NSX Manager password to a different value.
            returned: on success
            type: string
            sample: nsx_manager_initial_password_example
        vcenter_username:
            description:
                - The SDDC includes an administrator username and initial password for vCenter. You can
                  change this initial username to a different value in vCenter.
            returned: on success
            type: string
            sample: vcenter_username_example
        nsx_manager_username:
            description:
                - The SDDC includes an administrator username and initial password for NSX Manager. You
                  can change this initial username to a different value in NSX Manager.
            returned: on success
            type: string
            sample: nsx_manager_username_example
        ssh_authorized_keys:
            description:
                - One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for
                  the default user on each ESXi host. Use a newline character to separate multiple keys.
                  The SSH keys must be in the format required for the `authorized_keys` file.
                - "This attribute is not guaranteed to reflect the public SSH keys
                  currently installed on the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the public SSH keys that Oracle
                  Cloud VMware Solution will install on any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you upgrade the existing ESXi hosts in the SDDC to use different
                  SSH keys, you should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update
                  the SDDC's `sshAuthorizedKeys` with the new public keys.
            returned: on success
            type: string
            sample: ssh_authorized_keys_example
        workload_network_cidr:
            description:
                - The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application
                  workloads.
            returned: on success
            type: string
            sample: workload_network_cidr_example
        nsx_overlay_segment_name:
            description:
                - The VMware NSX overlay workload segment to host your application. Connect to workload
                  portgroup in vCenter to access this overlay segment.
            returned: on success
            type: string
            sample: nsx_overlay_segment_name_example
        nsx_edge_uplink_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PrivateIp` object that is
                  the virtual IP (VIP) for the NSX Edge Uplink. Use this OCID as the route target for
                  route table rules when setting up connectivity between the SDDC and other networks.
                  For information about `PrivateIp` objects, see the Core Services API.
            returned: on success
            type: string
            sample: ocid1.nsxedgeuplinkip.oc1..xxxxxxEXAMPLExxxxxx
        provisioning_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management subnet used
                  to provision the SDDC.
            returned: on success
            type: string
            sample: ocid1.provisioningsubnet.oc1..xxxxxxEXAMPLExxxxxx
        vsphere_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the vSphere component of the VMware environment.
                - "This attribute is not guaranteed to reflect the vSphere VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the vSphere VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the vSphere component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `vsphereVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx
        vmotion_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the vMotion component of the VMware environment.
                - "This attribute is not guaranteed to reflect the vMotion VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the vMotion VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the vMotion component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `vmotionVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx
        vsan_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the vSAN component of the VMware environment.
                - "This attribute is not guaranteed to reflect the vSAN VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the vSAN VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the vSAN component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `vsanVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx
        nsx_v_tep_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the NSX VTEP component of the VMware environment.
                - "This attribute is not guaranteed to reflect the NSX VTEP VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the NSX VTEP VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the NSX VTEP component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `nsxVTepVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx
        nsx_edge_v_tep_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the NSX Edge VTEP component of the VMware environment.
                - "This attribute is not guaranteed to reflect the NSX Edge VTEP VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the NSX Edge VTEP VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the NSX Edge VTEP component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `nsxEdgeVTepVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx
        nsx_edge_uplink1_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the NSX Edge Uplink 1 component of the VMware environment.
                - "This attribute is not guaranteed to reflect the NSX Edge Uplink 1 VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the NSX Edge Uplink 1 VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the NSX Edge Uplink 1 component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `nsxEdgeUplink1VlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx
        nsx_edge_uplink2_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the NSX Edge Uplink 2 component of the VMware environment.
                - "This attribute is not guaranteed to reflect the NSX Edge Uplink 2 VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the NSX Edge Uplink 2 VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the NSX Edge Uplink 2 component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `nsxEdgeUplink2VlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx
        hcx_private_ip_id:
            description:
                - HCX Private IP
            returned: on success
            type: string
            sample: ocid1.hcxprivateip.oc1..xxxxxxEXAMPLExxxxxx
        hcx_fqdn:
            description:
                - HCX Fully Qualified Domain Name
            returned: on success
            type: string
            sample: hcx_fqdn_example
        hcx_initial_password:
            description:
                - HCX initial password
            returned: on success
            type: string
            sample: hcx_initial_password_example
        hcx_vlan_id:
            description:
                - HCX vlan id
            returned: on success
            type: string
            sample: ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx
        is_hcx_enabled:
            description:
                - HCX enabled or not
            returned: on success
            type: bool
            sample: true
        hcx_on_prem_key:
            description:
                - HCX on-premise license key
            returned: on success
            type: string
            sample: hcx_on_prem_key_example
        time_created:
            description:
                - The date and time the SDDC was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_updated:
            description:
                - The date and time the SDDC was updated, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the SDDC.
            returned: on success
            type: string
            sample: CREATING
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        items:
            description:
                - A list of SDDCs.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that
                          contains the SDDC.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                compute_availability_domain:
                    description:
                        - The availability domain that the SDDC's ESXi hosts are running in.
                    returned: on success
                    type: string
                    sample: compute_availability_domain_example
                display_name:
                    description:
                        - A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits,
                          whitespaces, dashes and underscores.
                          Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                vmware_software_version:
                    description:
                        - In general, this is a specific version of bundled VMware software supported by
                          Oracle Cloud VMware Solution (see
                          L(ListSupportedVmwareSoftwareVersions,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/ocvs/20200501/SupportedVmwareSoftwareVersionSummary/
                          ListSupportedVmwareSoftwareVersions)).
                        - "This attribute is not guaranteed to reflect the version of
                          software currently installed on the ESXi hosts in the SDDC. The purpose
                          of this attribute is to show the version of software that the Oracle
                          Cloud VMware Solution will install on any new ESXi hosts that you *add to this
                          SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/EsxiHost/CreateEsxiHost)."
                        - Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer
                          version of bundled VMware software supported by the Oracle Cloud VMware Solution, you
                          should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/ocvs/20200501/Sddc/UpdateSddc) to update the SDDC's
                          `vmwareSoftwareVersion` with that new version.
                    returned: on success
                    type: string
                    sample: vmware_software_version_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that
                          contains the SDDC.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                esxi_hosts_count:
                    description:
                        - The number of ESXi hosts in the SDDC.
                    returned: on success
                    type: int
                    sample: 56
                hcx_fqdn:
                    description:
                        - HCX Fully Qualified Domain Name
                    returned: on success
                    type: string
                    sample: hcx_fqdn_example
                is_hcx_enabled:
                    description:
                        - HCX enabled or not
                    returned: on success
                    type: bool
                    sample: true
                vcenter_fqdn:
                    description:
                        - FQDN for vCenter
                        - "Example: `vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com`"
                    returned: on success
                    type: string
                    sample: vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com
                nsx_manager_fqdn:
                    description:
                        - FQDN for NSX Manager
                        - "Example: `nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`"
                    returned: on success
                    type: string
                    sample: nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com
                time_created:
                    description:
                        - The date and time the SDDC was created, in the format defined by
                          L(RFC3339,https://tools.ietf.org/html/rfc3339).
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                time_updated:
                    description:
                        - The date and time the SDDC was updated, in the format defined by
                          L(RFC3339,https://tools.ietf.org/html/rfc3339).
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                lifecycle_state:
                    description:
                        - The current state of the SDDC.
                    returned: on success
                    type: string
                    sample: CREATING
                freeform_tags:
                    description:
                        - Free-form tags for this resource. Each tag is a simple key-value pair with no
                          predefined name, type, or namespace. For more information, see L(Resource
                          Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                        - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - Defined tags for this resource. Each key is predefined and scoped to a
                          namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                        - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_availability_domain": "Uocm:PHX-AD-1",
        "display_name": "display_name_example",
        "instance_display_name_prefix": "instance_display_name_prefix_example",
        "vmware_software_version": "vmware_software_version_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "esxi_hosts_count": 56,
        "vcenter_fqdn": "vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com",
        "nsx_manager_fqdn": "nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com",
        "vcenter_private_ip_id": "ocid1.vcenterprivateip.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_manager_private_ip_id": "ocid1.nsxmanagerprivateip.oc1..xxxxxxEXAMPLExxxxxx",
        "vcenter_initial_password": "vcenter_initial_password_example",
        "nsx_manager_initial_password": "nsx_manager_initial_password_example",
        "vcenter_username": "vcenter_username_example",
        "nsx_manager_username": "nsx_manager_username_example",
        "ssh_authorized_keys": "ssh_authorized_keys_example",
        "workload_network_cidr": "workload_network_cidr_example",
        "nsx_overlay_segment_name": "nsx_overlay_segment_name_example",
        "nsx_edge_uplink_ip_id": "ocid1.nsxedgeuplinkip.oc1..xxxxxxEXAMPLExxxxxx",
        "provisioning_subnet_id": "ocid1.provisioningsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "vsphere_vlan_id": "ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx",
        "vmotion_vlan_id": "ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "vsan_vlan_id": "ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_v_tep_vlan_id": "ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_edge_v_tep_vlan_id": "ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_edge_uplink1_vlan_id": "ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_edge_uplink2_vlan_id": "ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "hcx_private_ip_id": "ocid1.hcxprivateip.oc1..xxxxxxEXAMPLExxxxxx",
        "hcx_fqdn": "hcx_fqdn_example",
        "hcx_initial_password": "hcx_initial_password_example",
        "hcx_vlan_id": "ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "is_hcx_enabled": true,
        "hcx_on_prem_key": "hcx_on_prem_key_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "items": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "compute_availability_domain": "compute_availability_domain_example",
            "display_name": "display_name_example",
            "vmware_software_version": "vmware_software_version_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "esxi_hosts_count": 56,
            "hcx_fqdn": "hcx_fqdn_example",
            "is_hcx_enabled": true,
            "vcenter_fqdn": "vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com",
            "nsx_manager_fqdn": "nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com",
            "time_created": "2016-08-25T21:10:29.600Z",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.ocvp import SddcClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SddcFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "sddc_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sddc, sddc_id=self.module.params.get("sddc_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compute_availability_domain",
            "display_name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sddcs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SddcFactsHelperCustom = get_custom_class("SddcFactsHelperCustom")


class ResourceFactsHelper(SddcFactsHelperCustom, SddcFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            sddc_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compute_availability_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sddc",
        service_client_class=SddcClient,
        namespace="ocvp",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sddcs=result)


if __name__ == "__main__":
    main()
