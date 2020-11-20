# Overview

This sample shows how a File System can be created and accessed through compute instances, through OCI ansible cloud modules.

The sample
- Generates all network related dependencies (e.g. VCN, subnets) and security list with configuration required by File System Service
- Generates required certificates required by instances
- Demonstrates the procedure to create File System Service components e.g. Mount Target, File System, Export and Snapshot
- Demonstrates how to mount the File System through a compute instance and how to access the contents through another compute instance

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- compartment_id
- tenancy_ocid