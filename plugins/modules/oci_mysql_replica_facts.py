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
module: oci_mysql_replica_facts
short_description: Fetches details about one or multiple Replica resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Replica resources in Oracle Cloud Infrastructure
    - Lists all the read replicas that match the specified filters.
    - If I(replica_id) is specified, the details of a single Replica will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple replicas.
        type: str
    display_name:
        description:
            - A filter to return only the resource matching the given display name exactly.
        type: str
        aliases: ["name"]
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    lifecycle_state:
        description:
            - The LifecycleState of the read replica.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "NEEDS_ATTENTION"
            - "FAILED"
    replica_id:
        description:
            - The Replica L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific replica.
        type: str
        aliases: ["id"]
    configuration_id:
        description:
            - The requested Configuration instance.
        type: str
    is_up_to_date:
        description:
            - Filter instances if they are using the latest revision of the
              Configuration they are associated with.
        type: bool
    sort_by:
        description:
            - The field to sort by. You can sort by one field only. By default, the Time field is sorted in descending order and the Display Name field in
              ascending order.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use (ASC or DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific replica
  oci_mysql_replica_facts:
    # required
    replica_id: "ocid1.replica.oc1..xxxxxxEXAMPLExxxxxx"

- name: List replicas
  oci_mysql_replica_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    replica_id: "ocid1.replica.oc1..xxxxxxEXAMPLExxxxxx"
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    is_up_to_date: true
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
replicas:
    description:
        - List of Replica resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the read replica.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_id:
            description:
                - The OCID of the DB System the read replica is associated with.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that contains the read replica.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the read replica. It does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User provided description of the read replica.
            returned: on success
            type: str
            sample: description_example
        lifecycle_state:
            description:
                - The state of the read replica.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the state of the read replica.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the read replica was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the read replica was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        mysql_version:
            description:
                - The MySQL version currently in use by the read replica.
            returned: on success
            type: str
            sample: mysql_version_example
        availability_domain:
            description:
                - The name of the Availability Domain the read replica is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - The name of the Fault Domain the read replica is located in.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        ip_address:
            description:
                - The IP address the read replica is configured to listen on.
            returned: on success
            type: str
            sample: ip_address_example
        port:
            description:
                - The port the read replica is configured to listen on.
            returned: on success
            type: int
            sample: 56
        port_x:
            description:
                - The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_delete_protected:
            description:
                - Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow.
                  Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If
                  the DB System is delete protected, read replicas can still be deleted individually if they are not delete
                  protected themselves.
            returned: on success
            type: bool
            sample: true
        shape_name:
            description:
                - "The shape currently in use by the read replica. The shape determines the resources allocated:
                  CPU cores and memory for VM shapes, CPU cores, memory and storage for non-VM (bare metal) shapes.
                  To get a list of shapes, use the L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/mysql/20190415/ShapeSummary/ListShapes)
                  operation."
            returned: on success
            type: str
            sample: shape_name_example
        configuration_id:
            description:
                - The OCID of the Configuration currently in use by the read replica.
            returned: on success
            type: str
            sample: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
        replica_overrides:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                mysql_version:
                    description:
                        - The MySQL version to be used by the read replica.
                    returned: on success
                    type: str
                    sample: mysql_version_example
                shape_name:
                    description:
                        - "The shape to be used by the read replica. The shape determines the resources allocated:
                          CPU cores and memory for VM shapes, CPU cores, memory and storage for non-VM (bare metal) shapes.
                          To get a list of shapes, use the L(ListShapes,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/mysql/20190415/ShapeSummary/ListShapes) operation."
                    returned: on success
                    type: str
                    sample: shape_name_example
                configuration_id:
                    description:
                        - The OCID of the Configuration to be used by the read replica.
                    returned: on success
                    type: str
                    sample: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "mysql_version": "mysql_version_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domain": "FAULT-DOMAIN-1",
        "ip_address": "ip_address_example",
        "port": 56,
        "port_x": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_delete_protected": true,
        "shape_name": "shape_name_example",
        "configuration_id": "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx",
        "replica_overrides": {
            "mysql_version": "mysql_version_example",
            "shape_name": "shape_name_example",
            "configuration_id": "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.mysql import ReplicasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlReplicaFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "replica_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replica, replica_id=self.module.params.get("replica_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "db_system_id",
            "lifecycle_state",
            "replica_id",
            "configuration_id",
            "is_up_to_date",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_replicas,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MysqlReplicaFactsHelperCustom = get_custom_class("MysqlReplicaFactsHelperCustom")


class ResourceFactsHelper(MysqlReplicaFactsHelperCustom, MysqlReplicaFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            db_system_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "NEEDS_ATTENTION",
                    "FAILED",
                ],
            ),
            replica_id=dict(aliases=["id"], type="str"),
            configuration_id=dict(type="str"),
            is_up_to_date=dict(type="bool"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="replica",
        service_client_class=ReplicasClient,
        namespace="mysql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(replicas=result)


if __name__ == "__main__":
    main()
