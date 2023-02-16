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
module: oci_compute_instance_maintenance_reboot_facts
short_description: Fetches details about a InstanceMaintenanceReboot resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a InstanceMaintenanceReboot resource in Oracle Cloud Infrastructure
    - Gets the maximum possible date that a maintenance reboot can be extended. For more information, see
      L(Infrastructure Maintenance,https://docs.cloud.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific instance_maintenance_reboot
  oci_compute_instance_maintenance_reboot_facts:
    # required
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
instance_maintenance_reboot:
    description:
        - InstanceMaintenanceReboot resource
    returned: on success
    type: complex
    contains:
        time_maintenance_reboot_due_max:
            description:
                - "The maximum extension date and time for the maintenance reboot, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  The range for the maintenance extension is between 1 and 14 days from the initial scheduled maintenance date.
                  Example: `2018-05-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "time_maintenance_reboot_due_max": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceMaintenanceRebootFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_maintenance_reboot,
            instance_id=self.module.params.get("instance_id"),
        )


InstanceMaintenanceRebootFactsHelperCustom = get_custom_class(
    "InstanceMaintenanceRebootFactsHelperCustom"
)


class ResourceFactsHelper(
    InstanceMaintenanceRebootFactsHelperCustom, InstanceMaintenanceRebootFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(instance_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_maintenance_reboot",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_maintenance_reboot=result)


if __name__ == "__main__":
    main()
