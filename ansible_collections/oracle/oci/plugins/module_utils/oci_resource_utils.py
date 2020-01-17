# Copyright (c) 2020 Oracle and/or its affiliates.
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

# import the customisation files.
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_identity_custom_helpers,
    oci_network_custom_helpers,
)
from ansible.module_utils import six
import sys
import re
import inspect
import os

try:
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OCIResourceFactsHelperBase:
    def __init__(self, module, resource_type, service_client_class, namespace):
        self.module = module
        self.resource_type = resource_type
        self.service_client_class = service_client_class
        self.client = oci_config_utils.create_service_client(
            self.module, self.service_client_class
        )
        self.namespace = namespace

    def get_required_params_for_get(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError("get not supported by {0}".format(self.resource_type))

    def get_required_params_for_list(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError(
            "list not supported by {0}".format(self.resource_type)
        )

    def get_resource(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError("get not supported by {0}".format(self.resource_type))

    def list_resources(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError(
            "list not supported by {0}".format(self.resource_type)
        )

    def is_get(self):
        try:
            if all(
                [
                    self.module.params.get(get_param) is not None
                    for get_param in self.get_required_params_for_get()
                ]
            ):
                return True
        except NotImplementedError:
            return False
        return False

    def is_list(self):
        try:
            if all(
                [
                    self.module.params.get(list_param) is not None
                    for list_param in self.get_required_params_for_list()
                ]
            ):
                return True
        except NotImplementedError:
            return False
        return False

    def fail(self):
        self.module.fail_json(
            msg="Specify {0} to get all resources or {1} to get a specific resource.".format(
                self.get_required_params_for_list(), self.get_required_params_for_get()
            )
        )

    def get(self):
        resource = self.get_resource().data
        return to_dict(resource)

    def list(self):
        resources = self.list_resources()
        return to_dict(resources)


class OCIActionsHelperBase:
    def __init__(self, module, resource_type, service_client_class, namespace):
        self.module = module
        self.resource_type = resource_type
        self.service_client_class = service_client_class
        self.client = oci_config_utils.create_service_client(
            self.module, self.service_client_class
        )
        self.namespace = namespace
        self.check_mode = self.module.check_mode

    def get_module_resource_id_param(self):
        """Expected to be generated inside the module."""
        pass

    def get_module_resource_id(self):
        """Expected to be generated inside the module."""
        pass

    def get_get_fn(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError("get not supported by {0}".format(self.resource_type))

    def get_resource(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError("get not supported by {0}".format(self.resource_type))

    def get_action_fn(self, action):
        action_fn = getattr(self, action, None)
        if not (action_fn and callable(action_fn)):
            return None
        return action_fn

    def is_action_necessary(self, action):
        if action.upper() in oci_common_utils.ALWAYS_PERFORM_ACTIONS:
            return True
        resource = self.get_resource().data
        if hasattr(
            resource, "lifecycle_state"
        ) and resource.lifecycle_state in self.get_action_idempotent_states(action):
            return False
        return True

    def get_action_idempotent_states(self, action):
        return oci_common_utils.ACTION_IDEMPOTENT_STATES.get(action.upper(), [])

    def get_action_desired_states(self, action):
        return oci_common_utils.ACTION_DESIRED_STATES.get(
            action.upper(), oci_common_utils.DEFAULT_READY_STATES
        )

    def perform_action(self, action):

        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))

        try:
            get_response = self.get_resource()
        except ServiceError as se:
            self.module.fail_json(
                msg="Getting resource failed with exception: {0}".format(se.message)
            )
        else:
            resource = to_dict(get_response.data)

        is_action_necessary = self.is_action_necessary(action)
        if not is_action_necessary:
            return oci_common_utils.get_result(
                changed=False, resource_type=self.resource_type, resource=resource
            )

        if self.check_mode:
            return oci_common_utils.get_result(
                changed=True, resource_type=self.resource_type, resource=resource
            )

        try:
            actioned_resource = action_fn()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(actioned_resource),
            )


class OCIResourceHelperBase:
    NAME_PARAMETERS = ["display_name", "name"]
    USE_NAME_AS_IDENTIFIER_ENV_VAR_KEY = "OCI_USE_NAME_AS_IDENTIFIER"

    def __init__(self, module, resource_type, service_client_class, namespace):
        self.module = module
        self.resource_type = resource_type
        self.service_client_class = service_client_class
        self.client = oci_config_utils.create_service_client(
            self.module, self.service_client_class
        )
        self.namespace = namespace
        self.check_mode = self.module.check_mode

    def get_module_resource_id_param(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError(
            "{0} does not have a resource id.".format(self.resource_type)
        )

    def get_module_resource_id(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError(
            "{0} does not have a resource id.".format(self.resource_type)
        )

    def get_get_fn(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError("get not supported by {0}".format(self.resource_type))

    def get_resource(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError("get not supported by {0}".format(self.resource_type))

    def list_resources(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError(
            "list not supported by {0}".format(self.resource_type)
        )

    def create_resource(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError(
            "create not supported by {0}".format(self.resource_type)
        )

    def update_resource(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError(
            "update not supported by {0}".format(self.resource_type)
        )

    def delete_resource(self):
        """Expected to be generated inside the module."""
        raise NotImplementedError(
            "delete not supported by {0}".format(self.resource_type)
        )

    def get_create_model_class(self):
        """Expected to be generated inside the module."""
        pass

    def get_update_model_class(self):
        """Expected to be generated inside the module."""
        pass

    # some values are computed by the server based on user input
    # this function allows us to normalize user input values only for
    # the purposes of comparison to existing values
    # e.g. we can convert input: "foo" to input: "foo{service_added_suffix"}
    # to allow matching the appropriate resource
    def convert_request_model_fields_to_computed_server_values(self, model):
        """Expected to be generated inside the module."""
        pass

    def _has_name_parameter(self):
        if any(
            [
                True
                for parameter in self.NAME_PARAMETERS
                if self.module.params.get(parameter)
            ]
        ):
            return True
        return False

    def _has_resource_id_in_params(self):
        try:
            id_param = self.get_module_resource_id_param()
            if self.module.params.get(id_param):
                return True
            return False
        except NotImplementedError:
            return False

    def _use_name_as_identifier(self):
        if all(
            [
                os.environ.get(self.USE_NAME_AS_IDENTIFIER_ENV_VAR_KEY),
                self._has_name_parameter(),
                not self._has_resource_id_in_params(),
            ]
        ):
            return True
        return False

    def is_delete(self):
        if not self.module.params.get("state") == "absent":
            return False
        return True

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False
        if not self.get_module_resource_id():
            return False
        return True

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False
        if self.get_module_resource_id():
            return False
        return True

    def is_delete_using_name(self):
        if not self.module.params.get("state") == "absent":
            return False
        if not self._use_name_as_identifier():
            return False
        return True

    def is_update_using_name(self):
        if not self.module.params.get("state") == "present":
            return False
        if not self._use_name_as_identifier():
            return False
        try:
            self.get_resource_using_name()
        except ServiceError as se:
            if se.status == 404:
                return False
            raise
        return True

    def get_resource_name_parameter(self):
        for parameter in self.NAME_PARAMETERS:
            if self.module.params.get(parameter):
                return parameter
        return None

    def get_resource_using_name(self):
        name_parameter = self.get_resource_name_parameter()
        if not name_parameter:
            self.module.fail_json(
                msg="Resource does not have a {0} or not specified.".format(
                    name_parameter
                )
            )
        existing_resources = [
            existing_resource
            for existing_resource in self.list_resources()
            if hasattr(existing_resource, name_parameter)
            and getattr(existing_resource, name_parameter)
            == self.module.params.get(name_parameter)
        ]
        if len(existing_resources) > 1:
            self.module.fail_json(
                msg="Duplicate resources with {0} {1} exist.".format(
                    name_parameter, self.module.params.get(name_parameter)
                )
            )
        elif len(existing_resources) == 0:
            oci_common_utils.raise_does_not_exist_service_error(
                message="Resource with {0} {1} does not exist.".format(
                    name_parameter, self.module.params.get(name_parameter)
                )
            )
        return oci_common_utils.get_default_response_from_resource(
            resource=existing_resources[0]
        )

    def _is_resource_active(self, resource):
        if "lifecycle_state" not in resource.attribute_map:
            return True
        return resource.lifecycle_state not in oci_common_utils.DEAD_STATES

    def get_exclude_attributes(self):
        return ["freeform_tags", "node_count"]

    def get_attributes_to_consider(self, create_model):
        if self.module.params.get("key_by") is not None:
            return self.module.params["key_by"]
        return [
            attr
            for attr in create_model.attribute_map
            if attr not in self.get_exclude_attributes()
        ]

    def get_create_model(self):
        return convert_input_data_to_model_class(
            self.module.params, self.get_create_model_class()
        )

    def get_update_model(self):
        return convert_input_data_to_model_class(
            self.module.params, self.get_update_model_class()
        )

    def get_user_provided_value(self, attr):
        return self.module.params.get(attr)

    def get_matching_resource(self):

        create_model = self.get_create_model()
        self.convert_request_model_fields_to_computed_server_values(create_model)
        attributes_to_consider = (
            [
                parameter
                for parameter in self.NAME_PARAMETERS
                if self.module.params.get(parameter)
            ]
            if self._use_name_as_identifier()
            else self.get_attributes_to_consider(create_model)
        )
        for resource in self.list_resources():
            if not self._is_resource_active(resource):
                continue
            resource_dict = to_dict(resource)
            if oci_common_utils.is_dict_subset(
                source_dict=to_dict(create_model),
                target_dict=resource_dict,
                attrs=attributes_to_consider,
            ):
                return resource
        return None

    def create(self):

        if self.module.params.get("force_create"):
            if self.check_mode:
                return oci_common_utils.get_result(
                    changed=True, resource_type=self.resource_type, resource=dict()
                )
        else:
            resource_matched = self.get_matching_resource()
            if resource_matched:
                return oci_common_utils.get_result(
                    changed=False,
                    resource_type=self.resource_type,
                    resource=to_dict(resource_matched),
                )

        if self.check_mode:
            return oci_common_utils.get_result(
                changed=True, resource_type=self.resource_type, resource=dict()
            )

        try:
            created_resource = self.create_resource()

        except MaximumWaitTimeExceeded as ex:
            self.module.fail_json(msg=str(ex))
        except ServiceError as se:
            self.module.fail_json(msg=se.message)
        else:
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(created_resource),
            )

    def is_update_necessary(self):
        current_resource_dict = to_dict(self.get_resource().data)
        update_model = self.get_update_model()
        self.convert_request_model_fields_to_computed_server_values(update_model)
        update_model_dict = to_dict(update_model)
        return not oci_common_utils.are_dicts_equal(
            update_model_dict, current_resource_dict, update_model.attribute_map
        )

    def update(self):

        try:
            get_response = self.get_resource()
        except ServiceError as se:
            self.module.fail_json(
                msg="Getting resource failed with exception: {0}".format(se.message)
            )
        else:
            resource = to_dict(get_response.data)

        is_update_necessary = self.is_update_necessary()
        if not is_update_necessary:
            return oci_common_utils.get_result(
                changed=False, resource_type=self.resource_type, resource=resource
            )

        if self.check_mode:
            return oci_common_utils.get_result(
                changed=True, resource_type=self.resource_type, resource=resource
            )

        try:
            updated_resource = self.update_resource()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Updating resource failed with exception: {0}".format(se.message)
            )
        else:
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(updated_resource),
            )

    def delete(self):

        try:

            if not self.get_module_resource_id():
                self.module.fail_json(
                    msg="Specify {0} with state as 'absent' to delete a {1}.".format(
                        self.get_module_resource_id_param(), self.resource_type.upper()
                    )
                )

        except NotImplementedError:
            # a few resources have no resource identifier (because they don't follow the
            # normal path convention: DELETE /resources/{resourceId} (e.g. AppCatalogSubscription)
            # so there can be a delete without a resourceId
            pass

        try:
            get_response = self.get_resource()
        except ServiceError as se:
            if se.status == 404:
                return oci_common_utils.get_result(
                    changed=False, resource_type=self.resource_type, resource=dict()
                )
            self.module.fail_json(
                msg="Getting resource failed with exception: {0}".format(se.message)
            )
        else:
            resource = to_dict(get_response.data)
            if (
                "lifecycle_state" in resource
                and resource["lifecycle_state"] in oci_common_utils.DEAD_STATES
            ):
                return oci_common_utils.get_result(
                    changed=False, resource_type=self.resource_type, resource=resource
                )

        if self.check_mode:
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=oci_common_utils.get_resource_with_state(resource, "DELETED"),
            )

        try:
            deleted_resource = self.delete_resource()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            if se.status == 404:
                return oci_common_utils.get_result(
                    changed=True,
                    resource_type=self.resource_type,
                    resource=oci_common_utils.get_resource_with_state(
                        resource, "DELETED"
                    ),
                )
            self.module.fail_json(
                msg="Deleting resource failed with exception: {0}".format(se.message)
            )
        else:
            if deleted_resource:
                resource = to_dict(deleted_resource)
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=oci_common_utils.get_resource_with_state(resource, "DELETED"),
            )

    def set_required_ids_in_module_when_name_is_identifier(self, resource):
        id_param = self.get_module_resource_id_param()
        if resource.get(id_param):
            self.module.params[id_param] = resource[id_param]
        elif resource.get("id"):
            self.module.params[id_param] = resource["id"]

    def update_using_name(self):

        try:
            get_response = self.get_resource_using_name()
        except ServiceError as se:
            self.module.fail_json(
                msg="Getting resource failed with exception: {0}".format(se.message)
            )
        else:
            resource = to_dict(get_response.data)

        self.set_required_ids_in_module_when_name_is_identifier(resource)
        is_update_necessary = self.is_update_necessary()
        if not is_update_necessary:
            return oci_common_utils.get_result(
                changed=False, resource_type=self.resource_type, resource=resource
            )

        if self.check_mode:
            return oci_common_utils.get_result(
                changed=True, resource_type=self.resource_type, resource=resource
            )

        try:
            updated_resource = self.update_resource()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Updating resource failed with exception: {0}".format(se.message)
            )
        else:
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(updated_resource),
            )

    def delete_using_name(self):

        try:
            get_response = self.get_resource_using_name()
        except ServiceError as se:
            if se.status == 404:
                return oci_common_utils.get_result(
                    changed=False, resource_type=self.resource_type, resource=dict()
                )
            self.module.fail_json(
                msg="Getting resource failed with exception: {0}".format(se.message)
            )
        else:
            resource = to_dict(get_response.data)
            if (
                "lifecycle_state" in resource
                and resource["lifecycle_state"] in oci_common_utils.DEAD_STATES
            ):
                return oci_common_utils.get_result(
                    changed=False, resource_type=self.resource_type, resource=resource
                )

        if self.check_mode:
            return oci_common_utils.get_result(
                changed=True,
                resource_type=self.resource_type,
                resource=oci_common_utils.get_resource_with_state(resource, "DELETED"),
            )

        self.set_required_ids_in_module_when_name_is_identifier(resource)
        try:
            deleted_resource = self.delete_resource()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            if se.status == 404:
                return oci_common_utils.get_result(
                    changed=True,
                    resource_type=self.resource_type,
                    resource=oci_common_utils.get_resource_with_state(
                        resource, "DELETED"
                    ),
                )
            self.module.fail_json(
                msg="Deleting resource failed with exception: {0}".format(se.message)
            )
        else:
            if deleted_resource:
                resource = to_dict(deleted_resource)
            return oci_common_utils.get_result(
                changed=True, resource_type=self.resource_type, resource=resource
            )


# convert dictionary to a Python SDK model class
# for example:
#   data: {
#        'hostname_label': 'mytestinstance',
#        'subnet_id': 'ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx',
#        'display_name': 'my_vnic'
#   }
#
# model_class: <class 'oci.core.models.create_vnic_details.CreateVnicDetails'>
#
# will create a CreateVnicDetails instance with the relevant fields populated
# based on 'data'
def convert_input_data_to_model_class(data, model_class):
    # e.g. oci.core.models.create_vnic_details.LaunchInstanceDetails -> oci.core.models
    namespace = ".".join(model_class.__module__.split(".")[0:-1])

    # e.g. 'oci.core.models' -> <module 'oci.core.models'>
    module = sys.modules[namespace]

    # if the type is polymoprhic, data might be a subtype of model_class
    # and thus we need to parse it as the correct subtype based on the discriminator
    # if we parse based on the declared (base) type, we will skip all fields that are
    # only defined on the subtype
    model_instance = model_class()
    if hasattr(model_instance, "get_subtype"):
        # get_subtype expects the camelCase version of the data (i.e. if discriminator field
        # name is source_type in python it expects sourceType)
        camelized_top_level_keys = dict(
            (camelize(key), value) for key, value in six.iteritems(data)
        )
        subtype_name = model_instance.get_subtype(camelized_top_level_keys)
        model_class = getattr(module, subtype_name)
        model_instance = model_class()

    for attr in model_instance.attribute_map:
        if data.get(attr) is None:
            continue

        value = data[attr]

        # e.g. LaunchInstanceDetails.swagger_types.get('create_vnic_details') -> 'CreateVnicDetails'
        swagger_type = model_instance.swagger_types.get(attr)
        # if data is complex, we need to convert nested values
        if hasattr(module, swagger_type):
            value = convert_input_data_to_model_class(
                value, getattr(module, swagger_type)
            )
        elif swagger_type.find("list[") == 0:
            # convert individual items in the list to complex type
            element_swagger_type = re.match(r"list\[(.*)\]", swagger_type).group(1)
            if hasattr(module, element_swagger_type):
                converted_values = []
                for element in value:
                    converted_values.append(
                        convert_input_data_to_model_class(
                            element, getattr(module, element_swagger_type)
                        )
                    )
                value = converted_values
        elif swagger_type.find("dict(") == 0:
            # convert individual values in dict to complex type
            match = re.match(r"dict\(([^,]*), (.*)\)", swagger_type)
            entry_value_swagger_type = match.group(2)

            if hasattr(module, entry_value_swagger_type):
                converted_values = {}
                for key in value:
                    converted_values[key] = convert_input_data_to_model_class(
                        value[key], getattr(module, entry_value_swagger_type)
                    )

                value = converted_values

        setattr(model_instance, attr, value)
    return model_instance


# Converts an argument to camel case with a lower case first character. For example
# "my_param" would turn into "myParam" and "this_other_param" would be "thisOtherParam"
#
# Supports both UpperCaseCamel and lowerCaseCamel, though lower case is considered the default
def camelize(to_camelize, uppercase_first_letter=False):
    if not to_camelize:
        return ""

    if uppercase_first_letter:
        return re.sub(r"(?:^|[_-])(.)", lambda m: m.group(1).upper(), to_camelize)
    else:
        return (
            to_camelize[0].lower()
            + camelize(to_camelize, uppercase_first_letter=True)[1:]
        )


def get_custom_class_mapping(modules):
    """Find the custom classes in the given modules and return a mapping with class name as key and class as value"""
    custom_class_mapping = {}
    for module in modules:
        for obj_name in dir(module):
            if not obj_name.endswith("Custom"):
                continue
            obj = getattr(module, obj_name)
            if inspect.isclass(obj):
                custom_class_mapping[obj_name] = obj
    return custom_class_mapping


# Due to the generalisations made about the resource APIs or because of the ease of use enhancements, the generated
# modules might not always be perfect. The custom behaviour is handled by having a custom class which is used to
# override the generated behaviour. Create a mapping of those custom classes so that we can dynamically override
# the behaviour.
custom_helper_mapping = get_custom_class_mapping(
    [oci_identity_custom_helpers, oci_network_custom_helpers]
)


class DefaultHelperCustom:
    """Default class with no customizations"""


def get_custom_class(custom_class_name):
    """Return the custom class from mapping using the given name if exists, else return the default custom class."""
    custom_class = custom_helper_mapping.get(custom_class_name)
    if not custom_class:
        return DefaultHelperCustom
    return custom_class
