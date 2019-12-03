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
module: oci_autonomous_exadata_infrastructure
short_description: Manage an AutonomousExadataInfrastructure resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AutonomousExadataInfrastructure resource in Oracle Cloud Infrastructure
    - For I(state=present), launches a new Autonomous Exadata Infrastructure in the specified compartment and availability domain.
version_added: "2.5"
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment the Autonomous Exadata Infrastructure
              belongs in.
            - Required for create using I(state=present).
    display_name:
        description:
            - The user-friendly name for the Autonomous Exadata Infrastructure. It does not have to be unique.
        aliases: ["name"]
    availability_domain:
        description:
            - The availability domain where the Autonomous Exadata Infrastructure is located.
            - Required for create using I(state=present).
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the Autonomous Exadata Infrastructure is
              associated with.
            - "**Subnet Restrictions:**
              - For Autonomous Exadata Infrastructures, do not use a subnet that overlaps with 192.168.128.0/20"
            - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
              Specifying an overlapping subnet will cause the private interconnect to malfunction.
              This restriction applies to both the client subnet and backup subnet.
            - Required for create using I(state=present).
    shape:
        description:
            - The shape of the Autonomous Exadata Infrastructure. The shape determines resources allocated to the Autonomous Exadata Infrastructure (CPU cores,
              memory and storage). To get a list of shapes, use the ListDbSystemShapes operation.
            - Required for create using I(state=present).
    hostname:
        description:
            - The host name for the Autonomous Exadata Infrastructure. The host name must begin with an alphabetic character and
              can contain a maximum of 30 alphanumeric characters, including hyphens (-).
            - The maximum length of the combined hostname and domain is 63 characters.
            - "**Note:** The hostname must be unique within the subnet. If it is not unique,
              the Autonomous Exadata Infrastructure will fail to provision."
    domain:
        description:
            - A domain name used for the Autonomous Exadata Infrastructure. If the Oracle-provided Internet and VCN
              Resolver is enabled for the specified subnet, the domain name for the subnet is used
              (don't provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.
    license_model:
        description:
            - The Oracle license model that applies to all the databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    maintenance_window_details:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            day_of_week:
                description:
                    - Day of the week that the patch should be applied to the Autonomous Exadata Infrastructure. Patches are applied during the first week of
                      the quarter.
                choices:
                    - "ANY"
                    - "SUNDAY"
                    - "MONDAY"
                    - "TUESDAY"
                    - "WEDNESDAY"
                    - "THURSDAY"
                    - "FRIDAY"
                    - "SATURDAY"
                required: true
            hour_of_day:
                description:
                    - Hour of the day that the patch should be applied.
                type: int
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    autonomous_exadata_infrastructure_id:
        description:
            - The Autonomous Exadata Infrastructure  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present), I(state=absent).
        aliases: ["id"]
    state:
        description:
            - The state of the AutonomousExadataInfrastructure.
            - Use I(state=present) to create or update an AutonomousExadataInfrastructure.
            - Use I(state=absent) to delete an AutonomousExadataInfrastructure.
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create autonomous_exadata_infrastructure
  oci_autonomous_exadata_infrastructure:
      compartment_id: ocid1.tenancy.oc1.<var>&lt;unique_ID&gt;</var>
      display_name: tst3dbsys
      availability_domain: Uocm:PHX-AD-1
      subnet_id: ocid1.subnet.oc1.<var>&lt;unique_ID&gt;</var>
      shape: Exadata.Half1.168
      hostname: athena
      domain: my.company.com

- name: Update autonomous_exadata_infrastructure
  oci_autonomous_exadata_infrastructure:
      display_name: new displayname
      autonomous_exadata_infrastructure_id: ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete autonomous_exadata_infrastructure
  oci_autonomous_exadata_infrastructure:
      autonomous_exadata_infrastructure_id: ocid1.autonomousexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx
      state: absent

"""

RETURN = """
autonomous_exadata_infrastructure:
    description:
        - Details of the AutonomousExadataInfrastructure resource acted upon by the current operation
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
    sample: {
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient
    from oci.database.models import LaunchAutonomousExadataInfrastructureDetails
    from oci.database.models import UpdateAutonomousExadataInfrastructureDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousExadataInfrastructureHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    @staticmethod
    def get_module_resource_id_param():
        return "autonomous_exadata_infrastructure_id"

    def get_module_resource_id(self):
        return self.module.params.get("autonomous_exadata_infrastructure_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_exadata_infrastructure,
            autonomous_exadata_infrastructure_id=self.module.params.get(
                "autonomous_exadata_infrastructure_id"
            ),
        )

    def list_resources(self):
        list_method_params = ["compartment_id"]

        kwargs = dict(
            (param, self.module.params[param])
            for param in list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_exadata_infrastructures, **kwargs
        )

    def get_create_model_class(self):
        return LaunchAutonomousExadataInfrastructureDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_common_utils.call_with_backoff(
            self.client.launch_autonomous_exadata_infrastructure,
            launch_autonomous_exadata_infrastructure_details=create_details,
        )

    def get_update_model_class(self):
        return UpdateAutonomousExadataInfrastructureDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_autonomous_exadata_infrastructure,
            autonomous_exadata_infrastructure_id=self.module.params.get(
                "autonomous_exadata_infrastructure_id"
            ),
            update_autonomous_exadata_infrastructures_details=update_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.terminate_autonomous_exadata_infrastructure,
            autonomous_exadata_infrastructure_id=self.module.params.get(
                "autonomous_exadata_infrastructure_id"
            ),
        )


AutonomousExadataInfrastructureHelperCustom = get_custom_class(
    "AutonomousExadataInfrastructureHelperCustom"
)


class ResourceHelper(
    AutonomousExadataInfrastructureHelperCustom,
    AutonomousExadataInfrastructureHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            availability_domain=dict(type="str"),
            subnet_id=dict(type="str"),
            shape=dict(type="str"),
            hostname=dict(type="str"),
            domain=dict(type="str"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            maintenance_window_details=dict(
                type="dict",
                options=dict(
                    day_of_week=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ANY",
                            "SUNDAY",
                            "MONDAY",
                            "TUESDAY",
                            "WEDNESDAY",
                            "THURSDAY",
                            "FRIDAY",
                            "SATURDAY",
                        ],
                    ),
                    hour_of_day=dict(type="int"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            autonomous_exadata_infrastructure_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_exadata_infrastructure",
        service_client_class=DatabaseClient,
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
