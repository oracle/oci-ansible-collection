# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class HttpMonitorHelperCustom:
    def list_resources(self):
        existing_http_monitor_summary = to_dict(
            super(HttpMonitorHelperCustom, self).list_resources()
        )
        result = [
            oci_common_utils.call_with_backoff(
                self.client.get_http_monitor, monitor_id=http_monitor["id"]
            ).data
            for http_monitor in existing_http_monitor_summary
        ]
        return result


class PingMonitorHelperCustom:
    def list_resources(self):
        existing_ping_monitor_summary = to_dict(
            super(PingMonitorHelperCustom, self).list_resources()
        )
        result = [
            oci_common_utils.call_with_backoff(
                self.client.get_ping_monitor, monitor_id=ping_monitor["id"]
            ).data
            for ping_monitor in existing_ping_monitor_summary
        ]
        return result


class HttpProbeHelperCustom:
    def get_module_resource_id(self):
        return None

    def list_resources(self):
        return []


class PingProbeHelperCustom:
    def get_module_resource_id(self):
        return None

    def list_resources(self):
        return []
