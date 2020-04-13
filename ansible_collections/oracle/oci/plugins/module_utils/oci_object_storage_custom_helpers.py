# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BucketHelperCustom:
    def __init__(self, *args, **kwargs):
        super(BucketHelperCustom, self).__init__(*args, **kwargs)
        self.module.params["bucket_name"] = self.module.params["name"]
        self.module.params["namespace"] = self.module.params["namespace_name"]

    # Bucket does not have an id. Even though name could be used as the resource identitifer, the resource id is
    # generally used to differentiate between create and update/delete. But since name is required for all of them,
    # it may not be very useful to have that as the resource id. So just return None so that other functions work
    # as intended.
    def get_module_resource_id(self):
        return None

    # Base class decides if it is an update based on the presence of the resource id. Since this module does not have
    # one (read comments for get_module_resource_id), override to check the existence of the bucket to decide if it
    # is an update.
    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False
        try:
            self.get_resource()
        except ServiceError as se:
            if se.status == 404:
                return False
            raise
        return True

    def list_resources(self, *args, **kwargs):
        # List returns a summary model. There are some parameters in the create model () which are not in the summary
        # model causing idempotence failures. So get the full model by making the get call. We would only be making
        # a single extra API call as name is a required parameter and we are filtering the resources by name first
        # and then make the get call.
        return [
            self.client.get_bucket(
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("name"),
            ).data
            for bucket in super(BucketHelperCustom, self).list_resources(
                *args, **kwargs
            )
            if bucket.name == self.module.params.get("name")
        ]
