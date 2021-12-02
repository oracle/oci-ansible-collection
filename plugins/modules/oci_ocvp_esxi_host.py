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
module: oci_ocvp_esxi_host
short_description: Manage an EsxiHost resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an EsxiHost resource in Oracle Cloud Infrastructure
    - For I(state=present), adds another ESXi host to an existing SDDC. The attributes of the specified
      `Sddc` determine the VMware software and other configuration settings used
      by the ESXi host.
    - Use the L(WorkRequest,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/WorkRequest/) operations to track the
      creation of the ESXi host.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    sddc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SDDC to add the
              ESXi host to.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - "A descriptive name for the ESXi host. It's changeable.
              Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating
              hyphens, Must be unique within the SDDC."
            - If this attribute is not specified, the SDDC's `instanceDisplayNamePrefix` attribute is used
              to name and incrementally number the ESXi host. For example, if you're creating the fourth
              ESXi host in the SDDC, and `instanceDisplayNamePrefix` is `MySDDC`, the host's display
              name is `MySDDC-4`.
            - Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    current_sku:
        description:
            - The billing option currently used by the ESXi host.
              L(ListSupportedSkus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus).
        type: str
        choices:
            - "HOUR"
            - "MONTH"
            - "ONE_YEAR"
            - "THREE_YEARS"
    next_sku:
        description:
            - The billing option to switch to after the existing billing cycle ends.
              If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
              L(ListSupportedSkus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus).
            - This parameter is updatable.
        type: str
        choices:
            - "HOUR"
            - "MONTH"
            - "ONE_YEAR"
            - "THREE_YEARS"
    compute_availability_domain:
        description:
            - The availability domain to create the ESXi host in.
              If keep empty, for AD-specific SDDC, new ESXi host will be created in the same availability domain;
              for multi-AD SDDC, new ESXi host will be auto assigned to the next availability domain following evenly distribution strategy.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    esxi_host_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the EsxiHost.
            - Use I(state=present) to create or update an EsxiHost.
            - Use I(state=absent) to delete an EsxiHost.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create esxi_host
  oci_ocvp_esxi_host:
    # required
    sddc_id: "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    current_sku: HOUR
    next_sku: HOUR
    compute_availability_domain: compute_availability_domain_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update esxi_host
  oci_ocvp_esxi_host:
    # required
    esxi_host_id: "ocid1.esxihost.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    next_sku: HOUR
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update esxi_host using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ocvp_esxi_host:
    # required
    display_name: display_name_example

    # optional
    next_sku: HOUR
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete esxi_host
  oci_ocvp_esxi_host:
    # required
    esxi_host_id: "ocid1.esxihost.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete esxi_host using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_ocvp_esxi_host:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
esxi_host:
    description:
        - Details of the EsxiHost resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the ESXi host.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A descriptive name for the ESXi host. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        sddc_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SDDC that the
                  ESXi host belongs to.
            returned: on success
            type: str
            sample: "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that
                  contains the SDDC.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        compute_instance_id:
            description:
                - In terms of implementation, an ESXi host is a Compute instance that
                  is configured with the chosen bundle of VMware software. The `computeInstanceId`
                  is the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of that Compute instance.
            returned: on success
            type: str
            sample: "ocid1.computeinstance.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the ESXi host was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        time_updated:
            description:
                - The date and time the ESXi host was updated, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the ESXi host.
            returned: on success
            type: str
            sample: CREATING
        current_sku:
            description:
                - The billing option currently used by the ESXi host.
                  L(ListSupportedSkus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus).
            returned: on success
            type: str
            sample: HOUR
        next_sku:
            description:
                - The billing option to switch to after the current billing cycle ends.
                  If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
                  L(ListSupportedSkus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus).
            returned: on success
            type: str
            sample: HOUR
        billing_contract_end_date:
            description:
                - "Current billing cycle end date. If the value in `currentSku` and `nextSku` are different, the value specified in `nextSku`
                  becomes the new `currentSKU` when the `contractEndDate` is reached.
                  Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        compute_availability_domain:
            description:
                - The availability domain of the ESXi host.
            returned: on success
            type: str
            sample: compute_availability_domain_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "sddc_id": "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_instance_id": "ocid1.computeinstance.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "current_sku": "HOUR",
        "next_sku": "HOUR",
        "billing_contract_end_date": "2016-08-25T21:10:29.600Z",
        "compute_availability_domain": "compute_availability_domain_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.ocvp import WorkRequestClient
    from oci.ocvp import EsxiHostClient
    from oci.ocvp.models import CreateEsxiHostDetails
    from oci.ocvp.models import UpdateEsxiHostDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EsxiHostHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_module_resource_id_param(self):
        return "esxi_host_id"

    def get_module_resource_id(self):
        return self.module.params.get("esxi_host_id")

    def get_get_fn(self):
        return self.client.get_esxi_host

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_esxi_host,
            esxi_host_id=self.module.params.get("esxi_host_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["sddc_id", "display_name"]

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
            self.client.list_esxi_hosts, **kwargs
        )

    def get_create_model_class(self):
        return CreateEsxiHostDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_esxi_host,
            call_fn_args=(),
            call_fn_kwargs=dict(create_esxi_host_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateEsxiHostDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_esxi_host,
            call_fn_args=(),
            call_fn_kwargs=dict(
                esxi_host_id=self.module.params.get("esxi_host_id"),
                update_esxi_host_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_esxi_host,
            call_fn_args=(),
            call_fn_kwargs=dict(esxi_host_id=self.module.params.get("esxi_host_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


EsxiHostHelperCustom = get_custom_class("EsxiHostHelperCustom")


class ResourceHelper(EsxiHostHelperCustom, EsxiHostHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            sddc_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            current_sku=dict(
                type="str", choices=["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
            ),
            next_sku=dict(
                type="str", choices=["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
            ),
            compute_availability_domain=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            esxi_host_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="esxi_host",
        service_client_class=EsxiHostClient,
        namespace="ocvp",
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
