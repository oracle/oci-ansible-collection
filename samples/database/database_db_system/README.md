# Overview

This sample shows how to create [Bare Metal and Virtual Machine DB Systems](https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Tasks/creatingDBsystem.htm). To explore more about
Oracle Cloud Infrastructure's Co-managed DB Systems, please visit
[here](https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Concepts/overview.htm).

The sample

- Sets up Virtual Machine DB System
- Get facts of specific DB System and lists available DB Homes
- Collects DB Node's VNIC information of a specified DB system
- Extracts Public and Private Ip of the DB Node from VNIC
- Creates backup from initial database
- Restore database from latest backup
- Creates new database from backup
- Updates database fields
- Lists all the databases available in specified DB Home and get facts of specific database

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI Ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:

- compartment_id
- availability_domain

Note: The sample, by default, sets up an Virtual Machine DB System, creates database in DB System, prints an information message,
runs a few tests to show that it is working, and tears down the DB System. If you want
to experiment with the DB System or Database after it is setup, comment out the invocation
to `teardown.yaml` at the end of `sample.yaml`.