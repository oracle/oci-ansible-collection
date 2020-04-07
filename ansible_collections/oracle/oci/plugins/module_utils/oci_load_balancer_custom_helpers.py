# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

"""This module contains all the customisations for load balancer modules."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils import six
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackendHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        name = "{ip_address}:{port}".format(
            ip_address=module.params.get("ip_address"), port=module.params.get("port")
        )
        module.params["backend_name"] = name
        module.params["name"] = name

        super(BackendHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # these methods don't get generated because of the customization around
    # ip_address + port instead of backend_name / name
    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def get_update_model(self):
        return get_update_model_merged_with_existing_resource(self)


class CertificateHelperCustom:
    def is_create(self):
        # the default implementation of is_create checks that resource id param
        # is empty, and in this case resource id param "certificate_name" is
        # required for creation
        if not self.module.params.get("state") == "present":
            return False

        return True

    def get_exclude_attributes(self):
        exclude_attributes = super(
            CertificateHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "private_key",
            "passphrase",
        ]


class ListenerHelperCustom:
    def get_resource(self):
        # normally get via list would be generated, but in this case the resource doesn't
        # have a GET or a LIST API so both are custom
        resources = self.list_resources()
        for resource in resources:
            if self.module.params["name"] == resource.name:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def list_resources(self):
        # there is no list_listeners operation so we have to manually add it
        load_balancer_id = self.module.params["load_balancer_id"]
        try:
            response = self.client.get_load_balancer(load_balancer_id)
            existing_lb = response.data
        except ServiceError as ex:
            if ex.status != 404:
                self.module.fail_json(msg=ex.message)

        return [
            listener for listener_name, listener in six.iteritems(existing_lb.listeners)
        ]

    def get_update_model(self):
        return get_update_model_merged_with_existing_resource(self)


class BackendSetHelperCustom:
    def get_update_model(self):
        return get_update_model_merged_with_existing_resource(self)


def get_update_model_merged_with_existing_resource(helper):
    update_model = oci_common_utils.convert_input_data_to_model_class(
        helper.module.params, helper.get_update_model_class()
    )

    # the nulls don't get passed through to the service anyway and we want to remove
    # them so any real values from the existing resource can take precedence
    update_model_dict = to_dict(update_model)

    update_model_dict_without_nulls = dict(
        (k, v) for k, v in six.iteritems(update_model_dict) if v is not None
    )
    existing_resource_dict = to_dict(helper.get_resource().data)

    # we convert to a dict first so we can combine values from a response model
    # with an analogous input model
    # for example, input model: UpdateListenerDetails and response model ListenerDetails
    for user_update_model_key, user_update_model_value in six.iteritems(
        update_model_dict_without_nulls
    ):
        skip_overwrite_for_key = False
        if existing_resource_dict.get(user_update_model_key) is not None:
            existing_resource_value = existing_resource_dict.get(user_update_model_key)
            if (
                isinstance(existing_resource_value, list)
                and isinstance(user_update_model_value, list)
                and len(existing_resource_value) > 0
                and len(user_update_model_value) > 0
                # if the lengths are different its going to mismatch anyway
                # so no need to try to populate server side defaults
                and len(existing_resource_value) == len(user_update_model_value)
                and isinstance(existing_resource_value[0], dict)
                and isinstance(user_update_model_value[0], dict)
            ):
                # we're looking at a field that is a list of complex objects
                # so we want to do the same updating that we do at the top level
                # where we merge values from existing_resource and user_update_model
                # so that valyes with server side defaults get handled
                # index = 0
                # for existing_item in existing_resource_value:
                #     item_update_model_dict_without_nulls = {
                #         k: v for k, v in six.iteritems(user_update_model_value[index]) if v is not None
                #     }
                #     existing_item.update(item_update_model_dict_without_nulls)
                #     index = index + 1
                index = 0
                for existing_item in existing_resource_value:
                    # find the matching item in user_update_model_value so we can merge those fields into this existing_item
                    corresponding_item_in_user_update_model_value = None
                    for user_update_item in user_update_model_value:
                        is_match = True
                        for key, value in six.iteritems(user_update_item):
                            if value is None:
                                # value is None from user input so ignore this field when trying to
                                # find a matching object in existing_item
                                continue

                            is_match = is_match and value == existing_item.get(key)

                        if is_match:
                            corresponding_item_in_user_update_model_value = (
                                user_update_item
                            )
                            break

                    if corresponding_item_in_user_update_model_value:
                        # we manually merged at least one nested dict so dont overwrite this key at the top level
                        skip_overwrite_for_key = True
                        item_update_model_dict_without_nulls = dict(
                            (k, v)
                            for k, v in six.iteritems(
                                corresponding_item_in_user_update_model_value
                            )
                            if v is not None
                        )

                        existing_item.update(item_update_model_dict_without_nulls)

                    index = index + 1

        if not skip_overwrite_for_key:
            existing_resource_dict[user_update_model_key] = user_update_model_value

    complete_update_model_dict = dict(existing_resource_dict)

    # once we have the combined dict representing the update model from params + existing fields
    # from get_resource respone, we convert that back to the update_model using this util function
    update_model = oci_common_utils.convert_input_data_to_model_class(
        complete_update_model_dict, helper.get_update_model_class()
    )

    return update_model
