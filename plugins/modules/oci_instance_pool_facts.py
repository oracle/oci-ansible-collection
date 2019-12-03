#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_instance_pool_facts
short_description: Retrieve facts of instance pools in OCI Compute Service
description:
    - This module retrieves information of a specified instance pool or all the instance pools in a specified
      compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. Required to get information of all the instance pools in a
                     specified compartment.
        required: false
    instance_pool_id:
        description: The OCID of the instance pool. Required to get information of the specified instance pool.
        required: false
        aliases: [ 'id' ]
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get information of all the instance pools for a specific availability domain & compartment_id
  oci_instance_pool_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...abcd

- name: Get information of a instance pool
  oci_instance_pool_facts:
    instance_pool_id: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...efgh
"""

RETURN = """
instance_pools:
    description: List of instance pool information
    returned: On success
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the instance pool.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: A user-friendly name for the instance pool.  Does not have to be unique.
            returned: always
            type: string
            sample: "backend-servers-pool"
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: The OCID of the instance pool.
            returned: always
            type: string
            sample: ocid1.instancepool.oc1.phx.xxxxxEXAMPLExxxxx...rz3fhq
        instance_configuration_id:
            description: The OCID of the instance configuration associated to the intance pool.
            returned: always
            type: string
            sample: ocid1.instanceconfiguration.oc1.phx.xxxxxEXAMPLExxxxx...rzxkhq
        lifecycle_state:
            description: The current state of the instance pool.
            returned: always
            type: string
            sample: RUNNING
        placement_configurations:
            description: The placement configurations for the instance pool.
            returned: always
            type: complex
            suboptions:
                availability_domain:
                    description: The availability domain to place instances.
                    returned: always
                    type: string
                primary_subnet_id:
                    description: The OCID of the primary subnet to place instances.
                    returned: always
                    type: string
                secondary_vnics:
                    description: A list of secondary VNIC configurations for instances in the pool.
                    required: false
                    suboptions:
                        display_name:
                            description: The displayName of the vnic. This is also use to match against the Instance
                                         Configuration defined secondary vnic.
                            returned: always
                            type: string
                        subnet_id:
                            description: The subnet OCID for the secondary vnic
                            returned: always
                            type: string
        size:
            description: The number of instances in the instance pool.
            returned: always
            type: int
            sample: 5
        time_created:
            description: The date and time the instance configuration was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: "2018-11-07T04:16:20.454000+00:00"
    sample: [{
                "compartment-id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...glmkwq",
                "defined-tags": {},
                "display-name": "backend-servers-pool",
                "freeform-tags": {},
                "id": "ocid1.instancepool.oc1.iad.xxxxxEXAMPLExxxxx...tztpq",
                "instance-configuration-id": "ocid1.instanceconfiguration.oc1.iad.xxxxxEXAMPLExxxxx...iejka",
                "lifecycle-state": "PROVISIONING",
                "placement-configurations": [
                    {
                        "availability-domain": "IwGV:US-ASHBURN-AD-1",
                        "primary-subnet-id": "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx...dq4a",
                        "secondary-vnic-subnets": null
                    }
                ],
                "size": 1,
                "time-created": "2018-11-09T16:58:35.270000+00:00"
        }]

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_management_client import ComputeManagementClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            instance_pool_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "instance_pool_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_management_client = oci_utils.create_service_client(
        module, ComputeManagementClient
    )

    instance_pool_id = module.params["instance_pool_id"]

    try:
        if instance_pool_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        compute_management_client.get_instance_pool,
                        instance_pool_id=instance_pool_id,
                    ).data
                )
            ]

        else:
            compartment_id = module.params["compartment_id"]
            inst_pool_summaries = to_dict(
                oci_utils.list_all_resources(
                    compute_management_client.list_instance_pools,
                    compartment_id=compartment_id,
                )
            )
            # Get model from summaries returned by `list_instance_pools`
            result = to_dict(
                [
                    oci_utils.call_with_backoff(
                        compute_management_client.get_instance_pool,
                        instance_pool_id=ip["id"],
                    ).data
                    for ip in inst_pool_summaries
                ]
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(instance_pools=result)


if __name__ == "__main__":
    main()
