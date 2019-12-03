#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_dhcp_options
short_description: Create,update and delete OCI Dhcp Options
description:
    - Creates OCI Dhcp Options
    - Update OCI Dhcp Options, if present, with a new display name
    - Update OCI Dhcp Options, if present, by appending new options to existing options
    - Update OCI Dhcp Options, if present, by purging existing options and replacing them with
      specified ones
    - Delete OCI Dhcp Options, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this
                     Dhcp Options would be created. Mandatory for create
                     operation.Optional for delete and update. Mutually exclusive
                     with dhcp_id.
        required: false
    vcn_id:
        description: Identifier of the Virtual Cloud Network to which the
                     Dhcp Options should be attached. Mandatory for create
                     operation. Optional for delete and update. Mutually exclusive
                     with dhcp_id.
        required: false
    dhcp_id:
        description: Identifier of the Dhcp Options. Mandatory for delete and update.
        required: false
        aliases: ['id']
    display_name:
        description: Name of the Dhcp Options. A user friendly name. Does not have to be unique,
                     and could be changed. If not specified, a default name would be provided.
        required: false
        aliases: ['name']
    options:
        description: A set of DHCP options. Mandatory for create and update.
        required: false
        suboptions:
            type:
                description: The specific DHCP option.
                required: true
                choices: ['DomainNameServer', 'SearchDomain']
            server_type:
                description: Applicable only for the I(type='DomainNameServer').Describes the
                             type of the server.
                required: true
                choices: ['VcnLocalPlusInternet', 'CustomDnsServer']
            custom_dns_servers:
                description: Applicable only for the I(type='DomainNameServer') and I(server_type='CustomDnsServer').
                             Maximum three DNS server ips are allowed as part of this option.
                required: false
            search_domain_names:
                description: Applicable only for the I(type='SearchDomain').A single search domain name
                             according to RFC 952 and RFC 1123. Do not include this option with an empty
                             list of search domain names, or with an empty string as the value for any search
                             domain name.
                required: true

    purge_dhcp_options:
        description: Purge existing Dhcp Options which are not present in the provided
                     Dhcp Options. If I(purge_dhcp_options=no), provided options would be
                     appended to existing options. I(purge_dhcp_options) and I(delete_dhcp_options)
                     are mutually exclusive.
        required: false
        default: 'yes'
        type: bool
    delete_dhcp_options:
        description: Delete existing Dhcp Options which are present in the Dhcp Options provided by
                     I(options). If I(delete_dhcp_options=yes), options provided by I(options) would be
                     deleted from existing options, if they are part of existing dhcp options.
                     If they are not part of existing dhcp options, they will be ignored.
                     I(delete_dhcp_options) and I(purge_dhcp_options) are mutually exclusive.
        required: false
        default: 'no'
        type: bool
    state:
        description: Create,update or delete Dhcp Options. For I(state=present), if it
                     does not exist, it gets created. If it exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']

author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
#Note: These examples do not set authentication details.
#Create/update Dhcp Options
- name: Create Dhcp options
  oci_dhcp_options:
    compartment_id: 'ocid1.compartment..xdsc'
    name: 'ansible_dhcp_options'
    vcn_id: 'ocid1.vcn..aaaa'
    options:
          - type: 'DomainNameServer'
            server_type: 'VcnLocalPlusInternet'
            custom_dns_servers: []
          - type: 'SearchDomain'
            search_domain_names: ['ansibletestvcn.oraclevcn.com']
    freeform_tags:
        region: 'east'
    defined_tags:
        features:
            capacity: 'medium'
    state: 'present'

# Update Dhcp Options by appending new options
- name: Update Dhcp Options by appending new options
  oci_dhcp_options:
    id: 'ocid1.dhcpoptions.oc1.aaa'
    purge_dhcp_options: 'no'
    options:
          - type: 'DomainNameServer'
            server_type: 'CustomDnsServer'
            custom_dns_servers: ['10.0.0.8']
          - type: 'SearchDomain'
            search_domain_names: ['ansibletestvcn.oraclevcn.com']
    state: 'present'

# Update Dhcp Options by purging existing options
- name: Update Dhcp Options by purging existing options
  oci_dhcp_options:
    dhcp_id: 'ocid1.dhcpoptions.oc1.aaa'
    options:
          - type: 'DomainNameServer'
            server_type: 'CustomDnsServer'
            custom_dns_servers: ['10.0.0.8', '10.0.0.10', '10.0.0.12']
          - type: 'SearchDomain'
            search_domain_names: ['ansibletestvcn.oraclevcn.com']
    state: 'present'

