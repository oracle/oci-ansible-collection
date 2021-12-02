#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_management_awr_db_wait_event_bucket_facts
short_description: Fetches details about a AwrDbWaitEventBucket resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AwrDbWaitEventBucket resource in Oracle Cloud Infrastructure
    - Summarizes AWR wait event data into value buckets and frequency, for the specified database in the AWR.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    awr_db_id:
        description:
            - "The parameter to filter the database by internal ID.
              Note that the internal ID of the database can be retrieved from the following endpoint:
              /managedDatabases/{managedDatabaseId}/awrDbs"
        type: str
        aliases: ["id"]
        required: true
    name:
        description:
            - The required single value query parameter to filter the entity name.
        type: str
        required: true
    inst_num:
        description:
            - The optional single value query parameter to filter the database instance number.
        type: str
    begin_sn_id_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to filter on the snapshot ID.
        type: int
    end_sn_id_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the snapshot ID.
        type: int
    time_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to query parameter to filter the timestamp.
        type: str
    time_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the timestamp.
        type: str
    num_bucket:
        description:
            - The number of buckets within the histogram.
        type: int
    min_value:
        description:
            - The minimum value of the histogram.
        type: float
    max_value:
        description:
            - The maximum value of the histogram.
        type: float
    container_id:
        description:
            - "The optional query parameter to filter the database container by an exact ID value.
              Note that the database container ID can be retrieved from the following endpoint:
              /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges"
        type: int
    sort_by:
        description:
            - The option to sort distribution data.
        type: str
        choices:
            - "CATEGORY"
            - "PERCENTAGE"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific awr_db_wait_event_bucket
  oci_database_management_awr_db_wait_event_bucket_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    awr_db_id: "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    inst_num: inst_num_example
    begin_sn_id_greater_than_or_equal_to: 56
    end_sn_id_less_than_or_equal_to: 56
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    num_bucket: 56
    min_value: 1.2
    max_value: 1.2
    container_id: 56
    sort_by: CATEGORY
    sort_order: ASC

"""

RETURN = """
awr_db_wait_event_bucket:
    description:
        - AwrDbWaitEventBucket resource
    returned: on success
    type: complex
    contains:
        category:
            description:
                - The name of the wait event frequency category. Normally, it is the upper range of the waits within the AWR wait event bucket.
            returned: on success
            type: str
            sample: category_example
        percentage:
            description:
                - The percentage of waits in a wait event bucket over the total waits of the database.
            returned: on success
            type: float
            sample: 1.2
    sample: {
        "category": "category_example",
        "percentage": 1.2
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AwrDbWaitEventBucketFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "awr_db_id",
            "name",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "num_bucket",
            "min_value",
            "max_value",
            "container_id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_awr_db_wait_event_buckets,
            managed_database_id=self.module.params.get("managed_database_id"),
            awr_db_id=self.module.params.get("awr_db_id"),
            name=self.module.params.get("name"),
            **optional_kwargs
        )


AwrDbWaitEventBucketFactsHelperCustom = get_custom_class(
    "AwrDbWaitEventBucketFactsHelperCustom"
)


class ResourceFactsHelper(
    AwrDbWaitEventBucketFactsHelperCustom, AwrDbWaitEventBucketFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            awr_db_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str", required=True),
            inst_num=dict(type="str"),
            begin_sn_id_greater_than_or_equal_to=dict(type="int"),
            end_sn_id_less_than_or_equal_to=dict(type="int"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            num_bucket=dict(type="int"),
            min_value=dict(type="float"),
            max_value=dict(type="float"),
            container_id=dict(type="int"),
            sort_by=dict(type="str", choices=["CATEGORY", "PERCENTAGE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_db_wait_event_bucket",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_db_wait_event_bucket=result)


if __name__ == "__main__":
    main()
