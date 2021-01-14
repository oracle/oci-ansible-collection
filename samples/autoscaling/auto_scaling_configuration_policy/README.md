# Overview

This sample shows how you can create an auto scaling configuration policy to manage your instance pool 

The sample
- generates a temporary host-specific SSH key-pair
- specifies the public key from that key-pair to connect to the instance during instance launch
- create an instance configuration that defines the settings to use when creating Compute instances as part of an instance pool, including details such as the base image, shape, and metadata
- creates set of compute instance pools (based on the instance configuration) and launches instances 
- demonstrates how various auto scaling configuration (scheduled, threshold) can be added to instance pools  

# Instructions

The sample needs the following environment variables as pre-requisite. Assign values according to your tenancy
- SAMPLE_COMPARTMENT_OCID
- SAMPLE_IMAGE_OCID # provide an OL image
- SAMPLE_AD_NAME
