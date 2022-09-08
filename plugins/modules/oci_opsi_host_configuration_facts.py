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
module: oci_opsi_host_configuration_facts
short_description: Fetches details about one or multiple HostConfiguration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HostConfiguration resources in Oracle Cloud Infrastructure
    - Gets a list of host insight configurations based on the query parameters specified. Either compartmentId or hostInsightId query parameter must be
      specified.
      When both compartmentId and compartmentIdInSubtree are specified, a list of host insight configurations in that compartment and in all sub-compartments
      will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    enterprise_manager_bridge_id:
        description:
            - Unique Enterprise Manager bridge identifier
        type: str
    id:
        description:
            - Optional list of host insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    exadata_insight_id:
        description:
            - Optional list of exadata insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    platform_type:
        description:
            - "Filter by one or more platform types.
              Supported platformType(s) for MACS-managed external host insight: [LINUX].
              Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX]."
        type: list
        elements: str
        choices:
            - "LINUX"
            - "SOLARIS"
            - "SUNOS"
            - "ZLINUX"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Host configuration list sort options.
        type: str
        choices:
            - "hostName"
            - "platformType"
    defined_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
              The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    defined_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
              or \\"{namespace}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
              The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    compartment_id_in_subtree:
        description:
            - A flag to search all resources within a given compartment and all sub-compartments.
        type: bool
    host_type:
        description:
            - Filter by one or more host types.
              Possible values are CLOUD-HOST, EXTERNAL-HOST
        type: list
        elements: str
    host_id:
        description:
            - Optional L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host (Compute Id)
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List host_configurations
  oci_opsi_host_configuration_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    enterprise_manager_bridge_id: "ocid1.enterprisemanagerbridge.oc1..xxxxxxEXAMPLExxxxxx"
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    exadata_insight_id: [ "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx" ]
    platform_type: [ "LINUX" ]
    sort_order: ASC
    sort_by: hostName
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true
    host_type: [ "host_type_example" ]
    host_id: "ocid1.host.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
host_configurations:
    description:
        - List of HostConfiguration resources
    returned: on success
    type: complex
    contains:
        host_insight_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host insight resource.
            returned: on success
            type: str
            sample: "ocid1.hostinsight.oc1..xxxxxxEXAMPLExxxxxx"
        entity_source:
            description:
                - Source of the host entity.
            returned: on success
            type: str
            sample: MACS_MANAGED_EXTERNAL_HOST
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        host_name:
            description:
                - The host name. The host name is unique amongst the hosts managed by the same management agent.
            returned: on success
            type: str
            sample: host_name_example
        platform_type:
            description:
                - "Platform type.
                  Supported platformType(s) for MACS-managed external host insight: [LINUX].
                  Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX]."
            returned: on success
            type: str
            sample: LINUX
        platform_version:
            description:
                - Platform version.
            returned: on success
            type: str
            sample: platform_version_example
        platform_vendor:
            description:
                - Platform vendor.
            returned: on success
            type: str
            sample: platform_vendor_example
        total_cpus:
            description:
                - Total CPU on this host.
            returned: on success
            type: int
            sample: 56
        total_memory_in_gbs:
            description:
                - Total amount of usable physical memory in gibabytes
            returned: on success
            type: float
            sample: 1.2
        cpu_architecture:
            description:
                - CPU architechure
            returned: on success
            type: str
            sample: cpu_architecture_example
        cpu_cache_in_mbs:
            description:
                - Size of cache memory in megabytes.
            returned: on success
            type: float
            sample: 1.2
        cpu_vendor:
            description:
                - Name of the CPU vendor.
            returned: on success
            type: str
            sample: cpu_vendor_example
        cpu_frequency_in_mhz:
            description:
                - Clock frequency of the processor in megahertz.
            returned: on success
            type: float
            sample: 1.2
        cpu_implementation:
            description:
                - Model name of processor.
            returned: on success
            type: str
            sample: cpu_implementation_example
        cores_per_socket:
            description:
                - Number of cores per socket.
            returned: on success
            type: int
            sample: 56
        total_sockets:
            description:
                - Number of total sockets.
            returned: on success
            type: int
            sample: 56
        threads_per_socket:
            description:
                - Number of threads per socket.
            returned: on success
            type: int
            sample: 56
        is_hyper_threading_enabled:
            description:
                - Indicates if hyper-threading is enabled or not
            returned: on success
            type: bool
            sample: true
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: [{
        "host_insight_id": "ocid1.hostinsight.oc1..xxxxxxEXAMPLExxxxxx",
        "entity_source": "MACS_MANAGED_EXTERNAL_HOST",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "host_name": "host_name_example",
        "platform_type": "LINUX",
        "platform_version": "platform_version_example",
        "platform_vendor": "platform_vendor_example",
        "total_cpus": 56,
        "total_memory_in_gbs": 1.2,
        "cpu_architecture": "cpu_architecture_example",
        "cpu_cache_in_mbs": 1.2,
        "cpu_vendor": "cpu_vendor_example",
        "cpu_frequency_in_mhz": 1.2,
        "cpu_implementation": "cpu_implementation_example",
        "cores_per_socket": 56,
        "total_sockets": 56,
        "threads_per_socket": 56,
        "is_hyper_threading_enabled": true,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HostConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "enterprise_manager_bridge_id",
            "id",
            "exadata_insight_id",
            "platform_type",
            "sort_order",
            "sort_by",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
            "host_type",
            "host_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_host_configurations, **optional_kwargs
        )


HostConfigurationFactsHelperCustom = get_custom_class(
    "HostConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    HostConfigurationFactsHelperCustom, HostConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            enterprise_manager_bridge_id=dict(type="str"),
            id=dict(type="list", elements="str"),
            exadata_insight_id=dict(type="list", elements="str"),
            platform_type=dict(
                type="list",
                elements="str",
                choices=["LINUX", "SOLARIS", "SUNOS", "ZLINUX"],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["hostName", "platformType"]),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
            host_type=dict(type="list", elements="str"),
            host_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="host_configuration",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(host_configurations=result)


if __name__ == "__main__":
    main()