# Update Dhcp Options by deleting existing options
- name: Update Dhcp Options by deleting existing options
  oci_dhcp_options:
    dhcp_id: 'ocid1.dhcpoptions.oc1.aaa'
    options:
          - type: 'DomainNameServer'
            server_type: 'CustomDnsServer'
            custom_dns_servers: ['10.0.0.8', '10.0.0.10', '10.0.0.12']
    delete_dhcp_options: 'yes'
    state: 'present'

#Delete Dhcp Options
- name: Delete Dhcp Options
  oci_dhcp_options:
    dhcp_id: 'ocid1.dhcpoptions..xdsc'
    state: 'absent'
"""

RETURN = """
    dhcp_options:
        description: Attributes of the created/updated Dhcp Options.
                    For delete, deleted Dhcp Options description will
                    be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Dhcp Options
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Dhcp Options during creation
                returned: always
                type: string
                sample: ansible_dhcp_options
            id:
                description: Identifier of the Dhcp Options
                returned: always
                type: string
                sample: ocid1.dhcpoptions.oc1.axdf
            vcn_id:
                description: Identifier of the Virtual Cloud Network to which the
                             Dhcp Options is attached.
                returned: always
                type: string
                sample: ocid1.vcn..ixcd
            lifecycle_state:
                description: The current state of the Dhcp Options
                returned: always
                type: string
                sample: AVAILABLE
            options:
                description: A list of dhcp options.
                returned: always
                type: list
                sample: [{"custom_dns_servers": [],"server_type": "CustomDnsServer","type": "DomainNameServer"},
                        {"search_domain_names": ["myansiblevcn.oraclevcn.com"],"type": "SearchDomain"}]
            time_created:
                description: Date and time when the Dhcp Options was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
        sample: {
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "freeform_tags":{"region":"east"},
                    "defined_tags":{"features":{"capacity":"medium"}},
                    "display_name":"ansible_dhcp_options",
                    "id":"ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"AVAILABLE",
                    "options":[
                                {
                                    "custom_dns_servers":[],
                                    "server_type":"VcnLocalPlusInternet",
                                    "type":"DomainNameServer"
                                },
                                {
                                    "search_domain_names":["ansibletestvcn.oraclevcn.com"],
                                    "type":"SearchDomain"
                                },
                                {
                                    "custom_dns_servers":["10.0.0.8"],
                                    "server_type":"CustomDnsServer",
                                    "type":"DomainNameServer"
                                }
                            ],
                    "time_created":"2017-11-26T16:41:06.996000+00:00",
                    "vcn_id":"ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
                }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded, ClientError
    from oci.util import to_dict
    from oci.core.models import (
        CreateDhcpDetails,
        DhcpDnsOption,
        UpdateDhcpDetails,
        DhcpSearchDomainOption,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_dhcp_options(virtual_network_client, module):
    result = dict(changed=False, dhcp_options="")
    dhcp_id = module.params.get("dhcp_id")
    exclude_attributes = {"display_name": True}
    try:
        if dhcp_id:
            existing_dhcp_options = oci_utils.get_existing_resource(
                virtual_network_client.get_dhcp_options, module, dhcp_id=dhcp_id
            )
            result = update_dhcp_options(
                virtual_network_client, existing_dhcp_options, module
            )
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="dhcp_options",
                create_fn=create_dhcp_options,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_dhcp_options,
                kwargs_list={
                    "compartment_id": module.params.get("compartment_id"),
                    "vcn_id": module.params.get("vcn_id"),
                },
                module=module,
                exclude_attributes=exclude_attributes,
                model=CreateDhcpDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ClientError as ex:
        module.fail_json(msg=ex.args[0])

    return result


def create_dhcp_options(virtual_network_client, module):
    options = get_options_objects(module.params["options"])
    create_dhcp_details = CreateDhcpDetails()
    for attribute in create_dhcp_details.attribute_map:
        create_dhcp_details.__setattr__(attribute, module.params.get(attribute))
    create_dhcp_details.options = options
    result = oci_utils.create_and_wait(
        resource_type="dhcp_options",
        create_fn=virtual_network_client.create_dhcp_options,
        kwargs_create={"create_dhcp_details": create_dhcp_details},
        client=virtual_network_client,
        get_fn=virtual_network_client.get_dhcp_options,
        get_param="dhcp_id",
        module=module,
    )
    return result


def update_dhcp_options(virtual_network_client, existing_dhcp_options, module):
    if existing_dhcp_options is None:
        raise ClientError(
            Exception(
                "No Dhcp Options with id "
                + module.params.get("dhcp_id")
                + " is found for update"
            )
        )
    result = dict(dhcp_options=to_dict(existing_dhcp_options), changed=False)
    name_tag_changed = False
    options_changed = False
    input_options = module.params.get("options")
    update_dhcp_details = UpdateDhcpDetails()
    existing_options = existing_dhcp_options.options
    attributes_to_compare = ["display_name", "freeform_tags", "defined_tags"]
    for attribute in attributes_to_compare:
        name_tag_changed = oci_utils.check_and_update_attributes(
            update_dhcp_details,
            attribute,
            module.params.get(attribute),
            getattr(existing_dhcp_options, attribute),
            name_tag_changed,
        )
    if input_options is not None:
        if input_options:
            options, options_changed = oci_utils.get_component_list_difference(
                get_options_objects(input_options),
                get_hashed_options(existing_options),
                module.params.get("purge_dhcp_options"),
                module.params.get("delete_dhcp_options"),
            )
    if options_changed:
        update_dhcp_details.options = options
    else:
        update_dhcp_details.options = existing_options

    if name_tag_changed or options_changed:
        result = oci_utils.update_and_wait(
            resource_type="dhcp_options",
            update_fn=virtual_network_client.update_dhcp_options,
            kwargs_update={
                "dhcp_id": existing_dhcp_options.id,
                "update_dhcp_details": update_dhcp_details,
            },
            client=virtual_network_client,
            get_fn=virtual_network_client.get_dhcp_options,
            get_param="dhcp_id",
            module=module,
        )

    return result


def get_hashed_options(options):
    hashed_options = []
    if options is None:
        return hashed_options
    for option in options:
        dhcp_option = None
        if option.type == "DomainNameServer":
            dhcp_option = oci_utils.create_hashed_instance(DhcpDnsOption)
            dhcp_option.type = "DomainNameServer"
            server_type = option.server_type
            dhcp_option.server_type = server_type
            if server_type == "CustomDnsServer":
                dhcp_option.custom_dns_servers = option.custom_dns_servers
            else:
                dhcp_option.custom_dns_servers = []
        elif option.type == "SearchDomain":
            dhcp_option = oci_utils.create_hashed_instance(DhcpSearchDomainOption)
            dhcp_option.type = "SearchDomain"
            dhcp_option.search_domain_names = option.search_domain_names
        hashed_options.append(dhcp_option)

    return hashed_options


def get_options_objects(options):
    dhcp_options = []
    for option in options:
        dhcp_option = None
        if option["type"] == "DomainNameServer":
            dhcp_option = oci_utils.create_hashed_instance(DhcpDnsOption)
            dhcp_option.type = "DomainNameServer"
            server_type = option["server_type"]
            dhcp_option.server_type = server_type
            if server_type == "CustomDnsServer":
                dhcp_option.custom_dns_servers = option.get("custom_dns_servers", None)
            else:
                dhcp_option.custom_dns_servers = []
        elif option["type"] == "SearchDomain":
            dhcp_option = oci_utils.create_hashed_instance(DhcpSearchDomainOption)
            dhcp_option.type = "SearchDomain"
            search_domain_names = option["search_domain_names"]
            if search_domain_names:
                dhcp_option.search_domain_names = option["search_domain_names"]
            else:
                raise ClientError("search_domain_names field should not be empty")
        dhcp_options.append(dhcp_option)
    return dhcp_options


def delete_dhcp_options(virtual_network_client, module):
    return oci_utils.delete_and_wait(
        resource_type="dhcp_options",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_dhcp_options,
        kwargs_get={"dhcp_id": module.params["dhcp_id"]},
        delete_fn=virtual_network_client.delete_dhcp_options,
        kwargs_delete={"dhcp_id": module.params["dhcp_id"]},
        module=module,
    )


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            vcn_id=dict(type="str", required=False),
            dhcp_id=dict(type="str", required=False, aliases=["id"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            options=dict(type=list, required=False),
            purge_dhcp_options=dict(type="bool", required=False, default=True),
            delete_dhcp_options=dict(type="bool", required=False, default=False),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["purge_dhcp_options", "delete_dhcp_options"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    state = module.params["state"]

    if state == "present":
        result = create_or_update_dhcp_options(virtual_network_client, module)
    elif state == "absent":
        result = delete_dhcp_options(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
