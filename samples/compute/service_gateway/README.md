# Overview

This sample shows how you can enable private access to Object Storage from compute instances, using a [Service Gateway](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm) as discussed 
[here](https://blogs.oracle.com/cloud-infrastructure/connect-private-instances-with-oracle-services-through-an-oracle-cloud-infrastructure-service-gateway) through OCI ansible cloud modules.

The sample
- Sets up a user, group and policies required for managing buckets
- Creates necessary API keys for the user and uploads them
- Sets up the VCN, the NAT Gateway, the Internet Gateway, the public and private subnets, and the necessary security lists and route rules. A bastion instance is provisioned in the public subnet and a private instance is provisioned in the private subnet.
- Compute instance is provisioned in the private subnet and oci cli is installed and required config is setup via cloud init script.
- Disable NAT Gateway to restrict public access to private instance.
- A bucket is created from the private instance using oci cli.
- Verifies that the bucket is created.
- After the setup, the private instance would have private access to Object Storage.

<b>Note:</b> This sample creates and copies the keys needed by oci cli to the private instance. This is not secure and [Instance principals](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm) provide a better way of achieving the same. Currently instance principals does not work on a private instance. This is a known issue and will be fixed soon. This sample will be updated to use instance pricipals accordingly.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI 
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`:
- tenancy_ocid
- instance_ad
- instance_compartment
- instance_image
- namespace_name
- region
 
Note: The sample, by default, sets up the topology, prints an information message, 
runs a few tests to show it is working, and tears down the topology. If you want
to experiment with the topology after it is setup, comment out the invocation 
to `teardown.yaml` at the end of `sample.yaml`.
