# Overview

This sample creates a cluster with Oracle Cloud Infrastructure Container Engine for
Kubernetes(OKE).

This sample:
- creates a configured VCN and related resources required for setting up an OKE cluster
- creates a cluster
- creates a node pool
- downloads the kubeconfig file for the cluster

# Pre-requisites
This sample requires [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) to be
installed and setup locally.

# Instructions

To run the sample, after ensuring that you have the pre-requisites for OCI 
ansible cloud modules, please provide values (that are specific to your tenancy)
for the following variables in the `vars` section of `sample.yaml`:
- ad1: Name of the first availability domain.
- ad2: Name of the second availability domain.
- ad3: Name of the third availability domain.
- cluster_compartment: OCID of the compartment in which you want to create OKE cluster.
- kubeconfig_path: Path to download the kubeconfig for the created cluster.
