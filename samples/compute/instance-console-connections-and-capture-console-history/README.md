# Overview

This sample shows how a [serial and VNC console connection](https://docs.cloud.oracle.com/iaas/Content/Compute/References/serialconsole.htm) can be created for a compute instance, and how the serial console data can be captured and fetched from a compute instance.

The sample
- generates a temporary SSH key-pair for the Serial console connection
- demonstrates how an instance console connection can be created for a compute instance
- demonstrates how serial console data for a compute instance can be captured, and then retrieved to the local machine for debugging/troubleshotting issues.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI ansible cloud modules, please provide values (that are specific to your tenancy) for the following variables in the `vars` section of `sample.yaml`:
- instance_ad
- instance_compartment
- instance_image  # provide an OL image
