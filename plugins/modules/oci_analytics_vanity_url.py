#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_analytics_vanity_url
short_description: Manage a VanityUrl resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VanityUrl resource in Oracle Cloud Infrastructure
    - For I(state=present), allows specifying a custom host name to be used to access the analytics instance.  This requires prior setup of DNS entry and
      certificate
      for this host.
version_added: "2.9"
author: Oracle (@oracle)
options:
    analytics_instance_id:
        description:
            - The OCID of the AnalyticsInstance.
        type: str
        required: true
    description:
        description:
            - Optional description.
        type: str
    hosts:
        description:
            - List of fully qualified hostnames supported by this vanity URL definition (max of 3).
            - Required for create using I(state=present).
        type: list
    passphrase:
        description:
            - Passphrase for the PEM Private key (if any).
            - This parameter is updatable.
        type: str
    private_key:
        description:
            - PEM Private key for HTTPS connections.
            - Required for create using I(state=present), update using I(state=present) with vanity_url_key present.
        type: str
    public_certificate:
        description:
            - PEM certificate for HTTPS connections.
            - Required for create using I(state=present), update using I(state=present) with vanity_url_key present.
        type: str
    ca_certificate:
        description:
            - PEM CA certificate(s) for HTTPS connections. This may include multiple PEM certificates.
            - Required for create using I(state=present), update using I(state=present) with vanity_url_key present.
        type: str
    vanity_url_key:
        description:
            - Specify unique identifier key of a vanity url to update or delete.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
    state:
        description:
            - The state of the VanityUrl.
            - Use I(state=present) to create or update a VanityUrl.
            - Use I(state=absent) to delete a VanityUrl.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vanity_url
  oci_analytics_vanity_url:
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    private_key: private_key_example
    public_certificate: public_certificate_example
    ca_certificate: ca_certificate_example

- name: Update vanity_url
  oci_analytics_vanity_url:
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    passphrase: passphrase_example
    private_key: private_key_example
    public_certificate: public_certificate_example
    ca_certificate: ca_certificate_example
    vanity_url_key: vanity_url_key_example

- name: Delete vanity_url
  oci_analytics_vanity_url:
    analytics_instance_id: "ocid1.analyticsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    vanity_url_key: vanity_url_key_example
    state: absent

"""

RETURN = """
vanity_url:
    description:
        - Details of the VanityUrl resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The vanity url unique identifier key.
            returned: on success
            type: string
            sample: key_example
        description:
            description:
                - Description of the vanity url.
            returned: on success
            type: string
            sample: description_example
        urls:
            description:
                - List of urls supported by this vanity URL definition (max of 3).
            returned: on success
            type: list
            sample: []
        hosts:
            description:
                - List of fully qualified hostnames supported by this vanity URL definition (max of 3).
            returned: on success
            type: list
            sample: []
        public_certificate:
            description:
                - PEM certificate for HTTPS connections.
            returned: on success
            type: string
            sample: public_certificate_example
    sample: {
        "key": "key_example",
        "description": "description_example",
        "urls": [],
        "hosts": [],
        "public_certificate": "public_certificate_example"
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
    from oci.analytics import AnalyticsClient
    from oci.analytics.models import CreateVanityUrlDetails
    from oci.analytics.models import UpdateVanityUrlDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VanityUrlHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update and delete"""

    def get_module_resource_id_param(self):
        return "vanity_url_key"

    def get_module_resource_id(self):
        return self.module.params.get("vanity_url_key")

    def get_create_model_class(self):
        return CreateVanityUrlDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vanity_url,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                create_vanity_url_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateVanityUrlDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vanity_url,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                vanity_url_key=self.module.params.get("vanity_url_key"),
                update_vanity_url_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_vanity_url,
            call_fn_args=(),
            call_fn_kwargs=dict(
                analytics_instance_id=self.module.params.get("analytics_instance_id"),
                vanity_url_key=self.module.params.get("vanity_url_key"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


VanityUrlHelperCustom = get_custom_class("VanityUrlHelperCustom")


class ResourceHelper(VanityUrlHelperCustom, VanityUrlHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            analytics_instance_id=dict(type="str", required=True),
            description=dict(type="str"),
            hosts=dict(type="list"),
            passphrase=dict(type="str", no_log=True),
            private_key=dict(type="str", no_log=True),
            public_certificate=dict(type="str"),
            ca_certificate=dict(type="str"),
            vanity_url_key=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vanity_url",
        service_client_class=AnalyticsClient,
        namespace="analytics",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
