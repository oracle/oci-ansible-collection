# Overview

This sample shows how a public compute instance can be [launched](https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/launchinginstance.htm) and [accessed](https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/accessinginstance.htm) from the internet using SSH, through OCI ansible cloud modules.

The sample 
- generates a temporary host-specific SSH key-pair
- specifies the public key from that key-pair to connect to the instance during instance launch and 
- demonstrates how the newly launched instance can be connected to using SSH.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- instance_ad
- instance_compartment
- instance_image  # provide an OL image

Additionally, you can set the `SAMPLE_PUBLIC_SSH_KEY` env variable  
to set the public ssh key for the compute instance.  
For example:
> export SAMPLE_PUBLIC_SSH_KEY="ssh-rsa AAA.................................xyz"

This must be the default ssh key on your system.  
You can run the following command to set the environment variable:
> export SAMPLE_PUBLIC_SSH_KEY=\`cat ~/.ssh/id_rsa.pub\`


If this is not set, the sample will generate a new key-pair every run anyway.
