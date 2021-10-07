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
module: oci_jms_fleet_facts
short_description: Fetches details about one or multiple Fleet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Fleet resources in Oracle Cloud Infrastructure
    - Returns a list of all the Fleets contained by a compartment.
    - If I(fleet_id) is specified, the details of a single Fleet will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    fleet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Fleet.
            - Required to get a specific fleet.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - The state of the lifecycle.
        type: str
        choices:
            - "ACTIVE"
            - "CREATING"
            - "DELETED"
            - "DELETING"
            - "FAILED"
            - "UPDATING"
    display_name:
        description:
            - The display name.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - "The field to sort Fleets. Only one sort order may be provided.
              Default order for _timeCreated_, _approximateJreCount_, _approximateInstallationCount_,
              _approximateApplicationCount_ and _approximateManagedInstanceCount_  is **descending**.
              Default order for _displayName_ is **ascending**.
              If no value is specified _timeCreated_ is default."
        type: str
        choices:
            - "displayName"
            - "timeCreated"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List fleets
  oci_jms_fleet_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific fleet
  oci_jms_fleet_facts:
    fleet_id: "ocid1.fleet.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
fleets:
    description:
        - List of Fleet resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Fleet.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the Fleet.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The Fleet's description.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment of the Fleet.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        approximate_jre_count:
            description:
                - The approximate count of all unique Java Runtimes in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_installation_count:
            description:
                - The approximate count of all unique Java installations in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_application_count:
            description:
                - The approximate count of all unique applications in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        approximate_managed_instance_count:
            description:
                - The approximate count of all unique managed instances in the Fleet in the past seven days.
                  This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - The creation date and time of the Fleet (formatted according to L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The lifecycle state of the Fleet.
            returned: on success
            type: str
            sample: ACTIVE
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`. (See L(Understanding Free-form
                  Tags,https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm))."
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`. (See L(Managing Tags and Tag
                  Namespaces,https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm).)"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "approximate_jre_count": 56,
        "approximate_installation_count": 56,
        "approximate_application_count": 56,
        "approximate_managed_instance_count": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.jms import JavaManagementServiceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FleetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "fleet_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fleet, fleet_id=self.module.params.get("fleet_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_fleets, **optional_kwargs
        )


FleetFactsHelperCustom = get_custom_class("FleetFactsHelperCustom")


class ResourceFactsHelper(FleetFactsHelperCustom, FleetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            fleet_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACTIVE",
                    "CREATING",
                    "DELETED",
                    "DELETING",
                    "FAILED",
                    "UPDATING",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="fleet",
        service_client_class=JavaManagementServiceClient,
        namespace="jms",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(fleets=result)


if __name__ == "__main__":
    main()
