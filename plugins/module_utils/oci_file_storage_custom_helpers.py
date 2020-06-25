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


class MountTargetFactsHelperCustom:
    def list_resources(self):
        existing_mount_targets_summary = to_dict(
            super(MountTargetFactsHelperCustom, self).list_resources()
        )
        result = [
            oci_common_utils.call_with_backoff(
                self.client.get_mount_target, mount_target_id=mount_target["id"],
            ).data
            for mount_target in existing_mount_targets_summary
        ]
        return result


class MountTargetHelperCustom:
    def get_exclude_attributes(self):
        exclude_attributes = super(
            MountTargetHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "hostname_label",
            "ip_address",
        ]
