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
module: oci_service_catalog_association_facts
short_description: Fetches details about one or multiple ServiceCatalogAssociation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ServiceCatalogAssociation resources in Oracle Cloud Infrastructure
    - Lists all the resource associations for a specific service catalog.
    - If I(service_catalog_association_id) is specified, the details of a single ServiceCatalogAssociation will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    service_catalog_association_id:
        description:
            - The unique identifier of the service catalog association.
            - Required to get a specific service_catalog_association.
        type: str
        aliases: ["id"]
    service_catalog_id:
        description:
            - The unique identifier for the service catalog.
        type: str
    entity_id:
        description:
            - The unique identifier of the entity associated with service catalog.
        type: str
    entity_type:
        description:
            - The type of the application in the service catalog.
        type: str
    sort_order:
        description:
            - The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Default is `TIMECREATED`
        type: str
        choices:
            - "TIMECREATED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific service_catalog_association
  oci_service_catalog_association_facts:
    # required
    service_catalog_association_id: "ocid1.servicecatalogassociation.oc1..xxxxxxEXAMPLExxxxxx"

- name: List service_catalog_associations
  oci_service_catalog_association_facts:

    # optional
    service_catalog_association_id: "ocid1.servicecatalogassociation.oc1..xxxxxxEXAMPLExxxxxx"
    service_catalog_id: "ocid1.servicecatalog.oc1..xxxxxxEXAMPLExxxxxx"
    entity_id: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
    entity_type: entity_type_example
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
service_catalog_associations:
    description:
        - List of ServiceCatalogAssociation resources
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "service_catalog_id": "ocid1.servicecatalog.oc1..xxxxxxEXAMPLExxxxxx",
        "entity_id": "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx",
        "entity_type": "entity_type_example",
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.service_catalog import ServiceCatalogClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ServiceCatalogAssociationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "service_catalog_association_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_catalog_association,
            service_catalog_association_id=self.module.params.get(
                "service_catalog_association_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "service_catalog_association_id",
            "service_catalog_id",
            "entity_id",
            "entity_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_service_catalog_associations, **optional_kwargs
        )


ServiceCatalogAssociationFactsHelperCustom = get_custom_class(
    "ServiceCatalogAssociationFactsHelperCustom"
)


class ResourceFactsHelper(
    ServiceCatalogAssociationFactsHelperCustom, ServiceCatalogAssociationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            service_catalog_association_id=dict(aliases=["id"], type="str"),
            service_catalog_id=dict(type="str"),
            entity_id=dict(type="str"),
            entity_type=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="service_catalog_association",
        service_client_class=ServiceCatalogClient,
        namespace="service_catalog",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(service_catalog_associations=result)


if __name__ == "__main__":
    main()
