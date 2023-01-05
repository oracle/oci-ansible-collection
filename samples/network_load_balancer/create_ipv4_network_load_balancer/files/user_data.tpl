#cloud-config

# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

runcmd:
  - sudo yum install -y yum-utils
  - sudo yum-config-manager --enable ol7_developer ol7_developer_epel
  - sudo yum clean all
  - sudo firewall-offline-cmd --zone=public --add-service=http
  - sudo systemctl restart firewalld
  - sudo yum install -y nginx
  - sudo systemctl start nginx
