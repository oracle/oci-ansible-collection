# Overview

This sample shows how you can simplify management of your Compute instances using resources such as instance configurations and instance pools, using OCI ansible modules. Instance pools give you the ability to provision and create multiple Compute instances based off of the same instance configuration, within the same region. 

The sample
- generates a temporary host-specific SSH key-pair
- specifies the public key from that key-pair to connect to the instance during instance launch
- create an instance configuration that defines the settings to use when creating Compute instances as part of an instance pool, including details such as the base image, shape, and metadata
- demonstrates how a set of compute instances (based on the instance configuration) can be launched using Instance Pools
- connects to one of the compute instances using SSH

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- instance_ad
- instance_compartment
- instance_image  # provide an OL image
