# Overview

This sample shows how to delete objects created within last X days from all the buckets in a namespace in Object Storage Service using OCI Ansible modules.
The sample can be modified to delete objects which are older than X days and this is helpful for organizations to control storage costs, by pruning old unnecessary objects stored in the OCI Object Storage Service.

The sample, for illustration, deletes objects created within last one day from all the buckets in the namespace.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI Ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:

- compartment_id
- namespace_name
