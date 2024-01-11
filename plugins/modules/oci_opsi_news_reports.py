#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_opsi_news_reports
short_description: Manage a NewsReports resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NewsReports resource in Oracle Cloud Infrastructure
    - For I(state=present), create a news report in Operations Insights. The report will be enabled in Operations Insights. Insights will be emailed as per
      selected frequency.
    - "This resource has the following action operations in the M(oracle.oci.oci_opsi_news_reports_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The news report name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The description of the news report.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - Compartment Identifier where the news report will be created.
            - Required for create using I(state=present).
        type: str
    status:
        description:
            - Defines if the news report will be enabled or disabled.
            - This parameter is updatable.
        type: str
        choices:
            - "DISABLED"
            - "ENABLED"
            - "TERMINATED"
    news_frequency:
        description:
            - News report frequency.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "WEEKLY"
    locale:
        description:
            - Language of the news report.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "EN"
    content_types:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            capacity_planning_resources:
                description:
                    - Supported resources for capacity planning content type.
                type: list
                elements: str
                required: true
    ons_topic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ONS topic.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    news_report_id:
        description:
            - Unique news report identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NewsReports.
            - Use I(state=present) to create or update a NewsReports.
            - Use I(state=absent) to delete a NewsReports.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create news_reports
  oci_opsi_news_reports:
    # required
    name: name_example
    description: description_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    news_frequency: WEEKLY
    locale: EN
    content_types:
      # required
      capacity_planning_resources: [ "capacity_planning_resources_example" ]
    ons_topic_id: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    status: DISABLED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update news_reports
  oci_opsi_news_reports:
    # required
    news_report_id: "ocid1.newsreport.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    status: DISABLED
    news_frequency: WEEKLY
    locale: EN
    content_types:
      # required
      capacity_planning_resources: [ "capacity_planning_resources_example" ]
    ons_topic_id: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update news_reports using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_news_reports:
    # required
    name: name_example

    # optional
    status: DISABLED
    news_frequency: WEEKLY
    locale: EN
    content_types:
      # required
      capacity_planning_resources: [ "capacity_planning_resources_example" ]
    ons_topic_id: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete news_reports
  oci_opsi_news_reports:
    # required
    news_report_id: "ocid1.newsreport.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete news_reports using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_news_reports:
    # required
    name: name_example
    state: absent

"""

RETURN = """
news_reports:
    description:
        - Details of the NewsReports resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        news_frequency:
            description:
                - News report frequency.
            returned: on success
            type: str
            sample: WEEKLY
        content_types:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                capacity_planning_resources:
                    description:
                        - Supported resources for capacity planning content type.
                    returned: on success
                    type: list
                    sample: []
        locale:
            description:
                - Language of the news report.
            returned: on success
            type: str
            sample: EN
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the news report resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The description of the news report.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The news report name.
            returned: on success
            type: str
            sample: name_example
        ons_topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ONS topic.
            returned: on success
            type: str
            sample: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        status:
            description:
                - Indicates the status of a news report in Operations Insights.
            returned: on success
            type: str
            sample: DISABLED
        time_created:
            description:
                - The time the the news report was first enabled. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the news report was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the news report.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: {
        "news_frequency": "WEEKLY",
        "content_types": {
            "capacity_planning_resources": []
        },
        "locale": "EN",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "ons_topic_id": "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "status": "DISABLED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateNewsReportDetails
    from oci.opsi.models import UpdateNewsReportDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NewsReportsHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(NewsReportsHelperGen, self).get_possible_entity_types() + [
            "newsreports",
            "newsreport",
            "opsinewsreports",
            "opsinewsreport",
            "newsreportsresource",
            "newsreportresource",
            "opsi",
        ]

    def get_module_resource_id_param(self):
        return "news_report_id"

    def get_module_resource_id(self):
        return self.module.params.get("news_report_id")

    def get_get_fn(self):
        return self.client.get_news_report

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_news_report, news_report_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_news_report,
            news_report_id=self.module.params.get("news_report_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "news_report_id"]

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
            self.client.list_news_reports, **kwargs
        )

    def get_create_model_class(self):
        return CreateNewsReportDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_news_report,
            call_fn_args=(),
            call_fn_kwargs=dict(create_news_report_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateNewsReportDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_news_report,
            call_fn_args=(),
            call_fn_kwargs=dict(
                news_report_id=self.module.params.get("news_report_id"),
                update_news_report_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_news_report,
            call_fn_args=(),
            call_fn_kwargs=dict(
                news_report_id=self.module.params.get("news_report_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NewsReportsHelperCustom = get_custom_class("NewsReportsHelperCustom")


class ResourceHelper(NewsReportsHelperCustom, NewsReportsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            status=dict(type="str", choices=["DISABLED", "ENABLED", "TERMINATED"]),
            news_frequency=dict(type="str", choices=["WEEKLY"]),
            locale=dict(type="str", choices=["EN"]),
            content_types=dict(
                type="dict",
                options=dict(
                    capacity_planning_resources=dict(
                        type="list", elements="str", required=True
                    )
                ),
            ),
            ons_topic_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            news_report_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="news_reports",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
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
