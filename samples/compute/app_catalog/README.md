# Overview

This sample shows how a public compute instance can be [launched](https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/launchinginstance.htm) and [accessed](https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/accessinginstance.htm) from the internet using SSH, through OCI ansible cloud modules.

The sample 
- generates a temporary host-specific SSH key-pair
- specifies the public key from that key-pair to connect to the instance during instance launch and 
- demonstrates how the newly launched instance can be connected to using SSH.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- instance_ad (example value for US Ashburn - `IwGV:US-ASHBURN-AD-1`, example value for US Phoenix - `IwGV:US-PHOENIX-AD-1`)
- instance_compartment
