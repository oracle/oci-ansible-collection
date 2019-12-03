# Copyright (c) 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.oracle import oci_common_utils

try:
    import oci
    from oci.exceptions import ServiceError
    from oci.object_storage.models import PutObjectLifecyclePolicyDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class ObjectLifecyclePolicyHelperCustom:
    # - Most modules use the *_id input parameter to determine if the operation
    #   is an update instead of a create, but in this case we don't need that
    #   because the ObjectLifecyclePolicy is identified uniquely by the namespace_name
    #   and bucket_name. Thus, a CREATE and UPDATE attempt look identical in a user playbook
    # - ObjectLifecyclePolicy only supports PUT and not POST so PutObjectLifecyclePolicy
    #   gets classified as an UPDATE operation on the resource and thus none of the normal
    #   create related operations are generated, thus we define them below

    # methods necessary for CREATE
    def list_resources(self):
        # ObjectLifecyclePolicy is defined per Bucket so listing is just returning
        # the single policy if it is defined and otherwise an empty list
        try:
            return [self.get_resource().data]
        except ServiceError as e:
            if e.code != "LifecyclePolicyNotFound":
                raise e

        return []

    def get_create_model_class(self):
        return PutObjectLifecyclePolicyDetails

    def create_resource(self):
        return self.update_resource()

    # override UPDATE to use CREATE underneath because there may be no existing
    # resource to fetch which is fine for CREATE but causes UPDATE to fail
    def update(self, check_applicable=True, wait_applicable=True):
        return self.create(
            check_applicable=check_applicable, wait_applicable=wait_applicable
        )
