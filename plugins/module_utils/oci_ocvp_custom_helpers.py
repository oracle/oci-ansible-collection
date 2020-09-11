# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_config_utils

try:
    from oci.ocvp import WorkRequestClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SddcHelperCustom:
    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    # As per console, a SDDC creation could take up to 3 hours but from the tests I see that it takes around 4 hours.
    # 4 hours is very long for the ansible module to wait but the other option would be to fallback to the default time
    # which would result in error for a user every time. So they will have to use wait: False option and do the waiting
    # themselves every time. But this way users who do need to wait until completion need no changes and for someone
    # not bothered about completion can just use wait: False flag.
    def get_default_module_wait_timeout(self):
        return int(4 * 3600)


class EsxiHostHelperCustom:
    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_default_module_wait_timeout(self):
        return int(1 * 3600)
