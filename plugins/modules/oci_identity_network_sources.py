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
module: oci_identity_network_sources
short_description: Manage a NetworkSources resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NetworkSources resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new network source in your tenancy.
    - You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy
      is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies)
      reside within the tenancy itself, unlike cloud resources such as compute instances, which typically
      reside within compartments inside the tenancy. For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "You must also specify a *name* for the network source, which must be unique across all network sources in your
      tenancy, and cannot be changed.
      You can use this name or the OCID when writing policies that apply to the network source. For more information
      about policies, see L(How Policies Work,https://docs.cloud.oracle.com/Content/Identity/Concepts/policies.htm)."
    - "You must also specify a *description* for the network source (although it can be an empty string). It does not
      have to be unique, and you can change it anytime with L(UpdateNetworkSource,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/20160918/NetworkSource/UpdateNetworkSource)."
    - After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
      object, first make sure its `lifecycleState` has changed to ACTIVE.
    - After your network resource is created, you can use it in policy to restrict access to only requests made from an allowed
      IP address specified in your network source. For more information, see L(Managing Network
      Sources,https://docs.cloud.oracle.com/Content/Identity/Tasks/managingnetworksources.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy (root compartment) containing the network source object.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - The name you assign to the network source during creation. The name must be unique across all groups
              in the tenancy and cannot be changed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    public_source_list:
        description:
            - A list of allowed public IP addresses and CIDR ranges.
        type: list
    virtual_source_list:
        description:
            - "A list of allowed VCN OCID and IP range pairs.
              Example:`\\"vcnId\\": \\"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\\", \\"ipRanges\\": [ \\"129.213.39.0/24\\" ]`"
        type: list
        suboptions:
            vcn_id:
                description:
                    - ""
                type: str
            ip_ranges:
                description:
                    - ""
                type: list
    services:
        description:
            - A list of services allowed to make on-behalf-of requests. These requests can have different source IP addresses
              than those listed in the network source.
              Currently, only `all` and `none` are supported. The default is `all`.
        type: list
    description:
        description:
            - The description you assign to the network source during creation. Does not have to be unique, and it's changeable.
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    network_source_id:
        description:
            - The OCID of the network source.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NetworkSources.
            - Use I(state=present) to create or update a NetworkSources.
            - Use I(state=absent) to delete a NetworkSources.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create network_sources
  oci_identity_network_sources:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    name: name_example
    description: description_example

- name: Update network_sources using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_network_sources:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    name: name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update network_sources
  oci_identity_network_sources:
    description: description_example
    network_source_id: ocid1.networksource.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete network_sources
  oci_identity_network_sources:
    network_source_id: ocid1.networksource.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete network_sources using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_network_sources:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    name: name_example
    state: absent

"""

RETURN = """
network_sources:
    description:
        - Details of the NetworkSources resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the network source.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the tenancy containing the network source. The tenancy is the root compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name you assign to the network source during creation. The name must be unique across
                  the tenancy and cannot be changed.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description you assign to the network source. Does not have to be unique, and it's changeable.
            returned: on success
            type: string
            sample: description_example
        public_source_list:
            description:
                - A list of allowed public IPs and CIDR ranges.
            returned: on success
            type: list
            sample: []
        virtual_source_list:
            description:
                - "A list of allowed VCN OCID and IP range pairs.
                  Example:`\\"vcnId\\": \\"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\\", \\"ipRanges\\": [ \\"129.213.39.0/24\\" ]`"
            returned: on success
            type: complex
            contains:
                vcn_id:
                    description:
                        - ""
                    returned: on success
                    type: string
                    sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
                ip_ranges:
                    description:
                        - ""
                    returned: on success
                    type: list
                    sample: []
        services:
            description:
                - A list of services allowed to make on-behalf-of requests. These requests can have different source IPs than
                  those specified in the network source.
                  Currently, only `all` and `none` are supported. The default is `all`.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - Date and time the group was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The network source object's current state. After creating a network source, make sure its `lifecycleState` changes from CREATING to
                  ACTIVE before using it.
            returned: on success
            type: string
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "public_source_list": [],
        "virtual_source_list": [{
            "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
            "ip_ranges": []
        }],
        "services": [],
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient
    from oci.identity.models import CreateNetworkSourceDetails
    from oci.identity.models import UpdateNetworkSourceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkSourcesHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "network_source_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_source_id")

    def get_get_fn(self):
        return self.client.get_network_source

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_network_source,
            network_source_id=self.module.params.get("network_source_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_network_sources, **kwargs
        )

    def get_create_model_class(self):
        return CreateNetworkSourceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_network_source,
            call_fn_args=(),
            call_fn_kwargs=dict(create_network_source_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateNetworkSourceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_network_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_source_id=self.module.params.get("network_source_id"),
                update_network_source_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_network_source,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_source_id=self.module.params.get("network_source_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


NetworkSourcesHelperCustom = get_custom_class("NetworkSourcesHelperCustom")


class ResourceHelper(NetworkSourcesHelperCustom, NetworkSourcesHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            public_source_list=dict(type="list"),
            virtual_source_list=dict(
                type="list",
                elements="dict",
                options=dict(vcn_id=dict(type="str"), ip_ranges=dict(type="list")),
            ),
            services=dict(type="list"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            network_source_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_sources",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
