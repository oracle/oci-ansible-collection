#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_application_vip_facts
short_description: Fetches details about one or multiple ApplicationVip resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ApplicationVip resources in Oracle Cloud Infrastructure
    - Gets a list of application virtual IP (VIP) addresses on a cloud VM cluster.
    - If I(application_vip_id) is specified, the details of a single ApplicationVip will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    application_vip_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the application virtual IP (VIP) address.
            - Required to get a specific application_vip.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple application_vips.
        type: str
    cloud_vm_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud VM cluster associated with the application virtual
              IP (VIP) address.
            - Required to list multiple application_vips.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for TIMECREATED is descending.
              Default order for DISPLAYNAME is ascending.
              The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "DISPLAYNAME"
            - "TIMECREATED"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "TERMINATING"
            - "TERMINATED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific application_vip
  oci_database_application_vip_facts:
    # required
    application_vip_id: "ocid1.applicationvip.oc1..xxxxxxEXAMPLExxxxxx"

- name: List application_vips
  oci_database_application_vip_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: DISPLAYNAME
    lifecycle_state: PROVISIONING

"""

RETURN = """
application_vips:
    description:
        - List of ApplicationVip resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        cloud_vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud VM cluster associated with the application
                  virtual IP (VIP) address.
            returned: on success
            type: str
            sample: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet associated with the application virtual IP
                  (VIP) address.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: ip_address_example
        hostname_label:
            description:
                - The hostname of the application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: hostname_label_example
        lifecycle_state:
            description:
                - The current lifecycle state of the application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the application virtual IP (VIP) address.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_assigned:
            description:
                - The date and time when the create operation for the application virtual IP (VIP) address completed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "cloud_vm_cluster_id": "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "ip_address_example",
        "hostname_label": "hostname_label_example",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "time_assigned": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApplicationVipFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "application_vip_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "cloud_vm_cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_application_vip,
            application_vip_id=self.module.params.get("application_vip_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_application_vips,
            compartment_id=self.module.params.get("compartment_id"),
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
            **optional_kwargs
        )


ApplicationVipFactsHelperCustom = get_custom_class("ApplicationVipFactsHelperCustom")


class ResourceFactsHelper(
    ApplicationVipFactsHelperCustom, ApplicationVipFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            application_vip_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            cloud_vm_cluster_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["DISPLAYNAME", "TIMECREATED"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "TERMINATING",
                    "TERMINATED",
                    "FAILED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="application_vip",
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

    module.exit_json(application_vips=result)


if __name__ == "__main__":
    main()
