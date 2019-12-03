#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_tag_namespace
short_description: Create, retire and reactivate tag namespaces in OCI
description:
    - This module allows the user to create, retire and reactivate tag namespaces in OCI. A tag namespace is a
      container for tag keys. It consists of a name, and zero or more tag key definitions. Tag namespaces are not case
      sensitive, and must be unique across the tenancy.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment containing the tag namespace (the compartment may also be the root
                     compartment of the Tenancy). Required for creating a tag namespace with I(state=present).
        required: false
    tag_namespace_id:
        description: The OCID of the tag namespace. Required when the tag namespace must be retired or reactivated.
        required: false
        aliases: ['id']
    name:
        description: The name assigned to the tag namespace during creation. It must be unique across all tag namespaces
                     in the tenancy and cannot be changed. All ascii characters are allowed except spaces and dots.
                     Note that names are case insenstive, that means you can not have two different namespaces with
                     same name but with different casing in one tenancy. Required when a tag namespace is created using
                     I(state=present).
        required: false
    description:
        description: A description to be associated with the tag namespace during creation. This does not have to be
                     unique, and can be changed later. Required when creating a tag namespace with I(state=present)
                     The length of the description must be between 1 and 400 characters.
        required: false
    reactivate:
        description: Whether a retired tag namespace needs to be reactivated
        required: false
        default: "no"
        type: bool
    state:
        description: The state of the tag namespace that must be asserted to. When I(state=present), and the
                     tag namespace doesn't exist, the tag namespace is created. When I(state=absent), the tag namespace
                     is retired. To reactivate a retired tag namespace, use I(reactivate=yes).
        required: false
        default: "present"
        choices: ['present', 'absent']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_tags ]
"""

EXAMPLES = """
- name: Create a new tag namespace
  oci_tag_namespace:
    compartment_id: "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx"
    name: "BillingTags"
    description: "This namespace contains tags that will be used in billing."

- name: Update the description of a tag namespace
  oci_tag_namespace:
    id: "ocid1.namespace.oc1..xxxxxEXAMPLExxxxx"
    description: "Tags used for billing"

- name: Retire a tag namespace
  oci_tag_namespace:
    id: "ocid1.namespace.oc1..xxxxxEXAMPLExxxxx"
    state: "absent"

- name: To reactivate a retired namespace
  oci_tag_namespace:
    id: "ocid1.namespace.oc1..xxxxxEXAMPLExxxxx"
    reactivate: "yes"
"""

RETURN = """
tag_namespace:
    description: Details of the tag namespace
    returned: On successful create or update of a tag namespace
    type: dict
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "description": "This namespace contains tags that will be used in billing.",
            "freeform_tags": {},
            "id": "ocid1.tagnamespace.oc1..xxxxxEXAMPLExxxxx",
            "is_retired": false,
            "name": "BillingTags",
            "time_created": "2018-01-15T17:36:10.388000+00:00"
     }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import CreateTagNamespaceDetails, UpdateTagNamespaceDetails
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None


def set_logger(provided_logger):
    global logger
    logger = provided_logger


def get_logger():
    return logger


def update_tag_namespace_state(identity_client, tag_namespace_id, module, is_retired):
    try:
        utnd = UpdateTagNamespaceDetails()
        utnd.is_retired = is_retired

        updated_tag_ns = oci_utils.call_with_backoff(
            identity_client.update_tag_namespace,
            tag_namespace_id=tag_namespace_id,
            update_tag_namespace_details=utnd,
        ).data

        get_logger().info("Retired Tag Namespace %s", tag_namespace_id)
        return updated_tag_ns, True
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))


def update_tag_namespace_description(
    identity_client, tag_namespace_id, description, module
):
    try:
        utnsd = UpdateTagNamespaceDetails()
        utnsd.description = description

        updated_tag_ns = oci_utils.call_with_backoff(
            identity_client.update_tag_namespace,
            tag_namespace_id=tag_namespace_id,
            update_tag_namespace_details=utnsd,
        ).data

        get_logger().info("Updated tag namespace %s", to_dict(updated_tag_ns))
        return updated_tag_ns, True
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def create_tag_namespace(identity_client, compartment_id, name, description, module):
    result = {}
    try:
        ctnsd = CreateTagNamespaceDetails()
        ctnsd.name = name
        ctnsd.description = description
        ctnsd.compartment_id = compartment_id
        oci_utils.add_tags_to_model_from_module(ctnsd, module)

        create_response = oci_utils.call_with_backoff(
            identity_client.create_tag_namespace, create_tag_namespace_details=ctnsd
        )

        get_logger().info("Created Tag Namespace %s", to_dict(create_response.data))

        result["tag_namespace"] = to_dict(create_response.data)
        result["changed"] = True
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))


def main():
    set_logger(oci_utils.get_logger("oci_tag_namespace"))

    module_args = oci_utils.get_taggable_arg_spec(supports_create=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            tag_namespace_id=dict(type="str", required=False, aliases=["id"]),
            name=dict(type="str", required=False),
            description=dict(type="str", required=False),
            reactivate=dict(type="bool", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["tag_namespace_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)
    state = module.params["state"]

    result = dict(changed=False)

    compartment_id = module.params.get("compartment_id", None)
    tag_ns_id = module.params.get("tag_namespace_id", None)
    name = module.params.get("name", None)
    description = module.params.get("description", None)

    get_logger().debug("Tag namespace id is " + str(tag_ns_id))

    if tag_ns_id is not None:
        tag_ns = oci_utils.call_with_backoff(
            identity_client.get_tag_namespace, tag_namespace_id=tag_ns_id
        ).data

        if state == "absent":
            get_logger().debug("Retire tag namespace %s requested", tag_ns_id)
            if tag_ns is not None:
                retired = False
                if not tag_ns.is_retired:
                    get_logger().debug("Retiring %s", tag_ns.id)
                    tag_ns, retired = update_tag_namespace_state(
                        identity_client, tag_ns_id, module, is_retired=True
                    )

                result["changed"] = retired
                result["tag_namespace"] = to_dict(tag_ns)
        # if the Tag-namespace doesn't exist, it is already deleted and so we return the default dict with
        # changed as False
        elif state == "present":
            desc_changed = False
            reactivated = False

            if tag_ns.description != description:
                tag_ns, desc_changed = update_tag_namespace_description(
                    identity_client, tag_ns_id, description, module
                )

            reactivate = module.params.get("reactivate", None)
            if reactivate:
                get_logger().debug("Reactivate tag namespace %s requested", tag_ns_id)
                if tag_ns.is_retired:
                    tag_ns, reactivated = update_tag_namespace_state(
                        identity_client, tag_ns_id, module, is_retired=False
                    )

            result["changed"] = desc_changed or reactivated
            result["tag_namespace"] = to_dict(tag_ns)
    else:
        result = oci_utils.check_and_create_resource(
            resource_type="tag_namespace",
            create_fn=create_tag_namespace,
            kwargs_create={
                "identity_client": identity_client,
                "compartment_id": compartment_id,
                "name": name,
                "description": description,
                "module": module,
            },
            list_fn=identity_client.list_tag_namespaces,
            kwargs_list={"compartment_id": compartment_id},
            module=module,
            model=CreateTagNamespaceDetails(),
            default_attribute_values={"defined_tags": {}},
        )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
