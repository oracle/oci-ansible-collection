# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_config_utils

try:
    from oci.apigateway import WorkRequestsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


# The waiter client for this service uses apigateway WorkRequestsClient
class ApigatewayGatewayHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        self.work_request_client = oci_config_utils.create_service_client(
            module, WorkRequestsClient
        )

        super(ApigatewayGatewayHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # override the waiting client with the WorkRequestsClient
    def get_waiter_client(self):
        return self.work_request_client


class ApigatewayDeploymentHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        self.work_request_client = oci_config_utils.create_service_client(
            module, WorkRequestsClient
        )

        super(ApigatewayDeploymentHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    def get_waiter_client(self):
        return self.work_request_client


# The waiter client for this service uses apigateway WorkRequestsClient
class ApigatewayApiHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        self.work_request_client = oci_config_utils.create_service_client(
            module, WorkRequestsClient
        )

        super(ApigatewayApiHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # override the waiting client with the WorkRequestsClient
    def get_waiter_client(self):
        return self.work_request_client

    def get_exclude_attributes(self):
        return super(ApigatewayApiHelperCustom, self).get_exclude_attributes() + [
            "content",
        ]

    # remove the content parameter for the idempotence check
    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            ApigatewayApiHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        update_model_dict.pop("content", None)
        return update_model_dict


# The waiter client for this service uses apigateway WorkRequestsClient
class ApigatewayWaasCertificateHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        self.work_request_client = oci_config_utils.create_service_client(
            module, WorkRequestsClient
        )

        super(ApigatewayWaasCertificateHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # override the waiting client with the WorkRequestsClient
    def get_waiter_client(self):
        return self.work_request_client

    def get_exclude_attributes(self):
        excluded_attributes = super(
            ApigatewayWaasCertificateHelperCustom, self
        ).get_exclude_attributes()
        if self.namespace == "apigateway":
            return excluded_attributes + [
                "private_key",
            ]
        return excluded_attributes

    def get_entity_type(self):
        return "certificate"
