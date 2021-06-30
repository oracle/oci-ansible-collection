#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_limits_resource_availability_facts
short_description: Fetches details about a ResourceAvailability resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ResourceAvailability resource in Oracle Cloud Infrastructure
    - "For a given compartmentId, resource limit name, and scope, returns the following:
        * The number of available resources associated with the given limit.
        * The usage in the selected compartment for the given limit.
        Note that not all resource limits support this API. If the value is not available, the API returns a 404 response."
version_added: "2.9"
author: Oracle (@oracle)
options:
    service_name:
        description:
            - The service name of the target quota.
        type: str
        required: true
    limit_name:
        description:
            - The limit name for which to fetch the data.
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the compartment for which data is being fetched.
        type: str
        required: true
    availability_domain:
        description:
            - "This field is mandatory if the scopeType of the target resource limit is AD.
              Otherwise, this field should be omitted.
              If the above requirements are not met, the API returns a 400 - InvalidParameter response."
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific resource_availability
  oci_limits_resource_availability_facts:
    service_name: service_name_example
    limit_name: limit_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
resource_availability:
    description:
        - ResourceAvailability resource
    returned: on success
    type: complex
    contains:
        used:
            description:
                - The current usage in the given compartment. To support resources with fractional counts,
                  the field rounds up to the nearest integer.
            returned: on success
            type: int
            sample: 56
        available:
            description:
                - The count of available resources. To support resources with fractional counts,
                  the field rounds down to the nearest integer.
            returned: on success
            type: int
            sample: 56
        fractional_usage:
            description:
                - The current most accurate usage in the given compartment.
            returned: on success
            type: float
            sample: 10
        fractional_availability:
            description:
                - The most accurate count of available resources.
            returned: on success
            type: float
            sample: 10
        effective_quota_value:
            description:
                - The effective quota value for the given compartment. This field is only present if there is a
                  current quota policy affecting the current resource in the target region or availability domain.
            returned: on success
            type: float
            sample: 10
    sample: {
        "used": 56,
        "available": 56,
        "fractional_usage": 10,
        "fractional_availability": 10,
        "effective_quota_value": 10
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.limits import LimitsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceAvailabilityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "service_name",
            "limit_name",
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "availability_domain",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_resource_availability,
            service_name=self.module.params.get("service_name"),
            limit_name=self.module.params.get("limit_name"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ResourceAvailabilityFactsHelperCustom = get_custom_class(
    "ResourceAvailabilityFactsHelperCustom"
)


class ResourceFactsHelper(
    ResourceAvailabilityFactsHelperCustom, ResourceAvailabilityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            service_name=dict(type="str", required=True),
            limit_name=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            availability_domain=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_availability",
        service_client_class=LimitsClient,
        namespace="limits",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_availability=result)


if __name__ == "__main__":
    main()
