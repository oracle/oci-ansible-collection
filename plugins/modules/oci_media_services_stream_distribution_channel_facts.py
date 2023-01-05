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
module: oci_media_services_stream_distribution_channel_facts
short_description: Fetches details about one or multiple StreamDistributionChannel resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple StreamDistributionChannel resources in Oracle Cloud Infrastructure
    - Lists the Stream Distribution Channels.
    - If I(stream_distribution_channel_id) is specified, the details of a single StreamDistributionChannel will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    stream_distribution_channel_id:
        description:
            - Unique Stream Distribution Channel path identifier.
            - Required to get a specific stream_distribution_channel.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only the resources with lifecycleState matching the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "NEEDS_ATTENTION"
            - "DELETED"
    display_name:
        description:
            - A filter to return only the resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default
              order for displayName is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific stream_distribution_channel
  oci_media_services_stream_distribution_channel_facts:
    # required
    stream_distribution_channel_id: "ocid1.streamdistributionchannel.oc1..xxxxxxEXAMPLExxxxxx"

- name: List stream_distribution_channels
  oci_media_services_stream_distribution_channel_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
stream_distribution_channels:
    description:
        - List of StreamDistributionChannel resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Stream Distribution Channel display name. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        domain_name:
            description:
                - Unique domain name of the Distribution Channel.
            returned: on success
            type: str
            sample: domain_name_example
        time_created:
            description:
                - The time when the Stream Distribution Channel was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the Stream Distribution Channel was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Stream Distribution Channel.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "domain_name": "domain_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
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
    from oci.media_services import MediaServicesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class StreamDistributionChannelFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "stream_distribution_channel_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_stream_distribution_channel,
            stream_distribution_channel_id=self.module.params.get(
                "stream_distribution_channel_id"
            ),
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
            self.client.list_stream_distribution_channels, **optional_kwargs
        )


StreamDistributionChannelFactsHelperCustom = get_custom_class(
    "StreamDistributionChannelFactsHelperCustom"
)


class ResourceFactsHelper(
    StreamDistributionChannelFactsHelperCustom, StreamDistributionChannelFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            stream_distribution_channel_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "NEEDS_ATTENTION", "DELETED"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="stream_distribution_channel",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(stream_distribution_channels=result)


if __name__ == "__main__":
    main()
