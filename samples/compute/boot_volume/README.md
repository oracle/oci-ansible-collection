# Overview

This sample shows how a new boot volume can be created using existing compute instance. 


This sample 
- generates a temporary host-specific SSH key-pair
- specifies the public key from that key-pair to connect to the instance during
  instance launch
- launches the instance
- connects to instance using ssh
- fetches boot volume id from the instance
- creats a new boot volume from existing boot volume

# Instructions

The sample needs the following environment variables as pre-requisite. Assign values according to your tenancy
- SAMPLE_COMPARTMENT_OCID
- SAMPLE_IMAGE_OCID # provide an OL image
- SAMPLE_AD_NAME
