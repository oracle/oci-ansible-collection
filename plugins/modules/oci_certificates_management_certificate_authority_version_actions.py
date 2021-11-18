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
module: oci_certificates_management_certificate_authority_version_actions
short_description: Perform actions on a CertificateAuthorityVersion resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CertificateAuthorityVersion resource in Oracle Cloud Infrastructure
    - For I(action=cancel_certificate_authority_version_deletion), cancels the scheduled deletion of the specified certificate authority (CA) version. Canceling
      a scheduled deletion restores the CA version's lifecycle state to what
      it was before its scheduled deletion.
    - For I(action=schedule_certificate_authority_version_deletion), schedules the deletion of the specified certificate authority (CA) version.
      This sets the lifecycle state of the CA version to `PENDING_DELETION`
      and then deletes it after the specified retention period ends. If needed, you can determine the status of the deletion by using
      `GetCertificateAuthorityVersion`.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    certificate_authority_id:
        description:
            - The OCID of the certificate authority (CA).
        type: str
        required: true
    certificate_authority_version_number:
        description:
            - The version number of the certificate authority (CA).
        type: int
        required: true
    time_of_deletion:
        description:
            - "An optional property indicating when to delete the CA version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
              Example: `2019-04-03T21:10:29.600Z`"
            - Applicable only for I(action=schedule_certificate_authority_version_deletion).
        type: str
    action:
        description:
            - The action to perform on the CertificateAuthorityVersion.
        type: str
        required: true
        choices:
            - "cancel_certificate_authority_version_deletion"
            - "schedule_certificate_authority_version_deletion"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action cancel_certificate_authority_version_deletion on certificate_authority_version
  oci_certificates_management_certificate_authority_version_actions:
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_authority_version_number: 789
    action: cancel_certificate_authority_version_deletion

- name: Perform action schedule_certificate_authority_version_deletion on certificate_authority_version
  oci_certificates_management_certificate_authority_version_actions:
    time_of_deletion: "2021-05-06T00:00:00.000Z"
    certificate_authority_id: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
    certificate_authority_version_number: "789"
    action: "schedule_certificate_authority_version_deletion"

"""

RETURN = """
certificate_authority_version:
    description:
        - Details of the CertificateAuthorityVersion resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        certificate_authority_id:
            description:
                - The OCID of the CA.
            returned: on success
            type: str
            sample: "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx"
        serial_number:
            description:
                - "A unique certificate identifier used in certificate revocation tracking, formatted as octets.
                  Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`"
            returned: on success
            type: str
            sample: 03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF
        time_created:
            description:
                - "A optional property indicating when the CA version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2019-04-03T21:10:29.600Z"
        version_number:
            description:
                - The version number of this CA.
            returned: on success
            type: int
            sample: 56
        issuer_ca_version_number:
            description:
                - The version number of the issuing CA.
            returned: on success
            type: int
            sample: 56
        version_name:
            description:
                - The name of the CA version. When the value is not null, a name is unique across versions for a given CA.
            returned: on success
            type: str
            sample: version_name_example
        subject_alternative_names:
            description:
                - A list of subject alternative names. A subject alternative name specifies the domain names, including subdomains, and IP addresses covered by
                  the certificates issued by this CA.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The subject alternative name type. Currently only DNS domain or host names and IP addresses are supported.
                    returned: on success
                    type: str
                    sample: DNS
                value:
                    description:
                        - The subject alternative name.
                    returned: on success
                    type: str
                    sample: value_example
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the CA version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2019-04-03T21:10:29.600Z"
        validity:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_of_validity_not_before:
                    description:
                        - "The date on which the certificate validity period begins, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                          format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2019-04-03T21:10:29.600Z"
                time_of_validity_not_after:
                    description:
                        - "The date on which the certificate validity period ends, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                          format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2019-04-03T21:10:29.600Z"
        stages:
            description:
                - A list of rotation states for this CA version.
            returned: on success
            type: list
            sample: []
        revocation_status:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_of_revocation:
                    description:
                        - "The time when the entity was revoked, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                          Example: `2019-04-03T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2019-04-03T21:10:29.600Z"
                revocation_reason:
                    description:
                        - The reason the certificate or certificate authority (CA) was revoked.
                    returned: on success
                    type: str
                    sample: UNSPECIFIED
    sample: {
        "certificate_authority_id": "ocid1.certificateauthority.oc1..xxxxxxEXAMPLExxxxxx",
        "serial_number": "03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF",
        "time_created": "2019-04-03T21:10:29.600Z",
        "version_number": 56,
        "issuer_ca_version_number": 56,
        "version_name": "version_name_example",
        "subject_alternative_names": [{
            "type": "DNS",
            "value": "value_example"
        }],
        "time_of_deletion": "2019-04-03T21:10:29.600Z",
        "validity": {
            "time_of_validity_not_before": "2019-04-03T21:10:29.600Z",
            "time_of_validity_not_after": "2019-04-03T21:10:29.600Z"
        },
        "stages": [],
        "revocation_status": {
            "time_of_revocation": "2019-04-03T21:10:29.600Z",
            "revocation_reason": "UNSPECIFIED"
        }
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
    from oci.certificates_management import CertificatesManagementClient
    from oci.certificates_management.models import (
        ScheduleCertificateAuthorityVersionDeletionDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CertificateAuthorityVersionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_certificate_authority_version_deletion
        schedule_certificate_authority_version_deletion
    """

    @staticmethod
    def get_module_resource_id_param():
        return "certificate_authority_version_number"

    def get_module_resource_id(self):
        return self.module.params.get("certificate_authority_version_number")

    def get_get_fn(self):
        return self.client.get_certificate_authority_version

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_certificate_authority_version,
            certificate_authority_id=self.module.params.get("certificate_authority_id"),
            certificate_authority_version_number=self.module.params.get(
                "certificate_authority_version_number"
            ),
        )

    def cancel_certificate_authority_version_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_certificate_authority_version_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_authority_id=self.module.params.get(
                    "certificate_authority_id"
                ),
                certificate_authority_version_number=self.module.params.get(
                    "certificate_authority_version_number"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def schedule_certificate_authority_version_deletion(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScheduleCertificateAuthorityVersionDeletionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_certificate_authority_version_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                certificate_authority_id=self.module.params.get(
                    "certificate_authority_id"
                ),
                certificate_authority_version_number=self.module.params.get(
                    "certificate_authority_version_number"
                ),
                schedule_certificate_authority_version_deletion_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


CertificateAuthorityVersionActionsHelperCustom = get_custom_class(
    "CertificateAuthorityVersionActionsHelperCustom"
)


class ResourceHelper(
    CertificateAuthorityVersionActionsHelperCustom,
    CertificateAuthorityVersionActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            certificate_authority_id=dict(type="str", required=True),
            certificate_authority_version_number=dict(type="int", required=True),
            time_of_deletion=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_certificate_authority_version_deletion",
                    "schedule_certificate_authority_version_deletion",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="certificate_authority_version",
        service_client_class=CertificatesManagementClient,
        namespace="certificates_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
