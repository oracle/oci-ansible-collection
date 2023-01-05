# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_config_utils,
    oci_wait_utils,
)
from ansible.module_utils import six

try:
    from oci.core import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError
    from oci.core.models import InstancePowerActionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False
import logging

logger = logging.getLogger(__name__)


class AppCatalogSubscriptionHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        module.params["resource_version"] = module.params["listing_resource_version"]

        super(AppCatalogSubscriptionHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # app_catalog_subscription does not have a resource id. It only has a create and delete operation.
    # Both can be distinguished based on the `state` attribute.
    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return True

    def is_delete(self):
        if not self.module.params.get("state") == "absent":
            return False

        return True

    def get_resource(self):
        app_catalog_subscriptions = oci_common_utils.list_all_resources(
            self.client.list_app_catalog_subscriptions,
            compartment_id=self.module.params["compartment_id"],
            listing_id=self.module.params["listing_id"],
        )
        for app_catalog_subscription in app_catalog_subscriptions:
            if (
                app_catalog_subscription.listing_resource_version
                == self.module.params["resource_version"]
            ):
                return oci_common_utils.get_default_response_from_resource(
                    resource=app_catalog_subscription
                )
        oci_common_utils.raise_does_not_exist_service_error(
            message="The app catalog subscription does not exist."
        )


def get_primary_ips(compute_client, network_client, instance):
    if not instance:
        return None, None

    primary_public_ip = None
    primary_private_ip = None

    vnic_attachments = oci_common_utils.list_all_resources(
        compute_client.list_vnic_attachments,
        compartment_id=instance["compartment_id"],
        instance_id=instance["id"],
    )

    if vnic_attachments:
        for vnic_attachment in vnic_attachments:
            if vnic_attachment.lifecycle_state == "ATTACHED":
                try:
                    vnic = network_client.get_vnic(vnic_attachment.vnic_id).data
                    if vnic.is_primary:
                        if vnic.public_ip:
                            primary_public_ip = vnic.public_ip
                        if vnic.private_ip:
                            primary_private_ip = vnic.private_ip
                except ServiceError as ex:
                    if ex.status == 404:
                        logger.debug(
                            "Either VNIC with ID {0} does not exist or you are not authorized to access it.".format(
                                vnic_attachment.vnic_id
                            )
                        )

    return primary_public_ip, primary_private_ip


def add_primary_ip_info(module, compute_client, network_client, instance):
    try:
        primary_public_ip, primary_private_ip = get_primary_ips(
            compute_client, network_client, instance
        )
        instance["primary_public_ip"] = primary_public_ip
        instance["primary_private_ip"] = primary_private_ip
    except ServiceError as ex:
        instance["primary_public_ip"] = None
        instance["primary_private_ip"] = None
        module.fail_json(msg=ex.message)


class InstanceHelperCustom:
    def __init__(self, *args, **kwargs):
        super(InstanceHelperCustom, self).__init__(*args, **kwargs)
        self.network_client = oci_config_utils.create_service_client(
            self.module, VirtualNetworkClient
        )

    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            InstanceHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # is_pv_encryption_in_transit_enabled is a top level param on LaunchInstanceDetails but it gets returned
        # inside Instance.LaunchOptions so we need to propagate the value so that the existing resource matching
        # logic works properly
        if create_model_dict.get("is_pv_encryption_in_transit_enabled") is not None:
            if create_model_dict.get("launch_options"):
                if (
                    create_model_dict["launch_options"].get(
                        "is_pv_encryption_in_transit_enabled"
                    )
                    is None
                ):
                    create_model_dict["launch_options"][
                        "is_pv_encryption_in_transit_enabled"
                    ] = create_model_dict.pop("is_pv_encryption_in_transit_enabled")
                else:
                    # is_pv_encryption_in_transit_enabled is set both as a top level parameter and also under
                    # launch_options. If the values match ignore the top level parameter. Else throw an error.
                    if (
                        create_model_dict["launch_options"][
                            "is_pv_encryption_in_transit_enabled"
                        ]
                        != create_model_dict["is_pv_encryption_in_transit_enabled"]
                    ):
                        self.module.fail_json(
                            "Conflicting values specified for is_pv_encryption_in_transit_enabled as a top level parameter and under launch_options parameter."
                        )
                    create_model_dict.pop("is_pv_encryption_in_transit_enabled")
            else:
                create_model_dict["launch_options"] = dict(
                    is_pv_encryption_in_transit_enabled=create_model_dict.pop(
                        "is_pv_encryption_in_transit_enabled"
                    )
                )
        # kms_key_id comes as null from get_instance even when instance has it. So ignore for idempotence.
        if create_model_dict.get("source_details"):
            create_model_dict["source_details"].pop("kms_key_id", None)
        return create_model_dict

    def prepare_result(self, *args, **kwargs):
        result = super(InstanceHelperCustom, self).prepare_result(*args, **kwargs)
        if result.get("instance"):
            add_primary_ip_info(
                self.module, self.client, self.network_client, result["instance"]
            )
        return result


class InstanceFactsHelperCustom:
    def __init__(self, *args, **kwargs):
        super(InstanceFactsHelperCustom, self).__init__(*args, **kwargs)
        self.network_client = oci_config_utils.create_service_client(
            self.module, VirtualNetworkClient
        )

    def get(self, *args, **kwargs):
        instance = super(InstanceFactsHelperCustom, self).get(*args, **kwargs)
        add_primary_ip_info(self.module, self.client, self.network_client, instance)
        return instance

    def list(self, *args, **kwargs):
        instances = super(InstanceFactsHelperCustom, self).list(*args, **kwargs)
        for instance in instances:
            add_primary_ip_info(self.module, self.client, self.network_client, instance)
        return instances


class BootVolumeAttachmentHelperCustom:
    # An instance can only be attached to one boot volume and the name given to the attachment does not affect the
    # resource. Also a display_name update to the attachment resource does not seem to take affect.
    # So exclude display_name for idempotency.

    # Irrespective of the value we pass for display_name we get
    # "Remote boot attachment for instance" as the name in response model
    def get_exclude_attributes(self):
        return super(
            BootVolumeAttachmentHelperCustom, self
        ).get_exclude_attributes() + ["display_name"]


class ImageShapeCompatibilityEntryHelperCustom:
    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return True


class VnicAttachmentHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            VnicAttachmentHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # The VNIC details specified in create_vnic_details are not available in the vnic_attachment directly. It has
        # vnic_id which can be used to fetch the required information. So update the key name for create_vnic_details
        # in the create model. The vnic information is added to the existing resource with the same key in
        # get_existing_resource_dict_for_idempotence_check so that the idempotence logic compares the vnic details.
        if create_model_dict.get("create_vnic_details") is not None:
            create_model_dict["vnic"] = create_model_dict.pop("create_vnic_details")
        return create_model_dict

    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        existing_resource_dict = super(
            VnicAttachmentHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)
        if existing_resource_dict.get("vnic_id"):
            # The information provided in create_vnic_details attr of create model does not exist directly in the
            # get model but have to be fetched from the vnic details. Fetch and add the information to the existing
            # resource so that the idempotence logic can compare the vnic details.
            virtual_network_client = oci_config_utils.create_service_client(
                self.module, VirtualNetworkClient
            )
            existing_vnic = to_dict(
                virtual_network_client.get_vnic(
                    vnic_id=existing_resource_dict.get("vnic_id")
                ).data
            )
            existing_resource_dict["vnic"] = existing_vnic
        return existing_resource_dict


# currently using string comparison method
def is_windows_instance(instance_os):
    if instance_os is None:
        return False
    return "windows" in instance_os.lower()


def get_windows_iscsi_attach_commands(iqn, ipv4, chap_username, chap_secret):
    connection_command = "Connect-IscsiTarget -NodeAddress {0} -TargetPortalAddress {1}".format(
        iqn, ipv4
    )
    if chap_username:
        connection_command = (
            connection_command
            + "  -AuthenticationType ONEWAYCHAP -ChapUsername {0} -ChapSecret {1}".format(
                chap_username, chap_secret
            )
        )
    connection_command = connection_command + "  -IsPersistent $True"

    iscsi_attach_commands = [
        "Set-Service -Name msiscsi -StartupType Automatic",
        "Start-Service msiscsi",
        "New-IscsiTargetPortal -TargetPortalAddress {0}".format(ipv4),
        connection_command,
    ]

    return iscsi_attach_commands


def get_iscsi_attach_commands(volume_attachment, instance_os):
    if not volume_attachment.get("attachment_type") == "iscsi":
        return []
    iqn = volume_attachment.get("iqn")
    ipv4 = volume_attachment.get("ipv4")
    port = volume_attachment.get("port")
    chap_username = volume_attachment.get("chap_username")
    chap_secret = volume_attachment.get("chap_secret")

    # os specific commands
    if is_windows_instance(instance_os):
        iscsi_attach_commands = get_windows_iscsi_attach_commands(
            iqn, ipv4, chap_username, chap_secret
        )
    else:
        iscsi_attach_commands = [
            "sudo iscsiadm -m node -o new -T {0} -p {1}:{2}".format(iqn, ipv4, port),
            "sudo iscsiadm -m node -o update -T {0} -n node.startup -v automatic".format(
                iqn
            ),
        ]

        if chap_username:
            iscsi_attach_commands.extend(
                [
                    "sudo iscsiadm -m node -T {0} -p {1}:{2} -o update -n node.session.auth.authmethod -v CHAP".format(
                        iqn, ipv4, port
                    ),
                    "sudo iscsiadm -m node -T {0} -p {1}:{2} -o update -n node.session.auth.username -v {3}".format(
                        iqn, ipv4, port, chap_username
                    ),
                    "sudo iscsiadm -m node -T {0} -p {1}:{2} -o update -n node.session.auth.password -v {3}".format(
                        iqn, ipv4, port, chap_secret
                    ),
                ]
            )
        iscsi_attach_commands.append(
            "sudo iscsiadm -m node -T {0} -p {1}:{2} -l".format(iqn, ipv4, port)
        )

    return iscsi_attach_commands


def get_iscsi_detach_commands(volume_attachment, instance_os):
    if not volume_attachment.get("attachment_type") == "iscsi":
        return []

    if is_windows_instance(instance_os):
        return []

    return [
        "sudo iscsiadm -m node -T {0} -p {1}:{2} -u".format(
            volume_attachment.get("iqn"),
            volume_attachment.get("ipv4"),
            volume_attachment.get("port"),
        ),
        "sudo iscsiadm -m node -o delete -T {0}".format(volume_attachment.get("iqn")),
    ]


def with_iscsi_commands(volume_attachment, instance_os):
    if not volume_attachment:
        return volume_attachment

    attach_commands = get_iscsi_attach_commands(volume_attachment, instance_os)
    detach_commands = get_iscsi_detach_commands(volume_attachment, instance_os)

    volume_attachment["iscsi_attach_commands"] = attach_commands
    volume_attachment["iscsi_detach_commands"] = detach_commands
    return volume_attachment


def get_instance(compute_client, instance_id):
    return oci_common_utils.call_with_backoff(
        compute_client.get_instance, instance_id=instance_id,
    )


def get_image(compute_client, image_id):
    return oci_common_utils.call_with_backoff(
        compute_client.get_image, image_id=image_id,
    )


def get_instance_os(compute_client, instance_id):
    instance = get_instance(compute_client, instance_id)
    image = get_image(compute_client, getattr(instance.data, "image_id", None))
    operating_system = getattr(image.data, "operating_system", None)
    return operating_system


def with_os_iscsi_commands(compute_client, volume_attachment):
    instance_os = get_instance_os(compute_client, volume_attachment.get("instance_id"))
    return with_iscsi_commands(volume_attachment, instance_os)


class VolumeAttachmentHelperCustom:
    def prepare_result(self, *args, **kwargs):
        result = super(VolumeAttachmentHelperCustom, self).prepare_result(
            *args, **kwargs
        )
        if not result.get("volume_attachment"):
            return result
        result["volume_attachment"] = with_os_iscsi_commands(
            self.client, result["volume_attachment"]
        )
        return result

    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            VolumeAttachmentHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # get model has the attribute name "attachment_type" which defines the attachment type where as it "type" in
        # get model. So change the key name to avoid mismatch.
        create_model_dict["attachment_type"] = create_model_dict.pop("type", None)

        return create_model_dict


class VolumeAttachmentFactsHelperCustom:
    def get(self, *args, **kwargs):
        volume_attachment = super(VolumeAttachmentFactsHelperCustom, self).get(
            *args, **kwargs
        )
        return with_os_iscsi_commands(self.client, volume_attachment)

    def list(self, *args, **kwargs):
        return [
            with_iscsi_commands(volume_attachment, "Linux")
            for volume_attachment in super(
                VolumeAttachmentFactsHelperCustom, self
            ).list(*args, **kwargs)
        ]


# The subtypes of ImageCapabilitySchemaDescriptor model has parameters with the same name but different types.
# Below is the list of subtypes and parameters (with different types):
#   EnumStringImageCapabilitySchemaDescriptor -> values (list[str]), default_value (str)
#   EnumIntegerImageCapabilityDescriptor -> values (list[int]), default_value (int)
#   BooleanImageCapabilitySchemaDescriptor -> default_value (bool)
# We cannot use the original parameter names in the module since we need to specify the type of each parameter in the
# module. So the parameter names are changed and we have a parameter for each sub type. You can see the parameter name
# mapping in the function `get_updated_image_capabilities_schema_data_parameter_name`. The parameter names are changed
# using the renamingConfig (poms/core/renamingConfig.yaml).
# All the below customisations (related to image capabilities) are either to update the models before sending to sdk
# or to update the return properties after getting the results from sdk.
def get_updated_image_capabilities_schema_data_parameter_name(descriptor_type, param):
    param_descriptor_type_map = {
        ("enumstring", "values"): "enum_string_values",
        ("enumstring", "default_value"): "enum_string_default_value",
        ("enuminteger", "values"): "enum_integer_values",
        ("enuminteger", "default_value"): "enum_integer_default_value",
        ("boolean", "default_value"): "boolean_default_value",
    }
    return param_descriptor_type_map.get((descriptor_type, param), param)


def get_resource_with_updated_schema_data_param_names(resource):
    if resource and resource.get("schema_data"):
        resource["schema_data"] = dict(
            (
                schema_data_key,
                dict(
                    (
                        get_updated_image_capabilities_schema_data_parameter_name(
                            schema_data.get("descriptor_type"), k
                        ),
                        v,
                    )
                    for k, v in six.iteritems(schema_data)
                ),
            )
            for schema_data_key, schema_data in six.iteritems(resource["schema_data"])
        )
    return resource


class ComputeImageCapabilitySchemaHelperCustom:
    def __init__(self, *args, **kwargs):
        super(ComputeImageCapabilitySchemaHelperCustom, self).__init__(*args, **kwargs)
        if self.module.params.get("schema_data"):
            self.module.params["schema_data"] = dict(
                (
                    schema_data_key,
                    dict(
                        (self.get_original_sdk_parameter_name(k), v)
                        for k, v in six.iteritems(schema_data)
                    ),
                )
                for schema_data_key, schema_data in six.iteritems(
                    self.module.params.get("schema_data")
                )
            )

    def get_original_sdk_parameter_name(self, param):
        if param in ["enum_string_values", "enum_integer_values"]:
            return "values"
        if param in [
            "enum_string_default_value",
            "enum_integer_default_value",
            "boolean_default_value",
        ]:
            return "default_value"
        return param

    def prepare_result(self, changed, resource_type, resource=None, msg=None):
        result = super(ComputeImageCapabilitySchemaHelperCustom, self).prepare_result(
            changed, resource_type, resource, msg
        )
        result[resource_type] = get_resource_with_updated_schema_data_param_names(
            result[resource_type]
        )
        return result


class ComputeImageCapabilitySchemaFactsHelperCustom:
    def get(self):
        resource = super(ComputeImageCapabilitySchemaFactsHelperCustom, self).get()
        return get_resource_with_updated_schema_data_param_names(resource)


class ComputeGlobalImageCapabilitySchemaVersionFactsHelperCustom:
    def get(self):
        resource = super(
            ComputeGlobalImageCapabilitySchemaVersionFactsHelperCustom, self
        ).get()
        return get_resource_with_updated_schema_data_param_names(resource)


class InstanceActionsHelperCustom:
    def instance_action(self):
        if self.module.params.get("action_type") is not None:
            action_details = oci_common_utils.convert_input_data_to_model_class(
                self.module.params, InstancePowerActionDetails
            )
        else:
            # We always generate and set the body params in request and instance_power_action_details
            # is a body param. In this case, body param is optional and is only be set if action_type
            # is not None. API throws "Invalid typeId provided" error if action_type is sent None.
            # This is special case so, setting action_details to None.
            action_details = None
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.instance_action,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_id=self.module.params.get("instance_id"),
                action=self.module.params.get("action"),
                instance_power_action_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


class InstanceConsoleConnectionHelperCustom:
    def get_exclude_attributes(self):
        exclude_attriubtes = super(
            InstanceConsoleConnectionHelperCustom, self
        ).get_exclude_attributes()

        remove_exclude_attributes = ["public_key"]
        exclude_attriubtes = [
            x for x in exclude_attriubtes if x not in remove_exclude_attributes
        ]

        return exclude_attriubtes
