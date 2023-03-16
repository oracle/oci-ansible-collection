# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from abc import abstractmethod

try:
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OciAnsibleError:
    @abstractmethod
    def format_error(self, **kwargs):
        pass


class OciAnsibleServiceError(OciAnsibleError):

    # overriding fail_json method
    def format_error(self, **kwargs):
        # traceback can be customised by setting kwargs['exception']
        error = kwargs.pop("error", None)
        if error is None:
            raise ValueError
        try:
            msg = kwargs.pop("msg")
        except KeyError:
            msg = ""

        msg += str(error.message or "")
        kwargs["msg"] = msg
        resource_helper = kwargs.pop("resource_helper", None)
        operation_name = str(error.operation_name)
        module_name = ""
        if resource_helper is not None:
            if operation_name.startswith("get") or operation_name.startswith("list"):
                module_suffix = "_facts"
            elif (
                operation_name.startswith("create")
                or operation_name.startswith("update")
                or operation_name.startswith("patch")
                or operation_name.startswith("delete")
                or operation_name.startswith("update_using_name")
                or operation_name.startswith("patch_using_name")
                or operation_name.startswith("delete_using_name")
            ):
                module_suffix = ""
            else:
                module_suffix = "_actions"

            module_name = (
                "oci_"
                + str(resource_helper.namespace)
                + "_"
                + str(resource_helper.resource_type)
                + module_suffix
                + "_module.html"
            )
        kwargs["http_response_status"] = str(error.status)
        kwargs["error_code"] = str(error.code)
        kwargs["service_name"] = str(error.target_service)
        kwargs["operation_name"] = str(error.operation_name)
        kwargs["opc_request_id"] = str(error.request_id)
        kwargs["request_endpoint"] = str(error.request_endpoint)
        kwargs["time"] = str(error.timestamp)
        # we can debate if need #examples in the end of module documentation link
        module_documentation = (
            "Refer to this link https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/collections/oracle/oci/"
            + module_name
        )
        kwargs["module_documentation"] = module_documentation
        kwargs[
            "troubleshooting_tips"
        ] = "Refer to troubleshooting guide https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/guides/troubleshooting-guide.html"
        return kwargs


class OciAnsibleBaseException(OciAnsibleError):
    def format_error(self, **kwargs):
        error = kwargs.pop("error", None)
        kwargs.pop("resource_helper", None)
        try:
            msg = kwargs.pop("msg")
        except KeyError:
            msg = ""
        msg += str(error or "")
        kwargs["msg"] = msg
        kwargs[
            "troubleshooting_tips"
        ] = "Refer to troubleshooting guide https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/guides/troubleshooting-guide.html"
        return kwargs


class OciAnsibleErrorFactory:
    def __init__(self):
        self.ERROR_DICT = {
            Exception: OciAnsibleBaseException,
        }
        if HAS_OCI_PY_SDK:
            self.ERROR_DICT[ServiceError] = OciAnsibleServiceError

    def get_object(self, error):
        if self.ERROR_DICT.get(error):
            return (self.ERROR_DICT.get(error))()
        else:
            return (self.ERROR_DICT.get(Exception))()
