# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from abc import abstractmethod

try:
    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OciAnsibleError:
    @abstractmethod
    def format_error(self, **kwargs):
        pass


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
        ] = "refer to this link https://docs.oracle.com/en-us/iaas/tools/oci-ansible-collection/latest/guides/troubleshooting-guide.html"
        return kwargs


class OciAnsibleErrorFactory:
    ERROR_DICT = {
        Exception: OciAnsibleBaseException,
    }

    @staticmethod
    def get_object(error):
        if OciAnsibleErrorFactory.ERROR_DICT.get(error):
            return (OciAnsibleErrorFactory.ERROR_DICT.get(error))()
        else:
            return (OciAnsibleErrorFactory.ERROR_DICT.get(Exception))()
