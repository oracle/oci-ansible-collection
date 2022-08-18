# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_config_utils

try:
    import oci

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpensearchClusterBackupHelperCustom:
    def get_waiter_client(self):
        # cluster_backup resource has a separate client but still uses OpensearchClusterClient for work request.
        return oci_config_utils.create_service_client(
            self.module, oci.opensearch.OpensearchClusterClient
        )
