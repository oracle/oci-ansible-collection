#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_network_cross_connect_group_facts
short_description: Fetches details about one or multiple CrossConnectGroup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CrossConnectGroup resources in Oracle Cloud Infrastructure
    - Lists the cross-connect groups in the specified compartment.
    - If I(cross_connect_group_id) is specified, the details of a single CrossConnectGroup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cross_connect_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cross-connect group.
            - Required to get a specific cross_connect_group.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple cross_connect_groups.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle
              state. The value is case insensitive.
        type: str
        choices:
            - "PROVISIONING"
            - "PROVISIONED"
            - "INACTIVE"
            - "TERMINATING"
            - "TERMINATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific cross_connect_group
  oci_network_cross_connect_group_facts:
    # required
    cross_connect_group_id: "ocid1.crossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx"

- name: List cross_connect_groups
  oci_network_cross_connect_group_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING

"""

RETURN = """
cross_connect_groups:
    description:
        - List of CrossConnectGroup resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the cross-connect group.
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
        id:
            description:
                - The cross-connect group's Oracle ID (OCID).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The cross-connect group's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        customer_reference_name:
            description:
                - A reference name or identifier for the physical fiber connection that this cross-connect
                  group uses.
            returned: on success
            type: str
            sample: customer_reference_name_example
        time_created:
            description:
                - The date and time the cross-connect group was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        macsec_properties:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                state:
                    description:
                        - Indicates whether or not MACsec is enabled.
                    returned: on success
                    type: str
                    sample: ENABLED
                primary_key:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        connectivity_association_name_secret_id:
                            description:
                                - Secret L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity
                                  association Key Name (CKN) of this MACsec key.
                            returned: on success
                            type: str
                            sample: "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx"
                        connectivity_association_name_secret_version:
                            description:
                                - The secret version of the connectivity association name secret in Vault.
                            returned: on success
                            type: int
                            sample: 56
                        connectivity_association_key_secret_id:
                            description:
                                - Secret L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) containing the Connectivity
                                  Association Key (CAK) of this MACsec key.
                            returned: on success
                            type: str
                            sample: "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx"
                        connectivity_association_key_secret_version:
                            description:
                                - The secret version of the `connectivityAssociationKey` secret in Vault.
                            returned: on success
                            type: int
                            sample: 56
                encryption_cipher:
                    description:
                        - Type of encryption cipher suite to use for the MACsec connection.
                    returned: on success
                    type: str
                    sample: AES128_GCM
        oci_physical_device_name:
            description:
                - The FastConnect device that terminates the physical connection.
            returned: on success
            type: str
            sample: oci_physical_device_name_example
        oci_logical_device_name:
            description:
                - The FastConnect device that terminates the logical connection.
                  This device might be different than the device that terminates the physical connection.
            returned: on success
            type: str
            sample: oci_logical_device_name_example
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "customer_reference_name": "customer_reference_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "macsec_properties": {
            "state": "ENABLED",
            "primary_key": {
                "connectivity_association_name_secret_id": "ocid1.connectivityassociationnamesecret.oc1..xxxxxxEXAMPLExxxxxx",
                "connectivity_association_name_secret_version": 56,
                "connectivity_association_key_secret_id": "ocid1.connectivityassociationkeysecret.oc1..xxxxxxEXAMPLExxxxxx",
                "connectivity_association_key_secret_version": 56
            },
            "encryption_cipher": "AES128_GCM"
        },
        "oci_physical_device_name": "oci_physical_device_name_example",
        "oci_logical_device_name": "oci_logical_device_name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CrossConnectGroupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "cross_connect_group_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cross_connect_group,
            cross_connect_group_id=self.module.params.get("cross_connect_group_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_cross_connect_groups,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


CrossConnectGroupFactsHelperCustom = get_custom_class(
    "CrossConnectGroupFactsHelperCustom"
)


class ResourceFactsHelper(
    CrossConnectGroupFactsHelperCustom, CrossConnectGroupFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cross_connect_group_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "PROVISIONED",
                    "INACTIVE",
                    "TERMINATING",
                    "TERMINATED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cross_connect_group",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(cross_connect_groups=result)


if __name__ == "__main__":
    main()
