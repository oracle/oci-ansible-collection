# Overview

This sample shows how you can enable local peering connection between two VCNs in the same region, using a [Local Peering Gateway] as discussed 
[here](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm) through OCI ansible cloud modules.

The sample
- Sets up a VCN with the Internet Gateway, the Local Peering Gateway, the subnet, the necessary security lists and the route rules.
- Sets up another VCN with the Local Peering Gateway, the subnet, the necessary security lists and the route rules.  
- Does the peering between both the Local Peering Gateways (LPGS).

# Instructions

The sample needs the following environment variables as pre-requisite. Assign values according to your tenancy

- SAMPLE_COMPARTMENT_OCID
- SAMPLE_AD_NAME 

Note: The sample, by default, sets up the topology, prints an information message
 and tears down the topology. If you want
to experiment with the topology after it is setup, comment out the invocation 
to `teardown.yaml` at the end of `sample.yaml`.
