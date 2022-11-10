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
    - For I(action=activate), (For tenancies that support identity domains) Activates a deactivated identity domain. You can only activate identity domains that
      your user account is not a part of.
      After you send the request, the `lifecycleDetails` of the identity domain is set to ACTIVATING. When the operation completes, the
      `lifecycleDetails` is set to null and the `lifecycleState` of the identity domain is set to ACTIVE.
      To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves
      the operation's status.
    - For I(action=change_compartment), (For tenancies that support identity domains) Moves the identity domain to a different compartment in the tenancy.
      To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves
      the operation's status.
    - For I(action=change_domain_license_type), (For tenancies that support identity domains) Changes the license type of the given identity domain. The
      identity domain's
      `lifecycleState` must be set to ACTIVE and the requested `licenseType` must be allowed. To retrieve the allowed `licenseType` for
      the identity domain, use L(ListAllowedDomainLicenseTypes,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/20160918/Domain/ListAllowedDomainLicenseTypes).
      After you send your request, the `lifecycleDetails` of this identity domain is set to UPDATING. When the update of the identity
      domain completes, then the `lifecycleDetails` is set to null.
      To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves
      the operation's status.
    - For I(action=deactivate), (For tenancies that support identity domains) Deactivates the specified identity domain. Identity domains must be in an ACTIVE
      `lifecycleState` and have no active apps present in the domain or underlying Identity Cloud Service stripe. You cannot deactivate
      the default identity domain.
      After you send your request, the `lifecycleDetails` of this identity domain is set to DEACTIVATING. When the operation completes,
      then the `lifecycleDetails` is set to null and the `lifecycleState` is set to INACTIVE.
      To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves
      the operation's status.
    - For I(action=enable_replication_to_region), (For tenancies that support identity domains) Replicates the identity domain to a new region (provided that
      the region is the
      tenancy home region or other region that the tenancy subscribes to). You can only replicate identity domains that are in an ACTIVE
      `lifecycleState` and not currently updating or already replicating. You also can only trigger the replication of secondary identity domains.
      The default identity domain is automatically replicated to all regions that the tenancy subscribes to.
      After you send the request, the `state` of the identity domain in the replica region is set to ENABLING_REPLICATION. When the operation
      completes, the `state` is set to REPLICATION_ENABLED.
      To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves
      the operation's status.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the destination compartment
              into which to move the identity domain.
            - Required for I(action=change_compartment).
        type: str
    license_type:
        description:
            - The license type of the identity domain.
            - Applicable only for I(action=change_domain_license_type).
        type: str
    domain_id:
        description:
            - The OCID of the identity domain.
        type: str
        aliases: ["id"]
        required: true
    replica_region:
        description:
            - A region to which you want identity domain replication to occur.
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
                - The OCID of the identity domain.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the identity domain.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The mutable display name of the identity domain.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The identity domain description. You can have an empty description.
            returned: on success
            type: str
            sample: description_example
        url:
            description:
                - Region-agnostic identity domain URL.
            returned: on success
            type: str
            sample: url_example
        home_region_url:
            description:
                - Region-specific identity domain URL.
            returned: on success
            type: str
            sample: home_region_url_example
        home_region:
            description:
                - The home region for the identity domain.
                  See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
                  for the full list of supported region names.
                - "Example: `us-phoenix-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        replica_regions:
            description:
                - The regions where replicas of the identity domain exist.
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
                        - Region-agnostic identity domain URL.
                    returned: on success
                    type: str
                    sample: url_example
                state:
                    description:
                        - The IDCS-replicated region state.
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
                - The license type of the identity domain.
            returned: on success
            type: str
            sample: license_type_example
        is_hidden_on_login:
            description:
                - Indicates whether the identity domain is hidden on the sign-in screen or not.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - Date and time the identity domain was created, in the format defined by RFC3339.
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
                - Any additional details about the current state of the identity domain.
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

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
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

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
