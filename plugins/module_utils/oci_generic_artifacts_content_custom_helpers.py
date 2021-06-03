# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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


class GenericArtifactContentHelperCustom:
    def get_existing_resource_dict_for_update(self):
        # Not considering the idempotency for upload
        # since the GetGenericArtifactContent api doesnt return the sha256 digest of the file
        # Also The artifact size could be big, so we are skipping idempotency
        return None

    def is_update_necessary(self, existing_resource_dict):
        # Not considering the idempotency for upload
        # since the GetGenericArtifactContent api doesnt return the sha256 digest of the file
        # Also The artifact size could big, so we are skipping idempotency
        return True

    def update_resource(self):
        file_path = self.module.params.get("generic_artifact_content_file")
        with open(file_path, "rb") as input_file:
            data = input_file.read()
        self.module.params["generic_artifact_content_body"] = data
        resource = super(GenericArtifactContentHelperCustom, self).update_resource()
        self.module.params.pop("generic_artifact_content_body", None)
        return resource
