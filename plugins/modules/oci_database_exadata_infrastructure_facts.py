#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_database_exadata_infrastructure_facts
short_description: Fetches details about one or multiple ExadataInfrastructure resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExadataInfrastructure resources in Oracle Cloud Infrastructure
    - Gets a list of the Exadata Cloud@Customer infrastructure resources in the specified compartment.
    - If I(exadata_infrastructure_id) is specified, the details of a single ExadataInfrastructure will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    exadata_infrastructure_id:
        description:
            - The Exadata infrastructure L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific exadata_infrastructure.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple exadata_infrastructures.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "CREATING"
            - "REQUIRES_ACTIVATION"
            - "ACTIVATING"
            - "ACTIVE"
            - "ACTIVATION_FAILED"
            - "FAILED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "DISCONNECTED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List exadata_infrastructures
  oci_database_exadata_infrastructure_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific exadata_infrastructure
  oci_database_exadata_infrastructure_facts:
    exadata_infrastructure_id: ocid1.exadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
exadata_infrastructures:
    description:
        - List of ExadataInfrastructure resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current lifecycle state of the Exadata infrastructure.
            returned: on success
            type: string
            sample: CREATING
        display_name:
            description:
                - The user-friendly name for the Exadata Cloud@Customer infrastructure. The name does not need to be unique.
            returned: on success
            type: string
            sample: display_name_example
        shape:
            description:
                - The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.
            returned: on success
            type: string
            sample: shape_example
        time_zone:
            description:
                - The time zone of the Exadata infrastructure. For details, see L(Exadata Infrastructure Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: string
            sample: time_zone_example
        cpus_enabled:
            description:
                - The number of enabled CPU cores.
            returned: on success
            type: int
            sample: 56
        max_cpu_count:
            description:
                - The total number of CPU cores available.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The memory allocated in GBs.
            returned: on success
            type: int
            sample: 56
        max_memory_in_gbs:
            description:
                - The total memory available in GBs.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The local node storage allocated in GBs.
            returned: on success
            type: int
            sample: 56
        max_db_node_storage_in_g_bs:
            description:
                - The total local node storage available in GBs.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - Size, in terabytes, of the DATA disk group.
            returned: on success
            type: float
            sample: 1.2
        max_data_storage_in_t_bs:
            description:
                - The total available DATA disk group size.
            returned: on success
            type: float
            sample: 1.2
        cloud_control_plane_server1:
            description:
                - The IP address for the first control plane server.
            returned: on success
            type: string
            sample: cloud_control_plane_server1_example
        cloud_control_plane_server2:
            description:
                - The IP address for the second control plane server.
            returned: on success
            type: string
            sample: cloud_control_plane_server2_example
        netmask:
            description:
                - The netmask for the control plane network.
            returned: on success
            type: string
            sample: netmask_example
        gateway:
            description:
                - The gateway for the control plane network.
            returned: on success
            type: string
            sample: gateway_example
        admin_network_cidr:
            description:
                - The CIDR block for the Exadata administration network.
            returned: on success
            type: string
            sample: admin_network_cidr_example
        infini_band_network_cidr:
            description:
                - The CIDR block for the Exadata InfiniBand interconnect.
            returned: on success
            type: string
            sample: infini_band_network_cidr_example
        corporate_proxy:
            description:
                - The corporate network proxy for access to the control plane network.
            returned: on success
            type: string
            sample: corporate_proxy_example
        dns_server:
            description:
                - The list of DNS server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        ntp_server:
            description:
                - The list of NTP server IP addresses. Maximum of 3 allowed.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the Exadata infrastructure was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        csi_number:
            description:
                - The CSI Number of the Exadata infrastructure.
            returned: on success
            type: string
            sample: csi_number_example
        contacts:
            description:
                - The list of contacts for the Exadata infrastructure.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the Exadata Infrastructure contact.
                    returned: on success
                    type: string
                    sample: name_example
                phone_number:
                    description:
                        - The phone number for the Exadata Infrastructure contact.
                    returned: on success
                    type: string
                    sample: phone_number_example
                email:
                    description:
                        - The email for the Exadata Infrastructure contact.
                    returned: on success
                    type: string
                    sample: email_example
                is_primary:
                    description:
                        - True, if this Exadata Infrastructure contact is a primary contact. False, if this Exadata Infrastructure is a secondary contact.
                    returned: on success
                    type: bool
                    sample: true
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "shape": "shape_example",
        "time_zone": "time_zone_example",
        "cpus_enabled": 56,
        "max_cpu_count": 56,
        "memory_size_in_gbs": 56,
        "max_memory_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "max_db_node_storage_in_g_bs": 56,
        "data_storage_size_in_tbs": 1.2,
        "max_data_storage_in_t_bs": 1.2,
        "cloud_control_plane_server1": "cloud_control_plane_server1_example",
        "cloud_control_plane_server2": "cloud_control_plane_server2_example",
        "netmask": "netmask_example",
        "gateway": "gateway_example",
        "admin_network_cidr": "admin_network_cidr_example",
        "infini_band_network_cidr": "infini_band_network_cidr_example",
        "corporate_proxy": "corporate_proxy_example",
        "dns_server": [],
        "ntp_server": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "csi_number": "csi_number_example",
        "contacts": [{
            "name": "name_example",
            "phone_number": "phone_number_example",
            "email": "email_example",
            "is_primary": true
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExadataInfrastructureFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "exadata_infrastructure_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_exadata_infrastructure,
            exadata_infrastructure_id=self.module.params.get(
                "exadata_infrastructure_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_exadata_infrastructures,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ExadataInfrastructureFactsHelperCustom = get_custom_class(
    "ExadataInfrastructureFactsHelperCustom"
)


class ResourceFactsHelper(
    ExadataInfrastructureFactsHelperCustom, ExadataInfrastructureFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "REQUIRES_ACTIVATION",
                    "ACTIVATING",
                    "ACTIVE",
                    "ACTIVATION_FAILED",
                    "FAILED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "DISCONNECTED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="exadata_infrastructure",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(exadata_infrastructures=result)


if __name__ == "__main__":
    main()
