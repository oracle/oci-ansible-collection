# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewaySdkHelperCustom:
    # update_resource has NoneWaiter but the sdk returns None response in that case
    # so explicitly calling get_resource method
    def update_resource(self):
        updated_resource = super(ApigatewaySdkHelperCustom, self).update_resource()
        return updated_resource or self.get_resource().data
