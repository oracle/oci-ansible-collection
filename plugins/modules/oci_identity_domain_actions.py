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
module: oci_identity_domain_actions
short_description: Perform actions on a Domain resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Domain resource in Oracle Cloud Infrastructure
    - "For I(action=activate), if the domain's {@code lifecycleState} is INACTIVE,
      1. Set the {@code lifecycleDetails} to ACTIVATING and asynchronously starts enabling
         the domain and return 202 ACCEPTED.
          1.1 Sets the domain status to ENABLED and set specified domain's
              {@code lifecycleState} to ACTIVE and set the {@code lifecycleDetails} to null.
      To track progress, HTTP GET on /iamWorkRequests/{iamWorkRequestsId} endpoint will provide
      the async operation's status. Deactivate a domain can be done using HTTP POST
      /domains/{domainId}/actions/deactivate.
      - If the domain's {@code lifecycleState} is ACTIVE, returns 202 ACCEPTED with no action
        taken on service side.
      - If domain is of {@code type} DEFAULT or DEFAULT_LIGHTWEIGHT or domain's {@code lifecycleState} is not INACTIVE,
        returns 400 BAD REQUEST.
      - If the domain doesn't exists, returns 404 NOT FOUND.
      - If the authenticated user is part of the domain to be activated, returns 400 BAD REQUEST
      - If error occurs while activating domain, returns 500 INTERNAL SERVER ERROR."
    - "For I(action=change_compartment), change the containing compartment for a domain.
      This is an asynchronous call where the Domain's compartment is changed and is updated with the new compartment information.
      To track progress, HTTP GET on /iamWorkRequests/{iamWorkRequestsId} endpoint will provide
      the async operation's status.
      The compartment change is complete when accessed via domain URL and
      also returns new compartment OCID.
      - If the domain doesn't exists, returns 404 NOT FOUND.
      - If Domain {@code type} is DEFAULT or DEFAULT_LIGHTWEIGHT, return 400 BAD Request
      - If Domain is not active or being updated, returns 400 BAD REQUEST.
      - If error occurs while changing compartment for domain, return 500 INTERNAL SERVER ERROR."
    - "For I(action=change_domain_license_type), if the domain's {@code lifecycleState} is ACTIVE, validates the requested {@code licenseType} update
      is allowed and
      1. Set the {@code lifecycleDetails} to UPDATING
      2. Asynchronously starts updating the domain and return 202 ACCEPTED.
          2.1 Successfully updates specified domain's {@code licenseType}.
      3. On completion set the {@code lifecycleDetails} to null.
      To track progress, HTTP GET on /iamWorkRequests/{iamWorkRequestsId} endpoint will provide
      the async operation's status.
      - If license type update is successful, return 202 ACCEPTED
      - If requested {@code licenseType} validation fails, returns 400 Bad request.
      - If Domain is not active or being updated, returns 400 BAD REQUEST.
      - If Domain {@code type} is DEFAULT or DEFAULT_LIGHTWEIGHT, return 400 BAD Request
      - If the domain doesn't exists, returns 404 NOT FOUND
      - If any internal error occurs, returns 500 INTERNAL SERVER ERROR."
    - "For I(action=deactivate), if the domain's {@code lifecycleState} is ACTIVE and no active Apps are present in domain,
      1. Set the {@code lifecycleDetails} to DEACTIVATING and asynchronously starts disabling
         the domain and return 202 ACCEPTED.
          1.1 Sets the domain status to DISABLED and set specified domain's
              {@code lifecycleState} to INACTIVE and set the {@code lifecycleDetails} to null.
      To track progress, HTTP GET on /iamWorkRequests/{iamWorkRequestsId} endpoint will provide
      the async operation's status. Activate a domain can be done using HTTP POST
      /domains/{domainId}/actions/activate.
      - If the domain's {@code lifecycleState} is INACTIVE, returns 202 ACCEPTED with no action
        taken on service side.
      - If domain is of {@code type} DEFAULT or DEFAULT_LIGHTWEIGHT or domain's {@code lifecycleState}
        is not ACTIVE, returns 400 BAD REQUEST.
      - If the domain doesn't exists, returns 404 NOT FOUND.
      - If any active Apps in domain, returns 400 BAD REQUEST.
      - If the authenticated user is part of the domain to be activated, returns 400 BAD REQUEST
      - If error occurs while deactivating domain, returns 500 INTERNAL SERVER ERROR."
    - "For I(action=enable_replication_to_region), replicate domain to a new region. This is an asynchronous call - where, at start,
      {@code state} of this domain in replica region is set to ENABLING_REPLICATION.
      On domain replication completion the {@code state} will be set to REPLICATION_ENABLED.
      To track progress, HTTP GET on /iamWorkRequests/{iamWorkRequestsId} endpoint will provide
      the async operation's status.
      If the replica region's {@code state} is already ENABLING_REPLICATION or REPLICATION_ENABLED,
      returns 409 CONFLICT.
      - If the domain doesn't exists, returns 404 NOT FOUND.
      - If home region is same as replication region, return 400 BAD REQUEST.
      - If Domain is not active or being updated, returns 400 BAD REQUEST.
      - If any internal error occurs, return 500 INTERNAL SERVER ERROR."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the destination compartment
              into which to move the domain.
            - Required for I(action=change_compartment).
        type: str
    license_type:
        description:
            - The License type of Domain
            - Applicable only for I(action=change_domain_license_type).
        type: str
    domain_id:
        description:
            - The OCID of the domain
        type: str
        aliases: ["id"]
        required: true
    replica_region:
        description:
            - A region for which domain replication is requested for.
              See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
              for the full list of supported region names.
            - "Example: `us-phoenix-1`"
            - Applicable only for I(action=enable_replication_to_region).
        type: str
    action:
        description:
            - The action to perform on the Domain.
        type: str
        required: true
        choices:
            - "activate"
            - "change_compartment"
            - "change_domain_license_type"
            - "deactivate"
            - "enable_replication_to_region"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on domain
  oci_identity_domain_actions:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    action: activate

