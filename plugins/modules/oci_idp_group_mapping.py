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
module: oci_idp_group_mapping
short_description: Create, update and delete Identity Provider (IdP) group mappings.
description: Create, update and delete IdP group mappings.
version_added: "2.5"
options:
    identity_provider_id:
        description: The identifier of the identity provider the IdP group mapping belongs to.
        required: true
        type: str
    mapping_id:
        description: The identifier of the IdpGroupMapping to update or delete.
        aliases: ['id']
        type: str
    idp_group_name:
        description: The IdP group name.
        type: str
    group_id:
        description: The identifier of the IAM Service group that is mapped to the IdP group.
        type: str
    state:
        description: Create, update or delete an IdP group mapping. For I(state=present), if the mapping does not exist,
                     it gets created. If it does exist, it gets updated. For I(state=absent), the mapping gets deleted.
        required: false
        default: 'present'
        choices: ['present','absent']

author: "Mike Ross (@mikeross)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Create IdP group mapping
  oci_idp_group_mapping:
    identity_provider_id: 'ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq'
    group_id: 'ocid1.group.oc1..xxxxxEXAMPLExxxxxsdxbsfda'
    idp_group_name: IdPGroupName

- name: Update IdP group name of an IdP group mapping
  oci_idp_group_mapping:
    identity_provider_id: 'ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq'
    mapping_id: 'ocid1.idpgroupmapping.oc1..xxxxxEXAMPLExxxxxbnmfuwba'
    idp_group_name: IdPGroupName
    group_id: 'ocid1.group.oc1..xxxxxEXAMPLExxxxxsdxbsfda'

- name: Deletes an IdP group mapping
  oci_idp_group_mapping:
    identity_provider_id: 'ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq'
    mapping_id: 'ocid1.idpgroupmapping.oc1..xxxxxEXAMPLExxxxxbnmfuwba'
    state: "absent"
"""

RETURN = """
idp_group_mapping:
    description: Attributes of the created / updated IdP group mapping
    returned: on success
    type: complex
    contains:
        id:
            description: The identifier of the IdpGroupMapping.
            returned: always
            type: string
            sample: ocid1.idpgroupmapping.oc1..xxxxxEXAMPLExxxxxbnmfuwba
        idp_id:
            description: The identifier of the Identity Provider this mapping belongs to.
            returned: always
            type: string
            sample: ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq
        idp_group_name:
            description: The name of the IdP group that is mapped to the IAM Service group.
            returned: always
            type: string
            sample: IdPGroupName
        group_id:
            description: The identifier of the IAM Service group that is mapped to the IdP group.
            returned: always
            type: string
            sample: ocid1.group.oc1..xxxxxEXAMPLExxxxxsdxbsfda
        compartment_id:
            description: The identifier of the tenancy containing the Identity Provider.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq
        time_created:
            description: Date and time the mapping was created.
            returned: always
            type: datetime
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description: The mapping's current state.  After creating a mapping object, make sure its lifecycle_state changes
                from CREATING to ACTIVE before using it.
            returned: always
            type: string
            sample: ACTIVE
        inactive_status:
            description: The detailed status of INACTIVE lifecycle_state.
            returned: always
            type: int
            sample: 0
    sample: {
                "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx..6glmkwq",
                "group_id": "ocid1.group.oc1..xxxxxEXAMPLExxxxxsdxbsfda",
                "id": "ocid1.idpgroupmapping.oc1..xxxxxEXAMPLExxxxxbnmfuwba",
                "idp_group_name": "IdPGroupName",
                "idp_id": "ocid1.saml2idp.oc1..xxxxxEXAMPLExxxxxbn4q4eq",
                "inactive_status": null,
                "lifecycle_state": "ACTIVE",
                "time_created": "2016-08-25T21:10:29.600Z"
            }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.exceptions import ServiceError, ClientError
    from oci.identity.models import (
        CreateIdpGroupMappingDetails,
        UpdateIdpGroupMappingDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_idp_group_mapping(identity_client, module):
    create_idp_group_mapping_details = CreateIdpGroupMappingDetails()
    for attribute in create_idp_group_mapping_details.attribute_map:
        create_idp_group_mapping_details.__setattr__(
            attribute, module.params.get(attribute)
        )

    identity_provider_id = module.params.get("identity_provider_id")

    result = oci_utils.create_and_wait(
        resource_type="idp_group_mapping",
        create_fn=identity_client.create_idp_group_mapping,
        kwargs_create={
            "identity_provider_id": identity_provider_id,
            "create_idp_group_mapping_details": create_idp_group_mapping_details,
        },
        client=identity_client,
        get_fn=identity_client.get_idp_group_mapping,
        get_param="mapping_id",
        kwargs_get={"identity_provider_id": identity_provider_id},
        module=module,
    )

    return result


def update_idp_group_mapping(identity_client, module):
    identity_provider_id = module.params.get("identity_provider_id")
    idp_group_mapping_id = module.params.get("mapping_id")

    return oci_utils.check_and_update_resource(
        resource_type="idp_group_mapping",
        client=identity_client,
        get_fn=identity_client.get_idp_group_mapping,
        kwargs_get={
            "identity_provider_id": identity_provider_id,
            "mapping_id": idp_group_mapping_id,
        },
        update_fn=identity_client.update_idp_group_mapping,
        primitive_params_update=["mapping_id", "identity_provider_id"],
        kwargs_non_primitive_update={
            UpdateIdpGroupMappingDetails: "update_idp_group_mapping_details"
        },
        module=module,
        update_attributes=UpdateIdpGroupMappingDetails().attribute_map.keys(),
        required_update_attributes=["group_id", "idp_group_name"],
    )


def delete_idp_group_mapping(identity_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="idp_group_mapping",
        client=identity_client,
        get_fn=identity_client.get_idp_group_mapping,
        kwargs_get={
            "mapping_id": module.params["mapping_id"],
            "identity_provider_id": module.params["identity_provider_id"],
        },
        delete_fn=identity_client.delete_idp_group_mapping,
        kwargs_delete={
            "mapping_id": module.params["mapping_id"],
            "identity_provider_id": module.params["identity_provider_id"],
        },
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_idp_group_mapping")
    set_logger(logger)

    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            mapping_id=dict(type="str", required=False, aliases=["id"]),
            identity_provider_id=dict(type="str", required=True),
            idp_group_name=dict(type="str", required=False),
            group_id=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)
    state = module.params["state"]
    idp_group_mapping_id = module.params.get("mapping_id")

    if state == "present":
        try:
            if idp_group_mapping_id:
                operation_display_text = "update"
                result = update_idp_group_mapping(identity_client, module)
            else:
                operation_display_text = "create"
                result = oci_utils.check_and_create_resource(
                    resource_type="idp_group_mapping",
                    create_fn=create_idp_group_mapping,
                    kwargs_create={
                        "identity_client": identity_client,
                        "module": module,
                    },
                    list_fn=identity_client.list_idp_group_mappings,
                    kwargs_list={
                        "identity_provider_id": module.params.get(
                            "identity_provider_id"
                        )
                    },
                    module=module,
                    model=CreateIdpGroupMappingDetails(),
                )
        except ServiceError as ex:
            get_logger().error(
                "Unable to %s IdpGroupMapping due to: %s",
                operation_display_text,
                ex.message,
            )
            module.fail_json(msg=ex.message)
        except ClientError as ex:
            get_logger().error(
                "Unable to %s IdpGroupMapping due to: %s",
                operation_display_text,
                str(ex),
            )
            module.fail_json(msg=str(ex))
    elif state == "absent":
        result = delete_idp_group_mapping(identity_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
