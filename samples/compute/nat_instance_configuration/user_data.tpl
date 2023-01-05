#cloud-config

# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

write_files:
  # Create file to be used when enabling ip forwarding
  - path: /etc/sysctl.d/98-ip-forward.conf
    content: |
      net.ipv4.ip_forward = 1

runcmd:
  # Run firewall commands to enable masquerading and port forwarding
  # Enable ip forwarding by setting sysctl kernel parameter
  - firewall-offline-cmd --direct --add-rule ipv4 nat POSTROUTING 0 -o ens3 -j MASQUERADE
  - firewall-offline-cmd --direct --add-rule ipv4 filter FORWARD 0 -i ens3 -j ACCEPT
  - /bin/systemctl restart firewalld
  - sysctl -p /etc/sysctl.d/98-ip-forward.conf
