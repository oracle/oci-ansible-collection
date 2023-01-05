#cloud-config

# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

write_files:

  # Create .oci directory
  # - path: /home/opc/.oci/
  #   owner: opc:opc
  #   permissions: "0600"

  # Copy the api private key
  - path: /root/oci_api_key.pem
    encoding: b64
    owner: root:root
    permissions: "0600"
    content: |
      "{{ api_private_key_contents | b64encode }}"

  # Create config file for oci cli
  - path: /root/config
    owner: root:root
    permissions: "0600"
    content: |
      [DEFAULT]
      tenancy={{ tenancy_ocid }}
      user={{ test_user_id }}
      key_file=/home/opc/.oci/oci_api_key.pem
      fingerprint={{ api_signing_key_fingerprint }}
      region={{ region }}
      pass_phrase={{ api_key_passphrase }}

runcmd:
  # create .oci directory
  - mkdir -p /home/opc/.oci/
  # copy the config and private key files to .oci directory
  - mv /root/oci_api_key.pem /home/opc/.oci/
  - mv /root/config /home/opc/.oci/
  # change the permissions and ownership
  - chown -R opc:opc /home/opc/.oci/
  - chmod -R 700 /home/opc/.oci/
  - chmod 600 /home/opc/.oci/*
  # Install oci cli
  - yum install -y yum-utils
  - yum-config-manager --enable ol7_developer ol7_developer_epel
  - yum clean all
  - yum install -y python-oci-sdk python-oci-cli
