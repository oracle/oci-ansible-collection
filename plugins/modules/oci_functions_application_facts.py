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
module: oci_functions_application_facts
short_description: Fetches details about one or multiple Application resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Application resources in Oracle Cloud Infrastructure
    - Lists applications for a compartment.
    - If I(application_id) is specified, the details of a single Application will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    application_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this application.
            - Required to get a specific application.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to which this resource belongs.
            - Required to list multiple applications.
        type: str
    lifecycle_state:
        description:
            - "A filter to return only applications that match the lifecycle state in this parameter.
              Example: `Creating`"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only applications with display names that match the display name string. Matching is exact.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - Specifies sort order.
            - "* **ASC:** Ascending sort order.
              * **DESC:** Descending sort order."
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the attribute with which to sort the rules.
            - "Default: `displayName`"
            - "* **timeCreated:** Sorts by timeCreated.
              * **displayName:** Sorts by displayName.
              * **id:** Sorts by id."
        type: str
        choices:
            - "timeCreated"
            - "id"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List applications
  oci_functions_application_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific application
  oci_functions_application_facts:
    application_id: ocid1.application.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
applications:
    description:
        - List of Application resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the application.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment that contains the application.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The display name of the application. The display name is unique within the compartment containing the application.
            returned: on success
            type: string
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the application.
            returned: on success
            type: string
            sample: CREATING
        config:
            description:
                - Application configuration for functions in this application (passed as environment variables). Can be overridden by function configuration.
                  Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values
                  should be limited to printable unicode characters.
                - "Example: `{\\"MY_FUNCTION_CONFIG\\": \\"ConfVal\\"}`"
                - The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each
                  key and value in UTF-8.
            returned: on success
            type: dict
            sample: {}
        subnet_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the subnets in which to run functions in the
                  application.
            returned: on success
            type: list
            sample: []
        syslog_url:
            description:
                - "A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
                  The syslog URL must be reachable from all of the subnets configured for the application.
                  Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging
                  service, and not to the syslog URL."
                - "Example: `tcp://logserver.myserver:1234`"
            returned: on success
            type: string
            sample: tcp://logserver.myserver:1234
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        time_created:
            description:
                - The time the application was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: string
            sample: 2018-09-12T22:47:12.613Z
        time_updated:
            description:
                - "The time the application was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2018-09-12T22:47:12.613Z`"
            returned: on success
            type: string
            sample: 2018-09-12T22:47:12.613Z
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "config": {},
        "subnet_ids": [],
        "syslog_url": "tcp://logserver.myserver:1234",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "time_created": "2018-09-12T22:47:12.613Z",
        "time_updated": "2018-09-12T22:47:12.613Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.functions import FunctionsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApplicationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "application_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_application,
            application_id=self.module.params.get("application_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_applications,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ApplicationFactsHelperCustom = get_custom_class("ApplicationFactsHelperCustom")


class ResourceFactsHelper(ApplicationFactsHelperCustom, ApplicationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            application_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "id", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="application",
        service_client_class=FunctionsManagementClient,
        namespace="functions",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(applications=result)


if __name__ == "__main__":
    main()
