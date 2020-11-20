# Overview

This sample shows how to provision a virtual cloud network (VCN) with two private subnets in different availability
domains and an IPSec VPN(using a dynamic routing gateway, a customer premises equipment and an IPSec connection). It
provisions resources illustrated in this [networking scenario]
(https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/scenariob.htm).

The sample provisions following resources:
- a VCN
- two private subnets
- a dynamic routing gateway(DRG)
- a customer premises equipment(CPE)
- an IPSec connection between DRG & CPE
Finally, it retrieves IPSec connection configuration information & status.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI
Ansible cloud modules, please provide values (that are specific to your tenancy and on-premise network):
for the following variables in the `vars` section of `sample.yaml`:
- ad1: Name of availability domain 1
- ad2: Name of availability domain 2
- sample_compartment: OCID of the compartment
- tenancy_ocid: OCID of the tenancy
