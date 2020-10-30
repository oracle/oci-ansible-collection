# Overview

This sample shows how to perform typical Identity and Access Management (IAM) tasks such as managing users, groups, policies through OCI ansible modules. 

The sample assumes the default user configured in the OCI configuration user is in the Administrator group or atleast has the required access for managing users, groups, policies. 
- Create a new group
- Create a policy 
- Create a user then add it to the group and policy
- Create user password
- Generate SSH keys and assign them to the user

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- sample_compartment_ocid
