# Overview

This sample shows how one File System can be exported using two different export paths on two different Mount Targets. Also, how a single Mount Target can export paths from two 
different File Systems.
The sample 
- Generates all network related dependencies (e.g. VCN, subnets) and security list with configuration required by File System Service
- Generates required certificates required by instance
- Demonstrates the procedure to create File System Service components e.g. Mount Target, File System, Export and Snapshot
- Demonstrates the procedure of how one File System can be exported on two different Mount Targets
- Demonstrates the procedure of how a single Mount Target can export paths from two different File Systems.
- Demonstrates how to mount the File System through a compute instance

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- compartment_id
- tenancy_ocid
