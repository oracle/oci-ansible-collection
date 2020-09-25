# Overview

This sample shows how you can enable internet access from compute instances in 
a private subnet, using a [NAT Gateway](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm) in a public subnet as discussed 
[here](https://blogs.oracle.com/cloud-infrastructure/access-resources-on-the-public-internet-through-an-oracle-cloud-infrastructure-nat-gateway-v2) through OCI ansible cloud modules.

The sample 
- sets up the VCN, the NAT Gateway, the Internet Gateway, the public and private subnets, and the necessary security lists and route rules. A bastion instance is provisioned in the public subnet and a private instance is provisioned in the private subnet.
- After the setup, the private instance would have outbound internet access
through the NAT Gateway and accessible via ssh from bastion instance.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI 
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`: 
- instance_ad
- instance_compartment
- instance_image
 
Note: The sample, by default, sets up the topology, prints an information message, 
runs a few tests to show it is working, and tears down the topology. If you want
to experiment with the topology after it is setup, comment out the invocation 
to `teardown.yaml` at the end of `sample.yaml`.
