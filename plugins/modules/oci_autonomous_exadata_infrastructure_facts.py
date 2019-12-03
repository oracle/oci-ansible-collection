#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_autonomous_exadata_infrastructure_facts
short_description: Fetches details about one or multiple AutonomousExadataInfrastructure resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousExadataInfrastructure resources in Oracle Cloud Infrastructure
    - Gets a list of the Autonomous Exadata Infrastructures in the specified compartment.
    - If I(autonomous_exadata_infrastructure_id) is specified, the details of a single AutonomousExadataInfrastructure will be returned.
version_added: "2.5"
options:
    autonomous_exadata_infrastructure_id:
        description:
            - The Autonomous Exadata Infrastructure  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific autonomous_exadata_infrastructure.
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple autonomous_exadata_infrastructures.
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME
              is ascending. The DISPLAYNAME sort order is case sensitive.
            - " **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted."
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "TERMINATING"
            - "TERMINATED"
            - "FAILED"
    availability_domain:
        description:
            - A filter to return only resources that match the given availability domain exactly.
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        aliases: ["name"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: List autonomous_exadata_infrastructures
  oci_autonomous_exadata_infrastructure_facts:
      compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific autonomous_exadata_infrastructure
  oci_autonomous_exadata_infrastructure_facts:
      autonomous_exadata_infrastructure_id: ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
autonomous_exadata_infrastructures:
    description:
        - List of AutonomousExadataInfrastructure resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Autonomous Exadata Infrastructure.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name for the Autonomous Exadata Infrastructure.
            returned: on success
            type: string
            sample: display_name_example
        availability_domain:
            description:
                - The name of the availability domain that the Autonomous Exadata Infrastructure is located in.
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        subnet_id:
            description:
                - The OCID of the subnet the Autonomous Exadata Infrastructure is associated with.
                - "**Subnet Restrictions:**
                  - For Autonomous Databases with Autonomous Exadata Infrastructure, do not use a subnet that overlaps with 192.168.128.0/20"
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and backup subnet.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        shape:
            description:
                - The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU
                  cores, memory and storage).
            returned: on success
            type: string
            sample: shape_example
        hostname:
            description:
                - The host name for the Autonomous Exadata Infrastructure node.
            returned: on success
            type: string
            sample: hostname_example
        domain:
            description:
                - The domain name for the Autonomous Exadata Infrastructure.
            returned: on success
            type: string
            sample: domain_example
        lifecycle_state:
            description:
                - The current lifecycle state of the Autonomous Exadata Infrastructure.
            returned: on success
            type: string
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state of the Autonomous Exadata Infrastructure.
            returned: on success
            type: string
            sample: lifecycle_details_example
        license_model:
            description:
                - The Oracle license model that applies to all databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.
            returned: on success
            type: string
            sample: LICENSE_INCLUDED
        time_created:
            description:
                - The date and time the Autonomous Exadata Infrastructure was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                day_of_week:
                    description:
                        - Day of the week that the patch should be applied to the Autonomous Exadata Infrastructure. Patches are applied during the first week
                          of the quarter.
                    returned: on success
                    type: string
                    sample: ANY
                hour_of_day:
                    description:
                        - Hour of the day that the patch should be applied.
                    returned: on success
                    type: int
                    sample: 56
        last_maintenance_run:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the Maintenance Run.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                compartment_id:
                    description:
                        - The OCID of the compartment.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - The user-friendly name for the Maintenance Run.
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - The text describing this Maintenance Run.
                    returned: on success
                    type: string
                    sample: description_example
                lifecycle_state:
                    description:
                        - The current state of the Maintenance Run.
                    returned: on success
                    type: string
                    sample: SCHEDULED
                lifecycle_details:
                    description:
                        - Additional information about the current lifecycleState.
                    returned: on success
                    type: string
                    sample: lifecycle_details_example
                time_scheduled:
                    description:
                        - The date and time the Maintenance Run is scheduled for.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_started:
                    description:
                        - The date and time the Maintenance Run starts.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_ended:
                    description:
                        - The date and time the Maintenance Run was completed.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                target_resource_type:
                    description:
                        - The type of the target resource on which the Maintenance Run occurs.
                    returned: on success
                    type: string
                    sample: AUTONOMOUS_DBSYSTEM
                target_resource_id:
                    description:
                        - The ID of the target resource on which the Maintenance Run occurs.
                    returned: on success
                    type: string
                    sample: ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx
                maintenance_type:
                    description:
                        - Maintenance type.
                    returned: on success
                    type: string
                    sample: PLANNED
                maintenance_subtype:
                    description:
                        - Maintenance sub-type.
                    returned: on success
                    type: string
                    sample: QUARTERLY
        next_maintenance_run:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the Maintenance Run.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                compartment_id:
                    description:
                        - The OCID of the compartment.
                    returned: on success
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - The user-friendly name for the Maintenance Run.
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - The text describing this Maintenance Run.
                    returned: on success
                    type: string
                    sample: description_example
                lifecycle_state:
                    description:
                        - The current state of the Maintenance Run.
                    returned: on success
                    type: string
                    sample: SCHEDULED
                lifecycle_details:
                    description:
                        - Additional information about the current lifecycleState.
                    returned: on success
                    type: string
                    sample: lifecycle_details_example
                time_scheduled:
                    description:
                        - The date and time the Maintenance Run is scheduled for.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_started:
                    description:
                        - The date and time the Maintenance Run starts.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_ended:
                    description:
                        - The date and time the Maintenance Run was completed.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                target_resource_type:
                    description:
                        - The type of the target resource on which the Maintenance Run occurs.
                    returned: on success
                    type: string
                    sample: AUTONOMOUS_DBSYSTEM
                target_resource_id:
                    description:
                        - The ID of the target resource on which the Maintenance Run occurs.
                    returned: on success
                    type: string
                    sample: ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx
                maintenance_type:
                    description:
                        - Maintenance type.
                    returned: on success
                    type: string
                    sample: PLANNED
                maintenance_subtype:
                    description:
                        - Maintenance sub-type.
                    returned: on success
                    type: string
                    sample: QUARTERLY
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {Department: Finance}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {Operations: {CostCenter: US}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "shape": "shape_example",
        "hostname": "hostname_example",
        "domain": "domain_example",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "license_model": "LICENSE_INCLUDED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "maintenance_window": {
            "day_of_week": "ANY",
            "hour_of_day": 56
        },
        "last_maintenance_run": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "lifecycle_state": "SCHEDULED",
            "lifecycle_details": "lifecycle_details_example",
            "time_scheduled": "2013-10-20T19:20:30+01:00",
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_ended": "2013-10-20T19:20:30+01:00",
            "target_resource_type": "AUTONOMOUS_DBSYSTEM",
            "target_resource_id": "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx",
            "maintenance_type": "PLANNED",
            "maintenance_subtype": "QUARTERLY"
        },
        "next_maintenance_run": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "lifecycle_state": "SCHEDULED",
            "lifecycle_details": "lifecycle_details_example",
            "time_scheduled": "2013-10-20T19:20:30+01:00",
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_ended": "2013-10-20T19:20:30+01:00",
            "target_resource_type": "AUTONOMOUS_DBSYSTEM",
            "target_resource_id": "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx",
            "maintenance_type": "PLANNED",
            "maintenance_subtype": "QUARTERLY"
        },
        "freeform_tags": {Department: Finance},
        "defined_tags": {Operations: {CostCenter: US}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousExadataInfrastructureFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return ["autonomous_exadata_infrastructure_id"]

    def get_required_params_for_list(self):
        return ["compartment_id"]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_exadata_infrastructure,
            autonomous_exadata_infrastructure_id=self.module.params.get(
                "autonomous_exadata_infrastructure_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "availability_domain",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_exadata_infrastructures,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AutonomousExadataInfrastructureFactsHelperCustom = get_custom_class(
    "AutonomousExadataInfrastructureFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousExadataInfrastructureFactsHelperCustom,
    AutonomousExadataInfrastructureFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            autonomous_exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "TERMINATING",
                    "TERMINATED",
                    "FAILED",
                ],
            ),
            availability_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_exadata_infrastructure",
        service_client_class=DatabaseClient,
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_exadata_infrastructures=result)


if __name__ == "__main__":
    main()
