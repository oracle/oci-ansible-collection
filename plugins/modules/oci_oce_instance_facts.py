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
module: oci_oce_instance_facts
short_description: Fetches details about one or multiple OceInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OceInstance resources in Oracle Cloud Infrastructure
    - Returns a list of OceInstances.
    - If I(oce_instance_id) is specified, the details of a single OceInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    oce_instance_id:
        description:
            - unique OceInstance identifier
            - Required to get a specific oce_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple oce_instances.
        type: str
    tenancy_id:
        description:
            - The ID of the tenancy in which to list resources.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    lifecycle_state:
        description:
            - Filter results on lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific oce_instance
  oci_oce_instance_facts:
    # required
    oce_instance_id: "ocid1.oceinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List oce_instances
  oci_oce_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated
    lifecycle_state: CREATING

"""

RETURN = """
oce_instances:
    description:
        - List of OceInstance resources
    returned: on success
    type: complex
    contains:
        identity_stripe:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                service_name:
                    description:
                        - "Name of the Identity Cloud Service instance in My Services to be used.
                          Example: `secondstripe`"
                    returned: on success
                    type: str
                    sample: service_name_example
                tenancy:
                    description:
                        - "Value of the Identity Cloud Service tenancy.
                          Example: `idcs-8416ebdd0d674f84803f4193cce026e9`"
                    returned: on success
                    type: str
                    sample: tenancy_example
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        guid:
            description:
                - Unique GUID identifier that is immutable on creation
            returned: on success
            type: str
            sample: guid_example
        description:
            description:
                - OceInstance description, can be updated
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - OceInstance Name
            returned: on success
            type: str
            sample: name_example
        tenancy_id:
            description:
                - Tenancy Identifier
            returned: on success
            type: str
            sample: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
        idcs_tenancy:
            description:
                - IDCS Tenancy Identifier
            returned: on success
            type: str
            sample: idcs_tenancy_example
        tenancy_name:
            description:
                - Tenancy Name
            returned: on success
            type: str
            sample: tenancy_name_example
        instance_usage_type:
            description:
                - Instance type based on its usage
            returned: on success
            type: str
            sample: PRIMARY
        add_on_features:
            description:
                - a list of add-on features for the ocm instance
            returned: on success
            type: list
            sample: []
        object_storage_namespace:
            description:
                - Object Storage Namespace of tenancy
            returned: on success
            type: str
            sample: object_storage_namespace_example
        admin_email:
            description:
                - Admin Email for Notification
            returned: on success
            type: str
            sample: admin_email_example
        upgrade_schedule:
            description:
                - Upgrade schedule type representing service to be upgraded immediately whenever latest version is released
                  or delay upgrade of the service to previous released version
            returned: on success
            type: str
            sample: UPGRADE_IMMEDIATELY
        waf_primary_domain:
            description:
                - Web Application Firewall(WAF) primary domain
            returned: on success
            type: str
            sample: waf_primary_domain_example
        instance_access_type:
            description:
                - Flag indicating whether the instance access is private or public
            returned: on success
            type: str
            sample: PUBLIC
        instance_license_type:
            description:
                - Flag indicating whether the instance license is new cloud or bring your own license
            returned: on success
            type: str
            sample: NEW
        time_created:
            description:
                - The time the the OceInstance was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the OceInstance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the instance lifecycle.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details of the current state of the instance lifecycle
            returned: on success
            type: str
            sample: STANDBY
        dr_region:
            description:
                - disaster recovery paired ragion name
            returned: on success
            type: str
            sample: us-phoenix-1
        state_message:
            description:
                - An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: state_message_example
        service:
            description:
                - "SERVICE data.
                  Example: `{\\"service\\": {\\"IDCS\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "identity_stripe": {
            "service_name": "service_name_example",
            "tenancy": "tenancy_example"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "guid": "guid_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "tenancy_id": "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "idcs_tenancy": "idcs_tenancy_example",
        "tenancy_name": "tenancy_name_example",
        "instance_usage_type": "PRIMARY",
        "add_on_features": [],
        "object_storage_namespace": "object_storage_namespace_example",
        "admin_email": "admin_email_example",
        "upgrade_schedule": "UPGRADE_IMMEDIATELY",
        "waf_primary_domain": "waf_primary_domain_example",
        "instance_access_type": "PUBLIC",
        "instance_license_type": "NEW",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "STANDBY",
        "dr_region": "us-phoenix-1",
        "state_message": "state_message_example",
        "service": {},
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.oce import OceInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OceInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oce_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_oce_instance,
            oce_instance_id=self.module.params.get("oce_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "tenancy_id",
            "display_name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_oce_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OceInstanceFactsHelperCustom = get_custom_class("OceInstanceFactsHelperCustom")


class ResourceFactsHelper(OceInstanceFactsHelperCustom, OceInstanceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            oce_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            tenancy_id=dict(type="str"),
            display_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="oce_instance",
        service_client_class=OceInstanceClient,
        namespace="oce",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(oce_instances=result)


if __name__ == "__main__":
    main()
