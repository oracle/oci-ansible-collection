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
module: oci_compute_management_instance_pool_instance_facts
short_description: Fetches details about one or multiple InstancePoolInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InstancePoolInstance resources in Oracle Cloud Infrastructure
    - List the instances in the specified instance pool.
    - If I(instance_id) is specified, the details of a single InstancePoolInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
        type: str
        aliases: ["id"]
        required: true
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
            - Required to get a specific instance_pool_instance.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple instance_pool_instances.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific instance_pool_instance
  oci_compute_management_instance_pool_instance_facts:
    # required
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List instance_pool_instances
  oci_compute_management_instance_pool_instance_facts:
    # required
    instance_pool_id: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
instance_pool_instances:
    description:
        - List of InstancePoolInstance resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_pool_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.
            returned: on success
            type: str
            sample: "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - The availability domain the instance is running in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        lifecycle_state:
            description:
                - The attachment state of the instance in relation to the instance pool.
            returned: on success
            type: str
            sample: ATTACHING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the
                  instance.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        fault_domain:
            description:
                - The fault domain the instance is running in.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        instance_configuration_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance configuration
                  used to create the instance.
            returned: on success
            type: str
            sample: "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
        region:
            description:
                - The region that contains the availability domain the instance is running in.
            returned: on success
            type: str
            sample: us-phoenix-1
        shape:
            description:
                - The shape of the instance. The shape determines the number of CPUs, amount of memory,
                  and other resources allocated to the instance.
            returned: on success
            type: str
            sample: shape_example
        state:
            description:
                - The lifecycle state of the instance. Refer to `lifecycleState` in the L(Instance,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/Instance) resource.
            returned: on success
            type: str
            sample: state_example
        time_created:
            description:
                - "The date and time the instance pool instance was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        load_balancer_backends:
            description:
                - The load balancer backends that are configured for the instance.
            returned: on success
            type: complex
            contains:
                load_balancer_id:
                    description:
                        - The OCID of the load balancer attached to the instance pool.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                backend_set_name:
                    description:
                        - The name of the backend set on the load balancer.
                    returned: on success
                    type: str
                    sample: backend_set_name_example
                backend_name:
                    description:
                        - The name of the backend in the backend set.
                    returned: on success
                    type: str
                    sample: backend_name_example
                backend_health_status:
                    description:
                        - The health of the backend as observed by the load balancer.
                    returned: on success
                    type: str
                    sample: OK
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_pool_id": "ocid1.instancepool.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "lifecycle_state": "ATTACHING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "fault_domain": "FAULT-DOMAIN-1",
        "instance_configuration_id": "ocid1.instanceconfiguration.oc1..xxxxxxEXAMPLExxxxxx",
        "region": "us-phoenix-1",
        "shape": "shape_example",
        "state": "state_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "load_balancer_backends": [{
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "backend_set_name": "backend_set_name_example",
            "backend_name": "backend_name_example",
            "backend_health_status": "OK"
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstancePoolInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "instance_pool_id",
            "instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "instance_pool_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_pool_instance,
            instance_pool_id=self.module.params.get("instance_pool_id"),
            instance_id=self.module.params.get("instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_instance_pool_instances,
            compartment_id=self.module.params.get("compartment_id"),
            instance_pool_id=self.module.params.get("instance_pool_id"),
            **optional_kwargs
        )


InstancePoolInstanceFactsHelperCustom = get_custom_class(
    "InstancePoolInstanceFactsHelperCustom"
)


class ResourceFactsHelper(
    InstancePoolInstanceFactsHelperCustom, InstancePoolInstanceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_pool_id=dict(aliases=["id"], type="str", required=True),
            instance_id=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_pool_instance",
        service_client_class=ComputeManagementClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_pool_instances=result)


if __name__ == "__main__":
    main()
