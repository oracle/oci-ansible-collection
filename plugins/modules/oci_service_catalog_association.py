#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_service_catalog_association
short_description: Manage a ServiceCatalogAssociation resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a ServiceCatalogAssociation resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an association between service catalog and a resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    service_catalog_id:
        description:
            - Identifier of the service catalog.
            - Required for create using I(state=present).
        type: str
    entity_id:
        description:
            - Identifier of the entity being associated with service catalog.
            - Required for create using I(state=present).
        type: str
    entity_type:
        description:
            - The type of the entity that is associated with the service catalog.
        type: str
    service_catalog_association_id:
        description:
            - The unique identifier of the service catalog association.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ServiceCatalogAssociation.
            - Use I(state=present) to create a ServiceCatalogAssociation.
            - Use I(state=absent) to delete a ServiceCatalogAssociation.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create service_catalog_association
  oci_service_catalog_association:
    # required
    service_catalog_id: "ocid1.servicecatalog.oc1..xxxxxxEXAMPLExxxxxx"
    entity_id: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    entity_type: entity_type_example

- name: Delete service_catalog_association
  oci_service_catalog_association:
    # required
    service_catalog_association_id: "ocid1.servicecatalogassociation.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
service_catalog_association:
    description:
        - Details of the ServiceCatalogAssociation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Identifier of the association.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        service_catalog_id:
            description:
                - Identifier of the service catalog.
            returned: on success
            type: str
            sample: "ocid1.servicecatalog.oc1..xxxxxxEXAMPLExxxxxx"
        entity_id:
            description:
                - Identifier of the entity being associated with service catalog.
            returned: on success
            type: str
            sample: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type:
            description:
                - The type of the entity that is associated with the service catalog.
            returned: on success
            type: str
            sample: entity_type_example
        time_created:
            description:
                - Timestamp of when the resource was associated with service catalog.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "service_catalog_id": "ocid1.servicecatalog.oc1..xxxxxxEXAMPLExxxxxx",
        "entity_id": "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx",
        "entity_type": "entity_type_example",
        "time_created": "2013-10-20T19:20:30+01:00"
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
    from oci.service_catalog import ServiceCatalogClient
    from oci.service_catalog.models import CreateServiceCatalogAssociationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceCatalogAssociationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "service_catalog_association_id"

    def get_module_resource_id(self):
        return self.module.params.get("service_catalog_association_id")

    def get_get_fn(self):
        return self.client.get_service_catalog_association

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_catalog_association,
            service_catalog_association_id=self.module.params.get(
                "service_catalog_association_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "service_catalog_association_id",
            "service_catalog_id",
            "entity_id",
            "entity_type",
        ]

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
            self.client.list_service_catalog_associations, **kwargs
        )

    def get_create_model_class(self):
        return CreateServiceCatalogAssociationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_service_catalog_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_service_catalog_association_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_service_catalog_association,
            call_fn_args=(),
            call_fn_kwargs=dict(
                service_catalog_association_id=self.module.params.get(
                    "service_catalog_association_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ServiceCatalogAssociationHelperCustom = get_custom_class(
    "ServiceCatalogAssociationHelperCustom"
)


class ResourceHelper(
    ServiceCatalogAssociationHelperCustom, ServiceCatalogAssociationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            service_catalog_id=dict(type="str"),
            entity_id=dict(type="str"),
            entity_type=dict(type="str"),
            service_catalog_association_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="service_catalog_association",
        service_client_class=ServiceCatalogClient,
        namespace="service_catalog",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
