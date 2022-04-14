# Overview

This sample shows how to create an [Autonomous Transaction Processing Database on Dedicated Infrastructure] (https://www.oracle.com/database/autonomous-transaction-processing.html). To explore more about
Oracle Cloud Infrastructure's Autonomous Transaction Processing Cloud Service, please visit
[here](https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Concepts/adboverview.htm).

The sample

- sets up an Autonomous Container (ACD) Database.
- sets up an Autonomous Transaction Processing (ATP) Database (ADB).
- List the Autonomous Transaction Processing Databases available in the compartment filtered by display name.
- Get facts of the ATP database created earlier.
- Stops and starts an ATP Database created earlier.
- Deletes the ADB created earlier.
- Deletes the ACD created earlier after waiting for backup to complete.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`:

- SAMPLE_COMPARTMENT_OCID
- SAMPLE_OCPU_COUNT
- SAMPLE_ADB_DISPLAY_NAME
- SAMPLE_DB_NAME
- SAMPLE_ADMIN_PASSWORD
- SAMPLE_DATA_STORAGE_SIZE_IN_GBS
- SAMPLE_IS_DEDICATED
- SAMPLE_CLOUD_AUTONOMOUS_VM_CLUSTER_ID
- SAMPLE_ACD_DISPLAY_NAME


Note: The sample, by default, sets up an Autonomous Transaction Processing Database, prints an information message,
runs a few tests to show that it is working and tears down the Autonomous Transaction Processing Database. If you want
to experiment with the Autonomous Transaction Processing Database after it is setup, comment out the invocation
to `teardown.yaml` at the end of `sample.yaml`.