#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_compartment
short_description: Manage compartments in OCI
description:
    - This module allows the user to create, delete & update a compartment in OCI.
version_added: "2.5"
options:
    parent_compartment_id:
        description: The OCID of the parent compartment containing the compartment. Use I(parent_compartment_id) to
                     create a compartment under a root or a non-root compartment. Required to create a compartment
                     under a non-root compartment with I(state=present).
        required: false
    compartment_id:
        description: The OCID of the compartment. Use I(compartment_id) to update a compartment. I(compartment_id) may
                     also be set to the tenancy ocid to create a compartment under the root compartment of the tenancy.
                     However it is recommended to use the I(parent_compartment_ocid) for that purpose.
        required: false
        aliases: [ 'id' ]
    description:
        description: The description to be assigned to the compartment. Required when creating a compartment with
                     I(state=present). I(description) should be minimum 1 character and maximum 100 characters long.
                     Does not have to be unique, and it's changeable.
        required: false
    name:
        description: Name of the compartment. The name must be unique across all compartments in the parent compartment.
                     Required when creating a compartment with I(state=present).
        required: false
    state:
        description: Create or update a compartment with I(state=present). Use I(state=absent) to delete a compartment.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_tags, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create a compartment under root compartment using parent_compartment_id option
  oci_compartment:
    parent_compartment_id: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'
    name: Project-A
    description: Compartment for Project-A

- name: Create a compartment under root compartment using compartment_id option. Though this is supported, it is
        recommended to use the parent_compartment_id as shown above to create a compartment under the root compartment
        of the tenancy.
  oci_compartment:
    compartment_id: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'
    name: Project-A
    description: Compartment for Project-A

- name: Create a compartment under a non-root compartment
  oci_compartment:
    parent_compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    name: Project-B
    description: Compartment for Project-B

- name: Update name and description of a non-root compartment
  oci_compartment:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    name: Project-Ansible
    description: Compartment for Project-Ansible

- name: Update description and tags of root compartment
  oci_compartment:
    compartment_id: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'
    freeform_tags:
      stage: test

- name: Delete compartment
  oci_compartment:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    state: absent
"""

RETURN = """
compartment:
    description: Information about the compartment
    returned: On successful operation
    type: dict
    sample: {"compartment_id": 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx',
            "defined_tags": {},
            "description": "Compartment for Project-Ansible",
            "freeform_tags": {},
            "id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status": null,
            "is_accessible": null,
            "lifecycle_state": "ACTIVE",
            "name": "Project-Ansible",
            "time_created": "2017-02-01T03:20:22.160000+00:00"
        }
work_request:
    description: Information about the work request
    returned: When a delete compartment request is raised
    type: dict
    sample: {"compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "errors": null,
            "id": "ocid1.identityworkrequest.oc1..xxxxxEXAMPLExxxxx",
            "logs": null,
            "operation_type": "DELETE_COMPARTMENT",
            "percent_complete": 0.0,
            "resources": null,
            "status": "ACCEPTED",
            "time_accepted": "2018-11-30T12:08:28.168000+00:00",
            "time_finished": null,
            "time_started": null
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import CreateCompartmentDetails
    from oci.identity.models import UpdateCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_compartment(identity_client, module):
    create_compartment_details = CreateCompartmentDetails()
    for attribute in create_compartment_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_compartment_details, attribute, module.params[attribute])

    # If parent_compartment_id is specified in module option, use it to set compartment_id attribute of
    # CreateCompartmentDetails model.
    if module.params["parent_compartment_id"]:
        create_compartment_details.compartment_id = module.params[
            "parent_compartment_id"
        ]

    result = oci_utils.create_and_wait(
        resource_type="compartment",
        create_fn=identity_client.create_compartment,
        kwargs_create={"create_compartment_details": create_compartment_details},
        client=identity_client,
        get_fn=identity_client.get_compartment,
        get_param="compartment_id",
        module=module,
    )
    return result


def update_compartment(identity_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="compartment",
        client=identity_client,
        get_fn=identity_client.get_compartment,
        kwargs_get={"compartment_id": module.params["compartment_id"]},
        update_fn=identity_client.update_compartment,
        primitive_params_update=["compartment_id"],
        kwargs_non_primitive_update={
            UpdateCompartmentDetails: "update_compartment_details"
        },
        module=module,
        update_attributes=UpdateCompartmentDetails().attribute_map.keys(),
    )
    return result


def delete_compartment(identity_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="compartment",
        client=identity_client,
        get_fn=identity_client.get_compartment,
        kwargs_get={"compartment_id": module.params["compartment_id"]},
        delete_fn=identity_client.delete_compartment,
        kwargs_delete={"compartment_id": module.params["compartment_id"]},
        module=module,
        process_work_request=True,
    )
    return result


def is_compartment_root(identity_client, compartment_id):
    # Returns True when compartment_id is OCID of the tenancy.
    compartment = oci_utils.call_with_backoff(
        identity_client.get_compartment, compartment_id=compartment_id
    ).data
    # Root compartment's parent compartment is None.
    return compartment.compartment_id is None


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False, aliases=["id"]),
            name=dict(type="str", required=False),
            description=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            parent_compartment_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        # Name of the compartment `name` is required when `parent_compartment_id` is provided to create a compartment.
        required_if=[["parent_compartment_id", not None, ["name"]]],
        required_one_of=[["parent_compartment_id", "compartment_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    state = module.params["state"]

    if state == "present":
        # For backward compatibility if tenancy OCID is specified in module option `compartment_id` along with option
        # `name`, then process the task as a request to create a sub-compartment under root compartment. If option
        # `name` is not specified or non-root compartment id is provided, process the task as a request to update
        # root/non-root compartment details.
        if module.params["compartment_id"]:
            if (
                is_compartment_root(identity_client, module.params["compartment_id"])
                and module.params["name"]
            ):
                # Create a sub-compartment under root.
                result = oci_utils.check_and_create_resource(
                    resource_type="compartment",
                    create_fn=create_compartment,
                    kwargs_create={
                        "identity_client": identity_client,
                        "module": module,
                    },
                    list_fn=identity_client.list_compartments,
                    kwargs_list={"compartment_id": module.params["compartment_id"]},
                    module=module,
                    model=CreateCompartmentDetails(),
                )
            else:
                # Update compartment details.
                result = update_compartment(identity_client, module)

        else:
            # Create a sub-compartment under compartment specified by module.params['parent_compartment_id'].
            result = oci_utils.check_and_create_resource(
                resource_type="compartment",
                create_fn=create_compartment,
                kwargs_create={"identity_client": identity_client, "module": module},
                list_fn=identity_client.list_compartments,
                kwargs_list={"compartment_id": module.params["parent_compartment_id"]},
                module=module,
                model=CreateCompartmentDetails(),
            )
    else:
        result = delete_compartment(identity_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
