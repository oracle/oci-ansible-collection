# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils._text import to_bytes

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class DataSafeConfigurationHelperCustom:
    def is_update(self):
        return True


class DataSafeOnPremConnectorHelperCustom:
    # base class returns: onpremconnector
    # expected value (value in the service response is): onpremconnectors
    def get_entity_type(self):
        return "onpremconnectors"


class DataSafeOnPremConnectorActionsHelperCustom:
    # get the binary response and store the data in the file provided
    def generate_on_prem_connector_configuration(self):
        dest = self.module.params.get("dest")
        if dest is None:
            raise ValueError("dest parameter is required")

        response = super(
            DataSafeOnPremConnectorActionsHelperCustom, self
        ).generate_on_prem_connector_configuration()
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None
