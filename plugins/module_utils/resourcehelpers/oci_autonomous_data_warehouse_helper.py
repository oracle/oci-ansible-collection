# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
from ansible.module_utils._text import to_bytes


try:
    import oci

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDataWarehouseHelperCustom:
    def get_action_desired_states(self, action):
        if action == "start":
            return ["AVAILABLE"]
        elif action == "stop":
            return ["STOPPED"]
        elif action == "restore":
            return ["AVAILABLE", "FAILED"]
        elif action == "generate_wallet":
            return ["AVAILABLE"]

    def get_action_idempotent_states(self, action):
        if action == "start":
            return ["AVAILABLE", "STARTING"]
        if action == "stop":
            return ["STOPPED", "STOPPING"]
        return []

    def is_action_necessary(self, action):
        if action == "restore":
            return True
        if action == "generate_wallet":
            if self.module.params.get("force"):
                return True
            wallet_file = self.module.params.get("wallet_file")
            if os.path.isfile(to_bytes(wallet_file)):
                return False
            return True
        resource = self.get_resource().data
        if action in [
            "start",
            "stop",
        ] and resource.lifecycle_state in self.get_action_idempotent_states(action):
            return False
        return True

    def generate_wallet(self):
        wallet_file = self.module.params.get("wallet_file")
        if wallet_file is None or len(wallet_file.strip()) == 0:
            self.module.fail_json("Wallet file must be declared")
        generate_wallet_response = super(
            AutonomousDataWarehouseHelperCustom, self
        ).generate_wallet()
        with open(to_bytes(wallet_file), "wb") as f:
            for d in generate_wallet_response.data:
                f.write(d)
