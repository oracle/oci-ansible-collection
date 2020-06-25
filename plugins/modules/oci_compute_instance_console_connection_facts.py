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
module: oci_compute_instance_console_connection_facts
short_description: Fetches details about one or multiple InstanceConsoleConnection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InstanceConsoleConnection resources in Oracle Cloud Infrastructure
    - Lists the console connections for the specified compartment or instance.
    - For more information about console access, see L(Accessing the Console,https://docs.cloud.oracle.com/Content/Compute/References/serialconsole.htm).
    - If I(instance_console_connection_id) is specified, the details of a single InstanceConsoleConnection will be returned.
version_added: "2.5"
options:
    instance_console_connection_id:
        description:
            - The OCID of the instance console connection.
            - Required to get a specific instance_console_connection.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple instance_console_connections.
        type: str
    instance_id:
        description:
            - The OCID of the instance.
        type: str
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List instance_console_connections
  oci_compute_instance_console_connection_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific instance_console_connection
  oci_compute_instance_console_connection_facts:
    instance_console_connection_id: ocid1.instanceconsoleconnection.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
instance_console_connections:
    description:
        - List of InstanceConsoleConnection resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment to contain the console connection.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        connection_string:
            description:
                - The SSH connection string for the console connection.
            returned: on success
            type: string
            sample: connection_string_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        fingerprint:
            description:
                - The SSH public key fingerprint for the console connection.
            returned: on success
            type: string
            sample: fingerprint_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the console connection.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        instance_id:
            description:
                - The OCID of the instance the console connection connects to.
            returned: on success
            type: string
            sample: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the console connection.
            returned: on success
            type: string
            sample: ACTIVE
        vnc_connection_string:
            description:
                - The SSH connection string for the SSH tunnel used to
                  connect to the console connection over VNC.
            returned: on success
            type: string
            sample: vnc_connection_string_example
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_string": "connection_string_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "fingerprint": "fingerprint_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "vnc_connection_string": "vnc_connection_string_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceConsoleConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "instance_console_connection_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_console_connection,
            instance_console_connection_id=self.module.params.get(
                "instance_console_connection_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "instance_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_instance_console_connections,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


InstanceConsoleConnectionFactsHelperCustom = get_custom_class(
    "InstanceConsoleConnectionFactsHelperCustom"
)


class ResourceFactsHelper(
    InstanceConsoleConnectionFactsHelperCustom, InstanceConsoleConnectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instance_console_connection_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            instance_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_console_connection",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_console_connections=result)


if __name__ == "__main__":
    main()
