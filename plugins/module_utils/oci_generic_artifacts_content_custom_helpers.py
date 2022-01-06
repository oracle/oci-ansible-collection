# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_config_utils,
    oci_common_utils,
)

import hashlib

try:
    from oci.artifacts import ArtifactsClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GenericArtifactContentHelperCustom:
    def __init__(self, *args, **kwargs):
        super(GenericArtifactContentHelperCustom, self).__init__(*args, **kwargs)
        self.artifacts_client = oci_config_utils.create_service_client(
            self.module, ArtifactsClient
        )

    def get_existing_resource_dict_for_update(self):
        # using get_generic_artifact_by_path of Artifacts Client as it returns sha256 digest of the file
        try:
            response = oci_common_utils.call_with_backoff(
                self.artifacts_client.get_generic_artifact_by_path,
                repository_id=self.module.params.get("repository_id"),
                artifact_path=self.module.params.get("artifact_path"),
                version=self.module.params.get("version"),
            ).data
        except ServiceError as se:
            if se.status == 404:
                return dict()
            raise
        return to_dict(response)

    def is_update_necessary(self, existing_resource_dict):
        # we need to compare the sha256 digest of the source file and the sha256 digest of the existing file
        # to check if the update is required
        file_path = self.module.params.get("generic_artifact_content_file")
        existing_sha256_digest = existing_resource_dict.get("sha256", None)

        h = hashlib.sha256()
        b = bytearray(oci_common_utils.MEBIBYTE)
        # using memoryview to store and calculate the sha256 instead of an array because
        # array internally would create a copy of the data whereas
        # memoryview allows accessing of the buffer without creating a copy of it internally.
        # hence it gives better performance in terms of memory using memoryview
        mv = memoryview(b)
        with open(file_path, "rb", buffering=0) as f:
            # iterate through the file content till number of bytes read 0.
            # f.readinto() returns number of bytes read.
            for n in iter(lambda: f.readinto(mv), 0):
                h.update(mv[:n])
        readable_hash = h.hexdigest()
        return readable_hash != existing_sha256_digest

    def update(self):
        file_path = self.module.params.get("generic_artifact_content_file")
        try:
            with open(file_path, "rb") as file:
                self.module.params["generic_artifact_content_body"] = file
                resource = super(GenericArtifactContentHelperCustom, self).update()
                self.module.params.pop("generic_artifact_content_body", None)
                return resource
        finally:
            self.module.params.pop("generic_artifact_content_body", None)
