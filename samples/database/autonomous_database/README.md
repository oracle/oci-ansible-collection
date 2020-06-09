# Overview

This sample shows how to create an [Autonomous Transaction Processing Database](https://www.oracle.com/database/autonomous-transaction-processing.html). To explore more about
Oracle Cloud Infrastructure's Autonomous Transaction Processing Cloud Service, please visit
[here](https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Concepts/adboverview.htm).

The sample

- sets up an Autonomous Transaction Processing Database.
- List all the Autonomous Transaction Processing Databases available in the compartment filtered by display name.
- Get facts of a specific database.
- Stops and starts an Autonomous Transaction Processing Database.
- Deletes an Autonomous Transaction Processing Database.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`:

- compartment_ocid
- cpu_core_count
- display_name
- admin_password
- db_name
- data_storage_size_in_tbs
- license_model

Note: The sample, by default, sets up an Autonomous Transaction Processing Database, prints an information message,
runs a few tests to show that it is working, and tears down the Autonomous Transaction Processing Database. If you want
to experiment with the Autonomous Transaction Processing Database after it is setup, comment out the invocation
to `teardown.yaml` at the end of `sample.yaml`.
