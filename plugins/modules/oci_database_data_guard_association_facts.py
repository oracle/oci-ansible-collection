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
module: oci_database_data_guard_association_facts
short_description: Fetches details about one or multiple DataGuardAssociation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DataGuardAssociation resources in Oracle Cloud Infrastructure
    - Lists all Data Guard associations for the specified database.
    - If I(data_guard_association_id) is specified, the details of a single DataGuardAssociation will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    data_guard_association_id:
        description:
            - The Data Guard association's L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific data_guard_association.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List data_guard_associations
  oci_database_data_guard_association_facts:
    database_id: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific data_guard_association
  oci_database_data_guard_association_facts:
    database_id: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx
    data_guard_association_id: ocid1.dataguardassociation.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
data_guard_associations:
    description:
        - List of DataGuardAssociation resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Data Guard association.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the reporting database.
            returned: on success
            type: string
            sample: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx
        role:
            description:
                - The role of the reporting database in this Data Guard association.
            returned: on success
            type: string
            sample: PRIMARY
        lifecycle_state:
            description:
                - The current state of the Data Guard association.
            returned: on success
            type: string
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState, if available.
            returned: on success
            type: string
            sample: lifecycle_details_example
        peer_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system containing the associated
                  peer database.
            returned: on success
            type: string
            sample: ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx
        peer_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home containing the associated peer
                  database.
            returned: on success
            type: string
            sample: ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx
        peer_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated peer database.
            returned: on success
            type: string
            sample: ocid1.peerdatabase.oc1..xxxxxxEXAMPLExxxxxx
        peer_data_guard_association_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the peer database's Data Guard association.
            returned: on success
            type: string
            sample: ocid1.peerdataguardassociation.oc1..xxxxxxEXAMPLExxxxxx
        peer_role:
            description:
                - The role of the peer database in this Data Guard association.
            returned: on success
            type: string
            sample: PRIMARY
        apply_lag:
            description:
                - The lag time between updates to the primary database and application of the redo data on the standby database,
                  as computed by the reporting database.
                - "Example: `9 seconds`"
            returned: on success
            type: string
            sample: 9 seconds
        apply_rate:
            description:
                - The rate at which redo logs are synced between the associated databases.
                - "Example: `180 Mb per second`"
            returned: on success
            type: string
            sample: 180 Mb per second
        protection_mode:
            description:
                - The protection mode of this Data Guard association. For more information, see
                  L(Oracle Data Guard Protection Modes,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: string
            sample: MAXIMUM_AVAILABILITY
        transport_type:
            description:
                - The redo transport type used by this Data Guard association.  For more information, see
                  L(Redo Transport Services,http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400)
                  in the Oracle Data Guard documentation.
            returned: on success
            type: string
            sample: SYNC
        time_created:
            description:
                - The date and time the Data Guard association was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
        "role": "PRIMARY",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "peer_db_system_id": "ocid1.peerdbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_db_home_id": "ocid1.peerdbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_database_id": "ocid1.peerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_data_guard_association_id": "ocid1.peerdataguardassociation.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_role": "PRIMARY",
        "apply_lag": "9 seconds",
        "apply_rate": "180 Mb per second",
        "protection_mode": "MAXIMUM_AVAILABILITY",
        "transport_type": "SYNC",
        "time_created": "2013-10-20T19:20:30+01:00"
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


class DataGuardAssociationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_id",
            "data_guard_association_id",
        ]

    def get_required_params_for_list(self):
        return [
            "database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_guard_association,
            database_id=self.module.params.get("database_id"),
            data_guard_association_id=self.module.params.get(
                "data_guard_association_id"
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
            self.client.list_data_guard_associations,
            database_id=self.module.params.get("database_id"),
            **optional_kwargs
        )


DataGuardAssociationFactsHelperCustom = get_custom_class(
    "DataGuardAssociationFactsHelperCustom"
)


class ResourceFactsHelper(
    DataGuardAssociationFactsHelperCustom, DataGuardAssociationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_id=dict(type="str", required=True),
            data_guard_association_id=dict(aliases=["id"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="data_guard_association",
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

    module.exit_json(data_guard_associations=result)


if __name__ == "__main__":
    main()
