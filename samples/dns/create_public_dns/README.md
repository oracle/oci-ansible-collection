# Overview

This sample shows how to create Public DNS zone and attach Steering Policy to it.

The sample
- Creates Public DNS zone
- Creates Steering Policy of type `CUSTOM`
- Attaches steering policy to zone to serve intelligent responses to DNS queries. 

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- compartment_id
