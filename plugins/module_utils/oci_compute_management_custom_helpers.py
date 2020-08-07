# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_config_utils,
)

try:
    import oci
    from oci.util import to_dict
    from oci.core import VirtualNetworkClient, ComputeClient, BlockstorageClient
    from oci.core.models import (
        InstanceConfigurationLaunchInstanceDetails,
        InstanceConfigurationBlockVolumeDetails,
        InstanceConfigurationAttachVnicDetails,
        InstanceConfigurationCreateVnicDetails,
        InstanceConfigurationAttachVolumeDetails,
        InstanceConfigurationCreateVolumeDetails,
        AttachLoadBalancerDetails,
        DetachLoadBalancerDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceConfigurationHelperCustom:
    def __init__(self, *args, **kwargs):
        super(InstanceConfigurationHelperCustom, self).__init__(*args, **kwargs)
        self.compute_client = oci_config_utils.create_service_client(
            self.module, ComputeClient
        )
        self.virtual_network_client = oci_config_utils.create_service_client(
            self.module, VirtualNetworkClient
        )
        self.blockstorage_client = oci_config_utils.create_service_client(
            self.module, BlockstorageClient
        )

    def get_instance_configuration_launch_details_from_instance(self, instance):
        launch_details = oci_common_utils.convert_input_data_to_model_class(
            to_dict(instance), InstanceConfigurationLaunchInstanceDetails
        )
        vnics = [
            self.virtual_network_client.get_vnic(vnic_id=vnic_attachment.vnic_id).data
            for vnic_attachment in self.compute_client.list_vnic_attachments(
                compartment_id=instance.compartment_id, instance_id=instance.id
            ).data
        ]
        primary_vnic = None
        for vnic in vnics:
            if vnic.is_primary:
                primary_vnic = vnic
        launch_details.create_vnic_details = oci_common_utils.convert_input_data_to_model_class(
            to_dict(primary_vnic), InstanceConfigurationCreateVnicDetails
        )
        return to_dict(launch_details)

    def get_instance_configuration_block_volume_from_instance(self, instance):
        secondary_vnics = []
        for vnic_attachment in self.compute_client.list_vnic_attachments(
            compartment_id=instance.compartment_id, instance_id=instance.id
        ).data:
            vnic = self.virtual_network_client.get_vnic(
                vnic_id=vnic_attachment.vnic_id
            ).data
            if vnic.is_primary:
                continue
            secondary_vnic = InstanceConfigurationAttachVnicDetails()
            secondary_vnic.display_name = vnic.display_name
            secondary_vnic.nic_index = vnic_attachment.nic_index
            secondary_vnic.create_vnic_details = oci_common_utils.convert_input_data_to_model_class(
                to_dict(vnic), InstanceConfigurationCreateVnicDetails
            )
            secondary_vnics.append(secondary_vnic)
        return to_dict(secondary_vnics)

    def get_instance_configuration_secondary_vnic_from_instance(self, instance):
        block_volumes = []
        for volume_attachment in self.compute_client.list_volume_attachments(
            compartment_id=instance.compartment_id, instance_id=instance.id
        ).data:
            volume = self.blockstorage_client.get_volume(
                volume_id=volume_attachment.volume_id
            ).data
            block_volume = InstanceConfigurationBlockVolumeDetails()
            block_volume.attach_details = oci_common_utils.convert_input_data_to_model_class(
                to_dict(volume_attachment), InstanceConfigurationAttachVolumeDetails
            )
            block_volume.create_details = oci_common_utils.convert_input_data_to_model_class(
                to_dict(volume), InstanceConfigurationCreateVolumeDetails
            )
            block_volumes.append(block_volume)
        return to_dict(block_volumes)

    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            InstanceConfigurationHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # source is the discriminator field and does not exist in the get model. Remove it so that it does not cause
        # the idempotence logic to cause a mis-match.
        create_model_dict.pop("source")
        # If the instance_configuration is being created from an instance, then get the details of the information
        # so that we can make a good comparison with the existing instance configurations. Else we would get
        # false positives since we would only be comparing basic information like display_name, compartment_id etc.
        # of instance_configuration.
        if create_model_dict.get("instance_id"):
            # If user chose to ignore instance_id, then skip getting the instance details for comparison.
            if self.module.params.get(
                "key_by"
            ) and "instance_id" not in self.module.params.get("key_by"):
                return create_model_dict
            instance = self.compute_client.get_instance(
                instance_id=create_model_dict.pop("instance_id")
            ).data
            create_model_dict["instance_details"] = dict()
            create_model_dict["instance_details"][
                "launch_details"
            ] = self.get_instance_configuration_launch_details_from_instance(instance)
            create_model_dict["instance_details"][
                "block_volumes"
            ] = self.get_instance_configuration_block_volume_from_instance(instance)
            create_model_dict["instance_details"][
                "secondary_vnics"
            ] = self.get_instance_configuration_secondary_vnic_from_instance(instance)

        return create_model_dict


class InstanceConfigurationActionsHelperCustom:

    # instance_configuration launch action returns an instance and not instance_configuration. Currently the base
    # classes do not support custom return field names and use the resource types. Until the feature is added
    # manually update the return field to instance.
    # TODO: Update base class to handle custom return field names from generated code.
    def prepare_result(self, *args, **kwargs):
        super_result = super(
            InstanceConfigurationActionsHelperCustom, self
        ).prepare_result(*args, **kwargs)
        super_result["instance"] = super_result.pop("instance_configuration", None)
        return super_result


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
