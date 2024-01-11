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
module: oci_database_management_iorm_plan_facts
short_description: Fetches details about a IormPlan resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a IormPlan resource in Oracle Cloud Infrastructure
    - Get the IORM plan from the specific exadata storage server.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_exadata_storage_server_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific iorm_plan
  oci_database_management_iorm_plan_facts:
    # required
    external_exadata_storage_server_id: "ocid1.externalexadatastorageserver.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
iorm_plan:
    description:
        - IormPlan resource
    returned: on success
    type: complex
    contains:
        plan_status:
            description:
                - The status of the IORM plan.
            returned: on success
            type: str
            sample: ACTIVE
        plan_objective:
            description:
                - The objective of the IORM plan.
            returned: on success
            type: str
            sample: AUTO
        db_plan:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - A list of DatabasePlanDirectives.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of a database or a profile.
                            returned: on success
                            type: str
                            sample: name_example
                        share:
                            description:
                                - The relative priority a database in the database plan. A higher share value implies
                                  higher priority and more access to the I/O resources.
                                  Use either share or (level, allocation). All plan directives in a database plan
                                  should use the same setting.
                                  Share-based resource allocation is the recommended method for a database plan.
                            returned: on success
                            type: int
                            sample: 56
                        level:
                            description:
                                - The allocation level. Valid values are from 1 to 8. Resources are allocated to level 1 first,
                                  and then remaining resources are allocated to level 2, and so on.
                            returned: on success
                            type: int
                            sample: 56
                        allocation:
                            description:
                                - The resource allocation as a percentage (0-100) within the level.
                            returned: on success
                            type: int
                            sample: 56
                        limit:
                            description:
                                - The maximum I/O utilization limit as a percentage of the available resources.
                            returned: on success
                            type: int
                            sample: 56
                        is_flash_cache_on:
                            description:
                                - Controls use of Exadata Smart Flash Cache by a database.
                                  This ensures that cache space is reserved for mission-critical databases.
                                  flashcache=off is invalid in a directive that contains the flashcachemin, flashcachelimit, or flashcachesize attributes.
                            returned: on success
                            type: bool
                            sample: true
                        is_pmem_cache_on:
                            description:
                                - Controls use of the persistent memory (PMEM) cache by a database. This ensures that cache space
                                  is reserved for mission-critical databases.
                                  pmemcache=off is invalid in a directive that contains the pmemcachemin, pmemcachelimit, or pmemcachesize attributes.
                            returned: on success
                            type: bool
                            sample: true
                        is_flash_log_on:
                            description:
                                - Controls use of Exadata Smart Flash Log by a database.
                                  This ensures that Exadata Smart Flash Log is reserved for mission-critical databases.
                            returned: on success
                            type: bool
                            sample: true
                        is_pmem_log_on:
                            description:
                                - Controls use of persistent memory logging (PMEM log) by a database.
                                  This ensures that PMEM log is reserved for mission-critical databases.
                            returned: on success
                            type: bool
                            sample: true
                        flash_cache_limit:
                            description:
                                - Defines a soft limit for space usage in Exadata Smart Flash Cache.
                                  If the cache is not full, the limit can be exceeded.
                                  You specify the value for flashcachelimit in bytes. You can also use the suffixes M (megabytes),
                                  G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
                                  The value for flashcachelimit must be at least 4 MB.
                                  The flashcachelimit and flashcachesize attributes cannot be specified in the same directive.
                                  The value for flashcachelimit cannot be smaller than flashcachemin, if it is specified.
                            returned: on success
                            type: str
                            sample: flash_cache_limit_example
                        flash_cache_min:
                            description:
                                - Specifies a minimum guaranteed space allocation in Exadata Smart Flash Cache.
                                  You specify the value for flashcachemin in bytes. You can also use the suffixes
                                  M (megabytes), G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
                                  The value for flashcachemin must be at least 4 MB.
                                  In any plan, the sum of all flashcachemin values cannot exceed the size of Exadata Smart Flash Cache.
                                  If flashcachelimit is specified, then the value for flashcachemin cannot exceed flashcachelimit.
                                  If flashcachesize is specified, then the value for flashcachemin cannot exceed flashcachesize.
                            returned: on success
                            type: str
                            sample: flash_cache_min_example
                        flash_cache_size:
                            description:
                                - Defines a hard limit for space usage in Exadata Smart Flash Cache.
                                  The limit cannot be exceeded, even if the cache is not full.
                                  In an IORM plan, if the size of Exadata Smart Flash Cache can accommodate all of the flashcachemin
                                  and flashcachesize allocations, then each flashcachesize definition represents a guaranteed space allocation.
                                  However, starting with Oracle Exadata System Software release 19.2.0 you can use the flashcachesize
                                  attribute to over-provision space in Exadata Smart Flash Cache. Consequently,
                                  if the size of Exadata Smart Flash Cache cannot accommodate all of the flashcachemin and flashcachesize
                                  allocations, then only flashcachemin is guaranteed.
                            returned: on success
                            type: str
                            sample: flash_cache_size_example
                        pmem_cache_limit:
                            description:
                                - Defines a soft limit for space usage in the persistent memory (PMEM) cache.
                                  If the cache is not full, the limit can be exceeded.
                                  You specify the value for pmemcachelimit in bytes. You can also use the suffixes M (megabytes),
                                  G (gigabytes), or T (terabytes) to specify larger values. For example, 300M, 150G, or 1T.
                                  The value for pmemcachelimit must be at least 4 MB.
                                  The pmemcachelimit and pmemcachesize attributes cannot be specified in the same directive.
                                  The value for pmemcachelimit cannot be smaller than pmemcachemin, if it is specified.
                            returned: on success
                            type: str
                            sample: pmem_cache_limit_example
                        pmem_cache_min:
                            description:
                                - Specifies a minimum guaranteed space allocation in the persistent memory (PMEM) cache.
                            returned: on success
                            type: str
                            sample: pmem_cache_min_example
                        pmem_cache_size:
                            description:
                                - Defines a hard limit for space usage in the persistent memory (PMEM) cache.
                                  The limit cannot be exceeded, even if the cache is not full.
                                  In an IORM plan, if the size of the PMEM cache can accommodate all of the pmemcachemin and
                                  pmemcachesize allocations, then each pmemcachesize definition represents a guaranteed space allocation.
                                  However, you can use the pmemcachesize attribute to over-provision space in the PMEM cache.
                                  Consequently, if the PMEM cache size cannot accommodate all of the pmemcachemin and pmemcachesize
                                  allocations, then only pmemcachemin is guaranteed.
                            returned: on success
                            type: str
                            sample: pmem_cache_size_example
                        asm_cluster:
                            description:
                                - Starting with Oracle Exadata System Software release 19.1.0, you can use the asmcluster attribute to
                                  distinguish between databases with the same name running in different Oracle ASM clusters.
                            returned: on success
                            type: str
                            sample: asm_cluster_example
                        type:
                            description:
                                - "Enables you to create a profile, or template, to ease management and configuration of resource plans
                                  in environments with many databases.
                                  type=database: Specifies a directive that applies to a specific database.
                                  If type in not specified, then the directive defaults to the database type.
                                  type=profile: Specifies a directive that applies to a profile rather than a specific database.
                                    To associate a database with an IORM profile, you must set the database initialization
                                    parameter db_performance_profile to the value of the profile name. Databases that map to a profile i
                                    nherit the settings specified in the profile."
                            returned: on success
                            type: str
                            sample: DATABASE
                        role:
                            description:
                                - Enables you specify different plan directives based on the Oracle Data Guard database role.
                            returned: on success
                            type: str
                            sample: PRIMARY
    sample: {
        "plan_status": "ACTIVE",
        "plan_objective": "AUTO",
        "db_plan": {
            "items": [{
                "name": "name_example",
                "share": 56,
                "level": 56,
                "allocation": 56,
                "limit": 56,
                "is_flash_cache_on": true,
                "is_pmem_cache_on": true,
                "is_flash_log_on": true,
                "is_pmem_log_on": true,
                "flash_cache_limit": "flash_cache_limit_example",
                "flash_cache_min": "flash_cache_min_example",
                "flash_cache_size": "flash_cache_size_example",
                "pmem_cache_limit": "pmem_cache_limit_example",
                "pmem_cache_min": "pmem_cache_min_example",
                "pmem_cache_size": "pmem_cache_size_example",
                "asm_cluster": "asm_cluster_example",
                "type": "DATABASE",
                "role": "PRIMARY"
            }]
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IormPlanFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "external_exadata_storage_server_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_iorm_plan,
            external_exadata_storage_server_id=self.module.params.get(
                "external_exadata_storage_server_id"
            ),
        )


IormPlanFactsHelperCustom = get_custom_class("IormPlanFactsHelperCustom")


class ResourceFactsHelper(IormPlanFactsHelperCustom, IormPlanFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_exadata_storage_server_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="iorm_plan",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(iorm_plan=result)


if __name__ == "__main__":
    main()
