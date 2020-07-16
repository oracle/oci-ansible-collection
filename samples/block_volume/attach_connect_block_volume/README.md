# Overview

This sample shows how a block volume can be attached to a compute
instance with the iSCSI volume attachment type, and how it can be connected 
to from the compute instance using `iscsiadm`. 


This sample 
- generates a temporary host-specific SSH key-pair
- specifies the public key from that key-pair to connect to the instance during
  instance launch
- launches the instance
- creats a new block volume for that instance
- attaches the volume to the instance in order to expand the available
  storage of that instance, specifying iSCSI as the volume attachment type
- connect to the attached volume and mount the volume from the compute
  instance. This is achieved by executing `iscsiadm` commands over ssh
  on the compute instance. `iscsiadm` commands are run on the compute 
  instance using SSH using the `command` ansible module.
  The `iscsiadm` command invocations uses theinformation returned by the 
  `oci_compute_volume_attachment` to connect to the attached block storage volume.
  This information can also be obtained through `oci_compute_volume_attachment_facts`.
- asserts that the volume was connected to from the instance, and is mountable.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI 
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`:
- instance_ad
- instance_compartment
- instance_image  # provide an OL image
