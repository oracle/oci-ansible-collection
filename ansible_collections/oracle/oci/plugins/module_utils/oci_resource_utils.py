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

import inspect
import os

try:
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OCIResourceCommonBase:
    """Base class for the Helper Classes to hold common code."""

    def prepare_result(self, changed, resource_type, resource=None):
        result = dict(changed=changed)
        result[resource_type] = resource
        return result

    def _is_resource_active(self, resource):
        if "lifecycle_state" not in resource.attribute_map:
            return True
        return resource.lifecycle_state not in oci_common_utils.DEAD_STATES


class OCIResourceFactsHelperBase(OCIResourceCommonBase):
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


class OCIActionsHelperBase(OCIResourceCommonBase):
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
            return self.prepare_result(
                changed=False, resource_type=self.resource_type, resource=resource
            )

        if self.check_mode:
            return self.prepare_result(
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
            return self.prepare_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(actioned_resource),
            )


class OCIResourceHelperBase(OCIResourceCommonBase):
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

    def get_resource_active_states(self):
        return oci_common_utils.DEFAULT_READY_STATES

    def get_resource_terminated_states(self):
        return oci_common_utils.DEFAULT_TERMINATED_STATES

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
            and self._is_resource_active(existing_resource)
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

    def get_exclude_attributes(self):
        return ["freeform_tags", "node_count"]

    def get_attributes_to_consider_for_create_idempotency_check(self, create_model):
        if self.module.params.get("key_by") is not None:
            return self.module.params["key_by"]
        return [
            attr
            for attr in create_model.attribute_map
            if attr not in self.get_exclude_attributes()
        ]

    def get_create_model(self):
        return oci_common_utils.convert_input_data_to_model_class(
            self.module.params, self.get_create_model_class()
        )

    def get_create_model_dict_for_idempotence_check(self, create_model):
        """This function allows any customisations that are needed in the create model for comparison during the
        idempotence check.

        This can be done for many reasons. For ex: some resource have different names for same parameter in create
        and get model making the idempotence logic to fail or we may need to update a value since the server computes
        and stores it differently etc."""
        return to_dict(create_model)

    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        """This function allows any customisations that are needed in the existing resource for comparison during the
        idempotence check.

        This can useful in scenarios where the existing resource does not have all the information used to create
        it but need multiple calls to get the information. For ex: create_vnic_details in attach_vnic_details has
        information which is not available in vnic_attachment completely. We need to get the vnic details which
        has the information and then do the comparison."""
        return to_dict(existing_resource)

    def get_update_model(self):
        return oci_common_utils.convert_input_data_to_model_class(
            self.module.params, self.get_update_model_class()
        )

    def get_update_model_dict_for_idempotence_check(self, update_model):
        """This function allows any customisations that are needed in the update model for comparison during the
        idempotence check.

        This can be done for many reasons. For ex: some resource have different names for same parameter in update
        and get model making the idempotence logic to fail or we may need to update a value since the server computes
        and stores it differently etc."""
        return to_dict(update_model)

    def get_user_provided_value(self, attr):
        return self.module.params.get(attr)

    def get_matching_resource(self):

        create_model = self.get_create_model()
        attributes_to_consider = (
            [
                parameter
                for parameter in self.NAME_PARAMETERS
                if self.module.params.get(parameter)
            ]
            if self._use_name_as_identifier()
            else self.get_attributes_to_consider_for_create_idempotency_check(
                create_model
            )
        )
        create_model_dict = self.get_create_model_dict_for_idempotence_check(
            create_model
        )
        for resource in self.list_resources():
            if not self._is_resource_active(resource):
                continue

            resource_dict = self.get_existing_resource_dict_for_idempotence_check(
                resource
            )
            if oci_common_utils.is_dict_subset(
                source_dict=create_model_dict,
                target_dict=resource_dict,
                attrs=attributes_to_consider,
            ):
                return resource
        return None

    def create(self):

        if self.module.params.get("force_create"):
            if self.check_mode:
                return self.prepare_result(
                    changed=True, resource_type=self.resource_type, resource=dict()
                )
        else:
            resource_matched = self.get_matching_resource()
            if resource_matched:
                return self.prepare_result(
                    changed=False,
                    resource_type=self.resource_type,
                    resource=to_dict(resource_matched),
                )

        if self.check_mode:
            return self.prepare_result(
                changed=True, resource_type=self.resource_type, resource=dict()
            )

        try:
            created_resource = self.create_resource()

        except MaximumWaitTimeExceeded as ex:
            self.module.fail_json(msg=str(ex))
        except ServiceError as se:
            self.module.fail_json(msg=se.message)
        else:
            return self.prepare_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(created_resource),
            )

    def is_update_necessary(self):
        current_resource_dict = to_dict(self.get_resource().data)
        update_model = self.get_update_model()
        update_model_dict = self.get_update_model_dict_for_idempotence_check(
            update_model
        )
        return not oci_common_utils.are_dicts_equal(
            update_model_dict, current_resource_dict
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
            return self.prepare_result(
                changed=False, resource_type=self.resource_type, resource=resource
            )

        if self.check_mode:
            return self.prepare_result(
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
            return self.prepare_result(
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
                return self.prepare_result(
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
                return self.prepare_result(
                    changed=False, resource_type=self.resource_type, resource=resource
                )

        if self.check_mode:
            return self.prepare_result(
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
                return self.prepare_result(
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
            return self.prepare_result(
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
            return self.prepare_result(
                changed=False, resource_type=self.resource_type, resource=resource
            )

        if self.check_mode:
            return self.prepare_result(
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
            return self.prepare_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(updated_resource),
            )

    def delete_using_name(self):

        try:
            get_response = self.get_resource_using_name()
        except ServiceError as se:
            if se.status == 404:
                return self.prepare_result(
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
                return self.prepare_result(
                    changed=False, resource_type=self.resource_type, resource=resource
                )

        if self.check_mode:
            return self.prepare_result(
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
                return self.prepare_result(
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
            return self.prepare_result(
                changed=True, resource_type=self.resource_type, resource=resource
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
# import the customisation files.
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_identity_custom_helpers,
    oci_network_custom_helpers,
    oci_compute_custom_helpers,
    oci_blockstorage_custom_helpers,
    oci_compute_management_custom_helpers,
    oci_audit_custom_helpers,
    oci_object_storage_custom_helpers,
    oci_file_storage_custom_helpers,
)  # noqa

custom_helper_mapping = get_custom_class_mapping(
    [
        oci_identity_custom_helpers,
        oci_network_custom_helpers,
        oci_compute_custom_helpers,
        oci_blockstorage_custom_helpers,
        oci_compute_management_custom_helpers,
        oci_audit_custom_helpers,
        oci_object_storage_custom_helpers,
        oci_file_storage_custom_helpers,
    ]
)


class DefaultHelperCustom:
    """Default class with no customizations"""


def get_custom_class(custom_class_name):
    """Return the custom class from mapping using the given name if exists, else return the default custom class."""
    custom_class = custom_helper_mapping.get(custom_class_name)
    if not custom_class:
        return DefaultHelperCustom
    return custom_class
