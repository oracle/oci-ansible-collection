# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

logger = oci_common_utils.get_logger("oci_announcements_service_custom_helpers")


class ConnectionHelperCustom:
    def get_exclude_attributes(self):
        return super(ConnectionHelperCustom, self).get_exclude_attributes() + [
            "tls_wallet",
            "tls_keystore",
        ]

    # overriding this to avoid comparison of fields not returned while getting the resource as they are sensitive
    # e.g. password is nested under admin_credentials
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            ConnectionHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        if create_model_dict.get("admin_credentials") is not None:
            create_model_dict["admin_credentials"].pop("password", None)
        if create_model_dict.get("ssh_details") is not None:
            create_model_dict["ssh_details"].pop("sshkey", None)

        return create_model_dict


class MigrationHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            MigrationHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        if create_model_dict.get("admin_credentials") is not None:
            create_model_dict["admin_credentials"].pop("password", None)
        if create_model_dict.get("golden_gate_details") is not None:
            if create_model_dict.get("golden_gate_details").get("hub") is not None:
                if (
                    create_model_dict.get("golden_gate_details")
                    .get("hub")
                    .get("rest_admin_credentials")
                    is not None
                ):
                    create_model_dict.get("golden_gate_details").get("hub").get(
                        "rest_admin_credentials"
                    ).pop("password", None)
                if (
                    create_model_dict.get("golden_gate_details")
                    .get("hub")
                    .get("source_db_admin_credentials")
                    is not None
                ):
                    create_model_dict.get("golden_gate_details").get("hub").get(
                        "source_db_admin_credentials"
                    ).pop("password", None)
                if (
                    create_model_dict.get("golden_gate_details")
                    .get("hub")
                    .get("source_container_db_admin_credentials")
                    is not None
                ):
                    create_model_dict.get("golden_gate_details").get("hub").get(
                        "source_container_db_admin_credentials"
                    ).pop("password", None)
                if (
                    create_model_dict.get("golden_gate_details")
                    .get("hub")
                    .get("target_db_admin_credentials")
                    is not None
                ):
                    create_model_dict.get("golden_gate_details").get("hub").get(
                        "target_db_admin_credentials"
                    ).pop("password", None)

        return create_model_dict
