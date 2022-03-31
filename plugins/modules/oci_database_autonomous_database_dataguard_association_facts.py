#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_database_autonomous_database_dataguard_association_facts
short_description: Fetches details about one or multiple AutonomousDatabaseDataguardAssociation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutonomousDatabaseDataguardAssociation resources in Oracle Cloud Infrastructure
    - Gets a list of the Autonomous Data Guard-enabled databases associated with the specified Autonomous Database.
    - If I(autonomous_database_dataguard_association_id) is specified, the details of a single AutonomousDatabaseDataguardAssociation will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    autonomous_database_dataguard_association_id:
        description:
            - The Autonomous Container Database-Autonomous Data Guard association
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific autonomous_database_dataguard_association.
        type: str
        aliases: ["id"]
    autonomous_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific autonomous_database_dataguard_association
  oci_database_autonomous_database_dataguard_association_facts:
    # required
    autonomous_database_dataguard_association_id: "ocid1.autonomousdatabasedataguardassociation.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"

- name: List autonomous_database_dataguard_associations
  oci_database_autonomous_database_dataguard_association_facts:
    # required
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
autonomous_database_dataguard_associations:
    description:
        - List of AutonomousDatabaseDataguardAssociation resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Autonomous Dataguard created for Autonomous Container Database where given Autonomous Database resides in.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        autonomous_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database that has a relationship with the
                  peer Autonomous Database.
            returned: on success
            type: str
            sample: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        role:
            description:
                - The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.
            returned: on success
            type: str
            sample: PRIMARY
        lifecycle_state:
            description:
                - The current state of Autonomous Data Guard.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState, if available.
            returned: on success
            type: str
            sample: lifecycle_details_example
        peer_role:
            description:
                - The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.
            returned: on success
            type: str
            sample: PRIMARY
        peer_autonomous_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the peer Autonomous Database.
            returned: on success
            type: str
            sample: "ocid1.peerautonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        peer_autonomous_database_life_cycle_state:
            description:
                - The current state of Autonomous Data Guard.
            returned: on success
            type: str
            sample: PROVISIONING
        protection_mode:
            description:
                - The protection mode of this Data Guard association. For more information, see
                  L(Oracle Data Guard Protection Modes,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: str
            sample: MAXIMUM_AVAILABILITY
        apply_lag:
            description:
                - The lag time between updates to the primary database and application of the redo data on the standby database,
                  as computed by the reporting database.
                - "Example: `9 seconds`"
            returned: on success
            type: str
            sample: apply_lag_example
        apply_rate:
            description:
                - The rate at which redo logs are synced between the associated databases.
                - "Example: `180 Mb per second`"
            returned: on success
            type: str
            sample: apply_rate_example
        is_automatic_failover_enabled:
            description:
                - Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association
            returned: on success
            type: bool
            sample: true
        transport_lag:
            description:
                - The approximate number of seconds of redo data not yet available on the standby Autonomous Container Database,
                  as computed by the reporting database.
                - "Example: `7 seconds`"
            returned: on success
            type: str
            sample: transport_lag_example
        time_last_synced:
            description:
                - The date and time of the last update to the apply lag, apply rate, and transport lag values.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date and time the Data Guard association was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_role_changed:
            description:
                - The date and time when the last role change action happened.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "autonomous_database_id": "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "role": "PRIMARY",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "peer_role": "PRIMARY",
        "peer_autonomous_database_id": "ocid1.peerautonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_autonomous_database_life_cycle_state": "PROVISIONING",
        "protection_mode": "MAXIMUM_AVAILABILITY",
        "apply_lag": "apply_lag_example",
        "apply_rate": "apply_rate_example",
        "is_automatic_failover_enabled": true,
        "transport_lag": "transport_lag_example",
        "time_last_synced": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_role_changed": "2013-10-20T19:20:30+01:00"
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


class AutonomousDatabaseDataguardAssociationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "autonomous_database_id",
            "autonomous_database_dataguard_association_id",
        ]

    def get_required_params_for_list(self):
        return [
            "autonomous_database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database_dataguard_association,
            autonomous_database_id=self.module.params.get("autonomous_database_id"),
            autonomous_database_dataguard_association_id=self.module.params.get(
                "autonomous_database_dataguard_association_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_database_dataguard_associations,
            autonomous_database_id=self.module.params.get("autonomous_database_id"),
            **optional_kwargs
        )


AutonomousDatabaseDataguardAssociationFactsHelperCustom = get_custom_class(
    "AutonomousDatabaseDataguardAssociationFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousDatabaseDataguardAssociationFactsHelperCustom,
    AutonomousDatabaseDataguardAssociationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            autonomous_database_dataguard_association_id=dict(
                aliases=["id"], type="str"
            ),
            autonomous_database_id=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_database_dataguard_association",
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

    module.exit_json(autonomous_database_dataguard_associations=result)


if __name__ == "__main__":
    main()