- name: Perform action change_compartment on domain
  oci_identity_domain_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action change_domain_license_type on domain
  oci_identity_domain_actions:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_domain_license_type

    # optional
    license_type: license_type_example

- name: Perform action deactivate on domain
  oci_identity_domain_actions:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    action: deactivate

- name: Perform action enable_replication_to_region on domain
  oci_identity_domain_actions:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"
    action: enable_replication_to_region

    # optional
    replica_region: us-phoenix-1

"""

RETURN = """
domain:
    description:
        - Details of the Domain resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the domain
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the domain.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The mutable display name of the domain
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The domain descripition
            returned: on success
            type: str
            sample: description_example
        url:
            description:
                - Region agnostic domain URL.
            returned: on success
            type: str
            sample: url_example
        home_region_url:
            description:
                - Region specific domain URL.
            returned: on success
            type: str
            sample: home_region_url_example
        home_region:
            description:
                - The home region for the domain.
                  See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
                  for the full list of supported region names.
                - "Example: `us-phoenix-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        replica_regions:
            description:
                - The regions domain is replication to.
            returned: on success
            type: complex
            contains:
                region:
                    description:
                        - A REPLICATION_ENABLED region, e.g. us-ashburn-1.
                          See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
                          for the full list of supported region names.
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                url:
                    description:
                        - Region agnostic domain URL.
                    returned: on success
                    type: str
                    sample: url_example
                state:
                    description:
                        - The IDCS replicated region state
                    returned: on success
                    type: str
                    sample: ENABLING_REPLICATION
        type:
            description:
                - The type of the domain.
            returned: on success
            type: str
            sample: DEFAULT
        license_type:
            description:
                - The License type of Domain
            returned: on success
            type: str
            sample: license_type_example
        is_hidden_on_login:
            description:
                - Indicates whether domain is hidden on login screen or not.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - Date and time the domain was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Any additional details about the current state of the Domain.
            returned: on success
            type: str
            sample: DEACTIVATING
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
        "display_name": "display_name_example",
        "description": "description_example",
        "url": "url_example",
        "home_region_url": "home_region_url_example",
        "home_region": "us-phoenix-1",
        "replica_regions": [{
            "region": "us-phoenix-1",
            "url": "url_example",
            "state": "ENABLING_REPLICATION"
        }],
        "type": "DEFAULT",
        "license_type": "license_type_example",
        "is_hidden_on_login": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "DEACTIVATING",
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient
    from oci.identity.models import ChangeDomainCompartmentDetails
    from oci.identity.models import ChangeDomainLicenseTypeDetails
    from oci.identity.models import EnableReplicationToRegionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DomainActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        change_compartment
        change_domain_license_type
        deactivate
        enable_replication_to_region
    """

    @staticmethod
    def get_module_resource_id_param():
        return "domain_id"

    def get_module_resource_id(self):
        return self.module.params.get("domain_id")

    def get_get_fn(self):
        return self.client.get_domain

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_domain, domain_id=self.module.params.get("domain_id"),
        )

    def activate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_domain,
            call_fn_args=(),
            call_fn_kwargs=dict(domain_id=self.module.params.get("domain_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDomainCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_domain_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                domain_id=self.module.params.get("domain_id"),
                change_domain_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_domain_license_type(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDomainLicenseTypeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_domain_license_type,
            call_fn_args=(),
            call_fn_kwargs=dict(
                domain_id=self.module.params.get("domain_id"),
                change_domain_license_type_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def deactivate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deactivate_domain,
            call_fn_args=(),
            call_fn_kwargs=dict(domain_id=self.module.params.get("domain_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable_replication_to_region(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableReplicationToRegionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_replication_to_region,
            call_fn_args=(),
            call_fn_kwargs=dict(
                domain_id=self.module.params.get("domain_id"),
                enable_replication_to_region_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DomainActionsHelperCustom = get_custom_class("DomainActionsHelperCustom")


class ResourceHelper(DomainActionsHelperCustom, DomainActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            license_type=dict(type="str"),
            domain_id=dict(aliases=["id"], type="str", required=True),
            replica_region=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "activate",
                    "change_compartment",
                    "change_domain_license_type",
                    "deactivate",
                    "enable_replication_to_region",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="domain",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
