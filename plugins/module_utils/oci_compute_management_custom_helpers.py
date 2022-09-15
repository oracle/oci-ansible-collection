# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


try:
    import oci
    from oci.util import to_dict
    from oci.exceptions import ServiceError
    from oci.core.models import (
        AttachLoadBalancerDetails,
        DetachLoadBalancerDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstancePoolActionsHelperCustom:
    LIFECYCLE_STATE_ATTACHED = "ATTACHED"
    LIFECYCLE_STATE_DETACHED = "DETACHED"

    def is_attach_load_balancer_necessary(self, instance_pool):
        if not instance_pool.load_balancers:
            return True
        user_load_balancer_attachment_details = to_dict(
            oci_common_utils.convert_input_data_to_model_class(
                self.module.params, AttachLoadBalancerDetails
            )
        )
        for existing_load_balancer_attachment in instance_pool.load_balancers:
            if (
                existing_load_balancer_attachment.lifecycle_state
                in oci_common_utils.DEAD_STATES
            ):
                continue
            if oci_common_utils.compare_dicts(
                user_load_balancer_attachment_details,
                to_dict(existing_load_balancer_attachment),
            ):
                return False
        return True

    def is_detach_load_balancer_necessary(self, instance_pool):
        if not instance_pool.load_balancers:
            return False
        user_load_balancer_detachment_details = to_dict(
            oci_common_utils.convert_input_data_to_model_class(
                self.module.params, DetachLoadBalancerDetails
            )
        )
        for existing_load_balancer_attachment in instance_pool.load_balancers:
            if (
                existing_load_balancer_attachment.lifecycle_state
                in oci_common_utils.DEAD_STATES
            ):
                continue
            if oci_common_utils.compare_dicts(
                user_load_balancer_detachment_details,
                to_dict(existing_load_balancer_attachment),
            ):
                return True
        return False

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource()
        if action == "attach_load_balancer":
            return self.is_attach_load_balancer_necessary(resource)
        elif action == "detach_load_balancer":
            return self.is_detach_load_balancer_necessary(resource)
        return super(InstancePoolActionsHelperCustom, self).is_action_necessary(
            action, resource
        )

    def attach_load_balancer(self):
        instance_pool = super(
            InstancePoolActionsHelperCustom, self
        ).attach_load_balancer()
        # wait until the load balancer attachment comes to a proper state

        def evaluate_response_for_load_balancer_attachment(response):
            if not response.data.load_balancers:
                return False
            user_load_balancer_attachment_details = to_dict(
                oci_common_utils.convert_input_data_to_model_class(
                    self.module.params, AttachLoadBalancerDetails
                )
            )
            for existing_load_balancer_attachment in response.data.load_balancers:
                if (
                    existing_load_balancer_attachment.lifecycle_state
                    in oci_common_utils.DEAD_STATES
                ):
                    continue
                if (
                    oci_common_utils.compare_dicts(
                        user_load_balancer_attachment_details,
                        to_dict(existing_load_balancer_attachment),
                    )
                    and existing_load_balancer_attachment.lifecycle_state
                    == self.LIFECYCLE_STATE_ATTACHED
                ):
                    return True
            return False

        wait_response = oci.wait_until(
            self.client,
            self.client.get_instance_pool(instance_pool.id),
            evaluate_response=evaluate_response_for_load_balancer_attachment,
            max_wait_seconds=self.get_wait_timeout(),
            fetch_func=lambda **kwargs: self.get_resource(),
        )
        return wait_response.data

    def detach_load_balancer(self):
        instance_pool = super(
            InstancePoolActionsHelperCustom, self
        ).detach_load_balancer()
        # wait until the load balancer is detached

        def evaluate_response_for_load_balancer_detachment(response):
            if not response.data.load_balancers:
                return True
            user_load_balancer_detachment_details = to_dict(
                oci_common_utils.convert_input_data_to_model_class(
                    self.module.params, DetachLoadBalancerDetails
                )
            )
            for existing_load_balancer_attachment in response.data.load_balancers:
                if (
                    oci_common_utils.compare_dicts(
                        user_load_balancer_detachment_details,
                        to_dict(existing_load_balancer_attachment),
                    )
                    and existing_load_balancer_attachment.lifecycle_state
                    == self.LIFECYCLE_STATE_DETACHED
                ):
                    return True
            return False

        wait_response = oci.wait_until(
            self.client,
            self.client.get_instance_pool(instance_pool.id),
            evaluate_response=evaluate_response_for_load_balancer_detachment,
            max_wait_seconds=self.get_wait_timeout(),
            fetch_func=lambda **kwargs: self.get_resource(),
        )
        return wait_response.data


class InstancePoolInstanceHelperCustom:
    # adding this override as get_get_model_from_summary_model in resource utils
    # needs get_module_resource_id_param to handle the TypeError case.
    # Refer get_get_model_from_summary_model to get more insights.
    def get_module_resource_id_param(self):
        return "instance_id"

    # is state is present the assuming it is always create
    # default value for state is present
    def is_create(self):
        return self.module.params.get("state") == "present"

    # instance_id is not there in response model and
    # Codegen marks instance_id as not required for idempotence check
    # In the response model we get "id", changing it to "instance_id"
    # and removing "instance_id" from excluded_attributes
    # in get_exclude_attibutes()
    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        existing_dict = super(
            InstancePoolInstanceHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)
        if "id" in existing_dict:
            existing_dict["instance_id"] = existing_dict["id"]
            existing_dict.pop("id", None)
        return existing_dict

    def get_exclude_attributes(self):
        exclude_attributes = super(
            InstancePoolInstanceHelperCustom, self
        ).get_exclude_attributes()

        remove_exclude_attributes = ["instance_id"]
        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exclude_attributes
        ]

        return exclude_attributes


class InstancePoolInstanceActionsHelperCustom:

    # when we do a get resource, we sometimes get 404 error from backend while the resource is detaching
    # so we return a dummy response sometimes.
    # Note: While detaching WORK_REQUEST_WAITER is used & it waits & after WORK REQUEST responses are finished
    # then in wait utils it calls get_resource & get_resource returns 404 & module fails.
    # This piece of code handles that
    def get_resource(self):
        try:
            return super(InstancePoolInstanceActionsHelperCustom, self).get_resource()
        except ServiceError as se:
            if se.status == 404:
                return oci_common_utils.get_default_response_from_resource(
                    resource=None
                )
            raise
