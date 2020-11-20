# Overview

This sample shows how a public load balancer  instance can be created, through OCI ansible cloud modules.

The sample 
- generates all network related dependencies (e.g. VCN, subnets)
- Generates required certificates required by load balancer 
- demonstrates the procedure to create public load balancer using ansible playbook.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- compartment_id
- tenancy_ocid
