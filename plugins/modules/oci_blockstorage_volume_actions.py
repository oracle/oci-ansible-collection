#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_blockstorage_volume_actions
short_description: Perform actions on a Volume resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Volume resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a volume into a different compartment within the same tenancy.
      For information about moving resources between compartments,
      see L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    volume_id:
        description:
            - The OCID of the volume.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the volume to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Volume.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on volume
  oci_blockstorage_volume_actions:
    # required
    volume_id: "ocid1.volume.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
volume:
    description:
        - Details of the Volume resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain of the volume.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
        id:
            description:
                - The OCID of the volume.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_hydrated:
            description:
                - Specifies whether the cloned volume's data has finished copying from the source volume or backup.
            returned: on success
            type: bool
            sample: true
        kms_key_id:
            description:
                - The OCID of the Vault service key which is the master encryption key for the volume.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of a volume.
            returned: on success
            type: str
            sample: PROVISIONING
        vpus_per_gb:
            description:
                - The number of volume performance units (VPUs) that will be applied to this volume per GB,
                  representing the Block Volume service's elastic performance options.
                  See L(Block Volume Performance Levels,https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for
                  more information.
                - "Allowed values:"
                - " * `0`: Represents Lower Cost option."
                - " * `10`: Represents Balanced option."
                - " * `20`: Represents Higher Performance option."
                - " * `30`-`120`: Represents the Ultra High Performance option."
                - For performance autotune enabled volumes, It would be the Default(Minimum) VPUs/GB.
            returned: on success
            type: int
            sample: 56
        size_in_gbs:
            description:
                - The size of the volume in GBs.
            returned: on success
            type: int
            sample: 56
        size_in_mbs:
            description:
                - The size of the volume in MBs. This field is deprecated. Use
                  sizeInGBs instead.
            returned: on success
            type: int
            sample: 56
        source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: blockVolumeReplica
                id:
                    description:
                        - The OCID of the block volume replica.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the volume was created. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        volume_group_id:
            description:
                - The OCID of the source volume group.
            returned: on success
            type: str
            sample: "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx"
        is_auto_tune_enabled:
            description:
                - Specifies whether the auto-tune performance is enabled for this volume. This field is deprecated.
                  Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
            returned: on success
            type: bool
            sample: true
        auto_tuned_vpus_per_gb:
            description:
                - The number of Volume Performance Units per GB that this volume is effectively tuned to.
            returned: on success
            type: int
            sample: 56
        block_volume_replicas:
            description:
                - The list of block volume replicas of this volume.
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                block_volume_replica_id:
                    description:
                        - The block volume replica's Oracle ID (OCID).
                    returned: on success
                    type: str
                    sample: "ocid1.blockvolumereplica.oc1..xxxxxxEXAMPLExxxxxx"
                availability_domain:
                    description:
                        - The availability domain of the block volume replica.
                        - "Example: `Uocm:PHX-AD-1`"
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
        autotune_policies:
            description:
                - The list of autotune policies enabled for this volume.
            returned: on success
            type: complex
            contains:
                autotune_type:
                    description:
                        - This specifies the type of autotunes supported by OCI.
                    returned: on success
                    type: str
                    sample: DETACHED_VOLUME
                max_vpus_per_gb:
                    description:
                        - This will be the maximum VPUs/GB performance level that the volume will be auto-tuned
                          temporarily based on performance monitoring.
                    returned: on success
                    type: int
                    sample: 56
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "system_tags": {},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_hydrated": true,
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "vpus_per_gb": 56,
        "size_in_gbs": 56,
        "size_in_mbs": 56,
        "source_details": {
            "type": "blockVolumeReplica",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "volume_group_id": "ocid1.volumegroup.oc1..xxxxxxEXAMPLExxxxxx",
        "is_auto_tune_enabled": true,
        "auto_tuned_vpus_per_gb": 56,
        "block_volume_replicas": [{
            "display_name": "display_name_example",
            "block_volume_replica_id": "ocid1.blockvolumereplica.oc1..xxxxxxEXAMPLExxxxxx",
            "availability_domain": "Uocm:PHX-AD-1"
        }],
        "autotune_policies": [{
            "autotune_type": "DETACHED_VOLUME",
            "max_vpus_per_gb": 56
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.core import BlockstorageClient
    from oci.core.models import ChangeVolumeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "volume_id"

    def get_module_resource_id(self):
        return self.module.params.get("volume_id")

    def get_get_fn(self):
        return self.client.get_volume

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume, volume_id=self.module.params.get("volume_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVolumeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_volume_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                volume_id=self.module.params.get("volume_id"),
                change_volume_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
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


VolumeActionsHelperCustom = get_custom_class("VolumeActionsHelperCustom")


class ResourceHelper(VolumeActionsHelperCustom, VolumeActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            volume_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
